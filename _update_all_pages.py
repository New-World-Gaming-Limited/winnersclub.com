#!/usr/bin/env python3
"""
Update all existing site pages to add /ar/ hreflang + language switcher AR entry.
Also update sitemap.xml, lang-redirect.js, and refresh /tr/ pages.
"""
import os, re, glob

ROOT = '/home/user/workspace/winnersclub.com'

# ── Step 1: Update hreflang and language switcher on ALL non-ar pages ─────

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changed = False
    
    # 1. Add hreflang="ar" link if missing
    if 'hreflang="ar"' not in content:
        # Insert before hreflang="x-default" line
        content = re.sub(
            r'(\s*<link rel="alternate" hreflang="x-default")',
            r'\n  <link rel="alternate" hreflang="ar" href="ARURL">\1',
            content, count=1
        )
        
        # Determine the AR URL for this page
        # Get path relative to ROOT
        rel = filepath.replace(ROOT + '/', '')
        # Figure out the slug (directory-based)
        parts = rel.split('/')
        if parts[0] == 'ar':
            # Skip ar pages themselves
            return False
        
        # Determine the page slug for ar URL
        # e.g. en/index.html -> ar/
        #      ko/casino/index.html -> ar/casino/
        #      promo-code/index.html -> ar/promo-code/
        
        # Find x-default href value to derive the path
        xdefault_match = re.search(r'hreflang="x-default" href="https://winnersclub\.com(/[^"]*)"', content)
        if xdefault_match:
            xd_path = xdefault_match.group(1)  # e.g. /promo-code/ or /casino/
            ar_url = f'https://winnersclub.com/ar{xd_path}'
        else:
            # Fallback: try to build from filepath
            if 'index.html' in rel:
                dir_parts = rel.replace('/index.html', '').split('/')
                # Remove locale prefix if present
                known_locales = ['en','ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi','ar']
                if dir_parts[0] in known_locales:
                    dir_parts = dir_parts[1:]
                if dir_parts and dir_parts[0]:
                    slug = '/'.join(dir_parts)
                    ar_url = f'https://winnersclub.com/ar/{slug}/'
                else:
                    ar_url = 'https://winnersclub.com/ar/'
            else:
                ar_url = 'https://winnersclub.com/ar/'
        
        content = content.replace('ARURL', ar_url)
        changed = True
    
    # 2. Add العربية to desktop language switcher if missing
    if 'العربية' not in content:
        # Add Arabic option to desktop lang-switcher (before closing </select>)
        # Pattern: last </select> in header-actions
        # We'll look for the pattern of the desktop switcher and add before closing tag
        content = re.sub(
            r'(<select class="lang-switcher"[^>]*>)(.*?)(</select>)',
            lambda m: m.group(1) + m.group(2) + '<option value="https://winnersclub.com/ar/">العربية</option>' + m.group(3),
            content, count=1, flags=re.DOTALL
        )
        
        # Add Arabic option to mobile lang selector (mobile-lang-block)
        content = re.sub(
            r'(<div class="mobile-lang-block">.*?<select[^>]*>)(.*?)(</select></div>)',
            lambda m: m.group(1) + m.group(2) + '<option value="/ar/">العربية (Arabic)</option>' + m.group(3),
            content, count=1, flags=re.DOTALL
        )
        changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Find all HTML files except in /ar/
def find_all_html(root):
    result = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden dirs, ar dir, and script dirs
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and not d.startswith('_')
                       and d != 'ar' and d != '__pycache__' and d != 'node_modules']
        for f in filenames:
            if f.endswith('.html') and not f.startswith('_'):
                full = os.path.join(dirpath, f)
                # Skip 404.html at root
                if full == os.path.join(root, '404.html'):
                    continue
                result.append(full)
    return result

print("Finding all HTML files...")
all_html = find_all_html(ROOT)
# Exclude /ar/ pages (already have ar hreflang)
all_html = [f for f in all_html if '/ar/' not in f.replace(ROOT, '')]
print(f"Found {len(all_html)} HTML files to update")

updated = 0
skipped = 0
for fp in all_html:
    try:
        if process_html_file(fp):
            updated += 1
        else:
            skipped += 1
    except Exception as e:
        print(f"ERROR {fp}: {e}")

print(f"Updated: {updated}, Skipped (already had ar): {skipped}")

