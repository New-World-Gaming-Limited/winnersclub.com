#!/usr/bin/env python3
"""
Replace Stake.com global exit link with new bets.com.au-tracked URL.

Source of truth: https://api.bets.com.au/api/brandbonus/all?siteid=72&countrycode=AD&languageid=1&channelid=1
Entry where BrandName='Stake.com', Promocode='MAX3000', sitename='Winnersclub.com'

OLD: https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000
NEW: https://www.winnersclub.com/link/e489d763260610214223/72/

Stake.us exit (https://stake.us/?c=MAX3000) is left untouched — that is the US-only affiliate path.
Informational links to help.stake.com, help.stake.us, stake.com/blog/..., stake.com/casino/...,
stake.com/legal/..., stake.com/promotions are first-party Stake content (allowed by rules) and untouched.
"""
import re
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")

OLD = "https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000"
NEW = "https://www.winnersclub.com/link/e489d763260610214223/72/"

stats = {"files_changed": 0, "replacements": 0}

# Plain-text replacement across all HTML files
for path in ROOT.rglob("*.html"):
    s = str(path)
    if "/.git/" in s or "/skills/" in s or "/node_modules/" in s:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue
    if OLD not in text:
        continue
    n = text.count(OLD)
    text = text.replace(OLD, NEW)
    path.write_text(text, encoding="utf-8")
    stats["files_changed"] += 1
    stats["replacements"] += n

# Also patch JS/CSS/JSON/TXT just in case (skills exists in repo as md/zip; ignore)
for ext in ("js", "json", "txt", "xml", "md"):
    for path in ROOT.rglob(f"*.{ext}"):
        s = str(path)
        if "/.git/" in s or "/skills/" in s or "/node_modules/" in s:
            continue
        # Skip our own audit/build/log markdown files in workspace root
        if path.name.startswith("_"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if OLD not in text:
            continue
        n = text.count(OLD)
        text = text.replace(OLD, NEW)
        path.write_text(text, encoding="utf-8")
        stats["files_changed"] += 1
        stats["replacements"] += n
        print(f"  also patched non-HTML: {path.relative_to(ROOT)}")

import json
print(json.dumps(stats, indent=2))
