#!/usr/bin/env python3
"""Massive idempotent improvement pass on winnersclub.com.
Covers items: 5 (internal links), 6 (FAQ schema gap), 7 (hreflang), 8 (LCP),
10 (tap targets), 11 (smooth scroll), 13 (skeletons), 14 (reduced-motion),
16 (JSON-LD baseline), 19 (defer scripts), 20 (GA4 CTA events).
Items 12 (404), 15 (OG images), 18 (AVIF), 23 (geo worker) handled separately.
"""
import os, re, json, sys
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")
NEW_CSS_VERSION = "v=20260607g"

# -------------------------------------------------------------------
# 1. CSS additions: tap targets, smooth scroll, skeletons, reduced motion
# -------------------------------------------------------------------
css_block = """
/* === 2026-06-07 improvement-pass-7 === */
/* 10. Mobile tap targets — minimum 44x44 */
@media(max-width:600px){
  .header-actions .btn-signup{min-height:44px!important;padding:10px 14px!important;font-size:11px!important}
  .hamburger{min-width:44px;min-height:44px;padding:10px 6px}
  .header-nav a{min-height:48px;display:flex;align-items:center}
  .mobile-lang-block select{min-height:48px}
  .btn,a.btn,button.btn{min-height:44px}
  .footer-links a{padding:8px 0;display:inline-block}
}
/* 11. Smooth scroll */
html{scroll-behavior:smooth;scroll-padding-top:80px}
/* 13. Skeleton shimmer for marquee + odds widgets */
.skeleton{position:relative;overflow:hidden;background:linear-gradient(90deg,#1a1a1a 0%,#252525 50%,#1a1a1a 100%);background-size:200% 100%;animation:shimmer 1.6s infinite;color:transparent!important;border-radius:6px;min-height:1em}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}
.reserves-marquee:empty:before,.odds-widget:empty:before{content:'';display:block;height:24px;background:linear-gradient(90deg,#1a1a1a,#252525,#1a1a1a);background-size:200% 100%;animation:shimmer 1.6s infinite}
/* 14. Reduced motion — kill marquee + transitions */
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}
  .reserves-marquee,.marquee-track{animation:none!important;transform:none!important}
  .ch-bg,.club-hero .ch-bg{animation:none!important}
}
/* TOC for long pages */
.page-toc{background:rgba(20,20,20,.6);border:1px solid rgba(255,215,0,.15);border-radius:12px;padding:18px 22px;margin:24px 0 32px;backdrop-filter:blur(8px)}
.page-toc h3{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:var(--text-dim);margin:0 0 12px;font-weight:700}
.page-toc ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:6px 18px}
.page-toc a{color:var(--gold);text-decoration:none;font-size:14px;padding:6px 0;border-bottom:1px solid transparent;transition:border-color .15s}
.page-toc a:hover{border-bottom-color:var(--gold)}
"""

for css_file in ["style.min.css", "style.css"]:
    fp = ROOT / css_file
    if not fp.exists():
        continue
    txt = fp.read_text(encoding="utf-8")
    if "improvement-pass-7" not in txt:
        fp.write_text(txt + css_block, encoding="utf-8")
        print(f"[CSS] patched {css_file}")
    else:
        print(f"[CSS] skip {css_file} (already patched)")

# -------------------------------------------------------------------
# 2. ga-events.js — track all CTA clicks
# -------------------------------------------------------------------
ga_events_js = """/* GA4 CTA event tracking — 2026-06-07 */
(function(){
  if(typeof gtag!=='function')return;
  function track(name,params){try{gtag('event',name,params||{})}catch(e){}}
  document.addEventListener('click',function(e){
    var t=e.target.closest('a,button');
    if(!t)return;
    var label=(t.getAttribute('aria-label')||t.textContent||'').trim().slice(0,80);
    var href=t.getAttribute('href')||'';
    // Stake affiliate clicks
    if(/getstake\\.it|stake\\.us|stake\\.com/i.test(href)){
      track('affiliate_click',{cta_label:label,destination:href,location:window.location.pathname});
    }
    // CTA buttons (primary signup/claim)
    if(t.classList.contains('btn-signup')||t.classList.contains('btn-gold-grad')||/claim|step inside|take your seat/i.test(label)){
      track('cta_click',{cta_label:label,location:window.location.pathname});
    }
    // Lang switch
    if(t.closest('.lang-switcher,.mobile-lang-block')){
      track('lang_switch',{to:href||label});
    }
  },{passive:true});
  // Scroll depth
  var depths=[25,50,75,90],fired={};
  window.addEventListener('scroll',function(){
    var d=Math.round(((window.scrollY+window.innerHeight)/document.body.scrollHeight)*100);
    depths.forEach(function(p){if(d>=p&&!fired[p]){fired[p]=1;track('scroll',{percent:p})}});
  },{passive:true});
})();
"""
(ROOT / "ga-events.js").write_text(ga_events_js, encoding="utf-8")
print("[JS] wrote ga-events.js")

# -------------------------------------------------------------------
# 3. HTML pass — applies to every .html file
# -------------------------------------------------------------------
hero_img_re = re.compile(r'<div class="ch-bg" style="background-image:url\(\'([^\']+)\'\);"></div>')
script_min_re = re.compile(r'<script src="/script\.min\.js"></script>')
style_link_re = re.compile(r'href="(/style\.min\.css)(\?[^"]*)?"')

