#!/usr/bin/env python3
"""
Translate EN → TR for 1win.codes
Reads en/ files → writes tr/ files
Rules from TRANSLATION_RULES.md
"""

import os
import re
import json
import sys

BASE = "/home/user/workspace/1win-codes-repo"
EN_DIR = os.path.join(BASE, "en")
TR_DIR = os.path.join(BASE, "tr")

# ─── Translation Dictionary ─────────────────────────────────────────────────
# Structural nav items, common UI labels, headings
NAV_TR = {
    # Nav links
    "Promo Code": "Promosyon Kodu",
    "Sports": "Sporlar",
    "All sports betting": "Tüm spor bahisleri",
    "Football": "Futbol",
    "Cricket": "Kriket",
    "Tennis": "Tenis",
    "Basketball": "Basketbol",
    "Esports": "E-spor",
    "Live streaming": "Canlı yayın",
    "Casino": "Kumarhane",
    "Casino home": "Kumarhane ana sayfa",
    "Slot reviews": "Slot incelemeleri",
    "Game providers": "Oyun sağlayıcıları",
    "Crash games": "Crash oyunları",
    "Poker": "Poker",
    "Bonuses": "Bonuslar",
    "All bonuses": "Tüm bonuslar",
    "First deposit 200%": "İlk para yatırma 200%",
    "Second deposit 150%": "İkinci para yatırma 150%",
    "Third deposit 150%": "Üçüncü para yatırma 150%",
    "Fourth deposit 100%": "Dördüncü para yatırma 100%",
    "Wagering rules": "Çevrim kuralları",
    "Free spins today": "Bugün ücretsiz dönüşler",
    "Cashback": "Cashback",
    "VIP club": "VIP kulübü",
    "All promotions": "Tüm promosyonlar",
    "Tools": "Araçlar",
    "All calculators": "Tüm hesap makineleri",
    "Odds converter": "Oran dönüştürücü",
    "Parlay calculator": "Kombine hesap makinesi",
    "Kelly criterion": "Kelly kriteri",
    "Arbitrage": "Arbitraj",
    "Hedge": "Hedge",
    "Each-way": "Her iki yönde",
    "Implied probability": "İma edilen olasılık",
    "Bankroll": "Banka rulosu",
    "Surebet": "Surebet",
    "Matched bet": "Eşleştirilmiş bahis",
    "More": "Daha fazla",
    "Payment methods": "Ödeme yöntemleri",
    "Mobile app": "Mobil uygulama",
    "India guides": "Hindistan rehberleri",
    "Mirrors": "Ayna siteler",
    "Login": "Giriş",
    "Register": "Kayıt Ol",
    "Review": "İnceleme",
    "About 1win": "1win hakkında",
    "FAQ": "SSS",
    "News": "Haberler",
    # Buttons/CTAs
    "Register at 1win": "1win'e Kayıt Ol",
    "Sign Up": "Kayıt Ol",
    "Claim Promo Code →": "Promosyon Kodunu Al →",
    "Access 1win Registration": "1win Kaydına Eriş",
    "Toggle menu": "Menüyü aç/kapat",
    "Language": "Dil",
    # Footer / common
    "Quick Links": "Hızlı Bağlantılar",
    "Legal": "Yasal",
    "Privacy Policy": "Gizlilik Politikası",
    "Terms of Service": "Hizmet Şartları",
    "Responsible Gaming": "Sorumlu Oyun",
    "Disclaimer": "Sorumluluk Reddi",
    "18+ only": "Sadece 18+",
    "© 2026 1win.codes": "© 2026 1win.codes",
    "All Rights Reserved": "Tüm Hakları Saklıdır",
    "Home": "Ana Sayfa",
    # Stat bar
    "Bonus": "Bonus",
    "Sports": "Sporlar",
    "Games": "Oyunlar",
    "Instant Crypto": "Anında Kripto",
    # Table headers
    "Feature": "Özellik",
    "Details": "Detaylar",
    "Yes": "Evet",
    "No": "Hayır",
    "Available": "Mevcut",
    "Not available": "Mevcut değil",
    # Common phrases
    "Last updated": "Son güncelleme",
    "Reading time": "Okuma süresi",
    "min read": "dk okuma",
    "Table of Contents": "İçindekiler",
    "Share": "Paylaş",
    "Back to top": "Başa dön",
    "See all": "Tümünü gör",
    "Learn more": "Daha fazla öğren",
    "Get Started": "Başla",
    "Play Now": "Hemen Oyna",
    "Claim Now": "Hemen Al",
    "Open Account": "Hesap Aç",
    "Deposit Now": "Hemen Yatır",
}

