#!/usr/bin/env python3
"""
1. Replace 2-letter switcher labels (EN, KO, ...) with native names.
2. Inject lang-redirect.js into every page <head> (before </head>) if missing.
"""
import os, re, glob

ROOT = "/home/user/workspace/winnersclub.com"

# Native language names (no emoji per house rules)
NATIVE = {
    "EN": "English",
    "KO": "한국어",
    "ZH": "中文",
    "VI": "Tiếng Việt",
    "TH": "ไทย",
    "MS": "Bahasa Melayu",
    "PT": "Português",
    "JA": "日本語",
}

# Build replacement pairs - each option line
OPT_REPLACEMENTS = []
for code, native in NATIVE.items():
    # match >EN<, >KO<, etc. inside an <option> tag (avoid touching other content)
    OPT_REPLACEMENTS.append((f">{code}</option>", f">{native}</option>"))

REDIRECT_TAG = '<script src="/lang-redirect.js" defer></script>'

def walk_html():
    for path in glob.glob(f"{ROOT}/**/*.html", recursive=True):
        if "/node_modules/" in path or "/build_helpers/" in path:
            continue
        yield path

switcher_changed = 0
redirect_added   = 0
total            = 0

for fp in walk_html():
    total += 1
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    orig = html

    # 1. swap labels
    for old, new in OPT_REPLACEMENTS:
        html = html.replace(old, new)
    if html != orig:
        switcher_changed += 1

    # 2. inject redirect script if missing
    if 'lang-redirect.js' not in html and '</head>' in html:
        html = html.replace('</head>', f'  {REDIRECT_TAG}\n</head>', 1)
        redirect_added += 1

    if html != orig:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)

print(f"Total HTML files: {total}")
print(f"Switcher labels updated in: {switcher_changed}")
print(f"Redirect script injected in: {redirect_added}")
