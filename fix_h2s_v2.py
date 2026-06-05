#!/usr/bin/env python3
"""Fix ALL-CAPS H2s for live-streaming, promotions, news, 1win-promo-code."""
import os, re

BASE = '/home/user/workspace/1win-codes-repo/en'

def fix_h2_allcaps(content, old_inner, new_inner):
    """Replace H2 inner text. old_inner is the text between h2 tags (no HTML tags)."""
    return content.replace(old_inner, new_inner, 1)

def load(fname):
    with open(os.path.join(BASE, fname), 'r') as f:
        return f.read()

def save(fname, s):
    with open(os.path.join(BASE, fname), 'w') as f:
        f.write(s)

# ── LIVE-STREAMING.HTML ───────────────────────────────────────────
print('\n== live-streaming.html ==')
ls = load('live-streaming.html')

ls_fixes = [
    # Find exact H2 text patterns
]

# Direct string replacements for H2 content-title patterns
ls_h2_pairs = [
    ('content-title center anim-fade-up">HOW TO WATCH', 'content-title center anim-fade-up">How to watch'),
    ('content-title center anim-fade-up">SPORTS COVERAGE', 'content-title center anim-fade-up">Sports coverage'),
    ('content-title center anim-fade-up">FEATURED', 'content-title center anim-fade-up">Featured'),
    ('content-title center anim-fade-up">STREAMING FEATURES', 'content-title center anim-fade-up">Streaming features'),
    ('content-title center anim-fade-up">POPULAR SPORTS', 'content-title center anim-fade-up">Popular sports to stream'),
    ('content-title center anim-fade-up">STREAMING FAQ', 'content-title center anim-fade-up">Frequently asked questions'),
    ('content-title center anim-fade-up">LIVE STREAMING', 'content-title center anim-fade-up">Live streaming'),
    ('content-title center anim-fade-up">AVAILABLE SPORTS', 'content-title center anim-fade-up">Available sports'),
    ('section-title">LIVE STREAMING', 'section-title">Live streaming'),
    ('section-title">HOW TO STREAM', 'section-title">How to stream'),
    ('section-title">STREAMING SPORTS', 'section-title">Streaming sports'),
    ('cta-banner-title">WATCH LIVE AND', 'cta-banner-title">Watch live and'),
    ('girl-break-title anim-fade-up">CATCH IT LIVE</h2>', 'girl-break-title anim-fade-up">Watch live with 1win</h2>'),
    ('girl-break-title anim-fade-up">STREAM AND BET', 'girl-break-title anim-fade-up">Stream and bet at 1win'),
    # CTA banner
    ('WATCH LIVE. BET LIVE.', 'Watch live. Bet live.'),
    ('STREAM AND BET', 'Stream and bet at 1win'),
]

for old, new in ls_h2_pairs:
    ls = ls.replace(old, new)

save('live-streaming.html', ls)
print('  OK: live-streaming.html')

# ── PROMOTIONS.HTML ───────────────────────────────────────────────
print('\n== promotions.html ==')
pr = load('promotions.html')

pr_pairs = [
    ('section-title">ALL <span class="text-gradient">PROMOTIONS</span>', 
     'section-title">All 2026 promotions'),
    ('section-title">CURRENT <span class="text-gradient">PROMOTIONS</span>',
     'section-title">Current 1win promotions'),
    ('section-title">WELCOME <span class="text-gradient">BONUS</span>',
     'section-title">Welcome bonus - 600% with XLBONUS'),
    ('section-title">VIP <span class="text-gradient-gold">REWARDS</span>',
     'section-title">VIP rewards and cashback'),
    ('section-title">LUCKY <span class="text-gradient">DRIVE</span>',
     'section-title">Lucky Drive Lamborghini raffle'),
    ('section-title">CASINO <span class="text-gradient">TOURNAMENTS</span>',
     'section-title">Casino tournaments and drops'),
    ('section-title">SPORTS <span class="text-gradient-gold">OFFERS</span>',
     'section-title">Sports betting promotions'),
    ('section-title">BONUS <span class="text-gradient">OFFERS</span>',
     'section-title">Bonus offers at 1win'),
    # Also the hero H1 area
    ('hero-title" style="margin-bottom:16px;">1WIN <span class="text-gradient">PROMOTIONS</span>',
     'hero-title" style="margin-bottom:16px;">1win promotions 2026'),
]

