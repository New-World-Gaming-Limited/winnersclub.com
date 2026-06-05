# -*- coding: utf-8 -*-
"""Generator for the 11 English WinnersClub 'ultimate Stake club' pages."""
import os, json, html

AFF = "https://www.getstake.it/i/maxbet/io/maxbet/u/maxbet/uo/maxbet"
GA = "G-WCFWWYWP7R"
ROOT = "/home/user/workspace/winnersclub.com"

# ---------- shared logo SVG (verbatim from index.html) ----------
LOGO_SVG = '''<svg width="200" height="38" viewBox="0 0 200 38" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="wc-crest" x1="4" y1="2" x2="36" y2="38" gradientUnits="userSpaceOnUse">
              <stop offset="0" stop-color="#FFEFAE"/>
              <stop offset="0.45" stop-color="#E8B736"/>
              <stop offset="1" stop-color="#7A5512"/>
            </linearGradient>
            <linearGradient id="wc-text-gold" x1="0" y1="10" x2="0" y2="30" gradientUnits="userSpaceOnUse">
              <stop offset="0" stop-color="#FFE57A"/>
              <stop offset="1" stop-color="#D6A21E"/>
            </linearGradient>
            <linearGradient id="wc-bar" x1="0" y1="0" x2="120" y2="0" gradientUnits="userSpaceOnUse">
              <stop offset="0" stop-color="#D6A21E" stop-opacity="0"/>
              <stop offset="0.5" stop-color="#FFE57A"/>
              <stop offset="1" stop-color="#D6A21E" stop-opacity="0"/>
            </linearGradient>
            <radialGradient id="wc-crest-inner" cx="20" cy="14" r="18" gradientUnits="userSpaceOnUse">
              <stop offset="0" stop-color="#FFE9A8" stop-opacity="0.8"/>
              <stop offset="1" stop-color="#FFE9A8" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <g>
            <path d="M4 6.5 L20 2.5 L36 6.5 L36 22 C36 30.2 28.5 35.8 20 38 C11.5 35.8 4 30.2 4 22 Z" fill="url(#wc-crest)"/>
            <path d="M4 6.5 L20 2.5 L36 6.5 L36 22 C36 30.2 28.5 35.8 20 38 C11.5 35.8 4 30.2 4 22 Z" fill="url(#wc-crest-inner)"/>
            <path d="M5.4 7.4 L20 3.7 L34.6 7.4 L34.6 21.8 C34.6 29 27.6 34.3 20 36.4 C12.4 34.3 5.4 29 5.4 21.8 Z" fill="none" stroke="#5A3F0E" stroke-width="0.4" opacity="0.55"/>
            <text x="20" y="22" font-family="Georgia, 'Times New Roman', serif" font-size="16" font-weight="700" font-style="italic" text-anchor="middle" fill="#1A1308" letter-spacing="-0.8">W</text>
            <text x="20" y="32" font-family="Georgia, 'Times New Roman', serif" font-size="9" font-weight="700" font-style="italic" text-anchor="middle" fill="#1A1308" letter-spacing="2">CLUB</text>
          </g>
          <g transform="translate(46, 0)">
            <text x="0" y="22" font-family="Inter, system-ui, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" letter-spacing="-0.4">Winners<tspan fill="url(#wc-text-gold)">Club</tspan></text>
            <rect x="0" y="28" width="150" height="1.2" fill="url(#wc-bar)"/>
          </g>
        </svg>'''

