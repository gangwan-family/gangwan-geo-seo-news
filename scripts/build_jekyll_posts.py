#!/usr/bin/env python3
"""Build Jekyll _posts from GEO-SEO News source markdown files."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NEWS_ROOT = REPO_ROOT / "GEO-SEO News"
POSTS_ROOT = REPO_ROOT / "_posts"
GENERATED_MARKER = "generated_from"


def split_front_matter(content: str) -> tuple[dict[str, object], str]:
    if not content.startswith("---\n"):
        return {}, content
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return {}, content
    front_matter_raw = parts[1]
    body = parts[2]
    return parse_front_matter(front_matter_raw), body.lstrip("\n")


def parse_front_matter(front_matter_raw: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_list_key: str | None = None

    for raw_line in front_matter_raw.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("- ") and current_list_key:
            values = data.setdefault(current_list_key, [])
            if isinstance(values, list):
                values.append(unquote_yaml(stripped[2:].strip()))
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue
        data[key] = unquote_yaml(value)
    return data


def unquote_yaml(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        inner = value[1:-1]
        if value[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\\\", "\\")
        return inner
    return value


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def slugify(value: str, fallback: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = lowered.strip("-")
    return lowered or fallback


def normalize_date(value: str, fallback: str) -> str:
    value = value.strip()
    if not value:
        return fallback
    if re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return value
    if re.match(r"^\d{4}-\d{2}-\d{2}T", value):
        return value
    return fallback


def iter_source_files() -> list[Path]:
    results: list[Path] = []
    for path in NEWS_ROOT.rglob("*.md"):
        rel_parts = path.relative_to(NEWS_ROOT).parts
        if len(rel_parts) < 3:
            continue
        if rel_parts[0].startswith("_"):
            continue
        if path.name == "README.md":
            continue
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", rel_parts[1]):
            continue
        results.append(path)
    return sorted(results)


def build_post(path: Path) -> tuple[Path, str]:
    relative_path = path.relative_to(REPO_ROOT)
    relative_source = path.relative_to(NEWS_ROOT)
    source_name, date_dir, *_rest = relative_source.parts
    content = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(content)

    title = str(front_matter.get("title") or path.stem).strip()
    source = str(front_matter.get("source") or source_name).strip()
    source_slug = slugify(source_name, "source")
    original_url = str(front_matter.get("original_url") or front_matter.get("url") or "").strip()
    author = str(front_matter.get("author") or "").strip()
    date_value = normalize_date(str(front_matter.get("published") or front_matter.get("date") or ""), date_dir)
    categories = front_matter.get("categories") or []
    if not isinstance(categories, list):
        categories = [str(categories)]
    categories = [str(item).strip() for item in categories if str(item).strip()]
    source_category = f"_src_{source_slug}"
    if source_category not in categories:
        categories.append(source_category)

    fingerprint = hashlib.sha1(str(relative_source).encode("utf-8")).hexdigest()[:8]
    slug = slugify(path.stem, fingerprint)
    year, month, _day = date_dir.split("-", 2)
    destination = POSTS_ROOT / year / month / f"{date_dir}-{slug}.md"

    lines = [
        "---",
        "layout: post",
        f"title: {yaml_quote(title)}",
        f"date: {date_value}",
        f"source: {yaml_quote(source)}",
        f"source_slug: {yaml_quote(source_slug)}",
        f"{GENERATED_MARKER}: {yaml_quote(str(relative_path))}",
    ]
    if original_url:
        lines.append(f"original_url: {yaml_quote(original_url)}")
    if author:
        lines.append(f"author: {yaml_quote(author)}")
    if categories:
        lines.append("categories:")
        lines.extend(f"  - {yaml_quote(category)}" for category in categories)
    lines.extend(["---", "", body.rstrip(), ""])
    return destination, "\n".join(lines)


def cleanup_stale_posts(desired_paths: set[Path], dry_run: bool) -> int:
    removed = 0
    for path in POSTS_ROOT.rglob("*.md"):
        if path in desired_paths:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        front_matter, _body = split_front_matter(content)
        if GENERATED_MARKER not in front_matter:
            continue
        removed += 1
        if not dry_run:
            path.unlink()
    return removed


def run(dry_run: bool) -> int:
    POSTS_ROOT.mkdir(parents=True, exist_ok=True)
    source_files = iter_source_files()
    desired_paths: set[Path] = set()
    written = 0
    unchanged = 0

    for source_path in source_files:
        destination, rendered = build_post(source_path)
        desired_paths.add(destination)
        current = destination.read_text(encoding="utf-8") if destination.exists() else None
        if current == rendered:
            unchanged += 1
            continue
        written += 1
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered, encoding="utf-8")

    removed = cleanup_stale_posts(desired_paths, dry_run=dry_run)

    print(f"source_files={len(source_files)}")
    print(f"written_posts={written}")
    print(f"unchanged_posts={unchanged}")
    print(f"removed_posts={removed}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print counts without writing files")
    args = parser.parse_args()
    return run(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
