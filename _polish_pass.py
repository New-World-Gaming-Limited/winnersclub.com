#!/usr/bin/env python3
"""
2026-06-07 polish pass — fix the 18-item punch-list.
Idempotent: safe to re-run.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent

# -----------------------------------------------------------------------------
# 1. Source comments: scrub "1WIN FAN SITE" header from style.css / script.js
# -----------------------------------------------------------------------------
for fn, label in [("style.css", "WINNERSCLUB — DARK VEGAS-CONCIERGE AESTHETIC"),
                  ("script.js", "WINNERSCLUB — JAVASCRIPT")]:
    p = ROOT / fn
    if p.exists():
        s = p.read_text()
        s = s.replace("1WIN FAN SITE — DARK PREMIUM GAMBLING AESTHETIC", label)
        s = s.replace("1WIN FAN SITE — JAVASCRIPT", label)
        p.write_text(s)

# -----------------------------------------------------------------------------
# 2. Replace Stake-branded SVG in footer with WinnersClub shield mark.
#    Across all 152 HTML files (8 locales × 19 pages).
# -----------------------------------------------------------------------------
WC_SHIELD = '''<svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub">
  <path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/>
  <path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text>
</svg>'''

# Pattern matches the entire <svg ... aria-label="Stake"> ... </svg> block
STAKE_SVG_RE = re.compile(
    r'<svg[^>]*aria-label="Stake"[^>]*>.*?</svg>',
    re.DOTALL
)

# -----------------------------------------------------------------------------
# 3. Drop sticky-bar bottom-padding into <main> via body class + adjust H1
#    line-break safety on mobile. We do this by appending a CSS v3 hot-fix
#    block to style.min.css and style.css.
# -----------------------------------------------------------------------------
V3_CSS = """
/* === 2026-06-07 polish-pass v3 — 18-item punch-list ==================== */

/* (1) Mobile H1 — guarantee subtitle blocks below MAXBET, never inline */
@media(max-width:760px){
  .ch-title{font-size:38px!important;line-height:1.08!important;letter-spacing:-1px!important;word-break:break-word}
  .ch-title .h1-sub{display:block!important;margin-top:14px!important;font-size:18px!important;font-style:italic;color:var(--text-dim);-webkit-text-fill-color:var(--text-dim);font-weight:400;letter-spacing:0;text-transform:lowercase;opacity:.9}
}

