#!/usr/bin/env python3
"""
Fix em/en dashes inside schema JSON-LD and in remaining body text.
Also fix schema name/description fields to match updated titles.
"""
import re, os

BASE = '/home/user/workspace/1win-codes-repo/en'

TARGET_PAGES = [
    '1win-promo-code.html', 'access.html', 'alternative-link.html',
    'app.html', 'aviator.html', 'casino.html', 'faq.html', 'index.html',
    'live-streaming.html', 'lucky-drive.html', 'mirrors.html', 'news.html',
    'payment-methods.html', 'poker.html', 'promo-code.html', 'promotions.html',
    'register.html', 'review.html', 'sports-betting.html', 'vip-club.html',
    'website.html',
]

def fix_file(fname):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    orig = s

    # Fix em dashes everywhere (including scripts/schema JSON)
    # Em dash in JSON schema titles/descriptions: use hyphen
    s = s.replace('—', '-')
    
    # Fix en dashes: in JSON schema "1-3" ranges, use "to"
    # In body copy ranges: use "to"
    # In schema JSON text values
    s = s.replace('1–3 business days', '1 to 3 business days')
    s = s.replace('3%–15%', '3% to 15%')
    s = s.replace('–', ' to ')
    
    # Fix remaining banned phrases that slipped through
    # "guaranteed" that might be in news.html or sports-betting.html
    s = re.sub(r'\bguaranteed\b', 'scheduled', s)
    
    # Fix schema JSON name fields to match new titles
    schema_fixes = {
        # access.html
        '"name": "1win Login - Access & Register | Promo Code XLBONUS"':
            '"name": "1win Login - Sign In, Password Recovery and Blocked Region Access"',
        # alternative-link.html schema
        '"name": "1win Alternative Link 2026 - Working Mirror Links & Access"':
            '"name": "1win Alternative Link 2026 - When the Main Domain Is Unreachable"',
        # app.html schema
        '"name": "1win App Download - iOS & Android | Promo Code XLBONUS"':
            '"name": "1win App Download - iOS, Android APK and Mobile Web | XLBONUS"',
        # aviator.html schema
        '"name": "1win Aviator - Crash Game | Use Promo Code XLBONUS"':
            '"name": "1win Aviator - Play the Original Crash Game with Code XLBONUS"',
        '"description": "Play Aviator on 1win - the provably fair crash game where you control the multiplier. Use promo code XLBONUS for a 600% deposit bonus to boost your stakes."':
            '"description": "Play Aviator at 1win with provably fair multipliers, dual-bet mode and 24/7 cash-out. Activate promo code XLBONUS for a 600% deposit bonus to boost your stakes."',
        # casino.html schema
        '"name": "1win Casino - 11,000+ Slots & Live Games | XLBONUS"':
            '"name": "1win Casino - 11,000+ Slots and Live Tables | XLBONUS 600%"',
        # live-streaming.html schema
        '"name": "1win Live Streaming - Watch Sport Free | XLBONUS 2026"':
            '"name": "1win Live Streaming - Free Sports Streams on 30+ Sports | XLBONUS"',
        # lucky-drive.html schema
        '"name": "1win Lucky Drive - Win a Lamborghini | Promo Code XLBONUS"':
            '"name": "1win Lucky Drive - Win a Lamborghini Urus SE with Code XLBONUS"',
        # mirrors.html schema
        '"name": "1win Mirror - Working Mirror Links 2026 | Promo Code XLBONUS"':
            '"name": "1win Mirror - Working Alternative Link May 2026 | XLBONUS"',
        # news.html schema
        '"name": "1win News - Latest Updates 2026 | Promo Code XLBONUS"':
            '"name": "1win News - Platform Updates, Promotions and Sports Coverage 2026"',
        # payment-methods.html schema
        '"name": "1win Payments - Crypto & Card Deposits | Promo Code XLBONUS"':
            '"name": "1win Deposits and Withdrawals - Crypto, Cards, UPI, PIX | XLBONUS"',
        # poker.html schema
        '"name": "1win Poker - Texas Hold\'em & Tournaments | XLBONUS"':
            '"name": "1win Poker - Texas Hold\'em, Omaha and Tournaments | XLBONUS"',
        # register.html schema
        '"name": "1win Register - Sign Up & Login | Promo Code XLBONUS"':
            '"name": "1win Register - Open an Account in 30 Seconds with Code XLBONUS"',
        # sports-betting.html schema
        '"name": "1win Sports Betting - Use Promo Code XLBONUS for 600% Bonus"':
            '"name": "1win Sportsbook - 30+ Sports, Live Cash-Out and Streaming | XLBONUS"',
        # vip-club.html schema
        '"name": "1win VIP Club - Exclusive Perks | Promo Code XLBONUS"':
            '"name": "1win VIP Club - 5 Tiers, Cashback up to 30%, Personal Manager"',
        # website.html schema
        '"name": "1win Website - Sportsbook & Casino | Promo Code XLBONUS"':
            '"name": "1win Website - Operator Info, Licence and Products at a Glance"',
    }
    
    for old, new in schema_fixes.items():
        s = s.replace(old, new)
    
    # Also fix og:description which may have em dashes
    # (already handled by global — -> - above)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    
    changed = s != orig
    return changed


changed_count = 0
for fname in TARGET_PAGES:
    changed = fix_file(fname)
    print(f'  {"OK" if changed else "no-op"}: {fname}')
    if changed:
        changed_count += 1

print(f'\nFixed {changed_count} files.')
