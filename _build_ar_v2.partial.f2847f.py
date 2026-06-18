#!/usr/bin/env python3
"""
Build /ar/ locale for winnersclub.com
Generates 19 HTML files in MSA Arabic with full RTL support.
"""
import os, re, shutil

SITE = '/home/user/workspace/winnersclub.com'
AR_DIR = os.path.join(SITE, 'ar')

PAGES = [
    'index', 'about-stake', 'aviator', 'casino', 'live-casino',
    'live-odds', 'mirror', 'news', 'originals', 'payments',
    'poker', 'promo-code', 'reserves', 'responsible-gambling',
    'slots', 'sports', 'stake-engine', 'stake-us-bonus', 'vip'
]

HREFLANG_BLOCK = '''  <link rel="alternate" hreflang="en" href="https://winnersclub.com/{en_path}">
  <link rel="alternate" hreflang="ko" href="https://winnersclub.com/ko/{path}">
  <link rel="alternate" hreflang="zh-Hans" href="https://winnersclub.com/zh/{path}">
  <link rel="alternate" hreflang="vi" href="https://winnersclub.com/vi/{path}">
  <link rel="alternate" hreflang="th" href="https://winnersclub.com/th/{path}">
  <link rel="alternate" hreflang="ms" href="https://winnersclub.com/ms/{path}">
  <link rel="alternate" hreflang="pt" href="https://winnersclub.com/pt/{path}">
  <link rel="alternate" hreflang="ja" href="https://winnersclub.com/ja/{path}">
  <link rel="alternate" hreflang="es" href="https://winnersclub.com/es/{path}">
  <link rel="alternate" hreflang="pt-BR" href="https://winnersclub.com/pt-br/{path}">
  <link rel="alternate" hreflang="tr" href="https://winnersclub.com/tr/{path}">
  <link rel="alternate" hreflang="id" href="https://winnersclub.com/id/{path}">
  <link rel="alternate" hreflang="fr" href="https://winnersclub.com/fr/{path}">
  <link rel="alternate" hreflang="ru" href="https://winnersclub.com/ru/{path}">
  <link rel="alternate" hreflang="hi" href="https://winnersclub.com/hi/{path}">
  <link rel="alternate" hreflang="ar" href="https://winnersclub.com/ar/{path}">
  <link rel="alternate" hreflang="x-default" href="https://winnersclub.com/{en_path}">'''

NAV_LINKS = '''<a href="/ar/casino/" class="nav-link">كازينو</a>
        <a href="/ar/sports/" class="nav-link">رياضة</a>
        <a href="/ar/poker/" class="nav-link">بوكر</a>
        <a href="/ar/aviator/" class="nav-link">أفياتور</a>
        <a href="/ar/promo-code/" class="nav-link">الرمز الترويجي</a>
        <a href="/ar/reserves/" class="nav-link">الاحتياطيات</a>
        <a href="/ar/about-stake/" class="nav-link">عن Stake</a>'''

MOBILE_LANG = '''<div class="mobile-lang-block"><label>اللغة</label><select onchange="if(this.value)window.location.href=this.value" aria-label="اللغة"><option value="">English</option><option value="/ko/">한국어 (Korean)</option><option value="/zh/">中文 (Chinese)</option><option value="/vi/">Tiếng Việt (Vietnamese)</option><option value="/th/">ไทย (Thai)</option><option value="/ms/">Bahasa Melayu (Malay)</option><option value="/pt/">Português (Portuguese)</option><option value="/ja/">日本語 (Japanese)</option><option value="/es/">Español (Spanish)</option><option value="/pt-br/">Português do Brasil (Portuguese - Brazil)</option><option value="/tr/">Türkçe (Turkish)</option><option value="/id/">Bahasa Indonesia (Indonesian)</option><option value="/fr/">Français (French)</option><option value="/ru/">Русский (Russian)</option><option value="/hi/">हिन्दी (Hindi)</option><option value="/ar/" selected>العربية (Arabic)</option></select></div>'''

DESKTOP_LANG = '''<select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="اللغة"><option value="https://winnersclub.com/">English</option><option value="https://winnersclub.com/ko/">한국어</option><option value="https://winnersclub.com/zh/">中文</option><option value="https://winnersclub.com/vi/">Tiếng Việt</option><option value="https://winnersclub.com/th/">ไทย</option><option value="https://winnersclub.com/ms/">Bahasa Melayu</option><option value="https://winnersclub.com/pt/">Português</option><option value="https://winnersclub.com/ja/">日本語</option><option value="https://winnersclub.com/es/">Español</option><option value="https://winnersclub.com/pt-br/">Português (BR)</option><option value="https://winnersclub.com/tr/">Türkçe</option><option value="https://winnersclub.com/id/">Bahasa Indonesia</option><option value="https://winnersclub.com/fr/">Français</option><option value="https://winnersclub.com/ru/">Русский</option><option value="https://winnersclub.com/hi/">हिन्दी</option><option value="" selected>العربية</option></select>'''

FOOTER_HTML = '''  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub">
  <path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/>
  <path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text>
</svg>
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">النادي مع Stake منذ 2017.</p>
          <div class="footer-badges">
            <span class="age-badge">+18</span>
            <span class="cert-badge">GamCare</span>
            <span class="cert-badge">SSL</span>
          </div>
        </div>
        <div class="footer-links-grid anim-stagger">
          <div class="footer-col">
            <h4>الصالة</h4>
            <a href="/ar/casino/">كازينو</a>
            <a href="/ar/sports/">المراهنات الرياضية</a>
            <a href="/ar/poker/">بوكر</a>
            <a href="/ar/aviator/">أفياتور</a>
            <a href="/ar/live-odds/">الأرباح المباشرة</a>
          </div>
          <div class="footer-col">
            <h4>الرمز</h4>
            <a href="/ar/promo-code/">الرمز الترويجي MAX3000</a>
            <a href="/ar/payments/">المدفوعات</a>
            <a href="/ar/mirror/">الوصول والمرايا</a>
          </div>
          <div class="footer-col">
            <h4>المعلومات</h4>
            <a href="/ar/about-stake/">عن Stake</a>
            <a href="/ar/reserves/">الاحتياطيات على السلسلة</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">WinnersClub هو النادي الداخلي الحصري للاعبي Stake. تُشغِّل شركة Medium Rare NV موقع Stake.com بموجب ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi>. أما Stake.us فهو منصة سويبستيكس منفصلة تُشغِّلها Sweepsteaks Limited. هذا الموقع لأغراض إعلامية فقط. ينطوي القمار على مخاطر. العب بمسؤولية. إن كنت تعاني من مشكلة في القمار أو تعرف شخصاً كذلك، تواصل مع GamCare أو جهة الدعم المحلية. للأعمار 18 عاماً فما فوق.</p>
        <p class="footer-copyright">&copy; 2026 winnersclub.com. جميع الحقوق محفوظة.</p>
      </div>
    </div>
  </footer>'''

ROOMS_GRID = '''<aside class="rooms-grid" aria-label="غرف أخرى في وينرز كلوب" style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);border:1px solid rgba(255,215,0,.12);border-radius:14px;"><h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#737378;margin:0 0 18px;font-weight:700;">غرف أخرى في وينرز كلوب</h3><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;"><li><a href="/ar/promo-code/">الرمز الترويجي Stake</a></li><li><a href="/ar/casino/">كازينو Stake</a></li><li><a href="/ar/sports/">المراهنات الرياضية</a></li><li><a href="/ar/poker/">بوكر Stake</a></li><li><a href="/ar/aviator/">أفياتور Stake</a></li><li><a href="/ar/reserves/">الاحتياطيات الموثقة</a></li><li><a href="/ar/about-stake/">عن Stake</a></li><li><a href="/ar/payments/">مدفوعات العملات الرقمية</a></li><li><a href="/ar/mirror/">مواقع المرآة</a></li><li><a href="/ar/live-odds/">الأرباح المباشرة</a></li><li><a href="/ar/originals/">ألعاب Stake الأصلية</a></li><li><a href="/ar/vip/">برنامج VIP</a></li><li><a href="/ar/slots/">مكتبة السلوتس</a></li><li><a href="/ar/live-casino/">الكازينو المباشر</a></li></ul></aside>'''

TICKER = '''  <div class="reserves-ticker"><div class="rt-inner"><span>Stake على السلسلة الآن: الاحتياطيات الموسومة <bdi dir="ltr">$339.53M</bdi> &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi> &middot; المصدر: Arkham Intel عبر cryptotips.com &middot; لقطة 28 مايو 2026</span><span>Stake على السلسلة الآن: الاحتياطيات الموسومة <bdi dir="ltr">$339.53M</bdi> &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; ترخيص كوراساو <bdi dir="ltr">OGL/2024/1451/0918</bdi> &middot; المصدر: Arkham Intel عبر cryptotips.com &middot; لقطة 28 مايو 2026</span></div></div>'''

PROMO_STRIP = '''  <aside class="promo-strip" aria-label="الرمز الترويجي MAX3000"><div class="ps-inner"><span class="ps-label">الرمز الترويجي</span><span class="ps-code">MAX3000</span><span class="ps-bonus">200% حتى <bdi dir="ltr">$3,000</bdi> &middot; شرط مراهنة 40x</span><a href="/ar/promo-code/" class="ps-cta">فتح صفحة الرمز &larr;</a></div></aside>'''

def build_head(title, desc, canonical_path, og_image='default.png', page_slug='', extra_jsonld=''):
    if page_slug == 'index' or page_slug == '':
        en_path = ''
        path_segment = ''
    else:
        en_path = f'{page_slug}/'
        path_segment = f'{page_slug}/'

    hreflang = HREFLANG_BLOCK.format(
        en_path=en_path,
        path=path_segment
    )

    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><script>document.documentElement.classList.add("js-anim");</script>
  <meta charset="UTF-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://winnersclub.com/ar/{path_segment}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://winnersclub.com/ar/{path_segment}">
  <meta property="og:image" content="https://winnersclub.com/images/og/{og_image}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <meta name="theme-color" content="#8b0a1a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900&family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
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
{extra_jsonld}
{hreflang}
  <script src="/lang-redirect.js" defer></script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">
<script type="application/ld+json" data-ld="org">{{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"The players back room for Stake. Promo code MAX3000 unlocks a 200% match up to $3,000 with 40x wagering."}}</script>
<meta name="twitter:image" content="https://winnersclub.com/images/og/{og_image}"><meta name="twitter:card" content="summary_large_image">
</head>'''

def build_header(current_path):
    return f'''<body>
  <!-- HEADER -->
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/ar/" class="header-logo" aria-label="WinnersClub الرئيسية">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        {NAV_LINKS}
      {MOBILE_LANG}</nav>
      <div class="header-actions">{DESKTOP_LANG}
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup" aria-label="ادخل الآن">ادخل الآن</a>
        <button class="hamburger" id="hamburger" aria-label="فتح القائمة"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>'''

def build_footer_scripts():
    return '''  <script src="/script.min.js?v=20260618a" defer></script>
  <script src="/voice.js" defer></script>
