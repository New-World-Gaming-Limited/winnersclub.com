#!/usr/bin/env python3
"""
Comprehensive hreflang fix:
  1. Rebuild full reciprocal clusters across all 47 lang folders + root
  2. Add country-language variants (en-XX, pt-BR, zh-Hans, es-XX)
  3. Fix x-default to point at /en/ canonical instead of self
  4. Dedupe clusters (the 9 index.html pages with 98 entries)
  5. Apply to root mirror pages too (./casino.html, ./mirrors.html, etc.)
"""

import re
import json
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://1win.codes"

LANG_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Z]{2})?$")
LANGS = sorted([
    d.name for d in ROOT.iterdir()
    if d.is_dir() and LANG_RE.match(d.name) and (d / "index.html").exists()
])
print(f"Discovered {len(LANGS)} language folders: {LANGS}")

# Country-language variants: attach to the relevant /en/country-XX or related page
COUNTRY_VARIANTS_FOR_PAGE = {
    # Country page key (no .html, no leading slash) -> [(variant, target_url)]
    "country-south-africa": [("en-ZA", "/en/country-south-africa")],
    "country-malawi": [("en-MW", "/en/country-malawi")],
    "country-tanzania": [("en-TZ", "/en/country-tanzania")],
    "country-malaysia": [("en-MY", "/en/country-malaysia")],
    "country-singapore": [("en-SG", "/en/country-singapore")],
    "country-india": [("en-IN", "/en/country-india")],
    "country-pakistan": [("en-PK", "/en/country-pakistan")],
    "country-bangladesh": [("en-BD", "/en/country-bangladesh")],
    "country-ghana": [("en-GH", "/en/country-ghana")],
    "country-kenya": [("en-KE", "/en/country-kenya")],
    "country-argentina": [("es-AR", "/es/country-argentina")],
    "country-chile": [("es-CL", "/es/country-chile")],
    "country-brazil": [("pt-BR", "/pt/country-brazil")],
}

# Country variants to add on EVERY index/homepage so global signal is strong
GLOBAL_COUNTRY_VARIANTS = [
    ("en-ZA", "/en/country-south-africa"),
    ("en-MW", "/en/country-malawi"),
    ("en-TZ", "/en/country-tanzania"),
    ("en-MY", "/en/country-malaysia"),
    ("en-SG", "/en/country-singapore"),
    ("en-IN", "/en/country-india"),
    ("en-PK", "/en/country-pakistan"),
    ("en-BD", "/en/country-bangladesh"),
    ("en-GH", "/en/country-ghana"),
    ("en-KE", "/en/country-kenya"),
    ("en-NG", "/en/country-india"),  # fallback: no country-nigeria yet
    ("pt-BR", "/pt/"),
    ("zh-Hans", "/zh/"),
    ("es-AR", "/es/country-argentina"),
    ("es-CL", "/es/country-chile"),
    ("es-MX", "/es/"),
]


def file_key(p: Path) -> tuple:
    """Return (lang_code, page_key). lang_code = '__root__' for root mirror pages."""
    rel = p.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    if len(parts) >= 2 and parts[0] in LANGS:
        lang = parts[0]
        inner = "/".join(parts[1:])
    else:
        lang = "__root__"
        inner = rel
    # Normalise to clean URL key (no .html, no /index.html)
    if inner.endswith("/index.html"):
        inner = inner[: -len("/index.html")]
    elif inner == "index.html":
        inner = ""
    elif inner.endswith(".html"):
        inner = inner[:-5]
    return (lang, inner)


def page_url(lang: str, key: str) -> str:
    if lang == "__root__":
        return f"{SITE}/{key}" if key else f"{SITE}/"
    return f"{SITE}/{lang}/{key}" if key else f"{SITE}/{lang}/"


def build_cluster(key: str, lang_set: dict) -> str:
    """Build the full hreflang cluster for a given page key."""
    lines = []

    # English canonical for x-default
    if "en" in lang_set:
        english_url = page_url("en", key)
    elif "__root__" in lang_set:
        english_url = page_url("__root__", key)
    else:
        english_url = f"{SITE}/"

    # Standard lang hreflangs - alphabetised
    for lang in LANGS:
        if lang in lang_set:
            url = page_url(lang, key)
            lines.append(f'  <link rel="alternate" hreflang="{lang}" href="{url}">')

    # Country-language variants for specific pages
    if key in COUNTRY_VARIANTS_FOR_PAGE:
        for variant, target_path in COUNTRY_VARIANTS_FOR_PAGE[key]:
            target_url = f"{SITE}{target_path}"
            lines.append(f'  <link rel="alternate" hreflang="{variant}" href="{target_url}">')

    # Global country variants ONLY on the homepage (key="" or key="index")
    if key == "":
        for variant, target_path in GLOBAL_COUNTRY_VARIANTS:
            target_url = f"{SITE}{target_path}"
            lines.append(f'  <link rel="alternate" hreflang="{variant}" href="{target_url}">')

    # x-default points to English canonical (NEVER self unless this IS the English version)
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{english_url}">')

    return "\n".join(lines)


def patch_file(p: Path, cluster: str) -> bool:
    text = p.read_text(encoding="utf-8")
    original = text

    # First, strip ALL existing hreflang links from the file (regardless of format/order).
    # Matches both rel-first and href-first attribute order, and both "<link ...>" and "<link ... />".
    strip_re = re.compile(
        r'\s*<link[^>]*hreflang="[^"]*"[^>]*?/?>\s*\n?',
        re.MULTILINE,
    )
    cleaned = strip_re.sub('', text)

    # Now inject the new block immediately before </head>
    new_block = "\n" + cluster + "\n  "

    if "</head>" in cleaned:
        new_text = cleaned.replace("</head>", new_block + "</head>", 1)
    else:
        return False

    if new_text != original:
        p.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    # Phase 1: discover all pages
    key_to_langs: dict[str, dict] = {}
    file_to_meta: dict[Path, tuple] = {}
    for p in ROOT.rglob("*.html"):
        s = p.as_posix()
        if "/.git/" in s or "/node_modules/" in s or "build_helpers" in s or "google0" in s:
            continue
        lang, key = file_key(p)
        file_to_meta[p] = (lang, key)
        key_to_langs.setdefault(key, {})[lang] = True

    print(f"\nDiscovered {len(key_to_langs)} unique page keys across {len(file_to_meta)} files")

    # Phase 2: patch every file
    patched = 0
    for p, (lang, key) in file_to_meta.items():
        cluster = build_cluster(key, key_to_langs[key])
        if patch_file(p, cluster):
            patched += 1
    print(f"Patched {patched} files")


if __name__ == "__main__":
    main()
