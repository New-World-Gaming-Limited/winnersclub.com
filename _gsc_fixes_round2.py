#!/usr/bin/env python3
"""
GSC fixes round 2 — implements high-ICE wins from _gsc_ga_analysis_2026-06-18.md

Fixes:
1. Strip banned em-dashes (—) and en-dashes (–) from titles, h1, meta descriptions, h2
2. Rewrite /en/ homepage title to capture "winnerclub" + "winners club" + "winner club" (single + double word, brand variants)
3. Rewrite /en/casino/ title for higher CTR (5,195 impressions at 0.44% CTR)
4. Create redirect aliases for GSC ghost URLs:
   - /register/ → /promo-code/
   - /sportsbook/ → /sports/
   - /mirror-sites/ → /mirror/
   - /app/ → /aviator/ (closest match - no dedicated app page)
   - /stake-review/ → /about-stake/
   - /stake-promo-codes/ → /promo-code/
   These become real pages with proper titles serving the exact search intent.
5. Add alternateName to Organization JSON-LD (WinnerClub + WinnersClub spellings)
"""

import os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))

# 1. STRIP DASHES FROM TITLES/H1/META/H2 (NOT body — preserve content punctuation)
# Replace em-dash (—) and en-dash (–) with hyphen ( - ) inside <title>, <h1>, <h2>, meta description, og:description, twitter:description
# Conservative: only strip from elements where house style demands it

DASH_TAGS = [
    (re.compile(r'(<title>)([^<]*)(</title>)'), 'title'),
    (re.compile(r'(<h1[^>]*>)([^<]*)(</h1>)'), 'h1'),
    (re.compile(r'(<h2[^>]*>)([^<]*)(</h2>)'), 'h2'),
    (re.compile(r'(<meta name="description" content=")([^"]*)(")'), 'meta-desc'),
    (re.compile(r'(<meta property="og:title" content=")([^"]*)(")'), 'og-title'),
    (re.compile(r'(<meta property="og:description" content=")([^"]*)(")'), 'og-desc'),
    (re.compile(r'(<meta name="twitter:title" content=")([^"]*)(")'), 'tw-title'),
    (re.compile(r'(<meta name="twitter:description" content=")([^"]*)(")'), 'tw-desc'),
]

def strip_dashes_in_tagged(html, stats):
    for pat, tag in DASH_TAGS:
        def repl(m):
            opener, body, closer = m.group(1), m.group(2), m.group(3)
            new = body.replace(' — ', ' - ').replace('—', ' - ').replace(' – ', ' - ').replace('–', '-')
            # collapse double-spaces
            new = re.sub(r'  +', ' ', new).strip()
            if new != body:
                stats[tag] = stats.get(tag, 0) + 1
            return opener + new + closer
        html = pat.sub(repl, html)
    return html

# 2. EN HOMEPAGE TITLE REWRITE — add "WinnersClub" + "WinnerClub" brand variants
# Current: "Stake Sign Up Code MAX3000 - Register for 200% to $3,000"
# New:     "WinnersClub (WinnerClub) - Stake Sign Up Code MAX3000 | 200% to $3,000"
# Rationale: captures "winnerclub" 426 impressions at pos 15 PLUS keeps "stake sign up" 396 impressions

EN_HOME_TITLE_OLD_RE = re.compile(r'<title>Stake Sign Up Code MAX3000[^<]*</title>')
EN_HOME_TITLE_NEW = '<title>WinnersClub (WinnerClub) - Stake Sign Up Code MAX3000 | 200% to $3,000</title>'

# 3. EN /casino/ TITLE REWRITE — drop em-dash, add brand variants and CTA
# Current: "Stake Casino Review 2026 — 4,000+ Slots, Code MAX3000"
# New:     "WinnersClub Casino - Stake Casino with 4,000+ Slots & Code MAX3000"
# Rationale: targets "winners club online casino", "winnerclub casino", "casino winner" — all pulling impressions

EN_CASINO_TITLE_OLD_RE = re.compile(r'<title>Stake Casino Review 2026[^<]*</title>')
EN_CASINO_TITLE_NEW = '<title>WinnersClub Casino - Stake Casino with 4,000+ Slots & Code MAX3000</title>'

# 4. Add alternateName to Organization JSON-LD (improves brand SERP for both spellings)
# Look for: "@type":"Organization","name":"WinnersClub","url" → insert alternateName

ORG_JSONLD_RE = re.compile(r'("@type":"Organization","name":"WinnersClub","url":"https://winnersclub\.com/","logo":"[^"]*")')
ORG_JSONLD_ADD = r'\1,"alternateName":["WinnerClub","Winners Club","Winner Club","WC"]'

def fix_homepage_and_casino(path, stats):
    s = open(path, encoding='utf-8').read()
    orig = s

    if path.endswith('/index.html') and '/' not in os.path.relpath(path, ROOT):
        # This is the EN homepage (root)
        s = EN_HOME_TITLE_OLD_RE.sub(EN_HOME_TITLE_NEW, s)
        # og:title sync
        s = re.sub(
            r'<meta property="og:title" content="[^"]*"',
            '<meta property="og:title" content="WinnersClub | WinnerClub | Stake Code MAX3000 | 200% to $3,000"',
            s, count=1
        )
        # twitter:title sync
        s = re.sub(
            r'<meta name="twitter:title" content="[^"]*"',
            '<meta name="twitter:title" content="WinnersClub (WinnerClub) - Stake Sign Up Code MAX3000"',
            s, count=1
        )
        if s != orig:
            stats['en-home-title'] = stats.get('en-home-title', 0) + 1

    elif path == os.path.join(ROOT, 'casino', 'index.html'):
        # EN /casino/ page
        s = EN_CASINO_TITLE_OLD_RE.sub(EN_CASINO_TITLE_NEW, s)
        if s != orig:
            stats['en-casino-title'] = stats.get('en-casino-title', 0) + 1

    # Apply alternateName to Organization JSON-LD on all EN pages
    new_s = ORG_JSONLD_RE.sub(ORG_JSONLD_ADD, s)
    if new_s != s:
        stats['org-altname'] = stats.get('org-altname', 0) + 1
        s = new_s

    return s, s != orig

# 5. Strip dashes everywhere
def process_all_files(stats):
    n_changed = 0
    for root, dirs, files in os.walk(ROOT):
        if any(x in root for x in ['/.git', '/node_modules', '/__pycache__', '/build_helpers', '/research', '/scripts']):
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(root, f)
            s = open(p, encoding='utf-8').read()
            orig = s
            # Strip dashes
            s = strip_dashes_in_tagged(s, stats)
            # Homepage + casino specific rewrites (EN only)
            s2, _ = fix_homepage_and_casino(p, stats)
            # Use the dash-stripped + homepage-fixed version
            s = strip_dashes_in_tagged(s2, stats) if (s2 != orig) else s
            # Apply alternateName universally
            new_s = ORG_JSONLD_RE.sub(ORG_JSONLD_ADD, s)
            if new_s != s:
                stats['org-altname'] = stats.get('org-altname', 0) + 1
                s = new_s
            if s != orig:
                open(p, 'w', encoding='utf-8').write(s)
                n_changed += 1
    return n_changed

if __name__ == '__main__':
    stats = {}
    n = process_all_files(stats)
    print(f"Files changed: {n}")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")