<script src="/ga-events.js" defer></script>'''

# ─── Page content functions ────────────────────────────────────────────────────

def page_index():
    slug = 'index'
    title = 'وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000'
    desc = 'النادي الداخلي الحصري للاعبي Stake.com. استخدم الرمز الترويجي MAX3000 للحصول على مكافأة 200% حتى $3,000 مع شرط مراهنة 40x. GGR $4.7B، أكثر من 21 مليون حساب، احتياطيات على السلسلة $339M. Medium Rare NV، كوراساو OGL/2024/1451/0918، تأسست 2017.'
    path_seg = ''

    jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000",
  "description": "النادي الداخلي الحصري للاعبي Stake.com. الرمز الترويجي MAX3000 يفتح مكافأة 200% حتى $3,000 مع شرط مراهنة 40x. GGR $4.7B، أكثر من 21 مليون حساب.",
  "url": "https://winnersclub.com/ar/"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://winnersclub.com/ar/"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "هل MAX3000 هو أكبر رمز مكافأة لـ Stake؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "نعم. مكافأة 200% حتى $3,000 مع شرط مراهنة 40x على مجموع الإيداع والمكافأة. معظم الرموز العامة تقف عند 100% / $1,000. MAX3000 هو الرمز الذي يقدمه النادي عند المدخل."
      }
    },
    {
      "@type": "Question",
      "name": "هل Stake.com موثوق؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "تعمل Stake تحت ترخيص كوراساو OGL/2024/1451/0918 بموجب شركة Medium Rare NV منذ 2017. الاحتياطيات على السلسلة بلغت $339.53M بتاريخ 28 مايو 2026، ويمكن تتبعها علناً على Arkham. المؤسسان Ed Craven (مولود 1995 في ملبورن) وBijan Tehrani يديران أيضاً منصة Kick."
      }
    },
    {
      "@type": "Question",
      "name": "كيف يمكن التحقق من احتياطيات Stake؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "تفضل بزيارة صفحة الاحتياطيات على winnersclub.com/ar/reserves/. لقطة 28 مايو 2026 تُظهر $339.53M في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%، أرصدة ستيبل كوين ضخمة. كل شيء قابل للتتبع عبر Arkham Intel من خلال cryptotips.com."
      }
    },
    {
      "@type": "Question",
      "name": "من أين يمكنني اللعب؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "يغطي ترخيص كوراساو معظم الدول، لكن Stake تفرض قيوداً ذاتية في بعض المناطق. تفضل بزيارة صفحة مواقع المرآة للعثور على النطاق المناسب لمنطقتك."
      }
    },
    {
      "@type": "Question",
      "name": "ما مدى سرعة السحب؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "عمليات سحب العملات الرقمية تكتمل في 30 دقيقة إلى ساعة في الظروف الاعتيادية. TRX وXRP وSOL تُسوَّى في ثوانٍ. عمليات السحب الكبيرة قد تستلزم 2 إلى 4 أيام عمل للمراجعة. سحوبات MoonPay القانونية تستغرق 1 إلى 5 أيام عمل."
      }
    }
  ]
}
</script>'''

    content = f'''  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">إن وصلت إلى هذه الصفحة، فالحارس بالفعل أعجبه شأنك.</p>
        <h1 class="ch-title text-gradient-gold">الرمز الترويجي لـ Stake هو <bdi dir="ltr">MAX3000</bdi><span class="h1-sub">إلى داخل النادي.</span></h1>
        <p class="ch-sub">الغرفة الخلفية الحصرية للاعبي Stake. اهمس بالرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> عند المدخل لتحصل على <strong>مكافأة 200% حتى <bdi dir="ltr">$3,000</bdi></strong> مع <strong>شرط مراهنة 40x على مجموع الإيداع والمكافأة</strong>. لا مقارنة مع الرموز العامة الرخيصة التي لا تتجاوز $100 مع مصافحة باردة.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">احصل على 200% حتى <bdi dir="ltr">$3,000</bdi> على <bdi dir="ltr">Stake.com</bdi></a>
          <a href="/ar/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">ما الذي يفتحه MAX3000</a>
        </div>
      </div>
    </div>
  </section>
  {TICKER}
  {PROMO_STRIP}

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لماذا هذا <span class="text-gradient-gold">النادي</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>مكافأة بوزن حقيقي</h3><p>200% حتى <bdi dir="ltr">$3,000</bdi> مع شرط مراهنة 40x على مجموع الإيداع والمكافأة. رموز Stake الأخرى المتداولة على الإنترنت لا تتجاوز 100% / <bdi dir="ltr">$1,000</bdi>. إن لم تُقدم الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> خلال 24 ساعة من التسجيل، ستعود إلى القائمة الرخيصة.</p></div>
        <div class="club-card"><h3>الأموال معلقة على الجدار</h3><p>احتياطيات Arkham الموسومة بلغت <bdi dir="ltr">$339.53M</bdi> بتاريخ 28 مايو 2026. لا PDF يطلب منك الثقة، ولا عرض مسرحي للاحتياطيات. المحافظ مقروءة علناً، أي شخص لديه اتصال بالإنترنت يمكنه مراجعتها. <a href="/ar/reserves/" style="color:var(--gold);">الفاتورة، بحضورك.</a></p></div>
        <div class="club-card"><h3>للبيت وجه معروف</h3><p>Ed Craven (ملبورن، مولود 1995) وBijan Tehrani. التقيا على RuneScape، وأسسا Stake عام 2017، وأطلقا Kick عام 2022. ثروتهما المشتركة تُقدَّر بـ <bdi dir="ltr">US$5.6B</bdi> وفق Forbes. ليسا وراء ستار.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">خمس غرف، <span class="text-gradient-gold">رمز واحد</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">اختر بابك. MAX3000 صالح في الخمسة. لا يهم الموزع أين تصرف مكافأتك.</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));"><a href="/ar/casino/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">كازينو</div></a><a href="/ar/sports/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-sports-2.avif') type('image/avif'), url('/images/girl-sports-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">رياضة</div></a><a href="/ar/poker/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-poker-2.avif') type('image/avif'), url('/images/girl-poker-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">بوكر</div></a><a href="/ar/aviator/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-aviator-2.avif') type('image/avif'), url('/images/girl-aviator-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">أفياتور</div></a><a href="/ar/live-odds/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-lucky-drive-2.avif') type('image/avif'), url('/images/girl-lucky-drive-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">مباشر</div></a></div>
    </div>
  </section>
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title"><bdi dir="ltr">$3,000</bdi>. <span class="text-gradient-gold">شرط مراهنة 40x.</span> رمز واحد.</h2>
      <p class="girl-break-sub">اهمس بالرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للموزع عند التسجيل. الحسابات في صفك قبل أن تصل أول مشروب.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">أعطِ الرمز للموزع</a>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">ما يعرفه <span class="text-gradient-gold">النادي</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">المؤسسان</div><div class="ic-value"><bdi dir="ltr">Craven &amp; Tehrani</bdi></div><div class="ic-detail">Ed Craven (مولود 1995، ملبورن) وBijan Tehrani. التقيا على RuneScape. أسسا Stake عام 2017. أطلقا Kick عام 2022.</div></div>
        <div class="intel-card"><div class="ic-label">الكيان التشغيلي</div><div class="ic-value"><bdi dir="ltr">Medium Rare NV</bdi></div><div class="ic-detail">شركة كوراساو التي تُشغِّل Stake.com. الشركة الأم: Easygo Group Holdings، إيرادات FY2025 بلغت A$970M. Stake.us كيان سويبستيكس منفصل.</div></div>
        <div class="intel-card"><div class="ic-label">الترخيص</div><div class="ic-value"><bdi dir="ltr">Curaçao OGL/2024/1451/0918</bdi></div><div class="ic-detail">يغطي معظم الدول. انسحبت من المملكة المتحدة مارس 2025. محظورة في الولايات المتحدة (Stake.us السويبستيكس متاح في أكثر من 37 ولاية). أكثر من 22 موقع مرآة موثق.</div></div>
        <div class="intel-card"><div class="ic-label">الاحتياطيات</div><div class="ic-value"><bdi dir="ltr">$339.53M</bdi></div><div class="ic-detail">Arkham الموسوم بتاريخ 28 مايو 2026. Ethereum 74%، Solana 14%، أرصدة ستيبل كوين ضخمة. قابل للتتبع عبر cryptotips.com.</div></div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">بابان، <span class="text-gradient-gold">رمز واحد</span></h2>
        <p class="section-subtitle">MAX3000 معترف به على كلٍّ من Stake.com وStake.us. ما يستقبلك خلف كل باب مختلف. الموزع سيرشدك إلى الباب الصحيح بحسب بلد إقامتك.</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3>Stake.com - أموال حقيقية، عالمي</h3>
          <p>منصة الأموال الحقيقية التي تُشغِّلها Medium Rare NV بموجب ترخيص كوراساو OGL/2024/1451/0918. عملات رقمية وعملات قانونية. رياضة، كازينو، ألعاب أصلية، بوكر. مع الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> تحصل على <strong>200% حتى <bdi dir="ltr">$3,000</bdi></strong>، شرط مراهنة 40x على مجموع الإيداع والمكافأة، 30 يوماً، حد أدنى للإيداع <bdi dir="ltr">$10</bdi>. تواصل مع الدعم المباشر بعد الإيداع. يستلزم KYC المستوى 3. متاح في معظم الدول عدا الولايات المتحدة والمملكة المتحدة.</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">افتح الباب العالمي</a>
        </div>
        <div class="club-card">
          <h3>Stake.us - سويبستيكس، الولايات المتحدة</h3>
          <p>منصة السويبستيكس الأمريكية التي تُشغِّلها Sweepsteaks Limited. Gold Coins للعب، وStake Cash قابلة للاستبدال بعد 3x من رأس المال. لا إيداع أو سحب حقيقي، لا رياضة، كازينو فقط. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك أيضاً <strong>560,000 GC + 56 SC + 3.5% ريك باك</strong>. متاح في 37 ولاية.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">افتح الباب الأمريكي</a>
        </div>
      </div>
    </div>
  </section>
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">من عند المدخل</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل MAX3000 أكبر رمز مكافأة لـ Stake؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. مكافأة 200% حتى $3,000 مع شرط مراهنة 40x على مجموع الإيداع والمكافأة. معظم الرموز العامة تقف عند 100% / $1,000. MAX3000 هو ما يُقدمه النادي عند المدخل.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل Stake.com موثوق؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>تعمل Stake تحت ترخيص كوراساو OGL/2024/1451/0918 بموجب شركة Medium Rare NV منذ 2017. الاحتياطيات على السلسلة بلغت $339.53M بتاريخ 28 مايو 2026 وتخضع للتتبع العلني على Arkham. المؤسسان Ed Craven (ملبورن، 1995) وBijan Tehrani يديران Kick أيضاً.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">كيف يمكن التحقق من احتياطيات Stake؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>تفضل بزيارة <a href='/ar/reserves/'>صفحة الاحتياطيات</a>. لقطة 28 مايو 2026 تُظهر $339.53M في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%، أرصدة ستيبل كوين ضخمة. كل شيء قابل للتتبع عبر <a href='https://cryptotips.com/on-chain/stake/' target='_blank' rel='noopener'>cryptotips.com</a>.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">أين يمكنني اللعب؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>يغطي ترخيص كوراساو معظم الدول لكن Stake تفرض قيوداً ذاتية في بعضها. تفضل بزيارة <a href='/ar/mirror/'>صفحة مواقع المرآة</a> للعثور على النطاق المناسب لمنطقتك.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما مدى سرعة السحب؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>عمليات سحب العملات الرقمية تكتمل في 30 دقيقة إلى ساعة في ظروف عادية. TRX وXRP وSOL تُسوَّى في ثوانٍ إلى دقائق. عمليات السحب الكبيرة قد تستلزم 2 إلى 4 أيام عمل للمراجعة. سحوبات MoonPay القانونية تستغرق 1 إلى 5 أيام عمل. راجع <a href='/ar/payments/'>صفحة المدفوعات</a> للتفاصيل.</p></div>
        </div>
      </div>
    </div>
  </section>
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر الموزع أن وينرز كلوب أرسلك.</p>
    </div>
  </section>
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">الرمز هو <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. 200% حتى <bdi dir="ltr">$3,000</bdi>. باب Stake.com مفتوح</div>
    <div class="sticky-cta-actions">
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">احجز مكانك &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="إغلاق">&times;</button>
  </div>'''

    return build_head(title, desc, path_seg, og_image='default.png', page_slug='index', extra_jsonld=jsonld) + '\n' + build_header('/ar/') + '\n' + content + '\n' + FOOTER_HTML + '\n' + build_footer_scripts() + '\n' + ROOMS_GRID + '\n</body>\n</html>'


