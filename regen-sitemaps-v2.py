#!/usr/bin/env python3
"""
Regenerate all sitemap-{lang}.xml files with full hreflang xhtml:link
annotations on every <url> entry. Use clean URLs (no .html suffix).
"""

import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SITE = "https://1win.codes"
TODAY = date.today().isoformat()

LANG_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Z]{2})?$")
LANGS = sorted([
    d.name for d in ROOT.iterdir()
    if d.is_dir() and LANG_RE.match(d.name) and (d / "index.html").exists()
])


def file_key(p):
    rel = p.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    if len(parts) >= 2 and parts[0] in LANGS:
        lang = parts[0]
        inner = "/".join(parts[1:])
    else:
        lang = "__root__"
        inner = rel
    if inner.endswith("/index.html"):
        inner = inner[: -len("/index.html")]
    elif inner == "index.html":
        inner = ""
    elif inner.endswith(".html"):
        inner = inner[:-5]
    return (lang, inner)


def page_url(lang, key):
    if lang == "__root__":
        return f"{SITE}/{key}" if key else f"{SITE}/"
    return f"{SITE}/{lang}/{key}" if key else f"{SITE}/{lang}/"


def get_priority(key):
    if key in ("", "index"):
        return "1.0"
    if key in ("promo-code", "1win-promo-code", "casino", "mirrors", "register", "sports-betting"):
        return "0.9"
    if key.startswith("country-"):
        return "0.8"
    if key.startswith("promo-code/"):
        return "0.7"
    if key.startswith("news/") or key.startswith("news-"):
        return "0.5"
    return "0.7"


def discover():
    key_to_langs = {}
    for p in ROOT.rglob("*.html"):
        s = p.as_posix()
        if "/.git/" in s or "/node_modules/" in s or "build_helpers" in s or "google0" in s:
            continue
        lang, key = file_key(p)
        key_to_langs.setdefault(key, {})[lang] = True
    return key_to_langs


def build_sitemap_for(lang, key_to_langs):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for key, lang_set in sorted(key_to_langs.items()):
        if lang not in lang_set:
            continue
        url = page_url(lang, key)
        priority = get_priority(key)
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f"    <priority>{priority}</priority>")

        # Hreflang alternates
        for alt_lang in LANGS:
            if alt_lang in lang_set:
                alt_url = page_url(alt_lang, key)
                lines.append(f'    <xhtml:link rel="alternate" hreflang="{alt_lang}" href="{alt_url}"/>')

        # x-default
        if "en" in lang_set:
            en_url = page_url("en", key)
        elif "__root__" in lang_set:
            en_url = page_url("__root__", key)
        else:
            en_url = f"{SITE}/"
        lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}"/>')

        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    return "\n".join(lines)


def main():
    key_to_langs = discover()
    print(f"Discovered {len(key_to_langs)} unique page keys")

    for lang in LANGS:
        out = ROOT / f"sitemap-{lang}.xml"
        out.write_text(build_sitemap_for(lang, key_to_langs), encoding="utf-8")
    out = ROOT / "sitemap-root.xml"
    out.write_text(build_sitemap_for("__root__", key_to_langs), encoding="utf-8")
    print(f"Wrote {len(LANGS) + 1} sitemap files")

    # Update sitemap index to ensure all referenced
    idx = ROOT / "sitemap.xml"
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    lines.append(f"  <sitemap>\n    <loc>{SITE}/sitemap-root.xml</loc>\n    <lastmod>{TODAY}</lastmod>\n  </sitemap>")
    for lang in LANGS:
        lines.append(f"  <sitemap>\n    <loc>{SITE}/sitemap-{lang}.xml</loc>\n    <lastmod>{TODAY}</lastmod>\n  </sitemap>")
    lines.append("</sitemapindex>")
    idx.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote sitemap index ({len(LANGS) + 1} entries)")


if __name__ == "__main__":
    main()
