#!/usr/bin/env python3
"""Validate public-site navigation and fidelity to the canonical Markdown."""
from __future__ import annotations

from hashlib import sha256
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import posixpath
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
CANONICAL_HERO_STATEMENT = "Governance directs AI use. Security protects it. Evidence from real use informs the next decision."


def digest(value: str) -> str:
    return sha256(value.encode()).hexdigest()


def remove_document_title(markdown: str) -> str:
    value = re.sub(r"^#\s+.+(?:\r?\n|$)", "", markdown, count=1)
    return re.sub(r"^\s*\r?\n", "", value, count=1)


def plain_markdown(value: str) -> str:
    value = re.sub(r"^#{1,6}\s+", "", value, flags=re.M)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    return re.sub(r"\s+", " ", re.sub(r"[>*_`]", "", value)).strip()


def first_story_paragraph(markdown: str) -> str:
    story = re.search(r"^## The story\s*\n([\s\S]*?)(?=^## )", markdown, re.M)
    value = story.group(1) if story else markdown
    for paragraph in re.split(r"\r?\n\s*\r?\n", value):
        candidate = paragraph.strip()
        if candidate and not candidate.startswith(("#", "|", "-", "*")):
            return plain_markdown(candidate)
    return plain_markdown(value)


def document_title(markdown: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.M)
    return match.group(1).strip() if match else ""


def canonical_hero_statement(markdown: str) -> str:
    story = re.search(r"^## The story\s*\n([\s\S]*?)(?=^## )", markdown, re.M)
    values = re.findall(r"^\*\*([^\n*]+)\*\*$", story.group(1) if story else "", re.M)
    return next((plain_markdown(value) for value in values if plain_markdown(value) == CANONICAL_HERO_STATEMENT), "")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.h1 = 0
        self.article_h1 = 0
        self.article_depth = 0
        self.article_counts = {"paragraphs": 0, "tables": 0, "listItems": 0, "headings": 0}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        for key in ("href", "src"):
            if attributes.get(key):
                self.links.append(attributes[key])
        if tag == "h1":
            self.h1 += 1
            if self.article_depth:
                self.article_h1 += 1
        if tag == "article":
            self.article_depth += 1
        if self.article_depth:
            if tag == "p": self.article_counts["paragraphs"] += 1
            if tag == "table": self.article_counts["tables"] += 1
            if tag == "li": self.article_counts["listItems"] += 1
            if re.fullmatch(r"h[1-6]", tag): self.article_counts["headings"] += 1

    def handle_endtag(self, tag):
        if tag == "article" and self.article_depth:
            self.article_depth -= 1


