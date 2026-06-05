#!/usr/bin/env python3
"""
Comprehensive EN rewrite script for all 21 category HTML pages.
Replaces all visible text while preserving markup, classes, scripts, styles.
"""
import re
import os

BASE = '/home/user/workspace/1win-codes-repo/en'

def rewrite_file(filename, replacements):
    """Apply a list of (old, new) string replacements to a file."""
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new, 1)
        else:
            print(f"  WARNING: string not found in {filename}: {repr(old[:80])}")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    changed = content != original
    print(f"  {'CHANGED' if changed else 'no change'}: {filename}")
    return changed


def rewrite_file_all(filename, replacements):
    """Apply replacements globally (replace_all=True for each)."""
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    changed = content != original
    print(f"  {'CHANGED' if changed else 'no change'}: {filename}")
    return changed


# ==============================================================================
# PROMO-CODE.HTML
# ==============================================================================
print("\n=== promo-code.html ===")
rewrite_file('promo-code.html', [
    # Title & meta
    ('<title>1win Promo Code XLBONUS 2026 — Get 600% Deposit Bonus</title>',
     '<title>1win Promo Code XLBONUS — Get 600% on Your First 4 Deposits (2026)</title>'),
    ('content="Activate 1win promo code XLBONUS in 2026 and get a 600% bonus on your first deposit. Follow our step-by-step guide to claim the biggest 1win welcome offer."',
     'content="Enter 1win promo code XLBONUS at registration to unlock a 200% + 150% + 100% + 50% bonus across your first four deposits. Up to $1,050 total. Crypto and card welcome. T&amp;Cs apply, 18+."'),
    ('content="1win Promo Code XLBONUS 2026 — Get 600% Deposit Bonus"',
     'content="1win Promo Code XLBONUS — Get 600% on Your First 4 Deposits (2026)"'),
    # H1
    ('1WIN PROMO CODE <span class="text-gradient-gold">XLBONUS</span>',
     '1win Promo Code <span class="text-gradient-gold">XLBONUS</span>'),
    # Hero subtitle
    ('<p class="hero-subtitle" style="max-width:640px;margin:0 auto 32px;">\n        The most generous welcome bonus in online betting. Four deposits. Up to 600% bonus. No strings attached — just pure value.\n      </p>',
     '<p class="hero-subtitle" style="max-width:640px;margin:0 auto 32px;">\n        The only code that splits the 600% welcome bonus across four deposits instead of one. Enter it once at signup. The bonuses unlock automatically.\n      </p>'),
    # CTA button
    ('CLAIM YOUR 600% BONUS',
     'Claim My 600% Bonus'),
    # Section: Bonus Breakdown
    ('BONUS <span class="text-gradient-gold">BREAKDOWN</span>',
     'The 600% breakdown - exactly what you get'),
    ('Your first four deposits are supercharged. Here\'s exactly how the 600% total bonus works.',
     'Most operators sell a "200% welcome bonus" and stop there. XLBONUS keeps paying across four deposits.'),
    # Deposit cards
    ('<h3>First Deposit</h3>\n          <div class="bonus-pct">200%</div>\n          <p>Double your money plus extra. Deposit $100, play with $300.</p>\n          <span class="deposit-max">Up to $500</span>',
     '<h3>First deposit</h3>\n          <div class="bonus-pct">200%</div>\n          <p>Crypto rate +200%, fiat rate +175%. Deposit $100, play with $300.</p>\n          <span class="deposit-max">Max $300</span>'),
    ('<h3>Second Deposit</h3>\n          <div class="bonus-pct">150%</div>\n          <p>Still massive. Deposit $100, play with $250.</p>\n          <span class="deposit-max">Up to $400</span>',
     '<h3>Second deposit</h3>\n          <div class="bonus-pct">150%</div>\n          <p>Crypto rate +150%, fiat rate +125%. Deposit $100, play with $250.</p>\n          <span class="deposit-max">Max $250</span>'),
    ('<h3>Third Deposit</h3>\n          <div class="bonus-pct">100%</div>\n          <p>A perfect match. Deposit $100, play with $200.</p>\n          <span class="deposit-max">Up to $300</span>',
     '<h3>Third deposit</h3>\n          <div class="bonus-pct">100%</div>\n          <p>Crypto rate +100%, fiat rate +75%. Deposit $100, play with $200.</p>\n          <span class="deposit-max">Max $200</span>'),
    ('<h3>Fourth Deposit</h3>\n          <div class="bonus-pct">50%</div>\n          <p>Still a solid boost. Deposit $100, play with $150.</p>\n          <span class="deposit-max">Up to $200</span>',
     '<h3>Fourth deposit</h3>\n          <div class="bonus-pct">50%</div>\n          <p>Crypto rate +50%, fiat rate +25%. Deposit $100, play with $150.</p>\n          <span class="deposit-max">Max $300</span>'),
    # HOW TO ACTIVATE section
    ('HOW TO <span class="text-gradient">ACTIVATE</span>',
     'How to activate XLBONUS in four steps'),
    ('Three quick steps. Under 60 seconds. Then the bonus is yours.',
     'Click, register, deposit. The 200% first-deposit bonus lands within 60 seconds.'),
    # Activation steps
    ('<h4>1. Register</h4>\n          <p>Create your 1win account. During registration, enter promo code <span class="code-highlight">XLBONUS</span> in the promo code field.</p>',
     '<h4>Step 1: Register</h4>\n          <p>Click any "Register with XLBONUS" button on this page. This pre-fills code <span class="code-highlight">XLBONUS</span> on the registration form.</p>'),
    ('<h4>2. Make a Deposit</h4>\n          <p>Deposit $10 or more using any payment method — crypto, card, or bank transfer. The bonus activates automatically.</p>',
     '<h4>Step 2: Pick your currency</h4>\n          <p>Fill in your phone, email and currency. Pick the currency that matches your payment method to avoid conversion fees.</p>'),
    ('<h4>3. Play & Win</h4>\n          <p>Your bonus is credited instantly. Start playing sports, casino, Aviator, or poker with your boosted balance.</p>',
     '<h4>Step 3: Confirm XLBONUS and deposit</h4>\n          <p>Confirm XLBONUS is in the "Promo code" field. Make your first deposit. The 200% bonus credit lands within 60 seconds. Repeat for deposits two through four to unlock the full 600%.</p>'),
    # Girl break - UNLOCK section
    ('UNLOCK <span class=\'text-gradient\'>600%</span>',
     'Unlock 600% with XLBONUS'),
    ('The biggest welcome bonus anywhere. Four deposits, each one boosted. Use code XLBONUS and start winning bigger.',
     'XLBONUS splits the 600% across four deposits instead of one. Crypto deposits qualify for the full 600% rate. Fiat deposits get 500%.'),
    ('Claim XLBONUS',
     'Register with XLBONUS'),
    # Terms section
    ('TERMS & <span class="text-gradient">CONDITIONS</span>',
     'Bonus terms in plain English'),
    ('Transparent and fair. Here\'s what you need to know.',
     'Everything you need to know before you deposit.'),
    ('<span class="term-val">5x</span>\n          <span class="term-label">Wagering Requirement</span>',
     '<span class="term-val">35x</span>\n          <span class="term-label">Slots wagering</span>'),
    ('<span class="term-val">$10</span>\n          <span class="term-label">Minimum Deposit</span>',
     '<span class="term-val">5x</span>\n          <span class="term-label">Sports wagering (odds 3.0+)</span>'),
    ('<span class="term-val">30</span>\n          <span class="term-label">Days Validity</span>',
     '<span class="term-val">30</span>\n          <span class="term-label">Days per bonus leg</span>'),
    ('Bonus must be wagered 5x before withdrawal. Bet $500 bonus × 5 = $2,500 in total wagers.',
     'Bonus credit must be wagered 35x on slots or 5x on sports bets at odds of 3.0 or higher.'),
    ('Minimum deposit of $10 required to activate the bonus on each deposit.',
     'Each bonus leg expires 30 days after the deposit that triggered it. Max bet while wagering: $5 per spin on slots, $10 per ticket on sports.'),
    ('Bonus expires 30 days after activation if wagering is not completed.',
     'Real-money balance is wagered first, bonus balance second. Bonus funds become withdrawable once wagering is complete.'),
    ('Accumulator bets (3+ events, 1.40+ odds each) count toward wagering requirements.',
     'Eligibility: one bonus per household, IP, payment method and device. Account verification (KYC) required before first withdrawal.'),
    ('One promo code per account. XLBONUS cannot be combined with other welcome offers.',
     'Wagering must be completed inside the 30-day validity window or the bonus credit returns to 1win.'),
    # WHY XLBONUS section
    ('WHY <span class="text-gradient-gold">XLBONUS</span>?',
     'Why XLBONUS beats the default 1win sign-up offer'),
    ('See how XLBONUS stacks up against registering without a promo code.',
     'Without a code, 1win pays a base 200% on deposit one only. XLBONUS triples the total bonus pool and stretches it across four deposits.'),
    ('<td class="col-no-code"><span class="check-no">✗</span> Standard 100%</td>',
     '<td class="col-no-code"><span class="check-no">✗</span> Base 200%</td>'),
    ('<td class="col-xlbonus"><span class="check-yes">✓</span> $1,400</td>',
     '<td class="col-xlbonus"><span class="check-yes">✓</span> Up to $1,050</td>'),
    ('<td class="col-no-code"><span class="check-no">✗</span> $300</td>',
     '<td class="col-no-code"><span class="check-no">✗</span> Up to $300</td>'),
    ('<td class="col-no-code"><span class="check-no">—</span> 5x</td>',
     '<td class="col-no-code">35x slots / 5x sports</td>'),
    # OTHER PROMOS section
    ('OTHER <span class="text-gradient">PROMOTIONS</span>',
     'Other current 1win promotions'),
    ('XLBONUS is just the beginning. Check out these other ways to win big.',
     'Active promotions running alongside the welcome bonus.'),
    ('<h4>🏆 VIP Club</h4>\n          <p>Rise through 5 tiers for exclusive perks: personal manager, luxury gifts, higher limits, and priority withdrawals.</p>',
     '<h4>VIP Club</h4>\n          <p>Five tiers from Bronze to Diamond. Weekly cashback up to 30%. Personal manager from Gold tier. Every real-money bet earns Loyalty Points.</p>'),
    ('<h4>🚗 Lucky Drive</h4>\n          <p>Win a Lamborghini Urus SE worth $240,000. Every bet earns you automatic raffle tickets.</p>',
     '<h4>Lucky Drive raffle</h4>\n          <p>Lamborghini Urus SE, $240,000 prize. One automatic ticket per real-money bet of $1 or more. Draw: 31 December 2026.</p>'),
    ('<h4>🎰 Tournaments</h4>\n          <p>Compete in weekly casino and sports tournaments with prize pools up to $100,000.</p>',
     '<h4>Weekly cashback and boost</h4>\n          <p>Up to 30% of net losses returned on Monday (VIP-tier dependent). Accumulator boost: +7% to +15% on accas of 4+ legs.</p>'),
    # COUNTRY GUIDES section
    ('COUNTRY <span class="text-gradient">GUIDES</span>',
     'Country promo guides'),
    ('Step-by-step registration and bonus guides for 1win in your country, with local payment methods, currency, and example deposit amounts.',
     'Dedicated walkthroughs with local currency, local payment methods, and country-specific bonus amounts in your currency.'),
    # Final CTA banner
    ('MORE TO <span class=\'text-gradient-gold\'>WIN</span>',
     'More with XLBONUS'),
    ('Beyond the welcome bonus — cashback, free spins, tournament entries, and VIP rewards. The perks never stop.',
     'The welcome bonus is the start. Weekly cashback, accumulator boosts, Lucky Drive tickets, and VIP rewards all stack on top.'),
    ('See All Bonuses',
     'Register with XLBONUS'),
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span> NOW',
     'Claim your 600% bonus now'),
    ('Don\'t leave money on the table. Register with XLBONUS and start with up to 5x your deposit.',
     'Code XLBONUS must be entered on the registration form. It cannot be added after signup. Up to $1,050 total bonus credit.'),
    ('SIGN UP WITH XLBONUS',
     'Register with XLBONUS'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.',
     '1win.codes — independent affiliate review'),
])


