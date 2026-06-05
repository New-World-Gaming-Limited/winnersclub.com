#!/usr/bin/env python3
"""
Full EN rewrite for all 21 category pages.
Performs targeted string replacements preserving markup.
"""
import re, os

BASE = '/home/user/workspace/1win-codes-repo/en'

def rw(fname, pairs):
    """Apply (old,new) pairs to file. Reports missing strings."""
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    orig = s
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new, 1)
        else:
            print(f'  MISS [{fname}]: {repr(old[:70])}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'  {"OK" if s!=orig else "no-op"}: {fname}')

def rw_re(fname, pairs):
    """Apply (pattern,replacement) regex pairs to file."""
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    orig = s
    for pat, new in pairs:
        s = re.sub(pat, new, s, count=1, flags=re.IGNORECASE|re.DOTALL)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'  {"OK" if s!=orig else "no-op"}: {fname}')

# ─────────────────────────────────────────────────────────────────
# 1. PROMO-CODE.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== promo-code.html ==')
rw('promo-code.html', [
    ('<title>1win Promo Code XLBONUS 2026 — Get 600% Deposit Bonus</title>',
     '<title>1win Promo Code XLBONUS — Get 600% on Your First 4 Deposits (2026)</title>'),
    ('content="Activate 1win promo code XLBONUS in 2026 and get a 600% bonus on your first deposit. Follow our step-by-step guide to claim the biggest 1win welcome offer."',
     'content="Enter 1win promo code XLBONUS at registration to unlock a 200% + 150% + 100% + 50% bonus across your first four deposits. Up to $1,050 total. Crypto and card welcome. T&amp;Cs apply, 18+."'),
    ('og:title" content="1win Promo Code XLBONUS 2026 — Get 600% Deposit Bonus"',
     'og:title" content="1win Promo Code XLBONUS — Get 600% on Your First 4 Deposits (2026)"'),
    # H1
    ('1WIN PROMO CODE <span class="text-gradient-gold">XLBONUS</span>',
     '1win Promo Code <span class="text-gradient-gold">XLBONUS</span>'),
    # Hero subtitle
    ('The most generous welcome bonus in online betting. Four deposits. Up to 600% bonus. No strings attached — just pure value.',
     'The only code that splits the 600% welcome bonus across four deposits instead of one. Enter it once at signup. The bonuses unlock automatically.'),
    # CTA
    ('CLAIM YOUR 600% BONUS',
     'Claim My 600% Bonus'),
    # Section titles H2
    ('BONUS <span class="text-gradient-gold">BREAKDOWN</span>',
     'The 600% breakdown - exactly what you get'),
    ('Your first four deposits are supercharged. Here\'s exactly how the 600% total bonus works.',
     'Most operators sell a "200% welcome bonus" and stop there. XLBONUS keeps paying across four deposits.'),
    # Deposit cards
    ('<h3>First Deposit</h3>\n          <div class="bonus-pct">200%</div>\n          <p>Double your money plus extra. Deposit $100, play with $300.</p>\n          <span class="deposit-max">Up to $500</span>',
     '<h3>First deposit</h3>\n          <div class="bonus-pct">200%</div>\n          <p>Crypto rate +200%, fiat rate +175%. Example: deposit $100, play with $300.</p>\n          <span class="deposit-max">Max $300</span>'),
    ('<h3>Second Deposit</h3>\n          <div class="bonus-pct">150%</div>\n          <p>Still massive. Deposit $100, play with $250.</p>\n          <span class="deposit-max">Up to $400</span>',
     '<h3>Second deposit</h3>\n          <div class="bonus-pct">150%</div>\n          <p>Crypto rate +150%, fiat rate +125%. Example: deposit $100, play with $250.</p>\n          <span class="deposit-max">Max $250</span>'),
    ('<h3>Third Deposit</h3>\n          <div class="bonus-pct">100%</div>\n          <p>A perfect match. Deposit $100, play with $200.</p>\n          <span class="deposit-max">Up to $300</span>',
     '<h3>Third deposit</h3>\n          <div class="bonus-pct">100%</div>\n          <p>Crypto rate +100%, fiat rate +75%. Example: deposit $100, play with $200.</p>\n          <span class="deposit-max">Max $200</span>'),
    ('<h3>Fourth Deposit</h3>\n          <div class="bonus-pct">50%</div>\n          <p>Still a solid boost. Deposit $100, play with $150.</p>\n          <span class="deposit-max">Up to $200</span>',
     '<h3>Fourth deposit</h3>\n          <div class="bonus-pct">50%</div>\n          <p>Crypto rate +50%, fiat rate +25%. Example: deposit $100, play with $150.</p>\n          <span class="deposit-max">Max $300</span>'),
    # HOW TO ACTIVATE
    ('HOW TO <span class="text-gradient">ACTIVATE</span>',
     'How to activate XLBONUS in four steps'),
    ('Three quick steps. Under 60 seconds. Then the bonus is yours.',
     'Click, register, deposit. The 200% first-deposit bonus lands within 60 seconds.'),
    ('<h4>1. Register</h4>\n          <p>Create your 1win account. During registration, enter promo code <span class="code-highlight">XLBONUS</span> in the promo code field.</p>',
     '<h4>Step 1: Register</h4>\n          <p>Click any "Register with XLBONUS" button on this page. Code <span class="code-highlight">XLBONUS</span> is pre-filled on the form.</p>'),
    ('<h4>2. Make a Deposit</h4>\n          <p>Deposit $10 or more using any payment method — crypto, card, or bank transfer. The bonus activates automatically.</p>',
     '<h4>Step 2: Pick your currency</h4>\n          <p>Fill in your phone, email and currency. Pick the currency that matches your payment method to avoid conversion fees.</p>'),
    ('<h4>3. Play & Win</h4>\n          <p>Your bonus is credited instantly. Start playing sports, casino, Aviator, or poker with your boosted balance.</p>',
     '<h4>Step 3: Confirm code and deposit</h4>\n          <p>Confirm XLBONUS appears in the "Promo code" field. Make your first deposit. Bonus credit lands in 60 seconds. Repeat for deposits two through four.</p>'),
    # Girl break 1
    ('UNLOCK <span class=\'text-gradient\'>600%</span>',
     'Unlock 600% with XLBONUS'),
    ('The biggest welcome bonus anywhere. Four deposits, each one boosted. Use code XLBONUS and start winning bigger.',
     'XLBONUS splits the 600% across four deposits instead of one. Crypto deposits qualify for the full 600% rate. Fiat deposits get 500%.'),
    ('Claim XLBONUS',
     'Register with XLBONUS'),
    # Terms
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
     'Each bonus leg expires 30 days after the deposit that triggered it. Max bet while wagering: $5 per spin on slots.'),
    ('Bonus expires 30 days after activation if wagering is not completed.',
     'Real-money balance is wagered first, bonus balance second. Bonus becomes withdrawable once wagering is complete.'),
    ('Accumulator bets (3+ events, 1.40+ odds each) count toward wagering requirements.',
     'One bonus per household, IP, payment method and device. KYC required before first withdrawal.'),
    ('One promo code per account. XLBONUS cannot be combined with other welcome offers.',
     'Wagering must complete inside the 30-day validity window or bonus credit returns to 1win.'),
    # WHY XLBONUS
    ('WHY <span class="text-gradient-gold">XLBONUS</span>?',
     'Why XLBONUS beats the default 1win sign-up offer'),
    ('See how XLBONUS stacks up against registering without a promo code.',
     'Without a code, 1win pays a base 200% on deposit one only. XLBONUS stretches bonus across four deposits.'),
    ('<td class="col-no-code"><span class="check-no">✗</span> Standard 100%</td>',
     '<td class="col-no-code"><span class="check-no">✗</span> Base 200% on 1 deposit</td>'),
    ('<td class="col-xlbonus"><span class="check-yes">✓</span> $1,400</td>',
     '<td class="col-xlbonus"><span class="check-yes">✓</span> Up to $1,050</td>'),
    ('<td class="col-no-code"><span class="check-no">✗</span> $300</td>',
     '<td class="col-no-code"><span class="check-no">✗</span> Up to $300</td>'),
    ('<td class="col-no-code"><span class="check-no">—</span> 5x</td>',
     '<td class="col-no-code">35x slots / 5x sports</td>'),
    # OTHER PROMOS
    ('OTHER <span class="text-gradient">PROMOTIONS</span>',
     'Other current 1win promotions'),
    ('XLBONUS is just the beginning. Check out these other ways to win big.',
     'Active promotions running alongside the welcome bonus.'),
    ('<h4>🏆 VIP Club</h4>\n          <p>Rise through 5 tiers for exclusive perks: personal manager, luxury gifts, higher limits, and priority withdrawals.</p>',
     '<h4>VIP Club - 5 tiers</h4>\n          <p>Five tiers from Bronze to Diamond. Weekly cashback up to 30%. Personal manager from Gold tier. Auto-enrolled at first real-money deposit.</p>'),
    ('<h4>🚗 Lucky Drive</h4>\n          <p>Win a Lamborghini Urus SE worth $240,000. Every bet earns you automatic raffle tickets.</p>',
     '<h4>Lucky Drive raffle</h4>\n          <p>Lamborghini Urus SE, $240,000 prize. One automatic ticket per real-money bet of $1 or more. Draw: 31 December 2026.</p>'),
    ('<h4>🎰 Tournaments</h4>\n          <p>Compete in weekly casino and sports tournaments with prize pools up to $100,000.</p>',
     '<h4>Weekly cashback and boost</h4>\n          <p>Up to 30% of net losses returned on Mondays (VIP-tier dependent). Accumulator boost: +7% to +15% on accas of 4 or more legs.</p>'),
    # COUNTRY GUIDES
    ('COUNTRY <span class="text-gradient">GUIDES</span>',
     'Country promo guides'),
    ('Step-by-step registration and bonus guides for 1win in your country, with local payment methods, currency, and example deposit amounts.',
     'Dedicated walkthroughs with local currency, local payment methods, and country-specific bonus amounts.'),
    # Girl break 2
    ('MORE TO <span class=\'text-gradient-gold\'>WIN</span>',
     'More with XLBONUS'),
    ('Beyond the welcome bonus — cashback, free spins, tournament entries, and VIP rewards. The perks never stop.',
     'The welcome bonus is the start. Weekly cashback, accumulator boosts, Lucky Drive tickets, and VIP rewards all stack on top.'),
    ('See All Bonuses',
     'Register with XLBONUS'),
    # Final CTA banner
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span> NOW',
     'Claim your 600% bonus now'),
    ('Don\'t leave money on the table. Register with XLBONUS and start with up to 5x your deposit.',
     'Code XLBONUS must be entered on the registration form. It cannot be added after signup. Up to $1,050 total bonus credit.'),
    ('SIGN UP WITH XLBONUS',
     'Register with XLBONUS'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.',
     '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 2. AVIATOR.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== aviator.html ==')
