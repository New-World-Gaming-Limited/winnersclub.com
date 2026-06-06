#!/usr/bin/env python3
"""
For the lang-switcher, the SELECTED option label should be a 2-letter code (compact)
while the dropdown options keep native names (discoverable).
"""
import os, re, glob

ROOT = "/home/user/workspace/winnersclub.com"

NATIVE_TO_CODE = {
    "English": "EN",
    "한국어": "KO",
    "中文": "ZH",
    "Tiếng Việt": "VI",
    "ไทย": "TH",
    "Bahasa Melayu": "MS",
    "Português": "PT",
    "日本語": "JA",
}

# Pattern matches any <option value="..." selected>NATIVE</option>
def update(html):
    for native, code in NATIVE_TO_CODE.items():
        # Match "selected" option with the native label, swap label to code
        pat = re.compile(
            r'(<option\s+value="[^"]*"\s+selected\s*>)' + re.escape(native) + r'(</option>)'
        )
        html = pat.sub(rf'\1{code}\2', html)
    return html

changed = 0
for fp in glob.glob(f"{ROOT}/**/*.html", recursive=True):
    if "/node_modules/" in fp:
        continue
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    new = update(html)
    if new != html:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new)
        changed += 1

print(f"Files updated: {changed}")
