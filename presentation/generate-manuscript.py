#!/usr/bin/env python3
"""Create a human-readable slide and speaker-note review copy from a PPTX."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def texts_from_part(archive: zipfile.ZipFile, name: str) -> list[str]:
    root = ET.fromstring(archive.read(name))
    values: list[str] = []
    for paragraph in root.findall(".//a:p", NS):
        value = "".join(node.text or "" for node in paragraph.findall(".//a:t", NS)).strip()
        if value:
            values.append(value)
    return values


def natural_key(name: str) -> int:
    match = re.search(r"(\d+)", name)
    return int(match.group(1)) if match else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="PPTX input path")
    parser.add_argument("--output", required=True, type=Path, help="Markdown output path")
    args = parser.parse_args()

    with zipfile.ZipFile(args.input) as archive:
        slide_names = sorted(
            (name for name in archive.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=natural_key,
        )
        note_names = {
            natural_key(name): name
            for name in archive.namelist()
            if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)
        }
        lines = [
            "# AI Security Reference Architectures — presentation manuscript",
            "",
            "Derived from the exported PPTX. Review draft. Edit the canonical architecture sources and deck builder before regenerating this review copy.",
            "",
        ]
        for index, slide_name in enumerate(slide_names, start=1):
            lines.extend([f"## Slide {index}", "", *texts_from_part(archive, slide_name), ""])
            notes = texts_from_part(archive, note_names.get(index, "")) if index in note_names else []
            lines.extend(["### Speaker notes", "", *(notes or ["No speaker notes present."]), ""])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