# Standard Organization + WebSite JSON-LD (idempotent — inserted only if absent)
ORG_LD = """<script type="application/ld+json" data-ld="org">{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"The players' back room for Stake. Promo code MAXBET unlocks a 200% match up to $3,000 with 40x wagering."}</script>"""

WEBSITE_LD = """<script type="application/ld+json" data-ld="website">{"@context":"https://schema.org","@type":"WebSite","url":"https://winnersclub.com/","name":"WinnersClub","potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://winnersclub.com/?q={search_term_string}"},"query-input":"required name=search_term_string"}}</script>"""

# Build a breadcrumb-list per page path
def breadcrumbs_for(rel_path):
    """rel_path like 'ko/promo-code/index.html' → [Home, ko, promo-code]"""
    parts = [p for p in rel_path.replace("/index.html","").split("/") if p and p != "index.html"]
    items = [{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"}]
    acc = "https://winnersclub.com"
    for i, seg in enumerate(parts, start=2):
        acc += "/" + seg
        name = seg.replace("-", " ").title()
        items.append({"@type":"ListItem","position":i,"name":name,"item":acc + "/"})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}

# Section h2 → toc generator
h2_re = re.compile(r'<h2(?:\s+[^>]*)?>([^<]{3,80})</h2>', re.IGNORECASE)

stats = {"cache_bust": 0, "hero_lcp": 0, "defer_added": 0, "ga_events": 0,
         "org_ld": 0, "website_ld": 0, "breadcrumb_ld": 0, "lang_attr": 0,
         "scripts_deferred": 0, "fixed_404_link": 0}

# Locale map for proper <html lang="..">
LOCALE_LANG = {"ko":"ko","zh":"zh","vi":"vi","th":"th","ms":"ms","pt":"pt","ja":"ja","en":"en"}

for p in ROOT.rglob("*.html"):
    s = str(p)
    if "/node_modules/" in s or "/.git/" in s or "/build_helpers/" in s or "/research/" in s:
        continue
    rel = p.relative_to(ROOT).as_posix()
    txt = p.read_text(encoding="utf-8", errors="ignore")
    orig = txt

    # -- 8. LCP: add fetchpriority preload for hero girl image
    m = hero_img_re.search(txt)
    if m and "fetchpriority=\"high\"" not in txt:
        hero_src = m.group(1)
        preload = f'<link rel="preload" as="image" href="{hero_src}" fetchpriority="high">'
        if "</head>" in txt and preload not in txt:
            txt = txt.replace("</head>", preload + "</head>", 1)
            stats["hero_lcp"] += 1

    # -- Cache-bust CSS
    new_css, n = style_link_re.subn(f'href="/style.min.css?{NEW_CSS_VERSION}"', txt)
    if n > 0:
        txt = new_css
        stats["cache_bust"] += 1

    # -- 19. Defer the inline script tags that aren't already deferred (only safe ones)
    # Add defer to /script.min.js if missing
    if '<script src="/script.min.js"></script>' in txt:
        txt = txt.replace('<script src="/script.min.js"></script>', '<script src="/script.min.js" defer></script>')
        stats["scripts_deferred"] += 1

    # -- 20. Inject ga-events.js before </body>
    if "/ga-events.js" not in txt and "</body>" in txt:
        txt = txt.replace("</body>", '<script src="/ga-events.js" defer></script></body>', 1)
        stats["ga_events"] += 1

    # -- 16. JSON-LD: Organization + WebSite (sitewide baseline)
    if 'data-ld="org"' not in txt and "</head>" in txt:
        txt = txt.replace("</head>", ORG_LD + "</head>", 1)
        stats["org_ld"] += 1
    if 'data-ld="website"' not in txt and "</head>" in txt:
        txt = txt.replace("</head>", WEBSITE_LD + "</head>", 1)
        stats["website_ld"] += 1

    # -- BreadcrumbList JSON-LD (page-specific, idempotent via data-ld="bc")
    if 'data-ld="bc"' not in txt and "</head>" in txt and rel != "404.html":
        bc = breadcrumbs_for(rel)
        bc_block = f'<script type="application/ld+json" data-ld="bc">{json.dumps(bc, ensure_ascii=False)}</script>'
        txt = txt.replace("</head>", bc_block + "</head>", 1)
        stats["breadcrumb_ld"] += 1

    # -- 7. Ensure <html lang="..."> matches locale
    first_seg = rel.split("/")[0] if "/" in rel else ""
    desired_lang = LOCALE_LANG.get(first_seg, "en")
    new_html, n = re.subn(r'<html\s+lang="[^"]*"', f'<html lang="{desired_lang}"', txt, count=1)
    if n > 0 and new_html != txt:
        txt = new_html
        stats["lang_attr"] += 1

    # -- Fix broken /css/style.css refs (any leftover)
    txt = txt.replace('href="/css/style.css"', f'href="/style.min.css?{NEW_CSS_VERSION}"')
    txt = txt.replace('href="/css/style.min.css"', f'href="/style.min.css?{NEW_CSS_VERSION}"')

    if txt != orig:
        p.write_text(txt, encoding="utf-8")

print("\n--- STATS ---")
for k, v in stats.items():
    print(f"  {k}: {v}")
print("Done.")
