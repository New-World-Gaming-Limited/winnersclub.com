#!/usr/bin/env python3
"""Fix bad backslash escapes inside JSON-LD blocks across all pages.
Valid JSON escapes: \\" \\\\ \\/ \\b \\f \\n \\r \\t \\uXXXX. Anything else is invalid."""
import os, re, json

JSONLD_RE = re.compile(
    r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.DOTALL | re.IGNORECASE,
)

# Match a backslash followed by a char that's NOT one of the valid JSON escape chars
BAD_ESC_RE = re.compile(r'\\([^"\\/bfnrtu])')

fixed_files = 0
fixed_blocks = 0

def fix_block(m, path):
    global fixed_blocks
    opener, body, closer = m.group(1), m.group(2), m.group(3)
    try:
        json.loads(body)
        return m.group(0)
    except json.JSONDecodeError:
        pass
    new_body = BAD_ESC_RE.sub(r'\1', body)
    try:
        json.loads(new_body)
        fixed_blocks += 1
        print(f"  Fixed: {path}")
        return opener + new_body + closer
    except json.JSONDecodeError as e:
        print(f"  STILL BROKEN: {path}: {e}")
        return m.group(0)

for root, dirs, files in os.walk("."):
    if any(s in root for s in (".git", "node_modules", "build_helpers", "uploaded_attachments")):
        continue
    for f in files:
        if not f.endswith(".html"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8", errors="ignore") as fp:
            html = fp.read()
        orig = html
        html = JSONLD_RE.sub(lambda m: fix_block(m, path), html)
        if html != orig:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(html)
            fixed_files += 1

print(f"\nFixed {fixed_blocks} JSON-LD blocks in {fixed_files} files")

# Re-validate
broken = 0
for root, dirs, files in os.walk("."):
    if any(s in root for s in (".git", "node_modules", "build_helpers", "uploaded_attachments")):
        continue
    for f in files:
        if not f.endswith(".html"): continue
        path = os.path.join(root, f)
        with open(path, encoding="utf-8", errors="ignore") as fp:
            html = fp.read()
        for m in JSONLD_RE.finditer(html):
            try:
                json.loads(m.group(2))
            except:
                broken += 1
                print(f"  STILL BROKEN: {path}")
print(f"Remaining broken: {broken}")
