#!/usr/bin/env python3
"""Build the YouMind style library for wechat-style-studio.

This script converts the extracted YouMind style cards into a compact,
progressively-loadable skill reference library.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import Counter, OrderedDict
from pathlib import Path
from typing import Any

from PIL import Image


ARTICLE_CLASS_ORDER = [
    "清单型爆款教程",
    "步骤型深度指南",
    "爆款解释型文章",
    "观点型解释分析",
    "技术实操拆解",
    "叙事型长文",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def safe_id(rank: str, slug: str) -> str:
    slug = re.sub(r"[^a-z0-9-]+", "-", slug.lower()).strip("-")
    return f"{int(rank):04d}-{slug}"


def parse_summary(value: str) -> tuple[str, str]:
    if "；" in value:
        left, right = value.split("；", 1)
        return left.strip(), right.strip()
    return value.strip(), ""


def metric_int(row: dict[str, str], key: str) -> int:
    try:
        return int(row.get(key) or 0)
    except ValueError:
        return 0


def score(row: dict[str, Any]) -> int:
    metrics = row["metrics"]
    return metrics["views"] + 50 * metrics["likes"] + 80 * metrics["bookmarks"]


def unique_by_slug(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    result: list[dict[str, Any]] = []
    for row in rows:
        if row["slug"] in seen:
            continue
        seen.add(row["slug"])
        result.append(row)
    return result


def load_style_rows(source_root: Path) -> list[dict[str, Any]]:
    style_rows = read_csv(source_root / "style-skills" / "index.csv")
    article_rows = {row["rank"]: row for row in read_csv(source_root / "articles.csv")}
    rows: list[dict[str, Any]] = []

    for row in style_rows:
        article = article_rows[row["rank"]]
        article_class, article_hook = parse_summary(row["article_summary"])
        cover_class, cover_hint = parse_summary(row["cover_summary"])
        rank_slug = safe_id(row["rank"], row["slug"])
        rows.append(
            {
                "style_id": rank_slug,
                "rank": int(row["rank"]),
                "slug": row["slug"],
                "skill_id": row["skill_id"],
                "skill_name": row["skill_name"],
                "title": row["title"],
                "author": row["author"],
                "author_handle": article.get("author_handle", ""),
                "source_link": article.get("source_link", ""),
                "youmind_url": article.get("youmind_url", ""),
                "cover_image_url": article.get("cover_image_url", ""),
                "original_language": article.get("original_language", ""),
                "article_class": article_class,
                "article_hook": article_hook,
                "cover_class": cover_class,
                "cover_hint": cover_hint,
                "article_summary": row["article_summary"],
                "cover_summary": row["cover_summary"],
                "metrics": {
                    "views": metric_int(article, "views"),
                    "likes": metric_int(article, "likes"),
                    "reposts": metric_int(article, "reposts"),
                    "comments": metric_int(article, "comments"),
                    "bookmarks": metric_int(article, "bookmarks"),
                    "quotes": metric_int(article, "quotes"),
                },
                "reference_path": f"references/styles/{rank_slug}.md",
                "source_style_path": source_root / "style-skills" / row["skill_path"],
                "source_cover_path": Path(article["cover_local"]),
            }
        )
    return rows


def make_thumbnail(source: Path, target: Path, width: int = 720) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image = image.convert("RGB")
        height = max(1, round(width * image.height / image.width))
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        image.save(target, quality=82, optimize=True)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def skill_md() -> str:
    return """---
name: wechat-style-studio
description: Use when the user wants to choose, browse, recommend, mix, or apply YouMind viral article styles, cover styles, writing styles, “这种风格/那种风格”, “Dan Koe 风格”, “Claude Code 教程风”, or data-ranked WeChat public-account article and cover style references before rewriting or generating a cover.
---

# WeChat Style Studio

Choose and apply YouMind-derived viral writing and cover styles for WeChat public-account articles.

## Core Rule

Use progressive disclosure. Never bulk-read all 830 style cards.

1. Read `references/style-index.json` first.
2. Shortlist 3-5 candidate styles from the index.
3. Ask the user to pick one, unless they already named a specific style.
4. Read only the selected style card from `references/styles/`.
5. Pass the selected article style to `wechat-rewrite` and the selected cover style to `wechat-cover-image`.

## Inputs

The user may provide:

- Source material for a WeChat article.
- A named style, such as `Dan Koe`, `Claude Code 教程`, `黑白寓言`, `浅底信息图`, or a YouMind title.
- A mixing request, such as “文章用 A 风格，封面用 B 风格”.
- No style at all; in that case, recommend styles.

If source material is missing, first help the user choose a style, then ask for the material.

## Style Selection

When recommending styles:

- Prefer topic match first.
- Then prefer high `metrics.bookmarks`, `metrics.likes`, and `metrics.views`.
- Keep visual variety: do not recommend five styles with the same cover class unless the user asked for that class.
- Show 3-5 candidates with title, author, article class, cover class, and why it fits.

