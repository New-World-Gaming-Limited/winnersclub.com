#!/usr/bin/env python3
"""Remove the /nl/ Dutch locale completely:
1. Delete /nl/ directory
2. Strip <link rel="alternate" hreflang="nl"...> from all HTML pages
3. Strip <option value="/nl/">Nederlands...</option> from language switcher (desktop + mobile)
4. Strip any href="/nl/..." anchor entries from mobile lang lists
5. Remove /nl/ URLs from sitemap.xml
6. Remove 'nl' from lang-redirect.js supportedLangs and remove NL/BE country mappings
"""
import re, shutil
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")
stats = {"html_files_changed": 0, "hreflang_removed": 0, "switcher_removed": 0,
         "anchor_removed": 0, "sitemap_urls_removed": 0, "redirect_changes": 0}

# 1. Delete directory
nl_dir = ROOT / "nl"
if nl_dir.is_dir():
    shutil.rmtree(nl_dir)
    print(f"Removed {nl_dir}")

# 2-4. Clean every HTML file
# Patterns to remove (match optional surrounding whitespace and the line endings)
HTML_PATTERNS = [
    # Hreflang line variations
    (re.compile(r'\s*<link rel="alternate" hreflang="nl" href="[^"]*"\s*/?>\s*\n?'), "hreflang_removed"),
    # Desktop select option
    (re.compile(r'\s*<option value="/nl/"[^>]*>[^<]*</option>\s*\n?'), "switcher_removed"),
    # Mobile li anchor list entries (any variant)
    (re.compile(r'\s*<li><a href="/nl/"[^>]*>[^<]*</a></li>\s*\n?'), "anchor_removed"),
    (re.compile(r'\s*<a href="/nl/"[^>]*>[^<]*</a>\s*\n?'), "anchor_removed"),
]

html_files = list(ROOT.rglob("*.html"))
for path in html_files:
    if "/.git/" in str(path) or "/skills/" in str(path) or "/node_modules/" in str(path):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue
    original = text
    file_changed = False
    for pattern, key in HTML_PATTERNS:
        new_text, n = pattern.subn("", text)
        if n:
            text = new_text
            stats[key] += n
            file_changed = True
    if file_changed:
        path.write_text(text, encoding="utf-8")
        stats["html_files_changed"] += 1

# 5. Sitemap: remove <url>...</url> blocks containing /nl/ URLs and any nl xhtml:link inside other entries
sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    text = sitemap.read_text(encoding="utf-8")
    # Remove full <url>...</url> blocks where the <loc> contains /nl/
    url_block = re.compile(r'\s*<url>\s*<loc>https?://[^<]*/nl/[^<]*</loc>.*?</url>\s*', re.DOTALL)
    text2, n_blocks = url_block.subn("", text)
    # Remove any inline <xhtml:link rel="alternate" hreflang="nl" .../> entries inside surviving url blocks
    xhtml_nl = re.compile(r'\s*<xhtml:link\s+rel="alternate"\s+hreflang="nl"\s+href="[^"]*"\s*/?>\s*\n?')
    text3, n_xhtml = xhtml_nl.subn("", text2)
    if text3 != text:
        sitemap.write_text(text3, encoding="utf-8")
        stats["sitemap_urls_removed"] = n_blocks + n_xhtml
        print(f"sitemap: removed {n_blocks} <url> blocks and {n_xhtml} xhtml:link entries")

# 6. lang-redirect.js — remove nl from supportedLangs, remove NL and BE mappings
lr = ROOT / "lang-redirect.js"
if lr.exists():
    js = lr.read_text(encoding="utf-8")
    original_js = js
    # supportedLangs array: drop ,'nl' or 'nl', or ['nl', or just 'nl'
    js = js.replace(",'nl'", "")
    js = js.replace("'nl',", "")
    # country mappings line: remove 'NL':'nl', and 'BE':'nl',
    js = js.replace("'NL':'nl',", "")
    js = js.replace("'BE':'nl',", "")
    # Also handle reversed orders, just in case
    js = js.replace("'BE':'nl'", "")
    js = js.replace("'NL':'nl'", "")
    if js != original_js:
        lr.write_text(js, encoding="utf-8")
        stats["redirect_changes"] = 1

import json
print(json.dumps(stats, indent=2))
