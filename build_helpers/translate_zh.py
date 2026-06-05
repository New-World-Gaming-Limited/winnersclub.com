#!/usr/bin/env python3
"""
Translate EN pages to ZH (Simplified Chinese) for 1win.codes.
Reads from en/ writes to zh/.
"""

import os
import re
import sys
import json
import time
import subprocess

BASE = '/home/user/workspace/1win-codes-repo'
EN_DIR = os.path.join(BASE, 'en')
ZH_DIR = os.path.join(BASE, 'zh')

INVENTORY_FILE = os.path.join(BASE, 'build_helpers', 'en_page_inventory.txt')

SYSTEM_PROMPT = """You are a professional translator converting English HTML pages to Simplified Chinese (zh-CN) for a gambling affiliate website about 1win online casino.

CRITICAL RULES - follow every one:

1. PRESERVE VERBATIM (never translate these):
   - "XLBONUS" - always uppercase, never change
   - "1win" - always as "1win"  
   - "Curaçao 8048/JAZ" - exact string, never change
   - All game names: Sweet Bonanza, Gates of Olympus, Aviator, JetX, Spaceman, Lucky Drive, Book of Dead, etc.
   - All provider names: Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt, Relax Gaming
   - All payment brand names: Visa, Mastercard, Bitcoin, Ethereum, USDT, Skrill, Neteller, PIX, UPI, etc.
   - All URLs, /link/... paths, affiliate links
   - All HTML attributes: class, id, data-*, hreflang, canonical href values
   - All <script> and <style> tag contents - copy them exactly as-is
   - JSON-LD @type and @id values
   - Google Analytics code (G-S2MXR8D3HS)
   - All numbers stay Arabic: 600%, 200%, 150%, 100%, 50%, 30+, 11,000+, 12,000+, 40,000+, 400,000+
   - Sport league names in English (Premier League, La Liga, etc.)

2. LANGUAGE CHANGES:
   - Change <html lang="en"> to <html lang="zh">
   - Change canonical URL from /en/... to /zh/...
   - Keep ALL other hreflang alternate tags exactly as-is (they list all locales)

3. NAVIGATION LINKS: Change /en/ to /zh/ in ALL href attributes within the page navigation and internal links. But leave /link/... affiliate URLs unchanged.

4. NEVER USE:
   - Em dash (—) or en dash (–) - use comma, period, or rephrase instead
   - Chinese em dash (——) 
   - "数千", "数百" (use the actual numbers from source)
   - "世界级", "尖端", "下一代", "最先进"
   - "no strings attached" equivalent
   - "thousands of" equivalent - use the specific number

5. FIRST PARAGRAPH must contain: "1win" + "XLBONUS" + a specific number + "Curaçao 8048/JAZ" (or "库拉索8048/JAZ牌照")

6. CTA buttons - use these Chinese translations:
   - Register → 立即注册
   - Claim / Get → 领取
   - Open → 打开
   - Start → 开始
   - Play / Play Now → 立即游戏
   - Access → 访问
   - Sign Up → 立即注册

7. KEY VOCABULARY:
   - casino → 在线赌场 or 娱乐城
   - sports betting → 体育博彩
   - bonus → 奖金
   - promo code → 促销代码
   - deposit → 存款
   - withdrawal → 提款
   - welcome bonus → 欢迎奖金
   - free spins → 免费旋转
   - jackpot → 累积奖池
   - slot → 老虎机
   - live dealer → 真人荷官
   - cryptocurrency → 加密货币

8. OUTPUT: Return the COMPLETE translated HTML file. Do NOT truncate or summarize. Do NOT add any explanation before or after the HTML. Just output the full HTML.

9. JSON-LD: Translate the "name" and "description" fields in JSON-LD, but preserve @context, @type, @id, url, and all structural properties verbatim.

10. Meta tags: Translate title, description, og:title, og:description into Chinese.

11. For news/article pages: Keep article dates, times, and structured data intact.

The target reader is a Simplified Chinese (mainland China) speaker interested in online gambling."""


def call_perplexity(content, page_path):
    """Call Perplexity API to translate content."""
    prompt = f"""Translate the following HTML page from English to Simplified Chinese (zh-CN).
Page: {page_path}

{content}"""
    
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 16000,
        "temperature": 0.1
    }
    
    result = subprocess.run(
        ['pplx-tool', 'chat_completions'],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env={**os.environ}
    )
    
    if result.returncode != 0:
        print(f"  ERROR calling API: {result.stderr[:200]}")
        return None
    
    try:
        resp = json.loads(result.stdout)
        return resp['choices'][0]['message']['content']
    except Exception as e:
        print(f"  ERROR parsing response: {e}")
        print(f"  stdout: {result.stdout[:300]}")
        return None


