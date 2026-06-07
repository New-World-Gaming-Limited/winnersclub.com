#!/usr/bin/env python3
"""Convert background-image: url() and <img> references to use AVIF where available.
For background-image we can't use <picture> — instead we leave webp as-is (CSS doesn't
support format negotiation cleanly). For <img> tags we wrap in <picture>."""
from pathlib import Path
import re

ROOT = Path("/home/user/workspace/winnersclub.com")
IMG_DIR = ROOT / "images"

avif_set = {p.stem for p in IMG_DIR.glob("*.avif")}

# <img src="/images/foo.webp" ...> → <picture><source srcset="/images/foo.avif" type="image/avif"><img src="/images/foo.webp" ...></picture>
img_re = re.compile(r'<img([^>]*?)src="(/images/([^"./]+)\.webp)"([^>]*)>')

count = 0
for p in ROOT.rglob("*.html"):
    s = str(p)
    if "/node_modules/" in s or "/.git/" in s or "/build_helpers/" in s or "/research/" in s:
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    orig = txt
    def replace(m):
        pre, full, name, post = m.group(1), m.group(2), m.group(3), m.group(4)
        if name in avif_set:
            avif_url = f"/images/{name}.avif"
            return f'<picture><source srcset="{avif_url}" type="image/avif"><img{pre}src="{full}"{post}></picture>'
        return m.group(0)
    txt = img_re.sub(replace, txt)
    if txt != orig:
        p.write_text(txt, encoding="utf-8")
        count += 1

print(f"Wired AVIF into {count} html files")