def page_promo_code():
    slug = 'promo-code'
    title = 'رمز Stake الترويجي MAX3000 - مكافأة 200% حتى $3,000 عند التسجيل'
    desc = 'رمز Stake الترويجي MAX3000: 200% على أول إيداع، حتى $3,000 مكافأة، شرط مراهنة 40x على الإيداع والمكافأة، KYC المستوى 3 مطلوب. تم التحقق يونيو 2026. آلة حاسبة مباشرة.'
    path_seg = 'promo-code/'

    jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "رمز Stake الترويجي MAX3000: 200% حتى $3,000",
  "description": "رمز Stake الترويجي MAX3000، 200% على أول إيداع، حتى $3,000، شرط مراهنة 40x على الإيداع والمكافأة. KYC المستوى 3 مطلوب. تم التحقق يونيو 2026.",
  "url": "https://winnersclub.com/ar/promo-code/"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://winnersclub.com/ar/"},
    {"@type": "ListItem", "position": 2, "name": "الرمز الترويجي", "item": "https://winnersclub.com/ar/promo-code/"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Offer",
  "name": "رمز Stake الترويجي MAX3000",
  "description": "200% على أول إيداع في Stake.com، حتى $3,000 مكافأة. حد أدنى للإيداع $10، حد أقصى للتأهل $1,500. شرط مراهنة 40x على مجموع الإيداع والمكافأة. KYC المستوى 3 مطلوب. للعملاء الجدد فقط.",
  "areaServed": "عالمياً (باستثناء الولايات المتحدة والمملكة المتحدة وأستراليا وأجزاء من أوروبا)",
  "url": "https://winnersclub.com/ar/promo-code/",
  "priceCurrency": "USD",
  "price": "0",
  "seller": {"@type": "Organization", "name": "Stake.com"}
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "ما هو الرمز الترويجي لـ Stake.com؟", "acceptedAnswer": {"@type": "Answer", "text": "الرمز هو MAX3000. سجِّل على Stake.com عبر رابط الشراكة، أكمل KYC المستوى 3، أودع ما بين $10 و$1,500 كأول إيداع، ثم افتح الدردشة المباشرة وأبلغهم برمز MAX3000. يتحقق الدعم من أهليتك ويُضيف مكافأة 200% حتى $3,000 خلال 24 إلى 48 ساعة."}},
    {"@type": "Question", "name": "ما الحد الأقصى لمكافأة MAX3000؟", "acceptedAnswer": {"@type": "Answer", "text": "مكافأة 200% تصل حتى $3,000. إيداع $1,500 يمنحك كامل $3,000. الحد الأدنى للتأهل $10 والحد الأقصى $1,500. الإيداعات التي تتجاوز $1,500 تُعالَج لكن المكافأة لا تزيد."}},
    {"@type": "Question", "name": "ما شرط المراهنة؟", "acceptedAnswer": {"@type": "Answer", "text": "40x على مجموع الإيداع والمكافأة. مثال: إيداع $500 يُنتج مكافأة $1,000، مجموع $1,500 × 40 = $60,000 مراهنة مطلوبة. العاب الكازينو ذات ميزة البيت 4% وما فوق تساهم بنسبة 100%، المراهنات الرياضية بنسبة 75%."}},
    {"@type": "Question", "name": "هل التحقق من الهوية ضروري؟", "acceptedAnswer": {"@type": "Answer", "text": "نعم. تطلب Stake.com KYC المستوى 3 قبل صرف مكافأة الترحيب. ادخل على الإعدادات ثم التحقق، وقدِّم وثيقة هوية مع صورة وإثبات عنوان ووثائق مصدر الأموال. لن تُصرف المكافأة إلا بعد اجتياز المستوى 3."}},
    {"@type": "Question", "name": "كيف تُصرف المكافأة؟", "acceptedAnswer": {"@type": "Answer", "text": "ليست رمزاً مرجعياً تلقائياً بل رصيد يُضاف يدوياً من قِبل المشغّل. بعد الإيداع افتح الدردشة المباشرة لـ Stake وأخبرهم أنك سجلت برمز MAX3000. يُضاف 200% خلال 24 إلى 48 ساعة بعد التحقق."}}
  ]
}
</script>'''

    content = f'''  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-promo-3.avif') type('image/avif'), url('/images/girl-promo-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">إن وجدت هذه الصفحة، فقد وجدت الرمز.</p>
        <h1 class="ch-title text-gradient-gold">الرمز الترويجي <bdi dir="ltr">MAX3000</bdi> لـ <bdi dir="ltr">Stake.com</bdi><span class="h1-sub">200% حتى $3,000 على Stake.com.</span></h1>
        <p class="ch-sub">الرمز هو <bdi dir="ltr">MAX3000</bdi>. مكافأة 200% على أول إيداع حتى <bdi dir="ltr">$3,000</bdi>. شرط مراهنة 40x على الإيداع والمكافأة. KYC المستوى 3 مطلوب للمطالبة. اللاعبون الأمريكيون لديهم <a href="/ar/stake-us-bonus/" style="color:var(--gold);text-decoration:underline;">ترحيب Stake.us السويبستيكس</a> بالرمز ذاته على منصة مختلفة.</p>
        <time datetime="2026-06-18" class="verified-stamp">آخر تحقق: 18 يونيو 2026</time>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">استخدم MAX3000 على Stake.com</a>
          <a href="#calculator" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">احسب مكافأتك</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">رمز النادي</div>
        <div class="code-display">MAX3000</div>
        <div class="code-meta">200% &middot; حتى <bdi dir="ltr">$3,000</bdi> مكافأة &middot; حد أدنى للإيداع <bdi dir="ltr">$10</bdi> &middot; شرط مراهنة 40x &middot; KYC المستوى 3 مطلوب &middot; عملاء جدد فقط +18</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAX3000">نسخ الرمز</button>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">أعطِ الرمز للموزع &rarr;</a>
        </div>
      </div>
    </div></section>

  <section class="section" id="calculator">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">آلة حاسبة <span class="text-gradient-gold">مكافأة Stake.com</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">حرِّك المنزلق. الحساب دقيق: إيداع بين $10 و$1,500، مكافأة 200% تصل حتى $3,000، شرط 40x على مجموع الإيداع والمكافأة.</p>
      </div>
      <div class="bonus-calc">
        <h3>مبلغ أول إيداع على Stake.com</h3>
        <div class="bonus-calc-input">
          <label for="depAmount">مبلغ الإيداع (USD)</label>
          <input type="range" id="depRange" min="10" max="1500" step="10" value="500">
          <input type="number" id="depAmount" min="10" max="1500" step="10" value="500">
        </div>
        <div class="bonus-calc-row">
          <div class="stat">
            <p class="stat-label">المكافأة المُقدَّمة</p>
            <p class="stat-value" id="bonusOut">$1,000</p>
            <p class="stat-sub">200% من الإيداع، حد أقصى $3,000</p>
          </div>
          <div class="stat">
            <p class="stat-label">متطلبات المراهنة</p>
            <p class="stat-value" id="wagerOut">$60,000</p>
            <p class="stat-sub">(الإيداع + المكافأة) × 40</p>
          </div>
          <div class="stat">
            <p class="stat-label">إجمالي الرصيد القابل للعب</p>
            <p class="stat-value" id="totalOut">$1,500</p>
            <p class="stat-sub">الإيداع + المكافأة</p>
          </div>
          <div class="stat">
            <p class="stat-label">كفاءة المطابقة</p>
            <p class="stat-value" id="effOut">200%</p>
            <p class="stat-sub">تنخفض عند تجاوز حد $1,500</p>
          </div>
        </div>
        <p class="bonus-calc-footer"><strong style="color:var(--gold);">الحد الأقصى للمكافأة هو $3,000.</strong> إيداع $1,500 يمنحك كامل $3,000. الإيداعات الأعلى تُعالَج لكن المكافأة لا تزيد عن $3,000.</p>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="bonus-calc-cta">المطالبة بـ MAX3000 على Stake.com &rarr;</a>
      </div>

      <div class="eligibility-grid">
        <div class="item"><strong>العمر</strong><span>18 عاماً فما فوق (21+ في بعض المناطق)</span></div>
        <div class="item"><strong>نوع العميل</strong><span>عملاء جدد فقط، أول إيداع فقط</span></div>
        <div class="item"><strong>الحد الأدنى للإيداع</strong><span>$10 أو ما يعادلها بالعملات الرقمية</span></div>
        <div class="item"><strong>الحد الأقصى للمكافأة</strong><span>$3,000 (عند إيداع $1,500)</span></div>
        <div class="item"><strong>KYC</strong><span>المستوى 3 مطلوب قبل صرف المكافأة</span></div>
        <div class="item"><strong>طريقة المطالبة</strong><span>تواصل مع الدعم المباشر بعد الإيداع</span></div>
        <div class="item"><strong>وقت الصرف</strong><span>24 إلى 48 ساعة بعد التحقق</span></div>
        <div class="item"><strong>تتبع التقدم</strong><span>تحقق من التقدم في تبويب VIP</span></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">مساعدة Stake، مكافأة الترحيب</a> · <a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">مساعدة Stake، مستويات KYC</a> · <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com، شروط MAX3000</a></p>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مقارنة جميع رموز <span class="text-gradient-gold">Stake النشطة</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">سبعة رموز، فائز واحد. لهذا السبب لا يوصي النادي إلا بـ MAX3000.</p></div>
      <table class="data-table" style="max-width:100%;overflow-x:auto;display:block;">
        <thead>
          <tr>
            <th>الرمز</th>
            <th>نسبة المطابقة</th>
            <th>الحد الأقصى للمكافأة</th>
            <th>أدوار مجانية</th>
            <th>الحد الأدنى للإيداع</th>
            <th>ريك باك فقط</th>
            <th>ملاحظات</th>
          </tr>
        </thead>
        <tbody>
          <tr class="win">
            <td><strong>MAX3000</strong></td>
            <td>200%</td>
            <td>$3,000</td>
            <td>لا</td>
            <td>$10</td>
            <td>لا</td>
            <td>رمز النادي. دعم مباشر يُضيف 200% يدوياً، شرط مراهنة 40x على الإيداع والمكافأة.</td>
          </tr>
          <tr>
            <td>NEWBONUS</td>
            <td>200%</td>
            <td>$3,000</td>
            <td>N/A</td>
            <td>$10</td>
            <td>لا</td>
            <td>رمز متاح عموماً، يعمل على جميع المرايا. لا أدوار.</td>
          </tr>
          <tr>
            <td>HELLA200</td>
            <td>200%</td>
            <td>$3,000</td>
            <td>N/A</td>
            <td>$50</td>
            <td>لا</td>
            <td>حد أدنى للإيداع أعلى. لا أدوار مجانية.</td>
          </tr>
          <tr>
            <td>STRAFECASVIP</td>
            <td>200%</td>
            <td>$2,000</td>
            <td>N/A</td>
            <td>$10</td>
            <td>لا</td>
            <td>شراكة Strafe. سقف أقل بـ $1,000 من MAX3000.</td>
          </tr>
          <tr>
            <td>HELLAGOOD</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>نعم (5%)</td>
            <td>ريك باك فقط. لا مطابقة على الإيداع.</td>
          </tr>
          <tr>
            <td>HELLAFREE</td>
            <td>N/A</td>
            <td>$1 بلا إيداع</td>
            <td>N/A</td>
            <td>لا يوجد</td>
            <td>لا</td>
            <td>$1 مجاني بعد KYC. قيمة ضئيلة.</td>
          </tr>
        </tbody>
      </table>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">دليل freetips.com لرموز Stake</a>, <a href="https://stake.com/promotions/welcome-offer" target="_blank" rel="noopener">شروط العرض الترحيبي من Stake</a></p>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">خطوات <span class="text-gradient-gold">المطالبة</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">التسجيل، التحقق، الإيداع، إبلاغ الدعم المباشر برمز MAX3000. المكافأة تُضاف يدوياً من قِبل المشغل.</p></div>
      <div class="step-cards anim-stagger" id="redeem">
        <div class="step-card"><h3>1. افتح الباب</h3><p>ادخل على <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener">Stake.com عبر رابط الشراكة</a> وانقر على التسجيل. البريد الإلكتروني، اسم المستخدم، كلمة المرور، تاريخ الميلاد.</p></div>
        <div class="step-card"><h3>2. التحقق حتى المستوى 3</h3><p>تشترط Stake <strong>KYC المستوى 3</strong> قبل صرف مكافأة الترحيب. ارفع وثيقة هوية مع صورة، وإثبات عنوان، ووثائق إضافية للمستوى 3. العرض الترحيبي مشروط باجتياز هذه المرحلة.</p></div>
        <div class="step-card"><h3>3. أودع المبلغ الأول (10 دولار فما فوق)</h3><p>أودع ما بين $10 و$1,500. مكافأة 200% تتناسب مع مبلغ الإيداع حتى سقف $3,000. الإيداع الأعلى من $1,500 يُعالَج لكن المكافأة لا تزيد.</p></div>
        <div class="step-card"><h3>4. اطلب MAX3000 عبر الدردشة المباشرة</h3><p>بعد تأكيد الإيداع افتح الدعم المباشر في Stake وأخبرهم أنك سجلت برمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> وتريد المطالبة بمكافأة الترحيب. بعد التحقق تُضاف مكافأة 200% خلال <strong>24 إلى 48 ساعة</strong>.</p></div>
      </div>
      <div class="club-body" style="margin-top:32px;padding:20px;background:var(--elevated);border-radius:10px;border-right:3px solid var(--gold);border-left:none;">
        <p style="margin:0;font-size:14px;color:var(--text-dim);"><strong style="color:var(--gold);">مهم:</strong> مكافأة الترحيب في Stake.com ليست رمزاً تُدخله في حقل إحالة تلقائي، بل رصيد يُضاف يدوياً من قِبل المشغل. سجِّل عبر رابط الشراكة، أكمل KYC المستوى 3، أودع، ثم افتح الدردشة المباشرة وأبلغهم برمز MAX3000. يمكن متابعة التقدم في شرط المراهنة (الإيداع + المكافأة) × 40 من <strong>تبويب VIP</strong> بعد التفعيل.</p>
      </div>
    </div>
  </section>

  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-promo-2.avif') type('image/avif'), url('/images/girl-promo-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">أكبر رمز <span class="text-gradient-gold">في الصالة</span></h2>
      <p class="girl-break-sub">اهمس بالرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للموزع. 200% حتى <bdi dir="ltr">$3,000</bdi> على Stake.com. فريق الدعم المباشر يتولى الباقي.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">أعطِ الرمز للموزع</a>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">هل تلعب <span class="text-gradient-gold">من الولايات المتحدة؟</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Stake.com محظورة في الولايات المتحدة. رمز MAX3000 يفتح أيضاً ترحيب Stake.us السويبستيكس لكن هيكل المكافأة مختلف تماماً: Stake Cash مجانية وGold Coins عند التسجيل، توزيع يومي مدى الحياة، 3x من رأس المال قبل الاستبدال.</p>
      </div>
      <div class="club-body" style="max-width:720px;margin:0 auto;text-align:center;">
        <p>منصة مختلفة، عملة مختلفة، شروط مختلفة. خصصنا صفحة منفصلة بآلة حاسبة وتفاصيل الأهلية.</p>
        <a href="/ar/stake-us-bonus/" class="btn btn-signup btn-gold-grad" style="margin-top:20px;display:inline-block;">افتح آلة حاسبة مكافأة Stake.us &rarr;</a>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الشروط بلغة <span class="text-gradient-gold">عربية واضحة</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">بلا حروف صغيرة مخفية في PDF. نشرح الشروط الفعلية بوضوح.</p></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>المراهنة: 40x على الإيداع والمكافأة معاً</h3>
          <p>شرط التداول لا يُطبَّق على المكافأة وحدها بل على <em>مجموع</em> الإيداع والمكافأة. إيداع $500 + مكافأة $1,000 = $1,500 × 40 = $60,000 مراهنة مطلوبة. احسب قبل أن تستهدف كامل المكافأة.</p>
        </div>
        <div class="club-card">
          <h3>KYC المستوى 3 إلزامي</h3>
          <p>تتدرج Stake في التحقق. المستوى 1 يتيح المراهنة، المستوى 2 يرفع حدود الإيداع، <strong>المستوى 3</strong> هو مرحلة التحقق الموثقة التي تفتح مكافأة الترحيب والسحوبات الكبيرة. ادخل على الإعدادات ثم التحقق لرفع وثيقة هويتك وإثبات العنوان ووثائق مصدر الأموال.</p>
        </div>
        <div class="club-card">
          <h3>نسبة مساهمة كل نوع من الألعاب</h3>
          <p>العاب الكازينو ذات ميزة البيت 4% وما فوق تساهم بنسبة 100%. المراهنات الرياضية بنسبة 75%. العاب الموزع المباشر والسلوتس ذات معدل العائد المرتفع (أقل من 4% ميزة بيت) تساهم بنسبة مخفضة أو صفر. ركِّز على Stake Originals والسلوتس ذات ميزة البيت +4%.</p>
        </div>
        <div class="club-card">
          <h3>طريقة الصرف</h3>
          <p>بعد أول إيداع تواصل مع الدعم المباشر وأبلغهم برمز MAX3000. يتحقق الدعم من KYC المستوى 3 ثم يُضيف مكافأة 200% خلال <strong>24 إلى 48 ساعة</strong>. لا يوجد حقل إدخال رمز إحالة تلقائي؛ مكافأة الترحيب تُضاف يدوياً من قِبل المشغل.</p>
        </div>
        <div class="club-card">
          <h3>للعملاء الجدد، أول إيداع فقط</h3>
          <p>MAX3000 ينطبق فقط على أول إيداع مؤهَّل في حساب Stake.com جديد. لا تُطبَّق بأثر رجعي على الحسابات القائمة، ولا تُطبَّق الإيداعات اللاحقة بموجب هذا العرض الترحيبي.</p>
        </div>
        <div class="club-card">
          <h3>الحد الأدنى للإيداع والدول المقيَّدة</h3>
          <p>الحد الأدنى للإيداع المُفعِّل هو $10، والحد الأقصى المؤهَّل للمكافأة هو $1,500. الولايات المتحدة والمملكة المتحدة (منذ مارس 2025) وأستراليا وأجزاء كبيرة من أوروبا مقيَّدة على stake.com. اللاعبون الأمريكيون لديهم <a href="/ar/stake-us-bonus/" style="color:var(--gold);">ترحيب Stake.us</a> المنفصل، وسائر المناطق يمكنها مراجعة <a href="/ar/mirror/" style="color:var(--gold);">صفحة المرايا</a> للنطاقات المتاحة.</p>
        </div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com رموز Stake</a>, <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">مساعدة Stake، مكافأة الترحيب</a></p>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">رموز سقوط المكافآت: <span class="text-gradient-gold">الميزة الخفية</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">خارج العرض الترحيبي، تُشغِّل Stake رموزاً مجانية محدودة الوقت. معظم اللاعبين يفوتهم هذا.</p></div>
      <div class="club-body">
        <p>رموز سقوط المكافآت هي رموز أبجدية رقمية قصيرة تُنشر على قنوات تيليغرام وحسابات التواصل الاجتماعي الرسمية لـ Stake. خلافاً لمكافأة الترحيب، لا يوجد عليها شرط مراهنة؛ القيمة المُودَعة نقد مجاني. لكنك تحتاج إلى رهانات بمبلغ معين خلال الأيام السبعة الماضية للتأهل، وتنتهي صلاحيتها بسرعة عندما يمتلئ حد المطالبة.</p>
        <p>القيمة المعتادة <strong>$1 إلى $5 لكل رمز</strong>، وتُنشر عدة رموز يومياً عبر قنوات متعددة. مجمَّعةً لا يمكن تجاهلها. كبار VIP من الذهب فما فوق يحصلون على رموز بقيم أعلى عبر البريد الإلكتروني وقنوات تيليغرام خاصة.</p>
        <p><strong>طريقة المطالبة:</strong> إعدادات الحساب ← العروض ← <em>مطالبة برمز المكافأة</em>، أدخل الرمز واضغط إرسال. لا حاجة لإيداع.</p>
      </div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:32px;">
        <div class="club-card">
          <h3>@StakecomDailyDrops</h3>
          <p>القناة الرئيسية على تيليغرام للرموز العامة. تُنشر عدة رموز يومياً. فعِّل الإشعارات لأن الرمز ينتهي فور امتلاء حد المطالبة.</p>
        </div>
        <div class="club-card">
          <h3>@StakeCasino</h3>
          <p>القناة الرسمية الرئيسية لـ Stake. إعلانات رسمية وعروض ترويجية أكبر. اشترك إلى جانب قناة الرموز.</p>
        </div>
        <div class="club-card">
          <h3>@Stake على X</h3>
          <p>يظهر أحياناً على فيد Stake في X/تويتر رموز سقوط خلال المناسبات الرياضية الكبرى والبطولات.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العروض المستمرة: <span class="text-gradient-gold">أكثر من $700,000 أسبوعياً</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">مكافأة الترحيب مجرد بداية. توزِّع Stake أكثر من 700,000 دولار أسبوعياً على اللاعبين الحاليين.</p></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));">
        <div class="club-card">
          <h3>سباق يومي بـ $100,000</h3>
          <p>يشارك جميع اللاعبين المسجلين تلقائياً دون الحاجة للتقديم. العب في الكازينو لتجمع نقاط المتصدرين. بنهاية الـ 24 ساعة، يتقاسم أفضل 5,000 لاعب الجائزة البالغة $100,000. السباق يُعاد تلقائياً، فكل تدوير يساهم في الدورة التالية.</p>
        </div>
        <div class="club-card">
          <h3>سحب أسبوعي بـ $75,000</h3>
          <p>تذكرة واحدة لكل $1,000 تراهن بها خلال فترة التأهل. لا حاجة للتقديم. تُسحَب جوائز $75,000 كل سبت الساعة 2 مساءً بتوقيت غرينيتش على بث مباشر. لا حد أقصى لتجميع التذاكر فاللاعبون الأكثر رهاناً ينتفعون أكثر.</p>
        </div>
        <div class="club-card">
          <h3>فتح الكازينو بـ $50,000</h3>
          <p>بعثات أسبوعية على الألعاب الجديدة والمميزة. أقل رهان مؤهَّل €0.10. تُوزَّع $50,000 أسبوعياً بين أعلى الرهانات وسقوط جوائز عشوائية.</p>
        </div>
        <div class="club-card">
          <h3>Pragmatic Drops &amp; Wins</h3>
          <p>تُشغِّل Stake هذا العرض الشبكي الشهير لـ Pragmatic Play: Sweet Bonanza وGates of Olympus 1000 وSugar Rush وغيرها. تسقط جوائز عشوائياً أثناء الدورات الحقيقية. أكثر من 50,000 جائزة تُوزَّع عبر الشبكة أسبوعياً. الرهان الحقيقي على الألعاب المؤهَّلة هو الشرط الوحيد.</p>
        </div>
        <div class="club-card">
          <h3>عروض تأمين الرياضة</h3>
          <p>عروض تأمين خاصة بالأحداث: دفع مبكر لـ NHL عند التقدم بهدفين، دفع مبكر لـ NBA بتقدم النصف، استرداد MLB للـ 9 أدوار، تأمين قرارات UFC المتقاربة، دفع مبكر للدوري الإنجليزي الممتاز، حماية باري الكومبو من Stake Shield، استرداد بعض سباقات الخيول.</p>
        </div>
        <div class="club-card">
          <h3>مكافأة إعادة شحن VIP</h3>
          <p>VIP من رتبة Platinum فما فوق يحصلون على مكافآت إعادة شحن: Platinum I كل 14 يوماً، Platinum IV دائماً. يُحسَب المبلغ بناءً على الخسائر الأخيرة فتأتيك إعادة الشحن أكبر في الفترات الصعبة. الجمعة هي اليوم الافتراضي لإعادة الشحن لرتب VIP الأدنى.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">من عند المدخل</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما هو الرمز الترويجي لـ Stake.com؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>الرمز هو <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. سجِّل عبر رابط الشراكة، أكمل KYC المستوى 3، أودع ما بين $10 و$1,500، ثم أبلغ الدعم المباشر برمز MAX3000. تُضاف مكافأة 200% حتى $3,000 خلال 24 إلى 48 ساعة.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما الحد الأقصى لمكافأة MAX3000؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>مكافأة 200% تصل حتى <strong>$3,000</strong>. إيداع $1,500 يمنحك كامل $3,000. الحد الأدنى للتأهل $10 والحد الأقصى $1,500. الإيداعات الأعلى تُعالَج لكن المكافأة لا تزيد عن $3,000.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما شرط المراهنة؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p><strong>40x على مجموع الإيداع والمكافأة.</strong> عند إيداع $500 تحصل على مكافأة $1,000، المجموع $1,500 يستلزم مراهنة $60,000. العاب الكازينو ذات ميزة بيت 4%+ تساهم بنسبة 100%، المراهنات الرياضية بنسبة 75%. التقدم يظهر في تبويب VIP.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل التحقق من الهوية ضروري؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. تطلب Stake.com <strong>KYC المستوى 3</strong> قبل صرف مكافأة الترحيب. ادخل على الإعدادات ثم التحقق وقدِّم وثيقة هوية مع صورة وإثبات عنوان ووثائق مصدر الأموال. لن تُصرف المكافأة إلا بعد اجتياز المستوى 3.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">كيف تُصرف المكافأة؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>مكافأة MAX3000 في Stake.com ليست إحالة تلقائية بل <strong>رصيد يُضاف يدوياً من قِبل المشغل</strong>. بعد الإيداع افتح الدردشة المباشرة وأبلغهم برمز MAX3000 واطلب مكافأة الترحيب. تُضاف مكافأة 200% خلال <strong>24 إلى 48 ساعة</strong>.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل تصلح للرياضة والكازينو معاً؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. مطابقة الإيداع تشمل الكازينو والرياضة والبوكر. المراهنات الرياضية تساهم بنسبة 75% في شرط المراهنة، العاب الكازينو ذات ميزة بيت 4%+ بنسبة 100%، الموزعون المباشرون والسلوتس ذات RTP المرتفع بنسبة مخفضة أو صفر.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">للعملاء الجدد فقط؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. MAX3000 ينطبق فقط على أول إيداع مؤهَّل في حساب Stake.com جديد. الحسابات القائمة لا يُطبَّق عليها بأثر رجعي، لكن يمكنها الاستفادة من رموز سقوط المكافآت المنشورة على تيليغرام Stake وهي لا تتطلب شرط مراهنة.</p></div>
        </div>
      </div>
    </div>
  </section>
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر الموزع أن وينرز كلوب أرسلك.</p>
    </div>
  </section>
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">الرمز هو <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. 200% حتى <bdi dir="ltr">$3,000</bdi> على Stake.com. أخبر الدعم المباشر بعد أول إيداع.</div>
    <div class="sticky-cta-actions">
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">احجز مكانك &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="إغلاق">&times;</button>
  </div>
  <script>
    (function(){{
      var range = document.getElementById('depRange');
      var num = document.getElementById('depAmount');
      var bonusOut = document.getElementById('bonusOut');
      var wagerOut = document.getElementById('wagerOut');
      var totalOut = document.getElementById('totalOut');
      var effOut = document.getElementById('effOut');
      if(!range || !num) return;
      var fmt = function(n){{ return '$' + Math.round(n).toLocaleString('en-US'); }};
      function recalc(){{
        var dep = parseFloat(num.value);
        if(isNaN(dep) || dep < 10) dep = 10;
        if(dep > 1500) dep = 1500;
        num.value = dep;
        range.value = dep;
        var bonus = Math.min(dep * 2, 3000);
        var total = dep + bonus;
        var wager = total * 40;
        var eff = (bonus / dep) * 100;
        bonusOut.textContent = fmt(bonus);
        wagerOut.textContent = fmt(wager);
        totalOut.textContent = fmt(total);
        effOut.textContent = Math.round(eff) + '%';
      }}
      range.addEventListener('input', function(){{ num.value = range.value; recalc(); }});
      num.addEventListener('input', recalc);
      num.addEventListener('change', recalc);
      recalc();
    }})();
  </script>'''

    return build_head(title, desc, path_seg, og_image='promo-code.png', page_slug='promo-code', extra_jsonld=jsonld) + '\n' + build_header('/ar/promo-code/') + '\n' + content + '\n' + FOOTER_HTML + '\n' + build_footer_scripts() + '\n' + ROOMS_GRID + '\n</body>\n</html>'


def make_simple_page(slug, title, desc, h1_ar, sub_ar, sections_html, og_image='default.png', extra_jsonld=''):
    """Generic builder for simpler pages."""
    path_seg = f'{slug}/' if slug != 'index' else ''
    bc_items = f'{{"@type":"ListItem","position":1,"name":"الرئيسية","item":"https://winnersclub.com/ar/"}}'
    if slug != 'index':
        bc_items += f',{{"@type":"ListItem","position":2,"name":"{title[:40]}","item":"https://winnersclub.com/ar/{slug}/"}}'

    base_jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebPage","name":"{title}","description":"{desc}","url":"https://winnersclub.com/ar/{path_seg}"}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{bc_items}]}}
</script>
{extra_jsonld}'''

    hero = f'''  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">{h1_ar}</h1>
        <p class="ch-sub">{sub_ar}</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">ادخل برمز <bdi dir="ltr">MAX3000</bdi></a>
          <a href="/ar/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">تفاصيل الرمز الترويجي</a>
        </div>
      </div>
    </div>
  </section>
  {TICKER}
  {PROMO_STRIP}'''

    sticky = '''  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">الرمز هو <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span>. 200% حتى <bdi dir="ltr">$3,000</bdi>. Stake.com</div>
    <div class="sticky-cta-actions">
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">احجز مكانك &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="إغلاق">&times;</button>
  </div>'''

    sig = '''  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر الموزع أن وينرز كلوب أرسلك.</p>
    </div>
  </section>'''

    return (build_head(title, desc, path_seg, og_image=og_image, page_slug=slug, extra_jsonld=base_jsonld) + '\n' +
            build_header(f'/ar/{path_seg}') + '\n' + hero + '\n' + sections_html + '\n' + sig + '\n' + sticky + '\n' +
            FOOTER_HTML + '\n' + build_footer_scripts() + '\n' + ROOMS_GRID + '\n</body>\n</html>')


