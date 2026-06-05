#!/usr/bin/env python3
"""Fix remaining ALL-CAPS H1s across the 21 target pages."""
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

# 1win-promo-code.html
rw('1win-promo-code.html', [
    ('GUIDE TO THE <span class="text-gradient">1WIN PROMO CODE XLBONUS</span>',
     '1win Promo Code XLBONUS - complete guide'),
])

# access.html
rw('access.html', [
    ('1WIN <span class="text-gradient">LOGIN</span>',
     '1win login - access your account'),
])

# alternative-link.html
rw('alternative-link.html', [
    ('1WIN ALTERNATIVE <span class="text-gradient">LINK</span>',
     '1win alternative link'),
])

# faq.html
rw('faq.html', [
    ('1WIN <span class="text-gradient">FAQ</span>',
     '1win FAQ'),
])

# index.html
rw('index.html', [
    ('BET AND PLAY AT <span class="text-gradient">1WIN</span>',
     '1win Promo Code XLBONUS - Get a 600% Welcome Bonus'),
])

# live-streaming.html
rw('live-streaming.html', [
    ('1WIN LIVE <span class="text-gradient">STREAMING</span>',
     '1win live streaming'),
])

# mirrors.html
rw('mirrors.html', [
    ('1WIN <span class="text-gradient">MIRROR</span>',
     '1win mirror - working alternative link'),
])

# news.html
rw('news.html', [
    ('1WIN <span class="text-gradient">NEWS</span>',
     '1win news 2026'),
])

# poker.html
rw('poker.html', [
    ('1WIN <span class="text-gradient">POKER</span>',
     '1win poker'),
])

# promotions.html
rw('promotions.html', [
    ('1WIN <span class="text-gradient">PROMOTIONS</span>',
     '1win promotions 2026'),
])

# website.html
rw('website.html', [
    ('1WIN <span class="text-gradient">WEBSITE</span>',
     '1win website - operator information'),
])

print('\nH1 fixes done.')