Good candidate format:

```text
1. 如何用 1 天时间彻底重塑你的人生 — Dan Koe
   文章：强教练型清单教程；封面：黑白低饱和 editorial
   适合：个人成长、认知重塑、强行动承诺
```

When the user says “这种/那种风格” and points to an existing article or cover, match by:

1. Exact title/slug/author.
2. Article class and cover class.
3. Keywords in title, article hook, and cover hint.
4. Engagement score as tie-breaker.

## Applying A Style

After a style is selected:

1. Read the selected `references/styles/<style-id>.md`.
2. Extract the `文章 Skill` section and reuse its article prompt/fingerprint.
3. Extract the `封面 Skill` section and reuse its cover prompt/fingerprint.
4. If the user mixes two styles, read exactly two style cards: one for article, one for cover.
5. Summarize the selected pairing before writing:

```text
已选风格：
- 文章：<title> / <article class>
- 封面：<title> / <cover class>
```

## Coordination With Other Skills

- For rewriting, use `wechat-rewrite` after selecting the article style.
- For cover generation, use `wechat-cover-image` after selecting the cover style.
- For the full workflow, use `wechat-article-pipeline`; this style studio runs before rewrite and cover generation.

## Useful References

- `references/style-index.json`: compact machine-readable index for all 830 styles.
- `references/representative-styles.md`: recommended styles by score and visual class.
- `references/style-gallery.md`: human-readable gallery and full directory.
- `references/styles/`: full style cards; load only selected cards.

## Output Shape

When only selecting styles:

```text
## 推荐风格
1. ...

## 我建议
<one recommendation and why>

## 下一步
请回复编号，或说“文章用 1，封面用 3”。
```

When applying styles:

```text
## 已选风格
- 文章：
- 封面：

## 风格使用说明
- 写作：
- 封面：

## 交给后续 skill
- Rewrite: use `wechat-rewrite`
- Cover: use `wechat-cover-image`
```
"""


def openai_yaml() -> str:
    return """interface:
  display_name: "公众号风格工作室"
  short_description: "从 830 个 YouMind 爆款文章/封面风格中推荐、选择、混搭并应用到公众号创作。"
  default_prompt: "Use $wechat-style-studio to recommend YouMind viral writing and cover styles for my WeChat article, then help me pick one."
