#!/usr/bin/env python3
"""Check common BSSw blog article formatting issues."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MONTHS = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}

TRACKS = {
    "deep dive",
    "experience",
    "community",
    "how to",
    "bright spots",
    "bssw fellowship",
}

REQUIRED_METADATA = {"publish", "track", "topics"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article", type=Path, help="Path to Articles/Blog/*.md")
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Exit nonzero when warnings are present.",
    )
    return parser.parse_args()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def find_metadata(text: str) -> tuple[str | None, dict[str, str], int | None]:
    for match in re.finditer(r"<!---\s*(.*?)\s*--->", text, flags=re.DOTALL):
        block = match.group(1)
        if re.search(r"^\s*Publish\s*:", block, flags=re.IGNORECASE | re.MULTILINE):
            fields: dict[str, str] = {}
            for raw_line in block.splitlines():
                line = raw_line.strip()
                if not line or ":" not in line:
                    continue
                key, value = line.split(":", 1)
                fields[key.strip().lower()] = value.strip()
            return block, fields, line_number(text, match.start())
    return None, {}, None


def check_article(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return [f"{path}: file does not exist"], warnings

    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    if path.suffix.lower() != ".md":
        errors.append("Article file should be Markdown (*.md).")
    if "Articles" not in path.parts or "Blog" not in path.parts:
        warnings.append("Article path is not under Articles/Blog.")

    first_nonblank = next((line for line in lines if line.strip()), "")
    if not first_nonblank.startswith("# "):
        errors.append("First nonblank line should be the level-one article title.")

    if not re.search(r"^#### Contributed by .+", text, flags=re.MULTILINE):
        errors.append("Missing `#### Contributed by ...` line.")

    pub = re.search(
        r"^#### Publication date:\s+([A-Z][a-z]+)\s+(\d{1,2}),\s+(\d{4})\s*$",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not pub:
        errors.append("Missing publication date line in the form `#### Publication date: Month D, YYYY`.")
    else:
        month = pub.group(1).capitalize()
        if month not in MONTHS:
            errors.append(f"Unknown publication month `{pub.group(1)}`.")
        file_date = re.match(r"^(\d{4})-(\d{2})-", path.name)
        if file_date and month in MONTHS:
            pub_prefix = f"{pub.group(3)}-{MONTHS[month]}"
            filename_prefix = f"{file_date.group(1)}-{file_date.group(2)}"
            if filename_prefix != pub_prefix:
                warnings.append(
                    f"Filename prefix `{filename_prefix}` does not match publication month `{pub_prefix}`."
                )

    has_hero = "**Hero Image:**" in text
    has_begin_deck = "<!-- begin deck -->" in text and "<!-- end deck -->" in text
    has_old_deck = "<!-- deck text start -->" in text and "<!-- deck text end -->" in text
    has_deck = has_begin_deck or has_old_deck
    if has_hero and has_deck:
        warnings.append("Blog has both hero image and deck text; confirm this is intentional.")
    if not has_hero and not has_deck:
        errors.append("Blog should have either hero image or deck text.")
    if "<!-- begin deck -->" in text and "<!-- end deck -->" not in text:
        errors.append("Deck text starts but does not end with `<!-- end deck -->`.")

    deck_match = re.search(r"<!-- begin deck -->(.*?)<!-- end deck -->", text, flags=re.DOTALL)
    if deck_match and re.search(r"https?://|\]\(", deck_match.group(1)):
        errors.append("Deck text should not contain links.")

    metadata_block, metadata, metadata_line = find_metadata(text)
    if metadata_block is None:
        errors.append("Missing formatted metadata block with Publish, Track, and Topics.")
    else:
        missing = REQUIRED_METADATA - set(metadata)
        if missing:
            errors.append(f"Metadata block on line {metadata_line} is missing: {', '.join(sorted(missing))}.")
        track = metadata.get("track", "").strip().lower()
        if track and track not in TRACKS:
            warnings.append(f"Metadata track `{metadata.get('track')}` is not one of the known blog tracks.")
        topics = metadata.get("topics", "")
        if topics and len([topic for topic in topics.split(",") if topic.strip()]) > 5:
            warnings.append("Metadata lists more than five topics; confirm the topic set is intentionally broad.")

    for match in re.finditer(r"<img\b[^>]*>", text, flags=re.IGNORECASE):
        tag = match.group(0)
        line = line_number(text, match.start())
        src_match = re.search(r"src=['\"]([^'\"]+)['\"]", tag, flags=re.IGNORECASE)
        if not src_match:
            errors.append(f"Image tag on line {line} is missing `src`.")
            continue
        src = src_match.group(1)
        if not src.startswith("../../images/"):
            warnings.append(f"Image on line {line} uses nonstandard src `{src}`.")
        else:
            image_path = path.parent / src
            if not image_path.resolve().exists():
                warnings.append(f"Image on line {line} points to missing file `{src}`.")
        line_text = lines[line - 1] if line - 1 < len(lines) else ""
        is_hero_line = has_hero and line_text.lstrip().startswith("- ")
        if not is_hero_line and "class=" not in tag:
            warnings.append(f"Body image on line {line} is missing a `class` attribute.")
        if "alt=" not in tag:
            warnings.append(f"Image on line {line} is missing `alt` text.")

    if re.search(r"!\[[^\]]*\]\([^)]*\)", text):
        warnings.append("Markdown image syntax found; BSSw blog articles should use HTML image tags.")

    if "<sup>[" in text and "sfer-ezikiw" not in text:
        warnings.append("Inline citation markers found without generated `sfer-ezikiw` references.")

    for idx, line in enumerate(lines, start=1):
        if line.startswith("### ") and not any(prev.startswith("## ") for prev in lines[: idx - 1]):
            warnings.append(f"Line {idx} uses `###` before any `##` heading.")
            break

    return errors, warnings


def main() -> int:
    args = parse_args()
    errors, warnings = check_article(args.article)

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    if not errors and not warnings:
        print("OK: no common BSSw blog formatting issues found.")
    elif not errors:
        print(f"OK: no errors found; {len(warnings)} warning(s) reported.")

    if errors or (warnings and args.strict_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
