#!/usr/bin/env python3
"""
Audit script for Arabic (AR) translated pages.
Checks all 184 pages from en_page_inventory.txt.
"""
import os
import json
import re
import sys

AR_BASE = '/home/user/workspace/1win-codes-repo/ar/'
EN_BASE = '/home/user/workspace/1win-codes-repo/en/'
INVENTORY = '/home/user/workspace/1win-codes-repo/build_helpers/en_page_inventory.txt'

BANNED_PHRASES = [
    'hit the tables', 'dominate every match', 'outplay everyone',
    'no strings attached', 'bet anywhere win everywhere',
    'thousands of', 'hundreds of',
    'world-class', 'cutting-edge', 'next-generation', 'state-of-the-art',
    # Arabic equivalents
    'الآلاف من', 'المئات من', 'عالمي المستوى', 'أحدث التقنيات', 'الجيل التالي', 'حديث'
]

def check_json_ld(content):
    """Extract and validate all JSON-LD blocks."""
    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    for s in scripts:
        try:
            json.loads(s.strip())
        except json.JSONDecodeError as e:
            return False, str(e)
    return True, None

def audit_file(page_path):
    """Audit a single AR file. Returns list of issues."""
    ar_path = os.path.join(AR_BASE, page_path)
    issues = []

    if not os.path.exists(ar_path):
        return [f"MISSING: {page_path}"]

    with open(ar_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. No em dashes, no en dashes
    if '—' in content:
        issues.append(f"EM_DASH: found em dash in {page_path}")
    if '–' in content:
        issues.append(f"EN_DASH: found en dash in {page_path}")

    # 2. XLBONUS present (uppercase)
    if 'XLBONUS' not in content:
        issues.append(f"NO_XLBONUS: XLBONUS not found in {page_path}")

    # 3. Curaçao 8048/JAZ present
    if 'Curaçao 8048/JAZ' not in content and '8048/JAZ' not in content and '8048' not in content:
        issues.append(f"NO_CURACAO: Curaçao 8048/JAZ not found in {page_path}")

    # 4. No banned phrases (case-insensitive, with Arabic word boundary awareness)
    content_lower = content.lower()
    for phrase in BANNED_PHRASES:
        phrase_lower = phrase.lower()
        if phrase_lower in content_lower:
            # For Arabic phrases, check word boundaries to avoid false positives
            # e.g. 'حديث' should not match inside 'تحديث' (update)
            idx = content_lower.find(phrase_lower)
            found_standalone = False
            while idx >= 0:
                before = content_lower[idx-1] if idx > 0 else ' '
                after = content_lower[idx+len(phrase_lower)] if idx+len(phrase_lower) < len(content_lower) else ' '
                # Arabic chars range: \u0600-\u06FF
                before_is_ar = '\u0600' <= before <= '\u06ff'
                after_is_ar = '\u0600' <= after <= '\u06ff'
                if not before_is_ar and not after_is_ar:
                    found_standalone = True
                    break
                idx = content_lower.find(phrase_lower, idx+1)
            if found_standalone:
                issues.append(f"BANNED_PHRASE '{phrase}': found in {page_path}")

    # 5. html lang="ar"
    if 'lang="ar"' not in content and "lang='ar'" not in content:
        issues.append(f"WRONG_LANG: html lang is not 'ar' in {page_path}")

    # 6. hreflang block: check for all 46 locales + x-default
    required_locales = ['ar','bg','bn','cs','da','de','el','en','es','et','fa','fi','fr',
                        'he','hi','hr','hu','id','it','ja','kk','ko','lo','lt','lv','mn',
                        'ms','mt','nb','nl','pl','pt','ro','ru','sk','sl','sq','sr','sv',
                        'th','tl','tr','uk','ur','uz','vi','zh','x-default']
    for loc in required_locales:
        if f'hreflang="{loc}"' not in content and f"hreflang='{loc}'" not in content:
            issues.append(f"MISSING_HREFLANG_{loc}: in {page_path}")

    # 7. canonical points to /ar/
    # Extract canonical href
    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    if canonical_match:
        canonical = canonical_match.group(1)
        if '/ar/' not in canonical and not canonical.endswith('/ar/'):
            issues.append(f"WRONG_CANONICAL: '{canonical}' doesn't contain /ar/ in {page_path}")
    else:
        issues.append(f"NO_CANONICAL: in {page_path}")

    # 8. JSON-LD validates
    valid, err = check_json_ld(content)
    if not valid:
        issues.append(f"INVALID_JSON_LD: {err} in {page_path}")

    # 9. dir="rtl" present
    if 'dir="rtl"' not in content and "dir='rtl'" not in content:
        issues.append(f"NO_RTL: dir=rtl not found in {page_path}")

    # 10. GA4 present
    if 'G-S2MXR8D3HS' not in content:
        issues.append(f"NO_GA4: GA4 tracking not found in {page_path}")

    # 11. exit-tracker.js present
    if 'exit-tracker.js' not in content:
        issues.append(f"NO_EXIT_TRACKER: exit-tracker.js not found in {page_path}")

    # 12. Eastern Arabic numerals check (should use ASCII numerals for 8048, XLBONUS amounts etc.)
    eastern_digits = re.findall(r'[٠١٢٣٤٥٦٧٨٩]', content)
    if eastern_digits:
        # Only warn if they appear in critical strings
        critical_check = any(d in content for d in ['٨٠٤٨', '٦٠٠٪', '٢٠٠٪'])
        if critical_check:
            issues.append(f"EASTERN_NUMERALS: Eastern Arabic numerals in critical strings in {page_path}")

    return issues

def main():
    with open(INVENTORY) as f:
        pages = [l.strip() for l in f if l.strip()]

    all_issues = []
    missing_count = 0
    clean_count = 0
    issue_count = 0

    for page in pages:
        page_issues = audit_file(page)
        if page_issues:
            if any('MISSING' in i for i in page_issues):
                missing_count += 1
            else:
                issue_count += 1
            all_issues.extend(page_issues)
        else:
            clean_count += 1

    print(f"=== AR Audit Results ===")
    print(f"Pages: {len(pages)}")
    print(f"Clean: {clean_count}")
    print(f"Missing: {missing_count}")
    print(f"With issues: {issue_count}")
    print(f"Total issues: {len(all_issues)}")
    print()

    if all_issues:
        print("Issues:")
        for issue in all_issues[:100]:  # limit output
            print(f"  {issue}")
        if len(all_issues) > 100:
            print(f"  ... and {len(all_issues) - 100} more issues")

    return all_issues

if __name__ == '__main__':
    issues = main()
    sys.exit(0 if not issues else 1)
