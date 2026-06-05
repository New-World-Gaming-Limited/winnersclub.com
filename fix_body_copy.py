#!/usr/bin/env python3
"""
Fix hero subtitles, first paragraphs and key body copy across all 21 pages.
Ensures every page has: brand + code + specific number + trust signal in first paragraph.
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
    print(f'  {"OK" if s!=orig else "no-op"}: {fname}')

# ─────────────────────────────────────────────────────────────────
# APP.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== app.html ==')
rw('app.html', [
    # Hero subtitle  
    ('The full 1win experience in your pocket. Sports betting, 10,000+ casino games, live streaming, and instant withdrawals, all from your phone. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     'Native apps for iPhone and Android. 1win covers 30+ sports and 11,000+ casino games in a 58 MB app. Live streams, biometric login, in-play cash-out, push alerts. Curaçao-licensed (8048/JAZ). Download with code XLBONUS for a 600% welcome bonus.'),
    # "Download the app. Bet from anywhere." subtitle tagline
    ('Download the app. Bet from anywhere.',
     'Download the 1win app'),
    # CTA banner subtitle
    ('content="Download the 1win app for iOS or Android (APK direct or Google Play). Bet live, stream matches, deposit via UPI, PIX, crypto. Promo code XLBONUS gives 600% welcome bonus."',
     'content="Download the 1win app for iOS or Android (APK direct or Google Play). 30+ sports, 11,000+ casino games. Promo code XLBONUS gives 600% welcome bonus. Curaçao-licensed."'),
])

# ─────────────────────────────────────────────────────────────────
# MIRRORS.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== mirrors.html ==')
rw('mirrors.html', [
    ('Access 1win.pro from anywhere in the world. Working mirror links, updated regularly. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     '1win mirrors are identical copies of the 1win site on different domains. If your ISP blocks 1win.com, the mirror gives you the same login, same balance, same 600% XLBONUS bonus terms. Curaçao-licensed (8048/JAZ). We refresh the working link every 24 hours.'),
])

# ─────────────────────────────────────────────────────────────────
# ACCESS.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== access.html ==')
rw('access.html', [
    ('Access 1win from anywhere in the world. Log in with your existing account or register in under 60 seconds.',
     '1win account access: log in with phone, email or social, recover a forgotten password, or reach the site from a blocked region via a working mirror. 1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ). New players: register with code XLBONUS for a 600% welcome bonus.'),
])

# ─────────────────────────────────────────────────────────────────
# ALTERNATIVE-LINK.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== alternative-link.html ==')
rw('alternative-link.html', [
    ('A 1win alternative link lets you access the full 1win platform when the main domain is blocked by your ISP or restricted in your region. Same account, same balance, different address. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     '1win\'s alternative link is a separate URL that loads the full platform when the primary domain is unavailable. It differs from a mirror: the alternative link is the official fallback endpoint, not a third-party clone. Same 30+ sports, same 11,000+ casino games, same XLBONUS 600% bonus. Curaçao-licensed (8048/JAZ).'),
])

# ─────────────────────────────────────────────────────────────────
# WEBSITE.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== website.html ==')
rw('website.html', [
    ('Access the official 1win website for world-class sports betting, casino games, poker and more. Use promo code XLBONUS for a 600% welcome bonus.',
     '1win is operated by 1win N.V., licensed under Curaçao Gaming Authority licence 8048/JAZ. The platform covers 30+ sports, 11,000+ casino games from 70+ providers, 18 fiat currencies and 6 crypto networks. Founded 2018. Use code XLBONUS for a 600% welcome bonus across your first four deposits.'),
])

# ─────────────────────────────────────────────────────────────────
# INDEX.HTML - Hero subtitle
# ─────────────────────────────────────────────────────────────────
print('\n== index.html ==')
rw('index.html', [
    ('Looking for 1win betting &amp; casino? This is the right site. Use promo code <span class="code-highlight">XLBONUS</span> for a 600% deposit bonus. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     'Code XLBONUS stacks a 200% + 150% + 100% + 50% bonus across your first four deposits. 1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ). 600% total, auto-activated.'),
    # Also fix the two paragraphs that say "over 25 different sports" and "thousands"
    ('Log in to your 1win account to place sports bets and play casino games. Your 1win account allows you to bet on over 25 different sports, with 1,000+ betting markets available every day. At the sportsbook you can bet live in-play on lots of different sports, all with great odds. Live streaming is also available.',
     '1win covers 30+ sports with 1,000+ daily markets, live in-play betting with cash-out on every selection, and free streams on selected football and tennis matches. Curaçao-licensed (8048/JAZ), founded 2018.'),
    ('Choose from 11,000+ casino games. The 1win casino has all of the top games from the best software providers. Register in seconds to play slot games, table games, blackjack, roulette, poker and more.',
     '11,000+ casino games from 70+ providers including Pragmatic Play, Evolution, NetEnt and Spribe. Live dealer tables 24/7. Daily drops and tournaments worth $50,000+ a week.'),
    ('1win offers online sports betting and casino games to 100,000+ players every day. 1win.pro is a global betting site accessible all over the world. New players can use the 1win promo code <span class="code-highlight">XLBONUS</span> when registering to get a bonus worth up to 600% your deposit.',
     '1win is a globally accessible sportsbook and casino, operating under Curaçao licence 8048/JAZ. New players use promo code <span class="code-highlight">XLBONUS</span> to unlock a 600% welcome bonus across four deposits, up to $1,050 total.'),
    ('1win is available in over 12 languages. Bet on 20+ sports and play 11,000+ casino games from anywhere.',
     '1win is available in 15 languages. Bet on 30+ sports and play 11,000+ casino games from anywhere.'),
    ('Join 1win players worldwide. Claim your 600% bonus with code <span class="code-highlight">XLBONUS</span> and start winning today.',
     'Claim your 600% bonus with code <span class="code-highlight">XLBONUS</span>. Curaçao-licensed, 4-hour average withdrawals.'),
    ('Compete against the best. Weekly tournaments with fixed prize pools.',
     'Compete in weekly tournaments with fixed prize pools worth $50,000+ each week.'),
])

# ─────────────────────────────────────────────────────────────────
# POKER.HTML - Fix hero sub after OUTPLAY EVERYONE fix
# ─────────────────────────────────────────────────────────────────
print('\n== poker.html ==')
rw('poker.html', [
    ('Play Texas Hold\'em and Omaha at 1win. Texas Hold\'em, Omaha, massive tournament prize pools, and a community of grinders who came to dominate.',
     'Play Texas Hold\'em, Omaha, and Stud at 1win. 1win covers 60+ poker variants with cash tables running 24/7 at micro to high stakes. Use code XLBONUS for a 600% welcome bonus. Curaçao-licensed (8048/JAZ).'),
    ('From freerolls to six-figure scheduled prize pools, there\'s a tournament running every hour.',
     'Freerolls, sit-and-go, and multi-table tournaments running every hour. Scheduled prize pools daily.'),
])

# ─────────────────────────────────────────────────────────────────
# LIVE-STREAMING.HTML
# ─────────────────────────────────────────────────────────────────
print('\n== live-streaming.html ==')
rw('live-streaming.html', [
    ('Watch live sports for free at 1win. 30+ sports covered including football, tennis, basketball, eSports and more. Register with promo code XLBONUS for 600% bonus.',
     '1win live streaming covers 30+ sports including Premier League, IPL, ATP, NBA and esports. Free streams for logged-in account holders on selected fixtures, no extra fee. Register with code XLBONUS for a 600% welcome bonus. Curaçao-licensed (8048/JAZ).'),
])

# ─────────────────────────────────────────────────────────────────
# PROMOTIONS.HTML - Hero subtitle
# ─────────────────────────────────────────────────────────────────
print('\n== promotions.html ==')
with open(os.path.join(BASE, 'promotions.html'), 'r') as f:
    promo_s = f.read()

# Find the hero-subtitle paragraph
promo_hero_match = re.search(r'(<p class="hero-subtitle"[^>]*>)\s*(.*?)\s*(</p>)', promo_s, re.DOTALL)
if promo_hero_match:
    old_sub = promo_hero_match.group(0)
    new_sub = promo_hero_match.group(1) + '\n        All active 1win promotions for 2026: the 600% XLBONUS welcome bonus, weekly cashback up to 30%, Lucky Drive Lamborghini raffle, accumulator boost, and daily casino drops from Pragmatic Play. Curaçao-licensed (8048/JAZ), 18+.\n      ' + promo_hero_match.group(3)
    promo_s = promo_s.replace(old_sub, new_sub, 1)
    print('  Promotions hero subtitle updated')

with open(os.path.join(BASE, 'promotions.html'), 'w') as f:
    f.write(promo_s)
print('  OK: promotions.html')

# ─────────────────────────────────────────────────────────────────
# NEWS.HTML - Hero sub
# ─────────────────────────────────────────────────────────────────
print('\n== news.html ==')
rw('news.html', [
    ('Stay ahead of the game. The latest updates on promotions, tournaments, new features, and everything happening in the world of 1win.',
     '1win news for 2026: new game launches, platform updates, Lucky Drive announcements, bonus changes and sports coverage. 1win covers 30+ sports, 11,000+ casino games. Curaçao-licensed (8048/JAZ). Use code XLBONUS for a 600% welcome bonus.'),
])

# ─────────────────────────────────────────────────────────────────
# 1WIN-PROMO-CODE.HTML - Hero sub fix
# ─────────────────────────────────────────────────────────────────
print('\n== 1win-promo-code.html ==')
rw('1win-promo-code.html', [
    ('Complete guide to using the 1win promo code XLBONUS. Get a 600% welcome deposit bonus across four deposits, the most generous welcome offer available at 1win.',
     'The complete guide to 1win promo code XLBONUS. Enter it at signup to unlock 200% + 150% + 100% + 50% across your first four deposits: 600% total, up to $1,050 bonus credit. 1win is Curaçao-licensed (8048/JAZ). T&Cs apply, 18+.'),
])

# ─────────────────────────────────────────────────────────────────
# FAQ.HTML - Check first body paragraph
# ─────────────────────────────────────────────────────────────────
print('\n== faq.html ==')
rw('faq.html', [
    # Hero subtitle
    ('Everything we get asked about 1win, answered. Bonus, withdrawals, mirrors, app, account, and more.',
     'Frequently asked questions about 1win: how to use promo code XLBONUS, deposit and withdrawal times, mirror access, 600% bonus wagering, KYC, app install, account verification. 42 questions answered. Updated May 2026.'),
])

print('\nBody copy fixes done.')
