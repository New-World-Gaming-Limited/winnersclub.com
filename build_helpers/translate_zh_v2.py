#!/usr/bin/env python3
"""
Translate EN pages to ZH (Simplified Chinese) for 1win.codes.
Uses pplx llm extract via subprocess.
Reads from en/ writes to zh/.
"""

import os
import re
import sys
import json
import time
import subprocess
import tempfile

BASE = '/home/user/workspace/1win-codes-repo'
EN_DIR = os.path.join(BASE, 'en')
ZH_DIR = os.path.join(BASE, 'zh')
INVENTORY_FILE = os.path.join(BASE, 'build_helpers', 'en_page_inventory.txt')

INSTRUCTION = """Translate only the visible text content from English to Simplified Chinese (zh-CN) for this 1win online casino affiliate HTML page.

RULES - follow all of them precisely:

1. TRANSLATE text in these tags: <title>, <meta name="description">, <meta property="og:title">, <meta property="og:description">, text between <h1>, <h2>, <h3>, <h4>, <p>, <li>, <span>, <a> tags (only link text, not href), <button> text, <td>, <th>, <label>, <dt>, <dd>.

2. NEVER translate/change:
   - "XLBONUS" - always uppercase exact
   - "1win" - keep as "1win"
   - "Curaçao 8048/JAZ" - exact string unchanged
   - All game names: Sweet Bonanza, Gates of Olympus, Aviator, JetX, Spaceman, Lucky Drive, Book of Dead, Reactoonz, Fire Joker, Starburst, etc.
   - Provider names: Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt, Relax Gaming
   - Payment brands: Visa, Mastercard, Bitcoin, Ethereum, USDT, Skrill, Neteller, UPI, PIX, etc.
   - All href values (URLs), src values, class names, id names, data-* values
   - Content inside <script> and <style> tags - copy EXACTLY as-is
   - JSON-LD content inside <script type="application/ld+json"> - translate only name/description/text fields but keep all @type, @id, url, etc. unchanged
   - HTML attributes: lang (except <html lang>, which becomes "zh"), hreflang values
   - Numbers: 600%, 200%, 150%, 100%, 50%, 11,000+, 12,000+, 400,000+, 30+, etc.
   - Sport league names (Premier League, La Liga, etc.)

3. CHANGE:
   - <html lang="en"> → <html lang="zh">
   - canonical href /en/... → /zh/...
   - Navigation hrefs /en/xxx → /zh/xxx (but NOT affiliate /link/... URLs)
   - Keep ALL hreflang alternate tags exactly as-is

4. NEVER use:
   - Em dash — or en dash – (use comma or period instead)
   - Chinese em dash ——
   - 数千 standalone (meaning "thousands of" - use the actual number like 11,000) - NOTE: 数千万 is OK
   - 数百 standalone (meaning "hundreds of" - use the actual number) - NOTE: 数百万 is OK
   - 世界级, 尖端, 下一代, 最先进

5. FIRST PARAGRAPH must mention: 1win + XLBONUS + a specific number + Curaçao 8048/JAZ

6. CTA translations:
   - Register / Sign Up → 立即注册
   - Claim → 领取
   - Open → 打开
   - Start → 开始
   - Play Now → 立即游戏
   - Access → 访问
   - Get → 获取

7. Key vocabulary:
   - casino → 在线赌场 or 娱乐城
   - sports betting → 体育博彩
   - bonus → 奖金
   - promo code → 促销代码
   - deposit → 存款
   - withdrawal → 提款
   - free spins → 免费旋转
   - slot → 老虎机

Return the COMPLETE HTML with Chinese translations applied. Do not truncate."""

OUTPUT_SCHEMA = json.dumps({
    "type": "object",
    "properties": {
        "translated_html": {
            "type": "string",
            "description": "The complete HTML page with text translated to Simplified Chinese (zh-CN)"
        }
    },
    "required": ["translated_html"]
})


