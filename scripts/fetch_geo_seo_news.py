#!/usr/bin/env python3
"""Fetch GEO/SEO news feeds and save new posts as Markdown notes."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
NEWS_ROOT = REPO_ROOT / "GEO-SEO News"
SOURCES_PATH = NEWS_ROOT / "sources.json"
STATE_PATH = NEWS_ROOT / "_state" / "seen.json"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
# Modern browser request headers. OpenAI (and other Cloudflare-fronted sites)
# reject requests that lack the Sec-Fetch-* / Sec-CH-UA hints with HTTP 403 +
# a bot "challenge" interstitial, which makes article extraction fail. These
# headers are sent by every real browser, so they are safe for all sources.
SEC_FETCH_HEADERS = {
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-CH-UA": '"Chromium";v="126", "Not)A;Brand";v="99"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"macOS"',
}
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    **SEC_FETCH_HEADERS,
}
ARTICLE_MARKER = "## 原文正文"
SKIP_TAGS = {"script", "style", "svg", "noscript", "template", "form", "button", "nav", "footer", "aside"}
BLOCK_TAGS = {
    "address",
    "blockquote",
    "div",
    "figcaption",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "li",
    "p",
    "pre",
    "td",
    "th",
    "tr",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style"}:
            self.skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        return normalize_space(" ".join(self.parts))


class ArticleMarkdownExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lines: list[str] = []
        self.current: list[str] = []
        self.skip_depth = 0
        self.list_depth = 0
        self.heading_level: int | None = None
        self.in_link = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in BLOCK_TAGS:
            self.flush()
            if re.fullmatch(r"h[1-6]", tag):
                self.heading_level = min(int(tag[1]) + 1, 6)
        if tag in {"ul", "ol"}:
            self.list_depth += 1
        elif tag == "br":
            self.flush()
        elif tag == "a":
            self.in_link = True

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in BLOCK_TAGS:
            prefix = ""
            if self.heading_level:
                prefix = "#" * self.heading_level + " "
            elif tag == "li":
                prefix = "- "
            self.flush(prefix=prefix)
            self.heading_level = None
        elif tag in {"ul", "ol"} and self.list_depth:
            self.list_depth -= 1
        elif tag == "a":
            self.in_link = False

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        value = normalize_space(data)
        if value:
            self.current.append(value)

    def flush(self, prefix: str = "") -> None:
        text = normalize_space(" ".join(self.current))
        self.current = []
        if not text:
            return
        line = f"{prefix}{text}" if prefix else text
        if not self.lines or self.lines[-1] != line:
            self.lines.append(line)

    def markdown(self) -> str:
        self.flush()
        cleaned: list[str] = []
        for line in self.lines:
            if is_boilerplate_line(line):
                continue
            cleaned.append(line)
        return "\n\n".join(cleaned).strip()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def strip_html(value: str) -> str:
    value = html.unescape(value or "")
    parser = TextExtractor()
    parser.feed(value)
    parser.close()
    text = parser.text()
    return text or normalize_space(value)


def truncate(value: str, max_chars: int = 1200) -> str:
    value = normalize_space(value)
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 1].rstrip() + "..."


def is_boilerplate_line(value: str) -> bool:
    lowered = value.lower().strip()
    if len(lowered) <= 2:
        return True
    boilerplate = {
        "skip to main content",
        "sign in",
        "subscribe",
        "privacy policy",
        "terms of service",
        "cookie policy",
        "share",
        "share this article",
        "read more",
        "related articles",
        "recommended",
        "advertisement",
    }
    return lowered in boilerplate


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def child_text(element: ET.Element, *names: str) -> str:
    wanted = set(names)
    for child in list(element):
        if local_name(child.tag) in wanted:
            return normalize_space("".join(child.itertext()))
    return ""


def child_attr(element: ET.Element, child_name: str, attr_name: str) -> str:
    for child in list(element):
        if local_name(child.tag) == child_name:
            value = child.attrib.get(attr_name)
            if value:
                return normalize_space(value)
    return ""


def parse_date(value: str) -> datetime | None:
    value = normalize_space(value)
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def safe_filename(title: str, fallback: str) -> str:
    value = html.unescape(title or "").strip()
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    if not value:
        value = fallback
    if len(value) > 140:
        value = value[:140].rstrip(" .")
    return value or fallback


def load_sources() -> list[dict[str, Any]]:
    with SOURCES_PATH.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    sources = data.get("sources", data) if isinstance(data, dict) else data
    if not isinstance(sources, list):
        raise ValueError(f"Invalid sources file: {SOURCES_PATH}")
    return sources


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {"version": 1, "entries": {}}
    with STATE_PATH.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if "entries" not in data or not isinstance(data["entries"], dict):
        data["entries"] = {}
    return data


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_PATH.open("w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")


def fetch_bytes(url: str, timeout: int = 40) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers=REQUEST_HEADERS)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        return response.read(), content_type


def fetch_bytes_with_curl(url: str, timeout: int = 20) -> tuple[bytes, str]:
    command = [
        "curl",
        "-L",
        "--silent",
        "--show-error",
        "--max-time",
        str(timeout),
        "-A",
        USER_AGENT,
        "-H",
        f"Accept: {REQUEST_HEADERS['Accept']}",
        "-H",
        f"Accept-Language: {REQUEST_HEADERS['Accept-Language']}",
    ]
    for name, value in SEC_FETCH_HEADERS.items():
        command.extend(["-H", f"{name}: {value}"])
    command.append(url)
    result = subprocess.run(command, capture_output=True, check=False)
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(stderr or f"curl exited with {result.returncode}")
    return result.stdout, "text/html; charset=utf-8"


def fetch_feed(url: str) -> bytes:
    raw, _content_type = fetch_bytes(url)
    return raw


def decode_response(raw: bytes, content_type: str) -> str:
    charset_match = re.search(r"charset=([^\s;]+)", content_type or "", re.IGNORECASE)
    encodings = [charset_match.group(1)] if charset_match else []
    encodings.extend(["utf-8", "latin-1"])
    for encoding in encodings:
        try:
            return raw.decode(encoding)
        except (LookupError, UnicodeDecodeError):
            continue
    return raw.decode("utf-8", errors="replace")


def parse_feed(raw: bytes) -> list[ET.Element]:
    root = ET.fromstring(raw)
    items = [element for element in root.iter() if local_name(element.tag) == "item"]
    if items:
        return items
    return [element for element in root.iter() if local_name(element.tag) == "entry"]


def candidate_article_fragments(html_text: str) -> list[str]:
    patterns = [
        r"<article\b[^>]*>.*?</article>",
        r"<main\b[^>]*>.*?</main>",
        r"<div\b[^>]*(?:class|id)=['\"][^'\"]*(?:article|post|entry|content|story|body|rich-text|prose)[^'\"]*['\"][^>]*>.*?</div>",
    ]
    candidates: list[str] = []
    for pattern in patterns:
        candidates.extend(re.findall(pattern, html_text, flags=re.IGNORECASE | re.DOTALL))
    candidates.append(html_text)
    return candidates


def extract_article_text(html_text: str) -> str:
    best_text = ""
    best_score = -1
    for fragment in candidate_article_fragments(html_text):
        parser = ArticleMarkdownExtractor()
        parser.feed(fragment)
        parser.close()
        text = parser.markdown()
        if not text:
            continue
        score = len(text)
        lowered = text.lower()
        score -= lowered.count("subscribe") * 200
        score -= lowered.count("cookie") * 100
        score -= lowered.count("privacy") * 100
        if score > best_score:
            best_score = score
            best_text = text
    return best_text


def fetch_article_text(url: str) -> tuple[str, str | None]:
    if not url:
        return "", "missing URL"
    try:
        raw, content_type = fetch_bytes(url, timeout=20)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        try:
            raw, content_type = fetch_bytes_with_curl(url, timeout=20)
        except Exception as curl_exc:  # noqa: BLE001 - preserve both failure reasons.
            return "", f"{exc}; curl fallback failed: {curl_exc}"
    except Exception as exc:  # noqa: BLE001 - keep scheduled job resilient.
        try:
            raw, content_type = fetch_bytes_with_curl(url, timeout=20)
        except Exception as curl_exc:  # noqa: BLE001 - preserve both failure reasons.
            return "", f"{exc}; curl fallback failed: {curl_exc}"
    html_text = decode_response(raw, content_type)
    article_text = extract_article_text(html_text)
    if not article_text:
        return "", "article text not found"
    return article_text, None


def extract_entry(source: dict[str, str], item: ET.Element, fetched_at: datetime) -> dict[str, Any]:
    title = child_text(item, "title") or "Untitled"
    link = child_text(item, "link")
    if not link:
        link = child_attr(item, "link", "href")
    guid = child_text(item, "guid", "id") or link
    raw_description = child_text(item, "description", "summary")
    if not raw_description:
        raw_description = child_text(item, "encoded", "content")
    raw_date = child_text(item, "pubDate", "published", "updated")
    published_at = parse_date(raw_date) or fetched_at
    categories = [
        normalize_space("".join(child.itertext()))
        for child in list(item)
        if local_name(child.tag) == "category" and normalize_space("".join(child.itertext()))
    ]
    author = child_text(item, "creator", "author")
    if author and " " not in author:
        author_name = child_text(item, "name")
        author = author_name or author
    entry_key_base = guid or link or f"{source['name']}:{title}:{published_at.isoformat()}"
    entry_hash = hashlib.sha1(entry_key_base.encode("utf-8")).hexdigest()
    return {
        "key": f"{source['slug']}:{entry_hash}",
        "hash": entry_hash[:10],
        "source": source["name"],
        "source_slug": source["slug"],
        "title": html.unescape(title),
        "url": link,
        "guid": guid,
        "published_at": published_at,
        "published_date": published_at.date().isoformat(),
        "fetched_at": fetched_at,
        "categories": sorted(set(categories)),
        "author": author,
        "summary": truncate(strip_html(raw_description)),
        "full_text": "",
        "full_text_error": "",
    }


def markdown_for(entry: dict[str, Any]) -> str:
    categories = entry["categories"]
    frontmatter = [
        "---",
        f"title: {yaml_quote(entry['title'])}",
        f"source: {yaml_quote(entry['source'])}",
        f"published: {entry['published_at'].isoformat()}",
        f"fetched_at: {entry['fetched_at'].isoformat()}",
        f"url: {yaml_quote(entry['url'])}",
        f"guid: {yaml_quote(entry['guid'])}",
    ]
    if entry["author"]:
        frontmatter.append(f"author: {yaml_quote(entry['author'])}")
    if categories:
        frontmatter.append("categories:")
        frontmatter.extend(f"  - {yaml_quote(category)}" for category in categories)
    frontmatter.append("---")

    lines = [
        *frontmatter,
        "",
        f"# {entry['title']}",
        "",
        f"- Source: {entry['source']}",
        f"- Published: {entry['published_at'].date().isoformat()}",
        f"- URL: {entry['url']}",
    ]
    if entry["author"]:
        lines.append(f"- Author: {entry['author']}")
    if categories:
        lines.append(f"- Categories: {', '.join(categories)}")
    lines.extend(["", "## RSS 摘要", ""])
    lines.append(entry["summary"] or "No RSS summary provided.")
    lines.extend(["", ARTICLE_MARKER, ""])
    if entry.get("full_text"):
        lines.append(entry["full_text"])
    elif entry.get("full_text_error"):
        lines.append(f"原文正文抓取失败：{entry['full_text_error']}")
    else:
        lines.append("原文正文未抓取。")
    lines.extend(["", "## 原文链接", "", f"[Read original]({entry['url']})", ""])
    return "\n".join(lines)


def output_path_for(entry: dict[str, Any]) -> Path:
    date_dir = NEWS_ROOT / entry["source"] / entry["published_date"]
    filename = safe_filename(entry["title"], entry["hash"])
    path = date_dir / f"{filename}.md"
    if path.exists():
        path = date_dir / f"{filename}-{entry['hash']}.md"
    return path


def enrich_full_text(entry: dict[str, Any], source: dict[str, Any]) -> None:
    if not source.get("save_full_text", True):
        entry["full_text"] = ""
        entry["full_text_error"] = "full-text capture disabled for this source"
        return
    full_text, error = fetch_article_text(entry["url"])
    entry["full_text"] = full_text
    entry["full_text_error"] = error or ""


def save_entry(entry: dict[str, Any], source: dict[str, Any], dry_run: bool) -> Path:
    path = output_path_for(entry)
    if not dry_run:
        enrich_full_text(entry, source)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown_for(entry), encoding="utf-8")
    return path


def update_existing_entry(entry: dict[str, Any], source: dict[str, Any], path: Path, dry_run: bool) -> bool:
    if not path.is_file():
        return False
    current = path.read_text(encoding="utf-8")
    if ARTICLE_MARKER in current and "原文正文未抓取" not in current and "原文正文抓取失败" not in current:
        return False
    if dry_run:
        return True
    enrich_full_text(entry, source)
    path.write_text(markdown_for(entry), encoding="utf-8")
    return True


def run(dry_run: bool, lookback_days: int, max_per_source: int) -> int:
    sources = load_sources()
    state = load_state()
    seen = state["entries"]
    fetched_at = datetime.now(timezone.utc)
    cutoff = fetched_at - timedelta(days=lookback_days) if lookback_days > 0 else None
    saved_count = 0
    updated_count = 0
    success_count = 0
    failures: list[str] = []

    for source in sources:
        try:
            raw = fetch_feed(source["url"])
            items = parse_feed(raw)
            success_count += 1
        except Exception as exc:  # noqa: BLE001 - keep scheduled job resilient.
            failures.append(f"{source['name']}: {exc}")
            continue

        entries = [extract_entry(source, item, fetched_at) for item in items]
        if cutoff is not None:
            entries = [entry for entry in entries if entry["published_at"] >= cutoff]
        entries.sort(key=lambda entry: entry["published_at"])
        if max_per_source > 0 and len(entries) > max_per_source:
            entries = entries[-max_per_source:]
        for entry in entries:
            if entry["key"] in seen:
                existing_rel_path = seen[entry["key"]].get("path", "")
                if existing_rel_path:
                    existing_path = REPO_ROOT / existing_rel_path
                    if update_existing_entry(entry, source, existing_path, dry_run):
                        updated_count += 1
                        action = "would update" if dry_run else "updated"
                        print(f"{action}: {existing_path.relative_to(REPO_ROOT)}")
                continue
            path = save_entry(entry, source, dry_run=dry_run)
            seen[entry["key"]] = {
                "source": entry["source"],
                "title": entry["title"],
                "url": entry["url"],
                "published": entry["published_at"].isoformat(),
                "path": str(path.relative_to(REPO_ROOT)),
                "first_seen": fetched_at.isoformat(),
            }
            saved_count += 1
            print(f"saved: {path.relative_to(REPO_ROOT)}")

    state["last_run_at"] = fetched_at.isoformat()
    if not dry_run and (saved_count or updated_count):
        save_state(state)

    if failures:
        print("Feed failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)

    print(f"new_entries={saved_count}")
    print(f"updated_entries={updated_count}")
    if success_count == 0:
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print new files without writing them")
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=7,
        help="only sync posts published within this many days; use 0 to disable",
    )
    parser.add_argument(
        "--max-per-source",
        type=int,
        default=20,
        help="maximum new posts to save per source per run; use 0 to disable",
    )
    args = parser.parse_args()
    return run(
        dry_run=args.dry_run,
        lookback_days=args.lookback_days,
        max_per_source=args.max_per_source,
    )


if __name__ == "__main__":
    raise SystemExit(main())