# ==============================================================================
# AVIATOR.HTML
# ==============================================================================
print("\n=== aviator.html ===")
with open(os.path.join(BASE, 'aviator.html'), 'r') as f:
    av = f.read()

av_replacements = [
    # Meta
    ('<title>1win Aviator — Crash Game | Use Promo Code XLBONUS</title>',
     '<title>1win Aviator — Play the Original Crash Game with Code XLBONUS</title>'),
    ('content="Play Aviator on 1win — the provably fair crash game where you control the multiplier. Use promo code XLBONUS for a 600% deposit bonus to boost your stakes."',
     'content="Play Aviator at 1win with provably fair multipliers, dual-bet mode and 24/7 cash-out. Activate promo code XLBONUS for a 600% deposit bonus to boost your stakes. Free demo available."'),
    ('content="1win Aviator — Crash Game | Use Promo Code XLBONUS"',
     'content="1win Aviator — Play the Original Crash Game with Code XLBONUS"'),
    # H1
    ('1WIN <span class="text-gradient-gold">AVIATOR</span>',
     '1win <span class="text-gradient-gold">Aviator</span>'),
    # HOW IT WORKS
    ('HOW <span class="text-gradient">IT WORKS</span>',
     'How the game works in 90 seconds'),
    # WHEN TO CASH OUT
    ('WHEN TO <span class="text-gradient-gold">CASH OUT</span>',
     'When to cash out'),
    # Girl break - RIDE THE WAVE
    ("RIDE THE <span class='text-gradient'>WAVE</span>",
     'Play Aviator with XLBONUS'),
    # AVIATOR STATISTICS
    ('AVIATOR <span class="text-gradient">STATISTICS</span>',
     'Aviator round statistics (last 100 rounds, sample)'),
    # AUTO-BET FEATURES
    ('AUTO-BET <span class="text-gradient">FEATURES</span>',
     'Aviator features at 1win'),
    # PRO TIPS
    ('PRO <span class="text-gradient-gold">TIPS</span>',
     'Cash-out strategies and habits'),
    # NERVES OF STEEL
    ("NERVES OF <span class='text-gradient-gold'>STEEL</span>",
     'Related crash games on 1win'),
    # WHY PLAY AVIATOR AT 1WIN
    ('WHY PLAY <span class="text-gradient">AVIATOR AT 1WIN</span>',
     'Aviator on 1win with XLBONUS'),
    # AVIATOR PROMO CODE
    ('AVIATOR <span class="text-gradient-gold">PROMO CODE</span>',
     'Aviator promo code XLBONUS'),
    # Big CTA H2
    ('GET 600% MORE TO PLAY AVIATOR — <span class="text-gradient-gold">600% BONUS</span>',
     'Get 600% more to play Aviator'),
    # FAQ H2
    ('FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>',
     'Frequently asked questions'),
]

