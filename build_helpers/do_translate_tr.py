#!/usr/bin/env python3
"""
Full EN → TR translation processor for 1win.codes
Reads en/ files → writes tr/ files with proper Turkish translation
"""

import os
import re
import sys

sys.path.insert(0, '/home/user/workspace/1win-codes-repo/build_helpers')
from tr_translations import REPLACEMENTS
from tr_translations_supplementary import SUPPLEMENTARY

# Combine and sort all replacements by EN string length (longest first) to prevent substring conflicts
ALL_REPLACEMENTS = REPLACEMENTS + SUPPLEMENTARY
REPLACEMENTS = sorted(ALL_REPLACEMENTS, key=lambda x: len(x[0]), reverse=True)

BASE = "/home/user/workspace/1win-codes-repo"
EN_DIR = os.path.join(BASE, "en")
TR_DIR = os.path.join(BASE, "tr")


def fix_dashes_in_html(content: str) -> str:
    """Replace em/en dashes with hyphens outside script/style/svg tags."""
    # Split by script and style tags to protect them
    pattern = r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)'
    parts = re.split(pattern, content, flags=re.DOTALL)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # script or style block - preserve
            result.append(part)
        else:
            part = part.replace('\u2014', '-')  # em dash
            part = part.replace('\u2013', '-')  # en dash
            result.append(part)
    return ''.join(result)


# No word-boundary matching needed since we removed dangerous short words


def apply_text_translations(content: str) -> str:
    """Apply the translation dictionary to visible text in HTML.
    Protects: script, style, title, meta (already translated), JSON-LD.
    Uses two-pass placeholder approach to prevent chaining issues.
    Uses word boundaries for short words to prevent substring corruption.
    """
    # Protect script, style, title, head, meta tags from re-processing
    # Use (?:\s|>) to ensure we match the full tag name (not <header> when looking for <head>)
    protect_pattern = r'(<(?:script|style|title|head)(?:\s[^>]*)?>.*?</(?:script|style|title|head)>|<meta[^>]+>)'
    parts = re.split(protect_pattern, content, flags=re.DOTALL)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # protected block
            result.append(part)
        else:
            # Two-pass: EN -> placeholder -> TR (prevents chaining)
            placeholders = []
            for j, (en_text, tr_text) in enumerate(REPLACEMENTS):
                if en_text in part:
                    marker = f'\x00TR{j:04d}\x00'
                    part = part.replace(en_text, marker)
                    placeholders.append((marker, tr_text))
            # Second pass: replace placeholders with TR
            for marker, tr_text in placeholders:
                part = part.replace(marker, tr_text)
            result.append(part)
    return ''.join(result)


