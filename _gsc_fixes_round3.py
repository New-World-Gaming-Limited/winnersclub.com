#!/usr/bin/env python3
"""
Round 3 GSC + UX fixes
1. Strip ALL remaining em/en dashes site-wide (body content, tables, FAQs)
2. Fix broken empty-comma <td>,</td> cells in /ja/casino, /ja/poker, /ko/promo-code
3. Fix desktop hero dead-space (padding-right:40% → 0) — addresses 72.7% desktop bounce
"""
import os, re, sys
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")

stats = {
    "files_changed": 0,
    "dashes_replaced": 0,
    "broken_cells_fixed": 0,
    "desktop_hero_fixed": 0,
}

# -------- 1. Strip dashes site-wide --------
# Replace en-dash (–) and em-dash (—) intelligently:
#  - " – " or " — "  -> ", "
#  - between numbers/letters "10–20" -> "10 to 20"  (we'll handle generically: replace with " to ")
#  - the bare "—" inside text -> ", "
# We'll do this only on HTML files, and only in body content (skip <script>/<style> safely by replacing all,
# since JSON-LD and CSS shouldn't have these characters).

DASHES = {"\u2013", "\u2014"}  # en-dash, em-dash

def strip_dashes(text: str) -> tuple[str, int]:
    count = 0
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in DASHES:
            count += 1
            # Look at left/right neighbours
            left = text[i-1] if i > 0 else ""
            right = text[i+1] if i+1 < len(text) else ""
            # Pattern: " – " or " — "
            if left == " " and right == " ":
                out.append(",")  # collapses to ", "
                i += 1
                continue
            # Numeric/word range: 10–20, A–Z, 2-4 days
            if (left.isalnum() and right.isalnum()):
                out.append(" to ")
                i += 1
                continue
            # Default: comma
            out.append(",")
            i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out), count

# -------- 2. Fix broken <td>,</td> cells --------
# These are visible empty cells with bare commas. Replace with em-dash equivalent then strip.
# But the proper fix is "—" → we want literal text. Use "N/A" or just empty styled cell.
BROKEN_TD_PATTERN = re.compile(r"<td>,</td>")

def fix_broken_cells(text: str) -> tuple[str, int]:
    new, n = BROKEN_TD_PATTERN.subn('<td style="color:var(--text-muted);">N/A</td>', text)
    return new, n

# -------- 3. Fix desktop hero padding --------
# style.css contains: .hero-content{...padding-right:40%}
def fix_desktop_hero(text: str) -> tuple[str, int]:
    # Only patch CSS files
    target = "max-width:var(--container);margin:0 auto;width:100%;text-align:left;padding-right:40%"
    replacement = "max-width:var(--container);margin:0 auto;width:100%;text-align:left;padding-right:0"
    if target in text:
        return text.replace(target, replacement), 1
    return text, 0

# -------- Run --------
html_files = list(ROOT.rglob("*/index.html")) + [ROOT / "index.html", ROOT / "404.html"]
html_files = [f for f in html_files if f.is_file() and "/skills/" not in str(f) and "/node_modules/" not in str(f)]

for path in html_files:
    try:
        original = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"skip {path}: {e}", file=sys.stderr)
        continue
    text = original
    text, d1 = strip_dashes(text)
    text, d2 = fix_broken_cells(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        stats["files_changed"] += 1
        stats["dashes_replaced"] += d1
        stats["broken_cells_fixed"] += d2

# CSS
css_path = ROOT / "style.css"
css = css_path.read_text(encoding="utf-8")
css2, d3 = fix_desktop_hero(css)
if d3:
    css_path.write_text(css2, encoding="utf-8")
    stats["files_changed"] += 1
    stats["desktop_hero_fixed"] = d3

import json
print(json.dumps(stats, indent=2))
