#!/usr/bin/env python3
"""Build the public Applying Secure Business AI guide from canonical Markdown."""

import hashlib
import html
import math
import os
import textwrap
from pathlib import Path
import re
import subprocess

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "applying-secure-business-ai.md"
GUIDE = ROOT / "content" / "guides" / "applying-secure-business-ai-guide.md"
ASSET_DIR = ROOT / "public" / "images"
DOWNLOAD_DIR = ROOT / "public" / "downloads"
TMP_DIR = ROOT / "tmp" / "application-render"


def clean_markdown(value):
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("**", "").replace("`", "").strip()


def section(text, heading, level=2):
    marks = "#" * level
    match = re.search(rf"^{marks} {re.escape(heading)}\s*$\n(.*?)(?=^{marks} |\Z)", text, re.M | re.S)
    if not match:
        raise ValueError(f"Missing canonical section: {heading}")
    return match.group(1).strip()


def bullets(body, heading):
    block = section(body, heading, 3)
    return [clean_markdown(line[2:]) for line in block.splitlines() if line.startswith("- ")]


def labeled(body, label):
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$", body, re.M)
    if not match:
        raise ValueError(f"Missing stage field: {label}")
    return clean_markdown(match.group(1))


def load_data():
    source = SOURCE.read_text()
    guide = GUIDE.read_text()
    stage_table = section(source, "The six progressive stages")
    compact = []
    for line in stage_table.splitlines():
        if re.match(r"^\| \*\*[0-5] ", line):
            compact.append([clean_markdown(cell) for cell in line.strip("|").split("|")])
    if len(compact) != 6:
        raise ValueError(f"Expected six compact stage rows, found {len(compact)}")
    stages = []
    for number, row in enumerate(compact):
        name = re.sub(r"^[0-5]\s+", "", row[0])
        body = section(guide, f"Stage {number} — {name}")
        intro = clean_markdown(body.split("\n\n", 1)[0])
        stages.append({
            "number": str(number), "name": name,
            "business_goal": intro,
            "security_help": row[2], "before_expansion": row[4],
            "overview_goal": labeled(body, "Overview business goal"),
            "overview_help": labeled(body, "Overview security help"),
            "overview_ready": labeled(body, "Overview for next decision"),
            "decision": labeled(body, "Decision"),
            "understand": bullets(body, "What must be understood"),
            "outcomes": bullets(body, "Security outcomes"),
            "work": bullets(body, "Security support"),
            "deliverables": bullets(body, "Candidate deliverables"),
            "checklist": bullets(body, "Checklist"),
            "evidence": labeled(body, "Evidence"),
            "example": labeled(body, "Running example"),
        })
    coverage = []
    for line in section(guide, "Coverage across the journey").splitlines():
        if line.startswith("|") and not line.startswith(("| Concern", "|---")):
            coverage.append([clean_markdown(cell) for cell in line.strip("|").split("|")])
    how_to = []
    how_body = section(guide, "How to use the framework")
    for block in re.split(r"(?m)^### ", how_body)[1:]:
        title, body = block.split("\n", 1)
        items = [clean_markdown(line[2:]) for line in body.splitlines() if line.startswith("- ")]
        how_to.append({"title": clean_markdown(title), "items": items})
    if len(how_to) != 4:
        raise ValueError(f"Expected four how-to blocks, found {len(how_to)}")
    limits = section(guide, "Sources and limits")
    outcome_body = section(source, "The outcome approach")
    outcome_match = re.search(r"^\*\*(Intended business change.+reassessment\.)\*\*$", outcome_body, re.M)
    if not outcome_match:
        raise ValueError("Missing canonical outcome chain")
    return {
        "title": "Applying Secure Business AI",
        "subtitle": "How security supports business-led AI development and transformation",
        "state": "Proposed neutral application companion | Review draft | 14 September 2026",
        "approach": clean_markdown(outcome_match.group(1)),
        "how_to": how_to,
        "shared_foundations": clean_markdown(section(guide, "Shared foundations")),
        "source_limits": {
            "source": labeled(limits, "Source"),
            "status": bullets(limits, "Status"),
            "interpretation": bullets(limits, "Interpretation"),
            "pending": bullets(limits, "Still to be assessed"),
        },
        "stages": stages, "coverage": coverage,
    }


