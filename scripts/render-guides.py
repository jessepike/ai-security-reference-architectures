#!/usr/bin/env python3
"""Render the architect reference guides from their canonical Markdown.

This renderer deliberately reads only the named guide files and their
corresponding diagram PNGs.  It does not use any other workspace material.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    LongTable,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    TableStyle,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


ROOT = Path(__file__).resolve().parents[1]
GUIDES = (
    ("01-secure-business-ai-guide.md", "01-secure-business-ai.png", "01-secure-business-ai-guide.pdf"),
    ("02-defend-against-ai-guide.md", "02-defend-against-ai.png", "02-defend-against-ai-guide.pdf"),
    ("03-defend-with-ai-guide.md", "03-defend-with-ai.png", "03-defend-with-ai-guide.pdf"),
    ("04-ai-governance-guide.md", "04-ai-governance.png", "04-ai-governance-guide.pdf"),
)
NAVY = colors.HexColor("#102D46")
TEAL = colors.HexColor("#007D82")
MINT = colors.HexColor("#E5F4F2")
INK = colors.HexColor("#17232F")
SLATE = colors.HexColor("#506273")
LINE = colors.HexColor("#C9D5DD")
PALE = colors.HexColor("#F4F8FA")
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
FONT_REGULAR = "DejaVuSans"
FONT_BOLD = "DejaVuSans-Bold"
FONT_ITALIC = "DejaVuSans-Oblique"
CURRENT_ANCHORS: dict[str, str] = {}
CURRENT_MARKDOWN_DIR = ROOT
CURRENT_OUTPUT_DIR = ROOT


def register_fonts() -> None:
    """Use a Unicode-capable family available in the isolated dev VM."""
    if FONT_REGULAR not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont(FONT_REGULAR, str(FONT_DIR / "DejaVuSans.ttf")))
        pdfmetrics.registerFont(TTFont(FONT_BOLD, str(FONT_DIR / "DejaVuSans-Bold.ttf")))
        pdfmetrics.registerFont(TTFont(FONT_ITALIC, str(FONT_DIR / "DejaVuSans-Oblique.ttf")))
        pdfmetrics.registerFontFamily(
            FONT_REGULAR,
            normal=FONT_REGULAR,
            bold=FONT_BOLD,
            italic=FONT_ITALIC,
            boldItalic=FONT_BOLD,
        )


def inline_markdown(text: str) -> str:
    """Turn the useful subset of Markdown inline syntax into ReportLab XML."""
    text = html.escape(text.strip())
    def replace_link(match: re.Match) -> str:
        label, target = match.group(1), html.unescape(match.group(2))
        if target.startswith("#"):
            destination = CURRENT_ANCHORS.get(target[1:])
            if destination:
                return f'<a href="#{destination}" color="#007D82"><u>{label}</u></a>'
        if "://" not in target and not target.startswith("mailto:"):
            path_part, separator, fragment = target.partition("#")
            if path_part:
                package_target = (CURRENT_MARKDOWN_DIR / path_part).resolve()
                try:
                    rel = package_target.relative_to(ROOT / "content").as_posix()
                    if rel.endswith('.png'):
                        target = 'https://ai.jessepike.dev/images/' + Path(rel).name
                    elif rel.startswith('guides/'):
                        target = 'https://ai.jessepike.dev/' + rel.removesuffix('.md')
                    elif rel.startswith(('01-', '02-', '03-')):
                        target = 'https://ai.jessepike.dev/architectures/' + rel.removesuffix('.md')
                    elif rel == '00-ai-security.md':
                        target = 'https://ai.jessepike.dev/'
                    elif rel == '04-ai-governance.md':
                        target = 'https://ai.jessepike.dev/governance'
                    elif rel == 'guide-index.md':
                        target = 'https://ai.jessepike.dev/guides'
                    else:
                        target = 'https://ai.jessepike.dev/' + rel.removesuffix('.md')
                    if separator:
                        target += f"#{fragment}"
                except ValueError:
                    if package_target.is_relative_to(ROOT / 'public'):
                        target = 'https://ai.jessepike.dev/' + package_target.relative_to(ROOT / 'public').as_posix()
                        if separator:
                            target += f"#{fragment}"
        # Relative package links remain portable from output/pdf/, while web
        # references remain clickable URLs. Neither form exposes Markdown syntax.
        return f'<a href="{target}" color="#007D82"><u>{label}</u></a>'
    text = re.sub(r"\[([^]]+)\]\(([^ )]+)(?:\s+[^)]*)?\)", replace_link, text)
    text = re.sub(r"`([^`]+)`", rf'<font name="{FONT_REGULAR}">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*|__([^_]+)__", lambda m: f"<b>{m.group(1) or m.group(2)}</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)|(?<!_)_([^_]+)_(?!_)", lambda m: f"<i>{m.group(1) or m.group(2)}</i>", text)
    return text.replace("  ", " ")


@dataclass
class Block:
    kind: str
    value: object
    level: int = 0


def is_table_separator(line: str) -> bool:
    cells = [x.strip() for x in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def parse_markdown(markdown: str) -> list[Block]:
    lines = markdown.replace("\r\n", "\n").split("\n")
    blocks: list[Block] = []
    i = 0
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(Block("paragraph", " ".join(x.strip() for x in paragraph)))
            paragraph = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            i += 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", stripped)
        if heading:
            flush_paragraph()
            blocks.append(Block("heading", heading.group(2), len(heading.group(1))))
            i += 1
            continue
        if re.fullmatch(r"[-*_]{3,}", stripped):
            flush_paragraph()
            blocks.append(Block("rule", ""))
            i += 1
            continue
        image = re.fullmatch(r"!\[([^]]+)\]\([^)]+\)", stripped)
        if image:
            flush_paragraph()
            blocks.append(Block("image_alt", image.group(1)))
            i += 1
            continue
        if "|" in stripped and i + 1 < len(lines) and is_table_separator(lines[i + 1]):
            flush_paragraph()
            rows: list[list[str]] = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                if is_table_separator(lines[i]):
                    i += 1
                    continue
                rows.append([cell.strip() for cell in lines[i].strip().strip("|").split("|")])
                i += 1
            blocks.append(Block("table", rows))
            continue
        bullet = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.+)$", line)
        if bullet:
            flush_paragraph()
            indent = len(bullet.group(1).expandtabs(2)) // 2
            blocks.append(Block("list", (bullet.group(2), bullet.group(3)), indent))
            i += 1
            continue
        if stripped.startswith(">"):
            flush_paragraph()
            blocks.append(Block("quote", stripped.lstrip("> ")))
            i += 1
            continue
        paragraph.append(stripped)
        i += 1
    flush_paragraph()
    return blocks


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("GuideTitle", parent=base["Title"], fontName=FONT_BOLD, fontSize=19, leading=23, textColor=NAVY, alignment=TA_CENTER, spaceAfter=8),
        "subtitle": ParagraphStyle("GuideSubtitle", parent=base["Normal"], fontName=FONT_REGULAR, fontSize=11, leading=15, textColor=SLATE, alignment=TA_CENTER),
        "h1": ParagraphStyle("H1", parent=base["Heading1"], fontName=FONT_BOLD, fontSize=17, leading=22, textColor=NAVY, spaceBefore=14, spaceAfter=8, keepWithNext=True),
        "h2": ParagraphStyle("H2", parent=base["Heading2"], fontName=FONT_BOLD, fontSize=13, leading=17, textColor=TEAL, spaceBefore=12, spaceAfter=6, keepWithNext=True),
        "h3": ParagraphStyle("H3", parent=base["Heading3"], fontName=FONT_BOLD, fontSize=11.3, leading=14, textColor=NAVY, spaceBefore=10, spaceAfter=4, keepWithNext=True),
        "body": ParagraphStyle("Body", parent=base["BodyText"], fontName=FONT_REGULAR, fontSize=10.6, leading=15.1, textColor=INK, spaceAfter=8),
        "source_body": ParagraphStyle("SourceBody", parent=base["BodyText"], fontName=FONT_REGULAR, fontSize=10.0, leading=14.1, textColor=INK, spaceAfter=4),
        "bullet": ParagraphStyle("Bullet", parent=base["BodyText"], fontName=FONT_REGULAR, fontSize=10.4, leading=14.6, leftIndent=17, firstLineIndent=-11, bulletIndent=0, textColor=INK, spaceAfter=4),
        "source_bullet": ParagraphStyle("SourceBullet", parent=base["BodyText"], fontName=FONT_REGULAR, fontSize=9.2, leading=11.7, leftIndent=17, firstLineIndent=-11, bulletIndent=0, textColor=INK, spaceAfter=0),
        "quote": ParagraphStyle("Quote", parent=base["BodyText"], fontName=FONT_ITALIC, fontSize=10.5, leading=14.6, leftIndent=16, rightIndent=16, borderColor=TEAL, borderWidth=2, borderPadding=8, borderLeft=True, textColor=SLATE, spaceBefore=4, spaceAfter=8),
        "table": ParagraphStyle("Table", parent=base["BodyText"], fontName=FONT_REGULAR, fontSize=8.7, leading=11.3, textColor=INK),
        "tablehead": ParagraphStyle("TableHead", parent=base["BodyText"], fontName=FONT_BOLD, fontSize=8.6, leading=11.0, textColor=colors.white),
    }


class GuideDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and getattr(flowable, "_bookmark", None):
            key, title, level = flowable._bookmark
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level, closed=False)


def _footer(canvas, doc) -> None:
    canvas.saveState()
    w, _ = canvas._pagesize
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 0.46 * inch, w - doc.rightMargin, 0.46 * inch)
    canvas.setFont(FONT_REGULAR, 8)
    canvas.setFillColor(SLATE)
    canvas.drawString(doc.leftMargin, 0.28 * inch, "Architect reference guide  |  Review draft")
    canvas.drawRightString(w - doc.rightMargin, 0.28 * inch, f"{doc.page}")
    canvas.restoreState()


def _diagram_footer(canvas, doc) -> None:
    canvas.saveState()
    w, _ = canvas._pagesize
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 0.55 * inch, stroke=0, fill=1)
    canvas.setFont(FONT_REGULAR, 8)
    canvas.setFillColor(colors.white)
    canvas.drawString(0.55 * inch, 0.21 * inch, "Architect reference guide  |  Review draft")
    canvas.drawRightString(w - 0.55 * inch, 0.21 * inch, f"{doc.page}")
    canvas.restoreState()


def _title_from_blocks(blocks: Iterable[Block], fallback: str) -> str:
    for block in blocks:
        if block.kind == "heading" and block.level == 1:
            return str(block.value)
    return fallback


def heading_slug(text: str) -> str:
    clean = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"^-+|-+$", "", re.sub(r"[^a-z0-9]+", "-", clean))


def _table(rows: list[list[str]], styles: dict[str, ParagraphStyle], available_width: float) -> LongTable:
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    data = []
    for r, row in enumerate(normalized):
        style = styles["tablehead"] if r == 0 else styles["table"]
        data.append([Paragraph(inline_markdown(cell), style) for cell in row])
    column_widths = [available_width / width] * width
    table = LongTable(data, colWidths=column_widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def build_guide(markdown_path: Path, image_path: Path, output_path: Path) -> None:
    global CURRENT_ANCHORS, CURRENT_MARKDOWN_DIR, CURRENT_OUTPUT_DIR
    register_fonts()
    blocks = parse_markdown(markdown_path.read_text(encoding="utf-8"))
    if not blocks:
        raise ValueError(f"Guide is empty: {markdown_path}")
    title = _title_from_blocks(blocks, markdown_path.stem.replace("-", " ").title())
    CURRENT_MARKDOWN_DIR = markdown_path.parent
    CURRENT_OUTPUT_DIR = output_path.parent
    CURRENT_ANCHORS = {}
    heading_count = 0
    for block in blocks:
        if block.kind == "heading":
            heading_count += 1
            CURRENT_ANCHORS[heading_slug(str(block.value))] = f"h{heading_count}"
    styles = make_styles()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    portrait_w, portrait_h = letter
    diagram_w, diagram_h = landscape(letter)
    portrait_bottom = 0.55 * inch if markdown_path.name.startswith("03-") else 0.70 * inch
    doc = GuideDoc(
        str(output_path),
        pagesize=diagram_w and landscape(letter),
        leftMargin=0.68 * inch,
        rightMargin=0.68 * inch,
        topMargin=0.72 * inch,
        bottomMargin=portrait_bottom,
        title=title,
        author="",
        subject="Architect reference guide",
    )
    doc.addPageTemplates([
        PageTemplate("diagram", pagesize=(diagram_w, diagram_h), frames=[
            Frame(0.55 * inch, 0.74 * inch, diagram_w - 1.10 * inch, diagram_h - 1.33 * inch, id="diagram-frame")
        ], onPage=_diagram_footer),
        PageTemplate("portrait", pagesize=(portrait_w, portrait_h), frames=[
            Frame(0.68 * inch, portrait_bottom, portrait_w - 1.36 * inch, portrait_h - 0.72 * inch - portrait_bottom, id="portrait-frame")
        ], onPage=_footer),
    ])

    story = [
        Spacer(1, 0.10 * inch),
        Paragraph(inline_markdown(title), styles["title"]),
        Paragraph("High-level reference architecture", styles["subtitle"]),
        Spacer(1, 0.20 * inch),
    ]
    max_image_height = diagram_h - 2.55 * inch
    image = Image(
        str(image_path),
        width=diagram_w - 1.10 * inch,
        height=max_image_height,
        kind="proportional",
    )
    story.extend([image, Spacer(1, 0.12 * inch), Paragraph("Diagram for conversation and orientation; detailed guidance follows.", styles["subtitle"]), NextPageTemplate("portrait"), PageBreak()])

    heading_index = 0
    source_section = False
    width = portrait_w - 1.36 * inch
    for block in blocks:
        if block.kind == "heading":
            level = min(block.level, 3)
            heading_index += 1
            if level <= 2:
                source_section = "source" in str(block.value).lower()
            para = Paragraph(inline_markdown(str(block.value)), styles[f"h{level}"])
            para._bookmark = (f"h{heading_index}", str(block.value), level - 1)
            story.append(para)
        elif block.kind == "paragraph":
            paragraph_style = styles["source_body"] if source_section else styles["body"]
            story.append(Paragraph(inline_markdown(str(block.value)), paragraph_style))
        elif block.kind == "image_alt":
            pass  # The diagram is already present on the opening page.
        elif block.kind == "list":
            marker, item = block.value
            indent = "&nbsp;" * (block.level * 4)
            visible_marker = marker if str(marker)[0].isdigit() else "•"
            list_style = styles["source_bullet"] if source_section else styles["bullet"]
            story.append(Paragraph(f"{indent}<b>{visible_marker}</b>&nbsp;&nbsp;{inline_markdown(str(item))}", list_style))
        elif block.kind == "quote":
            story.append(Paragraph(inline_markdown(str(block.value)), styles["quote"]))
        elif block.kind == "table":
            story.extend([Spacer(1, 0.04 * inch), _table(block.value, styles, width), Spacer(1, 0.10 * inch)])
        elif block.kind == "rule":
            story.append(Spacer(1, 0.08 * inch))
    doc.build(story)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Render all guides.")
    parser.add_argument("--guide", choices=[g[0] for g in GUIDES], help="Render one guide by Markdown filename.")
    args = parser.parse_args()
    if not (args.all or args.guide):
        parser.error("select --all or --guide")
    selected = [g for g in GUIDES if args.all or g[0] == args.guide]
    for markdown, image, output in selected:
        markdown_path = ROOT / "content" / "guides" / markdown
        image_path = ROOT / "public" / "images" / image
        if not markdown_path.exists() or not image_path.exists():
            raise FileNotFoundError(f"Missing required input: {markdown_path if not markdown_path.exists() else image_path}")
        build_guide(markdown_path, image_path, ROOT / "public" / "downloads" / output)
        print(output)


if __name__ == "__main__":
    main()
