#!/usr/bin/env python3
"""
Replace the hardcoded EN/KO language switcher with the full 8-locale switcher.
Per-page aware: the current locale shows as `selected` and has empty value,
the others link to the corresponding localized URL for that same page.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://winnersclub.com"

# Locale dir -> display label
LOCALES = [
    (None, "EN"),
    ("ko", "KO"),
    ("zh", "ZH"),
    ("vi", "VI"),
    ("th", "TH"),
    ("ms", "MS"),
    ("pt", "PT"),
    ("ja", "JA"),
]

PAGES = [
    "", "promo-code", "casino", "sports", "poker", "mirror", "about-stake",
    "aviator", "payments", "reserves", "live-odds", "originals",
    "stake-engine", "vip", "slots", "live-casino", "responsible-gambling",
    "news", "stake-us-bonus",
]

# Match any <select ... onchange=...location.href...>...</select> that contains a >EN<, >KO<, or current-locale tag option
SWITCHER_RE = re.compile(
    r'<select[^>]*onchange="if\(this\.value\)window\.location\.href=this\.value"[^>]*>.*?</select>',
    re.DOTALL,
)


def page_url(lang_dir, slug):
    if lang_dir is None:
        return f"{SITE}/" if slug == "" else f"{SITE}/{slug}/"
    if slug == "":
        return f"{SITE}/{lang_dir}/"
    return f"{SITE}/{lang_dir}/{slug}/"


def build_switcher(current_lang_dir, slug):
    """Build the switcher HTML for the given page."""
    options = []
    for lang_dir, label in LOCALES:
        if lang_dir == current_lang_dir:
            options.append(f'<option value="" selected>{label}</option>')
        else:
            options.append(f'<option value="{page_url(lang_dir, slug)}">{label}</option>')
    # Detect which class was used (lang-switcher vs lang-select) - default to lang-switcher
    # Both styles exist; we keep whichever class the file currently uses to preserve CSS scoping.
    return options  # return options list; caller will assemble with the original class


def patch_file(path, lang_dir, slug):
    text = path.read_text(encoding="utf-8")
    options = build_switcher(lang_dir, slug)
    # Find existing switcher; preserve its class name
    m = SWITCHER_RE.search(text)
    if not m:
        return 0
    cls_match = re.search(r'class="(lang-(?:switcher|select))"', m.group(0))
    cls = cls_match.group(1) if cls_match else "lang-switcher"
    # If original had no class, no class is added back (keeps minimal markup)
    new_switcher = (
        f'<select class="{cls}" onchange="if(this.value)window.location.href=this.value" aria-label="Language">'
        + "".join(options)
        + '</select>'
    )
    new_text = text[:m.start()] + new_switcher + text[m.end():]
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return 1
    return 0


def main():
    total = 0
    files_changed = 0
    for slug in PAGES:
        for lang_dir, _ in LOCALES:
            if lang_dir is None:
                p = ROOT / "index.html" if slug == "" else ROOT / slug / "index.html"
            else:
                p = ROOT / lang_dir / "index.html" if slug == "" else ROOT / lang_dir / slug / "index.html"
            if not p.exists():
                continue
            n = patch_file(p, lang_dir, slug)
            if n > 0:
                files_changed += 1
                total += n
    print(f"Files changed: {files_changed} | switchers replaced: {total}")


if __name__ == "__main__":
    main()