DATA = load_data()
W, H = 13.333 * inch, 7.5 * inch
NAVY = HexColor("#102B3F")
NAVY_2 = HexColor("#183F59")
TEAL = HexColor("#0A7C78")
TEAL_2 = HexColor("#12A6A0")
PALE = HexColor("#EAF6F5")
BLUE_PALE = HexColor("#EEF4F7")
INK = HexColor("#17242E")
MUTED = HexColor("#536875")
LINE = HexColor("#C9D8DE")
WHITE = white


def safe(s):
    return html.escape(str(s), quote=True)


def wrap_pdf(text, font, size, width):
    words = str(text).split()
    lines, current = [], ""
    for word in words:
        trial = word if not current else current + " " + word
        if stringWidth(trial, font, size) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_text(c, text, x, y, width, size=10, color=INK, font="Helvetica", leading=None, max_lines=None):
    leading = leading or size * 1.28
    lines = wrap_pdf(text, font, size, width)
    if max_lines and len(lines) > max_lines:
        raise ValueError(f"Text overflow ({len(lines)} lines > {max_lines}): {text}")
    c.setFillColor(color)
    c.setFont(font, size)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullets(c, items, x, y, width, size=8.4, leading=10.5, gap=3, color=INK):
    for item in items:
        c.setFillColor(TEAL)
        c.circle(x + 2, y + 2.2, 1.6, fill=1, stroke=0)
        y = draw_text(c, item, x + 11, y, width - 11, size=size, color=color, leading=leading)
        y -= gap
    return y


def footer(c, page_no, label="APPLYING SECURE BUSINESS AI"):
    c.setStrokeColor(LINE)
    c.line(36, 25, W - 36, 25)
    c.setFont("Helvetica", 6.5)
    c.setFillColor(MUTED)
    c.drawString(36, 13, "PROPOSED NEUTRAL APPLICATION COMPANION | REVIEW DRAFT | 14 SEPTEMBER 2026")
    c.drawRightString(W - 36, 13, f"{label}  |  {page_no}")


def footer_at(c, page_no, page_w, label="APPLYING SECURE BUSINESS AI"):
    c.setStrokeColor(LINE); c.line(36, 25, page_w - 36, 25)
    c.setFont("Helvetica", 6.5); c.setFillColor(MUTED)
    c.drawString(36, 13, "PROPOSED NEUTRAL APPLICATION COMPANION | REVIEW DRAFT | 14 SEPTEMBER 2026")
    c.drawRightString(page_w - 36, 13, f"{label}  |  {page_no}")


def page_title(c, eyebrow, title, sub=None):
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(36, H - 34, eyebrow.upper())
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 23)
    c.drawString(36, H - 61, title)
    if sub:
        draw_text(c, sub, 36, H - 79, W - 72, size=8.3, color=MUTED, leading=10)


def card(c, x, y, w, h, title, fill=WHITE, stroke=LINE, title_color=TEAL):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    c.setFillColor(title_color)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(x + 12, y + h - 17, title.upper())


def svg_wrap(text, chars):
    return textwrap.wrap(text, width=chars, break_long_words=False, break_on_hyphens=False)


