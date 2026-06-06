#!/usr/bin/env python3
"""
For legacy pages without </head>, inject lang-redirect.js before <body>.
Also rewrite the hreflang block on these pages to the canonical 9-link cluster
(en + 7 locales + x-default).
"""
import os, re, glob

ROOT = "/home/user/workspace/winnersclub.com"

LOCALES = ["en","ko","zh","vi","th","ms","pt","ja"]

def page_slug(path):
    """winnersclub.com/foo/index.html -> ('en','foo'); winnersclub.com/ko/foo/index.html -> ('ko','foo')."""
    rel = os.path.relpath(path, ROOT)
    parts = rel.split(os.sep)
    if parts[0] in LOCALES[1:]:
        lang = parts[0]
        slug = parts[1] if len(parts) > 2 else ""  # parts[-1] is index.html
    else:
        lang = "en"
        slug = parts[0] if len(parts) > 1 else ""
    # Strip index.html if slug somehow ended up as that
    if slug == "index.html":
        slug = ""
    return lang, slug

def build_hreflang(slug):
    parts = []
    def url_for(lang):
        if lang == "en":
            return f"https://winnersclub.com/{slug}/" if slug else "https://winnersclub.com/"
        return f"https://winnersclub.com/{lang}/{slug}/" if slug else f"https://winnersclub.com/{lang}/"
    # canonical hreflang attribute values
    attr_map = {"en":"en","ko":"ko","zh":"zh-Hans","vi":"vi","th":"th","ms":"ms","pt":"pt","ja":"ja"}
    for l in LOCALES:
        parts.append(f'  <link rel="alternate" hreflang="{attr_map[l]}" href="{url_for(l)}">')
    parts.append(f'  <link rel="alternate" hreflang="x-default" href="{url_for("en")}">')
    return "\n".join(parts)

REDIRECT_TAG = '<script src="/lang-redirect.js" defer></script>'

fixed_head    = 0
fixed_hreflang = 0
fixed_redirect = 0

# Pages flagged as missing </head> or having too few hreflang
TARGET_PAGES = [
    "originals", "stake-engine", "vip", "slots",
    "live-casino", "responsible-gambling", "news",
]

for lang in LOCALES:
    for slug in TARGET_PAGES:
        if lang == "en":
            fp = os.path.join(ROOT, slug, "index.html")
        else:
            fp = os.path.join(ROOT, lang, slug, "index.html")
        if not os.path.exists(fp):
            continue
        with open(fp, "r", encoding="utf-8") as f:
            html = f.read()
        orig = html

        # 1. Replace hreflang block with full 9-link cluster.
        # Find first hreflang link and last hreflang link, replace whole range.
        hreflang_re = re.compile(r'(\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', re.MULTILINE)
        new_block = "\n" + build_hreflang(slug) + "\n"
        if hreflang_re.search(html):
            html = hreflang_re.sub(new_block, html, count=1)
            fixed_hreflang += 1

        # 2. Inject lang-redirect.js before <body> if missing
        if 'lang-redirect.js' not in html:
            if '</head>' in html:
                html = html.replace('</head>', f'  {REDIRECT_TAG}\n</head>', 1)
            else:
                # inject before <body
                html = re.sub(r'(\s*<body)', f'\n  {REDIRECT_TAG}\n\\1', html, count=1)
            fixed_redirect += 1

        if html != orig:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(html)

print(f"Hreflang blocks rewritten: {fixed_hreflang}")
print(f"Redirect script added:    {fixed_redirect}")
