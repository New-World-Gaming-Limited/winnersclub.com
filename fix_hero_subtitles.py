#!/usr/bin/env python3
"""Fix hero subtitles for remaining pages."""
import os

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

print('\n== sports-betting.html ==')
rw('sports-betting.html', [
    ('Bet on 30+ sports at 1win. 30+ sports, 1,000+ live events daily, and the sharpest odds in the industry. Use code XLBONUS for a 600% welcome bonus. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     '30+ sports. 1,000+ daily markets. Live in-play on every match with cash-out and free streaming on selected football and tennis fixtures. 1win is Curaçao-licensed (8048/JAZ). Welcome bonus 600% with code XLBONUS.'),
])

print('\n== casino.html ==')
rw('casino.html', [
    ('OVER 11,000 GAMES AWAIT. From high-voltage slots to immersive live dealer tables, the house is loaded and the chips are stacked. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     '11,000+ games. 70+ providers. Live dealer tables 24/7. 1win is Curaçao-licensed (8048/JAZ). The 600% XLBONUS bonus plays on every category at 100% wagering weight.'),
])

print('\n== aviator.html ==')
rw('aviator.html', [
    ('The plane takes off. The multiplier climbs. Cash out before it crashes, or watch your bet soar to 100x and beyond. Pure adrenaline. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     'The Spribe crash game where a plane takes off, a multiplier ticks up from 1.00x and you cash out before it flies off the screen. Provably fair, two simultaneous bets, autoplay supported. RTP 97%. Use code XLBONUS for a 600% deposit bonus.'),
])

print('\n== review.html ==')
rw('review.html', [
    ('Our complete expert review of 1win covering sportsbook, casino, odds, payments, app, and bonuses for 2026. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     'We funded a real account, deposited $500, placed 47 bets, played 21 slot sessions, ran one withdrawal and timed every support ticket. Here is the honest verdict on 1win in 2026. Curaçao-licensed (8048/JAZ). Code XLBONUS unlocks 600% welcome bonus.'),
])

print('\n== register.html ==')
rw('register.html', [
    ('Open your 1win account in under 60 seconds. Register by phone, email, or social media and claim your welcome bonus. Use our <a href="/en/promo-code"><strong>promo code guide</strong></a> for the XLBONUS 600% bonus.',
     'Three signup methods: phone, email or social. 1win covers 30+ sports and 11,000+ casino games. Promo code XLBONUS must be entered on the registration form for a 600% welcome bonus. Curaçao-licensed (8048/JAZ). Cannot be added after signup.'),
])

print('\n== payment-methods.html ==')
rw('payment-methods.html', [
    ('FAST. SECURE. YOUR WAY.',
     'Crypto for speed, cards for convenience, regional rails for currency: PIX, UPI, M-Pesa, SBP, EasyEFT. 4-hour average withdrawal across all methods. 1win is Curaçao-licensed (8048/JAZ). Zero fees on every crypto network. Code XLBONUS unlocks a 600% welcome bonus.'),
])

print('\n== vip-club.html ==')
rw('vip-club.html', [
    ('Exclusive privileges for high rollers. Rise through 5 tiers and unlock personal managers, luxury gifts, unlimited withdrawals, and VIP-only events.',
     'Five tiers from Bronze to Diamond. Every real-money bet earns Loyalty Points. Higher tier means higher cashback (up to 30%), faster withdrawals, and a personal account manager from Gold upward. 1win is Curaçao-licensed (8048/JAZ). Code XLBONUS gives you a 600% bankroll head-start.'),
])

print('\n== lucky-drive.html ==')
rw('lucky-drive.html', [
    ('The ultimate giveaway. Play your favorite games, earn tickets automatically, and win a brand-new Lamborghini Urus SE, or one of hundreds of cash prizes.',
     'The 2026 Urus SE is the plug-in hybrid super SUV with 800 HP and a $240,000 value. Every real-money bet earns a Lucky Drive ticket automatically. 1win is Curaçao-licensed (8048/JAZ). Register with code XLBONUS for a 600% deposit bonus to bet more and earn more tickets.'),
])

print('\nHero subtitle fixes done.')