def build_overview_svg():
    stages = DATA["stages"]
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">',
        '<rect width="1920" height="1080" fill="#ffffff"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif}.title{font-size:58px;font-weight:700;fill:#102B3F}.sub{font-size:24px;fill:#536875}.num{font-size:34px;font-weight:700;fill:#ffffff}.stage{font-size:21px;font-weight:700;fill:#ffffff}.label{font-size:14px;font-weight:700;fill:#0A7C78;letter-spacing:1px}.body{font-size:17px;fill:#17242E}.small{font-size:15px;fill:#536875}.foot{font-size:14px;fill:#536875}</style>',
        f'<text x="72" y="82" class="title">{safe(DATA["title"])}</text>',
        f'<text x="72" y="121" class="sub">{safe(DATA["subtitle"])}</text>',
        '<rect x="72" y="150" width="1776" height="52" rx="12" fill="#102B3F"/>',
        f'<text x="960" y="183" text-anchor="middle" font-size="19" fill="#ffffff">{safe(DATA["approach"])}</text>'
    ]
    gap, x0, total = 14, 72, 1776
    cw = (total - gap * 5) / 6
    colors = ["#0A7C78", "#0B8883", "#0D918C", "#119B95", "#17908F", "#176E79"]
    for i, s in enumerate(stages):
        x = x0 + i * (cw + gap)
        out += [f'<rect x="{x:.1f}" y="230" width="{cw:.1f}" height="626" rx="16" fill="#F8FBFC" stroke="#C9D8DE" stroke-width="2"/>',
                f'<rect x="{x:.1f}" y="230" width="{cw:.1f}" height="78" rx="16" fill="{colors[i]}"/>',
                f'<rect x="{x:.1f}" y="286" width="{cw:.1f}" height="22" fill="{colors[i]}"/>',
                f'<text x="{x+18:.1f}" y="281" class="num">{s["number"]}</text>']
        name_lines = svg_wrap(s["name"], 18)
        for j, line in enumerate(name_lines):
            out.append(f'<text x="{x+66:.1f}" y="261" class="stage" fill="#ffffff">{safe(line)}</text>')
            if j:
                out[-1] = f'<text x="{x+66:.1f}" y="{261+j*23}" font-size="21" font-weight="700" fill="#ffffff">{safe(line)}</text>'
        yy = 342
        for label, key, maxchars in [("BUSINESS GOAL", "overview_goal", 24), ("SECURITY HELPS", "overview_help", 24), ("FOR NEXT DECISION", "overview_ready", 24)]:
            out.append(f'<text x="{x+18:.1f}" y="{yy}" class="label">{label}</text>')
            yy += 28
            for line in svg_wrap(s[key], maxchars):
                out.append(f'<text x="{x+18:.1f}" y="{yy}" class="body">{safe(line)}</text>')
                yy += 23
            yy += 20
    out += [
        '<rect x="72" y="884" width="1776" height="92" rx="15" fill="#EAF6F5" stroke="#A9D8D5" stroke-width="2"/>',
        '<text x="96" y="918" class="label">ONE LIVING RECORD ACROSS THE JOURNEY</text>',
        '<text x="96" y="951" font-size="22" fill="#17242E">Facts  |  value  |  consequences  |  conditions  |  obligations  |  controls  |  evidence  |  decisions  |  change</text>',
        '<text x="960" y="998" text-anchor="middle" class="small">Stages describe an AI effort; governance responsibilities apply throughout.</text>',
        '<text x="960" y="1020" text-anchor="middle" class="small">Material change or new evidence can reopen earlier work.</text>',
        '<path d="M 1740 1034 C 1560 1052, 380 1052, 190 1034" fill="none" stroke="#0A7C78" stroke-width="4"/>',
        '<path d="M 190 1028 l 18 8 l -4 -20 z" fill="#0A7C78"/>',
        '<text x="1848" y="1063" text-anchor="end" class="foot">Proposed neutral application companion | Review draft | 14 September 2026</text>',
        '</svg>'
    ]
    (ROOT / "secure-business-ai-overview.svg").write_text("\n".join(out))


