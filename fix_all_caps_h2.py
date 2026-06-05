#!/usr/bin/env python3
"""
Fix ALL remaining ALL-CAPS H2s across all 21 target pages.
Uses regex to find and convert them to sentence case.
"""
import os, re

BASE = '/home/user/workspace/1win-codes-repo/en'

TARGET_PAGES = [
    '1win-promo-code.html', 'access.html', 'alternative-link.html',
    'app.html', 'aviator.html', 'casino.html', 'faq.html', 'index.html',
    'live-streaming.html', 'lucky-drive.html', 'mirrors.html', 'news.html',
    'payment-methods.html', 'poker.html', 'promo-code.html', 'promotions.html',
    'register.html', 'review.html', 'sports-betting.html', 'vip-club.html',
    'website.html',
]

# Words that should stay uppercase in headings
PRESERVE_UPPER = {'XLBONUS', '1WIN', 'FAQ', 'FAQs', 'VPN', 'KYC', 'UPI', 'PIX',
                  'APK', 'iOS', 'HTML', 'ID', 'OTP', 'SMS', 'UFC', 'IPL', 'NBA',
                  'NFL', 'MMA', 'ATP', 'WTA', 'BTC', 'ETH', 'USDT', 'TRX', 'LTC',
                  'DOGE', 'ISP', 'DNS', 'VIP', 'RTP', 'SLA', '2FA', 'URL',
                  '1WIN', 'A&E', 'UK', 'US', 'EU', 'SA', 'RNG'}

def smart_sentence_case(text):
    """Convert ALL-CAPS text to Sentence case, preserving known abbreviations."""
    if not text:
        return text
    
    # If it's already not all-caps, leave it
    words = text.split()
    upper_words = sum(1 for w in words if w.replace("'", '').isupper() and len(w) > 1)
    alpha_words = sum(1 for w in words if any(c.isalpha() for c in w))
    
    if alpha_words == 0 or upper_words / max(alpha_words, 1) < 0.5:
        return text  # Not mostly uppercase, leave it
    
    # Convert to sentence case
    result = []
    for i, word in enumerate(words):
        # Strip punctuation for comparison
        clean = re.sub(r'[^A-Za-z0-9]', '', word)
        
        if clean.upper() in PRESERVE_UPPER:
            result.append(word)
        elif i == 0:
            # Capitalize first letter of sentence
            result.append(word[0].upper() + word[1:].lower() if word else word)
        elif clean.isupper() and len(clean) > 1:
            # Regular all-caps word -> lowercase
            result.append(word.lower())
        else:
            result.append(word)
    
    return ' '.join(result)


def fix_h2_in_content(content):
    """Find all H2 tags and fix their inner text."""
    
    def fix_h2(m):
        open_tag = m.group(1)
        inner = m.group(2)
        close_tag = m.group(3)
        
        # Extract text, keeping HTML tags
        text_only = re.sub(r'<[^>]+>', '', inner).strip()
        
        # Check if mostly uppercase
        alpha_chars = [c for c in text_only if c.isalpha()]
        if not alpha_chars:
            return m.group(0)
        
        upper_ratio = sum(1 for c in alpha_chars if c.isupper()) / len(alpha_chars)
        
        if upper_ratio < 0.6:
            return m.group(0)  # Not mostly uppercase
        
        # Fix: replace the text parts (not inside tags)
        # Strategy: process text nodes within H2
        def fix_text_node(tm):
            txt = tm.group(0)
            # Only fix if it's a text node (not inside a tag)
            return smart_sentence_case(txt)
        
        # Split by HTML tags and fix text nodes
        parts = re.split(r'(<[^>]+>)', inner)
        fixed_parts = []
        for part in parts:
            if part.startswith('<'):
                fixed_parts.append(part)
            else:
                fixed_parts.append(smart_sentence_case(part))
        
        fixed_inner = ''.join(fixed_parts)
        return open_tag + fixed_inner + close_tag
    
    return re.sub(r'(<h2[^>]*>)(.*?)(</h2>)', fix_h2, content, flags=re.DOTALL)


changed_count = 0
for fname in TARGET_PAGES:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    orig = s
    
    # Split out scripts and styles first
    parts = re.split(r'(<script[\s\S]*?</script>|<style[\s\S]*?</style>)', s)
    new_parts = []
    for part in parts:
        if part.startswith('<script') or part.startswith('<style'):
            new_parts.append(part)
        else:
            new_parts.append(fix_h2_in_content(part))
    s = ''.join(new_parts)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    
    if s != orig:
        changed_count += 1
        print(f'  OK: {fname}')
    else:
        print(f'  no-op: {fname}')

print(f'\nFixed {changed_count} files.')

# Verify: show remaining ALL-CAPS H2s
print('\n=== Remaining ALL-CAPS H2s (>60% uppercase) ===')
for fn in TARGET_PAGES:
    s = open(os.path.join(BASE, fn), encoding='utf-8').read()
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', s, re.DOTALL)
    for h2 in h2s:
        txt = re.sub(r'<[^>]+>', '', h2).strip()
        alpha = [c for c in txt if c.isalpha()]
        if alpha and sum(1 for c in alpha if c.isupper())/len(alpha) > 0.6 and len(txt) > 5:
            print(f'  {fn}: {repr(txt[:70])}')