def translate_with_pplx(html_content, rel_path):
    """Use pplx llm extract to translate HTML."""
    # Prepare input as JSONL
    input_obj = {"path": rel_path, "html": html_content}
    input_line = json.dumps(input_obj, ensure_ascii=False)
    
    result = subprocess.run(
        [
            'pplx', 'llm', 'extract',
            '--instruction', INSTRUCTION,
            '--output-schema', OUTPUT_SCHEMA,
            '--max-tokens', '32000'
        ],
        input=input_line,
        capture_output=True,
        text=True,
        env={**os.environ}
    )
    
    if result.returncode != 0:
        print(f"  PPLX ERROR: {result.stderr[:300]}")
        return None
    
    try:
        # Parse the JSONL output (may have leading warnings line)
        lines = [l for l in result.stdout.strip().split('\n') if l.strip()]
        for line in lines:
            parsed = json.loads(line)
            if 'results' in parsed:
                results = parsed['results']
                if results and results[0].get('result'):
                    return results[0]['result']['translated_html']
                elif results and results[0].get('error'):
                    print(f"  LLM ERROR: {results[0]['error']}")
                    return None
        print(f"  NO RESULT in output: {result.stdout[:200]}")
        return None
    except Exception as e:
        print(f"  PARSE ERROR: {e}")
        print(f"  stdout: {result.stdout[:300]}")
        return None


def post_process(html, rel_path):
    """Apply mechanical fixes after translation."""
    # Ensure lang="zh"
    html = re.sub(r'<html\s+lang="[^"]*"', '<html lang="zh"', html)
    
    # Fix canonical: /en/ -> /zh/
    html = re.sub(
        r'(<link\s+rel="canonical"\s+href="https://1win\.codes)/en/',
        r'\1/zh/',
        html
    )
    
    # Fix internal nav links /en/ -> /zh/
    # Save hreflang en href value first
    hreflang_en_match = re.search(
        r'<link\s+rel="alternate"\s+hreflang="en"\s+href="([^"]+)"', html
    )
    hreflang_en_url = hreflang_en_match.group(1) if hreflang_en_match else None
    
    # Replace /en/ with /zh/ in href attributes
    html = re.sub(r'href="/en/', 'href="/zh/', html)
    
    # Restore hreflang en href  
    if hreflang_en_url:
        html = re.sub(
            r'(<link\s+rel="alternate"\s+hreflang="en"\s+href=")[^"]*(")',
            f'\\g<1>{hreflang_en_url}\\g<2>',
            html
        )
    
    # Remove em/en dashes from anywhere in the text
    html = html.replace('——', ',').replace('—', ',').replace('–', '-')
    
    # Fix Curaçao 8048/JAZ: normalize common LLM variations to exact required string
    # Pattern: Curaçao + something + 8048/JAZ or Curacao + ...
    import re as _re
    # Replace "Curaçao 执照 (8048/JAZ)" -> "Curaçao 8048/JAZ"
    html = _re.sub(r'Cura[çc]ao\s+[^8]*?\(?8048/JAZ\)?', 'Curaçao 8048/JAZ', html)
    # Replace "Curacao 博彩许可证" -> "Curaçao 8048/JAZ" if no number follows
    html = _re.sub(r'Curacao\s+(?:博彩|赌博)?[执许]照(?:[，,。]|$)', 'Curaçao 8048/JAZ。', html)
    
    return html


