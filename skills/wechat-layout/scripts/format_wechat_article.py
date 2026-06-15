#!/usr/bin/env python3
"""Format a Chinese article into WeChat-ready inline HTML."""

import argparse
import html
import re
import sys
import time
from pathlib import Path


P_STYLE = (
    "margin: 0 0 24px; padding: 0; font-size: 17px; line-height: 1.6; "
    "letter-spacing: 0.544px; color: rgba(0,0,0,0.9); text-align: justify;"
)
HR_STYLE = "margin: 0 0 24px; border: 0; border-top: 1px solid rgba(0,0,0,0.1);"
IMG_P_STYLE = "margin: 0 0 24px; text-align: center;"
IMG_STYLE = "max-width: 100%; height: auto; display: block; margin: 0 auto;"


def slugify(value):
    value = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff_-]+", "-", value.strip())
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value[:60] or f"wechat-layout-{time.strftime('%Y%m%d-%H%M%S')}"


def read_input(path):
    if path:
        return Path(path).expanduser().read_text(encoding="utf-8")
    return sys.stdin.read()


def extract_title_and_body(raw):
    text = raw.replace("\r\n", "\n").replace("\r", "\n").strip()
    title = ""

    title_match = re.search(r"^## 推荐主标题\s*\n+(.+?)(?:\n{2,}|$)", text, flags=re.M | re.S)
    if title_match:
        title = title_match.group(1).strip().splitlines()[0].strip()

    body_match = re.search(r"^## 改写正文\s*\n+(.+?)(?=\n## 改写说明|\n## 标题备选|\Z)", text, flags=re.M | re.S)
    if body_match:
        body = body_match.group(1).strip()
    else:
        body = text

    body = re.sub(r"^## 推荐主标题\s*\n+.+?(?=\n## |\Z)", "", body, flags=re.M | re.S).strip()
    body = re.sub(r"^## 标题备选\s*\n+.+?(?=\n## |\Z)", "", body, flags=re.M | re.S).strip()
    body = re.sub(r"^## 改写说明\s*\n+.+$", "", body, flags=re.M | re.S).strip()

    if not title:
        first_line = next((line.strip("# ").strip() for line in body.splitlines() if line.strip()), "")
        if len(first_line) <= 40 and not first_line.endswith(("。", "，", "；")):
            title = first_line
            body = body.replace(first_line, "", 1).strip()

    return title, body


def normalize_blocks(body):
    lines = [line.strip() for line in body.splitlines()]
    blocks = []
    current = []

    for line in lines:
        if not line:
            if current:
                blocks.append("".join(current).strip())
                current = []
            continue
        if line in {"---", "———", "***"}:
            if current:
                blocks.append("".join(current).strip())
                current = []
            blocks.append("---")
            continue
        if line.startswith("#"):
            if current:
                blocks.append("".join(current).strip())
                current = []
            blocks.append(line.lstrip("#").strip())
            continue
        current.append(line)

    if current:
        blocks.append("".join(current).strip())

    return [block for block in blocks if block]


def auto_insert_separators(blocks):
    if "---" in blocks or len(blocks) < 14:
        return blocks

    cues = (
        "第一条", "具身智能", "赛车手", "是时代幸运", "软件人能往哪走",
        "从软件到硬件", "你说我不害怕吗", "无所谓的，真的"
    )
    result = []
    separator_count = 0
    for idx, block in enumerate(blocks):
        should_separate = idx > 3 and separator_count < 4 and any(block.startswith(cue) for cue in cues)
        if should_separate and result and result[-1] != "---":
            result.append("---")
            separator_count += 1
        result.append(block)
    return result


def block_to_html(block):
    if block == "---":
        return f'<hr style="{HR_STYLE}">'
    escaped = html.escape(block, quote=False)
    return f'<p style="{P_STYLE}">{escaped}</p>'


def image_to_html(src):
    escaped_src = html.escape(src, quote=True)
    return f'<p style="{IMG_P_STYLE}"><img src="{escaped_src}" style="{IMG_STYLE}" alt=""></p>'


def render_html(title, blocks, append_image=None):
    body_html = "\n".join(block_to_html(block) for block in blocks)
    if append_image:
        body_html = body_html + "\n" + image_to_html(append_image)
    return body_html + "\n"


def render_text(title, blocks, append_image=None):
    parts = []
    for block in blocks:
        parts.append("----------" if block == "---" else block)
        parts.append("")
    if append_image:
        parts.append(f"[封面插图：{append_image}]")
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Format an article into WeChat-ready inline HTML.")
    parser.add_argument("--input", help="Input article file. Reads stdin when omitted.")
    parser.add_argument("--output-dir", default=".", help="Output directory.")
    parser.add_argument("--basename", help="Output basename without extension.")
    parser.add_argument("--append-image", help="Optional image path to append at the end of the article body.")
    args = parser.parse_args()

    raw = read_input(args.input)
    title, body = extract_title_and_body(raw)
    blocks = auto_insert_separators(normalize_blocks(body))

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    base = args.basename or slugify(title)

    html_path = output_dir / f"{base}.html"
    text_path = output_dir / f"{base}.txt"
    html_path.write_text(render_html(title, blocks, args.append_image), encoding="utf-8")
    text_path.write_text(render_text(title, blocks, args.append_image), encoding="utf-8")

    print(f"HTML: {html_path}")
    print(f"TXT: {text_path}")
    print(f"Title: {title}")
    print(f"Paragraphs: {sum(1 for block in blocks if block != '---')}")
    print(f"Separators: {sum(1 for block in blocks if block == '---')}")
    if args.append_image:
        print(f"Appended image: {args.append_image}")


if __name__ == "__main__":
    main()
