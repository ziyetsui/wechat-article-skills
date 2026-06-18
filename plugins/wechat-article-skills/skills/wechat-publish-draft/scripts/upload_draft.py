#!/usr/bin/env python3
"""Upload WeChat-ready HTML and a cover image to a WeChat Official Account draft box."""

import argparse
import json
import mimetypes
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent
LEGACY_ROOT = Path("/Users/ziye/Library/Mobile Documents/com~apple~CloudDocs/wiki/30-39 Automation and Agents/31 Agent Workflows/31.11 WeChat Skill")
LEGACY_ENV_FILES = [
    LEGACY_ROOT / "skills/wechat-publisher/.env",
    LEGACY_ROOT / "scripts/.env",
]
TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token"
UPLOAD_IMG_URL = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
ADD_MATERIAL_URL = "https://api.weixin.qq.com/cgi-bin/material/add_material"
DRAFT_ADD_URL = "https://api.weixin.qq.com/cgi-bin/draft/add"


def load_env_files(extra_env=None):
    paths = []
    if extra_env:
        paths.append(Path(extra_env).expanduser())
    paths.extend([
        SCRIPT_DIR / ".env",
        SKILL_DIR / ".env",
        *LEGACY_ENV_FILES,
    ])
    loaded = []
    for path in paths:
        if path.exists():
            load_dotenv(path, override=False)
            loaded.append(str(path))
    return loaded


def request_with_retry(method, url, *, retries=3, timeout=45, **kwargs):
    for attempt in range(retries):
        try:
            response = requests.request(method, url, timeout=timeout, **kwargs)
            return response
        except (requests.Timeout, requests.ConnectionError) as exc:
            if attempt == retries - 1:
                raise RuntimeError(f"Network request failed: {exc}") from exc
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError("Network request failed")


def wechat_hint(data):
    code = data.get("errcode")
    msg = data.get("errmsg", "")
    if code == 40164:
        return "IP whitelist error. Add this machine/server outbound IP in WeChat backend: 设置与开发 -> 基本配置 -> IP白名单."
    if code == 40013:
        return "Invalid AppID. Check WECHAT_APPID."
    if code in {40001, 40125}:
        return "Invalid AppSecret or token credential. Check WECHAT_APPSECRET."
    if code == 48001:
        return "API not authorized for this account. Check Official Account interface permissions."
    if code == 45009:
        return "API call quota exceeded."
    if "invalid credential" in msg:
        return "Access token is invalid or expired; retry after fetching a fresh token."
    return ""


def fail_with_wechat_error(context, data):
    hint = wechat_hint(data)
    message = f"{context} failed: {json.dumps(data, ensure_ascii=False)}"
    if hint:
        message += f"\nHint: {hint}"
    raise RuntimeError(message)


def get_credentials(account):
    suffix = f"_{account.upper()}" if account else ""
    appid = os.getenv(f"WECHAT_APPID{suffix}") or os.getenv("WECHAT_APPID")
    secret = os.getenv(f"WECHAT_APPSECRET{suffix}") or os.getenv("WECHAT_APPSECRET")
    if not appid or not secret:
        label = account or "default"
        raise RuntimeError(f"Missing WECHAT_APPID/WECHAT_APPSECRET for account '{label}'.")
    return appid, secret


def get_access_token(appid, appsecret):
    params = {"grant_type": "client_credential", "appid": appid, "secret": appsecret}
    response = request_with_retry("GET", TOKEN_URL, params=params)
    data = response.json()
    token = data.get("access_token")
    if not token:
        fail_with_wechat_error("Get access_token", data)
    return token


def mime_for(path):
    mime, _ = mimetypes.guess_type(str(path))
    return mime or "application/octet-stream"


def upload_inline_image(token, image_path):
    image_path = Path(image_path)
    with image_path.open("rb") as handle:
        files = {"media": (image_path.name, handle, mime_for(image_path))}
        response = request_with_retry("POST", UPLOAD_IMG_URL, params={"access_token": token}, files=files)
    data = response.json()
    url = data.get("url")
    if not url:
        fail_with_wechat_error(f"Upload inline image {image_path}", data)
    return url


def upload_cover_material(token, image_path):
    image_path = Path(image_path)
    with image_path.open("rb") as handle:
        files = {"media": (image_path.name, handle, mime_for(image_path))}
        response = request_with_retry(
            "POST",
            ADD_MATERIAL_URL,
            params={"access_token": token, "type": "image"},
            files=files,
        )
    data = response.json()
    media_id = data.get("media_id")
    if not media_id:
        fail_with_wechat_error(f"Upload cover material {image_path}", data)
    return media_id


def resolve_image_src(src, html_dir):
    parsed = urlparse(src)
    if parsed.scheme in {"http", "https", "data"}:
        return None
    path = Path(src).expanduser()
    if not path.is_absolute():
        path = html_dir / path
    return path


