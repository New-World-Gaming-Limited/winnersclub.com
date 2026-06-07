#!/usr/bin/env python3
"""Fix mobile header: hide desktop lang-switcher on mobile + clone into mobile nav."""
from pathlib import Path
import re

ROOT = Path("/home/user/workspace/winnersclub.com")

# 1. Append CSS to hide .lang-switcher on mobile and style mobile-nav lang block
for css_file in ["style.min.css", "style.css"]:
    fp = ROOT / css_file
    if not fp.exists(): continue
    txt = fp.read_text(encoding="utf-8")
    marker = "/* === 2026-06-07 lang-mobile-fix === */"
    if marker in txt: continue
    extra = f"""
{marker}
@media(max-width:900px){{
  .header-actions .lang-switcher{{display:none!important}}
  .header-actions{{gap:8px}}
  .header-actions .btn-signup{{padding:8px 14px;font-size:12px}}
}}
.mobile-lang-block{{display:none;padding:14px 16px 6px;border-top:1px solid var(--border);margin-top:8px}}
.mobile-lang-block label{{display:block;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--text-dim);margin-bottom:8px}}
.mobile-lang-block select{{width:100%;background:var(--surface);color:var(--white);border:1px solid var(--border);border-radius:8px;padding:12px 14px;font-size:15px;font-weight:600;appearance:none;-webkit-appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23FFD700' stroke-width='2'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center}}
@media(max-width:768px){{.mobile-lang-block{{display:block}}}}
"""
    fp.write_text(txt + extra, encoding="utf-8")
    print(f"patched {css_file}")

# 2. Inject mobile-lang-block into every header-nav across all html files
mobile_lang_html = '''<div class="mobile-lang-block"><label>Language</label><select onchange="if(this.value)window.location.href=this.value" aria-label="Language"><option value="">English</option><option value="/ko/">한국어 (Korean)</option><option value="/zh/">中文 (Chinese)</option><option value="/vi/">Tiếng Việt (Vietnamese)</option><option value="/th/">ไทย (Thai)</option><option value="/ms/">Bahasa Melayu (Malay)</option><option value="/pt/">Português (Portuguese)</option><option value="/ja/">日本語 (Japanese)</option></select></div>'''

nav_close_re = re.compile(r'(<nav class="header-nav"[^>]*>.*?)</nav>', re.DOTALL)
count = 0
for p in ROOT.rglob("*.html"):
    if "/node_modules/" in str(p) or "/.git/" in str(p): continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    if "mobile-lang-block" in txt:
        continue
    m = nav_close_re.search(txt)
    if not m:
        continue
    new = txt[:m.end(1)] + mobile_lang_html + txt[m.end(1):]
    p.write_text(new, encoding="utf-8")
    count += 1

print(f"injected mobile-lang-block into {count} html files")
