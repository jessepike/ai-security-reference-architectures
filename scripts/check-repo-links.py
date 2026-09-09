#!/usr/bin/env python3
"""Check repository Markdown's relative file links outside generated site output."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re

root = Path(__file__).resolve().parents[1]
files = list(root.glob('*.md'))
for folder in ('content', 'docs', 'presentation'):
    files.extend((root / folder).rglob('*.md'))
errors = []
checked = 0
for source in files:
    for match in re.finditer(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', source.read_text()):
        target = urlsplit(match.group(1).strip('<>'))
        if target.scheme or target.netloc or not target.path:
            continue
        checked += 1
        resolved = (source.parent / unquote(target.path)).resolve()
        if not resolved.is_relative_to(root) or not resolved.exists():
            errors.append(f'{source.relative_to(root)} -> {match.group(1)}')
print(json.dumps({'relative_file_links': checked, 'errors': errors}, indent=2))
raise SystemExit(bool(errors))