for old, new in av_replacements:
    if old in av:
        av = av.replace(old, new, 1)
    else:
        print(f"  WARNING not found: {repr(old[:80])}")

with open(os.path.join(BASE, 'aviator.html'), 'w') as f:
    f.write(av)
print("  CHANGED: aviator.html")


# ==============================================================================
# CASINO.HTML
# ==============================================================================
print("\n=== casino.html ===")
with open(os.path.join(BASE, 'casino.html'), 'r') as f:
    ca = f.read()

ca_replacements = [
    # Meta
    ('<title>1win Casino — 11,000+ Slots &amp; Live Games | XLBONUS</title>',
     '<title>1win Casino — 11,000+ Slots and Live Tables | XLBONUS 600%</title>'),
    ('content="Play 11,000+ slots, live dealer tables, and jackpots at 1win Casino. Enter promo code XLBONUS to collect your 600% welcome bonus and start winning today."',
     'content="Play 11,000+ casino games at 1win: slots, live blackjack, roulette and jackpots from Pragmatic Play, Evolution, NetEnt and 67 more providers. Use code XLBONUS for a 600% welcome bonus."'),
    ('content="1win Casino — 11,000+ Games | Promo Code XLBONUS"',
     'content="1win Casino — 11,000+ Slots and Live Tables | XLBONUS 600%"'),
    # H1
    ('1WIN <span class="text-gradient">CASINO</span>',
     '1win <span class="text-gradient">Casino</span>'),
    # GAME CATEGORIES
    ('GAME <span class="text-gradient">CATEGORIES</span>',
     'Game categories'),
    # TOP PROVIDERS
    ('TOP <span class="text-gradient-gold">PROVIDERS</span>',
     'Top providers on the platform'),
    # Girl break - FEEL THE THRILL (BANNED)
    ("FEEL THE <span class='text-gradient'>THRILL</span>",
     'Claim your 600% casino bonus'),
    # LIVE CASINO
    ('LIVE <span class="text-gradient">CASINO</span>',
     'Live casino at 1win'),
    # CURRENT JACKPOTS
    ('CURRENT <span class="text-gradient-gold">JACKPOTS</span>',
     'Current jackpots'),
    # EXCLUSIVE FEATURES
    ('EXCLUSIVE <span class="text-gradient">FEATURES</span>',
     'Tournaments and drops'),
    # JACKPOTS AWAIT
    ("JACKPOTS <span class='text-gradient-gold'>AWAIT</span>",
     'Daily and weekly rewards'),
    # WHY PLAY AT 1WIN CASINO
    ('WHY PLAY AT <span class="text-gradient">1WIN CASINO</span>',
     'Why play at 1win casino'),
    # 1WIN CASINO PROMO CODE
    ('1WIN CASINO <span class="text-gradient-gold">PROMO CODE</span>',
     '1win casino promo code XLBONUS'),
    # Big CTA H2
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>',
     'Claim your 600% bonus'),
    # FAQ
    ('FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>',
     'Frequently asked questions'),
]

