#!/usr/bin/env python3
"""Migrate legacy Thai inner pages onto the unified shell.

For each Thai inner page that still uses the legacy <nav>...</nav>:
1. Replace the <nav> block with the unified <header class="site-header"> block
2. Ensure the unified stylesheet is linked in <head>
3. Remove duplicate inline CSS for nav (optional - leave for now to avoid breaking)
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# The unified header block, exactly as seen in th/index.html (path-agnostic since lang-switcher uses absolute URLs)
UNIFIED_HEADER = '''  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/th/" class="header-logo" aria-label="WinnersClub home">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        <a href="/th/casino/" class="nav-link">คาสิโน</a>
        <a href="/th/sports/" class="nav-link">สปอร์ต</a>
        <a href="/th/poker/" class="nav-link">โป๊กเกอร์</a>
        <a href="/th/aviator/" class="nav-link">เอเวียเตอร์</a>
        <a href="/th/promo-code/" class="nav-link">โปรโมโค้ด</a>
        <a href="/th/reserves/" class="nav-link">ทุนสำรอง</a>
        <a href="/th/about-stake/" class="nav-link">เกี่ยวกับ</a>
      <div class="mobile-lang-block"><label>ภาษา</label><select onchange="if(this.value)window.location.href=this.value" aria-label="ภาษา"><option value="">English</option><option value="/ko/">한국어 (Korean)</option><option value="/zh/">中文 (Chinese)</option><option value="/vi/">Tiếng Việt (Vietnamese)</option><option value="/th/">ไทย (Thai)</option><option value="/ms/">Bahasa Melayu (Malay)</option><option value="/pt/">Português (Portuguese)</option><option value="/ja/">日本語 (Japanese)</option><option value="/es/">Español (Spanish)</option><option value="/pt-br/">Português do Brasil (Portuguese - Brazil)</option><option value="/tr/">Türkçe (Turkish)</option><option value="/id/">Bahasa Indonesia (Indonesian)</option><option value="/fr/">Français (French)</option><option value="/ru/">Русский (Russian)</option><option value="/hi/">हिन्दी (Hindi)</option></select></div></nav>
      <div class="header-actions"><select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="ภาษา"><option value="https://winnersclub.com/">English</option><option value="https://winnersclub.com/ko/">한국어</option><option value="https://winnersclub.com/zh/">中文</option><option value="https://winnersclub.com/vi/">Tiếng Việt</option><option value="https://winnersclub.com/th/">ไทย</option><option value="https://winnersclub.com/ms/">Bahasa Melayu</option><option value="https://winnersclub.com/pt/">Português</option><option value="https://winnersclub.com/ja/">日本語</option><option value="https://winnersclub.com/es/">Español</option><option value="https://winnersclub.com/pt-br/">Português (BR)</option><option value="https://winnersclub.com/tr/">Türkçe</option><option value="https://winnersclub.com/id/">Bahasa Indonesia</option><option value="https://winnersclub.com/fr/">Français</option><option value="https://winnersclub.com/ru/">Русский</option><option value="https://winnersclub.com/hi/">हिन्दी</option></select>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup" aria-label="เข้ามาเลย">เข้ามาเลย</a>
        <button class="hamburger" id="hamburger" aria-label="เปิด/ปิดเมนู"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
'''

LEGACY_PAGES = [
    'about-stake', 'aviator', 'live-casino', 'live-odds', 'mirror', 'news',
    'originals', 'payments', 'poker', 'reserves', 'responsible-gambling',
    'slots', 'sports', 'stake-engine', 'stake-us-bonus', 'vip',
]

LEGACY_NAV_RE = re.compile(r'<nav>\s*\n?(?:.*?\n)*?</nav>', re.S)
HEAD_CLOSE_RE = re.compile(r'(\s*</head>)', re.I)
STYLESHEET_RE = re.compile(r'<link rel="stylesheet" href="/style\.min\.css', re.I)

def process(path):
    s = open(path, encoding='utf-8').read()
    if 'class="site-header"' in s:
        return False, 'already unified'

    orig = s

    # 1. Inject unified stylesheet into <head> if not present
    if not STYLESHEET_RE.search(s):
        s = HEAD_CLOSE_RE.sub(r'  <link rel="stylesheet" href="/style.min.css?v=20260616d">\1', s, count=1)

    # 2. Replace legacy <nav>...</nav> with unified <header>
    m = LEGACY_NAV_RE.search(s)
    if m:
        s = s[:m.start()] + UNIFIED_HEADER + s[m.end():]
    else:
        return False, 'no legacy <nav> found'

    if s != orig:
        open(path, 'w', encoding='utf-8').write(s)
        return True, 'ok'
    return False, 'no change'

def main():
    updated = 0
    for page in LEGACY_PAGES:
        p = os.path.join(ROOT, 'th', page, 'index.html')
        if not os.path.exists(p):
            print(f"  skip (missing): {p}")
            continue
        ok, msg = process(p)
        if ok:
            updated += 1
            print(f"  updated: th/{page}/")
        else:
            print(f"  skipped: th/{page}/ ({msg})")
    print(f"Total: {updated}")

if __name__ == '__main__':
    main()
