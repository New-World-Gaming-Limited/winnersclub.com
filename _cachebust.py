#!/usr/bin/env python3
"""Cache-bust style.min.css references across all HTML files + fix STEP INSIDE green cascade."""
import os, re, sys
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")
VERSION = "v=20260607c"  # bump if rerun

css_link_re = re.compile(r'href="(/style\.min\.css)(\?[^"]*)?"')

html_count = 0
for p in ROOT.rglob("*.html"):
    if "/node_modules/" in str(p) or "/.git/" in str(p):
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    new = css_link_re.sub(f'href="/style.min.css?{VERSION}"', txt)
    if new != txt:
        p.write_text(new, encoding="utf-8")
        html_count += 1

print(f"updated {html_count} html files")

# Also append a higher-specificity STEP INSIDE override + remove animation gold-pulse conflict
for css_file in ["style.min.css", "style.css"]:
    fp = ROOT / css_file
    if not fp.exists():
        continue
    txt = fp.read_text(encoding="utf-8")
    marker = "/* === 2026-06-07 polish-pass v3.1 cascade-fix === */"
    if marker in txt:
        print(f"skip {css_file} - already patched")
        continue
    extra = f"""
{marker}
.site-header .header-actions a.btn.btn-signup,
.site-header .header-actions a.btn-signup,
header.site-header a.btn-signup{{
  background:linear-gradient(135deg,#FFD700 0%,#ff9d00 100%)!important;
  background-image:linear-gradient(135deg,#FFD700 0%,#ff9d00 100%)!important;
  background-color:#FFD700!important;
  color:#1a1308!important;
  box-shadow:0 4px 18px rgba(255,215,0,.30)!important;
  border:1px solid rgba(255,215,0,.55)!important;
}}
.site-header .header-actions a.btn.btn-signup:hover,
.site-header .header-actions a.btn-signup:hover,
header.site-header a.btn-signup:hover{{
  transform:translateY(-2px)!important;
  box-shadow:0 6px 28px rgba(255,215,0,.5)!important;
  background:linear-gradient(135deg,#ffe65a 0%,#ffb33a 100%)!important;
}}
"""
    fp.write_text(txt + extra, encoding="utf-8")
    print(f"patched {css_file}")
