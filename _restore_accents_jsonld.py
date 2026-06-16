#!/usr/bin/env python3
"""Second pass: restore accents inside JSON-LD string values (name/description/text/headline/articleBody/answerText)."""
import os, re, json, sys

# Import the FIXES dict from the main script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("_restore_accents", os.path.join(os.path.dirname(__file__), "_restore_accents.py"))
ra = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ra)

ROOT = os.path.dirname(os.path.abspath(__file__))
JSONLD_BLOCK = re.compile(r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)', re.S | re.I)

def apply_to_string(s, compiled_fixes):
    for pat, new in compiled_fixes:
        s = pat.sub(new, s)
    return s

def fix_jsonld_block(content, compiled_fixes):
    """Parse JSON-LD, fix string values, re-serialize."""
    try:
        data = json.loads(content)
    except Exception:
        # Try to do conservative string replacement directly (preserve formatting)
        return apply_string_values_regex(content, compiled_fixes)

    def walk(node):
        if isinstance(node, dict):
            return {k: (apply_to_string(v, compiled_fixes) if isinstance(v, str) and k in {"name","description","text","headline","articleBody","answerText","question","caption","alternateName","disambiguatingDescription","reviewBody"} else walk(v)) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(x) for x in node]
        return node

    fixed = walk(data)
    # Re-serialize keeping unicode (not ASCII-escaped)
    return json.dumps(fixed, ensure_ascii=False, separators=(', ', ': '))

def apply_string_values_regex(content, compiled_fixes):
    """Fallback: regex over "key": "value" pairs for known keys."""
    keys = r'(name|description|text|headline|articleBody|answerText|question|caption|reviewBody)'
    pat = re.compile(r'"' + keys + r'"\s*:\s*"((?:[^"\\]|\\.)*)"')
    def repl(m):
        key, val = m.group(1), m.group(2)
        # Unescape, fix, re-escape
        try:
            decoded = json.loads('"' + val + '"')
        except Exception:
            decoded = val
        fixed = apply_to_string(decoded, compiled_fixes)
        return '"' + key + '": ' + json.dumps(fixed, ensure_ascii=False)
    return pat.sub(repl, content)

def process_file(path, compiled_fixes):
    s = open(path, encoding="utf-8").read()
    def repl(m):
        opener, body, closer = m.group(1), m.group(2), m.group(3)
        # Try regex-based first (preserves formatting better)
        new_body = apply_string_values_regex(body, compiled_fixes)
        return opener + new_body + closer
    new_s = JSONLD_BLOCK.sub(repl, s)
    if new_s != s:
        open(path, "w", encoding="utf-8").write(new_s)
        return True
    return False

def walk(loc_dir):
    for root, dirs, files in os.walk(loc_dir):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(root, f)

def main():
    total = 0
    for loc, pairs in ra.FIXES.items():
        loc_path = os.path.join(ROOT, loc)
        if not os.path.isdir(loc_path):
            continue
        cfixes = ra.compile_fixes(pairs)
        n = 0
        for p in walk(loc_path):
            if process_file(p, cfixes):
                n += 1
        total += n
        print(f"  {loc}: {n} files updated")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