for old, new in ca_replacements:
    if old in ca:
        ca = ca.replace(old, new, 1)
    else:
        print(f"  WARNING not found: {repr(old[:80])}")

with open(os.path.join(BASE, 'casino.html'), 'w') as f:
    f.write(ca)
print("  CHANGED: casino.html")


# ==============================================================================
# SPORTS-BETTING.HTML
# ==============================================================================
print("\n=== sports-betting.html ===")
with open(os.path.join(BASE, 'sports-betting.html'), 'r') as f:
    sb = f.read()

sb_replacements = [
    # Meta
    ('<title>', '<title>'),  # placeholder
]

# Re-read fresh
with open(os.path.join(BASE, 'sports-betting.html'), 'r') as f:
    sb = f.read()

# Find actual title
sb_title_old = re.search(r'<title>([^<]+)</title>', sb)
if sb_title_old:
    old_title = sb_title_old.group(0)
    sb = sb.replace(old_title, '<title>1win Sportsbook — 30+ Sports, Live Cash-Out and Streaming | XLBONUS</title>', 1)

sb_desc_old = re.search(r'(<meta name="description" content=")[^"]+(")', sb)
if sb_desc_old:
    sb = sb.replace(sb_desc_old.group(0), 
        '<meta name="description" content="Bet on 30+ sports at 1win: football, cricket, tennis, basketball, MMA and esports. Live in-play, cash-out on every selection, free streams on selected matches. Code XLBONUS unlocks 600% bonus.">', 1)

