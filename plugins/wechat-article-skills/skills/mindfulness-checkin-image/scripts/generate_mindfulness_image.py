#!/usr/bin/env python3
"""Generate 3:4 mindfulness check-in quote images via APiYi GPT Image 2."""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image


DEFAULT_BASE_URL = "https://api.apiyi.com/v1"
DEFAULT_MODEL = "gpt-image-2"
DEFAULT_GENERATION_SIZE = "1440x1920"
DEFAULT_FINAL_SIZE = "1080x1440"
DEFAULT_OUTPUT_DIR = str(Path.home() / "Desktop" / "正念打卡" / "generated")

PALETTES = {
    "yellow": "pale lemon edges, a deeper warm yellow glow in the center, creamy highlights",
    "green": "pale mint edges, a luminous lime-green center, soft yellow undertones",
    "orange": "warm yellow top, creamy right side, soft orange glow from the lower-left corner",
}


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
    request = urllib.request.Request(url, headers={"User-Agent": "mindfulness-checkin-image-skill/1.0"})
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


def slugify(text):
    cleaned = re.sub(r"\s+", "-", text.strip().lower())
    cleaned = re.sub(r"[^a-z0-9\u4e00-\u9fff-]+", "", cleaned)
    cleaned = cleaned.strip("-")
    return cleaned[:36] or "mindfulness"


def choose_palette(text, requested):
    if requested != "auto":
        return requested
    if re.search(r"当下|生命|时刻|呼吸|存在|看见|觉察", text):
        return "green"
    if re.search(r"勇敢|能量|力量|开始|行动|太阳|热爱", text):
        return "orange"
    return "yellow"


def build_prompt(args):
    palette_name = choose_palette(args.text, args.palette)
    palette = PALETTES[palette_name]
    subtitle_block = ""
    if args.translation:
        subtitle_block = f'\nSmall subtitle, render exactly:\n"{args.translation}"\n'

    return f"""Create a vertical 3:4 mindfulness affirmation poster, {args.size}.

Main text, render exactly in Chinese:
"{args.text}"
{subtitle_block}
Visual style: soft abstract luminous gradient background, calm poster for a daily mindfulness check-in, {palette}, gentle radial glow, subtle paper grain, lots of clean negative space. Center the text block slightly above the optical center. Use elegant high-contrast black Chinese typography, large and readable, with generous line spacing. If a subtitle is provided, set it below the Chinese text in smaller elegant serif or clean sans typography.

Composition: minimal, editorial, peaceful, generous margins, no characters, no objects unless they are extremely subtle abstract light fields.

Strictly avoid: any watermark, logo, Xiaohongshu mark, app badge, QR code, signature, account ID, handle, copyright line, bottom-right text, platform UI, sticker, frame, border, extra captions, misspelled text, clutter, photorealistic scene, stock imagery."""


def build_payload(args, prompt):
    payload = {
        "model": args.model,
        "prompt": prompt,
    }

    if args.model in {"gpt-image-2", "gpt-image-2-vip"}:
        payload["size"] = args.size

    if args.model == "gpt-image-2":
        payload["quality"] = args.quality
        payload["output_format"] = "jpeg"
        payload["output_compression"] = args.output_compression

    return payload


def main():
    parser = argparse.ArgumentParser(description="Generate a 3:4 mindfulness check-in image through APiYi GPT Image 2.")
    parser.add_argument("--text", required=True, help="Exact main sentence to render on the card.")
    parser.add_argument("--translation", default="", help="Optional small English subtitle.")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Directory for generated files.")
    parser.add_argument("--basename", default=None, help="Base filename without extension.")
    parser.add_argument("--palette", default="auto", choices=["auto", "yellow", "green", "orange"])
    parser.add_argument("--model", default=os.environ.get("MINDFULNESS_IMAGE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--base-url", default=os.environ.get("APIYI_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--size", default=DEFAULT_GENERATION_SIZE, help="Generation size for models that accept size.")
    parser.add_argument("--quality", default="high", choices=["auto", "low", "medium", "high"])
    parser.add_argument("--final-size", default=DEFAULT_FINAL_SIZE, type=parse_size)
    parser.add_argument("--output-compression", default=92, type=int)
    parser.add_argument("--timeout", default=600, type=int)
    parser.add_argument("--dry-run", action="store_true", help="Print request payload without calling the API.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    basename = args.basename or f"mindfulness-{timestamp}-{slugify(args.text)}"
    prompt = build_prompt(args)
    payload = build_payload(args, prompt)
    request_preview = {
        "url": f"{args.base_url.rstrip('/')}/images/generations",
        "payload": payload,
        "final_size": f"{args.final_size[0]}x{args.final_size[1]}",
    }

    if args.dry_run:
        print(json.dumps(request_preview, ensure_ascii=False, indent=2))
        return

    response = post_json(request_preview["url"], payload, get_api_key(), args.timeout)
    raw_bytes = image_bytes_from_response(response, args.timeout)

    raw_image = Image.open(BytesIO(raw_bytes))
    raw_ext = "jpg" if raw_image.format == "JPEG" else (raw_image.format or "png").lower()
    if raw_ext == "jpeg":
        raw_ext = "jpg"

    raw_path = output_dir / f"{basename}-raw.{raw_ext}"
    raw_path.write_bytes(raw_bytes)

    final_image = cover_resize(raw_image, args.final_size)
    final_path = output_dir / f"{basename}-{args.final_size[0]}x{args.final_size[1]}.jpg"
    final_image.save(final_path, format="JPEG", quality=94, optimize=True)

    print(json.dumps({
        "raw": str(raw_path),
        "final": str(final_path),
        "model": args.model,
        "generation_size": args.size if args.model in {"gpt-image-2", "gpt-image-2-vip"} else "prompt-controlled",
        "final_size": f"{args.final_size[0]}x{args.final_size[1]}",
        "palette": choose_palette(args.text, args.palette),
        "prompt": prompt,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