def overview_page(c, page_no=1):
    c.setFillColor(WHITE); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 28); c.drawString(36, H-42, DATA["title"])
    c.setFillColor(MUTED); c.setFont("Helvetica", 11); c.drawString(36, H-60, DATA["subtitle"])
    c.setFillColor(NAVY); c.roundRect(36, H-100, W-72, 27, 6, fill=1, stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica", 7.7); c.drawCentredString(W/2, H-90, DATA["approach"])
    x0, gap, y, h = 36, 7, 115, 305
    cw = (W-72-gap*5)/6
    stage_colors = [TEAL, HexColor("#0B8883"), HexColor("#0D918C"), HexColor("#119B95"), HexColor("#178B8B"), HexColor("#176E79")]
    for i, s in enumerate(DATA["stages"]):
        x = x0+i*(cw+gap)
        c.setFillColor(HexColor("#F8FBFC")); c.setStrokeColor(LINE); c.roundRect(x,y,cw,h,7,fill=1,stroke=1)
        c.setFillColor(stage_colors[i]); c.roundRect(x,y+h-42,cw,42,7,fill=1,stroke=0); c.rect(x,y+h-42,cw,8,fill=1,stroke=0)
        c.setFillColor(WHITE); c.setFont("Helvetica-Bold",15); c.drawString(x+9,y+h-27,s["number"])
        draw_text(c,s["name"],x+31,y+h-21,cw-37,size=8,color=WHITE,font="Helvetica-Bold",leading=9,max_lines=2)
        yy=y+h-61
        for label,key in [("BUSINESS GOAL","overview_goal"),("SECURITY HELPS","overview_help"),("FOR NEXT DECISION","overview_ready")]:
            c.setFillColor(TEAL); c.setFont("Helvetica-Bold",6); c.drawString(x+9,yy,label); yy-=11
            yy=draw_text(c,s[key],x+9,yy,cw-18,size=9.1,leading=11.2,max_lines=6); yy-=16
    c.setFillColor(PALE); c.setStrokeColor(HexColor("#A9D8D5")); c.roundRect(36,58,W-72,55,7,fill=1,stroke=1)
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold",6.4); c.drawString(48,98,"ONE LIVING RECORD ACROSS THE JOURNEY")
    c.setFillColor(INK); c.setFont("Helvetica",7.7); c.drawString(48,82,"Facts  |  value  |  consequences  |  conditions  |  obligations  |  controls  |  evidence  |  decisions  |  change")
    c.setFillColor(MUTED); c.setFont("Helvetica",6.8); c.drawCentredString(W/2,66,"Stages describe an AI effort; governance responsibilities apply throughout.")
    c.setFillColor(MUTED); c.setFont("Helvetica",7); c.drawCentredString(W/2,47,"Material change or new evidence can reopen earlier work.")
    c.setStrokeColor(TEAL); c.setLineWidth(1.8); c.line(W-108,36,96,36); c.line(96,36,103,40); c.line(96,36,103,32)
    footer(c,page_no,"APPLYING SECURE BUSINESS AI | OVERVIEW")


def how_to_page(c, n):
    page_title(c,"How to use the framework","Start with the decision, then scale the work","One common approach fits built, bought, embedded and already-operating AI. Depth follows exposure and uncertainty.")
    cols=[]
    for idx, block in enumerate(DATA["how_to"]):
        cols.append((36 if idx % 2 == 0 else W/2+8, block["title"], block["items"]))
    for idx,(x,title,items) in enumerate(cols):
        y=280 if idx<2 else 83
        card(c,x,y,W/2-50,165,title,fill=BLUE_PALE if idx%2==0 else PALE)
        draw_bullets(c,items,x+14,y+126,W/2-78,size=9,leading=12,gap=6)
    draw_text(c,"SHARED FOUNDATIONS: "+DATA["shared_foundations"],36,69,W-72,size=6.8,color=MUTED,font="Helvetica-Bold",leading=8,max_lines=2)
    footer(c,n)


def stage_page(c,s,n):
    pw, ph = letter
    c.setFillColor(WHITE); c.rect(0,0,pw,ph,fill=1,stroke=0)
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold",9); c.drawString(36,ph-34,f'STAGE {s["number"]}')
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold",25); c.drawString(36,ph-61,s["name"])
    draw_text(c,s["business_goal"],36,ph-82,pw-72,size=10,color=MUTED,leading=12,max_lines=2)
    c.setFillColor(NAVY); c.roundRect(36,ph-154,pw-72,52,7,fill=1,stroke=0)
    c.setFillColor(TEAL_2); c.setFont("Helvetica-Bold",7.5); c.drawString(49,ph-118,"DECISION")
    draw_text(c,s["decision"],49,ph-133,pw-98,size=8.1,color=WHITE,leading=9.2,max_lines=3)
    left, right, colw = 36, 316, 260
    # Two readable columns with fixed, non-overlapping cards.
    card(c,left,389,colw,241,"What must be understood",fill=BLUE_PALE)
    draw_bullets(c,s["understand"],left+14,594,colw-28,size=9.5,leading=12,gap=6)
    card(c,left,142,colw,232,"Security outcomes",fill=PALE)
    yy=draw_bullets(c,s["outcomes"],left+14,338,colw-28,size=9.7,leading=12.3,gap=7)
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold",8); c.drawString(left+14,yy-1,"EVIDENCE")
    draw_text(c,s["evidence"],left+14,yy-15,colw-28,size=9,color=MUTED,leading=11,max_lines=6)
    card(c,right,389,colw,241,"Security support and deliverables",fill=WHITE)
    yy=draw_bullets(c,s["work"],right+14,594,colw-28,size=9.2,leading=11.5,gap=5)
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold",8); c.drawString(right+14,yy-1,"CANDIDATE DELIVERABLES")
    draw_text(c," | ".join(s["deliverables"]),right+14,yy-16,colw-28,size=8.7,color=MUTED,leading=10.8,max_lines=7)
    card(c,right,142,colw,232,"Checklist",fill=WHITE)
    draw_bullets(c,s["checklist"],right+14,338,colw-28,size=9.1,leading=11.4,gap=4)
    c.setFillColor(NAVY); c.roundRect(36,45,pw-72,82,7,fill=1,stroke=0)
    c.setFillColor(TEAL_2); c.setFont("Helvetica-Bold",8); c.drawString(49,105,"ILLUSTRATIVE EXAMPLE | INVENTED, NOT TEST EVIDENCE")
    draw_text(c,s["example"],49,88,pw-98,size=9.1,color=WHITE,leading=11.2,max_lines=4)
    footer_at(c,n,pw)


def matrix_page(c,n):
    page_title(c,"Coverage across the journey","Follow every concern across the stages","The map tests coverage. Each effort applies only the depth justified by its exposure, uncertainty and decision.")
    x0,y0=36,61; table_w=W-72; head_h=54
    row_h=min(42, 336/len(DATA["coverage"]))
    first=130; sw=(table_w-first)/6
    table_top=y0+len(DATA["coverage"])*row_h
    c.setFillColor(NAVY); c.rect(x0,table_top,table_w,head_h,fill=1,stroke=0)
    c.setFillColor(WHITE); c.setFont("Helvetica-Bold",9); c.drawString(x0+8,table_top+22,"CONCERN")
    for j,s in enumerate(DATA["stages"]):
        draw_text(c,s["number"]+" "+s["name"],x0+first+j*sw+6,table_top+32,sw-10,size=9,color=WHITE,font="Helvetica-Bold",leading=10.5,max_lines=3)
    for i,row in enumerate(DATA["coverage"]):
        y=y0+(len(DATA["coverage"])-1-i)*row_h
        c.setFillColor(BLUE_PALE if i%2==0 else WHITE); c.rect(x0,y,table_w,row_h,fill=1,stroke=0)
        c.setStrokeColor(LINE); c.rect(x0,y,table_w,row_h,fill=0,stroke=1)
        c.setFillColor(NAVY); c.setFont("Helvetica-Bold",9); draw_text(c,row[0],x0+7,y+27,first-12,size=9,color=NAVY,font="Helvetica-Bold",leading=10.5,max_lines=3)
        for j,cell in enumerate(row[1:]):
            draw_text(c,cell,x0+first+j*sw+5,y+27,sw-9,size=9,color=INK,leading=10.5,max_lines=3)
    footer(c,n)


def sources_page(c,n):
    page_title(c,"Sources and limits","What this package establishes","This guide presents a proposed neutral application companion for review. Its labels preserve the authority of the canonical sources.")
    card(c,36,264,W*0.54,180,"Source and status",fill=BLUE_PALE)
    items=[DATA["source_limits"]["source"]]+DATA["source_limits"]["status"]
    draw_bullets(c,items,51,410,W*0.54-30,size=8.6,leading=11,gap=6)
    card(c,W*0.58,95,W*0.42-36,349,"Interpretation",fill=PALE)
    items2=DATA["source_limits"]["interpretation"]
    draw_bullets(c,items2,W*0.58+15,410,W*0.42-66,size=8.5,leading=10.8,gap=6)
    card(c,36,95,W*0.54,146,"What remains to be tested",fill=WHITE)
    remaining=DATA["source_limits"]["pending"]
    draw_bullets(c,remaining,51,205,W*0.54-30,size=8.6,leading=10.8,gap=5)
    footer(c,n)


def build_pdfs():
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    p=canvas.Canvas(str(DOWNLOAD_DIR/"applying-secure-business-ai-overview.pdf"),pagesize=(W,H),pageCompression=1)
    p.setTitle("Applying Secure Business AI overview")
    overview_page(p,1); p.showPage(); p.save()
    g=canvas.Canvas(str(DOWNLOAD_DIR/"applying-secure-business-ai-guide.pdf"),pagesize=(W,H),pageCompression=1)
    g.setTitle("Applying Secure Business AI guide")
    overview_page(g,1); g.showPage()
    how_to_page(g,2); g.showPage()
    for i,s in enumerate(DATA["stages"],start=3):
        g.setPageSize(letter); stage_page(g,s,i); g.showPage()
    g.setPageSize((W,H))
    matrix_page(g,9); g.showPage()
    sources_page(g,10); g.showPage(); g.save()


def main():
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    build_overview_svg()
    generated_svg = ROOT / "secure-business-ai-overview.svg"
    public_svg = ASSET_DIR / "applying-secure-business-ai.svg"
    generated_svg.replace(public_svg)
    subprocess.run([
        "rsvg-convert", "--width", "1920", "--height", "1080",
        "--output", str(ASSET_DIR / "applying-secure-business-ai.png"), str(public_svg),
    ], check=True)
    build_pdfs()


if __name__ == "__main__":
    main()
