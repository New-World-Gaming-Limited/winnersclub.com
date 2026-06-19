#!/usr/bin/env python3
"""Round 2 cleanup: fix broken JS, strip remaining /nl/ option entries with full URL format."""
import re
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")
stats = {"html_files_changed": 0, "switcher_removed": 0, "js_fixed": 0}

# Fix broken JS: 'NL':'BE': → (nothing) and remove the orphan comment
lr = ROOT / "lang-redirect.js"
js = lr.read_text(encoding="utf-8")
original = js
# Remove the broken construct and orphaned Dutch comment
js = re.sub(r"\s*//\s*Dutch[^\n]*\n", "\n", js)
js = js.replace("'NL':'BE':", "")
# Defensive: any residual ''nl'' or empty NL entries
js = re.sub(r"\s*'NL':\s*,?", "", js)
js = re.sub(r"\s*'BE':\s*,?", "", js)
if js != original:
    lr.write_text(js, encoding="utf-8")
    stats["js_fixed"] = 1

# Strip remaining /nl/ option entries — match BOTH full-URL and relative paths,
# and BOTH "Nederlands" and "Nederlands (Dutch)" labels
SWITCHER_PATTERNS = [
    re.compile(r'<option value="https?://winnersclub\.com/nl/"[^>]*>[^<]*</option>'),
    re.compile(r'<option value="/nl/"[^>]*>[^<]*</option>'),
    re.compile(r'<a href="https?://winnersclub\.com/nl/"[^>]*>[^<]*</a>'),
    re.compile(r'<a href="/nl/"[^>]*>[^<]*</a>'),
    re.compile(r'<li><a href="[^"]*nl/"[^>]*>[^<]*</a></li>'),
]

for path in ROOT.rglob("*.html"):
    if "/.git/" in str(path) or "/skills/" in str(path) or "/node_modules/" in str(path):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue
    original = text
    for pat in SWITCHER_PATTERNS:
        new_text, n = pat.subn("", text)
        if n:
            text = new_text
            stats["switcher_removed"] += n
    if text != original:
        path.write_text(text, encoding="utf-8")
        stats["html_files_changed"] += 1

import json
print(json.dumps(stats, indent=2))
