#!/usr/bin/env python3
"""Validate the built public site's local navigation, fragments and downloads."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for k in ('href','src'):
            if a.get(k):self.links.append(a[k])
pages={}
for f in DIST.rglob('*.html'):
    p=Page();p.feed(f.read_text());pages[f]=p
errors=[]
for f,p in pages.items():
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        base=DIST if u.path.startswith('/') else f.parent
        target=(base/unquote(u.path).lstrip('/')).resolve() if u.path else f
        if target.is_dir():
            target=(target/'index.html') if (target/'index.html').exists() else target.with_suffix('.html')
        if not target.exists() and not target.suffix:target=target.with_suffix('.html')
        if not target.exists():errors.append(f'{f.relative_to(DIST)} -> {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{f.relative_to(DIST)} -> missing fragment {link}')
for path in DIST.rglob('*'):
    if path.is_file() and path.suffix in {'.html','.md','.js','.css','.json'}:
        value=path.read_text()
        for marker in ('/Users/','/mnt/mac/','VERCEL_OIDC_TOKEN','BEGIN PRIVATE KEY','localhost:'):
            if marker in value:errors.append(f'Private marker {marker} in {path.relative_to(DIST)}')
print(json.dumps({'pages':len(pages),'errors':errors},indent=2))
raise SystemExit(bool(errors))
