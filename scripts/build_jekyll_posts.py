#!/usr/bin/env python3
"""Build Jekyll _posts plus calendar/date archives from GEO-SEO News markdown."""

from __future__ import annotations

import argparse
import calendar
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NEWS_ROOT = REPO_ROOT / "GEO-SEO News"
POSTS_ROOT = REPO_ROOT / "_posts"
DATE_ARCHIVE_ROOT = REPO_ROOT / "date"
DATA_ROOT = REPO_ROOT / "_data"
CALENDAR_DATA_PATH = DATA_ROOT / "calendar.json"
GENERATED_MARKER = "generated_from"
DATE_ARCHIVE_MARKER = "generated_date_archive"


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


def normalize_categories(value: object, source_slug: str) -> list[str]:
    categories = value or []
    if not isinstance(categories, list):
        categories = [str(categories)]
    normalized = [str(item).strip() for item in categories if str(item).strip()]
    source_category = f"_src_{source_slug}"
    if source_category not in normalized:
        normalized.append(source_category)
    return normalized


def markdown_to_excerpt(body: str, limit: int = 180) -> str:
    text = body
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return yaml_quote(str(value))


def emit_yaml_block(key: str, value: object, indent: int = 0) -> list[str]:
    pad = " " * indent
    if isinstance(value, list):
        if not value:
            return [f"{pad}{key}: []"]
        lines = [f"{pad}{key}:"]
        lines.extend(emit_yaml_list(value, indent + 2))
        return lines
    if isinstance(value, dict):
        if not value:
            return [f"{pad}{key}: {{}}"]
        lines = [f"{pad}{key}:"]
        lines.extend(emit_yaml_dict(value, indent + 2))
        return lines
    return [f"{pad}{key}: {yaml_scalar(value)}"]


def emit_yaml_dict(value: dict[str, object], indent: int = 0) -> list[str]:
    lines: list[str] = []
    for key, item in value.items():
        lines.extend(emit_yaml_block(str(key), item, indent))
    return lines


def emit_yaml_list(values: list[object], indent: int = 0) -> list[str]:
    pad = " " * indent
    lines: list[str] = []
    for item in values:
        if isinstance(item, dict):
            lines.append(f"{pad}-")
            lines.extend(emit_yaml_dict(item, indent + 2))
        elif isinstance(item, list):
            if not item:
                lines.append(f"{pad}- []")
            else:
                lines.append(f"{pad}-")
                lines.extend(emit_yaml_list(item, indent + 2))
        else:
            lines.append(f"{pad}- {yaml_scalar(item)}")
    return lines


def build_post(path: Path) -> tuple[Path, str, dict[str, object]]:
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
    categories = normalize_categories(front_matter.get("categories"), source_slug)

    fingerprint = hashlib.sha1(str(relative_source).encode("utf-8")).hexdigest()[:8]
    slug = slugify(path.stem, fingerprint)
    year, month, _day = date_dir.split("-", 2)
    destination = POSTS_ROOT / year / month / f"{date_dir}-{slug}.md"
    url = f"/{date_dir}/{slug}/"
    excerpt = markdown_to_excerpt(body)

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

    post_data = {
        "title": title,
        "source": source,
        "source_slug": source_slug,
        "date": date_dir,
        "url": url,
        "excerpt": excerpt,
        "categories": [category for category in categories if not category.startswith("_src_")],
        "original_url": original_url,
        "author": author,
    }
    return destination, "\n".join(lines), post_data