def post_process(html, page_path):
    """Apply mechanical fixes after translation."""
    # Ensure lang="zh"
    html = re.sub(r'<html\s+lang="[^"]*"', '<html lang="zh"', html)
    
    # Fix canonical: /en/ -> /zh/
    html = re.sub(
        r'(<link\s+rel="canonical"\s+href="https://1win\.codes)/en/',
        r'\1/zh/',
        html
    )
    
    # Fix internal navigation links /en/ -> /zh/ (but not in hreflang alternates which point to other locales)
    # Only fix links that point to /en/ in href attributes (nav links, buttons)
    # We need to be careful not to change hreflang="en" href which should stay
    # The hreflang for en points to /en/ and MUST stay
    # But nav links /en/xxx should become /zh/xxx
    
    # Fix nav links and internal page links
    def fix_en_link(m):
        attr = m.group(0)
        # Don't fix hreflang alternate links (they reference other locales correctly)
        return attr
    
    # Fix href="/en/..." in anchor tags that are NOT part of hreflang
    # Strategy: fix href="/en/ to href="/zh/ globally, then restore hreflang en href
    
    # Save hreflang en href
    hreflang_en = re.search(r'<link\s+rel="alternate"\s+hreflang="en"\s+href="([^"]+)"', html)
    
    # Replace /en/ with /zh/ in href attributes
    html = re.sub(r'href="/en/', 'href="/zh/', html)
    
    # Restore hreflang en
    if hreflang_en:
        en_url = hreflang_en.group(1)
        # The hreflang en line now has /zh/ instead of /en/, fix it back
        html = re.sub(
            r'(<link\s+rel="alternate"\s+hreflang="en"\s+href=")[^"]*(")',
            f'\\g<1>{en_url}\\g<2>',
            html
        )
    
    # Remove any em dashes or en dashes from text content
    # Replace em dash in text
    html = html.replace('——', ',').replace('—', ',').replace('–', '-')
    
    # Ensure XLBONUS is present (sanity check - if missing, something went wrong)
    if 'XLBONUS' not in html:
        print(f"  WARNING: XLBONUS not found in translated output for {page_path}")
    
    return html


def translate_page(rel_path):
    """Translate a single page."""
    en_path = os.path.join(EN_DIR, rel_path)
    zh_path = os.path.join(ZH_DIR, rel_path)
    
    # Create directory if needed
    zh_dir = os.path.dirname(zh_path)
    os.makedirs(zh_dir, exist_ok=True)
    
    if not os.path.exists(en_path):
        print(f"  SKIP (not found): {en_path}")
        return False
    
    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    print(f"  Translating {rel_path} ({len(en_content)} chars)...")
    
    translated = call_perplexity(en_content, rel_path)
    
    if not translated:
        print(f"  FAILED: {rel_path}")
        return False
    
    # Clean up - sometimes the API adds markdown code fences
    translated = translated.strip()
    if translated.startswith('```html'):
        translated = translated[7:]
    elif translated.startswith('```'):
        translated = translated[3:]
    if translated.endswith('```'):
        translated = translated[:-3]
    translated = translated.strip()
    
    # Post-process
    translated = post_process(translated, rel_path)
    
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f"  OK: {rel_path}")
    return True


def load_inventory():
    with open(INVENTORY_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def audit_file(zh_path, rel_path):
    """Audit a single translated file for rule compliance."""
    issues = []
    
    if not os.path.exists(zh_path):
        return [f"MISSING: {rel_path}"]
    
    with open(zh_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'XLBONUS' not in content:
        issues.append("missing XLBONUS")
    
    if 'Curaçao 8048/JAZ' not in content:
        issues.append("missing Curaçao 8048/JAZ")
    
    em_count = content.count('—') + content.count('–')
    if em_count > 0:
        issues.append(f"has {em_count} em/en dashes")
    
    if 'lang="zh"' not in content and "lang='zh'" not in content:
        issues.append("wrong lang attribute")
    
    # Check canonical
    canonical_match = re.search(r'rel="canonical"\s+href="([^"]+)"', content)
    if canonical_match:
        canon_url = canonical_match.group(1)
        if '/en/' in canon_url:
            issues.append(f"canonical still has /en/: {canon_url}")
    
    # Check for banned phrases
    banned = ['数千', '数百', '世界级', '尖端', '下一代', '最先进', '——']
    for b in banned:
        if b in content:
            issues.append(f"banned phrase: {b}")
    
    # Validate JSON-LD
    json_ld_blocks = re.findall(r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>', content, re.DOTALL)
    for i, block in enumerate(json_ld_blocks):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            issues.append(f"invalid JSON-LD block {i+1}: {e}")
    
    return issues


def main():
    pages = load_inventory()
    
    # Check command line args for range
    start_idx = 0
    end_idx = len(pages)
    
    if len(sys.argv) >= 3:
        start_idx = int(sys.argv[1])
        end_idx = int(sys.argv[2])
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'audit':
            # Audit mode
            print("Running audit on all zh/ files...")
            total_issues = 0
            clean = 0
            for rel_path in pages:
                zh_path = os.path.join(ZH_DIR, rel_path)
                issues = audit_file(zh_path, rel_path)
                if issues:
                    print(f"  ISSUES {rel_path}: {', '.join(issues)}")
                    total_issues += len(issues)
                else:
                    clean += 1
            print(f"\nAudit: pages={len(pages)}, clean={clean}, total_issues={total_issues}")
            return
    
    batch = pages[start_idx:end_idx]
    print(f"Translating pages {start_idx+1}-{end_idx} of {len(pages)} total")
    
    success = 0
    failed = []
    
    for i, rel_path in enumerate(batch):
        print(f"\n[{start_idx+i+1}/{len(pages)}] {rel_path}")
        ok = translate_page(rel_path)
        if ok:
            success += 1
        else:
            failed.append(rel_path)
        
        # Small delay to avoid rate limiting
        time.sleep(0.5)
    
    print(f"\n=== BATCH DONE: {success}/{len(batch)} succeeded ===")
    if failed:
        print(f"Failed: {failed}")


if __name__ == '__main__':
    main()
