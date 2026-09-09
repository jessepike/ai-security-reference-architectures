#!/usr/bin/env python3
"""Record the public content/artifact hashes after validation and before commit."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
paths = {root / 'README.md', root / 'decisions.md'}
project_records = (
    'intent.md', 'PURPOSE.md', 'AGENTS.md', 'CLAUDE.md', 'ROADMAP.md',
    'BACKLOG.md', 'status.md', 'lessons.md', 'docs/downstream-use.md',
    'docs/downstream-register.md', 'docs/exploration/README.md',
)
paths.update(root / name for name in project_records)
for pattern in ('content/**/*.md', 'public/images/*.png', 'public/downloads/*.pdf',
                'public/downloads/*.pptx', 'presentation/*.md', 'presentation/*.mjs'):
    paths.update(root.glob(pattern))
record = {
    'edition': '2026-09-canonical-package-alignment',
    'status': 'Review draft',
    'scope': 'Canonical content, project records and artifact integrity; not architecture acceptance or deployed effectiveness.',
    'files': [
        {'path': path.relative_to(root).as_posix(), 'bytes': path.stat().st_size,
         'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        for path in sorted(paths)
    ],
}
target = root / 'docs/release-manifest.json'
target.write_text(json.dumps(record, indent=2) + '\n')
print(f'Recorded {len(record["files"])} source/artifact hashes in docs/release-manifest.json')
