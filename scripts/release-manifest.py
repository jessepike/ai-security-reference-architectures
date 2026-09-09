#!/usr/bin/env python3
"""Record the public content/artifact hashes after validation and before commit."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
paths = {root / 'README.md', root / 'decisions.md'}
for pattern in ('content/**/*.md', 'public/images/*.png', 'public/downloads/*.pdf',
                'public/downloads/*.pptx', 'presentation/*.md', 'presentation/*.mjs'):
    paths.update(root.glob(pattern))
record = {
    'edition': '2026-09-integrated-security-and-governance-story',
    'status': 'Review draft',
    'scope': 'Source and artifact integrity; not architecture acceptance or deployed effectiveness.',
    'files': [
        {'path': path.relative_to(root).as_posix(), 'bytes': path.stat().st_size,
         'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        for path in sorted(paths)
    ],
}
target = root / 'docs/release-manifest.json'
target.write_text(json.dumps(record, indent=2) + '\n')
print(f'Recorded {len(record["files"])} source/artifact hashes in docs/release-manifest.json')
