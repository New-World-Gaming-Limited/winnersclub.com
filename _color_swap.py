#!/usr/bin/env python3
"""
Swap banned blue/purple/teal palette to gold/velvet brand palette.
Per user rule: NEVER use blue/purple/teal colors. Site palette is gold #FFD700 + velvet #8b0a1a.
"""
import re
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")

GOLD = "#FFD700"
GOLD_RGB = "255,215,0"
VELVET = "#8b0a1a"
VELVET_RGB = "139,10,26"
GOLD_DEEP = "#fa0"   # already used in gradients

# In style.css, do a complete remap:
# --blue:#0075ff      -> map to gold so any var(--blue) usage becomes gold
# --purple:#9b59b6    -> map to velvet
# Plus loose hex/rgba replacements

CSS_REPLACEMENTS = [
    # Token redefinitions
    ("--blue:#0075ff",   f"--blue:{GOLD}"),
    ("--purple:#9b59b6", f"--purple:{VELVET}"),
    # Gradient secondary blues
    ("#00d4ff", GOLD_DEEP),  # used in text-gradient
    ("#05c",   "#a07000"),    # darker gold for button shadow
    ("#39f",   GOLD),         # hover state
    # CTA banner background gradient was blue/purple
    ("#0a1628", "#1a0d0d"),   # dark velvet-tinted
    ("#1a0a2e", "#2a0a0e"),   # dark velvet-tinted
    # Loose purple hex
    ("#9b59b6", VELVET),
    ("#a855f7", VELVET),
    # rgba blues
    ("rgba(0,117,255,",  f"rgba({GOLD_RGB},"),
    # rgba purple variants
    ("rgba(155,89,182,", f"rgba({VELVET_RGB},"),
    ("rgba(168,85,247,", f"rgba({VELVET_RGB},"),
    # glow-blue shadow definition
    ("--glow-blue:0 0 30px rgba(0,117,255,0.4),0 0 60px rgba(0,117,255,0.2)",
     f"--glow-blue:0 0 30px rgba({GOLD_RGB},0.4),0 0 60px rgba({GOLD_RGB},0.2)"),
]

stats = {"css_replacements": 0, "html_files_changed": 0, "html_replacements": 0}

# --- CSS ---
css_path = ROOT / "style.css"
css = css_path.read_text(encoding="utf-8")
original = css
for old, new in CSS_REPLACEMENTS:
    count = css.count(old)
    if count:
        css = css.replace(old, new)
        stats["css_replacements"] += count
if css != original:
    css_path.write_text(css, encoding="utf-8")
    print(f"style.css: {stats['css_replacements']} replacements applied")

# --- HTML inline color swaps (rare but real, e.g. inline styles) ---
HTML_REPLACEMENTS = [
    ("#0075ff", GOLD),
    ("#9b59b6", VELVET),
    ("#a855f7", VELVET),
    ("rgba(0,117,255,",  f"rgba({GOLD_RGB},"),
    ("rgba(155,89,182,", f"rgba({VELVET_RGB},"),
    ("rgba(168,85,247,", f"rgba({VELVET_RGB},"),
]

for html in list(ROOT.rglob("*/index.html")) + [ROOT / "index.html", ROOT / "404.html"]:
    if not html.is_file() or "/skills/" in str(html):
        continue
    try:
        text = html.read_text(encoding="utf-8")
    except Exception:
        continue
    orig = text
    file_count = 0
    for old, new in HTML_REPLACEMENTS:
        c = text.count(old)
        if c:
            text = text.replace(old, new)
            file_count += c
    if text != orig:
        html.write_text(text, encoding="utf-8")
        stats["html_files_changed"] += 1
        stats["html_replacements"] += file_count

import json
print(json.dumps(stats, indent=2))