def audit_file(zh_path, rel_path):
    """Audit a translated file for rule compliance."""
    issues = []
    
    if not os.path.exists(zh_path):
        return [f"FILE_MISSING"]
    
    with open(zh_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if len(content) < 500:
        return [f"FILE_TOO_SHORT ({len(content)} chars)"]
    
    if 'XLBONUS' not in content:
        issues.append("MISSING_XLBONUS")
    
    if 'Curaçao 8048/JAZ' not in content:
        issues.append("MISSING_CURACAO")
    
    em_count = content.count('—') + content.count('–')
    if em_count > 0:
        issues.append(f"HAS_DASHES({em_count})")
    
    if 'lang="zh"' not in content:
        issues.append("WRONG_LANG")
    
    canonical_match = re.search(r'rel="canonical"\s+href="([^"]+)"', content)
    if canonical_match:
        canon_url = canonical_match.group(1)
        if '/en/' in canon_url:
            issues.append(f"CANONICAL_EN({canon_url})")
    
    # Check banned phrases - 数百/数千 only banned as vague quantity ("hundreds of", "thousands of")
    # Allowed: 数百万 (millions), 数百搜 (many searches), 数百搭 (wild combos), 数千万 (tens of millions), 数千倍 (thousands times)
    # Banned: 数百名/数百个/数百种 数千名/数千个/数千种 (vague counts of things)
    if re.search(r'数百[名个种款分钟秒小时元美]', content):
        issues.append("BANNED(数百)")
    if re.search(r'数千[名个种款分钟秒小时元美]', content):
        issues.append("BANNED(数千)")
    banned_plain = ['世界级', '尖端', '下一代', '最先进']
    for b in banned_plain:
        if b in content:
            issues.append(f"BANNED({b})")
    
    # Check Chinese em dash
    if '——' in content:
        issues.append("CHINESE_EMDASH")
    
    # Validate JSON-LD
    json_ld_blocks = re.findall(
        r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>',
        content, re.DOTALL
    )
    for i, block in enumerate(json_ld_blocks):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as e:
            issues.append(f"INVALID_JSONLD({i+1}:{str(e)[:30]})")
    
    return issues


def load_inventory():
    with open(INVENTORY_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def translate_page(rel_path, force=False):
    """Translate a single page."""
    en_path = os.path.join(EN_DIR, rel_path)
    zh_path = os.path.join(ZH_DIR, rel_path)
    
    os.makedirs(os.path.dirname(zh_path), exist_ok=True)
    
    if not os.path.exists(en_path):
        print(f"  SKIP_MISSING_EN: {en_path}")
        return 'skip'
    
    if os.path.exists(zh_path) and not force:
        # Quick check if existing file is good
        issues = audit_file(zh_path, rel_path)
        if not issues:
            print(f"  SKIP_EXISTS_CLEAN: {rel_path}")
            return 'skip_clean'
        else:
            print(f"  RETRANSLATE (issues: {', '.join(issues)}): {rel_path}")
    
    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    print(f"  Translating ({len(en_content)} chars): {rel_path}")
    
    translated = translate_with_pplx(en_content, rel_path)
    
    if not translated:
        print(f"  FAILED: {rel_path}")
        return 'fail'
    
    # Clean markdown fences if present
    translated = translated.strip()
    if translated.startswith('```html'):
        translated = translated[7:]
    elif translated.startswith('```'):
        translated = translated[3:]
    if translated.endswith('```'):
        translated = translated[:-3]
    translated = translated.strip()
    
    translated = post_process(translated, rel_path)
    
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    # Verify
    issues = audit_file(zh_path, rel_path)
    if issues:
        print(f"  WRITTEN_WITH_ISSUES ({', '.join(issues)}): {rel_path}")
        return 'issues'
    else:
        print(f"  OK: {rel_path}")
        return 'ok'


def main():
    pages = load_inventory()
    
    if len(sys.argv) >= 2 and sys.argv[1] == 'audit':
        print("Running full audit...")
        all_issues = {}
        clean = 0
        for rel_path in pages:
            zh_path = os.path.join(ZH_DIR, rel_path)
            issues = audit_file(zh_path, rel_path)
            if issues:
                all_issues[rel_path] = issues
                print(f"  ISSUES {rel_path}: {', '.join(issues)}")
            else:
                clean += 1
        total = sum(len(v) for v in all_issues.values())
        print(f"\npages: {len(pages)}, issues: {total}, clean: {clean}")
        return all_issues
    
    # Parse range args
    start_idx = int(sys.argv[1]) if len(sys.argv) >= 2 else 0
    end_idx = int(sys.argv[2]) if len(sys.argv) >= 3 else len(pages)
    force = '--force' in sys.argv
    
    batch = pages[start_idx:end_idx]
    print(f"\nProcessing pages {start_idx+1}-{end_idx} ({len(batch)} pages)")
    
    results = {'ok': 0, 'issues': 0, 'fail': 0, 'skip': 0, 'skip_clean': 0}
    failed = []
    
    for i, rel_path in enumerate(batch):
        print(f"\n[{start_idx+i+1}/{len(pages)}] {rel_path}")
        status = translate_page(rel_path, force=force)
        results[status] = results.get(status, 0) + 1
        if status in ('fail', 'issues'):
            failed.append((rel_path, status))
        time.sleep(0.3)
    
    print(f"\n=== BATCH COMPLETE ===")
    print(f"Results: {results}")
    if failed:
        print(f"Problems: {failed}")
    
    return results


if __name__ == '__main__':
    main()