def build_calendar_data(posts_by_date: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    months: list[dict[str, object]] = []
    month_keys = sorted({date_key[:7] for date_key in posts_by_date}, reverse=True)
    latest_month = month_keys[0] if month_keys else ""
    month_calendar = calendar.Calendar(firstweekday=0)

    for month_key in month_keys:
        year = int(month_key[:4])
        month_num = int(month_key[5:7])
        weeks: list[list[dict[str, object]]] = []
        for week in month_calendar.monthdatescalendar(year, month_num):
            rendered_week: list[dict[str, object]] = []
            for day in week:
                date_key = day.isoformat()
                day_posts = posts_by_date.get(date_key, [])
                rendered_week.append(
                    {
                        "date": date_key,
                        "day": day.day,
                        "in_month": day.month == month_num,
                        "has_posts": bool(day_posts),
                        "count": len(day_posts),
                        "url": f"/date/{date_key}/" if day_posts else "",
                    }
                )
            weeks.append(rendered_week)

        month_days = []
        for date_key in sorted(
            [key for key in posts_by_date if key.startswith(month_key)],
            reverse=True,
        ):
            day_posts = posts_by_date[date_key]
            month_days.append(
                {
                    "date": date_key,
                    "day": int(date_key[-2:]),
                    "count": len(day_posts),
                    "url": f"/date/{date_key}/",
                    "sources": sorted({str(post["source"]) for post in day_posts}),
                }
            )

        months.append(
            {
                "month": month_key,
                "year": year,
                "month_num": month_num,
                "label": f"{year}年{month_num:02d}月",
                "anchor": f"month-{month_key}",
                "weeks": weeks,
                "days": month_days,
            }
        )

    return {
        "latest_month": latest_month,
        "weekdays": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        "months": months,
    }


def build_date_archive_page(date_key: str, posts: list[dict[str, object]]) -> str:
    date_label = f"{date_key[:4]}年{date_key[5:7]}月{date_key[8:10]}日"
    sources = sorted({str(post["source"]) for post in posts})
    entries = [
        {
            "title": str(post["title"]),
            "url": str(post["url"]),
            "source": str(post["source"]),
            "excerpt": str(post["excerpt"]),
            "categories": list(post.get("categories", [])),
        }
        for post in posts
    ]

    lines = [
        "---",
        "layout: date_archive",
        f"title: {yaml_quote(date_label)}",
        f"date_value: {yaml_quote(date_key)}",
        f"date_label: {yaml_quote(date_label)}",
        f"permalink: /date/{date_key}/",
        f"{DATE_ARCHIVE_MARKER}: true",
        f"post_count: {len(posts)}",
    ]
    lines.extend(emit_yaml_block("sources", sources))
    lines.extend(emit_yaml_block("entries", entries))
    lines.extend(["---", ""])
    return "\n".join(lines)


def write_date_archives(posts_by_date: dict[str, list[dict[str, object]]], dry_run: bool) -> tuple[int, set[Path]]:
    DATE_ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)
    desired_paths: set[Path] = set()
    written = 0

    for date_key in sorted(posts_by_date.keys(), reverse=True):
        destination = DATE_ARCHIVE_ROOT / date_key / "index.html"
        desired_paths.add(destination)
        rendered = build_date_archive_page(date_key, posts_by_date[date_key])
        current = destination.read_text(encoding="utf-8") if destination.exists() else None
        if current == rendered:
            continue
        written += 1
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered, encoding="utf-8")

    return written, desired_paths


def write_calendar_data(calendar_data: dict[str, object], dry_run: bool) -> int:
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(calendar_data, ensure_ascii=False, indent=2) + "\n"
    current = CALENDAR_DATA_PATH.read_text(encoding="utf-8") if CALENDAR_DATA_PATH.exists() else None
    if current == rendered:
        return 0
    if not dry_run:
        CALENDAR_DATA_PATH.write_text(rendered, encoding="utf-8")
    return 1


def cleanup_stale_generated_files(root: Path, desired_paths: set[Path], marker_key: str, dry_run: bool) -> int:
    removed = 0
    if not root.exists():
        return 0
    for path in root.rglob("*.md" if root == POSTS_ROOT else "*.html"):
        if path in desired_paths:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        front_matter, _body = split_front_matter(content)
        if marker_key not in front_matter:
            continue
        removed += 1
        if not dry_run:
            path.unlink()
    return removed


def run(dry_run: bool) -> int:
    POSTS_ROOT.mkdir(parents=True, exist_ok=True)
    source_files = iter_source_files()
    desired_post_paths: set[Path] = set()
    written_posts = 0
    unchanged_posts = 0
    posts_by_date: dict[str, list[dict[str, object]]] = defaultdict(list)

    for source_path in source_files:
        destination, rendered, post_data = build_post(source_path)
        desired_post_paths.add(destination)
        posts_by_date[str(post_data["date"])].append(post_data)
        current = destination.read_text(encoding="utf-8") if destination.exists() else None
        if current == rendered:
            unchanged_posts += 1
            continue
        written_posts += 1
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered, encoding="utf-8")

    for date_key, entries in posts_by_date.items():
        entries.sort(key=lambda item: (str(item["source"]), str(item["title"])))

    removed_posts = cleanup_stale_generated_files(POSTS_ROOT, desired_post_paths, GENERATED_MARKER, dry_run=dry_run)
    written_archives, desired_archive_paths = write_date_archives(posts_by_date, dry_run=dry_run)
    removed_archives = cleanup_stale_generated_files(
        DATE_ARCHIVE_ROOT,
        desired_archive_paths,
        DATE_ARCHIVE_MARKER,
        dry_run=dry_run,
    )
    calendar_data = build_calendar_data(posts_by_date)
    written_calendar = write_calendar_data(calendar_data, dry_run=dry_run)

    print(f"source_files={len(source_files)}")
    print(f"written_posts={written_posts}")
    print(f"unchanged_posts={unchanged_posts}")
    print(f"removed_posts={removed_posts}")
    print(f"written_date_archives={written_archives}")
    print(f"removed_date_archives={removed_archives}")
    print(f"written_calendar_data={written_calendar}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print counts without writing files")
    args = parser.parse_args()
    return run(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