class ArticleSemantics(HTMLParser):
    targets = {"p": "paragraphs", "li": "listItems", "th": "tableCells", "td": "tableCells"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.all_text: list[str] = []
        self.values = {"paragraphs": [], "tableCells": [], "listItems": [], "headings": []}
        self.frames: list[tuple[str, str, list[str]]] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.targets or re.fullmatch(r"h[1-6]", tag):
            self.frames.append((tag, self.targets.get(tag, "headings"), []))

    def handle_data(self, data):
        text = re.sub(r"\s+", " ", data)
        if not text.strip():
            for _, _, frame_text in self.frames:
                frame_text.append(text)
            return
        self.all_text.append(text)
        for _, _, frame_text in self.frames:
            frame_text.append(text)

    def handle_endtag(self, tag):
        if not self.frames or self.frames[-1][0] != tag:
            return
        _, collection, frame_text = self.frames.pop()
        value = re.sub(r"\s+", " ", "".join(frame_text)).strip()
        if value:
            self.values[collection].append(value)

    def digests(self) -> dict[str, str]:
        headings = digest("␞".join(self.values["headings"]))
        paragraphs = digest("␞".join(self.values["paragraphs"]))
        cells = digest("␞".join(self.values["tableCells"]))
        list_items = digest("␞".join(self.values["listItems"]))
        return {
            "canonicalTextSha256": digest("␞".join((headings, paragraphs, cells, list_items))),
            "paragraphTextSha256": paragraphs,
            "tableCellTextSha256": cells,
            "listItemTextSha256": list_items,
            "headingTextSha256": headings
        }


def source_path(relative: str) -> Path:
    if relative == "decisions.md":
        return ROOT / relative
    if not relative.startswith("content/"):
        raise ValueError(f"unexpected canonical source path: {relative}")
    return ROOT / relative


def article_html(html: str, source: str) -> str | None:
    escaped = re.escape(source)
    match = re.search(rf'<article\b(?=[^>]*\bdata-source="{escaped}")[^>]*>([\s\S]*?)</article>', html)
    return match.group(1) if match else None


errors: list[str] = []
pages: dict[Path, Page] = {}
html_by_path: dict[Path, str] = {}
for file in DIST.rglob("*.html"):
    value = file.read_text()
    parser = Page()
    parser.feed(value)
    pages[file] = parser
    html_by_path[file] = value

for file, page in pages.items():
    if page.h1 != 1:
        errors.append(f"{file.relative_to(DIST)} has {page.h1} document H1 elements (expected 1)")
    if page.article_h1:
        errors.append(f"{file.relative_to(DIST)} repeats a document H1 inside its canonical article")
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        base = DIST if url.path.startswith("/") else file.parent
        target = (base / unquote(url.path).lstrip("/")).resolve() if url.path else file
        if target.is_dir():
            target = target / "index.html" if (target / "index.html").exists() else target.with_suffix(".html")
        if not target.exists() and not target.suffix:
            target = target.with_suffix(".html")
        if not target.exists():
            errors.append(f"{file.relative_to(DIST)} -> missing {link}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"{file.relative_to(DIST)} -> missing fragment {link}")

manifest_path = DIST / "fidelity-manifest.json"
if not manifest_path.exists():
    errors.append("missing fidelity-manifest.json")
    manifest = {"articles": []}
else:
    manifest = json.loads(manifest_path.read_text())

for record in manifest.get("articles", []):
    route = record["route"]
    relative_html = "index.html" if route == "/" else f"{route.strip('/')}.html"
    file = DIST / relative_html
    if not file.exists():
        errors.append(f"fidelity route missing output: {route}")
        continue
    source = source_path(record["source"])
    if not source.exists():
        errors.append(f"fidelity source missing: {record['source']}")
        continue
    markdown = source.read_text()
    if digest(markdown) != record["sourceSha256"]:
        errors.append(f"{route} source digest does not match canonical Markdown")
    if digest(remove_document_title(markdown)) != record["articleSourceSha256"]:
        errors.append(f"{route} article source is not the canonical Markdown without its document title")
    body = article_html(html_by_path[file], record["source"])
    if body is None:
        errors.append(f"{route} has no article bound to {record['source']}")
        continue
    if digest(body) != record["renderedSha256"]:
        errors.append(f"{route} rendered canonical article differs from the fidelity manifest")
    parser = Page()
    parser.feed(f"<article>{body}</article>")
    for field in ("paragraphs", "tables", "listItems", "headings"):
        if parser.article_counts[field] != record[field]:
            errors.append(f"{route} {field}: rendered {parser.article_counts[field]}, canonical {record[field]}")
    semantics = ArticleSemantics()
    semantics.feed(body)
    for field, value in semantics.digests().items():
        if value != record[field]:
            errors.append(f"{route} {field} differs from canonical Markdown tokens")

manifest_routes = {record["route"] for record in manifest.get("articles", [])}
for file, html in html_by_path.items():
    sources = re.findall(r'<article\b[^>]*\bdata-source="([^"]+)"', html)
    route = "/" if file.name == "index.html" else f"/{file.relative_to(DIST).with_suffix('').as_posix()}"
    if len(sources) != 1:
        errors.append(f"{route} has {len(sources)} canonical article bindings (expected 1)")
    elif route not in manifest_routes:
        errors.append(f"{route} has a canonical article but no fidelity manifest entry")

if len(manifest_routes) != len(manifest.get("articles", [])):
    errors.append("fidelity manifest has duplicate route entries")

if manifest.get("articles"):
    sample = manifest["articles"][0]
    sample_file = DIST / ("index.html" if sample["route"] == "/" else f"{sample['route'].strip('/')}.html")
    sample_body = article_html(sample_file.read_text(), sample["source"])
    if sample_body:
        mutated = re.sub(r"(?<=>)([^<]*?)([A-Za-z])", lambda match: f">{match.group(1)}Z", sample_body, count=1)
        mutation_semantics = ArticleSemantics()
        mutation_semantics.feed(mutated)
        if (digest(mutated) == sample["renderedSha256"] or
                mutation_semantics.digests()["canonicalTextSha256"] == sample["canonicalTextSha256"]):
            errors.append("fidelity mutation self-test did not detect changed article text")

overview = ROOT / "content" / "00-ai-security.md"
overview_html = html_by_path.get(DIST / "index.html", "")
summary = re.search(r'<p class="hero-intro" data-overview-summary="true">([\s\S]*?)</p>', overview_html)
if not summary:
    errors.append("overview has no marked complete-sentence summary")
elif not overview.exists():
    errors.append("overview canonical source is missing")
else:
    visible = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", summary.group(1)))).strip()
    expected = first_story_paragraph(overview.read_text())
    if visible != expected:
        errors.append("overview summary does not match the first complete story paragraph")
    if visible.endswith("…") or not re.search(r"[.!?][\"')\]]?$", visible):
        errors.append("overview summary is not a complete sentence")
    title_match = re.search(r'<h1 id="ai-security" data-canonical-hero-title="true">([\s\S]*?)</h1>', overview_html)
    statement_match = re.search(r'<p class="hero-statement" data-canonical-hero-statement="true">([\s\S]*?)</p>', overview_html)
    expected_title = document_title(overview.read_text())
    expected_statement = canonical_hero_statement(overview.read_text())
    visible_title = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", title_match.group(1)))).strip() if title_match else ""
    visible_statement = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", statement_match.group(1)))).strip() if statement_match else ""
    if visible_title != expected_title:
        errors.append("overview hero title does not match the canonical document title or retain the ai-security anchor")
    if not expected_statement or visible_statement != expected_statement:
        errors.append("overview hero statement does not match the required canonical bold statement")

for path in DIST.rglob("*"):
    if path.is_file() and path.suffix in {".html", ".md", ".js", ".css", ".json"}:
        value = path.read_text()
        for marker in ("/Users/", "/mnt/mac/", "VERCEL_OIDC_TOKEN", "BEGIN PRIVATE KEY", "localhost:"):
            if marker in value:
                errors.append(f"private marker {marker} in {path.relative_to(DIST)}")

archive_errors: list[str] = []
archive_path = DIST / "downloads" / "ai-security-reference-architectures.zip"
if not archive_path.exists():
    archive_errors.append("clean reference package is missing")
else:
    with zipfile.ZipFile(archive_path) as archive:
        names = {entry.filename for entry in archive.infolist() if not entry.is_dir()}
        for source in sorted(name for name in names if name.endswith(".md")):
            text = archive.read(source).decode("utf-8")
            for target in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)", text):
                url = urlsplit(target.strip("<>"))
                if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
                    continue
                candidate = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(url.path)))
                if candidate.startswith("../") or candidate == "..":
                    archive_errors.append(f"{source} -> outside public package: {target}")
                elif candidate not in names:
                    archive_errors.append(f"{source} -> missing package file: {target}")
errors.extend(f"ZIP {error}" for error in archive_errors)

print(json.dumps({"pages": len(pages), "articles": len(manifest.get("articles", [])), "archiveErrors": archive_errors, "errors": errors}, indent=2))
raise SystemExit(bool(errors))