STAKE_FOOTER_SVG = '''<svg width="80" height="38" viewBox="0 0 74 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Stake">
            <path d="M29.1115 10.208C30.1487 10.208 31.0356 10.842 31.0959 12.6963L31.4601 21.4219L35.4465 11.6406C35.8806 10.5914 36.6194 10.208 37.7228 10.208H40.6838C42.2819 10.208 42.6501 11.6798 42.0109 13.1904L36.1096 27.7871C35.5337 29.2101 34.9846 29.9971 33.6701 29.9971L29.0451 30C27.5587 29.9999 26.7382 29.0408 26.7111 27.4277L26.3976 20.1523L23.3039 27.7773C22.7823 29.0196 22.2671 30 20.9797 30L16.924 29.9941C15.3081 29.9941 14.3853 29.1437 14.343 27.2295L14.1144 21.8594L15.3625 15.1953C15.8237 12.3645 14.8889 11.1646 14.093 10.2148L17.5275 10.2109C18.872 10.211 19.4293 10.8084 19.4806 12.4844L19.84 21.4248L23.841 11.5889C24.2119 10.6845 24.906 10.208 26.0969 10.208H29.1115Z" fill="white"/>
            <path d="M7.85174 10.6641C9.28687 9.94345 10.6554 10.0338 11.7619 10.7754C12.9287 11.6226 13.5922 12.9158 13.2336 14.6885L10.924 26.9912C10.5862 28.993 8.65369 30.3133 6.64276 29.9336C4.74922 29.5748 3.35277 27.7988 3.72967 25.6641L5.03826 18.5391L4.22479 18.9072C2.71416 19.5856 0.937298 18.9073 0.261897 17.3877C-0.413447 15.8681 0.262199 14.0858 1.77264 13.4043L7.85174 10.6641Z" fill="white"/>
            <path d="M49.2443 10.2119C51.2703 10.212 51.7946 11.1853 51.3332 13.3047L48.8039 27.1504C48.5479 28.6639 48.1102 29.9969 46.3224 29.9971H43.1476C41.6276 29.9971 41.0944 28.8513 41.3537 27.3799L43.964 12.7324C44.2263 11.1736 44.899 10.212 46.8498 10.2119H49.2443Z" fill="white"/>
            <path d="M67.5851 10.2051C69.5359 10.2051 70.4343 10.5584 71.5197 11.5322C73.3285 13.1514 73.6701 15.5666 73.2629 17.4873L71.466 27.1445C71.2158 28.6069 70.8296 29.9912 69.0656 29.9912L65.9572 29.9941C64.6034 29.9941 63.8884 29.0049 64.1535 27.3135L65.4142 19.7607C65.5949 18.3738 65.3328 17.3905 64.5793 16.7754C63.4065 15.8196 61.7479 16.2354 60.9064 17.2002C60.3638 17.7791 60.1169 18.5663 59.8273 20.1611L58.5607 27.1533C58.3225 28.5342 57.9366 29.9969 56.1037 29.9971H52.9797C51.035 29.9971 50.8989 28.3024 51.1193 27.3164L53.7512 12.7295C54.0076 11.3907 54.4814 10.208 56.6369 10.208L58.8771 10.2051C60.6138 10.2051 61.6483 10.8506 61.1027 13.2988L60.8703 14.5107C62.0672 12.0716 65.0013 10.2052 67.5851 10.2051Z" fill="white"/>
            <path d="M48.5988 1C50.5736 1.00011 52.175 2.60414 52.175 4.58203C52.175 6.55993 50.5736 8.16395 48.5988 8.16406C46.6239 8.16406 45.0226 6.56 45.0226 4.58203C45.0226 2.60407 46.6239 1 48.5988 1Z" fill="white"/>
          </svg>'''

# ---------- nav ----------
NAV = '''      <nav class="header-nav" id="mainNav">
        <a href="/casino/" class="nav-link">Casino</a>
        <a href="/sports/" class="nav-link">Sports</a>
        <a href="/poker/" class="nav-link">Poker</a>
        <a href="/aviator/" class="nav-link">Aviator</a>
        <a href="/promo-code/" class="nav-link">Promo Code</a>
        <a href="/reserves/" class="nav-link">Reserves</a>
        <a href="/about-stake/" class="nav-link">About</a>
      </nav>'''

LANG = '<select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="Language"><option value="" selected>EN</option></select>'


def head(title, desc, path, og_title=None, jsonld=None):
    canonical = f"https://winnersclub.com/{path}"
    og_title = og_title or title
    jl = ""
    for block in (jsonld or []):
        jl += '\n<script type="application/ld+json">\n' + json.dumps(block, indent=2, ensure_ascii=False) + '\n</script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="theme-color" content="#141415">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{html.escape(og_title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="/images/og-default.png">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.min.css">
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA}', {{anonymize_ip: true}});
  </script>
  <script src="/exit-tracker.js" defer></script>{jl}
</head>
<body>
'''


def header():
    return f'''  <!-- HEADER -->
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/" class="header-logo" aria-label="WinnersClub home">
        {LOGO_SVG}
      </a>
{NAV}
      <div class="header-actions">{LANG}
        <a href="{AFF}" target="_blank" rel="noopener" class="btn btn-signup" aria-label="Step inside">Step inside</a>
        <button class="hamburger" id="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
'''


def hero(img, tease, title_html, sub_html, primary_text, primary_href, secondary_text=None, secondary_href=None):
    sec = ""
    if secondary_text:
        sec = f'<a href="{secondary_href}" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">{secondary_text}</a>'
    return f'''  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:url('/images/{img}');"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">{tease}</p>
        <h1 class="ch-title text-gradient-gold">{title_html}</h1>
        <p class="ch-sub">{sub_html}</p>
        <div class="ch-actions">
          <a href="{primary_href}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">{primary_text}</a>
          {sec}
        </div>
      </div>
    </div>
  </section>