sb_og_title = re.search(r'(<meta property="og:title" content=")[^"]+(")', sb)
if sb_og_title:
    sb = sb.replace(sb_og_title.group(0),
        '<meta property="og:title" content="1win Sportsbook — 30+ Sports, Live Cash-Out and Streaming | XLBONUS">', 1)

sb_og_desc = re.search(r'(<meta property="og:description" content=")[^"]+(")', sb)
if sb_og_desc:
    sb = sb.replace(sb_og_desc.group(0),
        '<meta property="og:description" content="Bet on 30+ sports at 1win: football, cricket, tennis, basketball, MMA and esports. Live in-play, cash-out on every selection, free streams on selected matches. Code XLBONUS unlocks 600% bonus.">', 1)

# H1 - find and replace
sb = re.sub(r'1WIN\s+<span class="text-gradient(?:-gold)?">SPORTS\s*(?:BETTING)?</span>', 
            'Sports betting at 1win', sb, count=1)
# Try alternate pattern
sb = re.sub(r'(<h1[^>]*>)[^<]*1WIN[^<]*SPORT[^<]*(</h1>)',
            r'\1Sports betting at 1win\2', sb, count=1)

# H2 replacements
h2_replacements = [
    (r'SPORTS\s+(?:WE\s+)?COVER(?:AGE)?', 'Sports we cover'),
    (r'HOW\s+(?:LIVE\s+)?BETTING\s+WORKS', 'How live betting works'),
    (r'TYPES?\s+OF\s+BET', 'Types of bet at 1win'),
    (r'HOW\s+TO\s+(?:PLACE\s+A\s+)?BET', 'How to place a bet in three steps'),
    (r'SPORTS?\s+BONUSES?', 'Bonuses for sports bettors'),
    (r'LIVE\s+THE\s+ACTION', 'Place your first bet'),
    (r'DOMINATE\s+EVERY\s+MATCH', 'Sports betting with XLBONUS'),
    (r'OUTPLAY\s+EVERYONE', 'Bet with XLBONUS'),
    (r'BET\s+ANYWHERE\.?\s*WIN\s+EVERYWHERE\.?', 'Bet on 30+ sports'),
    (r'FREQUENTLY\s+ASKED\s+<span[^>]*>QUESTIONS</span>', 'Frequently asked questions'),
]

for pat, repl in h2_replacements:
    sb = re.sub(r'(<h2[^>]*>)([^<]*?)' + pat + r'([^<]*?)(</h2>)', 
                lambda m: m.group(1) + repl + m.group(4), 
                sb, count=1, flags=re.IGNORECASE)

