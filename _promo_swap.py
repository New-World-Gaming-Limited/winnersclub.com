#!/usr/bin/env python3
"""Replace MAXBET promo code with MAX3000 site-wide.
Covers: copy text, meta tags, JSON-LD, sitemap, robots, JS, CSS, manifest.
Updates affiliate URLs: getstake.it old → new, stake.us ?c= param.
Preserves: file names, image filenames, the literal historical paths under /images/.
"""
import os, re

OLD_URL_RE = re.compile(r"https://www\.getstake\.it/i/[Mm]axbet/io/maxbet/u/[^/]+/uo/[^\"' >]+")
NEW_URL = "https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000"

STAKE_US_RE = re.compile(r"(stake\.us/\?c=)maxbet", re.IGNORECASE)

# We replace MAXBET and maxbet ONLY when used as the promo code, not when part of:
# - image paths /images/...
# - URL paths already handled above
# Strategy: do URL replacements first, then bulk replace remaining "MAXBET"/"Maxbet"/"maxbet" tokens
# but ONLY when surrounded by word boundaries and NOT inside src/href to images.

# We use a two-pass approach: protect image filenames first.
IMG_PROTECT_RE = re.compile(r'(/images/[^"\'\s>]+)')

EXCLUDE_DIRS = (".git", "node_modules", "__pycache__", "tmp", "build_helpers", "uploaded_attachments")
EXCLUDE_FILES = ("_promo_swap.py",)
INCLUDE_EXT = (".html", ".css", ".js", ".json", ".xml", ".txt", ".md", ".webmanifest")

def process(path):
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    orig = text

    # 1. Replace old getstake URLs with new one
    text = OLD_URL_RE.sub(NEW_URL, text)

    # 2. Replace stake.us ?c=maxbet → ?c=MAX3000  (preserve trailing chars)
    text = STAKE_US_RE.sub(r"\1MAX3000", text)

    # 3. Protect image filenames (replace then restore)
    protected = {}
    def protect(m):
        key = f"\x00IMG{len(protected)}\x00"
        protected[key] = m.group(1)
        return key
    text = IMG_PROTECT_RE.sub(protect, text)

    # 4. Replace promo code tokens (case-sensitive variants)
    #    MAXBET → MAX3000
    #    Maxbet → Max3000  (less common, in labels)
    #    maxbet → MAX3000  (in copy/URLs — promo codes are usually shown uppercase)
    # Use word boundaries to avoid breaking things accidentally
    text = re.sub(r"\bMAXBET\b", "MAX3000", text)
    text = re.sub(r"\bMaxbet\b", "Max3000", text)
    # lowercase: covers stake.us anchor text like "stake.us/?c=maxbet" already handled
    # but still need to catch remaining "maxbet" in copy
    text = re.sub(r"\bmaxbet\b", "MAX3000", text)

    # 5. Restore image filenames
    for key, val in protected.items():
        text = text.replace(key, val)

    if text != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    return False

changed = 0
total = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not any(s in d for s in EXCLUDE_DIRS)]
    for f in files:
        if f in EXCLUDE_FILES: continue
        if not f.endswith(INCLUDE_EXT): continue
        path = os.path.join(root, f)
        total += 1
        if process(path):
            changed += 1

print(f"Scanned {total} files, modified {changed}")