def page_casino():
    slug = 'casino'
    title = 'كازينو Stake - أكثر من 3000 لعبة مع الرمز MAX3000'
    desc = 'كازينو Stake.com: أكثر من 3000 لعبة، سلوتس، كازينو مباشر، ألعاب أصلية. استخدم الرمز MAX3000 للحصول على 200% حتى $3,000. ترخيص كوراساو OGL/2024/1451/0918.'

    faq_jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":"كم عدد الألعاب في كازينو Stake؟","acceptedAnswer":{"@type":"Answer","text":"يضم كازينو Stake أكثر من 3,000 لعبة تشمل السلوتس والطاولات والموزعين المباشرين والألعاب الأصلية. يُضاف محتوى جديد أسبوعياً من أبرز موردي البرمجيات."}},
  {"@type":"Question","name":"هل يمكن استخدام رمز MAX3000 في الكازينو؟","acceptedAnswer":{"@type":"Answer","text":"نعم. مكافأة 200% حتى $3,000 تنطبق على الكازينو والرياضة والبوكر والألعاب الأصلية. العاب الكازينو ذات ميزة بيت 4%+ تساهم بنسبة 100% في شرط المراهنة."}}
]}
</script>'''

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مكتبة الكازينو: <span class="text-gradient-gold">أكثر من 3,000 لعبة</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>السلوتس</h3><p>أكثر من 2,000 سلوت من Pragmatic Play وHacksaw Gaming وPlay'n GO وNoLimit City وBigTimeGaming وEvolution. من Sweet Bonanza إلى Wanted Dead or A Wild. فلاتر RTP وقوائم المفضلة لإدارة مكتبتك.</p></div>
        <div class="club-card"><h3>الكازينو المباشر</h3><p>طاولات روليت وبلاك جاك وباكارا وبوكر مباشرة مع موزعين حقيقيين. Evolution Gaming هي المورد الأساسي. استوديو بث حصري لـ Stake مع موزعين على الهواء على مدار الساعة. حدود رهان تبدأ من $0.10 حتى ستة أرقام.</p></div>
        <div class="club-card"><h3>Stake Originals</h3><p>ألعاب مطوَّرة داخلياً حصراً: Crash وDice وPlinko وKeno وMines وLimbo وHilo. كل لعبة تُحقق نتائج قابلة للتتبع على السلسلة. نسبة إرجاع (RTP) من 97% إلى 99%. تساهم بنسبة 100% في شرط المراهنة.</p></div>
        <div class="club-card"><h3>ألعاب الطاولة الكلاسيكية</h3><p>بلاك جاك وروليت وباكارا وسيك بو وبوكر الكازينو بنسخ متعددة من عدة موردين. إصدارات الاحتمال المنخفض مثل Atlantic City Blackjack تساهم بنسبة مخفضة في شرط المراهنة - تحقق من قواعد الألعاب.</p></div>
        <div class="club-card"><h3>دفع المراهنات</h3><p>يمكنك اللعب بالبيتكوين وإيثريوم وليتكوين وريبل وتيثر وسولانا وعشرات العملات الرقمية الأخرى. تتوفر أيضاً طرق دفع قانونية عبر MoonPay. لا حد أدنى للسحب بالعملات الرقمية. يُضاف إيداعك فوراً.</p></div>
        <div class="club-card"><h3>ضمان الشفافية</h3><p>تستخدم ألعاب Stake Originals مولِّد أرقام عشوائي قابل للإثبات (Provably Fair) يمكنك التحقق منه. تعرض كل لعبة نسبة RTP الخاصة بها. قسم التحليلات يُظهر سجل رهاناتك، ومتوسط RTP الفعلي، وإجمالي المراهنات.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العروض الترويجية <span class="text-gradient-gold">في الكازينو</span></h2></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>سباق $100,000 اليومي</h3><p>جميع اللاعبين المسجلين يشاركون تلقائياً. العب في الكازينو لجمع نقاط المتصدرين. أفضل 5,000 لاعب يتقاسمون $100,000 كل 24 ساعة. السباق يُعاد تلقائياً.</p></div>
        <div class="club-card"><h3>فتح الكازينو: $50,000 أسبوعياً</h3><p>بعثات أسبوعية على الألعاب الجديدة والمميزة بحد أدنى €0.10 للرهان المؤهَّل. $50,000 تُوزَّع أسبوعياً بين أعلى الرهانات وسقوط الجوائز العشوائية.</p></div>
        <div class="club-card"><h3>Pragmatic Drops &amp; Wins</h3><p>أكثر من 50,000 جائزة عبر الشبكة أسبوعياً على ألعاب Pragmatic Play المؤهَّلة. جوائز تسقط أثناء الدورات الحقيقية. Sweet Bonanza وGates of Olympus 1000 ضمن الألعاب المشاركة.</p></div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">موردو البرمجيات <span class="text-gradient-gold">الرئيسيون</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">السلوتس</div><div class="ic-value">Pragmatic Play</div><div class="ic-detail">الشريك الأبرز. Sweet Bonanza وGates of Olympus وSugar Rush ضمن أكثر من 200 عنوان على Stake.</div></div>
        <div class="intel-card"><div class="ic-label">الكازينو المباشر</div><div class="ic-value">Evolution Gaming</div><div class="ic-detail">المورد الرائد عالمياً للألعاب المباشرة. روليت وبلاك جاك وباكارا وألعاب مباشرة أخرى. بث عالي الجودة.</div></div>
        <div class="intel-card"><div class="ic-label">سلوتس متميزة</div><div class="ic-value">NoLimit City</div><div class="ic-detail">Wanted Dead or A Wild وMemento وmental ضمن عروض الخطر العالي ذات تعدد المضاعفات.</div></div>
        <div class="intel-card"><div class="ic-label">الأصليات</div><div class="ic-value">Stake In-House</div><div class="ic-detail">Crash وDice وPlinko وMines وKeno وLimbo وHilo. Provably Fair، قابلة للتتبع، RTP 97-99%.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">كيف تُعظِّم <span class="text-gradient-gold">مكافأتك في الكازينو</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>ركِّز على الألعاب ذات ميزة البيت +4%</h3><p>شرط المراهنة يُستوفى أسرع بالألعاب ذات ميزة بيت 4% وما فوق لأنها تساهم بنسبة 100%. الموزعون المباشرون والسلوتس ذات RTP المرتفع (ميزة بيت أقل من 4%) تساهم بنسبة مخفضة أو صفر.</p></div>
        <div class="club-card"><h3>Stake Originals خيار ممتاز</h3><p>Crash وDice وMines وPlinko تساهم بنسبة 100% في شرط المراهنة مع RTP يبدأ من 97%. إستراتيجية ثابتة الرهان تُبقي الانكشاف متوقعاً. تتبَّع تقدمك في تبويب VIP.</p></div>
        <div class="club-card"><h3>السباق اليومي: نقاط مجانية</h3><p>سباق $100,000 اليومي يمنحك قيمة إضافية مجانية على كل رهان في الكازينو. لا حاجة للتقديم. كل لعبة تُضيف نقاطاً في المتصدرين يُعيَّد حسابها كل 24 ساعة.</p></div>
      </div>
    </div>
  </section>
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">حول الكازينو</span></h2></div>
      <div class="faq-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">كم عدد الألعاب في كازينو Stake؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>أكثر من 3,000 لعبة تشمل السلوتس والطاولات والموزعين المباشرين والألعاب الأصلية من أبرز موردي البرمجيات. يُضاف محتوى جديد أسبوعياً.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">هل يمكن استخدام MAX3000 في الكازينو؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>نعم. مكافأة 200% حتى $3,000 صالحة في الكازينو والرياضة والبوكر. العاب ذات ميزة بيت 4%+ تساهم بنسبة 100%.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">هل ألعاب Stake عادلة؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>الألعاب الأصلية تستخدم Provably Fair وهو نظام تشفيري يمكنك التحقق منه. الموردون الخارجيون (Evolution وPragmatic) مرخصون ومراجَعون من جهات مستقلة. Stake مرخصة بموجب كوراساو OGL/2024/1451/0918.</p></div></div>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'كازينو <bdi dir="ltr">Stake</bdi> - أكثر من 3,000 لعبة',
        'من السلوتس إلى الموزعين المباشرين. استخدم الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> للحصول على مكافأة 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png', extra_jsonld=faq_jsonld)


def page_sports():
    slug = 'sports'
    title = 'مراهنات Stake الرياضية - كرة القدم والبطولات العالمية مع MAX3000'
    desc = 'مراهنات Stake الرياضية: أكثر من 40 رياضة، تغطية مباشرة، أرباح تنافسية. الرمز MAX3000 يفتح 200% حتى $3,000. ترخيص كوراساو OGL/2024/1451/0918.'

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المراهنات الرياضية على <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>أكثر من 40 رياضة</h3><p>كرة القدم، كرة السلة، التنس، الهوكي، البيسبول، كرة اليد، الكريكيت، الرغبي، الملاكمة، MMA، ألعاب الفيديو التنافسية، سباقات الخيول وغيرها. تغطية شاملة للبطولات الكبرى عالمياً.</p></div>
        <div class="club-card"><h3>مراهنة مباشرة</h3><p>أرباح تتغير لحظة بلحظة أثناء المباريات. رهانات خاصة بالأحداث المباشرة: تسجيل الهدف التالي، بطل الشوط، الفائز بالمجموعة. إحصاءات مباشرة مدمجة في واجهة المراهنة.</p></div>
        <div class="club-card"><h3>كومبو متعدد الأحداث</h3><p>ادمج ما يصل إلى 20 حدثاً في تحديد واحد متراكم. عوامل الضرب تجعل مبالغ المكافآت ضخمة على حساب الاحتمال. Stake Shield يحمي من خسارة حدث واحد في بعض الكومبوهات.</p></div>
        <div class="club-card"><h3>كرة القدم: الدوريات الكبرى</h3><p>الدوري الإنجليزي الممتاز، دوري أبطال أوروبا، الليغا، البوندسليغا، الدوري الفرنسي، الدوري الإيطالي، الدوريات الأمريكية وأمريكا اللاتينية. تغطية كاملة من البطولات الكبرى حتى الدرجات الدنيا.</p></div>
        <div class="club-card"><h3>المراهنات بالعملات الرقمية</h3><p>ضع رهاناتك بالبيتكوين وإيثريوم وليتكوين وريبل وتيثر وسولانا وعشرات العملات الأخرى. يُودَع الرهان فوراً. تُستوفى السحوبات بالعملات الرقمية خلال 30 دقيقة إلى ساعة في الظروف الاعتيادية.</p></div>
        <div class="club-card"><h3>الأرباح والسوق</h3><p>أرباح Stake تنافسية مع تغطية ضيقة للفارق على الأحداث الكبرى. إحصاءات مقارنة الأرباح تُظهر لك موقف Stake مقارنةً بالسوق. راجع صفحة الأرباح المباشرة لأرقام في الوقت الفعلي.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">عروض تأمين <span class="text-gradient-gold">الرياضة</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">هوكي الجليد (NHL)</div><div class="ic-value">تقدم 2-0 يُدفع مبكراً</div><div class="ic-detail">إذا تقدم فريقك بهدفين في الثلثين الأول أو الثاني يُدفع الرهان مبكراً حتى لو عادل الخصم أو فاز.</div></div>
        <div class="intel-card"><div class="ic-label">كرة السلة (NBA)</div><div class="ic-value">دفع مبكر بتقدم نصف المباراة</div><div class="ic-detail">يتقدم فريقك بـ 12 نقطة أو أكثر لحظة الصافرة في منتصف المباراة، ويُدفع رهانك فوراً.</div></div>
        <div class="intel-card"><div class="ic-label">البيسبول (MLB)</div><div class="ic-value">استرداد 9 أدوار</div><div class="ic-detail">إذا اتعادلت المباراة بعد 9 أدوار منتظمة يسترد رهانك بالكامل.</div></div>
        <div class="intel-card"><div class="ic-label">كرة القدم (الدوري الإنجليزي الممتاز)</div><div class="ic-value">دفع مبكر بتقدم 2-0</div><div class="ic-detail">كما في NHL، يُدفع رهانك مبكراً عند تقدم الفريق بهدفين حتى لو انتهت المباراة بنتيجة مختلفة.</div></div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">MAX3000 و<span class="text-gradient-gold">الرياضة</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>مكافأة الترحيب صالحة للرياضة</h3><p>رمز MAX3000 يمنحك مكافأة 200% حتى $3,000 صالحة للاستخدام في الرياضة والكازينو. المراهنات الرياضية تساهم بنسبة 75% في شرط المراهنة البالغ 40x على مجموع الإيداع والمكافأة.</p></div>
        <div class="club-card"><h3>إستراتيجية المزج</h3><p>لتحقيق كفاءة أعلى في استيفاء شرط المراهنة امزج بين الرياضة والكازينو. الكازينو (100%) يستوفي الشرط أسرع، لكن الرياضة تُضيف تنوعاً وإثارة. جرِّب الكومبو متعدد الرياضات لتضخيم الأرباح.</p></div>
        <div class="club-card"><h3>سباق المتصدرين اليومي</h3><p>رهانات السبورت أيضاً تتراكم في سباق الـ $100,000 اليومي. كل 1,000 دولار رهان تحصل على تذكرة في السحب الأسبوعي الذي يوزع $75,000 كل سبت.</p></div>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'المراهنات الرياضية على <bdi dir="ltr">Stake</bdi>',
        'أكثر من 40 رياضة، مراهنة مباشرة، عروض تأمين. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png')


def page_poker():
    slug = 'poker'
    title = 'بوكر Stake - Texas Hold\'em ومزيد مع الرمز MAX3000'
    desc = 'بوكر Stake.com: Texas Hold\'em وOmaha ومزيد. مباريات حية، برامج VIP، رمز MAX3000 يفتح 200% حتى $3,000.'

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">طاولات بوكر <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Texas Hold'em</h3><p>أشهر صيغ البوكر في العالم. طاولات بحدود رهان متعددة من ميكرو ستيكس حتى نوشتي عالٍ. مباريات Sit & Go وتورنامنتات مجدولة متاحة على مدار الساعة. واجهة نظيفة تُظهر بطاقات المجتمع وإجراءات اللاعبين بوضوح.</p></div>
        <div class="club-card"><h3>Omaha</h3><p>Pot Limit Omaha (PLO) الأكثر حدة من Texas Hold'em. تحصل على أربع بطاقات بدلاً من اثنتين مما يزيد احتمالات التقوية ويرفع حجم الأوعية. طاولات PLO و PLO Hi/Lo متاحة بحدود متعددة.</p></div>
        <div class="club-card"><h3>مكافأة الترحيب صالحة للبوكر</h3><p>رمز MAX3000 ينطبق على الوعاء في بوكر Stake. المساهمة في شرط المراهنة تعتمد على نوع الرهان في طاولة البوكر. تفقد صفحة الرمز الترويجي للتفاصيل الكاملة حول نسب المساهمة.</p></div>
        <div class="club-card"><h3>VIP والريك باك</h3><p>لاعبو البوكر يتأهلون لبرنامج VIP الكامل. يُحتسب كل رهان في الوعاء ضمن حجم الرهان الشهري الإجمالي الذي يرفع رتبتك في VIP. رتب Platinum وDiamond تُطلق ريك باك أسبوعياً ومكافآت إعادة شحن.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">برامج البوكر <span class="text-gradient-gold">الخاصة</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">حجم الطاولة</div><div class="ic-value">6 إلى 9 لاعبين</div><div class="ic-detail">طاولات سداسية وتسعية متاحة بحدود مختلفة. يتسارع إيقاع اللعب في الطاولات الصغيرة.</div></div>
        <div class="intel-card"><div class="ic-label">أصغر حد</div><div class="ic-value">$0.01/$0.02</div><div class="ic-detail">طاولات ميكرو متاحة للمبتدئين. يمكن إيداع حد أدنى والجلوس بـ 20 سنتاً.</div></div>
        <div class="intel-card"><div class="ic-label">التورنامنتات</div><div class="ic-value">Sit & Go + مجدولة</div><div class="ic-detail">تورنامنتات Sit & Go تنطلق فور امتلاء الطاولة. التورنامنتات المجدولة بجوائز مضمونة.</div></div>
        <div class="intel-card"><div class="ic-label">العملة</div><div class="ic-value">العملات الرقمية والقانونية</div><div class="ic-detail">العب بالبيتكوين أو إيثريوم أو دولار. يُعرض الرصيد بالعملة المختارة لكل طاولة.</div></div>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'بوكر <bdi dir="ltr">Stake</bdi> - طاولات حية وتورنامنتات',
        '<bdi dir="ltr">Texas Hold\'em</bdi> وOmaha ومزيد. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png')


def page_aviator():
    slug = 'aviator'
    title = 'أفياتور Stake - لعبة التحطق مع الرمز MAX3000'
    desc = 'لعبة أفياتور على Stake.com: راهن وحدد لحظة انسحابك قبل أن تتحطق الطائرة. مضاعف ينمو حتى 10,000x. الرمز MAX3000 يفتح 200% حتى $3,000.'

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">كيف تعمل <span class="text-gradient-gold">لعبة أفياتور</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>آلية اللعبة</h3><p>تقلع طائرة وينطلق مضاعف في النمو من 1x. راهن أي مبلغ واضغط على "سحب" في أي لحظة لتحجز ربحك. إن لم تسحب قبل التحطق، تخسر رهانك. الطاولة مشتركة، يرى جميع اللاعبين المضاعف نفسه في الوقت الفعلي.</p></div>
        <div class="club-card"><h3>المضاعفات</h3><p>المضاعف قد ينتهي عند 1.01x أو يصل إلى 10,000x. التوزيع يعتمد على Provably Fair. الإجماليات التاريخية قابلة للعرض في اللعبة. RTP الاسمي حوالي 97% مع تباين عالٍ.</p></div>
        <div class="club-card"><h3>السحب التلقائي</h3><p>حدد مضاعفاً مستهدفاً مسبقاً وسيسحب الرهان تلقائياً عند الوصول إليه. مثال: اضبط السحب التلقائي عند 2x وكل جولة ستتضاعف أرباحك إن لم تتحطق قبل 2x.</p></div>
        <div class="club-card"><h3>الرهان المزدوج</h3><p>افتح رهانين في وقت واحد على جولة واحدة. اسحب الرهان الأول عند 1.5x لضمان ربح جزئي، ودع الثاني يسير نحو مضاعفات أعلى. يُقلل المخاطر ويتيح تصيد الجوائز الكبيرة.</p></div>
        <div class="club-card"><h3>إحصاءات الجلسة</h3><p>تتبَّع ربحيتك اللحظية عبر جدول "إحصاءات جولتي". اعرض توزيع نقاط السحب التاريخية، ومعدل مضاعف التحطق، ومتوسط RTP الخاص بك.</p></div>
        <div class="club-card"><h3>الدردشة المباشرة</h3><p>اللعبة تعمل في غرفة مشتركة مع دردشة. اللاعبون يشاركون لحظات السحب الكبيرة ويتنافسون على القمم في لوحة المتصدرين اليومية.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أفياتور و<span class="text-gradient-gold">مكافأة MAX3000</span></h2></div>
      <div class="club-body">
        <p>مكافأة MAX3000 (200% حتى $3,000) صالحة لاستخدامها في أفياتور. لكن نسبة مساهمتها في شرط المراهنة البالغ 40x تعتمد على تصنيف Stake لميزة البيت في اللعبة. بما أن RTP الاسمي لأفياتور حوالي 97% فميزة البيت حوالي 3%، مما يضعها في نطاق المساهمة المخفضة في بعض الحالات. تحقق من صفحة شروط المكافأة في Stake للتأكد من نسبة المساهمة الدقيقة الحالية.</p>
        <p>نصيحة النادي: لاستيفاء شرط المراهنة بأكفأ طريقة ركِّز على ألعاب الكازينو ذات ميزة بيت 4%+ أو Stake Originals (Crash وDice وMines) التي تساهم بنسبة 100% ثم انتقل إلى أفياتور بعد ذلك للمتعة.</p>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'لعبة أفياتور على <bdi dir="ltr">Stake</bdi>',
        'راهن، وشاهد المضاعف ينمو، واسحب قبل التحطق. مضاعف يصل إلى 10,000x. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png')


def page_live_casino():
    slug = 'live-casino'
    title = 'الكازينو المباشر في Stake - موزعون حقيقيون مع MAX3000'
    desc = 'كازينو Stake المباشر: روليت وبلاك جاك وباكارا مع موزعين حقيقيين عبر Evolution Gaming. الرمز MAX3000 يفتح 200% حتى $3,000.'

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الكازينو المباشر على <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>روليت مباشرة</h3><p>روليت أوروبية وأمريكية وفرنسية ومزيد. موزعون حقيقيون في استوديوهات عالية الجودة. Speed Roulette وImmersive Roulette وAutomatic Roulette لمن يفضل وتيرة أسرع.</p></div>
        <div class="club-card"><h3>بلاك جاك مباشر</h3><p>Classic Blackjack وInfinite Blackjack وFree Bet Blackjack. طاولات بحدود رهان متنوعة. استوديو Stake حصري بطاولات مخصصة مع موزعين على الهواء 24/7.</p></div>
        <div class="club-card"><h3>باكارا مباشرة</h3><p>Mini Baccarat وPunto Banco والباكارا السريعة. سجل توزيع بطاقات يُظهر التاريخ. رهانات جانبية مثل Dragon Bonus وPerfect Pair.</p></div>
        <div class="club-card"><h3>ألعاب تلفزيونية مباشرة</h3><p>Crazy Time وDream Catcher وMonopoly Live وLightning Roulette من Evolution. ألعاب تفاعلية بمضاعفات عشوائية. خيار مثالي للاسترخاء بحدود رهان منخفضة نسبياً.</p></div>
        <div class="club-card"><h3>بوكر كازينو مباشر</h3><p>Casino Hold'em وThree Card Poker وUltimate Texas Hold'em. راهن ضد الكازينو لا ضد لاعبين آخرين. جوائز Progressive Jackpot على بعض الطاولات.</p></div>
        <div class="club-card"><h3>الحدود والعملات</h3><p>رهانات تبدأ من $0.10 على معظم الطاولات. الحد الأقصى يصل إلى ستة أرقام على طاولات VIP. اللعب بالعملات الرقمية والقانونية متاح. لا رسوم معاملات إضافية على الرهانات داخل الكازينو.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الكازينو المباشر و<span class="text-gradient-gold">شرط المراهنة</span></h2></div>
      <div class="club-body">
        <p>ألعاب الموزع المباشر في Stake تساهم بنسبة مخفضة أو صفر في شرط المراهنة البالغ 40x لمكافأة MAX3000 (هذا شرط معتاد لدى معظم الكازينوهات). الباكارا والبلاك جاك على وجه الخصوص عادةً ما تُصنَّف بنسبة مساهمة صفر أو منخفضة جداً بسبب انخفاض ميزة البيت.</p>
        <p>النصيحة العملية: استخدم مكافأتك في السلوتس أو Stake Originals أو الألعاب ذات ميزة البيت 4%+ لاستيفاء شرط المراهنة، ثم انتقل إلى الكازينو المباشر للاستمتاع بتجربة الموزع الحقيقي بعد ذلك.</p>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'الكازينو المباشر على <bdi dir="ltr">Stake</bdi>',
        'موزعون حقيقيون، روليت وبلاك جاك وباكارا. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png')


def page_live_odds():
    slug = 'live-odds'
    title = 'أرباح Stake المباشرة - تغطية لحظية للرياضة العالمية'
    desc = 'أرباح Stake المباشرة: تغطية لحظية لكرة القدم والبطولات الكبرى عالمياً. مقارنة الأرباح، تحليل القيمة. الرمز MAX3000 يفتح 200% حتى $3,000.'

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الأرباح المباشرة <span class="text-gradient-gold">على Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>كرة القدم: الدوريات الكبرى</h3><p>أرباح لحظية على الدوري الإنجليزي الممتاز ودوري أبطال أوروبا والليغا والبوندسليغا والدوري الفرنسي والإيطالي والدوريات الأمريكية. فارق ضيق على المباريات ذات الحجم التداولي العالي.</p></div>
        <div class="club-card"><h3>كرة السلة: NBA وEuroLeague</h3><p>أرباح ربع لحظية وتوتال مباشر. نوع رهانات "الشوط الأول" يتيح رهانات قصيرة المدى. إحصاءات مباشرة مدمجة في واجهة الرهان لمتابعة تسجيلات الفرق.</p></div>
        <div class="club-card"><h3>التنس: ATP وWTA وGrand Slam</h3><p>رهانات بالمباراة والمجموعة والتايبريك. أرباح تتغير بعد كل نقطة في المجموعات الحاسمة. تغطية الـ 4 Grand Slams كاملة مع أسواق خاصة.</p></div>
        <div class="club-card"><h3>الإي سبورت</h3><p>CS2 وDota 2 وLeague of Legends وValorant. أرباح الخريطة تتغير بعد كل جولة. تغطية البطولات الكبرى مثل ESL وMajors وTI. Stake أحد الكازينوهات الرائدة في تغطية الإي سبورت.</p></div>
        <div class="club-card"><h3>MMA والملاكمة</h3><p>UFC وBellator وONE Championship. أرباح المباراة الرئيسية تُنشر أسابيع مقدماً. رهانات الطريقة وجولة الإنهاء متاحة. التغييرات الأخيرة في الأرباح تعكس الأخبار من المعسكرات.</p></div>
        <div class="club-card"><h3>سباقات الخيول</h3><p>سباقات المملكة المتحدة وأيرلندا وأستراليا. أرباح SP (السعر المبدئي) وأرباح مبكرة. رهانات Each Way على السباقات بأكثر من 5 خيول. استرداد بعض السباقات المؤهلة.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">قراءة <span class="text-gradient-gold">الأرباح</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">أرباح أوروبية</div><div class="ic-value">العشري</div><div class="ic-detail">مثال 2.50 تعني مضاعفة الرهان 2.5x عند الفوز. $100 × 2.50 = $250 صافي العائد $150.</div></div>
        <div class="intel-card"><div class="ic-label">أرباح أمريكية</div><div class="ic-value">مونيلاين</div><div class="ic-detail">+150 تعني ربح $150 على $100. 150- تعني تخسر $150 للفوز بـ $100.</div></div>
        <div class="intel-card"><div class="ic-label">الهامش</div><div class="ic-value">فارق الكتاب</div><div class="ic-detail">الفرق بين الأرباح الحقيقية وما تدفعه Stake. الأحداث الكبرى تحمل هامشاً أضيق يعني قيمة أفضل.</div></div>
        <div class="intel-card"><div class="ic-label">تحرك الأرباح</div><div class="ic-value">إشارة السوق</div><div class="ic-detail">تراجع الأرباح قبل المباراة يعني أموالاً كبيرة تدعم ذلك الطرف. مراقبة الخطوط مهارة أساسية للمراهن.</div></div>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'الأرباح المباشرة على <bdi dir="ltr">Stake</bdi>',
        'تغطية لحظية لأكثر من 40 رياضة. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png')


def page_mirror():
    slug = 'mirror'
    title = 'موقع مرآة Stake - النطاقات البديلة stake.ac وstake.bet وstake.games'
    desc = 'مواقع مرآة Stake.com الرسمية: stake.ac وstake.bet وstake.games. الرمز MAX3000 يعمل على جميع النطاقات. 200% حتى $3,000.'

    faq_jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":"ما هي مواقع مرآة Stake الرسمية؟","acceptedAnswer":{"@type":"Answer","text":"المواقع البديلة الرسمية لـ Stake.com هي stake.ac وstake.bet وstake.games. جميعها تُشغِّلها Medium Rare NV ويعمل عليها رمز MAX3000 بالشروط ذاتها."}},
  {"@type":"Question","name":"هل رمز MAX3000 يعمل على مواقع المرآة؟","acceptedAnswer":{"@type":"Answer","text":"نعم. الرمز MAX3000 صالح على stake.com وstake.ac وstake.bet وstake.games وجميع النطاقات الرسمية الأخرى. شروط المكافأة والرمز ذاتها على جميع النطاقات."}}
]}
</script>'''

    sections = f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">النطاقات البديلة <span class="text-gradient-gold">الرسمية</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>stake.ac</h3><p>أبرز النطاقات البديلة. نفس المحتوى ونفس الحساب. إن واجهت أي قيود على stake.com في منطقتك جرب stake.ac. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يعمل بالشروط ذاتها.</p></div>
        <div class="club-card"><h3>stake.bet</h3><p>نطاق بديل موثوق. يرتكز على دومين .bet المناسب للمراهنات الرياضية. تسجيل الدخول بنفس بيانات stake.com. التحويل بين النطاقات شفاف.</p></div>
        <div class="club-card"><h3>stake.games</h3><p>نطاق .games يبرز جانب الألعاب. نفس الوظائف الكاملة بما فيها السلوتس والكازينو المباشر والمراهنات الرياضية. الرمز MAX3000 صالح عليه أيضاً.</p></div>
        <div class="club-card"><h3>ملاحظة الاستخدام</h3><p>مواقع المرآة ليست "طرقاً للتحايل" على القيود القانونية الصارمة. إن كانت منطقتك محظورة قانونياً من stake.com فمواقع المرآة تخضع للحظر ذاته. تصفح دائماً وفق القوانين المحلية لبلدك.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المناطق والنطاقات <span class="text-gradient-gold">المتاحة</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">المنطقة العربية</div><div class="ic-value">متاحة عموماً</div><div class="ic-detail">معظم الدول العربية لا تخضع لقوائم حظر Stake الرسمية. تحقق دائماً من القوانين المحلية قبل اللعب.</div></div>
        <div class="intel-card"><div class="ic-label">الولايات المتحدة</div><div class="ic-value">stake.us فقط</div><div class="ic-detail">Stake.com محظورة في الولايات المتحدة. stake.us هي المنصة القانونية للمقيمين الأمريكيين.</div></div>
        <div class="intel-card"><div class="ic-label">المملكة المتحدة</div><div class="ic-value">انسحبت مارس 2025</div><div class="ic-detail">Stake انسحبت طوعاً من سوق المملكة المتحدة في مارس 2025. المواطنون البريطانيون لا يمكنهم التسجيل.</div></div>
        <div class="intel-card"><div class="ic-label">الترخيص</div><div class="ic-value">كوراساو OGL/2024/1451/0918</div><div class="ic-detail">يغطي معظم دول العالم. المحظورون يُمنعون عند التسجيل أو خلال KYC لا عبر الوصول إلى الموقع.</div></div>
      </div>
    </div>
  </section>
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة حول <span class="text-gradient-gold">مواقع المرآة</span></h2></div>
      <div class="faq-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">ما هي مواقع مرآة Stake الرسمية؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>المواقع البديلة الرسمية هي <bdi dir="ltr">stake.ac</bdi> و<bdi dir="ltr">stake.bet</bdi> و<bdi dir="ltr">stake.games</bdi>. جميعها تُشغِّلها Medium Rare NV ويعمل عليها رمز MAX3000 بالشروط ذاتها.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">هل MAX3000 يعمل على مواقع المرآة؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>نعم. الرمز MAX3000 صالح على جميع النطاقات الرسمية بما فيها stake.ac وstake.bet وstake.games. شروط المكافأة ذاتها على جميعها.</p></div></div>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'موقع مرآة <bdi dir="ltr">Stake</bdi> - النطاقات البديلة الرسمية',
        '<bdi dir="ltr">stake.ac</bdi> و<bdi dir="ltr">stake.bet</bdi> و<bdi dir="ltr">stake.games</bdi>. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يعمل على الجميع.',
        sections, og_image='default.png', extra_jsonld=faq_jsonld)


