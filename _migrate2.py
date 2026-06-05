#!/usr/bin/env python3
"""
WinnersClub migration pass 2:
1. Swap affiliate URL repo-wide:
     OLD: https://playstake.io/landing?c=max3000&offer=max3000
     NEW: https://www.getstake.it/i/maxbet/io/maxbet/u/maxbet/uo/maxbet
2. Strip hreflang alternates for non-EN locales from EVERY page
3. Inject <meta name="robots" content="noindex,nofollow"> into every non-EN locale page
4. Rewrite robots.txt to:
     - Disallow each non-EN locale folder
     - Keep only sitemap.xml + sitemap-root.xml + sitemap-en.xml references
5. Rebuild sitemap.xml and sitemap-index.xml to point only at EN + root
6. Remove locale-specific sitemap-*.xml files (keep en/root/index)
7. Replace lang-selector button content with static "EN" (kill dropdown)
"""

import os, re, sys
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")

OLD_URL = "https://playstake.io/landing?c=max3000&offer=max3000"
NEW_URL = "https://www.getstake.it/i/maxbet/io/maxbet/u/maxbet/uo/maxbet"

NON_EN_LOCALES = [
    "ar","bg","bn","ca","cs","da","de","el","es","et","fa","fi","fr","gl","he",
    "hi","hr","hu","id","it","ja","kk","ko","lo","lt","lv","mn","ms","mt","nb",
    "nl","pl","pt","ro","ru","sk","sl","sq","sr","sv","th","tl","tr","uk","ur",
    "uz","vi","zh",
]

stats = {
    "files_scanned": 0,
    "url_swaps": 0,
    "hreflang_stripped": 0,
    "noindex_injected": 0,
    "lang_selector_stripped": 0,
    "files_modified": 0,
}

# Regex to strip hreflang lines for any non-EN locale
hreflang_pat = re.compile(
    r'\s*<link\s+rel="alternate"\s+hreflang="(?P<hl>[^"]+)"[^>]*>\s*\n?',
    re.IGNORECASE,
)

# Lang selector — collapse to plain "EN"
lang_selector_pat = re.compile(
    r'<(div|button|a|span)\s+class="lang-selector"[^>]*>.*?</\1>',
    re.IGNORECASE | re.DOTALL,
)
LANG_SELECTOR_REPLACEMENT = '<span class="lang-selector" aria-label="Language">EN</span>'


def is_non_en_locale_file(path: Path) -> bool:
    """Return True if file lives under a non-EN locale folder at the repo root."""
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    if len(parts) >= 1 and parts[0] in NON_EN_LOCALES:
        return True
    return False


def process_html(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return
    orig = text

    # 1) Affiliate URL swap (any HTML)
    if OLD_URL in text:
        count = text.count(OLD_URL)
        text = text.replace(OLD_URL, NEW_URL)
        stats["url_swaps"] += count

    # 2) Strip non-EN hreflang alternates from EVERY HTML
    def keep_hreflang(m):
        hl = m.group("hl").lower()
        # Keep EN and x-default
        if hl == "en" or hl == "x-default" or hl.startswith("en-"):
            return m.group(0)
        stats["hreflang_stripped"] += 1
        return ""
    text = hreflang_pat.sub(keep_hreflang, text)

    # 3) If this is a non-EN locale page, inject noindex + canonical to EN
    if is_non_en_locale_file(path) and path.suffix == ".html":
        if 'name="robots"' not in text:
            text = text.replace(
                "<head>",
                '<head>\n  <meta name="robots" content="noindex,nofollow">',
                1,
            )
            stats["noindex_injected"] += 1
        else:
            text = re.sub(
                r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>',
                '<meta name="robots" content="noindex,nofollow">',
                text,
                count=1,
            )

    # 4) Collapse the lang selector dropdown to static "EN"
    new_text, n = lang_selector_pat.subn(LANG_SELECTOR_REPLACEMENT, text)
    if n:
        stats["lang_selector_stripped"] += n
        text = new_text

    if text != orig:
        path.write_text(text, encoding="utf-8")
        stats["files_modified"] += 1


def process_other(path: Path):
    """Affiliate URL swap in non-HTML (xml, txt, json, md, js, css)."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return
    if OLD_URL not in text:
        return
    count = text.count(OLD_URL)
    text = text.replace(OLD_URL, NEW_URL)
    stats["url_swaps"] += count
    path.write_text(text, encoding="utf-8")
    stats["files_modified"] += 1


def walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip .git, node_modules
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
        for fn in filenames:
            p = Path(dirpath) / fn
            stats["files_scanned"] += 1
            ext = p.suffix.lower()
            if ext == ".html":
                process_html(p)
            elif ext in (".xml", ".txt", ".json", ".md", ".js", ".css"):
                process_other(p)


def rewrite_robots():
    robots_path = ROOT / "robots.txt"
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
    ]
    for loc in NON_EN_LOCALES:
        lines.append(f"Disallow: /{loc}/")
    lines.extend([
        "",
        "Sitemap: https://winnersclub.com/sitemap.xml",
    ])
    robots_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def clean_sitemaps():
    """Delete per-locale sitemap-XX.xml files (keep en, root)."""
    removed = 0
    for f in ROOT.glob("sitemap-*.xml"):
        name = f.name
        if name in ("sitemap-en.xml", "sitemap-root.xml", "sitemap-index.xml"):
            continue
        f.unlink()
        removed += 1
    return removed


def rewrite_master_sitemap():
    """Point sitemap.xml to just sitemap-en.xml + sitemap-root.xml as a sitemapindex."""
    body = '''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://winnersclub.com/sitemap-root.xml</loc>
  </sitemap>
  <sitemap>
    <loc>https://winnersclub.com/sitemap-en.xml</loc>
  </sitemap>
</sitemapindex>
'''
    (ROOT / "sitemap.xml").write_text(body, encoding="utf-8")
    # Also overwrite sitemap-index.xml if it exists, to match
    si = ROOT / "sitemap-index.xml"
    if si.exists():
        si.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    walk()
    rewrite_robots()
    removed = clean_sitemaps()
    rewrite_master_sitemap()
    print("=== migration pass 2 done ===")
    for k, v in stats.items():
        print(f"  {k}: {v:,}")
    print(f"  locale_sitemaps_removed: {removed}")
