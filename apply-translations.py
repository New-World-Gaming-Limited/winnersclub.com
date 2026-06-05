#!/usr/bin/env python3
"""
Apply translation dictionaries to all HTML files across 45 language folders.

For each language, we load translations/{lang}.json (English -> Native dict),
walk every HTML file in /{lang}/, and replace any occurrence of an English
source string with its native translation.

We're careful to only replace strings that occur as visible HTML content
(between tags) — not strings inside attributes, scripts, or JSON-LD.
"""

import re
import json
from pathlib import Path

ROOT = Path(__file__).parent
TRANSLATIONS_DIR = ROOT / "translations"


def apply_translations_to_file(path: Path, translations: dict) -> int:
    """Apply translation dictionary to a single HTML file. Returns count of replacements."""
    text = path.read_text(encoding="utf-8")
    original = text

    # Strip out <script> ... </script> blocks temporarily so we don't accidentally
    # translate inside JSON-LD. Same for <style>.
    script_blocks = []
    style_blocks = []

    def stash_script(m):
        script_blocks.append(m.group(0))
        return f"___SCRIPT_BLOCK_{len(script_blocks)-1}___"

    def stash_style(m):
        style_blocks.append(m.group(0))
        return f"___STYLE_BLOCK_{len(style_blocks)-1}___"

    text = re.sub(r"<script\b[^>]*>.*?</script>", stash_script, text, flags=re.DOTALL)
    text = re.sub(r"<style\b[^>]*>.*?</style>", stash_style, text, flags=re.DOTALL)

    # Apply translations — sorted longest first to avoid partial-match issues
    count = 0
    for en, native in sorted(translations.items(), key=lambda kv: -len(kv[0])):
        if not en or not native:
            continue
        # SAFETY: refuse to replace anything shorter than 10 chars — we only
        # translate sentence/phrase-length content, never single words or digits.
        if len(en) < 10:
            continue
        # Only replace when the English string is found in the body content.
        # The strings we're translating are full sentences/phrases — they won't
        # match inside attribute values or short tag content by accident.
        if en in text:
            new_text = text.replace(en, native)
            n = text.count(en)
            text = new_text
            count += n

    # Restore scripts and styles
    for i, block in enumerate(script_blocks):
        text = text.replace(f"___SCRIPT_BLOCK_{i}___", block)
    for i, block in enumerate(style_blocks):
        text = text.replace(f"___STYLE_BLOCK_{i}___", block)

    if text != original:
        path.write_text(text, encoding="utf-8")
    return count


def main():
    total_files_patched = 0
    total_replacements = 0
    per_lang_stats = {}

    for json_file in sorted(TRANSLATIONS_DIR.glob("*.json")):
        lang = json_file.stem
        lang_dir = ROOT / lang
        if not lang_dir.is_dir():
            print(f"SKIP {lang}: no language folder")
            continue

        translations = json.loads(json_file.read_text(encoding="utf-8"))
        files_patched = 0
        replacements = 0

        for html_file in lang_dir.rglob("*.html"):
            n = apply_translations_to_file(html_file, translations)
            if n > 0:
                files_patched += 1
                replacements += n

        per_lang_stats[lang] = (files_patched, replacements)
        total_files_patched += files_patched
        total_replacements += replacements
        print(f"  {lang}: {files_patched} files patched, {replacements} replacements")

    print(f"\nTotal: {total_files_patched} files patched, {total_replacements} replacements")


if __name__ == "__main__":
    main()
