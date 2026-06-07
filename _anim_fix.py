#!/usr/bin/env python3
"""Inject inline <script> to set .js-anim ASAP, and bump CSS cache version."""
import re, os, glob

OLD_V = "20260607g"
NEW_V = "20260607h"

INLINE = '<script>document.documentElement.classList.add("js-anim");</script>'

pages = []
for root, dirs, files in os.walk("."):
    if any(skip in root for skip in (".git", "node_modules", "__pycache__")):
        continue
    for f in files:
        if f.endswith(".html"):
            pages.append(os.path.join(root, f))

print(f"Processing {len(pages)} HTML files...")

changed = 0
for path in pages:
    with open(path, "r", encoding="utf-8") as fp:
        html = fp.read()

    orig = html

    # 1. Inject inline script right after <head> if not already there
    if 'classList.add("js-anim")' not in html:
        html = re.sub(r"(<head[^>]*>)", r"\1" + INLINE, html, count=1)

    # 2. Bump CSS cache version
    html = html.replace(f"style.min.css?v={OLD_V}", f"style.min.css?v={NEW_V}")
    html = html.replace(f"style.css?v={OLD_V}", f"style.css?v={NEW_V}")
    # also bump script.min.js if it has a version
    html = html.replace(f"script.min.js?v={OLD_V}", f"script.min.js?v={NEW_V}")

    if html != orig:
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(html)
        changed += 1

print(f"Updated {changed} files.")
