#!/usr/bin/env python3
"""Replace inline background-image: url(/images/*.webp) with AVIF version + add image-set fallback.

CSS image-set() syntax lets browsers pick the best format:
  background-image: image-set(url('/images/foo.avif') type('image/avif'), url('/images/foo.webp') type('image/webp'));
"""
from pathlib import Path
import re

ROOT = Path("/home/user/workspace/winnersclub.com")
IMG_DIR = ROOT / "images"

avif_set = {p.stem for p in IMG_DIR.glob("*.avif")}

# match: background[-image]: url('/images/foo.webp') ... | background: url('/images/foo.webp') ... (with single or double quotes)
bg_re = re.compile(r"""(background(?:-image)?\s*:\s*)(?:url\(['"]?)/images/([^'"./]+)\.webp(['"]?\))""")

count = 0
for p in ROOT.rglob("*.html"):
    s = str(p)
    if "/node_modules/" in s or "/.git/" in s or "/build_helpers/" in s or "/research/" in s:
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    orig = txt
    def repl(m):
        prop, name, close = m.group(1), m.group(2), m.group(3)
        if name in avif_set:
            return f"{prop}image-set(url('/images/{name}.avif') type('image/avif'), url('/images/{name}.webp') type('image/webp'))"
        return m.group(0)
    txt = bg_re.sub(repl, txt)
    if txt != orig:
        p.write_text(txt, encoding="utf-8")
        count += 1

print(f"Updated background-image AVIF on {count} html files")