def process_html_images(html_content, html_dir, token, dry_run=False):
    pattern = re.compile(r'(<img\b[^>]*\bsrc=[\"\'])([^\"\']+)([\"\'][^>]*>)', flags=re.I)
    replacements = {}
    warnings = []

    for _prefix, src, _suffix in pattern.findall(html_content):
        parsed = urlparse(src)
        if parsed.scheme in {"http", "https"}:
            if "mmbiz.qpic.cn" not in parsed.netloc and "qpic.cn" not in parsed.netloc:
                warnings.append(f"Remote non-WeChat image left unchanged: {src}")
            continue
        if parsed.scheme == "data":
            warnings.append("Data URL image left unchanged; WeChat may strip it.")
            continue

        image_path = resolve_image_src(src, html_dir)
        if not image_path or not image_path.exists():
            warnings.append(f"Local image not found: {src}")
            continue
        if src in replacements:
            continue
        replacements[src] = f"DRY_RUN_WECHAT_IMAGE_URL/{image_path.name}" if dry_run else upload_inline_image(token, image_path)

    for src, wechat_url in replacements.items():
        html_content = html_content.replace(src, wechat_url)
    return html_content, replacements, warnings


def create_draft(token, article):
    payload = {"articles": [article]}
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    response = request_with_retry(
        "POST",
        DRAFT_ADD_URL,
        params={"access_token": token},
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    data = response.json()
    media_id = data.get("media_id")
    if not media_id:
        fail_with_wechat_error("Create draft", data)
    return media_id, data


def redacted(value, keep=8):
    if not value:
        return ""
    if len(value) <= keep * 2:
        return f"{value[:3]}...{value[-3:]}"
    return f"{value[:keep]}...{value[-keep:]}"


def build_article(args, content, thumb_media_id):
    article = {
        "title": args.title,
        "content": content,
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 0 if args.no_open_comment else 1,
        "only_fans_can_comment": 1 if args.only_fans_can_comment else 0,
    }
    if args.author:
        article["author"] = args.author
    if args.digest:
        article["digest"] = args.digest
    if args.source_url:
        article["content_source_url"] = args.source_url
    if args.pic_crop_235_1:
        article["pic_crop_235_1"] = args.pic_crop_235_1
    if args.pic_crop_1_1:
        article["pic_crop_1_1"] = args.pic_crop_1_1
    return article


def main():
    parser = argparse.ArgumentParser(description="Upload HTML article to WeChat Official Account draft box.")
    parser.add_argument("--html", required=True, help="WeChat-ready HTML file path.")
    parser.add_argument("--title", required=True, help="Article title.")
    parser.add_argument("--cover", help="Cover image path. Required unless --cover-media-id is set.")
    parser.add_argument("--cover-media-id", help="Existing WeChat media_id for cover image.")
    parser.add_argument("--account", help="Account suffix, e.g. A reads WECHAT_APPID_A and WECHAT_APPSECRET_A.")
    parser.add_argument("--author", default="")
    parser.add_argument("--digest", default="")
    parser.add_argument("--source-url", default="")
    parser.add_argument("--pic-crop-235-1", default="", help="Optional WeChat crop coordinate string for 2.35:1 cover.")
    parser.add_argument("--pic-crop-1-1", default="", help="Optional WeChat crop coordinate string for 1:1 cover.")
    parser.add_argument("--only-fans-can-comment", action="store_true")
    parser.add_argument("--no-open-comment", action="store_true")
    parser.add_argument("--env-file", help="Extra .env file to load first.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print planned payload without calling WeChat.")
    args = parser.parse_args()

    loaded_envs = load_env_files(args.env_file)
    html_path = Path(args.html).expanduser().resolve()
    if not html_path.exists():
        raise SystemExit(f"HTML file not found: {html_path}")

    cover_path = Path(args.cover).expanduser().resolve() if args.cover else None
    if not args.cover_media_id and (not cover_path or not cover_path.exists()):
        raise SystemExit("Cover image not found. Provide --cover or --cover-media-id.")

    appid, appsecret = get_credentials(args.account)
    html_content = html_path.read_text(encoding="utf-8")

    token = "DRY_RUN_ACCESS_TOKEN" if args.dry_run else get_access_token(appid, appsecret)
    processed_html, image_replacements, warnings = process_html_images(html_content, html_path.parent, token, dry_run=args.dry_run)
    thumb_media_id = args.cover_media_id or (
        f"DRY_RUN_COVER_MEDIA_ID/{cover_path.name}" if args.dry_run else upload_cover_material(token, cover_path)
    )
    article = build_article(args, processed_html, thumb_media_id)

    if args.dry_run:
        print(json.dumps({
            "status": "dry-run",
            "account": args.account or "default",
            "loaded_env_files": loaded_envs,
            "appid": redacted(appid, keep=4),
            "html": str(html_path),
            "cover": str(cover_path) if cover_path else None,
            "inline_images": len(image_replacements),
            "warnings": warnings,
            "draft_payload_preview": {
                "articles": [{
                    **{k: v for k, v in article.items() if k != "content"},
                    "content_length": len(article["content"]),
                }]
            },
        }, ensure_ascii=False, indent=2))
        return

    draft_media_id, result = create_draft(token, article)
    print(f"DRAFT_MEDIA_ID:{draft_media_id}")
    print(json.dumps({
        "status": "success",
        "account": args.account or "default",
        "html": str(html_path),
        "cover": str(cover_path) if cover_path else None,
        "cover_media_id": redacted(thumb_media_id),
        "inline_images": len(image_replacements),
        "warnings": warnings,
        "draft_media_id": redacted(draft_media_id),
        "raw_errcode": result.get("errcode", 0),
    }, ensure_ascii=False, indent=2), file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