/* (2) STEP INSIDE button — gold gradient instead of green grass */
.header-actions .btn-signup,
.btn-signup:not(.btn-gold-grad){
  background:linear-gradient(135deg,#FFD700 0%,#ff9d00 100%)!important;
  color:#1a1308!important;
  font-weight:800!important;
  text-shadow:none!important;
  box-shadow:0 4px 14px rgba(255,215,0,.28)!important;
}
.header-actions .btn-signup:hover,
.btn-signup:not(.btn-gold-grad):hover{
  transform:translateY(-2px) scale(1.02)!important;
  box-shadow:0 0 32px rgba(255,215,0,.5)!important;
}

/* (3) Hero subtitles — pull out of background overlay, add shadow */
.ch-sub,.page-hero-sub,.hero-subtitle{
  text-shadow:0 2px 12px rgba(0,0,0,.85),0 0 24px rgba(0,0,0,.6);
}
.ch-sub.text-gradient-gold,.page-hero-sub.text-gradient-gold{
  color:#e8e8e8!important;
  -webkit-text-fill-color:#e8e8e8!important;
  background:none!important;
}
/* Lift overlay darkness another notch on hero so gold subhead reads */
.club-hero .ch-overlay,
.page-hero .hero-overlay{
  background:linear-gradient(180deg,rgba(20,20,21,.55) 0,rgba(20,20,21,.7) 55%,rgba(20,20,21,.95) 100%)!important;
}

/* (4) Hero portrait focal point — keep face in frame */
.club-hero .ch-bg,
.page-hero .hero-bg,
.page-hero-bg,
.hero-bg{background-position:center 28%!important}
@media(max-width:760px){
  .club-hero .ch-bg,.page-hero .hero-bg,.page-hero-bg,.hero-bg{background-position:center 18%!important}
}

/* (5) About page — center the 2-card row so it doesn't look abandoned */
.about-cards,.entity-cards,.icon-card-grid.cols-2{
  max-width:760px;margin-left:auto;margin-right:auto;
}

/* (6) Sticky CTA — give main padding so last lines aren't covered */
body{padding-bottom:90px}
@media(max-width:768px){body{padding-bottom:140px}}
.sticky-cta{border-top:1px solid rgba(255,215,0,.28)!important}
.sticky-cta::before{
  background:linear-gradient(90deg,transparent,rgba(255,215,0,.4),rgba(255,215,0,.7),rgba(255,215,0,.4),transparent)!important;
  height:1px!important;
}

/* (7) Marquee — make it animate on mobile, no clip */
.reserves-marquee,.marquee,.ticker{
  overflow:hidden;white-space:nowrap;position:relative;
}
.reserves-marquee>*,.marquee>*,.ticker>*{
  display:inline-block;padding-left:100%;animation:wc-marquee 38s linear infinite;
}
@keyframes wc-marquee{
  0%{transform:translateX(0)}
  100%{transform:translateX(-100%)}
}

/* (8) Section header variety — alternate underline treatments */
.section-divider{
  height:2px;width:80px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  margin:0 auto;display:block;
}
.section-header:nth-of-type(odd) .section-divider{
  background:linear-gradient(90deg,transparent,#8b0a1a,var(--gold),#8b0a1a,transparent);
}

/* (9) Card hover — premium gold glow on all card grids */
.feature-card,.casino-card,.icon-card,.poker-feature-card,
.aviator-feature,.tournament-card,.action-card,.bonus-code-card,
.payment-info-card,.tip-card,.risk-card,.step-card{
  transition:transform .35s var(--ease),border-color .35s var(--ease),box-shadow .35s var(--ease)!important;
}
.feature-card:hover,.casino-card:hover,.icon-card:hover,.poker-feature-card:hover,
.aviator-feature:hover,.tournament-card:hover,.action-card:hover,.bonus-code-card:hover,
.payment-info-card:hover,.tip-card:hover,.risk-card:hover,.step-card:hover{
  transform:translateY(-3px)!important;
  border-color:rgba(255,215,0,.45)!important;
  box-shadow:0 0 0 1px rgba(255,215,0,.18),0 14px 36px rgba(0,0,0,.45),0 0 28px rgba(255,215,0,.08)!important;
}

/* (10) Footer brand mark already swapped via Python — give it room */
.footer-brand svg{margin-bottom:16px;max-width:200px;height:auto}

/* (11) Lang switcher — settle the desktop dead space.
       Pull the switcher closer to STEP INSIDE button. */
@media(min-width:1101px){
  .header-actions{gap:14px}
  .lang-switcher{min-width:72px;max-width:96px}
}

/* (12) Typography hierarchy — H2 serif accent + gold underline */
h2:not(.section-title):not(.cta-banner-title):not(.hero-title):not(.ch-title):not(.page-hero-title),
.content-title,
section.section h2{
  font-family:'Playfair Display',Georgia,serif;
  font-weight:700;
  font-style:normal;
  letter-spacing:-.3px;
}
.feature-card h3,.casino-card h3,.icon-card h3,.poker-feature-card h3,
.aviator-feature h3,.action-card h3,.step-card h3{
  font-family:'Playfair Display',Georgia,serif;
  font-weight:700;
  font-size:20px;
  letter-spacing:-.2px;
  position:relative;
  padding-bottom:10px;
  margin-bottom:12px;
}
.feature-card h3::after,.casino-card h3::after,.icon-card h3::after,
.poker-feature-card h3::after,.aviator-feature h3::after,
.action-card h3::after,.step-card h3::after{
  content:"";position:absolute;left:0;bottom:0;width:32px;height:1px;
  background:linear-gradient(90deg,var(--gold),transparent);
}

/* (13) Lock italic to hero/sub-leads only */
.feature-card p,.casino-card p,.icon-card p,.poker-feature-card p,
.aviator-feature p,.tournament-card p,.action-card p,.step-card p,
.faq-answer p,.tip-card p,.bonus-code-card p,.risk-card p{
  font-style:normal!important;
}

/* (14) "LAST VERIFIED" chip — premium gold pill */
.last-verified,.verified-chip,
[class*="last-verified"]{
  display:inline-flex!important;
  align-items:center;
  gap:8px;
  background:rgba(255,215,0,.08)!important;
  border:1px solid rgba(255,215,0,.5)!important;
  color:#FFD700!important;
  font-style:normal!important;
  font-weight:700!important;
  font-size:12px!important;
  letter-spacing:.08em!important;
  text-transform:uppercase!important;
  padding:8px 16px!important;
  border-radius:999px!important;
  opacity:1!important;
}

/* (15) Card padding consistency */
.feature-card,.casino-card,.icon-card,.poker-feature-card,
.aviator-feature,.tournament-card,.action-card,.bonus-code-card,
.payment-info-card,.tip-card,.risk-card,.step-card{
  padding:32px 28px!important;
}
.feature-grid,.casino-grid,.icon-card-grid,.poker-features,
.aviator-features,.tournament-grid,.payment-info-grid{
  gap:24px!important;
}

/* (16) Footer — wake it up with 3-column structure already there;
       refresh styling so it doesn't read as dead space */
.site-footer{padding:80px 24px 40px!important;border-top:1px solid rgba(255,215,0,.2)!important}
.footer-top{grid-template-columns:280px 1fr!important;gap:60px!important}
.footer-col h4{color:var(--gold)!important;font-size:12px!important;letter-spacing:1.5px!important;border-bottom:1px solid rgba(255,215,0,.18);padding-bottom:8px;margin-bottom:14px!important}
.footer-col a{transition:color .2s,padding-left .2s}
.footer-col a:hover{color:var(--gold)!important;padding-left:4px}
.footer-disclaimer{border-top:1px solid rgba(255,215,0,.1);padding-top:24px}

/* (17) Favicon variants — declared in <head>, this is just a safety hint */

/* (18) 5-room category grid — let it breathe at 1280-1400px */
.five-rooms-grid,.rooms-grid,.category-grid.rooms-5{
  display:grid;
  grid-template-columns:repeat(5,1fr);
  gap:18px;
}
@media(max-width:1280px){.five-rooms-grid,.rooms-grid,.category-grid.rooms-5{grid-template-columns:repeat(3,1fr)}}
@media(max-width:760px){.five-rooms-grid,.rooms-grid,.category-grid.rooms-5{grid-template-columns:1fr}}

/* --- bonus polish: section dividers + breathing room */
.section,section.section,.content-section{padding-top:96px!important;padding-bottom:96px!important}
@media(max-width:760px){.section,section.section,.content-section{padding-top:56px!important;padding-bottom:56px!important}}

/* Body italic lockdown */
body p{font-style:normal}
.hero-subtitle,.ch-sub,.page-hero-sub,.section-subtitle{font-style:italic}
"""

# Append CSS to both files
for css_file in [ROOT / "style.min.css", ROOT / "style.css"]:
    if css_file.exists():
        s = css_file.read_text()
        marker = "/* === 2026-06-07 polish-pass v3"
        # Remove any previous v3 block (idempotency)
        if marker in s:
            s = s[:s.index(marker)].rstrip() + "\n"
        s = s.rstrip() + "\n" + V3_CSS
        css_file.write_text(s)

# -----------------------------------------------------------------------------
# 4. Walk every HTML file and:
#    a) replace the Stake-branded footer SVG with the WinnersClub shield
#    b) ensure <link rel="preconnect" href="https://fonts.googleapis.com"> +
#       Playfair Display font load (for new H2 serif)
#    c) add favicon variants in <head>
#    d) ensure body has class "wc-body" so sticky padding rule applies (we
#       used `body{padding-bottom}` directly so this isn't strictly needed)
# -----------------------------------------------------------------------------
PLAYFAIR_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">'

FAVICON_LINKS = (
    '<link rel="icon" type="image/svg+xml" href="/favicon.svg">'
    '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">'
    '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">'
)

count_svg = 0
count_font = 0
count_fav = 0
for html in ROOT.rglob("*.html"):
    if any(seg in html.parts for seg in (".git", "__pycache__", "research", "build_helpers")):
        continue
    s = html.read_text(encoding="utf-8", errors="ignore")
    orig = s

    # 4a) Footer SVG swap
    if 'aria-label="Stake"' in s:
        s = STAKE_SVG_RE.sub(WC_SHIELD, s)
        count_svg += 1

    # 4b) Inject Playfair font if missing (place before </head>)
    if "Playfair+Display" not in s and "</head>" in s:
        s = s.replace("</head>", PLAYFAIR_LINK + "</head>", 1)
        count_font += 1

    # 4c) Favicon: only add if not already present
    if "favicon.svg" not in s and "</head>" in s:
        s = s.replace("</head>", FAVICON_LINKS + "</head>", 1)
        count_fav += 1

    if s != orig:
        html.write_text(s, encoding="utf-8")

print(f"Footer SVG swapped on {count_svg} pages")
print(f"Playfair font injected on {count_font} pages")
print(f"Favicon links injected on {count_fav} pages")

# -----------------------------------------------------------------------------
# 5. Build favicon.svg + favicon-32.png + apple-touch-icon.png
#    (gold shield + W on dark)
# -----------------------------------------------------------------------------
FAVICON_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFD700"/>
      <stop offset="1" stop-color="#b8860b"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="12" fill="#141415"/>
  <path d="M32 6 L52 12 L52 32 C52 44 42 54 32 58 C22 54 12 44 12 32 L12 12 Z" fill="url(#g)" stroke="#141415" stroke-width="1.5"/>
  <path d="M20 24 L26 44 L32 30 L38 44 L44 24" stroke="#141415" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
(ROOT / "favicon.svg").write_text(FAVICON_SVG)
print("favicon.svg written")