'''


def voice_player(transcript):
    return f'''  <!-- VOICE PLAYER -->
  <span class="vp-listen-label">Listen - the hostess will walk you through it.</span>
  <div class="voice-player" data-audio="" data-transcript-id="page-transcript" data-open="false">
    <button class="vp-btn" aria-label="Play the hostess welcome">&#9658;</button>
    <div class="vp-meta">
      <div class="vp-title">The hostess's welcome</div>
      <div class="vp-line">A short briefing. <span class="vp-transcript">Read the transcript</span></div>
    </div>
  </div>
  <div class="voice-transcript" id="page-transcript"><p>{transcript}</p></div>
'''


def girl_break(img, title_html, sub_html, btn_text="Hand the dealer the code"):
    return f'''  <!-- GIRL BREAK -->
  <section class="girl-break girl-right">
    <div class="girl-break-bg" style="background: url('/images/{img}') center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">{title_html}</h2>
      <p class="girl-break-sub">{sub_html}</p>
      <a href="{AFF}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">{btn_text}</a>
    </div>
  </section>
'''


def faq_section(items):
    rows = ""
    for q, a in items:
        rows += f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{q}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{a}</p></div>
        </div>
'''
    return f'''  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title">Questions <span class="text-gradient-gold">at the door</span></h2></div>
      <div class="faq-list">
{rows}      </div>
    </div>
  </section>
'''


def signature():
    return '''  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Tell the dealer WinnersClub sent you.</p>
    </div>
  </section>
'''


def sticky_cta():
    return f'''  <!-- STICKY CTA -->
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">The code is <span class="code-highlight">MAXBET</span>. 200% up to $3,000. The door's open at Stake.com</div>
    <div class="sticky-cta-actions">
      <a href="{AFF}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Take your seat &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="Dismiss">&times;</button>
  </div>
'''


def footer():
    return f'''  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          {STAKE_FOOTER_SVG}
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">THE CLUB'S BEEN AT STAKE SINCE 2017.</p>
          <div class="footer-badges">
            <span class="age-badge">18+</span>
            <span class="cert-badge">GamCare</span>
            <span class="cert-badge">SSL</span>
          </div>
        </div>
        <div class="footer-links-grid">
          <div class="footer-col">
            <h4>The floor</h4>
            <a href="/casino/">Casino</a>
            <a href="/sports/">Sportsbook</a>
            <a href="/poker/">Poker</a>
            <a href="/aviator/">Aviator</a>
            <a href="/live-odds/">Live Odds</a>
          </div>
          <div class="footer-col">
            <h4>The code</h4>
            <a href="/promo-code/">Promo Code MAXBET</a>
            <a href="/payments/">Payments</a>
            <a href="/mirror/">Access &amp; Mirrors</a>
          </div>
          <div class="footer-col">
            <h4>The intel</h4>
            <a href="/about-stake/">About Stake</a>
            <a href="/reserves/">On-chain Reserves</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">WinnersClub is the players' insider club for Stake. Stake.com is operated by Medium Rare NV under Curacao licence 1668/JAZ. Stake.us is a separate sweepstakes platform run by Sweepsteaks Limited. This site is for informational purposes only. Gambling involves risk - please play responsibly. If you or someone you know has a gambling problem, contact GamCare or a local support organisation. 18+.</p>
        <p class="footer-copyright">&copy; 2026 winnersclub.com. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="/script.min.js" defer></script>
  <script src="/voice.js" defer></script>
</body>
</html>
'''


def page(path, head_html, body_sections, extra_scripts=""):
    out = head_html + header()
    for s in body_sections:
        out += s
    out += signature() + sticky_cta() + footer()
    if extra_scripts:
        out = out.replace('  <script src="/voice.js" defer></script>', '  <script src="/voice.js" defer></script>\n' + extra_scripts)
    if path == "":
        fp = os.path.join(ROOT, "index.html")
    else:
        d = os.path.join(ROOT, path)
        os.makedirs(d, exist_ok=True)
        fp = os.path.join(d, "index.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(out)
    return fp


def section(title_html, inner_html, surface=False, sub=None):
    bg = ' style="background:var(--surface);"' if surface else ''
    subh = f'<p class="section-subtitle">{sub}</p>' if sub else ''
    return f'''  <section class="section"{bg}>
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title">{title_html}</h2>{subh}</div>
      {inner_html}
    </div>
  </section>
'''


def jsonld_webpage(name, desc, path):
    return {"@context": "https://schema.org", "@type": "WebPage", "name": name,
            "description": desc, "url": f"https://winnersclub.com/{path}"}

def jsonld_breadcrumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": u}
                                 for i, (n, u) in enumerate(items)]}

def jsonld_faq(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