# Girl break slogans
sb = re.sub(r"LIVE\s+THE\s+<span class='text-gradient(?:-gold)?'>\s*ACTION\s*</span>",
            "Sports betting at 1win", sb, count=1)
sb = re.sub(r"DOMINATE\s+EVERY\s+<span class='text-gradient(?:-gold)?'>\s*MATCH\s*</span>",
            "Bet on 30+ sports with XLBONUS", sb, count=1)

# Big CTA text
sb = re.sub(r"BET ANYWHERE\.\s*WIN EVERYWHERE\.", "Bet on 30+ sports at 1win", sb)

with open(os.path.join(BASE, 'sports-betting.html'), 'w') as f:
    f.write(sb)
print("  CHANGED: sports-betting.html")


# ==============================================================================
# APP.HTML
# ==============================================================================
print("\n=== app.html ===")
with open(os.path.join(BASE, 'app.html'), 'r') as f:
    ap = f.read()

ap_title = re.search(r'<title>([^<]+)</title>', ap)
if ap_title:
    ap = ap.replace(ap_title.group(0), '<title>1win App Download — iOS, Android APK and Mobile Web | XLBONUS</title>', 1)

ap_desc = re.search(r'(<meta name="description" content=")[^"]+(")', ap)
if ap_desc:
    ap = ap.replace(ap_desc.group(0), 
        '<meta name="description" content="Download the 1win app for iOS or Android (APK direct or Google Play). Bet live, stream matches, deposit via UPI, PIX, crypto. Promo code XLBONUS gives 600% welcome bonus.">', 1)

ap_og_title = re.search(r'(<meta property="og:title" content=")[^"]+(")', ap)
if ap_og_title:
    ap = ap.replace(ap_og_title.group(0), '<meta property="og:title" content="1win App Download — iOS, Android APK and Mobile Web | XLBONUS">', 1)

ap_og_desc = re.search(r'(<meta property="og:description" content=")[^"]+(")', ap)
if ap_og_desc:
    ap = ap.replace(ap_og_desc.group(0), '<meta property="og:description" content="Download the 1win app for iOS or Android (APK direct or Google Play). Bet live, stream matches, deposit via UPI, PIX, crypto. Promo code XLBONUS gives 600% welcome bonus.">', 1)

# H1
ap = re.sub(r'(<h1[^>]*>)[^<]*(?:DOWNLOAD|DOWNLOAD THE)[^<]*(</h1>)',
            r'\1Download the 1win app\2', ap, count=1)
ap = re.sub(r'1WIN\s+<span[^>]*>APP</span>', 'Download the 1win app', ap, count=1)
ap = re.sub(r'1WIN APP\s*<span[^>]*>', 'Download the 1win app\n      <span class="invisible">', ap, count=1)

# H2 replacements using regex
app_h2 = [
    (r'APP\s+(?:VS\.?\s+)?(?:MOBILE\s+)?(?:WEB|BROWSER)', 'What the app gives you that the site does not'),
    (r'(?:HOW\s+TO\s+)?INSTALL\s+(?:THE\s+)?APP', 'Install in three steps'),
    (r'APP\s+PERMISSIONS?\s+(?:EXPLAINED)?', 'App permissions explained'),
    (r'(?:FIRST\s+)?DEPOSIT\s+(?:VIA|WITH|ON)\s+(?:THE\s+)?APP', 'First deposit with code XLBONUS via the app'),
    (r'TAKE\s+FLIGHT', 'Download the 1win app now'),
    (r'DRIVE\s+YOUR\s+DREAM', 'Download and play'),
    (r'FREQUENTLY\s+ASKED\s+<span[^>]*>QUESTIONS</span>', 'Frequently asked questions'),
]

for pat, repl in app_h2:
    ap = re.sub(pat, repl, ap, count=1, flags=re.IGNORECASE)

# Girl break slogan
ap = re.sub(r"TAKE\s+<span class='text-gradient(?:-gold)?'>\s*FLIGHT\s*</span>",
            "Download the 1win app", ap, count=1)
ap = re.sub(r"DRIVE\s+YOUR\s+<span class='text-gradient(?:-gold)?'>\s*DREAM\s*</span>",
            "Play anywhere with XLBONUS", ap, count=1)

with open(os.path.join(BASE, 'app.html'), 'w') as f:
    f.write(ap)
print("  CHANGED: app.html")


print("\nBatch 1 complete.")