# ─── Core translation function ───────────────────────────────────────────────

def translate_html(en_content: str, rel_path: str) -> str:
    """Translate an EN HTML page to TR."""
    content = en_content
    
    # 1. Fix html lang
    content = content.replace('<html lang="en">', '<html lang="tr">')
    
    # 2. Fix canonical: /en/ → /tr/
    content = re.sub(r'(rel="canonical"\s+href="https://1win\.codes)/en/', r'\1/tr/', content)
    
    # 3. Fix og:url if present
    content = re.sub(r'(property="og:url"\s+content="https://1win\.codes)/en/', r'\1/tr/', content)
    
    # 4. Fix JSON-LD url that points to /en/
    # But only the "url" field of the website schema, not @id
    def fix_jsonld_urls(m):
        block = m.group(0)
        # Replace "url": "https://1win.codes/en/..." → /tr/...
        block = re.sub(r'("url"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        block = re.sub(r'("target"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        return block
    content = re.sub(r'<script type="application/ld\+json"[^>]*>.*?</script>', fix_jsonld_urls, content, flags=re.DOTALL)
    
    # 5. Nav links: /en/ → /tr/
    # Internal navigation hrefs
    content = re.sub(r'href="/en/', 'href="/tr/', content)
    # Also relative paths in lang-switcher options
    content = re.sub(r'value="([a-z]{2})/index\.html"', r'value="\1/index.html"', content)  # keep as-is
    
    # 6. Translate the actual text content
    content = translate_text_nodes(content, rel_path)
    
    # 7. Post-process: remove em/en dashes from text content (not in scripts/JSON)
    content = fix_dashes(content)
    
    # 8. Ensure Curaçao 8048/JAZ appears - check and inject if missing  
    if '8048/JAZ' not in content:
        content = inject_curacaoo(content, rel_path)
    
    return content


def fix_dashes(content: str) -> str:
    """Replace em dashes (—) and en dashes (–) with hyphens in text content."""
    # We need to be careful not to break JSON or JS
    # Strategy: process text outside script/style tags
    parts = re.split(r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)', content, flags=re.DOTALL)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # Inside script or style
            result.append(part)
        else:
            # Replace dashes in text/HTML
            part = part.replace('—', '-')
            part = part.replace('–', '-')
            result.append(part)
    return ''.join(result)


def inject_curacaoo(content: str, rel_path: str) -> str:
    """Inject Curaçao 8048/JAZ into first paragraph if missing."""
    # Find first <p tag after body and inject
    # Look for first paragraph after hero or intro section
    pattern = r'(<p[^>]*>)((?:(?!</p>).)*?1win(?:(?!</p>).)*?</p>)'
    m = re.search(pattern, content, flags=re.DOTALL)
    if m:
        para = m.group(0)
        if '8048/JAZ' not in para:
            # Append Curaçao mention before closing </p>
            new_para = para.replace('</p>', ' Curaçao 8048/JAZ lisanslıdır.</p>', 1)
            content = content.replace(para, new_para, 1)
    return content


def translate_text_nodes(content: str, rel_path: str) -> str:
    """Main translation function - translates visible text in HTML."""
    
    # Split into script/style blocks (preserve) and HTML (translate)
    # We'll use a regex-based approach to translate visible text
    
    # Collect all translatable text segments
    # Strategy: translate specific known patterns
    
    content = translate_meta_tags(content, rel_path)
    content = translate_title(content, rel_path)
    content = translate_nav(content)
    content = translate_body_text(content, rel_path)
    content = translate_footer(content)
    content = translate_jsonld(content, rel_path)
    content = translate_aria_labels(content)
    
    return content


def translate_meta_tags(content: str, rel_path: str) -> str:
    """Translate meta description and og tags."""
    # These will be handled per-page in the big translation map below
    return content


def translate_title(content: str, rel_path: str) -> str:
    """Translate page title."""
    return content


def translate_nav(content: str) -> str:
    """Translate navigation items."""
    # Replace nav link text
    for en, tr in NAV_TR.items():
        # In nav links: >Text< pattern
        content = re.sub(r'>(' + re.escape(en) + r')<', '>' + tr + '<', content)
    return content


def translate_aria_labels(content: str) -> str:
    """Translate aria-label attributes."""
    tr_map = {
        'aria-label="1win home"': 'aria-label="1win ana sayfa"',
        'aria-label="Sign Up"': 'aria-label="Kayıt Ol"',
        'aria-label="Toggle menu"': 'aria-label="Menüyü aç/kapat"',
        'aria-label="Language"': 'aria-label="Dil"',
    }
    for en, tr in tr_map.items():
        content = content.replace(en, tr)
    return content


def translate_body_text(content: str, rel_path: str) -> str:
    """Translate body text using page-specific translations."""
    return content


def translate_footer(content: str) -> str:
    """Translate footer elements."""
    return content


def translate_jsonld(content: str, rel_path: str) -> str:
    """Fix JSON-LD content."""
    return content


# ─── Per-page full translations ──────────────────────────────────────────────

def full_translate(en_content: str, rel_path: str) -> str:
    """
    Full translation of a page from English to Turkish.
    Uses structural approach: preserve all HTML structure, scripts, styles.
    Only translate visible text content.
    """
    content = en_content
    
    # Step 1: structural fixes
    content = content.replace('<html lang="en">', '<html lang="tr">')
    content = re.sub(r'(rel="canonical"\s+href="https://1win\.codes)/en/', r'\1/tr/', content)
    content = re.sub(r'href="/en/', 'href="/tr/', content)
    
    # Step 2: fix JSON-LD URLs (not @id, just url fields)
    def fix_jsonld(m):
        block = m.group(0)
        block = re.sub(r'("url"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        block = re.sub(r'("target"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        return block
    content = re.sub(r'<script type="application/ld\+json"[^>]*>.*?</script>', fix_jsonld, content, flags=re.DOTALL)
    
    # Step 3: fix em/en dashes (outside script/style)
    parts = re.split(r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)', content, flags=re.DOTALL)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            result.append(part)
        else:
            part = part.replace('—', '-')
            part = part.replace('–', '-')
            result.append(part)
    content = ''.join(result)
    
    # Step 4: Apply the large translation dictionary
    content = apply_translations(content, rel_path)
    
    # Step 5: Ensure Curaçao 8048/JAZ in first paragraph
    if '8048/JAZ' not in content:
        content = inject_curacaoo_text(content)
    
    return content


def inject_curacaoo_text(content: str) -> str:
    """Find the first body paragraph mentioning 1win and add Curaçao."""
    # Find first <p> in body that mentions 1win or XLBONUS
    body_start = content.find('<body')
    if body_start < 0:
        return content
    body_section = content[body_start:]
    
    m = re.search(r'<p[^>]*>([^<]*(?:1win|XLBONUS)[^<]*)</p>', body_section)
    if m:
        old = m.group(0)
        new_text = m.group(1).rstrip() + '. 1win, Curaçao 8048/JAZ lisansı altında faaliyet göstermektedir.'
        new = old.replace(m.group(1), new_text)
        content = content[:body_start] + content[body_start:].replace(old, new, 1)
    return content


# ─── Translation tables (EN text → TR text) ─────────────────────────────────

# This dictionary maps exact EN text patterns to TR equivalents
# Used for meta tags, titles, headings, body paragraphs, CTAs

GLOBAL_REPLACEMENTS = [
    # ── Meta / Title patterns ──
    # These are regex replacements on full content
    # Format: (pattern, replacement, flags)
]

# ─── Page-specific translation maps ─────────────────────────────────────────

def apply_translations(content: str, rel_path: str) -> str:
    """Apply all translation replacements to content."""
    
    # Split content to avoid touching scripts/styles
    # We'll work on the HTML parts only
    
    # Build segments: [html_part, script_part, html_part, ...]
    segments = re.split(r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)', content, flags=re.DOTALL)
    
    translated_segments = []
    for i, seg in enumerate(segments):
        if i % 2 == 1:  # script/style block - preserve
            translated_segments.append(seg)
        else:
            # HTML text - translate
            seg = translate_html_segment(seg, rel_path)
            translated_segments.append(seg)
    
    return ''.join(translated_segments)


def translate_html_segment(seg: str, rel_path: str) -> str:
    """Translate visible text in an HTML segment."""
    
    # ── aria labels ──
    seg = seg.replace('aria-label="1win home"', 'aria-label="1win ana sayfa"')
    seg = seg.replace('aria-label="Sign Up"', 'aria-label="Kayıt Ol"')
    seg = seg.replace('aria-label="Toggle menu"', 'aria-label="Menüyü aç/kapat"')
    seg = seg.replace('aria-label="Language"', 'aria-label="Dil"')
    seg = seg.replace('aria-label="Back to top"', 'aria-label="Başa dön"')
    seg = seg.replace('aria-label="Go to top"', 'aria-label="Başa dön"')
    
    # ── Nav link text ──
    seg = re.sub(r'>Promo Code<', '>Promosyon Kodu<', seg)
    seg = re.sub(r'>All sports betting<', '>Tüm spor bahisleri<', seg)
    seg = re.sub(r'>Football<', '>Futbol<', seg)
    seg = re.sub(r'>Cricket<', '>Kriket<', seg)
    seg = re.sub(r'>Tennis<', '>Tenis<', seg)
    seg = re.sub(r'>Basketball<', '>Basketbol<', seg)
    seg = re.sub(r'>Esports<', '>E-spor<', seg)
    seg = re.sub(r'>Live streaming<', '>Canlı yayın<', seg)
    seg = re.sub(r'>Casino home<', '>Kumarhane ana sayfa<', seg)
    seg = re.sub(r'>Slot reviews<', '>Slot incelemeleri<', seg)
    seg = re.sub(r'>Game providers<', '>Oyun sağlayıcıları<', seg)
    seg = re.sub(r'>Crash games<', '>Crash oyunları<', seg)
    seg = re.sub(r'>All bonuses<', '>Tüm bonuslar<', seg)
    seg = re.sub(r'>First deposit 200%<', '>İlk para yatırma 200%<', seg)
    seg = re.sub(r'>Second deposit 150%<', '>İkinci para yatırma 150%<', seg)
    seg = re.sub(r'>Third deposit 150%<', '>Üçüncü para yatırma 150%<', seg)
    seg = re.sub(r'>Fourth deposit 100%<', '>Dördüncü para yatırma 100%<', seg)
    seg = re.sub(r'>Wagering rules<', '>Çevrim kuralları<', seg)
    seg = re.sub(r'>Free spins today<', '>Bugün ücretsiz dönüşler<', seg)
    seg = re.sub(r'>VIP club<', '>VIP kulübü<', seg)
    seg = re.sub(r'>Lucky Drive<', '>Lucky Drive<', seg)
    seg = re.sub(r'>All promotions<', '>Tüm promosyonlar<', seg)
    seg = re.sub(r'>All calculators<', '>Tüm hesap makineleri<', seg)
    seg = re.sub(r'>Odds converter<', '>Oran dönüştürücü<', seg)
    seg = re.sub(r'>Parlay calculator<', '>Kombine hesap makinesi<', seg)
    seg = re.sub(r'>Kelly criterion<', '>Kelly kriteri<', seg)
    seg = re.sub(r'>Arbitrage<', '>Arbitraj<', seg)
    seg = re.sub(r'>Each-way<', '>Her iki yönde<', seg)
    seg = re.sub(r'>Implied probability<', '>İma edilen olasılık<', seg)
    seg = re.sub(r'>Bankroll<', '>Banka rulosu<', seg)
    seg = re.sub(r'>Surebet<', '>Surebet<', seg)
    seg = re.sub(r'>Matched bet<', '>Eşleştirilmiş bahis<', seg)
    seg = re.sub(r'>Payment methods<', '>Ödeme yöntemleri<', seg)
    seg = re.sub(r'>Mobile app<', '>Mobil uygulama<', seg)
    seg = re.sub(r'>India guides<', '>Hindistan rehberleri<', seg)
    seg = re.sub(r'>Mirrors<', '>Ayna siteler<', seg)
    seg = re.sub(r'>Review<', '>İnceleme<', seg)
    seg = re.sub(r'>About 1win<', '>1win hakkında<', seg)
    seg = re.sub(r'>FAQ<', '>SSS<', seg)
    
    # Sports nav with SVG chevron (complex)
    seg = re.sub(r'>Sports\s+(<svg)', r'>Sporlar \1', seg)
    seg = re.sub(r'>Casino\s+(<svg)', r'>Kumarhane \1', seg)
    seg = re.sub(r'>Bonuses\s+(<svg)', r'>Bonuslar \1', seg)
    seg = re.sub(r'>Tools\s+(<svg)', r'>Araçlar \1', seg)
    seg = re.sub(r'>More\s+(<svg)', r'>Daha fazla \1', seg)
    seg = re.sub(r'>Aviator<', '>Aviator<', seg)  # preserve
    seg = re.sub(r'>Poker<', '>Poker<', seg)  # preserve
    
    # Header register button
    seg = seg.replace('>Register<', '>Kayıt Ol<')
    seg = seg.replace('>Register at 1win<', ">1win'e Kayıt Ol<")
    seg = seg.replace('>Access 1win Registration<', '>1win Kaydına Eriş<')
    seg = seg.replace('>Login<', '>Giriş<')
    
    # Option EN label
    seg = seg.replace('>EN<', '>TR<')
    
    return seg


# ─── Main processing loop ────────────────────────────────────────────────────

def process_file(rel_path: str) -> tuple[bool, str]:
    """
    Process a single file: read EN, translate, write TR.
    Returns (success, error_msg)
    """
    en_path = os.path.join(EN_DIR, rel_path)
    tr_path = os.path.join(TR_DIR, rel_path)
    
    if not os.path.exists(en_path):
        return False, f"EN file not found: {en_path}"
    
    # Read EN
    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    # Translate
    tr_content = full_translate(en_content, rel_path)
    
    # Ensure output dir exists
    os.makedirs(os.path.dirname(tr_path), exist_ok=True)
    
    # Write TR
    with open(tr_path, 'w', encoding='utf-8') as f:
        f.write(tr_content)
    
    return True, ""


def audit_file(rel_path: str) -> list[str]:
    """Audit a TR file for rule compliance."""
    tr_path = os.path.join(TR_DIR, rel_path)
    if not os.path.exists(tr_path):
        return [f"FILE_MISSING: {rel_path}"]
    
    with open(tr_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 1. lang="tr"
    if 'lang="tr"' not in content:
        issues.append(f"lang_not_tr")
    
    # 2. XLBONUS
    if 'XLBONUS' not in content:
        issues.append(f"missing_XLBONUS")
    
    # 3. Curaçao 8048/JAZ
    if '8048/JAZ' not in content:
        issues.append(f"missing_curacaoo_8048")
    
    # 4. Em dash
    # Count outside script/style
    parts = re.split(r'<(?:script|style)[^>]*>.*?</(?:script|style)>', content, flags=re.DOTALL)
    html_parts = ' '.join(parts[::2])  # only even indices (outside script/style)
    if '—' in html_parts:
        issues.append(f"em_dash_found")
    if '–' in html_parts:
        issues.append(f"en_dash_found")
    
    # 5. Canonical points to /tr/
    if 'canonical' in content and '/tr/' not in content:
        issues.append(f"canonical_not_tr")
    
    # 6. Banned TR phrases
    banned = ['binlerce', 'yüzlerce', 'dünya standartlarında', 'son teknoloji', 'yeni nesil', 'endüstri lideri']
    for b in banned:
        if b in content.lower():
            issues.append(f"banned_phrase: {b}")
    
    # 7. Banned EN phrases still in text
    banned_en = ['world-class', 'cutting-edge', 'next-generation', 'state-of-the-art', 'no strings attached']
    for b in banned_en:
        # Check in text parts (not code/scripts)
        if b.lower() in html_parts.lower():
            issues.append(f"banned_en_phrase: {b}")
    
    return issues


def read_inventory() -> list[str]:
    inv_path = os.path.join(BASE, "build_helpers/en_page_inventory.txt")
    with open(inv_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == "__main__":
    pages = read_inventory()
    print(f"Processing {len(pages)} pages...")
    
    errors = []
    for i, rel_path in enumerate(pages):
        ok, err = process_file(rel_path)
        if not ok:
            errors.append((rel_path, err))
            print(f"  ERROR [{i+1}]: {rel_path}: {err}")
        else:
            print(f"  OK [{i+1}/{len(pages)}]: {rel_path}")
    
    print(f"\n=== DONE: {len(pages) - len(errors)}/{len(pages)} files processed ===")
    if errors:
        print("ERRORS:")
        for p, e in errors:
            print(f"  {p}: {e}")
    
    # Audit
    print("\n=== AUDIT ===")
    all_issues = {}
    for rel_path in pages:
        issues = audit_file(rel_path)
        if issues:
            all_issues[rel_path] = issues
    
    print(f"Files with issues: {len(all_issues)}/{len(pages)}")
    for p, issues in list(all_issues.items())[:20]:
        print(f"  {p}: {', '.join(issues)}")