def page_payments():
    slug = 'payments'
    title = 'مدفوعات Stake - إيداع وسحب العملات الرقمية مع MAX3000'
    desc = 'مدفوعات Stake.com: البيتكوين وإيثريوم وليتكوين وريبل وتيثر وأكثر من 30 عملة رقمية. سحوبات خلال 30 دقيقة. الرمز MAX3000 يفتح 200% حتى $3,000.'

    faq_jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":"ما العملات الرقمية المقبولة في Stake؟","acceptedAnswer":{"@type":"Answer","text":"تقبل Stake.com البيتكوين (BTC) وإيثريوم (ETH) وليتكوين (LTC) وريبل (XRP) وتيثر (USDT) وسولانا (SOL) وترون (TRX) وبايننس كوين (BNB) وعشرات غيرها. طرق الدفع القانونية متاحة عبر MoonPay."}},
  {"@type":"Question","name":"كم تستغرق سحوبات Stake؟","acceptedAnswer":{"@type":"Answer","text":"سحوبات العملات الرقمية تُستوفى خلال 30 دقيقة إلى ساعة في الظروف الاعتيادية. TRX وXRP وSOL تُسوَّى في ثوانٍ إلى دقائق. السحوبات الكبيرة قد تستلزم 2 إلى 4 أيام عمل للمراجعة."}}
]}
</script>'''

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العملات الرقمية <span class="text-gradient-gold">المقبولة</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">BTC</div><div class="ic-value">بيتكوين</div><div class="ic-detail">الأكثر استخداماً. إيداع فوري بعد تأكيد البلوك. سحب خلال 30 دقيقة إلى ساعة. رسوم شبكة متغيرة.</div></div>
        <div class="intel-card"><div class="ic-label">ETH</div><div class="ic-value">إيثريوم</div><div class="ic-detail">74% من احتياطيات Stake بالإيثريوم وفق لقطة مايو 2026. سرعة تأكيد عالية مع رسوم gas متغيرة.</div></div>
        <div class="intel-card"><div class="ic-label">USDT / USDC</div><div class="ic-value">ستيبل كوين</div><div class="ic-detail">الأفضل لتجنب تذبذب الأسعار. USDT على Tron وEthereum وBSC. إيداع وسحب فوري تقريباً.</div></div>
        <div class="intel-card"><div class="ic-label">SOL</div><div class="ic-value">سولانا</div><div class="ic-detail">14% من احتياطيات Stake. تسوية في ثوانٍ. رسوم أقل من $0.01. مثالية للمعاملات المتكررة الصغيرة.</div></div>
        <div class="intel-card"><div class="ic-label">XRP</div><div class="ic-value">ريبل</div><div class="ic-detail">تسوية في 3 إلى 5 ثوانٍ. رسوم ثابتة منخفضة جداً. مناسب للمبالغ الكبيرة.</div></div>
        <div class="intel-card"><div class="ic-label">TRX</div><div class="ic-value">ترون</div><div class="ic-detail">تسوية شبه فورية. رسوم لا تُذكر. شائع بين لاعبي Stake في آسيا والشرق الأوسط.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">سرعة <span class="text-gradient-gold">السحب</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>العملات الرقمية: 30 دقيقة إلى ساعة</h3><p>معظم سحوبات العملات الرقمية تُنجز في ظروف عادية خلال 30 دقيقة إلى ساعة. السحوبات تمر بمراجعة أمنية تلقائية ثم تُرسل إلى المحفظة.</p></div>
        <div class="club-card"><h3>TRX وXRP وSOL: ثوانٍ</h3><p>هذه الشبكات تُسوِّي في ثوانٍ إلى دقائق بعد موافقة Stake. مثالية لمن يحتاج سيولة سريعة.</p></div>
        <div class="club-card"><h3>السحوبات الكبيرة: 2 إلى 4 أيام عمل</h3><p>السحوبات التي تتجاوز حدود معينة تخضع لمراجعة امتثال يدوية. KYC المستوى 3 مطلوب للسحوبات الكبيرة. عادةً تُنجز خلال يومي عمل.</p></div>
        <div class="club-card"><h3>MoonPay القانونية: 1 إلى 5 أيام عمل</h3><p>سحوبات العملات القانونية عبر MoonPay تستغرق وقتاً أطول بسبب معالجة البنوك والامتثال. رسوم تحويل إضافية قد تُطبَّق.</p></div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الإيداع وشرط <span class="text-gradient-gold">المكافأة</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>الحد الأدنى للإيداع: $10</h3><p>أول إيداع يُفعِّل مكافأة MAX3000 يجب أن يكون $10 على الأقل. إيداع $1,500 يمنحك كامل $3,000 (200% مطابقة). الإيداعات اللاحقة لا تُضاف إلى الحد.</p></div>
        <div class="club-card"><h3>التحويل اللحظي</h3><p>إيداع العملات الرقمية يُضاف فوراً بعد تأكيد بلوك واحد لمعظم الشبكات. USDT على Tron وSOL يُضافان شبه فورياً.</p></div>
        <div class="club-card"><h3>لا رسوم داخلية</h3><p>Stake لا تفرض رسوماً على الإيداع أو السحب. قد تدفع رسوم شبكة البلوك تشين لكن Stake ذاتها لا تأخذ عمولة على المعاملات.</p></div>
      </div>
    </div>
  </section>
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">المدفوعات</span></h2></div>
      <div class="faq-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">ما العملات الرقمية المقبولة؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>BTC وETH وLTC وXRP وUSDT وSOL وTRX وBNB وعشرات العملات الأخرى. طرق القانونية متاحة عبر MoonPay.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">كم تستغرق السحوبات؟<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button><div class="faq-answer"><p>30 دقيقة إلى ساعة للعملات الرقمية المعتادة. ثوانٍ لـ TRX وXRP وSOL. 2 إلى 4 أيام عمل للسحوبات الكبيرة. 1 إلى 5 أيام عمل لـ MoonPay.</p></div></div>
      </div>
    </div>
  </section>'''

    return make_simple_page(slug, title, desc,
        'مدفوعات <bdi dir="ltr">Stake</bdi> - إيداع وسحب العملات الرقمية',
        'أكثر من 30 عملة رقمية. سحوبات خلال 30 دقيقة. الرمز <span class="code-highlight"><bdi dir="ltr">MAX3000</bdi></span> يمنحك 200% حتى <bdi dir="ltr">$3,000</bdi>.',
        sections, og_image='default.png', extra_jsonld=faq_jsonld)


