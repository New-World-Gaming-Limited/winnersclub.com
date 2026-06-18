#!/usr/bin/env python3
"""Update sitemap.xml and lang-redirect.js for Arabic locale."""
import os, re

ROOT = '/home/user/workspace/winnersclub.com'

# ── Update sitemap.xml ────────────────────────────────────────────────────
AR_PAGES = [
    ('', '1.0'),          # index
    ('promo-code/', '1.0'),
    ('casino/', '0.9'),
    ('sports/', '0.9'),
    ('poker/', '0.9'),
    ('aviator/', '0.9'),
    ('live-casino/', '0.8'),
    ('live-odds/', '0.8'),
    ('originals/', '0.8'),
    ('slots/', '0.8'),
    ('payments/', '0.9'),
    ('reserves/', '0.8'),
    ('vip/', '0.8'),
    ('mirror/', '0.8'),
    ('about-stake/', '0.8'),
    ('responsible-gambling/', '0.7'),
    ('stake-engine/', '0.7'),
    ('news/', '0.7'),
    ('stake-us-bonus/', '0.8'),
]

def build_ar_sitemap_entries():
    """Build sitemap <url> entries for all 19 /ar/ pages."""
    hreflang_langs = [
        ('en', ''), ('ko', 'ko/'), ('zh-Hans', 'zh/'), ('vi', 'vi/'),
        ('th', 'th/'), ('ms', 'ms/'), ('pt', 'pt/'), ('ja', 'ja/'),
        ('es', 'es/'), ('pt-BR', 'pt-br/'), ('tr', 'tr/'), ('id', 'id/'),
        ('fr', 'fr/'), ('ru', 'ru/'), ('hi', 'hi/'), ('ar', 'ar/'),
        ('x-default', ''),
    ]
    
    entries = []
    for slug, priority in AR_PAGES:
        en_path = slug  # English equivalent
        loc = f'https://winnersclub.com/ar/{slug}'
        
        links = []
        for lang, prefix in hreflang_langs:
            href = f'https://winnersclub.com/{prefix}{slug}'
            links.append(f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>')
        
        entry = f'''  <url>
    <loc>{loc}</loc>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
{chr(10).join(links)}
  </url>'''
        entries.append(entry)
    
    return '\n'.join(entries)

# Also update existing sitemap entries to add ar hreflang
def update_sitemap():
    sitemap_path = os.path.join(ROOT, 'sitemap.xml')
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add AR to existing <url> blocks that don't have it
    def add_ar_to_url_block(match):
        block = match.group(0)
        if 'hreflang="ar"' in block:
            return block
        
        # Extract x-default href to derive the path
        xd_match = re.search(r'hreflang="x-default" href="https://winnersclub\.com(/[^"]*)"', block)
        if xd_match:
            xd_path = xd_match.group(1)  # e.g. /promo-code/
            ar_url = f'https://winnersclub.com/ar{xd_path}'
        else:
            ar_url = 'https://winnersclub.com/ar/'
        
        ar_link = f'    <xhtml:link rel="alternate" hreflang="ar" href="{ar_url}"/>'
        # Insert before x-default
        block = re.sub(
            r'(\s*<xhtml:link rel="alternate" hreflang="x-default")',
            '\n' + ar_link + r'\1',
            block, count=1
        )
        return block
    
    content = re.sub(r'<url>.*?</url>', add_ar_to_url_block, content, flags=re.DOTALL)
    
    # Append 19 new /ar/ entries before </urlset>
    ar_entries = build_ar_sitemap_entries()
    content = content.replace('</urlset>', ar_entries + '\n</urlset>')
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Count URLs
    count = content.count('<loc>')
    print(f"sitemap.xml updated: {count} total URLs")

update_sitemap()

# ── Update lang-redirect.js ───────────────────────────────────────────────
def update_lang_redirect():
    lr_path = os.path.join(ROOT, 'lang-redirect.js')
    with open(lr_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update supportedLangs array to include 'ar'
    content = content.replace(
        "var supportedLangs = ['en','ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi'];",
        "var supportedLangs = ['en','ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi','ar'];"
    )
    
    # Add Arabic country mappings after the Hindi section
    ar_mapping = """    // Arabic (Arab world)
    'SA':'ar','AE':'ar','EG':'ar','IQ':'ar','JO':'ar','KW':'ar','LB':'ar',
    'LY':'ar','MA':'ar','OM':'ar','PS':'ar','QA':'ar','SY':'ar','TN':'ar',
    'YE':'ar','BH':'ar','DZ':'ar','SD':'ar','MR':'ar',"""
    
    # Insert after Hindi mapping line
    content = content.replace(
        "    // Hindi (India)\n    'IN':'hi'",
        "    // Hindi (India)\n    'IN':'hi',\n" + ar_mapping
    )
    
    with open(lr_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("lang-redirect.js updated with Arabic country mappings")

update_lang_redirect()

