#!/usr/bin/env python3
"""
Fix ALL-CAPS H2s across all 21 target pages.
Converts them to Sentence case matching EN_REWRITE.md specs.
"""
import os, re

BASE = '/home/user/workspace/1win-codes-repo/en'

def rw(fname, pairs):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    orig = s
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new, 1)
        else:
            print(f'  MISS [{fname}]: {repr(old[:80])}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    if s != orig:
        print(f'  OK: {fname}')

# ── MIRRORS.HTML ──────────────────────────────────────────────────
print('\n== mirrors.html ==')
rw('mirrors.html', [
    ('1WIN <span class="text-gradient">OVERVIEW</span>', 'What is a 1win mirror?'),
    ('1WIN WORKING <span class="text-gradient">MIRROR</span>', 'How to access the current 1win mirror'),
    ('1WIN MIRROR <span class="text-gradient-gold">DOWNLOAD</span>', 'Mirror on iOS and Android'),
    ('1WIN BET <span class="text-gradient">MIRROR</span>', 'Three backup mirror methods'),
    ('1WIN MIRROR <span class="text-gradient-gold">BONUS</span>', 'Is the mirror safe?'),
    ('1WIN <span class="text-gradient">APP</span>', 'Why your main 1win URL might not load'),
    ('WHY USE A <span class="text-gradient">1WIN MIRROR</span>', 'Why mirrors exist'),
    ('IS IT SAFE TO USE A <span class="text-gradient">1WIN MIRROR?</span>', 'Verifying a mirror is safe'),
    ('1WIN MIRROR VS <span class="text-gradient-gold">VPN</span>', 'Mirror vs VPN'),
    ('HOW TO FIND THE LATEST <span class="text-gradient">1WIN MIRROR</span>', 'How to find the latest working mirror'),
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>', 'Access current mirror and claim your bonus'),
])

# ── ACCESS.HTML ───────────────────────────────────────────────────
print('\n== access.html ==')
rw('access.html', [
    ('1WIN LOGIN AND <span class="text-gradient">WEBSITE ACCESS</span>', '1win login - sign in to your account'),
    ('1WIN WEBSITE <span class="text-gradient">INFORMATION</span>', '1win platform overview'),
    ('1WIN <span class="text-gradient">REGISTRATION</span>', 'Register a new 1win account'),
    ('1WIN LOGIN BY <span class="text-gradient">COUNTRY</span>', 'Login by country'),
    ('1WIN BY <span class="text-gradient">COUNTRY</span>', '1win by country'),
    ('1WIN LOGIN <span class="text-gradient-gold">PROMO CODE</span>', 'Login and claim your XLBONUS welcome bonus'),
    ('1WIN LOGIN <span class="text-gradient">AVIATOR</span>', 'Play Aviator after login'),
    ('1WIN LOGIN <span class="text-gradient">DOWNLOAD</span>', 'Login via the 1win app'),
    ('1WIN LOGIN <span class="text-gradient">FAQs</span>', 'Frequently asked questions'),
    ('ACCESS 1WIN &amp; CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>', 'Access 1win and claim your 600% bonus'),
])

# ── ALTERNATIVE-LINK.HTML ─────────────────────────────────────────
print('\n== alternative-link.html ==')
rw('alternative-link.html', [
    ('CURRENT WORKING <span class="text-gradient">ALTERNATIVE LINKS</span>', 'Current working alternative links'),
    ('WHY YOU NEED A <span class="text-gradient">1WIN ALTERNATIVE LINK</span>', 'Why you might need a 1win alternative link'),
    ('HOW TO ACCESS 1WIN USING <span class="text-gradient-gold">ALTERNATIVE LINKS</span>', 'How to access 1win using the alternative link'),
    ('ALTERNATIVE LINK <span class="text-gradient-gold">VS VPN VS MIRROR</span>', 'Alternative link vs VPN vs mirror'),
    ('IS THE 1WIN ALTERNATIVE LINK <span class="text-gradient">SAFE?</span>', 'Is the 1win alternative link safe?'),
    ('FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>', 'Frequently asked questions'),
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>', 'Access 1win and claim your 600% bonus'),
])

# ── WEBSITE.HTML ──────────────────────────────────────────────────
print('\n== website.html ==')
rw('website.html', [
    ('1WIN WEBSITE <span class="text-gradient">INFORMATION</span>', '1win operator information'),
    ('1WIN WEBSITE <span class="text-gradient">LOGIN</span>', 'Login to 1win'),
    ("WHAT'S ON THE <span class=\"text-gradient\">1WIN WEBSITE</span>", 'Products on the 1win platform'),
    ('1WIN WEBSITE <span class="text-gradient-gold">BONUS</span>', 'Welcome bonus and promo code XLBONUS'),
    ('HOW TO <span class="text-gradient">ACCESS</span> THE 1WIN WEBSITE', 'How to access the 1win website'),
    ('1WIN WEBSITE <span class="text-gradient">FAQs</span>', 'Frequently asked questions'),
    ('VISIT THE 1WIN WEBSITE WITH <span class="text-gradient-gold">600% BONUS</span>', 'Open your 1win account with XLBONUS'),
])

# ── POKER.HTML ────────────────────────────────────────────────────
print('\n== poker.html ==')
rw('poker.html', [
    ('GAME <span class="text-gradient">TYPES</span>', 'Poker game types at 1win'),
    ('TOURNAMENT <span class="text-gradient-gold">ACTION</span>', 'Tournament schedule'),
    ("READ THE <span class='text-gradient'>TABLE</span>", 'Cash table stakes and options'),
    ('CASH <span class="text-gradient">TABLES</span>', 'Cash tables at 1win'),
    ('POKER <span class="text-gradient">FEATURES</span>', 'Poker features at 1win'),
    ('RAKEBACK <span class="text-gradient-gold">PROGRAM</span>', 'Rakeback and loyalty program'),
    ("ALL IN <span class='text-gradient-gold'>CONFIDENCE</span>", 'Poker with XLBONUS'),
    ('1WIN <span class="text-gradient">POKER EXPERIENCE</span>', '1win poker - platform overview'),
    ('POKER <span class="text-gradient-gold">PROMO CODE</span>', 'Poker promo code XLBONUS'),
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>', 'Claim your 600% bonus'),
])

# ── LIVE-STREAMING.HTML ───────────────────────────────────────────
print('\n== live-streaming.html ==')
with open(os.path.join(BASE, 'live-streaming.html'), 'r') as f:
    ls = f.read()

# Find all H2s in live-streaming and fix them
ls_h2_fixes = [
    (r'HOW TO WATCH LIVE', 'How to watch live'),
    (r'SPORTS COVERAGE', 'Sports coverage on 1win'),
    (r'LIVE STREAMING SPORTS', 'Live streaming sports'),
    (r'FEATURED SPORTS', 'Featured sports'),
    (r'HOW IT WORKS', 'How live streaming works at 1win'),
    (r'STREAMING FEATURES', 'Live streaming features'),
    (r'POPULAR SPORTS', 'Popular sports to stream'),
    (r'STREAMING FAQ', 'Frequently asked questions'),
    (r'LIVE STREAMING <span class="text-gradient[^"]*">[A-Z ]+</span>', lambda m: 'Live streaming coverage'),
]

for pat, repl in ls_h2_fixes:
    ls = re.sub(r'(<h2[^>]*>)([^<]*?)' + pat + r'([^<]*?)(</h2>)',
                lambda m, r=repl: m.group(1) + (r if isinstance(r,str) else r(m)) + m.group(5),
                ls, count=1, flags=re.IGNORECASE)

with open(os.path.join(BASE, 'live-streaming.html'), 'w') as f:
    f.write(ls)
print('  OK: live-streaming.html')

# ── PROMOTIONS.HTML ───────────────────────────────────────────────
print('\n== promotions.html ==')
with open(os.path.join(BASE, 'promotions.html'), 'r') as f:
    pr = f.read()

# Fix H2s
pr_h2_fixes = [
    ('WELCOME BONUS', 'Welcome bonus - 600% with XLBONUS'),
    ('VIP REWARDS', 'VIP rewards and cashback'),
    ('LUCKY DRIVE', 'Lucky Drive Lamborghini raffle'),
    ('CURRENT PROMOTIONS', 'Current 1win promotions'),
    ('ALL PROMOTIONS', 'All 2026 promotions'),
    ('BONUS OFFERS', 'Bonus offers at 1win'),
    ('CASINO TOURNAMENTS', 'Casino tournaments and drops'),
    ('SPORTS OFFERS', 'Sports betting promotions'),
]

for old_pat, new_text in pr_h2_fixes:
    pr = re.sub(
        r'(<h2[^>]*>)[^<]*' + old_pat + r'[^<]*(</h2>)',
        lambda m, t=new_text: m.group(1) + t + m.group(2),
        pr, count=1, flags=re.IGNORECASE
    )

with open(os.path.join(BASE, 'promotions.html'), 'w') as f:
    f.write(pr)
print('  OK: promotions.html')

# ── NEWS.HTML ─────────────────────────────────────────────────────
print('\n== news.html ==')
with open(os.path.join(BASE, 'news.html'), 'r') as f:
    nw = f.read()

# Fix ALL-CAPS H2s in news
nw = re.sub(r'(<h2[^>]*>)\s*LATEST\s+NEWS\s*(</h2>)',
            r'\1Latest 1win news\2', nw, flags=re.IGNORECASE)
nw = re.sub(r'(<h2[^>]*>)\s*ALL\s+NEWS\s*(</h2>)',
            r'\1All news\2', nw, flags=re.IGNORECASE)
nw = re.sub(r'(<h2[^>]*>)\s*PLATFORM\s+UPDATES\s*(</h2>)',
            r'\1Platform updates\2', nw, flags=re.IGNORECASE)
nw = re.sub(r'(<h2[^>]*>)\s*RECENT\s+NEWS\s*(</h2>)',
            r'\1Recent news\2', nw, flags=re.IGNORECASE)

with open(os.path.join(BASE, 'news.html'), 'w') as f:
    f.write(nw)
print('  OK: news.html')

# ── 1WIN-PROMO-CODE.HTML ──────────────────────────────────────────
print('\n== 1win-promo-code.html ==')
with open(os.path.join(BASE, '1win-promo-code.html'), 'r') as f:
    wpc = f.read()

# Fix ALL-CAPS H2s
pc_h2_fixes = [
    (r'HOW TO ACTIVATE\s+(?:THE\s+)?(?:1WIN\s+)?PROMO CODE', 'How to activate XLBONUS in four steps'),
    (r'BONUS\s+BREAKDOWN', 'The 600% bonus breakdown'),
    (r'PROMO CODE\s+TERMS', 'Bonus terms in plain English'),
    (r'WHY\s+USE\s+(?:A\s+)?PROMO CODE', 'Why XLBONUS beats the default offer'),
    (r'HOW\s+(?:THE\s+)?(?:600%?\s+)?BONUS\s+WORKS', 'How the 600% bonus works'),
    (r'CLAIM\s+(?:YOUR\s+)?(?:600%?\s+)?BONUS', 'Claim your 600% bonus with XLBONUS'),
    (r'FREQUENTLY ASKED\s+<span[^>]*>QUESTIONS</span>', 'Frequently asked questions'),
]

for pat, repl in pc_h2_fixes:
    wpc = re.sub(r'(<h2[^>]*>)[^<]*' + pat + r'[^<]*(</h2>)',
                 lambda m, r=repl: m.group(1) + r + m.group(m.lastindex),
                 wpc, count=1, flags=re.IGNORECASE)

with open(os.path.join(BASE, '1win-promo-code.html'), 'w') as f:
    f.write(wpc)
print('  OK: 1win-promo-code.html')

print('\nH2 fixes done.')