"""


def representative_sets(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    scored = sorted(unique_by_slug(rows), key=score, reverse=True)
    top = scored[:12]

    cover_reps: list[dict[str, Any]] = []
    for cover_class, _ in Counter(row["cover_class"] for row in rows).most_common():
        group = [row for row in scored if row["cover_class"] == cover_class]
        cover_reps.extend(group[:3])

    article_reps: list[dict[str, Any]] = []
    for article_class in ARTICLE_CLASS_ORDER:
        group = [row for row in scored if row["article_class"] == article_class]
        article_reps.extend(group[:3])

    return unique_by_slug(top), unique_by_slug(cover_reps), unique_by_slug(article_reps)


def lightweight_index(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        result.append(
            {
                "style_id": row["style_id"],
                "rank": row["rank"],
                "slug": row["slug"],
                "style_name": row["skill_name"],
                "title": row["title"],
                "author": row["author"],
                "author_handle": row["author_handle"],
                "article_class": row["article_class"],
                "article_hook": row["article_hook"],
                "cover_class": row["cover_class"],
                "cover_hint": row["cover_hint"],
                "metrics": row["metrics"],
                "reference_path": row["reference_path"],
                "cover_image_url": row["cover_image_url"],
                "youmind_url": row["youmind_url"],
                "source_link": row["source_link"],
            }
        )
    return result


def class_summary(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    counts = Counter(row[key] for row in rows)
    return [{"name": name, "count": count} for name, count in counts.most_common()]


def gallery_image(style_id: str, title: str, folder: str = "top") -> str:
    return f'<img src="../assets/covers/{folder}/{style_id}.jpg" alt="{title}" width="100%" />'


def md_link(row: dict[str, Any]) -> str:
    return f"[{row['title']}](styles/{row['style_id']}.md)"


def representative_markdown(top: list[dict[str, Any]], cover_reps: list[dict[str, Any]], article_reps: list[dict[str, Any]]) -> str:
    lines = [
        "# Representative YouMind Styles",
        "",
        "Use this file when you need a quick shortlist before searching all 830 styles.",
        "",
        "## Data Leaders",
        "",
    ]
    for row in top:
        lines.append(
            f"- **{row['title']}** — {row['author']}；文章：{row['article_class']}；封面：{row['cover_class']}；views {row['metrics']['views']} / bookmarks {row['metrics']['bookmarks']}；card: `{row['reference_path']}`"
        )

    lines.extend(["", "## Cover Style Representatives", ""])
    grouped: OrderedDict[str, list[dict[str, Any]]] = OrderedDict()
    for row in cover_reps:
        grouped.setdefault(row["cover_class"], []).append(row)
    for cover_class, group in grouped.items():
        lines.extend([f"### {cover_class}", ""])
        for row in group:
            lines.append(f"- **{row['title']}** — {row['article_class']}；`{row['reference_path']}`")
        lines.append("")

    lines.extend(["## Article Style Representatives", ""])
    grouped = OrderedDict()
    for row in article_reps:
        grouped.setdefault(row["article_class"], []).append(row)
    for article_class, group in grouped.items():
        lines.extend([f"### {article_class}", ""])
        for row in group:
            lines.append(f"- **{row['title']}** — {row['cover_class']}；`{row['reference_path']}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def style_gallery(rows: list[dict[str, Any]], top: list[dict[str, Any]], cover_reps: list[dict[str, Any]]) -> str:
    lines = [
        "# YouMind Style Gallery",
        "",
        "A browseable directory for 830 YouMind-derived WeChat article and cover style cards.",
        "",
        "## Top Data Styles",
        "",
        "<table>",
    ]
    for index in range(0, len(top), 3):
        lines.append("<tr>")
        for row in top[index : index + 3]:
            lines.append(
                f'<td width="33%" valign="top">{gallery_image(row["style_id"], row["title"], "top")}<br><b>{row["title"]}</b><br><sub>{row["article_class"]} · {row["cover_class"]}</sub><br><sub>{row["author"]}</sub></td>'
            )
        lines.append("</tr>")
    lines.extend(["</table>", "", "## Cover Systems", ""])

    grouped: OrderedDict[str, list[dict[str, Any]]] = OrderedDict()
    for row in cover_reps:
        grouped.setdefault(row["cover_class"], []).append(row)
    for cover_class, group in grouped.items():
        lines.extend([f"### {cover_class}", "", "<table>", "<tr>"])
        for row in group[:3]:
            lines.append(
                f'<td width="33%" valign="top">{gallery_image(row["style_id"], row["title"], "representative")}<br><b>{row["title"]}</b><br><sub>{row["article_class"]}</sub></td>'
            )
        lines.extend(["</tr>", "</table>", ""])

    lines.extend(
        [
            "## All Styles",
            "",
            "| Rank | Style | Author | Article | Cover | Metrics |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for row in rows:
        metrics = row["metrics"]
        lines.append(
            f"| {row['rank']} | {md_link(row)} | {row['author']} | {row['article_class']} | {row['cover_class']} | {metrics['views']} views / {metrics['bookmarks']} bookmarks |"
        )
    return "\n".join(lines) + "\n"


def build(source_root: Path, repo_root: Path) -> None:
    rows = load_style_rows(source_root)
    top, cover_reps, article_reps = representative_sets(rows)

    skill_root = repo_root / "skills" / "wechat-style-studio"
    references = skill_root / "references"
    styles_dir = references / "styles"
    assets = skill_root / "assets" / "covers"

    if skill_root.exists():
        shutil.rmtree(skill_root)

    write_text(skill_root / "SKILL.md", skill_md())
    write_text(skill_root / "agents" / "openai.yaml", openai_yaml())
    write_text(
        references / "style-index.json",
        json.dumps(
            {
                "schema_version": 1,
                "style_count": len(rows),
                "selection_policy": {
                    "read_first": "references/style-index.json",
                    "shortlist": "Use topic, article_class, cover_class, and metrics to recommend 3-5 styles.",
                    "load_later": "Read exactly the selected references/styles/<style-id>.md cards.",
                    "never": "Do not bulk-read all style cards.",
                },
                "article_classes": class_summary(rows, "article_class"),
                "cover_classes": class_summary(rows, "cover_class"),
                "styles": lightweight_index(rows),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
    )
    write_text(references / "representative-styles.md", representative_markdown(top, cover_reps, article_reps))
    write_text(references / "style-gallery.md", style_gallery(rows, top, cover_reps))

    for row in rows:
        source_card = row["source_style_path"]
        target_card = styles_dir / f"{row['style_id']}.md"
        text = source_card.read_text(encoding="utf-8")
        write_text(target_card, text)

    for row in top:
        make_thumbnail(row["source_cover_path"], assets / "top" / f"{row['style_id']}.jpg")
    for row in cover_reps:
        make_thumbnail(row["source_cover_path"], assets / "representative" / f"{row['style_id']}.jpg")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True, help="Extracted YouMind folder.")
    parser.add_argument("--repo-root", type=Path, default=Path("."), help="wechat-article-skills repo root.")
    args = parser.parse_args()
    build(args.source_root.resolve(), args.repo_root.resolve())
    print("built wechat-style-studio from", args.source_root)


if __name__ == "__main__":
    main()
