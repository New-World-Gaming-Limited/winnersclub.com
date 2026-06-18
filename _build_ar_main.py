#!/usr/bin/env python3
"""Build /ar/ locale for winnersclub.com - 19 Arabic (MSA/RTL) pages."""
import os, re

ROOT = '/home/user/workspace/winnersclub.com'

# ── Shared HTML fragments ──────────────────────────────────────────────────
HREFLANG = '''  <link rel="alternate" hreflang="en" href="https://winnersclub.com/{en_path}">
  <link rel="alternate" hreflang="ko" href="https://winnersclub.com/ko/{slug}">
  <link rel="alternate" hreflang="zh-Hans" href="https://winnersclub.com/zh/{slug}">
  <link rel="alternate" hreflang="vi" href="https://winnersclub.com/vi/{slug}">
  <link rel="alternate" hreflang="th" href="https://winnersclub.com/th/{slug}">
  <link rel="alternate" hreflang="ms" href="https://winnersclub.com/ms/{slug}">
  <link rel="alternate" hreflang="pt" href="https://winnersclub.com/pt/{slug}">
  <link rel="alternate" hreflang="ja" href="https://winnersclub.com/ja/{slug}">
  <link rel="alternate" hreflang="es" href="https://winnersclub.com/es/{slug}">
  <link rel="alternate" hreflang="pt-BR" href="https://winnersclub.com/pt-br/{slug}">
  <link rel="alternate" hreflang="tr" href="https://winnersclub.com/tr/{slug}">
  <link rel="alternate" hreflang="id" href="https://winnersclub.com/id/{slug}">
  <link rel="alternate" hreflang="fr" href="https://winnersclub.com/fr/{slug}">
  <link rel="alternate" hreflang="ru" href="https://winnersclub.com/ru/{slug}">
  <link rel="alternate" hreflang="hi" href="https://winnersclub.com/hi/{slug}">
  <link rel="alternate" hreflang="ar" href="https://winnersclub.com/ar/{slug}">
  <link rel="alternate" hreflang="x-default" href="https://winnersclub.com/{en_path}">'''

MOBILE_LANG = '''<div class="mobile-lang-block"><label>اللغة</label><select onchange="if(this.value)window.location.href=this.value" aria-label="اللغة"><option value="">English</option><option value="/ko/">한국어 (Korean)</option><option value="/zh/">中文 (Chinese)</option><option value="/vi/">Tiếng Việt (Vietnamese)</option><option value="/th/">ไทย (Thai)</option><option value="/ms/">Bahasa Melayu (Malay)</option><option value="/pt/">Português (Portuguese)</option><option value="/ja/">日本語 (Japanese)</option><option value="/es/">Español (Spanish)</option><option value="/pt-br/">Português do Brasil (Portuguese - Brazil)</option><option value="/tr/">Türkçe (Turkish)</option><option value="/id/">Bahasa Indonesia (Indonesian)</option><option value="/fr/">Français (French)</option><option value="/ru/">Русский (Russian)</option><option value="/hi/">हिन्दी (Hindi)</option><option value="/ar/" selected>العربية (Arabic)</option></select></div>'''

DESKTOP_LANG = '''<select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="اللغة"><option value="https://winnersclub.com/">English</option><option value="https://winnersclub.com/ko/">한국어</option><option value="https://winnersclub.com/zh/">中文</option><option value="https://winnersclub.com/vi/">Tiếng Việt</option><option value="https://winnersclub.com/th/">ไทย</option><option value="https://winnersclub.com/ms/">Bahasa Melayu</option><option value="https://winnersclub.com/pt/">Português</option><option value="https://winnersclub.com/ja/">日本語</option><option value="https://winnersclub.com/es/">Español</option><option value="https://winnersclub.com/pt-br/">Português (BR)</option><option value="https://winnersclub.com/tr/">Türkçe</option><option value="https://winnersclub.com/id/">Bahasa Indonesia</option><option value="https://winnersclub.com/fr/">Français</option><option value="https://winnersclub.com/ru/">Русский</option><option value="https://winnersclub.com/hi/">हिन्दी</option><option value="" selected>العربية</option></select>'''

FOOTER_SVG = '''<svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub">
  <path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/>
  <path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text>
</svg>'''

ORG_JSONLD = '{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"The players back room for Stake. Promo code MAX3000 unlocks a 200% match up to $3,000 with 40x wagering."}'
WEBSITE_JSONLD = '{"@context":"https://schema.org","@type":"WebSite","url":"https://winnersclub.com/","name":"WinnersClub","potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://winnersclub.com/?q={search_term_string}"},"query-input":"required name=search_term_string"}}'

def nav(slug_prefix):
    """Desktop nav links for /ar/ pages."""
    return f'''<a href="/ar/casino/" class="nav-link">كازينو</a>
        <a href="/ar/sports/" class="nav-link">الرياضة</a>
        <a href="/ar/poker/" class="nav-link">بوكر</a>
        <a href="/ar/aviator/" class="nav-link">أفياتور</a>
        <a href="/ar/promo-code/" class="nav-link">الرمز الترويجي</a>
        <a href="/ar/reserves/" class="nav-link">الاحتياطيات</a>
        <a href="/ar/about-stake/" class="nav-link">حول <bdi dir="ltr">Stake</bdi></a>'''

def footer_ar(page_slug=''):
    return f'''  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          {FOOTER_SVG}
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">النادي مع <bdi dir="ltr">Stake</bdi> منذ 2017.</p>
          <div class="footer-badges">
            <span class="age-badge">18+</span>
            <span class="cert-badge">GamCare</span>
            <span class="cert-badge">SSL</span>
          </div>
        </div>
        <div class="footer-links-grid anim-stagger">
          <div class="footer-col">
            <h4>الصالة</h4>
            <a href="/ar/casino/">كازينو</a>
            <a href="/ar/sports/">رياضة</a>
            <a href="/ar/poker/">بوكر</a>
            <a href="/ar/aviator/">أفياتور</a>
            <a href="/ar/live-odds/">أحداث مباشرة</a>
          </div>
          <div class="footer-col">
            <h4>الرمز</h4>
            <a href="/ar/promo-code/">الرمز الترويجي <bdi dir="ltr">MAX3000</bdi></a>
            <a href="/ar/payments/">المدفوعات</a>
            <a href="/ar/mirror/">مواقع المرآة</a>
          </div>
          <div class="footer-col">
            <h4>المعلومات</h4>
            <a href="/ar/about-stake/">حول <bdi dir="ltr">Stake</bdi></a>
            <a href="/ar/reserves/">الاحتياطيات على السلسلة</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer"><bdi dir="ltr">WinnersClub</bdi> هو النادي الداخلي الحصري للاعبي <bdi dir="ltr">Stake</bdi>. تُشغِّل <bdi dir="ltr">Stake.com</bdi> شركةُ <bdi dir="ltr">Medium Rare NV</bdi> بموجب ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi>. <bdi dir="ltr">Stake.us</bdi> منصة سحوبات مستقلة تُشغِّلها <bdi dir="ltr">Sweepsteaks Limited</bdi>. هذا الموقع لأغراض إعلامية فقط. القمار ينطوي على مخاطر، العب بمسؤولية. إذا كنت تعاني من مشكلة قمار فتواصل مع <bdi dir="ltr">GamCare</bdi> أو جهة دعم محلية. للبالغين 18 عاماً فأكثر.</p>
        <p class="footer-copyright">&copy; 2026 <bdi dir="ltr">winnersclub.com</bdi>. جميع الحقوق محفوظة.</p>
      </div>
    </div>
  </footer>'''

def rooms_grid_ar():
    return '''<aside class="rooms-grid" aria-label="غرف أخرى في وينرز كلوب" style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);border:1px solid rgba(255,215,0,.12);border-radius:14px;"><h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#737378;margin:0 0 18px;font-weight:700;">غرف أخرى في وينرز كلوب</h3><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;"><li><a href="/ar/promo-code/">الرمز الترويجي لـ Stake</a></li><li><a href="/ar/casino/">كازينو Stake</a></li><li><a href="/ar/sports/">الرياضة في Stake</a></li><li><a href="/ar/poker/">بوكر Stake</a></li><li><a href="/ar/aviator/">Stake Aviator</a></li><li><a href="/ar/reserves/">الاحتياطيات المُتحقق منها</a></li><li><a href="/ar/about-stake/">حول Stake.com</a></li><li><a href="/ar/payments/">مدفوعات العملات الرقمية</a></li><li><a href="/ar/mirror/">مواقع المرآة</a></li><li><a href="/ar/live-odds/">الأحداث المباشرة</a></li><li><a href="/ar/originals/">Stake Originals</a></li><li><a href="/ar/vip/">برنامج VIP</a></li><li><a href="/ar/slots/">مكتبة السلوتس</a></li><li><a href="/ar/live-casino/">الكازينو المباشر</a></li></ul></aside>'''

def ticker_ar():
    return '''<div class="reserves-ticker"><div class="rt-inner"><span><bdi dir="ltr">Stake</bdi> على السلسلة: <bdi dir="ltr">$339.53M</bdi> احتياطيات موسومة &middot; <bdi dir="ltr">Ethereum 74%</bdi> &middot; <bdi dir="ltr">Solana 14%</bdi> &middot; <bdi dir="ltr">Tron USDT 5%</bdi> &middot; <bdi dir="ltr">BNB Chain 6%</bdi> &middot; ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi> &middot; المصدر: <bdi dir="ltr">Arkham Intel</bdi> عبر <bdi dir="ltr">cryptotips.com</bdi> &middot; لقطة 28 مايو 2026</span><span><bdi dir="ltr">Stake</bdi> على السلسلة: <bdi dir="ltr">$339.53M</bdi> احتياطيات موسومة &middot; <bdi dir="ltr">Ethereum 74%</bdi> &middot; <bdi dir="ltr">Solana 14%</bdi> &middot; <bdi dir="ltr">Tron USDT 5%</bdi> &middot; <bdi dir="ltr">BNB Chain 6%</bdi> &middot; ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi> &middot; المصدر: <bdi dir="ltr">Arkham Intel</bdi> عبر <bdi dir="ltr">cryptotips.com</bdi> &middot; لقطة 28 مايو 2026</span></div></div>'''

def promo_strip_ar():
    return '''<aside class="promo-strip" aria-label="الرمز الترويجي MAX3000"><div class="ps-inner"><span class="ps-label">الرمز الترويجي</span><span class="ps-code"><bdi dir="ltr">MAX3000</bdi></span><span class="ps-bonus">200% حتى <bdi dir="ltr">$3,000</bdi> &middot; شرط رهان 40x</span><a href="/ar/promo-code/" class="ps-cta">فتح صفحة الرمز &rarr;</a></div></aside>'''

def page_template(
    lang='ar', dir_attr='rtl',
    title='', description='',
    canonical_path='ar/', og_url_path='ar/',
    og_image='default.png',
    hreflang_slug='', hreflang_en_path='',
    jsonld_extra='',
    page_bc_name='', page_bc_url='',
    hero_tease='', h1_main='', h1_sub='',
    hero_sub_html='', hero_img='girl-homepage-3',
    promo_strip=True, ticker=True,
    cta_btn_text='احصل على 200% حتى $3,000 في Stake.com',
    body_html='',
    sticky_text='',
    extra_scripts='',
    font_noto=True,
    page_slug='',
):
    noto_font = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;500;600;700;900&display=swap" rel="stylesheet">' if font_noto else ''
    
    bc_jsonld = f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"الرئيسية","item":"https://winnersclub.com/ar/"}}'
    if page_bc_name:
        bc_jsonld += f',{{"@type":"ListItem","position":2,"name":"{page_bc_name}","item":"https://winnersclub.com/{page_bc_url}"}}'
    bc_jsonld += ']}'
    
    hreflang_block = HREFLANG.format(
        en_path=hreflang_en_path or '',
        slug=hreflang_slug or ''
    )
    
    ticker_html = ticker_ar() if ticker else ''
    promo_html = promo_strip_ar() if promo_strip else ''
    
    if not sticky_text:
        sticky_text = f'الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. 200% حتى <bdi dir="ltr">$3,000</bdi>. باب <bdi dir="ltr">Stake.com</bdi> مفتوح'

    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><script>document.documentElement.classList.add("js-anim");</script>
  <meta charset="UTF-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://winnersclub.com/{canonical_path}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://winnersclub.com/{og_url_path}">
  <meta property="og:image" content="https://winnersclub.com/images/og/{og_image}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <meta name="theme-color" content="#8b0a1a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900&display=swap" rel="stylesheet">
  {noto_font}
  <link rel="stylesheet" href="/style.min.css?v=20260618a">
  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-WCFWWYWP7R"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-WCFWWYWP7R', {{anonymize_ip: true}});
  </script>
  <script src="/exit-tracker.js" defer></script>
{jsonld_extra}
<script type="application/ld+json">{bc_jsonld}</script>
<script type="application/ld+json" data-ld="org">{ORG_JSONLD}</script>
<script type="application/ld+json" data-ld="website">{WEBSITE_JSONLD}</script>
{hreflang_block}
  <script src="/lang-redirect.js" defer></script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap"><link rel="preload" as="image" href="/images/{hero_img}-3.avif" type="image/avif" fetchpriority="high">