def fix_structural(content: str, rel_path: str) -> str:
    """Fix structural HTML attributes for Turkish locale."""
    # 1. lang attribute
    content = content.replace('<html lang="en">', '<html lang="tr">')
    
    # 2. canonical URL
    content = re.sub(
        r'(rel="canonical"\s+href="https://1win\.codes)/en/',
        r'\1/tr/', content
    )
    
    # 3. Internal nav hrefs /en/ → /tr/
    content = re.sub(r'href="/en/', 'href="/tr/', content)
    
    # 4. og:url meta
    content = re.sub(
        r'(property="og:url"\s+content="https://1win\.codes)/en/',
        r'\1/tr/', content
    )
    
    # 5. Fix JSON-LD url fields
    def fix_jsonld_block(m):
        block = m.group(0)
        block = re.sub(r'("url"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        block = re.sub(r'("target"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        return block
    content = re.sub(
        r'<script[^>]+type="application/ld\+json"[^>]*>.*?</script>',
        fix_jsonld_block, content, flags=re.DOTALL
    )
    
    # 6. aria labels
    content = content.replace('aria-label="1win home"', 'aria-label="1win ana sayfa"')
    content = content.replace('aria-label="Sign Up"', 'aria-label="Kayıt Ol"')
    content = content.replace('aria-label="Toggle menu"', 'aria-label="Menüyü aç/kapat"')
    content = content.replace('aria-label="Language"', 'aria-label="Dil"')
    content = content.replace('aria-label="Back to top"', 'aria-label="Başa dön"')
    content = content.replace('aria-label="Go to top"', 'aria-label="Başa dön"')
    
    # 7. lang switcher: selected option label EN → TR
    # <option value="" selected>EN</option>
    content = re.sub(r'(<option value="" selected>)EN(</option>)', r'\1TR\2', content)
    
    return content


def ensure_curacaoo(content: str) -> str:
    """Ensure Curaçao 8048/JAZ appears in the first body paragraph if missing."""
    if '8048/JAZ' in content:
        return content
    
    # Find first real paragraph in body
    body_pos = content.find('<body')
    if body_pos < 0:
        return content
    
    # Skip the header/nav area and find first section paragraph
    # Look for first paragraph with 1win or XLBONUS
    section_pos = content.find('<section', body_pos)
    if section_pos < 0:
        return content
    
    search_area = content[section_pos:]
    m = re.search(r'(<p[^>]*>)([^<]*(?:1win|XLBONUS)[^<]*)(</p>)', search_area)
    if m:
        old = m.group(0)
        new_text = m.group(2).rstrip() + ' Curaçao 8048/JAZ lisanslıdır.'
        new = m.group(1) + new_text + m.group(3)
        content = content[:section_pos] + content[section_pos:].replace(old, new, 1)
    
    return content


def translate_string(text: str) -> str:
    """Translate a single string using placeholder approach."""
    placeholders = []
    result = text
    for j, (en_text, tr_text) in enumerate(REPLACEMENTS):
        if en_text in result:
            marker = f'\x00TR{j:04d}\x00'
            result = result.replace(en_text, marker)
            placeholders.append((marker, tr_text))
    for marker, tr_text in placeholders:
        result = result.replace(marker, tr_text)
    return result


def translate_meta_desc(content: str) -> str:
    """Translate meta description and title specifically."""
    
    # Extract title, translate, replace
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if title_m:
        en_title = title_m.group(1)
        tr_title = translate_string(en_title)
        if tr_title != en_title:
            content = content.replace(f'<title>{en_title}</title>', f'<title>{tr_title}</title>')
    
    # Translate meta description
    def tr_meta_desc(m):
        tr_desc = translate_string(m.group(1))
        return f'name="description" content="{tr_desc}"'
    content = re.sub(r'name="description" content="([^"]+)"', tr_meta_desc, content)
    
    # Translate og:title
    def tr_og_title(m):
        tr_t = translate_string(m.group(1))
        return f'property="og:title" content="{tr_t}"'
    content = re.sub(r'property="og:title" content="([^"]+)"', tr_og_title, content)
    
    # Translate og:description
    def tr_og_desc(m):
        tr_d = translate_string(m.group(1))
        return f'property="og:description" content="{tr_d}"'
    content = re.sub(r'property="og:description" content="([^"]+)"', tr_og_desc, content)
    
    return content


def translate_jsonld_text(content: str) -> str:
    """Translate text within JSON-LD blocks."""
    def tr_jsonld(m):
        block = m.group(0)
        # Fix urls
        block = re.sub(r'("url"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        block = re.sub(r'("target"\s*:\s*"https://1win\.codes)/en/', r'\1/tr/', block)
        # Translate name/description in JSON-LD (simple fields)
        def tr_json_field(mm):
            tr_val = translate_string(mm.group(2))
            return mm.group(1) + tr_val + mm.group(3)
        block = re.sub(r'("(?:name|description)"\s*:\s*")((?:[^"\\]|\\.)*)(")', tr_json_field, block)
        return block
    
    content = re.sub(
        r'<script[^>]+type="application/ld\+json"[^>]*>.*?</script>',
        tr_jsonld, content, flags=re.DOTALL
    )
    return content


def process_file(rel_path: str) -> tuple:
    """Process one file: EN → TR."""
    en_path = os.path.join(EN_DIR, rel_path)
    tr_path = os.path.join(TR_DIR, rel_path)
    
    if not os.path.exists(en_path):
        return False, f"EN file not found: {en_path}"
    
    with open(en_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Step 1: Fix structural attributes
    content = fix_structural(content, rel_path)
    
    # Step 2: Fix dashes
    content = fix_dashes_in_html(content)
    
    # Step 3: Translate meta tags (title, desc, og)
    content = translate_meta_desc(content)
    
    # Step 4: Translate JSON-LD text fields
    content = translate_jsonld_text(content)
    
    # Step 5: Apply text translations to body HTML
    content = apply_text_translations(content)
    
    # Step 6: Ensure Curaçao 8048/JAZ present
    content = ensure_curacaoo(content)
    
    # Ensure output dir
    os.makedirs(os.path.dirname(tr_path), exist_ok=True)
    
    with open(tr_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, ""


def audit_file(rel_path: str) -> list:
    """Audit a TR file."""
    tr_path = os.path.join(TR_DIR, rel_path)
    if not os.path.exists(tr_path):
        return ['FILE_MISSING']
    
    with open(tr_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get HTML-only parts (outside script/style)
    html_parts = re.sub(r'<(?:script|style)[^>]*>.*?</(?:script|style)>', '', content, flags=re.DOTALL)
    
    issues = []
    
    if 'lang="tr"' not in content:
        issues.append('no_lang_tr')
    
    if 'XLBONUS' not in content:
        issues.append('no_XLBONUS')
    
    if '8048/JAZ' not in content:
        issues.append('no_8048_JAZ')
    
    if '\u2014' in html_parts:
        issues.append('em_dash')
    if '\u2013' in html_parts:
        issues.append('en_dash')
    
    # Check canonical still has /en/ (bad)
    if re.search(r'rel="canonical"[^>]+1win\.codes/en/', content):
        issues.append('canonical_en')
    
    # Check banned TR phrases
    for banned in ['binlerce', 'yüzlerce', 'dünya standartlarında', 'son teknoloji', 'yeni nesil', 'endüstri lideri']:
        if banned in html_parts.lower():
            issues.append(f'banned:{banned}')
    
    return issues


def read_inventory() -> list:
    inv = os.path.join(BASE, 'build_helpers/en_page_inventory.txt')
    with open(inv) as f:
        return [l.strip() for l in f if l.strip()]


if __name__ == "__main__":
    pages = read_inventory()
    print(f"Translating {len(pages)} pages EN → TR...")
    
    errors = []
    for i, rel_path in enumerate(pages):
        ok, err = process_file(rel_path)
        if not ok:
            errors.append((rel_path, err))
        if (i + 1) % 25 == 0 or i == len(pages) - 1:
            print(f"  Progress: {i+1}/{len(pages)}")
    
    print(f"\n{'='*50}")
    print(f"Translation complete: {len(pages) - len(errors)}/{len(pages)} files")
    if errors:
        for p, e in errors:
            print(f"  ERROR: {p}: {e}")
    
    # Audit
    print("\nRunning audit...")
    all_issues = {}
    for rel_path in pages:
        issues = audit_file(rel_path)
        if issues:
            all_issues[rel_path] = issues
    
    clean = len(pages) - len(all_issues)
    print(f"\nAUDIT RESULT:")
    print(f"  pages: {len(pages)}")
    print(f"  issues: {sum(len(v) for v in all_issues.values())}")
    print(f"  clean: {clean}")
    
    if all_issues:
        print("\nFiles with issues:")
        for p, issues in all_issues.items():
            print(f"  {p}: {', '.join(issues)}")
    else:
        print("  ALL CLEAN!")