def page_reserves():
    slug = 'reserves'
    title = 'احتياطيات Stake على السلسلة - $339.53M موثقة على Arkham'
    desc = 'احتياطيات Stake.com على البلوك تشين: $339.53M موثقة على Arkham Intel. Ethereum 74%، Solana 14%. الرمز MAX3000 يفتح 200% حتى $3,000.'

    faq_jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":"كم تبلغ احتياطيات Stake على السلسلة؟","acceptedAnswer":{"@type":"Answer","text":"لقطة 28 مايو 2026 من Arkham Intel تُظهر $339.53M في المحافظ الموسومة لـ Stake. Ethereum 74%، Solana 14%، Tron USDT 5%، BNB Chain 6%. الأرقام قابلة للتتبع علنياً عبر cryptotips.com."}},
  {"@type":"Question","name":"كيف أتحقق من احتياطيات Stake بنفسي؟","acceptedAnswer":{"@type":"Answer","text":"تفضل بزيارة cryptotips.com/on-chain/stake/ للحصول على بيانات Arkham Intel المحدَّثة أسبوعياً. عناوين المحفظة موسومة علناً."}}
]}
</script>'''

    sections = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لقطة الاحتياطيات <span class="text-gradient-gold">28 مايو 2026</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">إجمالي الاحتياطيات الموسومة</div><div class="ic-value"><bdi dir="ltr">$339.53M</bdi></div><div class="ic-detail">لقطة Arkham Intel، 28 مايو 2026. جميع المحافظ موسومة علناً وقابلة للتحقق في الوقت الفعلي.</div></div>
        <div class="intel-card"><div class="ic-label">إيثريوم</div><div class="ic-value">74%</div><div class="ic-detail">الحصة الأكبر. يُعكس هذا قبول Stake للعاب العملات الرقمية وتفضيل اللاعبين للدفع بـ ETH.</div></div>
        <div class="intel-card"><div class="ic-label">سولانا</div><div class="ic-value">14%</div><div class="ic-detail">نمو ملحوظ مدفوع بشعبية SOL كخيار مدفوعات بسبب سرعته ورسومه المنخفضة.</div></div>
        <div class="intel-card"><div class="ic-label">ستيبل كوين + أخرى</div><div class="ic-value">12%</div><div class="ic-detail">USDT على Tron (5%)، BNB Chain (6%)، وأرصدة متنوعة على شبكات أخرى.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">ما أهمية <span class="text-gradient-gold">الاحتياطيات على السلسلة؟</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>لا تصدق كلامهم فقط</h3><p>خلافاً للكازينوهات التقليدية التي تُصدر PDF تطلب منك الثقة، محافظ Stake مقروءة علناً على البلوك تشين. أي شخص لديه اتصال بالإنترنت يستطيع التحقق من الرصيد في الوقت الفعلي عبر Arkham.</p></div>
        <div class="club-card"><h3>الدليل: GGR $4.7B</h3><p>إجمالي إيرادات القمار لـ Stake يُقدَّر بـ $4.7B منذ التأسيس. احتياطيات $339.53M تمثل حوالي 7% من الإيرادات التاريخية، وهي نسبة صحية تُشير إلى قدرة الدفع.</p></div>
        <div class="club-card"><h3>تتبع مستمر</h3><p>cryptotips.com يُحدِّث بيانات Arkham أسبوع