<meta name="twitter:image" content="https://winnersclub.com/images/og/{og_image}"><meta name="twitter:card" content="summary_large_image"></head>
<body>
  <!-- HEADER -->
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/ar/" class="header-logo" aria-label="WinnersClub الرئيسية">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        {nav(page_slug)}
      {MOBILE_LANG}</nav>
      <div class="header-actions">{DESKTOP_LANG}
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup" aria-label="انضم الآن">انضم الآن</a>
        <button class="hamburger" id="hamburger" aria-label="فتح القائمة"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/{hero_img}-3.avif') type('image/avif'), url('/images/{hero_img}-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">{hero_tease}</p>
        <h1 class="ch-title text-gradient-gold">{h1_main}<span class="h1-sub">{h1_sub}</span></h1>
        <p class="ch-sub">{hero_sub_html}</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">{cta_btn_text}</a>
          <a href="/ar/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">ما يفتحه <bdi dir="ltr">MAX3000</bdi></a>
        </div>
      </div>
    </div>
  </section>
  {ticker_html}
  {promo_html}
{body_html}
  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر الموزع أن <bdi dir="ltr">WinnersClub</bdi> أرسلك.</p>
    </div>
  </section>
  <!-- STICKY CTA -->
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">{sticky_text}</div>
    <div class="sticky-cta-actions">
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">احجز مكانك &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="إغلاق">&times;</button>
  </div>
  <!-- FOOTER -->
  {footer_ar(page_slug)}

  <script src="/script.min.js?v=20260618a" defer></script>
  <script src="/voice.js" defer></script>
{extra_scripts}
<script src="/ga-events.js" defer></script>{rooms_grid_ar()}</body>
</html>'''


def write_page(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  wrote {path.replace(ROOT+'/', '')}")


# ── Page builder helpers ───────────────────────────────────────────────────
def faq_section(items, title='أسئلة على باب النادي'):
    html = f'''  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">{title}</h2></div>
      <div class="faq-list">'''
    for q, a in items:
        html += f'''
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{q}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{a}</p></div>
        </div>'''
    html += '''
      </div>
    </div>
  </section>'''
    return html

def faq_jsonld(items):
    entries = []
    for q, a in items:
        clean_a = re.sub(r'<[^>]+>', '', a)
        clean_q = re.sub(r'<[^>]+>', '', q)
        entries.append(f'{{"@type":"Question","name":"{clean_q}","acceptedAnswer":{{"@type":"Answer","text":"{clean_a}"}}}}')
    return '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}'.format(items=','.join(entries))

def intel_cards(cards):
    html = '<div class="intel-grid anim-stagger">'
    for label, value, detail in cards:
        html += f'<div class="intel-card"><div class="ic-label">{label}</div><div class="ic-value">{value}</div><div class="ic-detail">{detail}</div></div>'
    html += '</div>'
    return html

def club_cards(cards):
    html = '<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">'
    for h3, p in cards:
        html += f'<div class="club-card"><h3>{h3}</h3><p>{p}</p></div>'
    html += '</div>'
    return html

def step_cards(steps):
    html = '<div class="step-cards anim-stagger">'
    for title, content in steps:
        html += f'<div class="step-card"><h3>{title}</h3><p>{content}</p></div>'
    html += '</div>'
    return html

def girl_break(title, sub, cta='انضم الآن', img='girl-homepage-2'):
    return f'''  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/{img}-2.avif') type('image/avif'), url('/images/{img}-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">{title}</h2>
      <p class="girl-break-sub">{sub}</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">{cta}</a>
    </div>
  </section>'''


# ══════════════════════════════════════════════════════════════════════════
# PAGE CONTENT FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════

def build_index():
    faqs = [
        ('هل <bdi dir="ltr">MAX3000</bdi> هو أكبر رمز مكافأة في <bdi dir="ltr">Stake</bdi>؟',
         'نعم. 200% حتى <bdi dir="ltr">$3,000</bdi> مع شرط رهان 40x على مجموع الإيداع والمكافأة. معظم الرموز العامة تقتصر على 100% / <bdi dir="ltr">$1,000</bdi>. <bdi dir="ltr">MAX3000</bdi> هو الرمز الذي يسلِّمه النادي عند المدخل.'),
        ('هل <bdi dir="ltr">Stake.com</bdi> موثوق؟',
         '<bdi dir="ltr">Stake</bdi> يعمل منذ 2017 تحت ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi> بواسطة <bdi dir="ltr">Medium Rare NV</bdi>. الاحتياطيات على السلسلة بلغت <bdi dir="ltr">$339.53M</bdi> في 28 مايو 2026 وهي قابلة للتتبع عبر <bdi dir="ltr">Arkham</bdi>. المؤسسان Ed Craven (مواليد 1995، ملبورن) و Bijan Tehrani يديران أيضاً Kick.'),
        ('هل يمكنني التحقق من احتياطيات <bdi dir="ltr">Stake</bdi>؟',
         'نعم، راجع صفحة الاحتياطيات في <a href="/ar/reserves/" style="color:var(--gold);">winnersclub.com/ar/reserves/</a>. لقطة 28 مايو 2026 تُظهر <bdi dir="ltr">$339.53M</bdi> في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%، رصيد عملات مستقرة بتسعة أرقام. كل شيء قابل للتتبع عبر <a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener">cryptotips.com</a>.'),
        ('أين يمكنني اللعب؟',
         'ترخيص كوراساو يغطي معظم الدول؛ غير أن <bdi dir="ltr">Stake</bdi> يفرض قيوداً ذاتية في الولايات المتحدة والمملكة المتحدة وبعض الدول الأخرى. راجع <a href="/ar/mirror/" style="color:var(--gold);">صفحة مواقع المرآة</a> لإيجاد النطاق المناسب لمنطقتك.'),
        ('كم تستغرق عمليات السحب؟',
         'عمليات سحب العملات الرقمية تكتمل عادةً في 30 دقيقة إلى ساعة. TRX وXRP وSOL تُسوَّى خلال ثوانٍ. السحوبات الكبيرة قد تستلزم مراجعة امتثال تستغرق يومين إلى أربعة أيام عمل. سحوبات العملة الورقية عبر MoonPay تستغرق 1 إلى 5 أيام عمل. راجع <a href="/ar/payments/" style="color:var(--gold);">صفحة المدفوعات</a> للتفاصيل.')
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    webpage_ld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000","description":"النادي الداخلي الحصري للاعبي Stake.com. الرمز الترويجي MAX3000 يفتح 200% حتى $3,000 مع شرط رهان 40x. GGR $4.7B، 21M+ حساب، $339M احتياطيات على السلسلة.","url":"https://winnersclub.com/ar/"}</script>'''
    
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لماذا هذا <span class="text-gradient-gold">النادي</span></h2></div>
      {club_cards([
        ('مكافأة بثقل حقيقي', 'أقصى 200% حتى <bdi dir="ltr">$3,000</bdi> مع شرط رهان 40x على مجموع الإيداع والمكافأة. الرموز الأخرى المتاحة للعموم تقف عند 100% / <bdi dir="ltr">$1,000</bdi>. لا تُسلِّم الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للموزع بعد التسجيل وستعود للقائمة الرخيصة.'),
        ('الأموال معلَّقة على الحائط', 'احتياطيات Arkham الموسومة <bdi dir="ltr">$339.53M</bdi> في 28 مايو 2026. لا PDF "ثق بنا"، لا عرض احتياطيات. المحافظ مقروءة علناً، أي شخص بإنترنت يستطيع المراجعة. <a href="/ar/reserves/" style="color:var(--gold);">أرني الإيصال.</a>'),
        ('للبيت وجه معروف', 'Ed Craven (ملبورن، مواليد 1995) وBijan Tehrani. التقيا في RuneScape وأسسا Stake في 2017، وأطلقا Kick في 2022. تقديرات Forbes لصافي ثروتهما المشترك <bdi dir="ltr">US$5.6B</bdi>. ليسوا شركة ورق.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">خمس غرف، <span class="text-gradient-gold">رمز واحد</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">اختر بابك. <bdi dir="ltr">MAX3000</bdi> يعمل في الخمسة جميعاً. الموزع لا يهتم أين تستخدم المكافأة.</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));"><a href="/ar/casino/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">كازينو</div></a><a href="/ar/sports/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-sports-2.avif') type('image/avif'), url('/images/girl-sports-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">رياضة</div></a><a href="/ar/poker/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-poker-2.avif') type('image/avif'), url('/images/girl-poker-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">بوكر</div></a><a href="/ar/aviator/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-aviator-2.avif') type('image/avif'), url('/images/girl-aviator-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">أفياتور</div></a><a href="/ar/live-odds/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-lucky-drive-2.avif') type('image/avif'), url('/images/girl-lucky-drive-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">مباشر</div></a></div>
    </div>
  </section>
  {girl_break('$3,000. <span class="text-gradient-gold">شرط رهان 40x.</span> رمز واحد.', 'همس <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للموزع عند التسجيل. الرياضيات في صفك قبل وصول أول مشروب.', 'سلِّم الرمز للموزع')}
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">ما يعرفه <span class="text-gradient-gold">النادي</span></h2></div>
      {intel_cards([
        ('المؤسسان', 'Craven &amp; Tehrani', 'Ed Craven (مواليد 1995، ملبورن) وBijan Tehrani. التقيا في RuneScape. أسسا Stake في 2017. أطلقا Kick في 2022.'),
        ('الكيان التشغيلي', 'Medium Rare NV', 'الكيان الكوراساوي المشغِّل لـ Stake.com. الشركة الأم: Easygo Group Holdings، إيرادات FY2025 بلغت A$970M. Stake.us كيان سحوبات منفصل.'),
        ('الترخيص', 'OGL/2024/1451/0918', 'يغطي معظم الدول. انسحب من المملكة المتحدة في مارس 2025. الولايات المتحدة محجوبة (Stake.us متاح في 30+ ولاية). أكثر من 22 موقع مرآة موثق.'),
        ('الاحتياطيات', '$339.53M', 'موسومة على Arkham في 28 مايو 2026. Ethereum 74%، Solana 14%، رصيد عملات مستقرة بتسعة أرقام. قابلة للتتبع عبر cryptotips.com.'),
      ])}
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">بابان، <span class="text-gradient-gold">رمز واحد</span></h2>
        <p class="section-subtitle"><bdi dir="ltr">MAX3000</bdi> معترف به في كل من <bdi dir="ltr">Stake.com</bdi> و<bdi dir="ltr">Stake.us</bdi>. الترحيب خلف كل باب مختلف. الموزع سيرشدك إلى الباب المناسب لبلدك.</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3><bdi dir="ltr">Stake.com</bdi> - مال حقيقي، عالمي</h3>
          <p>منصة المال الحقيقي بواسطة <bdi dir="ltr">Medium Rare NV</bdi> تحت ترخيص <bdi dir="ltr">OGL/2024/1451/0918</bdi>. عملات رقمية وورقية. رياضة وكازينو وأصليات وبوكر. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح <strong>200% حتى <bdi dir="ltr">$3,000</bdi></strong>، شرط رهان 40x على الإيداع والمكافأة، 30 يوماً، إيداع أدنى <bdi dir="ltr">$10</bdi>. اطلبها عبر دعم مباشر بعد الإيداع. مستوى KYC 3 مطلوب. متاح في معظم الدول باستثناء الولايات المتحدة والمملكة المتحدة.</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">افتح الباب العالمي</a>
        </div>
        <div class="club-card">
          <h3><bdi dir="ltr">Stake.us</bdi> - سحوبات، الولايات المتحدة</h3>
          <p>منصة سحوبات أمريكية بواسطة <bdi dir="ltr">Sweepsteaks Limited</bdi>. Gold Coins للعب، Stake Cash قابلة للاسترداد بعد 3x play-through. لا إيداع أو سحب حقيقي، لا رياضة، كازينو فقط. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يُعطي <strong>560K GC + 56 SC + 3.5% rakeback</strong>. متاح في 37 ولاية.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">افتح الباب الأمريكي</a>
        </div>
      </div>
    </div>
  </section>
  {faq_section(faqs)}'''
    
    return page_template(
        title='وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000',
        description='النادي الداخلي الحصري للاعبي Stake.com. الرمز الترويجي MAX3000 يفتح 200% حتى $3,000 مع شرط رهان 40x. GGR $4.7B، 21M+ حساب، $339M احتياطيات على السلسلة.',
        canonical_path='ar/',
        og_url_path='ar/',
        og_image='default.png',
        hreflang_slug='',
        hreflang_en_path='',
        jsonld_extra=webpage_ld + '\n' + faq_ld,
        hero_tease='إذا وجدت هذه الصفحة، فالحارس أعجبه وجهك بالفعل.',
        h1_main='الرمز الترويجي لـ Stake هو MAX3000',
        h1_sub='إلى داخل النادي.',
        hero_sub_html='الغرفة الخلفية الحصرية للاعبي Stake. همس <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> عند المدخل وستنتظرك <strong>200% حتى <bdi dir="ltr">$3,000</bdi></strong> مع <strong>شرط رهان 40x على الإيداع والمكافأة</strong>. بعيد عن الرموز الرخيصة المنتشرة.',
        hero_img='girl-homepage',
        body_html=body,
        sticky_text='الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. 200% حتى <bdi dir="ltr">$3,000</bdi>. باب <bdi dir="ltr">Stake.com</bdi> مفتوح',
    )


def build_promo_code():
    faqs = [
        ('ما هو الرمز الترويجي لـ <bdi dir="ltr">Stake.com</bdi>؟',
         'الرمز هو <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. سجِّل عبر رابط الشراكة، أكمل KYC مستوى 3، أودع بين <bdi dir="ltr">$10</bdi> و<bdi dir="ltr">$1,500</bdi>، ثم افتح الدعم المباشر وأخبرهم بـ<bdi dir="ltr">MAX3000</bdi>. الفريق يتحقق من الأهلية ويودع 200% حتى <bdi dir="ltr">$3,000</bdi> خلال 24-48 ساعة.'),
        ('ما الحد الأقصى لمكافأة <bdi dir="ltr">MAX3000</bdi>؟',
         '200% مطابقة بحد أقصى <bdi dir="ltr">$3,000</bdi> مكافأة. إيداع <bdi dir="ltr">$1,500</bdi> يُعطيك المكافأة الكاملة <bdi dir="ltr">$3,000</bdi>. الحد الأدنى للإيداع المؤهِّل <bdi dir="ltr">$10</bdi>، الحد الأقصى <bdi dir="ltr">$1,500</bdi>. الإيداع فوق <bdi dir="ltr">$1,500</bdi> يُعالَج لكن المكافأة لا تزيد.'),
        ('ما شرط الرهان؟',
         '40x على مجموع الإيداع والمكافأة. مثال: إيداع <bdi dir="ltr">$500</bdi> + مكافأة <bdi dir="ltr">$1,000</bdi> = مجموع <bdi dir="ltr">$1,500</bdi> × 40 = رهان <bdi dir="ltr">$60,000</bdi>. ألعاب الكازينو بهامش بيت أعلى من 4% تُسهم 100%، الرياضة 75%. تتبع التقدم من تبويب VIP.'),
        ('هل التحقق من الهوية مطلوب؟',
         'نعم. <bdi dir="ltr">Stake.com</bdi> يشترط KYC مستوى 3 قبل صرف مكافأة الترحيب. قدِّم هوية مصوَّرة وإثبات عنوان ومستندات مصدر الأموال من الإعدادات &rarr; التحقق. لن تُصرف المكافأة إلا بعد اجتياز المستوى 3.'),
        ('كيف تُصرف المكافأة؟',
         'ليست رمز إحالة تلقائياً، بل رصيد يُضاف يدوياً من المشغِّل. بعد إتمام أول إيداع، افتح الدعم المباشر لـ<bdi dir="ltr">Stake</bdi> وأخبرهم أنك سجَّلت بـ<bdi dir="ltr">MAX3000</bdi> وتريد مكافأة الترحيب. بعد التحقق من KYC مستوى 3 وأنه أول إيداع مؤهِّل، تصل 200% خلال <strong>24-48 ساعة</strong>.'),
        ('هل المكافأة للاعبين الجدد فقط؟',
         'نعم. <bdi dir="ltr">MAX3000</bdi> رمز ترحيب لأول إيداع مؤهِّل على حسابات <bdi dir="ltr">Stake.com</bdi> الجديدة فقط. الحسابات القائمة لا تستطيع التأهل بأثر رجعي.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    
    body = f'''  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">رمز النادي</div>
        <div class="code-display"><bdi dir="ltr">MAX3000</bdi></div>
        <div class="code-meta">200% مطابقة &middot; حتى <bdi dir="ltr">$3,000</bdi> مكافأة &middot; إيداع أدنى <bdi dir="ltr">$10</bdi> &middot; شرط رهان 40x على الإيداع والمكافأة &middot; KYC مستوى 3 مطلوب &middot; للعملاء الجدد 18+ فقط</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAX3000">نسخ الرمز</button>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">سلِّم الرمز للموزع &rarr;</a>
        </div>
      </div>
    </div></section>

  <section class="section" id="calculator">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">حاسبة مكافأة <span class="text-gradient-gold">Stake.com</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">حرِّك المزلق. الحسابات دقيقة: إيداع بين <bdi dir="ltr">$10</bdi> و<bdi dir="ltr">$1,500</bdi>، 200% مطابقة حتى <bdi dir="ltr">$3,000</bdi> مكافأة، شرط رهان 40x على المجموع.</p>
      </div>
      <div class="bonus-calc">
        <h3>مبلغ أول إيداع في <bdi dir="ltr">Stake.com</bdi></h3>
        <div class="bonus-calc-input">
          <label for="depAmount">مبلغ الإيداع (USD)</label>
          <input type="range" id="depRange" min="10" max="1500" step="10" value="500">
          <input type="number" id="depAmount" min="10" max="1500" step="10" value="500">
        </div>
        <div class="bonus-calc-row">
          <div class="stat">
            <p class="stat-label">المكافأة المُضافة</p>
            <p class="stat-value" id="bonusOut"><bdi dir="ltr">$1,000</bdi></p>
            <p class="stat-sub">200% من الإيداع، بحد أقصى <bdi dir="ltr">$3,000</bdi></p>
          </div>
          <div class="stat">
            <p class="stat-label">شرط الرهان</p>
            <p class="stat-value" id="wagerOut"><bdi dir="ltr">$60,000</bdi></p>
            <p class="stat-sub">(إيداع + مكافأة) × 40</p>
          </div>
          <div class="stat">
            <p class="stat-label">إجمالي الرصيد القابل للعب</p>
            <p class="stat-value" id="totalOut"><bdi dir="ltr">$1,500</bdi></p>
            <p class="stat-sub">رصيد الحساب بعد الاسترداد</p>
          </div>
          <div class="stat">
            <p class="stat-label">كفاءة المطابقة</p>
            <p class="stat-value" id="effOut">200%</p>
            <p class="stat-sub">ينخفض دون 200% إذا تجاوز الإيداع <bdi dir="ltr">$1,500</bdi></p>
          </div>
        </div>
        <p class="bonus-calc-footer"><strong style="color:var(--gold);">الحد الأقصى للمكافأة <bdi dir="ltr">$3,000</bdi>.</strong> أودع <bdi dir="ltr">$1,500</bdi> لتحصل على الكامل. الإيداع فوق <bdi dir="ltr">$1,500</bdi> يُعالَج لكن المكافأة لا تزيد.</p>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="bonus-calc-cta">احصل على <bdi dir="ltr">MAX3000</bdi> في <bdi dir="ltr">Stake.com</bdi> &rarr;</a>
      </div>
      <div class="eligibility-grid">
        <div class="item"><strong>العمر</strong><span>18+ (21+ في بعض المناطق)</span></div>
        <div class="item"><strong>نوع العميل</strong><span>عملاء جدد، أول إيداع فقط</span></div>
        <div class="item"><strong>الإيداع الأدنى</strong><span><bdi dir="ltr">$10 USD</bdi> أو ما يعادله من عملات رقمية</span></div>
        <div class="item"><strong>الحد الأقصى للمكافأة</strong><span><bdi dir="ltr">$3,000</bdi> (عند إيداع <bdi dir="ltr">$1,500</bdi>)</span></div>
        <div class="item"><strong>KYC</strong><span>مستوى 3 مطلوب قبل صرف المكافأة</span></div>
        <div class="item"><strong>طريقة الاسترداد</strong><span>تواصل مع الدعم المباشر بعد أول إيداع</span></div>
        <div class="item"><strong>وقت الصرف</strong><span>24-48 ساعة بعد تحقق الفريق من الأهلية</span></div>
        <div class="item"><strong>تتبع التقدم</strong><span>تبويب VIP يعرض تقدم شرط الرهان</span></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">مساعدة Stake، مكافأة الترحيب</a> &middot; <a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">مساعدة Stake، مستويات KYC</a> &middot; <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com، شروط MAX3000</a></p>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مقارنة رموز <span class="text-gradient-gold">Stake</span> النشطة</h2><p class="section-subtitle">سبعة رموز، فائز واحد. لماذا يوصي النادي بـ<bdi dir="ltr">MAX3000</bdi> فقط.</p></div>
      <table class="data-table" style="max-width:100%;overflow-x:auto;display:block;">
        <thead><tr><th>الرمز</th><th>المطابقة %</th><th>الحد الأقصى</th><th>الإيداع الأدنى</th><th>ملاحظة</th></tr></thead>
        <tbody>
          <tr class="win"><td><strong><bdi dir="ltr">MAX3000</bdi></strong></td><td>200%</td><td><bdi dir="ltr">$3,000</bdi></td><td><bdi dir="ltr">$10</bdi></td><td>رمز النادي. الدعم المباشر يُضيف 200% يدوياً، شرط رهان 40x.</td></tr>
          <tr><td><bdi dir="ltr">NEWBONUS</bdi></td><td>200%</td><td><bdi dir="ltr">$3,000</bdi></td><td><bdi dir="ltr">$10</bdi></td><td>رمز عام متاح، يعمل على جميع المرايا.</td></tr>
          <tr><td><bdi dir="ltr">HELLA200</bdi></td><td>200%</td><td><bdi dir="ltr">$3,000</bdi></td><td><bdi dir="ltr">$50</bdi></td><td>حد إيداع أدنى أعلى. بدون سبينات.</td></tr>
          <tr><td><bdi dir="ltr">STRAFECASVIP</bdi></td><td>200%</td><td><bdi dir="ltr">$2,000</bdi></td><td><bdi dir="ltr">$10</bdi></td><td>شراكة Strafe. الحد أقل بـ<bdi dir="ltr">$1,000</bdi> من MAX3000.</td></tr>
          <tr><td><bdi dir="ltr">HELLAGOOD</bdi></td><td>لا</td><td>لا</td><td>لا</td><td>rakeback فقط 5%. بدون مطابقة إيداع.</td></tr>
          <tr><td><bdi dir="ltr">HELLAFREE</bdi></td><td>لا</td><td><bdi dir="ltr">$1</bdi> بدون إيداع</td><td>لا</td><td><bdi dir="ltr">$1</bdi> مجاني بعد KYC. قيمة ضعيفة.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">خطوات <span class="text-gradient-gold">الاسترداد</span></h2><p class="section-subtitle">تسجيل، تحقق، إيداع، إخبار الدعم المباشر بـ<bdi dir="ltr">MAX3000</bdi>. المكافأة تُضاف يدوياً من المشغِّل.</p></div>
      {step_cards([
        ('1. افتح الباب', f'انتقل إلى <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener">Stake.com عبر رابط الشراكة</a> واضغط تسجيل. بريد إلكتروني، اسم مستخدم، كلمة مرور، تاريخ ميلاد.'),
        ('2. أكمل المستوى 3', 'تشترط <bdi dir="ltr">Stake</bdi> <strong>KYC مستوى 3</strong> قبل صرف المكافأة. ارفع هويتك المصوَّرة وإثبات العنوان ووثائق مستوى 3 الإضافية. عرض الترحيب مشروط باجتياز هذه المرحلة.'),
        ('3. أودع أول مرة (10$ فأكثر)', 'أودع بين <bdi dir="ltr">$10</bdi> و<bdi dir="ltr">$1,500</bdi>. 200% مطابقة تتناسب مع حد مكافأة <bdi dir="ltr">$3,000</bdi>. الإيداع فوق <bdi dir="ltr">$1,500</bdi> يُعالَج لكن المكافأة لا تزيد.'),
        ('4. اطلب MAX3000 عبر الدعم المباشر', 'بعد تأكيد الإيداع، افتح الدعم المباشر لـ<bdi dir="ltr">Stake</bdi> وأخبرهم أنك سجَّلت بـ<span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> وتريد مكافأة الترحيب. بعد التحقق تصل 200% خلال <strong>24-48 ساعة</strong>.'),
      ])}
      <div class="club-body" style="margin-top:32px;padding:20px;background:var(--elevated);border-radius:10px;border-right:3px solid var(--gold);">
        <p style="margin:0;font-size:14px;color:var(--text-dim);"><strong style="color:var(--gold);">مهم:</strong> مكافأة الترحيب في <bdi dir="ltr">Stake.com</bdi> ليست خانة إدخال تلقائية، بل رصيد يُضاف يدوياً. سجِّل عبر رابط الشراكة، أكمل KYC مستوى 3، أودع، ثم افتح الدعم المباشر وأخبرهم بـ<bdi dir="ltr">MAX3000</bdi>. تتبع التقدم (الإيداع + المكافأة) × 40 من <strong>تبويب VIP</strong> بعد التفعيل.</p>
      </div>
    </div>
  </section>

  {girl_break('أكبر رمز <span class="text-gradient-gold">في الصالة</span>', 'همس <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للموزع. 200% حتى <bdi dir="ltr">$3,000</bdi> في Stake.com، الدعم المباشر يتولى الباقي.', 'سلِّم الرمز للموزع', 'girl-promo')}

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العروض الدائمة: <span class="text-gradient-gold">700,000$+ أسبوعياً</span></h2><p class="section-subtitle">عرض الترحيب مجرد بداية. Stake توزع أكثر من 700,000 دولار أسبوعياً على اللاعبين القائمين.</p></div>
      {club_cards([
        ('سباق يومي $100,000', 'تسجيل تلقائي لجميع اللاعبين المسجَّلين، لا حاجة للتسجيل المنفصل. العب ألعاب الكازينو لتجمع نقاط المتصدرين. بعد 24 ساعة، أفضل 5,000 لاعب يتقاسمون $100,000. السباق يُعيد ضبط نفسه باستمرار.'),
        ('سحب أسبوعي $75,000', 'تذكرة لكل $1,000 تراهن خلال فترة الأهلية. لا تسجيل مطلوب. $75,000 تُوزَّع كل سبت في بث مباشر. لا حد أقصى لتراكم التذاكر.'),
        ('فتح الكازينو $50,000', 'بعثات أسبوعية في العناوين الجديدة والمميزة. رهان أدنى €0.10. $50,000 أسبوعياً تتوزع بين أكبر الراهنين وإسقاطات جوائز عشوائية.'),
        ('Pragmatic Drops & Wins', 'يُشغِّل Stake حملة شبكة Pragmatic Play الرائدة. Sweet Bonanza وGates of Olympus 1000 وSugar Rush وغيرها. جوائز تتساقط عشوائياً خلال سبينات المال الحقيقي. 50,000+ جائزة أسبوعياً عبر الشبكة.'),
        ('تأمين الرياضة', 'عروض تأمين مرتبطة بالأحداث: NHL صرف مبكر عند تقدم بهدفين، NBA تسوية في الشوط الأول عند التقدم بـ12+ نقطة، حماية باقة Stake Shield، استرداد السباقات. تتناوب حسب التقويم الرياضي.'),
        ('مكافأة إعادة تعبئة VIP', 'VIP من مستوى Platinum فصاعداً يحصل على مكافآت إعادة تعبئة، Platinum I كل 14 يوماً، Platinum IV في أي وقت. المبالغ مُرجَّحة بالخسائر الأخيرة.'),
      ])}
    </div>
  </section>

  {faq_section(faqs)}'''

    extra_scripts = '''  <script>
    (function(){
      var range=document.getElementById('depRange');
      var num=document.getElementById('depAmount');
      var bonusOut=document.getElementById('bonusOut');
      var wagerOut=document.getElementById('wagerOut');
      var totalOut=document.getElementById('totalOut');
      var effOut=document.getElementById('effOut');
      if(!range||!num) return;
      var fmt=function(n){return '$'+Math.round(n).toLocaleString('en-US');};
      function recalc(){
        var dep=parseFloat(num.value);
        if(isNaN(dep)||dep<10) dep=10;
        if(dep>1500) dep=1500;
        num.value=dep; range.value=dep;
        var bonus=Math.min(dep*2,3000);
        var total=dep+bonus;
        var wager=total*40;
        var eff=(bonus/dep)*100;
        bonusOut.textContent=fmt(bonus);
        wagerOut.textContent=fmt(wager);
        totalOut.textContent=fmt(total);
        effOut.textContent=Math.round(eff)+'%';
      }
      range.addEventListener('input',function(){num.value=range.value;recalc();});
      num.addEventListener('input',recalc);
      num.addEventListener('change',recalc);
      recalc();
    })();
  </script>'''

    return page_template(
        title='رمز Stake الترويجي MAX3000 - مكافأة 200% حتى $3,000 عند التسجيل',
        description='الرمز الترويجي لـ Stake.com هو MAX3000. أول إيداع 200% مطابقة حتى $3,000، شرط رهان 40x على الإيداع والمكافأة، KYC مستوى 3 مطلوب. تحقق يونيو 2026.',
        canonical_path='ar/promo-code/',
        og_url_path='ar/promo-code/',
        og_image='promo-code.png',
        hreflang_slug='promo-code/',
        hreflang_en_path='promo-code/',
        jsonld_extra=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage","name":"رمز Stake الترويجي MAX3000 - مكافأة 200% حتى $3,000","description":"الرمز MAX3000، 200% مطابقة حتى $3,000، شرط رهان 40x، KYC مستوى 3 مطلوب.","url":"https://winnersclub.com/ar/promo-code/"}}</script>\n<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Offer","name":"رمز Stake الترويجي MAX3000","description":"200% مطابقة حتى $3,000 مكافأة. إيداع أدنى $10، إيداع مؤهِّل أقصى $1,500. شرط رهان 40x على الإيداع والمكافأة. KYC مستوى 3 مطلوب.","url":"https://winnersclub.com/ar/promo-code/","priceCurrency":"USD","price":"0","seller":{{"@type":"Organization","name":"Stake.com"}}}}</script>\n' + faq_ld,
        page_bc_name='الرمز الترويجي',
        page_bc_url='ar/promo-code/',
        hero_tease='إذا وجدت هذه الصفحة، وجدت الرمز.',
        h1_main='الرمز الترويجي لـ Stake.com هو MAX3000',
        h1_sub='200% حتى $3,000 مطابقة في Stake.com.',
        hero_sub_html='الرمز هو <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. أول إيداع 200% مطابقة حتى <bdi dir="ltr">$3,000</bdi> مكافأة. شرط رهان 40x على الإيداع والمكافأة. KYC مستوى 3 للاسترداد. اللاعبون الأمريكيون لديهم <a href="/ar/stake-us-bonus/" style="color:var(--gold);text-decoration:underline;">ترحيب Stake.us</a> منفصل بنفس الرمز.',
        hero_img='girl-promo',
        body_html=body,
        sticky_text='الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. 200% / <bdi dir="ltr">$3,000</bdi>. تواصل مع الدعم المباشر بعد الإيداع.',
        extra_scripts=extra_scripts,
        page_slug='promo-code',
    )


def build_casino():
    faqs = [
        ('كم عدد الألعاب في كازينو <bdi dir="ltr">Stake</bdi>؟', 'أكثر من 3000 لعبة كازينو بما فيها سلوتس ولعب طاولة وكازينو مباشر وألعاب أصلية. يُضيف <bdi dir="ltr">Stake</bdi> عناوين جديدة أسبوعياً.'),
        ('هل الكازينو المباشر متاح؟', 'نعم. <bdi dir="ltr">Stake</bdi> يُشغِّل طاولات بلاك جاك وروليت وباكاراه وبوكر مباشرة مع موزعين بشريين حقيقيين. متاح على مدار الساعة.'),
        ('هل يمكنني استخدام <bdi dir="ltr">MAX3000</bdi> في الكازينو؟', 'نعم. مكافأة الترحيب 200% حتى <bdi dir="ltr">$3,000</bdi> تُطبَّق عبر كازينو Stake وسبورت بوك وبوكر. ألعاب الكازينو بهامش بيت أعلى من 4% تُسهم 100% في شرط الرهان.'),
        ('ما ألعاب Originals؟', 'Originals هي ألعاب حصرية طوَّرها <bdi dir="ltr">Stake</bdi> داخلياً: Crash وDice وLimbo وMines وKeno وPlinko وغيرها. RNG مُتحقق منه بشكل عادل، يمكنك التحقق من كل جولة. تُسهم 100% في شرط الرهان.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">غرفة <span class="text-gradient-gold">الكازينو</span></h2></div>
      {club_cards([
        ('+3000 لعبة', 'سلوتس ولعب طاولة وكازينو مباشر وأصلية. موردون كبار: Pragmatic Play وEvolution وHacksawGaming وNetEnt وPlay\'n GO. عناوين جديدة تُضاف أسبوعياً.'),
        ('RTP وهامش البيت', 'ألعاب <bdi dir="ltr">Stake Originals</bdi> بـ RNG مُتحقق منه بشكل عادل. هامش البيت في Dice 1%، Limbo 1%، Crash 1%. معظم السلوتس بـ RTP من 94% إلى 97%.'),
        ('الكازينو المباشر', 'بلاك جاك ورولیت وباكاراه وبوكر مع موزعين بشريين على مدار الساعة. دولة أوروبية وآسيوية ومزودون مميزون. أكثر من 100 طاولة في وقت الذروة.'),
        ('أصليات <bdi dir="ltr">Stake</bdi>', 'Crash وDice وLimbo وMines وKeno وPlinko وHilo وWheelحصرية لـ<bdi dir="ltr">Stake</bdi>. كل جولة مُتحقق منها. تُسهم 100% في شرط رهان <bdi dir="ltr">MAX3000</bdi>.'),
        ('مكافأة <bdi dir="ltr">MAX3000</bdi>', 'استخدم الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للحصول على 200% حتى <bdi dir="ltr">$3,000</bdi>. ألعاب الكازينو هي الأمثل لاستيفاء شرط الرهان. ألعاب بهامش بيت 4%+ تُسهم 100%.'),
        ('الدعم المباشر', 'دعم على مدار الساعة عبر الدردشة المباشرة. متاح بالعربية وعشرات اللغات الأخرى. الفريق يتولى استرداد <bdi dir="ltr">MAX3000</bdi> يدوياً خلال 24-48 ساعة.'),
      ])}
    </div>
  </section>
  {girl_break('أكثر من <span class="text-gradient-gold">3000 لعبة.</span> رمز واحد.', 'الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. اختر لعبتك وابدأ.', 'افتح الكازينو', 'girl-casino')}
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العروض الدائمة في <span class="text-gradient-gold">الكازينو</span></h2></div>
      {club_cards([
        ('سباق يومي $100,000', 'تسجيل تلقائي لجميع اللاعبين. العب وأكسب نقاط المتصدرين. أفضل 5,000 لاعب يتقاسمون $100,000 كل 24 ساعة.'),
        ('Pragmatic Drops & Wins', 'Sweet Bonanza وGates of Olympus 1000 وSugar Rush. جوائز تتساقط عشوائياً. 50,000+ جائزة أسبوعياً عبر الشبكة.'),
        ('فتح الكازينو $50,000', 'بعثات أسبوعية في العناوين الجديدة. رهان أدنى €0.10. $50,000 أسبوعياً بين أكبر الراهنين وإسقاطات عشوائية.'),
        ('مكافأة إعادة التعبئة', 'VIP من Platinum فصاعداً يحصل على مكافآت دورية. المبالغ مُرجَّحة بالخسائر الأخيرة.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''

    return page_template(
        title='كازينو Stake - أكثر من 3000 لعبة مع الرمز MAX3000',
        description='كازينو Stake.com: 3000+ لعبة، سلوتس وطاولات وكازينو مباشر وأصلية. الرمز MAX3000 يفتح 200% حتى $3,000 مع شرط رهان 40x.',
        canonical_path='ar/casino/',
        og_url_path='ar/casino/',
        og_image='casino.png',
        hreflang_slug='casino/',
        hreflang_en_path='casino/',
        jsonld_extra=faq_ld,
        page_bc_name='كازينو',
        page_bc_url='ar/casino/',
        hero_tease='3000+ لعبة تنتظر من يعرف الرمز.',
        h1_main='كازينو Stake مع الرمز MAX3000',
        h1_sub='أكثر من 3000 لعبة في صالة واحدة.',
        hero_sub_html='كازينو <bdi dir="ltr">Stake</bdi> يضم أكثر من 3000 لعبة: سلوتس وطاولات وكازينو مباشر وأصلية. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح <strong>200% حتى <bdi dir="ltr">$3,000</bdi></strong> مع شرط رهان 40x. ألعاب الكازينو بهامش بيت 4%+ تُسهم 100% في شرط الرهان.',
        hero_img='girl-casino',
        body_html=body,
        page_slug='casino',
    )

def build_sports():
    faqs = [
        ('هل Stake تُغطي الكرة الأقدام؟', 'نعم. <bdi dir="ltr">Stake</bdi> يغطي أكثر من 40 دوري كرة قدم عالمياً شاملاً الدوري الإنجليزي الممتاز والليغا واللاليغا والسيريه A ودوري الأبطال وغيرها. تُتيح رهانات مسبقة ومباشرة وباني باقات.'),
        ('ما حصة الرياضة في شرط الرهان؟', 'رهانات الرياضة تُسهم 75% في شرط رهان <bdi dir="ltr">MAX3000</bdi>. مثال: إيداع <bdi dir="ltr">$500</bdi> + مكافأة <bdi dir="ltr">$1,000</bdi> = مجموع <bdi dir="ltr">$1,500</bdi> × 40 = حاجة إلى <bdi dir="ltr">$80,000</bdi> رهان رياضي لاستيفاء الشرط بالكامل عبر الرياضة وحدها.'),
        ('هل الرهان المباشر متاح؟', 'نعم. <bdi dir="ltr">Stake</bdi> يُتيح رهانات مباشرة شاملة على الكرة الأقدام والتنس والبيسبول والـ NBA وغيرها. الخطوط تتحدث باستمرار خلال المباريات.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المراهنات <span class="text-gradient-gold">الرياضية</span></h2></div>
      {club_cards([
        ('40+ دوري عالمي', 'الدوري الإنجليزي الممتاز والليغا واللاليغا والسيريه A ودوري الأبطال. أيضاً NBA وNFL وNHL وMLB والتنس والكريكيت وe-sports.'),
        ('رهان مباشر', 'الخطوط تتحدث لحظياً خلال المباريات. رهانات المباشر على النتائج والهداف التالي والركلات الحرة ومئات الأسواق الأخرى.'),
        ('باني الباقات', 'ادمج أحداثاً متعددة في باقة واحدة. تُسهم رهانات الرياضة بـ75% في شرط رهان <bdi dir="ltr">MAX3000</bdi>. حماية Stake Shield للباقات.'),
        ('عروض الرياضة', 'NHL صرف مبكر عند تقدم بهدفين، NBA تسوية في الشوط الأول، استرداد الملاكمة عند قرار المحكمين، ماني باك سباقات الخيل.'),
        ('الرمز <bdi dir="ltr">MAX3000</bdi>', 'مكافأة الترحيب 200% حتى <bdi dir="ltr">$3,000</bdi> تشمل رهانات الرياضة. الرياضة تُسهم 75% مقابل 100% لألعاب الكازينو.'),
        ('Stake.us للأمريكيين', 'الولايات المتحدة محجوبة من <bdi dir="ltr">Stake.com</bdi>. <bdi dir="ltr">Stake.us</bdi> نموذج سحوبات بدون رياضة. <bdi dir="ltr">MAX3000</bdi> يعمل على كلا المنصتين.'),
      ])}
    </div>
  </section>
  {girl_break('40+ دوري. <span class="text-gradient-gold">رهان واحد.</span>', 'الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. العب الرياضة والكازينو بنفس المكافأة.', 'راهن الآن', 'girl-sports')}
  {faq_section(faqs)}'''

    return page_template(
        title='مراهنات Stake الرياضية - 40+ دوري مع الرمز MAX3000',
        description='سبورت بوك Stake.com: 40+ دوري، رهان مباشر، باني باقات، عروض رياضية دورية. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/sports/',
        og_url_path='ar/sports/',
        og_image='sports.png',
        hreflang_slug='sports/',
        hreflang_en_path='sports/',
        jsonld_extra=faq_ld,
        page_bc_name='الرياضة',
        page_bc_url='ar/sports/',
        hero_tease='أكثر من 40 دوري. رهانات مباشرة. مكافأة واحدة.',
        h1_main='المراهنات الرياضية في Stake مع MAX3000',
        h1_sub='40+ دوري، رهان مباشر، باني باقات.',
        hero_sub_html='سبورت بوك <bdi dir="ltr">Stake</bdi> يغطي الكرة الأقدام والـ NBA والتنس والـ NFL والـ NHL وأكثر. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. رهانات الرياضة تُسهم بـ75% في شرط الرهان.',
        hero_img='girl-sports',
        body_html=body,
        page_slug='sports',
    )


def build_poker():
    faqs = [
        ('هل بوكر Stake حقيقي؟', 'نعم. <bdi dir="ltr">Stake</bdi> يُشغِّل موقع بوكر كامل الميزات مع Cash Games وSit & Go وMulti-Table Tournaments. اللاعبون يلعبون ضد بعضهم، ليس ضد البيت.'),
        ('ما العملات المقبولة في البوكر؟', 'كل العملات الرقمية المدعومة في <bdi dir="ltr">Stake</bdi> تعمل في البوكر: BTC وETH وLTC وXRP وSOL وTRX وBNB وغيرها. أيضاً العملات الورقية عبر MoonPay.'),
        ('هل الرمز MAX3000 يعمل في البوكر؟', 'نعم. مكافأة 200% حتى <bdi dir="ltr">$3,000</bdi> تُطبَّق عبر منصة Stake كاملة بما فيها البوكر. أرباح البوكر (rake) لها حصة مختلفة في شرط الرهان.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">غرفة <span class="text-gradient-gold">البوكر</span></h2></div>
      {club_cards([
        ('Cash Games', 'طاولات No-Limit Hold\'em وPot-Limit Omaha بحصص متعددة. دخول وخروج في أي وقت. حصة المائدة (rake) تنافسية.'),
        ('Sit & Go', 'بطولات فورية بجداول ثابتة. من 2 لاعبين إلى 9. تبدأ فور اكتمال الطاولة. مناسبة للجلسات القصيرة.'),
        ('بطولات متعددة الطاولات', 'MTT بجوائز مضمونة، Satellites للبطولات الكبرى. مناسبة لمن يبحث عن جوائز أعلى.'),
        ('التحقق من النزاهة', 'كل يد في بوكر <bdi dir="ltr">Stake</bdi> قابلة للتحقق. السيد ما زال في طور التطوير لكن <bdi dir="ltr">Stake</bdi> يلتزم بمبدأ الشفافية.'),
        ('الرمز <bdi dir="ltr">MAX3000</bdi>', '200% حتى <bdi dir="ltr">$3,000</bdi> على أول إيداع. استخدم المكافأة على طاولات البوكر. احسب شرط الرهان قبل البدء.'),
        ('دعم متعدد اللغات', 'الدعم المباشر متاح بالعربية وعشرات اللغات. الفريق يتولى استرداد <bdi dir="ltr">MAX3000</bdi> خلال 24-48 ساعة.'),
      ])}
    </div>
  </section>
  {girl_break('البوكر <span class="text-gradient-gold">في Stake.</span> رمز واحد.', 'الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. Cash Games وبطولات تنتظر.', 'انضم لطاولة البوكر', 'girl-poker')}
  {faq_section(faqs)}'''
    return page_template(
        title='بوكر Stake - Cash Games وبطولات مع الرمز MAX3000',
        description='بوكر Stake.com: Cash Games وSit & Go وبطولات متعددة. الرمز MAX3000 يفتح 200% حتى $3,000 على أول إيداع.',
        canonical_path='ar/poker/',
        og_url_path='ar/poker/',
        og_image='poker.png',
        hreflang_slug='poker/',
        hreflang_en_path='poker/',
        jsonld_extra=faq_ld,
        page_bc_name='بوكر',
        page_bc_url='ar/poker/',
        hero_tease='الطاولة جاهزة. الرمز في يدك.',
        h1_main='بوكر Stake مع الرمز MAX3000',
        h1_sub='Cash Games وبطولات وSit & Go.',
        hero_sub_html='بوكر <bdi dir="ltr">Stake</bdi> يُقدِّم Cash Games وSit & Go وبطولات متعددة الطاولات. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi> على أول إيداع.',
        hero_img='girl-poker',
        body_html=body,
        page_slug='poker',
    )

def build_aviator():
    faqs = [
        ('ما لعبة Aviator؟', 'Aviator لعبة كراش من إنتاج Spribe. مضارب يطير ويرتفع مُضاعف الربح. تصرف قبل الانهيار. مضاعفات تصل إلى 10,000x.'),
        ('هل Aviator عادلة؟', 'Aviator من Spribe تستخدم بروتوكول Provably Fair قائم على cryptographic seed مشترك. كل جولة قابلة للتحقق.'),
        ('هل يمكنني لعب Aviator مع مكافأة MAX3000؟', 'نعم. مكافأة الترحيب 200% حتى <bdi dir="ltr">$3,000</bdi> تُطبَّق على Aviator. هامش بيت اللعبة ~3%. تحقق من نسبة مساهمتها في شرط الرهان.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لعبة <span class="text-gradient-gold">أفياتور</span></h2></div>
      {club_cards([
        ('ميكانيكية الكراش', 'مضارب يطير ومُضاعف الربح يرتفع. تصرف في أي وقت لحجز ربحك. انتظر طويلاً للحصول على مضاعف أكبر لكن احذر الانهيار. مضاعفات تصل إلى 10,000x.'),
        ('Provably Fair', 'من إنتاج Spribe. بروتوكول التحقق يعتمد على seed مشترك بين اللاعب والخادم. كل جولة قابلة للتحقق على موقع Stake.'),
        ('رهانات مزدوجة', 'ضع رهانَين في آنٍ واحد. اسحب الأول مبكراً لتأمين ربح صغير والثاني ابقه للمضاعف الكبير. استراتيجية شائعة.'),
        ('إحصاءات مباشرة', 'Stake يعرض أكبر فوز في آخر 500 جولة والجولات المرتفعة الأخيرة ورهانات الآخرين مباشرة.'),
        ('الرمز <bdi dir="ltr">MAX3000</bdi>', '200% حتى <bdi dir="ltr">$3,000</bdi> على أول إيداع. استخدم المكافأة في Aviator. هامش البيت ~3% يجعلها من الألعاب الجيدة لشرط الرهان.'),
        ('التوافق', 'Aviator تعمل على المتصفح والهاتف. لا تطبيق منفصل مطلوب. سرعة الرسم والإخراج الرقمي تجعلها مناسبة للاتصالات المتوسطة.'),
      ])}
    </div>
  </section>
  {girl_break('الطائرة ترتفع. <span class="text-gradient-gold">متى تسحب؟</span>', 'الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. العب Aviator مع مكافأة الترحيب.', 'العب Aviator', 'girl-aviator')}
  {faq_section(faqs)}'''
    return page_template(
        title='Aviator في Stake - لعبة الكراش مع الرمز MAX3000',
        description='Aviator في Stake.com: لعبة كراش من Spribe بتحقق Provably Fair. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/aviator/',
        og_url_path='ar/aviator/',
        og_image='aviator.png',
        hreflang_slug='aviator/',
        hreflang_en_path='aviator/',
        jsonld_extra=faq_ld,
        page_bc_name='أفياتور',
        page_bc_url='ar/aviator/',
        hero_tease='المضاعف يرتفع. الرمز في يدك.',
        h1_main='لعبة Aviator في Stake مع MAX3000',
        h1_sub='الكراش الأكثر شهرة في المنصة.',
        hero_sub_html='Aviator من Spribe في <bdi dir="ltr">Stake</bdi>: مضارب يطير ومضاعف يرتفع. اسحب قبل الانهيار. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        hero_img='girl-aviator',
        body_html=body,
        page_slug='aviator',
    )

def build_live_casino():
    faqs = [
        ('هل الكازينو المباشر متاح على مدار الساعة؟', 'نعم. طاولات <bdi dir="ltr">Stake</bdi> المباشرة تعمل على مدار الساعة طوال الأسبوع مع موزعين حقيقيين.'),
        ('من هم الموردون؟', '<bdi dir="ltr">Stake</bdi> يشتغل مع Evolution وPragmatic Play Live وEzugi. توفر هذه الموردون أكبر تغطية للعاب الطاولة المباشرة.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الكازينو <span class="text-gradient-gold">المباشر</span></h2></div>
      {club_cards([
        ('بلاك جاك مباشر', 'عشرات طاولات البلاك جاك بحصص متنوعة. طاولات VIP بحصص عالية. من €1 إلى آلاف الدولارات لكل يد.'),
        ('رولیت مباشر', 'رولیت أوروبية وأمريكية وفرنسية. Speed Roulette وLightning Roulette من Evolution. تتبع الإحصاءات مباشرة على الشاشة.'),
        ('باكاراه مباشر', 'Classic Baccarat وSpeed Baccarat وBaccarat Squeeze. رهانات منخفضة ومرتفعة. يُفضَّل لدى اللاعبين الآسيويين.'),
        ('بوكر مباشر', 'Casino Hold\'em وThree Card Poker وUltimate Texas Hold\'em. راهن ضد الموزع لا ضد لاعبين آخرين.'),
        ('ألعاب Game Show', 'Crazy Time وMonopoly Live وDeal or No Deal وMega Ball من Evolution. ترفيه مباشر بمضاعفات ضخمة.'),
        ('الرمز <bdi dir="ltr">MAX3000</bdi>', 'مكافأة الترحيب تُطبَّق في الكازينو المباشر. تحقق من نسبة مساهمة ألعاب المباشر في شرط الرهان.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='الكازينو المباشر في Stake - موزعون حقيقيون مع MAX3000',
        description='الكازينو المباشر في Stake.com: بلاك جاك ورولیت وباكاراه وبوكر مع موزعين بشريين. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/live-casino/',
        og_url_path='ar/live-casino/',
        og_image='live-casino.png',
        hreflang_slug='live-casino/',
        hreflang_en_path='live-casino/',
        jsonld_extra=faq_ld,
        page_bc_name='الكازينو المباشر',
        page_bc_url='ar/live-casino/',
        hero_tease='موزعون حقيقيون. طاولات مفتوحة الآن.',
        h1_main='الكازينو المباشر في Stake',
        h1_sub='بلاك جاك ورولیت وباكاراه 24/7.',
        hero_sub_html='كازينو <bdi dir="ltr">Stake</bdi> المباشر يُتيح بلاك جاك ورولیت وباكاراه وألعاب Game Show مع موزعين حقيقيين على مدار الساعة. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        hero_img='girl-casino',
        body_html=body,
        page_slug='live-casino',
    )


def build_live_odds():
    faqs = [
        ('كيف أقرأ الأوفياء في Stake؟', '<bdi dir="ltr">Stake</bdi> يعرض الأوفياء بصيغة عشرية (1.90)، كسرية (9/10)، وأمريكية (-111). اختر تنسيقك من إعدادات الحساب.'),
        ('هل الرهان المباشر متاح؟', 'نعم. <bdi dir="ltr">Stake</bdi> يُتيح رهانات مباشرة (In-Play) مع تحديثات لحظية للأوفياء خلال المباريات.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الأوفياء <span class="text-gradient-gold">المباشرة</span></h2></div>
      {club_cards([
        ('أوفياء مسبقة ومباشرة', 'راهن قبل الحدث أو خلاله. الأوفياء تتحدث لحظياً. أسواق المباشر تشمل نتيجة الشوط التالي والهداف التالي والكثير.'),
        ('تنسيقات الأوفياء', 'عشرية وكسرية وأمريكية. غيِّر التنسيق من الإعدادات. معظم اللاعبين العرب يفضلون العشرية.'),
        ('تغطية رياضية واسعة', 'الكرة الأقدام والتنس والـ NBA والـ NHL والـ NFL والكريكيت والـ e-sports والغولف وأكثر.'),
        ('باني الباقات', 'ادمج أحداثاً متعددة. المضاعف يرتفع مع كل إضافة. حماية Stake Shield لإنقاذ باقة خسرت لعبة واحدة.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='الأوفياء المباشرة في Stake - رهانات رياضية مع MAX3000',
        description='أوفياء Stake المباشرة: 40+ رياضة، رهان مسبق ومباشر، باني باقات. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/live-odds/',
        og_url_path='ar/live-odds/',
        og_image='live-odds.png',
        hreflang_slug='live-odds/',
        hreflang_en_path='live-odds/',
        jsonld_extra=faq_ld,
        page_bc_name='الأوفياء المباشرة',
        page_bc_url='ar/live-odds/',
        hero_tease='الأوفياء تتحدث. الرمز جاهز.',
        h1_main='الأوفياء المباشرة في Stake',
        h1_sub='رهانات رياضية مسبقة ومباشرة.',
        hero_sub_html='<bdi dir="ltr">Stake</bdi> يُتيح رهانات رياضية مسبقة ومباشرة على 40+ رياضة. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. رهانات الرياضة تُسهم 75% في شرط الرهان.',
        hero_img='girl-lucky-drive',
        body_html=body,
        page_slug='live-odds',
    )

def build_originals():
    faqs = [
        ('ما هي Stake Originals؟', 'Stake Originals ألعاب طوَّرتها <bdi dir="ltr">Stake</bdi> داخلياً. Crash وDice وLimbo وMines وKeno وPlinko وHilo والعجلة. كلها بـ RNG مُتحقق منه بشكل عادل.'),
        ('هل Originals Provably Fair؟', 'نعم. كل جولة في Stake Originals يمكن التحقق منها. يعتمد على seed مشترك بين اللاعب والخادم. هامش بيت Dice و Limbo 1%.'),
        ('هل يمكن لعب Originals مع MAX3000؟', 'نعم. Originals تُسهم 100% في شرط رهان <bdi dir="ltr">MAX3000</bdi>. هامش البيت المنخفض يجعلها من أفضل الخيارات لاستيفاء الشرط.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أصليات <span class="text-gradient-gold">Stake</span></h2></div>
      {club_cards([
        ('Crash', 'مضارب يطير ومُضاعف يرتفع. تصرف قبل الانهيار. مضاعفات حتى 1,000,000x. إحصاءات مباشرة ورهانات الآخرين مرئية.'),
        ('Dice', 'تنبأ بنتيجة رمية النرد. اضبط احتمالية الفوز (1% إلى 98%). هامش بيت 1%. بسيطة وفعالة.'),
        ('Limbo', 'رمية رقم عشوائي بين 1 وما لا نهاية. اضبط المُضاعف المستهدف. هامش 1%. سريعة ومثيرة.'),
        ('Mines', 'شبكة 5×5 مخفية فيها ألغام. اكشف المربعات بأمان واجمع الأرباح. كلما أبعدت كشفت ارتفع المُضاعف.'),
        ('Plinko', 'كرة تتساقط على مسمار وتُوزَّع في حواجز ومسارات. ارتفاع المُضاعف مرتبط بالجوانب. ميكانيكية بسيطة مُسلية.'),
        ('Keno', 'اختر أرقاماً من 40. 20 رقماً تُسحب عشوائياً. كلما تطابقت أكثر كلما ارتفع المُضاعف.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='Stake Originals - ألعاب حصرية بـ Provably Fair مع MAX3000',
        description='Stake Originals: Crash وDice وLimbo وMines وKeno وPlinko. RNG مُتحقق منه بشكل عادل. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/originals/',
        og_url_path='ar/originals/',
        og_image='originals.png',
        hreflang_slug='originals/',
        hreflang_en_path='originals/',
        jsonld_extra=faq_ld,
        page_bc_name='الأصليات',
        page_bc_url='ar/originals/',
        hero_tease='ألعاب لن تجدها في أي مكان آخر.',
        h1_main='Stake Originals - ألعاب حصرية',
        h1_sub='Crash وDice وLimbo وMines وPlinko.',
        hero_sub_html='<bdi dir="ltr">Stake Originals</bdi> ألعاب حصرية بـ RNG مُتحقق منه بشكل عادل: Crash وDice وLimbo وMines وKeno وPlinko وHilo. تُسهم 100% في شرط رهان <bdi dir="ltr">MAX3000</bdi>.',
        hero_img='girl-casino',
        body_html=body,
        page_slug='originals',
    )

def build_slots():
    faqs = [
        ('كم عدد السلوتس في Stake؟', '<bdi dir="ltr">Stake</bdi> يضم أكثر من 3000 سلوت من موردين كبار: Pragmatic Play وHacksaw Gaming وNetEnt وPlay\'n GO وNoLimit City وغيرهم.'),
        ('ما أفضل سلوت لاستيفاء شرط الرهان؟', 'سلوتس بـ RTP 96%+ وهامش بيت 4%+ تُسهم 100% في شرط رهان <bdi dir="ltr">MAX3000</bdi>. Stake Originals مثل Dice بهامش 1% أيضاً خيار جيد.'),
        ('هل يمكن لعب السلوتس مع MAX3000؟', 'نعم. مكافأة 200% حتى <bdi dir="ltr">$3,000</bdi> تشمل السلوتس. سلوتس بهامش بيت 4%+ تُسهم 100%، تلك بأقل من 4% تُسهم بنسبة أقل.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مكتبة <span class="text-gradient-gold">السلوتس</span></h2></div>
      {club_cards([
        ('Pragmatic Play', 'Sweet Bonanza وGates of Olympus 1000 وSugar Rush وBig Bass Bonanza. من أكثر الموردين إنتاجاً. Drops & Wins أسبوعياً.'),
        ('Hacksaw Gaming', 'Wanted Dead or a Wild وScream وXmas. مضاعفات عالية وبنية ميكانيكية خاصة. محبوب لدى اللاعبين المتقدمين.'),
        ('NoLimit City', 'Mental وTombstone RIP وDead or Alive وxBomb. سلوتس متطايرة بمضاعفات هائلة. للاعبين الجريئين.'),
        ('NetEnt وPlay\'n GO', 'Starburst وBook of Dead وRich Wilde. كلاسيكيات قاعدة متينة. RTP عالٍ نسبياً.'),
        ('الرمز <bdi dir="ltr">MAX3000</bdi>', '200% حتى <bdi dir="ltr">$3,000</bdi>. سلوتس بهامش 4%+ تُسهم 100%. اختر ألعابك بعناية لاستيفاء شرط الرهان بكفاءة.'),
        ('عمليات بحث وتصفية', '<bdi dir="ltr">Stake</bdi> يُتيح تصفية السلوتس حسب المورد وـ RTP والشعبية والجديد. سهل إيجاد لعبتك المفضلة.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='سلوتس Stake - 3000+ لعبة مع الرمز MAX3000',
        description='مكتبة سلوتس Stake.com: 3000+ لعبة من Pragmatic Play وHacksaw Gaming وNoLimit City وأكثر. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/slots/',
        og_url_path='ar/slots/',
        og_image='slots.png',
        hreflang_slug='slots/',
        hreflang_en_path='slots/',
        jsonld_extra=faq_ld,
        page_bc_name='السلوتس',
        page_bc_url='ar/slots/',
        hero_tease='+3000 سلوت. رمز واحد.',
        h1_main='سلوتس Stake - مكتبة ضخمة',
        h1_sub='3000+ سلوت من موردين عالميين.',
        hero_sub_html='<bdi dir="ltr">Stake</bdi> يضم أكثر من 3000 سلوت من Pragmatic Play وHacksaw Gaming وNoLimit City وNetEnt. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        hero_img='girl-casino',
        body_html=body,
        page_slug='slots',
    )


def build_payments():
    faqs = [
        ('ما العملات الرقمية المقبولة في Stake؟', '<bdi dir="ltr">Stake</bdi> يقبل BTC وETH وLTC وXRP وSOL وTRX وBNB وDOGE وAVAX وBCH وEOS وغيرها. قائمة تتوسع باستمرار.'),
        ('ما سرعة السحب؟', 'سحوبات العملات الرقمية: 30 دقيقة إلى ساعة. TRX وXRP وSOL ثوانٍ. سحوبات كبيرة قد تستلزم 2-4 أيام عمل. MoonPay عملة ورقية 1-5 أيام.'),
        ('هل هناك رسوم إيداع أو سحب؟', '<bdi dir="ltr">Stake</bdi> لا يفرض رسوماً داخلية على الإيداع والسحب. رسوم الشبكة (gas) يتحملها المستخدم. MoonPay يفرض رسوماً خاصة به.'),
        ('هل KYC مطلوب للسحب؟', 'KYC مستوى 2 كافٍ للسحب المعتاد. مستوى 3 مطلوب للسحوبات الكبيرة ولاسترداد مكافأة الترحيب. مستوى 3 يتطلب هوية مصوَّرة وإثبات عنوان ومصدر أموال.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مدفوعات <span class="text-gradient-gold">Stake</span></h2></div>
      {intel_cards([
        ('سرعة الإيداع', 'فوري', 'معظم العملات الرقمية تُؤكَّد في دقيقة إلى خمس دقائق بعد تأكيد الشبكة.'),
        ('سرعة السحب', '30 دق - 1 ساعة', 'التشفير المعتاد. TRX وSOL وXRP ثوانٍ. سحوبات كبيرة 2-4 أيام عمل.'),
        ('رسوم Stake', 'صفر', 'لا رسوم داخلية. رسوم الشبكة على المستخدم.'),
        ('عملات مدعومة', '+20 عملة', 'BTC ETH LTC XRP SOL TRX BNB DOGE AVAX BCH EOS USDT USDC وأكثر.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العملات الرقمية <span class="text-gradient-gold">المدعومة</span></h2></div>
      {club_cards([
        ('Bitcoin (BTC)', 'الملك. إيداع وسحب مدعوم. وقت تأكيد 10-60 دقيقة. رسوم شبكة متغيرة. الأعلى طلباً.'),
        ('Ethereum (ETH)', 'الثاني الأكثر شهرة. رسوم gas تتفاوت. سرعة تأكيد أعلى من BTC. يدعم USDT وUSDC على ERC-20.'),
        ('Solana (SOL)', 'سرعة فائقة ورسوم ضعيفة جداً. تأكيد ثوانٍ. مناسب للسحوبات السريعة والمتكررة.'),
        ('Tron (TRX)', 'USDT على TRC-20 رسومه منخفضة جداً (أقل من $1 في الغالب). سرعة تأكيد ثوانٍ إلى دقائق.'),
        ('Ripple (XRP)', 'سرعة فائقة ورسوم بضعة سنتات. ممتاز للتحويلات السريعة.'),
        ('MoonPay', 'إيداع بالعملة الورقية (بطاقات ائتمان وتحويل بنكي). رسوم MoonPay تنطبق. سحب ورقي 1-5 أيام.'),
      ])}
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مستويات <span class="text-gradient-gold">KYC</span></h2></div>
      {step_cards([
        ('مستوى KYC 1 - الأساسي', 'بريد إلكتروني وكلمة مرور. إيداع وسحب محدود. كافٍ للبدء لكن لا يكفي للمكافأة الكبيرة.'),
        ('مستوى KYC 2 - موسَّع', 'هوية مصوَّرة وإثبات عنوان. حدود إيداع وسحب أعلى. مطلوب لمعظم عمليات السحب المعتادة.'),
        ('مستوى KYC 3 - كامل', 'هوية مصوَّرة وإثبات عنوان ومصدر الأموال. مطلوب لاسترداد مكافأة الترحيب MAX3000 وللسحوبات الكبيرة. المستوى الأعلى.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='مدفوعات Stake - إيداع وسحب العملات الرقمية مع MAX3000',
        description='مدفوعات Stake.com: BTC وETH وSOL وTRX وXRP وأكثر. سحوبات خلال 30 دقيقة. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/payments/',
        og_url_path='ar/payments/',
        og_image='payments.png',
        hreflang_slug='payments/',
        hreflang_en_path='payments/',
        jsonld_extra=faq_ld,
        page_bc_name='المدفوعات',
        page_bc_url='ar/payments/',
        hero_tease='العملات الرقمية تدخل وتخرج بسرعة.',
        h1_main='مدفوعات Stake - العملات الرقمية',
        h1_sub='إيداع وسحب سريع بأكثر من 20 عملة.',
        hero_sub_html='<bdi dir="ltr">Stake</bdi> يدعم BTC وETH وSOL وTRX وXRP وBNB وأكثر من 20 عملة رقمية. السحوبات تكتمل في 30 دقيقة إلى ساعة. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='payments',
    )

def build_reserves():
    faqs = [
        ('أين يمكنني التحقق من احتياطيات Stake؟', 'عبر Arkham Intel. <bdi dir="ltr">Stake</bdi> نشر عناوين محافظه الموسومة علناً. cryptotips.com يُتابع هذه البيانات أسبوعياً.'),
        ('ما حجم احتياطيات Stake الحالية؟', 'لقطة 28 مايو 2026 تُظهر <bdi dir="ltr">$339.53M</bdi> في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%، Tron USDT 5%، BNB Chain 6%.'),
        ('هل الاحتياطيات على السلسلة ضمان للملاءة المالية؟', 'الاحتياطيات على السلسلة تُثبت الشفافية في حيازة الأصول. لكنها لا تُشكِّل ضماناً قانونياً كاملاً. هي أفضل بكثير من "ثق بنا" لكنها ليست تدقيقاً كاملاً.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">احتياطيات <span class="text-gradient-gold">Stake</span> على السلسلة</h2></div>
      {intel_cards([
        ('إجمالي الاحتياطيات', '$339.53M', 'محافظ Arkham الموسومة في 28 مايو 2026.'),
        ('Ethereum', '74%', 'الحصة الأكبر. ETH وERC-20 (USDT USDC).'),
        ('Solana', '14%', 'SOL وبروتوكولات DeFi على Solana.'),
        ('سلاسل أخرى', '12%', 'Tron (USDT TRC-20) 5%، BNB Chain 6%، سلاسل أخرى 1%.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لماذا الاحتياطيات على <span class="text-gradient-gold">السلسلة مهمة</span></h2></div>
      {club_cards([
        ('الشفافية القابلة للتتبع', 'أي شخص يستطيع التحقق من أرصدة المحافظ الموسومة على Arkham Intel أو blockchain explorer مباشرة. لا حاجة لتقرير تدقيق.'),
        ('يختلف عن "الاحتمالي"', 'معظم المنصات تُصدر بيانات ملاءة بدون تحقق مستقل. Stake نشر عناوين محافظه الفعلية. الفرق شاسع.'),
        ('cryptotips.com يتابع أسبوعياً', '<a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener" style="color:var(--gold);">cryptotips.com</a> يجمع بيانات Arkham أسبوعياً ويعرضها بشكل مُبسَّط. سهل المتابعة.'),
        ('مقارنة بالصناعة', 'عدد قليل من منصات القمار الكبرى تُفصح عن بيانات احتياطيات قابلة للتتبع علناً. Stake في مقدمة هذه الفئة.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='احتياطيات Stake على السلسلة - $339M مُتحقق منها',
        description='احتياطيات Stake.com: $339.53M في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%. تحقق وتابع عبر cryptotips.com.',
        canonical_path='ar/reserves/',
        og_url_path='ar/reserves/',
        og_image='reserves.png',
        hreflang_slug='reserves/',
        hreflang_en_path='reserves/',
        jsonld_extra=faq_ld,
        page_bc_name='الاحتياطيات',
        page_bc_url='ar/reserves/',
        hero_tease='الأموال معلَّقة على الحائط. اقرأها بنفسك.',
        h1_main='احتياطيات Stake على السلسلة',
        h1_sub='$339.53M في محافظ Arkham الموسومة.',
        hero_sub_html='<bdi dir="ltr">Stake</bdi> يُفصح عن احتياطياته على السلسلة. لقطة 28 مايو 2026: <bdi dir="ltr">$339.53M</bdi>. Ethereum 74%، Solana 14%. قابل للتتبع عبر Arkham Intel و<a href="https://cryptotips.com/on-chain/stake/" target="_blank" rel="noopener" style="color:var(--gold);">cryptotips.com</a>.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='reserves',
    )


def build_vip():
    faqs = [
        ('كيف أنضم إلى برنامج VIP في Stake؟', 'التسجيل تلقائي لجميع اللاعبين. كلما راهنت أكثر، ارتفع مستواك. Stake يُرسِل دعوات VIP مخصصة للاعبين ذوي الحجم العالي.'),
        ('ما مزايا VIP في Stake؟', 'مدير حساب مخصص، مكافآت إعادة تعبئة دورية، هدايا حصرية، دعوات لأحداث حصرية، حد رهان أعلى، معالجة سحب ذات أولوية.'),
        ('هل الرمز MAX3000 يُعطيني وضعاً خاصاً؟', '<bdi dir="ltr">MAX3000</bdi> مكافأة ترحيب، ليس تصنيفاً VIP. لكنه يمنحك بداية قوية تُساعد في بناء حجم رهان يُرقِّيك في المستويات.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">برنامج <span class="text-gradient-gold">VIP</span> في Stake</h2></div>
      {intel_cards([
        ('Bronze', 'المستوى الأدنى', 'للاعبين الجدد. الإيداع والسحب بمزايا أساسية.'),
        ('Silver & Gold', 'متوسط', 'مكافآت أسبوعية، دعم أسرع، حدود أعلى.'),
        ('Platinum', 'متقدم', 'مدير حساب، مكافآت إعادة تعبئة دورية.'),
        ('Diamond', 'القمة', 'مزايا مخصصة. VIP مُخصَّص لكبار اللاعبين.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مزايا <span class="text-gradient-gold">VIP</span></h2></div>
      {club_cards([
        ('مكافأة إعادة التعبئة', 'Platinum I كل 14 يوماً، Platinum IV في أي وقت. المبالغ مُرجَّحة بالخسائر الأخيرة. أفضل مزايا VIP في رأي كثير من اللاعبين.'),
        ('مدير حساب مخصص', 'Platinum فصاعداً يحصل على مدير VIP مخصص. تواصل مباشر، حل مشاكل أسرع، هدايا شخصية.'),
        ('حد رهان أعلى', 'VIP يحصلون على حدود رهان أعلى في الكازينو والسبورت بوك. مهم للاعبين ذوي الحجم الكبير.'),
        ('معالجة سحب ذات أولوية', 'طلبات سحب VIP تُعالَج بأولوية. مفيد للسحوبات الكبيرة.'),
        ('هدايا ودعوات أحداث', 'VIP Diamond وما فوق قد يتلقون هدايا فعلية ودعوات لأحداث رياضية وحفلات.'),
        ('الرمز <bdi dir="ltr">MAX3000</bdi> والـ VIP', 'ابدأ بـ 200% حتى <bdi dir="ltr">$3,000</bdi>. راهن لاستيفاء شرط الرهان. حجم الرهان يُراكم نقاط VIP.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='برنامج VIP في Stake - مزايا كبار اللاعبين مع MAX3000',
        description='برنامج VIP Stake.com: مكافآت إعادة تعبئة ومدير مخصص وهدايا حصرية. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/vip/',
        og_url_path='ar/vip/',
        og_image='vip.png',
        hreflang_slug='vip/',
        hreflang_en_path='vip/',
        jsonld_extra=faq_ld,
        page_bc_name='VIP',
        page_bc_url='ar/vip/',
        hero_tease='كبار اللاعبين يعرفون الفرق.',
        h1_main='برنامج VIP في Stake',
        h1_sub='مكافآت دورية ومدير مخصص وهدايا.',
        hero_sub_html='برنامج VIP في <bdi dir="ltr">Stake</bdi> يُقدِّم مكافآت إعادة تعبئة دورية ومديراً مخصصاً وحدوداً أعلى ودعوات أحداث حصرية. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك بداية قوية.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='vip',
    )

def build_mirror():
    faqs = [
        ('ما هي مواقع مرآة Stake؟', 'مواقع مرآة هي نطاقات بديلة رسمية لـ<bdi dir="ltr">Stake.com</bdi>. النطاقات المعروفة: stake.ac وstake.bet وstake.games. تُستخدم في مناطق قد يكون الوصول لـstake.com محجوباً فيها.'),
        ('هل الرمز MAX3000 يعمل على مواقع المرآة؟', 'نعم. <bdi dir="ltr">MAX3000</bdi> يعمل على جميع نطاقات <bdi dir="ltr">Stake</bdi> البديلة الرسمية بنفس الشروط: 200% حتى <bdi dir="ltr">$3,000</bdi>، شرط رهان 40x.'),
        ('هل مواقع المرآة آمنة؟', 'النطاقات الرسمية: stake.ac وstake.bet وstake.games آمنة ومُشغَّلة من نفس الشركة. تحقق دائماً من النطاق قبل تسجيل الدخول.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">نطاقات <span class="text-gradient-gold">Stake</span> البديلة</h2></div>
      {intel_cards([
        ('stake.com', 'النطاق الرئيسي', 'الموقع الأصلي. متاح في معظم الدول باستثناء الولايات المتحدة والمملكة المتحدة.'),
        ('stake.ac', 'مرآة رسمية', 'نطاق بديل رسمي. نفس المنصة ونفس الحساب ونفس الرموز.'),
        ('stake.bet', 'مرآة رسمية', 'نطاق بديل رسمي ثان. يعمل على جميع الأجهزة والمتصفحات.'),
        ('stake.games', 'مرآة رسمية', 'نطاق بديل رسمي ثالث. مفيد في مناطق قد يكون stake.com محجوباً فيها.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الرمز <bdi dir="ltr">MAX3000</bdi> على <span class="text-gradient-gold">جميع النطاقات</span></h2></div>
      <div class="club-body" style="max-width:720px;margin:0 auto;">
        <p>الرمز الترويجي <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يعمل على stake.com وstake.ac وstake.bet وstake.games بنفس الشروط: 200% مطابقة حتى <bdi dir="ltr">$3,000</bdi>، شرط رهان 40x على مجموع الإيداع والمكافأة، KYC مستوى 3 مطلوب.</p>
        <p>إذا كان stake.com غير متاح في منطقتك، جرِّب stake.ac أو stake.bet أو stake.games. كلها تصل إلى نفس المنصة ونفس الحساب.</p>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:20px;display:inline-block;">ادخل بـ MAX3000 الآن</a>
      </div>
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='مواقع مرآة Stake - النطاقات البديلة الرسمية مع MAX3000',
        description='مواقع مرآة Stake الرسمية: stake.ac وstake.bet وstake.games. الرمز MAX3000 يعمل على الجميع. 200% حتى $3,000.',
        canonical_path='ar/mirror/',
        og_url_path='ar/mirror/',
        og_image='mirror.png',
        hreflang_slug='mirror/',
        hreflang_en_path='mirror/',
        jsonld_extra=faq_ld,
        page_bc_name='مواقع المرآة',
        page_bc_url='ar/mirror/',
        hero_tease='الباب الرئيسي مغلق؟ هناك أبواب أخرى.',
        h1_main='مواقع مرآة Stake الرسمية',
        h1_sub='stake.ac وstake.bet وstake.games.',
        hero_sub_html='<bdi dir="ltr">Stake</bdi> لديه نطاقات بديلة رسمية: stake.ac وstake.bet وstake.games. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يعمل على الجميع. 200% حتى <bdi dir="ltr">$3,000</bdi>، شرط رهان 40x.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='mirror',
    )

def build_about_stake():
    faqs = [
        ('متى تأسست Stake؟', '<bdi dir="ltr">Stake</bdi> تأسست في 2017 على يد Ed Craven وBijan Tehrani.'),
        ('من يملك Stake؟', 'Ed Craven (مواليد 1995، ملبورن) وBijan Tehrani. الشركة الأم Easygo Group Holdings مُدرجة في أستراليا.'),
        ('ما ترخيص Stake؟', 'Curaçao OGL/2024/1451/0918 بواسطة Medium Rare NV. يغطي معظم الدول باستثناء الولايات المتحدة والمملكة المتحدة وأستراليا.'),
        ('ما حجم Stake؟', 'GGR <bdi dir="ltr">$4.7B</bdi>، 21M+ حساب، إيرادات Easygo FY2025 A$970M. واحدة من أكبر منصات القمار الرقمي في العالم.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">من هم <span class="text-gradient-gold">Stake</span></h2></div>
      {intel_cards([
        ('التأسيس', '2017', 'أسسها Ed Craven وBijan Tehrani. التقيا في RuneScape. بنيا المنصة من الصفر.'),
        ('الكيان القانوني', 'Medium Rare NV', 'كيان كوراساو مُشغِّل Stake.com. الشركة الأم Easygo Group Holdings.'),
        ('الترخيص', 'OGL/2024/1451/0918', 'كوراساو. يغطي 100+ دولة. انسحب من UK مارس 2025.'),
        ('الحجم', 'GGR $4.7B', '21M+ حساب. أكبر منصة قمار بالعملات الرقمية في العالم.'),
        ('الاحتياطيات', '$339.53M', 'محافظ Arkham الموسومة في 28 مايو 2026.'),
        ('Kick.com', 'منصة بث', 'Ed Craven وBijan Tehrani أطلقا Kick.com في 2022. بديل منافس لـ Twitch.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المؤسسان: <span class="text-gradient-gold">Craven &amp; Tehrani</span></h2></div>
      {club_cards([
        ('Ed Craven', 'مواليد 1995، ملبورن. التقى بـBijan في RuneScape Online وهو مراهق. درس هندسة الحاسوب. أسس Stake في 2017 وعمره 21 عاماً. أطلق Kick.com في 2022. تقديرات Forbes لثروته الشخصية تتجاوز US$3B. أحد أصغر المليارديرات الأستراليين.'),
        ('Bijan Tehrani', 'شريك مؤسس وCTO. خبرة تقنية عميقة. يُركِّز على تطوير المنتج والبنية التحتية. هادئ وأقل حضوراً علنياً من Craven.'),
        ('Easygo Group Holdings', 'الشركة الأم المُدرجة في أستراليا. FY2025: إيرادات A$970M، صافي ربح A$257M. تُشغِّل Stake.com وStake.us وKick.com وعمليات أخرى.'),
        ('الانطلاق من RuneScape', 'قصة تأسيس Stake غير تقليدية: شابان التقيا في لعبة RPG عبر الإنترنت وقررا بناء منصة قمار بالعملات الرقمية. من لعبة للألعاب إلى منصة بمليارات الدولارات.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='حول Stake.com - التاريخ والترخيص والمؤسسون',
        description='Stake.com تأسست 2017 من Ed Craven وBijan Tehrani. Medium Rare NV، كوراساو OGL/2024/1451/0918. GGR $4.7B، 21M+ حساب، $339M احتياطيات.',
        canonical_path='ar/about-stake/',
        og_url_path='ar/about-stake/',
        og_image='about-stake.png',
        hreflang_slug='about-stake/',
        hreflang_en_path='about-stake/',
        jsonld_extra=faq_ld,
        page_bc_name='حول Stake',
        page_bc_url='ar/about-stake/',
        hero_tease='وجه خلف الدار.',
        h1_main='حول Stake.com',
        h1_sub='التاريخ، الترخيص، المؤسسون.',
        hero_sub_html='<bdi dir="ltr">Stake.com</bdi> أسسها Ed Craven وBijan Tehrani في 2017. بواسطة <bdi dir="ltr">Medium Rare NV</bdi>، ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi>. GGR <bdi dir="ltr">$4.7B</bdi>، 21M+ حساب، <bdi dir="ltr">$339M</bdi> احتياطيات على السلسلة.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='about-stake',
    )


def build_responsible_gambling():
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المقامرة <span class="text-gradient-gold">المسؤولة</span></h2></div>
      {club_cards([
        ('القمار ترفيه لا دخل', 'القمار وسيلة ترفيه، ليس مصدر دخل موثوقاً. راهن فقط ما تستطيع خسارته. لا تطارد الخسائر.'),
        ('ضع حدوداً مسبقاً', 'Stake يُتيح تحديد حدود إيداع وخسارة ورهان من إعدادات الحساب. ضعها قبل البدء.'),
        ('استراحة أو إقصاء ذاتي', 'تحتاج استراحة؟ Stake يُتيح تعليق الحساب مؤقتاً أو الإقصاء الذاتي الكامل. اتصل بالدعم المباشر.'),
        ('GamCare', '<a href="https://www.gamcare.org.uk/" target="_blank" rel="noopener" style="color:var(--gold);">GamCare</a> مورد دعم مجاني سري لمشاكل القمار. خط نصيحة 24/7.'),
        ('Gambling Therapy', '<a href="https://www.gamblingtherapy.org/" target="_blank" rel="noopener" style="color:var(--gold);">Gambling Therapy</a> يُقدِّم دعماً نفسياً عبر الإنترنت لمشاكل القمار، متاح بالعربية.'),
        ('للأطفال', 'موقعنا مخصص لمن هم 18 عاماً فأكثر. استخدم أدوات رقابة الأبوين لمنع الوصول.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">علامات <span class="text-gradient-gold">المشكلة</span></h2></div>
      <div class="club-body">
        <p>إذا لاحظت أياً مما يلي، قد تكون بحاجة لمساعدة:</p>
        <ul style="margin-top:16px;">
          <li>تراهن بأموال لا تستطيع خسارتها</li>
          <li>تطارد خسائر سابقة</li>
          <li>القمار يؤثر على علاقاتك أو عملك</li>
          <li>تكذب على أحبائك بشأن قمارك</li>
          <li>تُقرض أو تبيع لتحصيل مال للقمار</li>
          <li>تشعر بالقلق أو الاكتئاب بسبب القمار</li>
        </ul>
        <p style="margin-top:20px;">إذا تعرفت على نفسك في هذه العلامات، تواصل مع <a href="https://www.gamcare.org.uk/" target="_blank" rel="noopener" style="color:var(--gold);">GamCare</a> أو <a href="https://www.gamblingtherapy.org/" target="_blank" rel="noopener" style="color:var(--gold);">Gambling Therapy</a> فوراً.</p>
      </div>
    </div>
  </section>'''
    return page_template(
        title='المقامرة المسؤولة في Stake - أدوات الحماية والدعم',
        description='المقامرة المسؤولة في Stake.com: حدود الإيداع والخسارة، إقصاء ذاتي، GamCare، Gambling Therapy. العب بمسؤولية.',
        canonical_path='ar/responsible-gambling/',
        og_url_path='ar/responsible-gambling/',
        og_image='default.png',
        hreflang_slug='responsible-gambling/',
        hreflang_en_path='responsible-gambling/',
        jsonld_extra='',
        page_bc_name='المقامرة المسؤولة',
        page_bc_url='ar/responsible-gambling/',
        hero_tease='النادي يهتم بالسلامة أيضاً.',
        h1_main='المقامرة المسؤولة',
        h1_sub='العب بوعي، العب بأمان.',
        hero_sub_html='القمار ترفيه عندما يُمارَس بمسؤولية. <bdi dir="ltr">Stake</bdi> يُقدِّم أدوات لضبط حدودك. إذا كنت تحتاج مساعدة، فريق GamCare وGambling Therapy متاحون.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='responsible-gambling',
        promo_strip=False,
        cta_btn_text='احصل على المساعدة - GamCare',
    )

def build_stake_engine():
    faqs = [
        ('ما هي محركات العب في Stake؟', '<bdi dir="ltr">Stake</bdi> تطلق باستمرار مزايا منصة جديدة. يشمل ذلك Stake.us لسوق الولايات المتحدة، وKick.com لبث الألعاب، والبطولات المدعومة.'),
        ('هل Stake.us مختلف عن Stake.com؟', 'تماماً. <bdi dir="ltr">Stake.us</bdi> يعمل بنموذج سحوبات بدون مال حقيقي: Gold Coins وStake Cash. مخصص للولايات المتحدة فقط. 18+ (21+ في بعض الولايات).'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">محرك <span class="text-gradient-gold">Stake</span></h2></div>
      {club_cards([
        ('البنية التحتية', 'Stake بُنيت على بنية تحتية مخصصة. معالجة ملايين الرهانات يومياً. وقت توقف شبه صفري في السنوات الأخيرة.'),
        ('Provably Fair', 'Stake Originals تستخدم RNG مُتحقق منه بشكل عادل. كل جولة يمكن التحقق منها. الشفافية في صميم المنصة.'),
        ('Stake.us', 'نموذج سحوبات للسوق الأمريكية. Gold Coins للعب، Stake Cash قابلة للاسترداد. 21M+ مستخدم عبر المنصتين.'),
        ('Kick.com', 'منصة بث مباشر أطلقها Ed Craven وBijan Tehrani في 2022. بديل منافس لـ Twitch. تنمو بسرعة.'),
        ('Easygo Group', 'الشركة الأم المُدرجة. FY2025: إيرادات A$970M، صافي ربح A$257M. من أسرع الشركات نمواً في القطاع.'),
        ('الترقيات الدائمة', 'Stake تُطلق باستمرار مزايا جديدة: ألعاب Originals وتغطية رياضية جديدة وشراكات وأحداث.'),
      ])}
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='محرك Stake - التقنية والبنية التحتية وراء المنصة',
        description='محرك Stake.com: Provably Fair وStake.us وKick.com وEasygo Group Holdings. الرمز MAX3000 يفتح 200% حتى $3,000.',
        canonical_path='ar/stake-engine/',
        og_url_path='ar/stake-engine/',
        og_image='default.png',
        hreflang_slug='stake-engine/',
        hreflang_en_path='stake-engine/',
        jsonld_extra=faq_ld,
        page_bc_name='محرك Stake',
        page_bc_url='ar/stake-engine/',
        hero_tease='ما خلف الستارة.',
        h1_main='محرك Stake - التقنية والبنية التحتية',
        h1_sub='Provably Fair وStake.us وEasygo Group.',
        hero_sub_html='<bdi dir="ltr">Stake</bdi> يُشغِّل منصة تقنية متكاملة: كازينو ومراهنات وبوكر وأصليات وKick.com وStake.us. بنية تحتية مخصصة تعالج ملايين الرهانات يومياً.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='stake-engine',
    )

def build_news():
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أخبار <span class="text-gradient-gold">Stake</span></h2></div>
      {club_cards([
        ('Easygo Group Holdings - FY2025', 'أفصحت الشركة الأم عن إيرادات FY2025 بلغت A$970M وصافي ربح A$257M. هذه الأرقام تُرسِّخ مكانة Stake كإحدى أسرع منصات القمار نمواً. المؤسس Ed Craven أحد أصغر المليارديرات الأستراليين.'),
        ('الاحتياطيات على السلسلة - أحدث لقطة', 'لقطة 28 مايو 2026 من Arkham Intel تُظهر $339.53M في محافظ Stake الموسومة. Ethereum 74%، Solana 14%، Tron USDT 5%، BNB Chain 6%. Stake من القلائل في الصناعة الذين يُفصحون عن احتياطيات قابلة للتتبع.'),
        ('Kick.com - منصة البث الشريكة', 'Ed Craven وBijan Tehrani أطلقا Kick.com في 2022 كبديل منافس لـ Twitch. المنصة نمت بسرعة وتستضيف بثوثات قمار حية لكبار اللاعبين.'),
        ('انسحاب المملكة المتحدة - مارس 2025', 'Stake انسحبت من السوق البريطانية في مارس 2025. اللاعبون البريطانيون لم يعودوا يستطيعون الوصول. السبب: متطلبات تنظيمية.'),
        ('Stake.us - التوسع الأمريكي', 'Stake.us وسَّعت عملياتها في الولايات المتحدة. الآن متاحة في 37 ولاية. نموذج سحوبات بدون مال حقيقي يستهدف السوق الأمريكية بشكل قانوني.'),
        ('شراكات الرياضة', 'Stake تُعلن شراكات رياضية كبرى بانتظام. رعاية أندية كرة قدم وبطولات Esports. توسيع العلامة التجارية عالمياً.'),
      ])}
    </div>
  </section>'''
    return page_template(
        title='أخبار Stake - آخر التطورات والتحديثات 2026',
        description='آخر أخبار Stake.com: Easygo FY2025، الاحتياطيات على السلسلة، Kick.com، انسحاب المملكة المتحدة، Stake.us. كل الأخبار في مكان واحد.',
        canonical_path='ar/news/',
        og_url_path='ar/news/',
        og_image='default.png',
        hreflang_slug='news/',
        hreflang_en_path='news/',
        jsonld_extra='',
        page_bc_name='الأخبار',
        page_bc_url='ar/news/',
        hero_tease='آخر ما يجري في دهاليز النادي.',
        h1_main='أخبار Stake - 2026',
        h1_sub='آخر التطورات والتحديثات.',
        hero_sub_html='آخر أخبار <bdi dir="ltr">Stake.com</bdi>: نتائج Easygo المالية، احتياطيات السلسلة، Kick.com، تطورات تنظيمية. النادي يتابع كل شيء.',
        hero_img='girl-homepage',
        body_html=body,
        page_slug='news',
    )

def build_stake_us_bonus():
    faqs = [
        ('ما الفرق بين Stake.com وStake.us؟', '<bdi dir="ltr">Stake.com</bdi> منصة مال حقيقي عالمية. <bdi dir="ltr">Stake.us</bdi> منصة سحوبات أمريكية بدون مال حقيقي تستخدم Gold Coins وStake Cash. الولايات المتحدة محجوبة من <bdi dir="ltr">Stake.com</bdi>.'),
        ('ماذا يُعطيني MAX3000 في Stake.us؟', '560,000 Gold Coins + 56 Stake Cash + 3.5% rakeback. يُطبَّق عند التسجيل عبر رابط MAX3000.'),
        ('هل Stake.us مجاني؟', 'يمكنك الحصول على Gold Coins مجاناً من إسقاطات يومية. Stake Cash قابلة للاسترداد بعد 3x play-through. لا إيداع مال حقيقي إلزامي.'),
    ]
    faq_ld = f'<script type="application/ld+json">{faq_jsonld(faqs)}</script>'
    body = f'''
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">ترحيب <span class="text-gradient-gold">Stake.us</span></h2></div>
      {intel_cards([
        ('Gold Coins', '560,000 GC', 'للعب فقط. لا يمكن استردادها. يُستخدم لجميع ألعاب الكازينو.'),
        ('Stake Cash', '56 SC', 'قابلة للاسترداد بعد 3x play-through. ليست مال حقيقي.'),
        ('Rakeback', '3.5%', 'نسبة من عمولة المائدة ترجع إليك باستمرار.'),
        ('الأهلية', '21+ فقط', 'Stake.us متاح في 37 ولاية أمريكية. لمن هم 21 عاماً فأكثر فقط.'),
      ])}
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الفرق بين <span class="text-gradient-gold">المنصتين</span></h2></div>
      <div class="club-grid">
        <div class="club-card">
          <h3><bdi dir="ltr">Stake.com</bdi> - عالمي</h3>
          <p>مال حقيقي. Curaçao OGL/2024/1451/0918. كازينو ورياضة وبوكر. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi>. للبالغين 18+ في معظم الدول باستثناء الولايات المتحدة والمملكة المتحدة.</p>
        </div>
        <div class="club-card">
          <h3><bdi dir="ltr">Stake.us</bdi> - أمريكي</h3>
          <p>سحوبات. Sweepsteaks Limited. كازينو فقط، لا رياضة. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يُعطي 560K GC + 56 SC + 3.5% rakeback. للبالغين 21+ في 37 ولاية.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">انضم إلى Stake.us</a>
        </div>
      </div>
    </div>
  </section>
  {faq_section(faqs)}'''
    return page_template(
        title='مكافأة Stake.us - MAX3000 يفتح 560K Gold Coins',
        description='مكافأة Stake.us بالرمز MAX3000: 560,000 Gold Coins + 56 Stake Cash + 3.5% rakeback. منصة سحوبات للولايات المتحدة. 21+ فقط.',
        canonical_path='ar/stake-us-bonus/',
        og_url_path='ar/stake-us-bonus/',
        og_image='default.png',
        hreflang_slug='stake-us-bonus/',
        hreflang_en_path='stake-us-bonus/',
        jsonld_extra=faq_ld,
        page_bc_name='مكافأة Stake.us',
        page_bc_url='ar/stake-us-bonus/',
        hero_tease='الباب الأمريكي مختلف.',
        h1_main='مكافأة Stake.us مع MAX3000',
        h1_sub='560K Gold Coins + 56 Stake Cash.',
        hero_sub_html='<bdi dir="ltr">Stake.us</bdi> منصة سحوبات أمريكية. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يُعطي 560,000 GC + 56 SC + 3.5% rakeback. مخصص لمن هم 21+ في الولايات المتحدة.',
        hero_img='girl-homepage',
        body_html=body,
        cta_btn_text='انضم إلى Stake.us بـ MAX3000',
        page_slug='stake-us-bonus',
    )


# ══════════════════════════════════════════════════════════════════════════
# MAIN EXECUTION
# ══════════════════════════════════════════════════════════════════════════

def main():
    pages = {
        'ar/index.html': build_index(),
        'ar/promo-code/index.html': build_promo_code(),
        'ar/casino/index.html': build_casino(),
        'ar/sports/index.html': build_sports(),
        'ar/poker/index.html': build_poker(),
        'ar/aviator/index.html': build_aviator(),
        'ar/live-casino/index.html': build_live_casino(),
        'ar/live-odds/index.html': build_live_odds(),
        'ar/originals/index.html': build_originals(),
        'ar/slots/index.html': build_slots(),
        'ar/payments/index.html': build_payments(),
        'ar/reserves/index.html': build_reserves(),
        'ar/vip/index.html': build_vip(),
        'ar/mirror/index.html': build_mirror(),
        'ar/about-stake/index.html': build_about_stake(),
        'ar/responsible-gambling/index.html': build_responsible_gambling(),
        'ar/stake-engine/index.html': build_stake_engine(),
        'ar/news/index.html': build_news(),
        'ar/stake-us-bonus/index.html': build_stake_us_bonus(),
    }
    
    print(f"\nBuilding {len(pages)} Arabic pages...")
    for rel_path, content in pages.items():
        full_path = os.path.join(ROOT, rel_path)
        write_page(full_path, content)
    
    print(f"\nDone. {len(pages)} files written.")

if __name__ == '__main__':
    main()

