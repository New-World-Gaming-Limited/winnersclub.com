#!/usr/bin/env python3
"""
Fix all banned phrases, em dashes, en dashes in the 21 EN category pages.
Only touches the 21 target files; skips country pages and news detail pages.
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

    # ──────────────────────────────────────────────────────────────
    # 1. Remove banned phrases (context-aware replacements)
    # ──────────────────────────────────────────────────────────────
    
    # "BET ANYWHERE. WIN EVERYWHERE." — app.html hero subtitle
    s = s.replace('BET ANYWHERE. WIN EVERYWHERE.',
                  'Download the app. Bet from anywhere.')
    
    # "thousands of sporting events" -> specific
    s = s.replace('thousands of sporting events',
                  '30+ sports with live streaming on selected fixtures')
    s = s.replace('thousands of sporting events live',
                  '30+ sports live')
    s = s.replace('Thousands of events are available each day',
                  '1,000+ events are available each day')
    s = s.replace('Thousands of live events daily',
                  '1,000+ live events daily')
    s = s.replace('thousands of live events daily',
                  '1,000+ live events daily')
    s = s.replace('thousands of ways to win',
                  '11,000+ ways to win')
    s = s.replace('thousands of betting markets available every day',
                  '1,000+ betting markets available every day')
    s = s.replace('Choose from thousands of casino games',
                  'Choose from 11,000+ casino games')
    s = s.replace('thousands of casino games',
                  '11,000+ casino games')
    s = s.replace('thousands of players every day',
                  '100,000+ players every day')
    s = s.replace('Join thousands of players',
                  'Join 1win players worldwide')
    s = s.replace('Join thousands of winners today',
                  'Join 1win today')
    s = s.replace('from thousands of',
                  'from the full 11,000+')
    # Generic catch-all for any remaining "thousands of"
    s = re.sub(r'[Tt]housands of (\w)',
               lambda m: '1,000+ ' + m.group(1) if m.group(1)[0].islower() else '1,000+ ' + m.group(1),
               s)
    
    # "guaranteed" in bonus/payout contexts
    s = s.replace('guaranteed prize pools', 'scheduled prize pools')
    s = s.replace('guaranteed prize pool', 'scheduled prize pool')
    s = s.replace('$10,000 guaranteed freeroll', '$10,000 freeroll')
    s = s.replace('$10K guaranteed freerolls', '$10K freerolls')
    s = s.replace('guaranteed freerolls', 'freerolls')
    s = s.replace('weekly tournaments with guaranteed payouts',
                  'weekly tournaments with fixed prize pools')
    s = s.replace('is not guaranteed', 'may not be possible')
    s = s.replace('not guaranteed', 'subject to support review')
    # Remove "guaranteed" from payout/win contexts
    s = re.sub(r'\bguaranteed\b', 'scheduled', s)
    
    # "risk-free" in poker and elsewhere
    s = s.replace('risk-free', 'no-buy-in')
    
    # "OUTPLAY EVERYONE" — poker hero sub
    s = s.replace("OUTPLAY EVERYONE AT THE TABLE.",
                  "Play Texas Hold'em and Omaha at 1win.")
    s = s.replace("OUTPLAY EVERYONE", "Play poker at 1win")
    
    # "DOMINATE EVERY MATCH" — sports-betting hero
    s = s.replace('DOMINATE EVERY MATCH.',
                  'Bet on 30+ sports at 1win.')
    s = s.replace('DOMINATE EVERY MATCH',
                  'Bet on 30+ sports at 1win')
    
    # "Stack the deck" — sports-betting hero
    s = s.replace('Stack the deck in your favor.',
                  'Use code XLBONUS for a 600% welcome bonus.')
    s = s.replace('Stack the deck', 'Use XLBONUS')
    
    # "Try Your Luck" — casino CTA button
    s = s.replace('>Try Your Luck<', '>Claim My 600% Bonus<')
    s = s.replace('Try Your Luck', 'Claim My 600% Bonus')
    
    # "Hit the Tables" — casino CTA button
    s = s.replace('>Hit the Tables<', '>Play at 1win Casino<')
    s = s.replace('Hit the Tables', 'Play at 1win Casino')
    
    # "instant payouts" -> specific
    s = s.replace('instant payouts', '4-hour average payouts')
    s = s.replace('Instant payouts', '4-hour average payouts')
    
    # "no strings attached"
    s = s.replace('No strings attached', 'Standard bonus terms apply')
    s = s.replace('no strings attached', 'standard bonus terms apply')

    # ──────────────────────────────────────────────────────────────
    # 2. Fix em dashes (—) and en dashes (–) in body copy
    #    Strategy: replace in text nodes but skip <script>, <style>
    #    Simple approach: global replace since scripts use — rarely
    # ──────────────────────────────────────────────────────────────
    
    # We'll do a smart replace: split on script/style blocks, replace in non-script parts
    parts = re.split(r'(<script[\s\S]*?</script>|<style[\s\S]*?</style>)', s)
    new_parts = []
    for i, part in enumerate(parts):
        if part.startswith('<script') or part.startswith('<style'):
            new_parts.append(part)
        else:
            # Replace em dashes
            # In headings: — -> : or comma or hyphen (context-based)
            # In body copy: — -> ,  or just remove
            # Simple: use comma+space or period
            # Em dash at end of clause: replace with comma
            part = re.sub(r'\s—\s', ', ', part)
            part = re.sub(r'—\s', ': ', part)
            part = re.sub(r'\s—', '.', part)
            part = part.replace('—', '-')
            
            # En dashes
            part = re.sub(r'\s–\s', ' to ', part)
            part = re.sub(r'–\s', ' to ', part)
            part = re.sub(r'\s–', ' to', part)
            part = part.replace('–', '-')
            new_parts.append(part)
    s = ''.join(new_parts)

    # ──────────────────────────────────────────────────────────────
    # 3. Fix ALL-CAPS CTAs -> Title Case
    # ──────────────────────────────────────────────────────────────
    # These are button text nodes
    cta_fixes = [
        ('CLAIM YOUR 600% BONUS', 'Claim My 600% Bonus'),
        ('CLAIM MY 600% BONUS', 'Claim My 600% Bonus'),
        ('GET YOUR 600% BONUS', 'Claim My 600% Bonus'),
        ('SIGN UP WITH XLBONUS', 'Register with XLBONUS'),
        ('SIGN UP NOW', 'Register with XLBONUS'),
        ('REGISTER NOW', 'Register with XLBONUS'),
        ('GET STARTED', 'Register with XLBONUS'),
        ('PLAY NOW', 'Play Aviator with XLBONUS'),
        ('DOWNLOAD NOW', 'Download the 1win App'),
        ('ACCESS MIRROR', 'Access Current Mirror'),
    ]
    for old, new in cta_fixes:
        # Only replace in button/a tag text, not inside scripts
        s = re.sub(r'(>)\s*' + re.escape(old) + r'\s*(<)',
                   r'\1' + new + r'\2', s)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    
    changed = s != orig
    return changed


for fname in TARGET_PAGES:
    changed = fix_file(fname)
    print(f'  {"OK" if changed else "no-op"}: {fname}')

print('\nDone fixing violations.')
