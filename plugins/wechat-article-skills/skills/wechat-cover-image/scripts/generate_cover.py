#!/usr/bin/env python3
"""Generate WeChat public-account cover images via APiYi GPT Image 2."""

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image


DEFAULT_BASE_URL = "https://api.apiyi.com/v1"
DEFAULT_MODEL = "gpt-image-2"
DEFAULT_GENERATION_SIZE = "1808x768"
DEFAULT_MAIN_SIZE = "900x383"
DEFAULT_SQUARE_SIZE = "500x500"


def parse_size(raw):
    try:
        width, height = raw.lower().split("x", 1)
        return int(width), int(height)
    except Exception as exc:
        raise argparse.ArgumentTypeError(f"Invalid size '{raw}', expected WIDTHxHEIGHT") from exc


def get_api_key():
    key = os.environ.get("APIYI_API_KEY") or os.environ.get("YI_API_KEY")
    if not key:
        raise SystemExit("Missing API key. Set APIYI_API_KEY or YI_API_KEY.")
    return key


def post_json(url, payload, api_key, timeout):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"APiYi request failed: HTTP {exc.code}\n{detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"APiYi request failed: {exc}") from exc


def download_url(url, timeout):
    request = urllib.request.Request(url, headers={"User-Agent": "wechat-cover-image-skill/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def image_bytes_from_response(response, timeout):
    data = response.get("data") or []
    if not data:
        raise SystemExit(f"APiYi response did not include image data:\n{json.dumps(response, ensure_ascii=False)[:1000]}")

    item = data[0]
    b64 = item.get("b64_json")
    if b64:
        if b64.startswith("data:"):
            b64 = b64.split(",", 1)[1]
        return base64.b64decode(b64)

    url = item.get("url")
    if url:
        return download_url(url, timeout)

    raise SystemExit(f"Unsupported image response shape:\n{json.dumps(item, ensure_ascii=False)[:1000]}")


def cover_resize(image, target_size):
    target_w, target_h = target_size
    image = image.convert("RGB")
    src_w, src_h = image.size
    scale = max(target_w / src_w, target_h / src_h)
    resized = image.resize((round(src_w * scale), round(src_h * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def build_payload(args):
    payload = {
        "model": args.model,
        "prompt": args.prompt,
    }

    if args.model in {"gpt-image-2", "gpt-image-2-vip"}:
        payload["size"] = args.size

    if args.model == "gpt-image-2":
        payload["quality"] = args.quality
        payload["output_format"] = "jpeg"
        payload["output_compression"] = args.output_compression

    return payload


def main():
    parser = argparse.ArgumentParser(description="Generate a WeChat cover image through APiYi GPT Image 2.")
    parser.add_argument("--prompt", required=True, help="Final image-generation prompt.")
    parser.add_argument("--output-dir", default=".", help="Directory for generated files.")
    parser.add_argument("--basename", default=None, help="Base filename without extension.")
    parser.add_argument("--model", default=os.environ.get("WECHAT_COVER_MODEL", DEFAULT_MODEL))
    parser.add_argument("--base-url", default=os.environ.get("APIYI_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--size", default=DEFAULT_GENERATION_SIZE, help="Generation size for models that accept size.")
    parser.add_argument("--quality", default="high", choices=["auto", "low", "medium", "high"])
    parser.add_argument("--main-size", default=DEFAULT_MAIN_SIZE, type=parse_size)
    parser.add_argument("--square-size", default=DEFAULT_SQUARE_SIZE, type=parse_size)
    parser.add_argument("--output-compression", default=90, type=int)
    parser.add_argument("--timeout", default=600, type=int)
    parser.add_argument("--dry-run", action="store_true", help="Print request payload without calling the API.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    basename = args.basename or f"wechat-cover-{time.strftime('%Y%m%d-%H%M%S')}"
    payload = build_payload(args)

    if args.dry_run:
        print(json.dumps({"url": f"{args.base_url.rstrip('/')}/images/generations", "payload": payload}, ensure_ascii=False, indent=2))
        return

    response = post_json(f"{args.base_url.rstrip('/')}/images/generations", payload, get_api_key(), args.timeout)
    raw_bytes = image_bytes_from_response(response, args.timeout)

    raw_path = output_dir / f"{basename}-raw"
    raw_image = Image.open(BytesIO(raw_bytes))
    raw_ext = "jpg" if raw_image.format == "JPEG" else (raw_image.format or "png").lower()
    if raw_ext == "jpeg":
        raw_ext = "jpg"
    raw_path = raw_path.with_suffix(f".{raw_ext}")
    raw_path.write_bytes(raw_bytes)

    main_image = cover_resize(raw_image, args.main_size)
    square_image = cover_resize(raw_image, args.square_size)

    main_path = output_dir / f"{basename}-{args.main_size[0]}x{args.main_size[1]}.jpg"
    square_path = output_dir / f"{basename}-{args.square_size[0]}x{args.square_size[1]}.jpg"
    main_image.save(main_path, format="JPEG", quality=92, optimize=True)
    square_image.save(square_path, format="JPEG", quality=92, optimize=True)

    print(json.dumps({
        "raw": str(raw_path),
        "main": str(main_path),
        "square": str(square_path),
        "model": args.model,
        "generation_size": args.size if args.model in {"gpt-image-2", "gpt-image-2-vip"} else "prompt-controlled",
        "main_size": f"{args.main_size[0]}x{args.main_size[1]}",
        "square_size": f"{args.square_size[0]}x{args.square_size[1]}",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
