#!/usr/bin/env python3
"""Sync root skills into the marketplace plugin package."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / "plugins" / "wechat-article-skills" / "skills"


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"missing source skills directory: {SOURCE}")
    if TARGET.exists():
        shutil.rmtree(TARGET)
    shutil.copytree(SOURCE, TARGET)
    print(f"synced {SOURCE} -> {TARGET}")


if __name__ == "__main__":
    main()