rw('aviator.html', [
    ('<title>1win Aviator — Crash Game | Use Promo Code XLBONUS</title>',
     '<title>1win Aviator — Play the Original Crash Game with Code XLBONUS</title>'),
    ('content="Play Aviator on 1win — the provably fair crash game where you control the multiplier. Use promo code XLBONUS for a 600% deposit bonus to boost your stakes."',
     'content="Play Aviator at 1win with provably fair multipliers, dual-bet mode and 24/7 cash-out. Activate promo code XLBONUS for a 600% deposit bonus to boost your stakes. Free demo available."'),
    ('og:title" content="1win Aviator — Crash Game | Use Promo Code XLBONUS"',
     'og:title" content="1win Aviator — Play the Original Crash Game with Code XLBONUS"'),
    # H1
    ('1WIN <span class="text-gradient-gold">AVIATOR</span>',
     '1win <span class="text-gradient-gold">Aviator</span>'),
    # H2s
    ('HOW <span class="text-gradient">IT WORKS</span>', 'How the game works in 90 seconds'),
    ('WHEN TO <span class="text-gradient-gold">CASH OUT</span>', 'When to cash out'),
    ("RIDE THE <span class='text-gradient'>WAVE</span>", 'Play Aviator with XLBONUS'),
    ('AVIATOR <span class="text-gradient">STATISTICS</span>', 'Aviator round statistics - last 100 rounds, sample'),
    ('AUTO-BET <span class="text-gradient">FEATURES</span>', 'Aviator features at 1win'),
    ('PRO <span class="text-gradient-gold">TIPS</span>', 'Cash-out strategies'),
    ("NERVES OF <span class='text-gradient-gold'>STEEL</span>", 'Related crash games on 1win'),
    ('WHY PLAY <span class="text-gradient">AVIATOR AT 1WIN</span>', 'Aviator on 1win with XLBONUS'),
    ('AVIATOR <span class="text-gradient-gold">PROMO CODE</span>', 'Aviator promo code XLBONUS'),
    ('GET 600% MORE TO PLAY AVIATOR — <span class="text-gradient-gold">600% BONUS</span>',
     'Get 600% more to play Aviator'),
    ('FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>', 'Frequently asked questions'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 3. CASINO.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== casino.html ==')
rw('casino.html', [
    ('<title>1win Casino — 11,000+ Slots &amp; Live Games | XLBONUS</title>',
     '<title>1win Casino — 11,000+ Slots and Live Tables | XLBONUS 600%</title>'),
    ('content="Play 11,000+ slots, live dealer tables, and jackpots at 1win Casino. Enter promo code XLBONUS to collect your 600% welcome bonus and start winning today."',
     'content="Play 11,000+ casino games at 1win: slots, live blackjack, roulette and jackpots from Pragmatic Play, Evolution, NetEnt and 67 more providers. Use code XLBONUS for a 600% welcome bonus."'),
    ('og:title" content="1win Casino — 11,000+ Games | Promo Code XLBONUS"',
     'og:title" content="1win Casino — 11,000+ Slots and Live Tables | XLBONUS 600%"'),
    # H1
    ('1WIN <span class="text-gradient">CASINO</span>',
     '1win <span class="text-gradient">Casino</span>'),
    # H2s
    ('GAME <span class="text-gradient">CATEGORIES</span>', 'Game categories'),
    ('TOP <span class="text-gradient-gold">PROVIDERS</span>', 'Top providers on the platform'),
    ("FEEL THE <span class='text-gradient'>THRILL</span>", 'Claim your 600% casino bonus'),
    ('LIVE <span class="text-gradient">CASINO</span>', 'Live casino at 1win'),
    ('CURRENT <span class="text-gradient-gold">JACKPOTS</span>', 'Current jackpots'),
    ('EXCLUSIVE <span class="text-gradient">FEATURES</span>', 'Tournaments and drops'),
    ("JACKPOTS <span class='text-gradient-gold'>AWAIT</span>", 'Daily and weekly rewards'),
    ('WHY PLAY AT <span class="text-gradient">1WIN CASINO</span>', 'Why play at 1win casino'),
    ('1WIN CASINO <span class="text-gradient-gold">PROMO CODE</span>', '1win casino promo code XLBONUS'),
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>', 'Claim your 600% bonus'),
    ('FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>', 'Frequently asked questions'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 4. SPORTS-BETTING.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== sports-betting.html ==')
rw('sports-betting.html', [
    ('<title>1win Sports Betting — Use Promo Code XLBONUS for 600% Bonus</title>',
     '<title>1win Sportsbook — 30+ Sports, Live Cash-Out and Streaming | XLBONUS</title>'),
    ('content="Bet on 30+ sports with 1win and multiply your bankroll. Use 1win promo code XLBONUS at signup to unlock a 600% welcome bonus. Live odds, in-play & more."',
     'content="Bet on 30+ sports at 1win: football, cricket, tennis, basketball, MMA and esports. Live in-play, cash-out on every selection, free streams on selected matches. Code XLBONUS unlocks 600% bonus."'),
    ('og:title" content="1win Sports Betting — Use Promo Code XLBONUS for 600% Bonus"',
     'og:title" content="1win Sportsbook — 30+ Sports, Live Cash-Out and Streaming | XLBONUS"'),
    # H1
    ('SPORTS BETTING <span class="text-gradient">ON 1WIN</span>',
     'Sports betting at 1win'),
    # H2s
    ('PICK YOUR <span class="text-gradient">BATTLEFIELD</span>', 'Sports we cover'),
    ('LIVE <span class="text-gradient">BETTING</span>', 'How live betting works'),
    ("LIVE THE <span class='text-gradient'>ACTION</span>", 'Bet live with XLBONUS'),
    ('BETTING <span class="text-gradient-gold">TYPES</span>', 'Types of bet at 1win'),
    ('HOW TO <span class="text-gradient">PLACE A BET</span>', 'How to place a bet in three steps'),
    ("YOUR WINNING <span class='text-gradient-gold'>STREAK</span>", 'Bonuses for sports bettors'),
    ('WHY BET AT <span class="text-gradient">1WIN</span>', 'Why bet at 1win'),
    ('1WIN SPORTS BETTING <span class="text-gradient-gold">PROMO CODE</span>', '1win sports betting promo code XLBONUS'),
    ('CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>', 'Claim your 600% bonus'),
    ('FREQUENTLY ASKED <span class="text-gradient">QUESTIONS</span>', 'Frequently asked questions'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 5. APP.HTML  
# ─────────────────────────────────────────────────────────────────
print('\n== app.html ==')
rw('app.html', [
    ('<title>1win App Download — iOS & Android | Promo Code XLBONUS</title>',
     '<title>1win App Download — iOS, Android APK and Mobile Web | XLBONUS</title>'),
    ('content="Download the 1win app for iOS and Android. Bet live, stream matches, and play casino games on the go. Enter promo code XLBONUS for a 600% welcome bonus."',
     'content="Download the 1win app for iOS or Android (APK direct or Google Play). Bet live, stream matches, deposit via UPI, PIX, crypto. Promo code XLBONUS gives 600% welcome bonus."'),
    ('og:title" content="1win App Download — iOS & Android | Promo Code XLBONUS"',
     'og:title" content="1win App Download — iOS, Android APK and Mobile Web | XLBONUS"'),
    # H1
    ('1WIN <span class="text-gradient">APP</span>',
     'Download the 1win app'),
    # H2s
    ('APP <span class="text-gradient">FEATURES</span>', 'What the app gives you that the site does not'),
    ('DOWNLOAD <span class="text-gradient">NOW</span>', 'Download in three steps'),
    ("BET FROM <span class='text-gradient'>ANYWHERE</span>", 'Download and start betting'),
    ('SLEEK <span class="text-gradient">INTERFACE</span>', 'A clean, fast mobile experience'),
    ('APP VS <span class="text-gradient">WEBSITE</span>', 'App vs mobile web'),
    ('HOW TO <span class="text-gradient">INSTALL</span>', 'Install in three steps'),
    ("ALWAYS <span class='text-gradient-gold'>CONNECTED</span>", 'First deposit with XLBONUS via the app'),
    ('1WIN APP <span class="text-gradient">FEATURES</span>', 'App permissions explained'),
    ('BET FROM <span class="text-gradient-gold">ANYWHERE</span>', 'Download the 1win app'),
    ('APP <span class="text-gradient">FAQ</span>', 'Frequently asked questions'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 6. PAYMENT-METHODS.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== payment-methods.html ==')
rw('payment-methods.html', [
    ('<title>1win Payments — Crypto & Card Deposits | Promo Code XLBONUS</title>',
     '<title>1win Deposits and Withdrawals — Crypto, Cards, UPI, PIX | XLBONUS</title>'),
    ('content="Deposit and withdraw on 1win with Visa, crypto (BTC, ETH, USDT), UPI, PIX & more. Zero crypto fees, instant deposits. Use promo code XLBONUS for 600% bonus."',
     'content="Deposit at 1win via Visa, Mastercard, BTC, ETH, USDT, UPI (India), PIX (Brazil), bank transfer and 30+ regional methods. Zero crypto fees. 4-hour average payouts. Promo code XLBONUS gives 600% bonus."'),
    ('og:title" content="1win Payments — Crypto & Card Deposits | Promo Code XLBONUS"',
     'og:title" content="1win Deposits and Withdrawals — Crypto, Cards, UPI, PIX | XLBONUS"'),
    # H1
    ('1WIN <span class="text-gradient">PAYMENTS</span>',
     '1win deposits and withdrawals'),
    # H2s
    ('PAYMENT <span class="text-gradient">METHODS</span>', 'Choose your method by what matters'),
    ('CRYPTO <span class="text-gradient-gold">PAYMENTS</span>', 'Crypto in detail'),
    ("INSTANT <span class='text-gradient'>PAYOUTS</span>", '4-hour average payouts'),
    ('METHOD <span class="text-gradient">COMPARISON</span>', 'Regional methods'),
    ('HOW TO <span class="text-gradient">DEPOSIT</span>', 'How to deposit in 4 steps'),
    ('HOW TO <span class="text-gradient-gold">WITHDRAW</span>', 'How to withdraw'),
    ('BANK-GRADE <span class="text-gradient">SECURITY</span>', 'Fees, limits, and the small print'),
    ('PAYMENTS <span class="text-gradient">FAQ</span>', 'Frequently asked questions'),
    ("YOUR MONEY, <span class='text-gradient-gold'>YOUR WAY</span>", 'Fast, safe, fee-free crypto payouts'),
    ('CRYPTO DEPOSITS <span class="text-gradient">AT 1WIN</span>', 'Crypto deposits at 1win'),
    ('DEPOSIT NOW. <span class="text-gradient-gold">WIN TONIGHT.</span>', 'Make your first deposit'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 7. VIP-CLUB.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== vip-club.html ==')
rw('vip-club.html', [
    ('<title>1win VIP Club — Exclusive Perks | Promo Code XLBONUS</title>',
     '<title>1win VIP Club — 5 Tiers, Cashback up to 30%, Personal Manager</title>'),
    ('content="Unlock 1win VIP Club with 5 tiers from Bronze to Diamond. Personal managers, luxury gifts & priority withdrawals await. Use promo code XLBONUS to start today."',
     'content="Climb the 1win VIP Club through 5 tiers from Bronze to Diamond. Weekly cashback up to 30%, personal account manager from Gold, exclusive tournaments. Promo code XLBONUS starts your VIP journey."'),
    ('og:title" content="1win VIP Club — Exclusive Perks | Promo Code XLBONUS"',
     'og:title" content="1win VIP Club — 5 Tiers, Cashback up to 30%, Personal Manager"'),
    # H1
    ('1WIN VIP <span class="text-gradient-gold">CLUB</span>',
     '1win VIP <span class="text-gradient-gold">Club</span>'),
    # H2s
    ('VIP <span class="text-gradient-gold">TIERS</span>', 'The five tiers'),
    ('BENEFITS <span class="text-gradient">COMPARISON</span>', 'What you get at each tier'),
    ("LIVE <span class='text-gradient'>LAVISH</span>", 'Climb faster with XLBONUS'),
    ('VIP <span class="text-gradient-gold">BENEFITS</span>', 'VIP benefits at each tier'),
    ('HOW TO <span class="text-gradient">JOIN</span>', 'How cashback is calculated'),
    ('LUXURY <span class="text-gradient-gold">GIFTS</span>', 'How to climb tiers faster'),
    ("ROYALTY <span class='text-gradient-gold'>TREATMENT</span>", 'Diamond tier - the top level'),
    ('VIP CLUB <span class="text-gradient">BENEFITS</span>', 'VIP Club benefits'),
    ('START VIP WITH <span class="text-gradient-gold">XLBONUS</span>', 'Start your VIP journey with XLBONUS'),
    ('START YOUR <span class="text-gradient-gold">VIP JOURNEY</span>', 'Start your VIP journey'),
    ('VIP CLUB <span class="text-gradient">FAQ</span>', 'Frequently asked questions'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 8. LUCKY-DRIVE.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== lucky-drive.html ==')
rw('lucky-drive.html', [
    ('<title>1win Lucky Drive — Win a Lamborghini | Promo Code XLBONUS</title>',
     '<title>1win Lucky Drive — Win a Lamborghini Urus SE with Code XLBONUS</title>'),
    ('content="Enter the 1win Lucky Drive giveaway for a chance to win a Lamborghini Urus SE. Use promo code XLBONUS to register and start earning raffle tickets today."',
     'content="Enter the 1win Lucky Drive raffle for a Lamborghini Urus SE worth $240,000. One automatic ticket per real-money bet. Use promo code XLBONUS to register and start earning tickets today."'),
    ('og:title" content="1win Lucky Drive — Win a Lamborghini | Promo Code XLBONUS"',
     'og:title" content="1win Lucky Drive — Win a Lamborghini Urus SE with Code XLBONUS"'),
    # H1
    ('1WIN LUCKY <span class="text-gradient-gold">DRIVE</span>',
     'Lucky Drive - Win a Lamborghini Urus SE'),
    # H2s (the inner h2 for prize visual is fine to rewrite)
    ('HOW TO <span class="text-gradient">ENTER</span>', 'How to enter in three steps'),
    ("DRIVE YOUR <span class='text-gradient'>DREAM</span>", 'Earn more tickets every day'),
    ('PRIZE <span class="text-gradient-gold">TIERS</span>', 'Prize tiers - not just the Lamborghini'),
    ('PAST <span class="text-gradient">WINNERS</span>', 'Past Lucky Drive winners'),
    ("WINNERS <span class='text-gradient-gold'>DRIVE</span>", 'When the draw happens'),
    ('HOW TO WIN AT <span class="text-gradient">LUCKY DRIVE</span>', 'Ticket earn rate'),
    ('MORE TICKETS = <span class="text-gradient-gold">MORE CHANCES</span>', 'More tickets, more chances'),
    ('LUCKY DRIVE <span class="text-gradient">FAQ</span>', 'Frequently asked questions'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 9. REVIEW.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== review.html ==')
rw('review.html', [
    ('<title>1win Review 2026 — Expert Sportsbook Rating | XLBONUS</title>',
     '<title>1win Review 2026 — Sportsbook and Casino Tested | Pros, Cons, Verdict</title>'),
    ('content="Expert 1win review 2026 covering sportsbook, casino, odds, payments, and mobile app. Use promo code XLBONUS for a 600% deposit bonus on your first top-up."',
     'content="Our 1win review 2026 covers the sportsbook, casino, Aviator, app, payments and bonus terms. Tested withdrawals, KYC, support response. Verdict: 4.5/5. Promo code XLBONUS unlocks 600% welcome."'),
    ('og:title" content="1win Review 2026 — Sportsbook &amp; Casino Expert Review | Promo Code XLBONUS"',
     'og:title" content="1win Review 2026 — Sportsbook and Casino Tested | Pros, Cons, Verdict"'),
    # H1
    ('1WIN <span class="text-gradient">REVIEW</span>',
     '1win review 2026 - independent verdict'),
    # H2s
    ('1WIN <span class="text-gradient">WELCOME BONUS</span>', 'The 1win welcome bonus tested'),
    ('1WIN <span class="text-gradient">SPORTSBOOK</span>', 'The 1win sportsbook tested'),
    ('1WIN <span class="text-gradient-gold">CASINO</span>', 'The 1win casino tested'),
    ('USING THE <span class="text-gradient">1WIN WEBSITE</span>', '1win website and app'),
    ('1WIN ODDS AND <span class="text-gradient">MARKETS</span>', 'Odds and markets - the long version'),
    ("30+ SPORTS <span class=\"text-gradient\">TO BET ON</span>", '30+ sports to bet on'),
    ('1WIN <span class="text-gradient">MOBILE APP</span>', '1win mobile app tested'),
    ('1WIN <span class="text-gradient-gold">PAYMENT METHODS</span>', '1win payment methods'),
    ('1WIN CUSTOMER <span class="text-gradient">SUPPORT</span>', 'Pros and cons'),
    ('1WIN REVIEW <span class="text-gradient">FAQs</span>', 'Verdict - 4.5 / 5'),
    ('READY TO JOIN? CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>',
     'Register with XLBONUS'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 10. REGISTER.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== register.html ==')
rw('register.html', [
    ('<title>1win Register Login Mobile 2026 — Sign Up, Get 1win ID & 600% Bonus | XLBONUS</title>',
     '<title>1win Register — Open an Account in 30 Seconds with Code XLBONUS</title>'),
    ('content="1win register login mobile guide 2026 — sign up in 30 seconds, get your 1win ID number, login from any phone or desktop. Apply promo code XLBONUS for a 600% welcome bonus across 4 deposits."',
     'content="Register at 1win in 30 seconds. Phone, email or one-click social signup. Enter promo code XLBONUS at registration for a 600% welcome bonus across your first four deposits. 18+, T&amp;Cs."'),
    ('og:title" content="1win Register &amp; Login 2026 — Sign Up With Promo Code XLBONUS for 600% Bonus"',
     'og:title" content="1win Register — Open an Account in 30 Seconds with Code XLBONUS"'),
    # H1
    ('1WIN <span class="text-gradient">REGISTER</span>',
     '1win register - open your account in 30 seconds'),
    # H2s
    ('1WIN REGISTER <span class="text-gradient">INFORMATION</span>', '1win registration - quick facts'),
    ('HOW TO COMPLETE <span class="text-gradient">1WIN REGISTRATION</span>', 'The fastest signup - register by phone'),
    ('1WIN <span class="text-gradient">REGISTRATION METHODS</span>', 'Register by email or social login'),
    ('1WIN <span class="text-gradient-gold">LOGIN</span>', '1win login - for existing users'),
    ('1WIN <span class="text-gradient">REGISTRATION BONUS</span>', 'Apply code XLBONUS - three ways to make sure it sticks'),
    ('1WIN BY <span class="text-gradient">COUNTRY</span>', 'Country-specific registration pages'),
    ('YOUR <span class="text-gradient">1WIN ID NUMBER</span>', 'KYC verification - what you need'),
    ("REGISTER IN <span class='text-gradient'>60 SECONDS</span>", 'Register now with XLBONUS'),
    ('1WIN REGISTER <span class="text-gradient">FAQs</span>', 'Frequently asked questions'),
    # Schema / body H2s
    ('1WIN REGISTER LOGIN MOBILE — FULL GUIDE',
     '1win register - full guide'),
    ('1WIN CREATE ACCOUNT — QUICK SIGN-UP METHODS',
     '1win create account - sign-up methods'),
    ('REGISTER TODAY &amp; CLAIM YOUR <span class="text-gradient-gold">600% BONUS</span>',
     'Register today and claim your 600% bonus'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 11. POKER.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== poker.html ==')
with open(os.path.join(BASE, 'poker.html'), 'r') as f:
    pk = f.read()

# Get all H2 patterns
pk_h2_hits = re.findall(r'<h2[^>]*>([^<]*(?:<[^/][^>]*>[^<]*</[^>]+>)?[^<]*)</h2>', pk)
print(f'  Poker H2s: {pk_h2_hits[:10]}')

rw('poker.html', [
    ('<title>1win Poker — Texas Hold\'em &amp; Tournaments | XLBONUS</title>',
     '<title>1win Poker — Texas Hold\'em, Omaha and Tournaments | XLBONUS</title>'),
    ('content="Join 1win Poker for Texas Hold\'em, Omaha, cash games, and tournaments. Use 1win promo code XLBONUS when you register to claim your 600% first deposit bonus."',
     'content="Play poker at 1win: Texas Hold\'em, Omaha, Stud and 60+ variants. Cash games, sit-and-go, multi-table tournaments. Register with promo code XLBONUS for a 600% welcome bonus. Curaçao licensed."'),
    ('og:title" content="1win Poker — Texas Hold\'em & Tournaments | Promo Code XLBONUS"',
     'og:title" content="1win Poker — Texas Hold\'em, Omaha and Tournaments | XLBONUS"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 12. LIVE-STREAMING.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== live-streaming.html ==')
rw('live-streaming.html', [
    ('<title>1win Live Streaming — Watch Sport Free | XLBONUS 2026</title>',
     '<title>1win Live Streaming — Free Sports Streams on 30+ Sports | XLBONUS</title>'),
    ('content="Watch free live sports streaming on 1win. 30+ sports including football, tennis and esports. Register with promo code XLBONUS for a 600% welcome bonus."',
     'content="Watch free live sports at 1win: Premier League, IPL, ATP, NBA and more. Free streams for logged-in users on selected fixtures. Register with code XLBONUS for a 600% welcome bonus. Curaçao licensed."'),
    ('og:title" content="1win Live Streaming — Watch Live Sport for Free | Promo Code XLBONUS"',
     'og:title" content="1win Live Streaming — Free Sports Streams on 30+ Sports | XLBONUS"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 13. PROMOTIONS.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== promotions.html ==')
rw('promotions.html', [
    ('<title>1win Promotions & Bonuses 2026 | Promo Code XLBONUS</title>',
     '<title>1win Promotions 2026 — Cashback, Tournaments, Lucky Drive | XLBONUS</title>'),
    ('content="Explore all 1win promotions in 2026: tournaments, reload bonuses & free spins. Use promo code XLBONUS to claim your 600% welcome bonus and never miss a deal."',
     'content="All active 1win promotions for 2026: 600% welcome with XLBONUS, weekly cashback up to 30%, Lucky Drive Lamborghini raffle, accumulator boost and daily casino drops. 18+, T&amp;Cs apply."'),
    ('og:title" content="1win Promotions & Bonuses 2026 | Promo Code XLBONUS"',
     'og:title" content="1win Promotions 2026 — Cashback, Tournaments, Lucky Drive | XLBONUS"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 14. NEWS.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== news.html ==')
rw('news.html', [
    ('<title>1win News — Latest Updates 2026 | Promo Code XLBONUS</title>',
     '<title>1win News — Platform Updates, Promotions and Sports Coverage 2026</title>'),
    ('content="Stay up to date with the latest 1win news in 2026: new games, promotions, sports events & platform updates. Use promo code XLBONUS for a 600% signup bonus."',
     'content="Latest 1win news for 2026: new game launches, platform updates, promotions, Lucky Drive announcements and sports coverage. Register with code XLBONUS for a 600% welcome bonus."'),
    ('og:title" content="1win News — Latest Updates 2026 | Promo Code XLBONUS"',
     'og:title" content="1win News — Platform Updates, Promotions and Sports Coverage 2026"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 15. MIRRORS.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== mirrors.html ==')
rw('mirrors.html', [
    ('<title>1win Alternative Link & Mirror 2026 — Working Access Links | XLBONUS 600% Bonus</title>',
     '<title>1win Mirror — Working Alternative Link May 2026 | XLBONUS</title>'),
    ('content="Get the working 1win alternative link for 2026. Instantly access 1win from any country with our verified mirror links. Claim 600% bonus with code XLBONUS."',
     'content="Cannot reach 1win? Use our verified working mirror link, refreshed daily. Same account, same balance, same bonus terms. Promo code XLBONUS still applies. 18+, T&amp;Cs."'),
    ('og:title" content="1win Alternative Link & Mirror 2026 — Working Access Links | XLBONUS 600% Bonus"',
     'og:title" content="1win Mirror — Working Alternative Link May 2026 | XLBONUS"'),
    # Body H2 (non-class)
    ('1WIN ALTERNATIVE LINK — DIRECT ACCESS 2026',
     '1win mirror - working alternative link'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 16. ACCESS.HTML  (login + recover password + access from blocked regions)
# ─────────────────────────────────────────────────────────────────
print('\n== access.html ==')
rw('access.html', [
    ('<title>1win Login — Access &amp; Register | Promo Code XLBONUS</title>',
     '<title>1win Login — Sign In, Password Recovery and Blocked Region Access</title>'),
    ('content="Access the 1win login screen from anywhere. Log in or create a new account at 1win. Use promo code XLBONUS for a 600% welcome bonus on your first deposit."',
     'content="Log in to your 1win account, recover your password, or access 1win from a blocked region. If the main site is unavailable, use our verified working mirror. Curaçao licensed (8048/JAZ)."'),
    ('og:title" content="1win Login — Access 1win Website &amp; Register | Promo Code XLBONUS"',
     'og:title" content="1win Login — Sign In, Password Recovery and Blocked Region Access"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 17. ALTERNATIVE-LINK.HTML  (alt link as alternative when main domain unreachable)
# ─────────────────────────────────────────────────────────────────
print('\n== alternative-link.html ==')
rw('alternative-link.html', [
    ('<title>1win Alternative Link 2026 — Working Mirror Links &amp; Access</title>',
     '<title>1win Alternative Link 2026 — When the Main Domain Is Unreachable</title>'),
    ('content="Find working 1win alternative links for 2026. Bypass geo-blocks and ISP restrictions instantly with the latest 1win mirror link. Use promo code XLBONUS for a 600% bonus."',
     'content="The 1win alternative link is a separate URL that loads the full 1win site when the primary domain is blocked or unreachable. Updated daily. Use code XLBONUS for a 600% welcome bonus."'),
    ('og:title" content="1win Alternative Link 2026 — Working Mirror Links &amp; Access"',
     'og:title" content="1win Alternative Link 2026 — When the Main Domain Is Unreachable"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 18. WEBSITE.HTML  (corporate brand/operator info page)
# ─────────────────────────────────────────────────────────────────
print('\n== website.html ==')
rw('website.html', [
    ('<title>1win Website — Sportsbook &amp; Casino | Promo Code XLBONUS</title>',
     '<title>1win Website — Operator Info, Licence and Products at a Glance</title>'),
    ('content="Access the official 1win website for sports betting, casino, poker and more. Use promo code XLBONUS for a 600% deposit bonus on your very first top-up."',
     'content="Everything about the 1win operator: Curaçao licence 8048/JAZ, company 1win N.V., 30+ sports, 11,000+ casino games, 18 fiat currencies, 6 crypto networks. Founded 2018. Promo code XLBONUS."'),
    ('og:title" content="1win Website — Access the Sportsbook &amp; Casino | Promo Code XLBONUS"',
     'og:title" content="1win Website — Operator Info, Licence and Products at a Glance"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 19. FAQ.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== faq.html ==')
rw('faq.html', [
    ('<title>1win FAQ — Questions & Answers | Promo Code XLBONUS</title>',
     '<title>1win FAQ — Bonus, Withdrawals, Mirror, Account Help | XLBONUS</title>'),
    ('content="Find answers to all your 1win questions: how to use promo code XLBONUS, registration, deposits, withdrawals, bonuses, betting rules, and account management."',
     'content="Frequently asked 1win questions: how to use code XLBONUS, deposit and withdrawal times, mirror access, bonus wagering, KYC, app install, account verification. Updated May 2026."'),
    ('og:title" content="1win FAQ — Questions & Answers | Promo Code XLBONUS"',
     'og:title" content="1win FAQ — Bonus, Withdrawals, Mirror, Account Help | XLBONUS"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 20. 1WIN-PROMO-CODE.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== 1win-promo-code.html ==')
rw('1win-promo-code.html', [
    ('<title>1win Promo Code XLBONUS 2026 — Complete Guide to 600% Bonus</title>',
     '<title>1win Promo Code XLBONUS — Complete 600% Bonus Guide (2026)</title>'),
    ('content="Use 1win promo code XLBONUS in 2026 for a 600% deposit bonus across four deposits. Complete step-by-step guide to claiming the maximum welcome offer here."',
     'content="The complete guide to 1win promo code XLBONUS: how it works, the 4-deposit 600% structure, activation steps, wagering requirements and bonus terms. Curaçao licensed, 18+, T&amp;Cs apply."'),
    ('og:title" content="1win Promo Code XLBONUS 2026 — Complete Guide to 600% Bonus"',
     'og:title" content="1win Promo Code XLBONUS — Complete 600% Bonus Guide (2026)"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

# ─────────────────────────────────────────────────────────────────
# 21. INDEX.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== index.html ==')
rw('index.html', [
    ('<title>1win Promo Code XLBONUS, 600% Bonus | Bet Big. Win Bigger.</title>',
     '<title>1win Promo Code XLBONUS — 600% Welcome Bonus (2026)</title>'),
    ('content="Use 1win promo code XLBONUS to unlock a 600% welcome bonus across your first 4 deposits. Sign up today and start winning on sports, casino, and Aviator."',
     'content="Get a 600% welcome bonus on your first four deposits at 1win with promo code XLBONUS. 30+ sports, 11,000+ casino games, Aviator, crypto payouts in 4 hours average. Curaçao licensed."'),
    ('og:title" content="1win Promo Code XLBONUS, 600% Bonus | Bet Big. Win Bigger."',
     'og:title" content="1win Promo Code XLBONUS — 600% Welcome Bonus (2026)"'),
    # Footer tagline
    ('BET BIG. WIN BIGGER.', '1win.codes - independent affiliate review'),
])

print('\n\nAll 21 pages processed.')