for old, new in pr_pairs:
    pr = pr.replace(old, new, 1)

save('promotions.html', pr)
print('  OK: promotions.html')

# ── NEWS.HTML ─────────────────────────────────────────────────────
print('\n== news.html ==')
nw = load('news.html')

nw_pairs = [
    ('content-title center anim-fade-up">LATEST <span class="text-gradient">NEWS</span>',
     'content-title center anim-fade-up">Latest 1win news'),
    ('content-title center anim-fade-up">RECENT <span class="text-gradient">NEWS</span>',
     'content-title center anim-fade-up">Recent news'),
    ('section-title">ALL <span class="text-gradient">NEWS</span>',
     'section-title">All news'),
    ('section-title">1WIN <span class="text-gradient">NEWS</span>',
     'section-title">1win news 2026'),
    # hero title fix (from fix_h1s.py ran already - just make sure)
    ('page-hero-title anim-fade-up">1win news 2026', 
     'page-hero-title anim-fade-up">1win news 2026'),
]

for old, new in nw_pairs:
    nw = nw.replace(old, new, 1)

save('news.html', nw)
print('  OK: news.html')

# ── 1WIN-PROMO-CODE.HTML ──────────────────────────────────────────
print('\n== 1win-promo-code.html ==')
wpc = load('1win-promo-code.html')

wpc_pairs = [
    # H2s 
    ('content-title center anim-fade-up">HOW TO ACTIVATE',
     'content-title center anim-fade-up">How to activate XLBONUS'),
    ('content-title center anim-fade-up">BONUS <span class="text-gradient">BREAKDOWN</span>',
     'content-title center anim-fade-up">The 600% bonus breakdown'),
    ('content-title center anim-fade-up">BONUS <span class="text-gradient-gold">BREAKDOWN</span>',
     'content-title center anim-fade-up">The 600% bonus breakdown'),
    ('content-title center anim-fade-up">PROMO CODE <span class="text-gradient">TERMS</span>',
     'content-title center anim-fade-up">Bonus terms in plain English'),
    ('content-title center anim-fade-up">WHY USE <span class="text-gradient">XLBONUS</span>',
     'content-title center anim-fade-up">Why XLBONUS beats the default offer'),
    ('content-title center anim-fade-up">HOW THE BONUS WORKS',
     'content-title center anim-fade-up">How the 600% bonus works'),
    ('content-title center anim-fade-up">HOW THE <span class="text-gradient">BONUS WORKS</span>',
     'content-title center anim-fade-up">How the 600% bonus works'),
    ('content-title center anim-fade-up">FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>',
     'content-title center anim-fade-up">Frequently asked questions'),
    # girl-break and CTA banner
    ("girl-break-title anim-fade-up\">TAKE YOUR <span class='text-gradient'>BONUS</span>",
     'girl-break-title anim-fade-up">Take your bonus'),
    ('cta-banner-title">CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>',
     'cta-banner-title">Claim your 600% bonus'),
    # Section titles
    ('section-title">HOW TO <span class="text-gradient">ACTIVATE</span>',
     'section-title">How to activate XLBONUS in four steps'),
    ('section-title">BONUS <span class="text-gradient">BREAKDOWN</span>',
     'section-title">The 600% bonus breakdown'),
    ('section-title">PROMO CODE <span class="text-gradient">TERMS</span>',
     'section-title">Bonus terms in plain English'),
    ('section-title">WHY USE <span class="text-gradient">XLBONUS</span>',
     'section-title">Why XLBONUS beats the default offer'),
    ('section-title">FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>',
     'section-title">Frequently asked questions'),
]

for old, new in wpc_pairs:
    wpc = wpc.replace(old, new, 1)

save('1win-promo-code.html', wpc)
print('  OK: 1win-promo-code.html')

print('\nH2 v2 fixes done.')
