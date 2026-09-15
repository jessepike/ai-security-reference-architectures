from pathlib import Path
from html import escape
import textwrap

ROOT = Path(__file__).parent
W, H = 1920, 1080

NAVY = "#092A43"
NAVY_2 = "#123B55"
TEAL = "#008C86"
TEAL_2 = "#159B95"
PALE = "#EAF5F5"
MIST = "#F2F6F8"
LINE = "#BCD1D8"
INK = "#102F43"
MUTED = "#577080"
WHITE = "#FFFFFF"


def text(x, y, value, size, *, color=INK, weight=400, family="Arial", anchor="start", tracking=0):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" letter-spacing="{tracking}">{escape(value)}</text>'


def wrapped(x, y, value, width_chars, size, *, color=INK, weight=400, line_height=1.28):
    lines = textwrap.wrap(value, width=width_chars, break_long_words=False, break_on_hyphens=False)
    result = []
    for i, line in enumerate(lines):
        result.append(text(x, y + i * size * line_height, line, size, color=color, weight=weight))
    return result, y + max(0, len(lines) - 1) * size * line_height


def card(x, number, title, status, status_color, items, footer):
    y, width, height = 235, 390, 520
    parts = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="24" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>',
        f'<path d="M {x+24} {y} H {x+width-24} Q {x+width} {y} {x+width} {y+24} V {y+102} H {x} V {y+24} Q {x} {y} {x+24} {y}" fill="{status_color}"/>',
        f'<circle cx="{x+42}" cy="{y+46}" r="22" fill="{WHITE}" fill-opacity=".18"/>',
        text(x+42, y+54, str(number), 23, color=WHITE, weight=700, anchor="middle"),
        text(x+76, y+42, status.upper(), 15, color=WHITE, weight=700, tracking=1.5),
        text(x+76, y+77, title, 27, color=WHITE, weight=700),
    ]
    cy = y + 143
    for item in items:
        parts.append(f'<circle cx="{x+31}" cy="{cy-6}" r="5" fill="{TEAL}"/>')
        lines, bottom = wrapped(x+48, cy, item, 37, 20, color=INK, line_height=1.3)
        parts.extend(lines)
        cy = bottom + 43
    parts.append(f'<line x1="{x+26}" y1="{y+height-70}" x2="{x+width-26}" y2="{y+height-70}" stroke="{LINE}"/>')
    foot, _ = wrapped(x+28, y+height-38, footer, 44, 15, color=MUTED, weight=600, line_height=1.15)
    parts.extend(foot)
    return parts


svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    f'<rect width="{W}" height="{H}" fill="{MIST}"/>',
    f'<rect x="0" y="0" width="{W}" height="180" fill="{NAVY}"/>',
    text(105, 67, "DEVELOPMENT ROADMAP", 17, color="#7DE0D8", weight=700, tracking=2.4),
    text(105, 122, "AI Security & Governance", 43, color=WHITE, weight=700),
    text(1815, 66, "SNAPSHOT", 14, color="#A9C8D5", weight=700, anchor="end", tracking=1.5),
    text(1815, 99, "15 September 2026", 21, color=WHITE, weight=600, anchor="end"),
    text(105, 157, "A recommended order for building confidence, learning from use and extending the public reference.", 21, color="#D7E7EC"),
]

cards = [
    (80, 1, "Reference foundation", "Established + live", TEAL, [
        "Three peer security views plus AI Governance",
        "Canonical sources, guides and five maps",
        "Editable presentation and public website",
    ], "Maintained shared reference"),
    (530, 2, "Application + CISO use", "Live", TEAL_2, [
        "Full six-stage application companion",
        "CISO walkthrough for a safe first experiment",
        "Stage 0 starter tools and Stage 1 handoff",
    ], "Practical entry point into the reference"),
    (980, 3, "Confidence + learning", "Recommended next", NAVY_2, [
        "Resolve 30 original review findings",
        "Human architecture review and CISO comprehension",
        "Public-writing cleanup and reuse terms",
    ], "Recommended before expanding playbooks"),
    (1430, 4, "Scoped application", "Future", "#506B7A", [
        "Select one real workflow and environment",
        "Learn, review and record any source change",
        "Authorize downstream adaptations separately",
    ], "Scope and authorization required"),
]
for c in cards:
    svg.extend(card(*c))

# Direction arrows; explicitly recommendations rather than dependencies.
for x in (470, 920, 1370):
    svg.append(f'<path d="M {x} 495 H {x+38}" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>')
    svg.append(f'<path d="M {x+28} 485 L {x+40} 495 L {x+28} 505" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')

svg.extend([
    f'<rect x="80" y="790" width="1760" height="180" rx="22" fill="{PALE}" stroke="#9DCFCB" stroke-width="2"/>',
    text(112, 835, "OPTIONAL EXPANSION FROM DISCUSSION", 14, color=TEAL, weight=700, tracking=1.7),
    text(112, 876, "Additional stage-specific playbooks", 27, color=NAVY, weight=700),
    text(112, 906, "Discover and guardrail  •  Pilot  •  Develop", 19, color=INK, weight=600),
    text(112, 934, "Production transition  •  Operate", 19, color=INK, weight=600),
    text(112, 963, "Proposal only. Reconsider after reader learning and a scoped real-workflow exploration; no work is commissioned.", 16, color=MUTED),
    f'<rect x="1504" y="833" width="300" height="78" rx="16" fill="{WHITE}" stroke="#9DCFCB"/>',
    text(1654, 865, "KEEP THE MODELS DISTINCT", 12, color=TEAL, weight=700, anchor="middle", tracking=1.2),
    text(1654, 887, "4 development workstreams", 16, color=NAVY, weight=700, anchor="middle"),
    text(1654, 908, "6 AI project stages", 16, color=NAVY, weight=700, anchor="middle"),
    text(80, 995, "Arrows show recommended order for learning, not dependencies, delivery dates or commitments.", 16, color=MUTED, weight=600),
    text(1840, 995, "Sources: ROADMAP.md · BACKLOG.md · production verification", 14, color=MUTED, anchor="end"),
    text(1840, 1034, "Discussion artifact · development roadmap", 14, color=MUTED, anchor="end"),
    "</svg>",
])

(ROOT / "development-roadmap.svg").write_text("\n".join(svg) + "\n")
print(ROOT / "development-roadmap.svg")
