#!/usr/bin/env python3
"""Build all 19 Arabic /ar/ pages for winnersclub.com.
MSA, RTL, full KO-depth content.
"""
import os, re

BASE = '/home/user/workspace/winnersclub.com'

# Hreflang block for all pages (will have page-specific URLs filled in)
def hreflang_block(page_path):
    """page_path is like '' for index, 'promo-code/' for subpages"""
    base = 'https://winnersclub.com'
    en_url = f"{base}/{page_path}" if page_path else f"{base}/"
    lines = []
    langs = [
        ('en', en_url),
        ('ko', f"{base}/ko/{page_path}"),
        ('zh-Hans', f"{base}/zh/{page_path}"),
        ('vi', f"{base}/vi/{page_path}"),
        ('th', f"{base}/th/{page_path}"),
        ('ms', f"{base}/ms/{page_path}"),
        ('pt', f"{base}/pt/{page_path}"),
        ('ja', f"{base}/ja/{page_path}"),
        ('es', f"{base}/es/{page_path}"),
        ('pt-BR', f"{base}/pt-br/{page_path}"),
        ('tr', f"{base}/tr/{page_path}"),
        ('id', f"{base}/id/{page_path}"),
        ('fr', f"{base}/fr/{page_path}"),
        ('ru', f"{base}/ru/{page_path}"),
        ('hi', f"{base}/hi/{page_path}"),
        ('ar', f"{base}/ar/{page_path}"),
        ('x-default', en_url),
    ]
    for lang, url in langs:
        lines.append(f'  <link rel="alternate" hreflang="{lang}" href="{url}">')
    return '\n'.join(lines)


def nav_block(current_page=''):
    """Arabic navigation header block"""
    pages = [
        ('casino/', 'كازينو'),
        ('sports/', 'الرياضة'),
        ('poker/', 'بوكر'),
        ('aviator/', 'أفياتور'),
        ('promo-code/', 'الرمز الترويجي'),
        ('reserves/', 'الاحتياطيات'),
        ('about-stake/', 'عن Stake'),
    ]
    links = '\n        '.join(
        f'<a href="/ar/{p[0]}" class="nav-link">{p[1]}</a>' for p in pages
    )
    mobile_opts = '<option value="">English</option><option value="/ar/" selected>العربية (Arabic)</option><option value="/ko/">한국어 (Korean)</option><option value="/zh/">中文 (Chinese)</option><option value="/vi/">Tiếng Việt (Vietnamese)</option><option value="/th/">ไทย (Thai)</option><option value="/ms/">Bahasa Melayu (Malay)</option><option value="/pt/">Português (Portuguese)</option><option value="/ja/">日本語 (Japanese)</option><option value="/es/">Español (Spanish)</option><option value="/pt-br/">Português do Brasil (Portuguese - Brazil)</option><option value="/tr/">Türkçe (Turkish)</option><option value="/id/">Bahasa Indonesia (Indonesian)</option><option value="/fr/">Français (French)</option><option value="/ru/">Русский (Russian)</option><option value="/hi/">हिन्दी (Hindi)</option>'
    desktop_opts = '<option value="https://winnersclub.com/">English</option><option value="https://winnersclub.com/ar/" selected>العربية</option><option value="https://winnersclub.com/ko/">한국어</option><option value="https://winnersclub.com/zh/">中文</option><option value="https://winnersclub.com/vi/">Tiếng Việt</option><option value="https://winnersclub.com/th/">ไทย</option><option value="https://winnersclub.com/ms/">Bahasa Melayu</option><option value="https://winnersclub.com/pt/">Português</option><option value="https://winnersclub.com/ja/">日本語</option><option value="https://winnersclub.com/es/">Español</option><option value="https://winnersclub.com/pt-br/">Português (BR)</option><option value="https://winnersclub.com/tr/">Türkçe</option><option value="https://winnersclub.com/id/">Bahasa Indonesia</option><option value="https://winnersclub.com/fr/">Français</option><option value="https://winnersclub.com/ru/">Русский</option><option value="https://winnersclub.com/hi/">हिन्दी</option>'
    return f'''  <!-- HEADER -->
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/ar/" class="header-logo" aria-label="WinnersClub الرئيسية">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        {links}
      <div class="mobile-lang-block"><label>اللغة</label><select onchange="if(this.value)window.location.href=this.value" aria-label="اللغة">{mobile_opts}</select></div></nav>
      <div class="header-actions"><select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="اللغة">{desktop_opts}</select>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup" aria-label="ادخل الآن">ادخل الآن</a>
        <button class="hamburger" id="hamburger" aria-label="فتح القائمة"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>'''


def footer_block():
    return '''  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub">
  <path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/>
  <path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="46" y="26" font-family="\'Inter\',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text>
</svg>
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">النادي مع Stake منذ 2017.</p>
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
            <a href="/ar/sports/">الرياضة</a>
            <a href="/ar/poker/">بوكر</a>
            <a href="/ar/aviator/">أفياتور</a>
            <a href="/ar/live-odds/">أوتار مباشرة</a>
          </div>
          <div class="footer-col">
            <h4>الرمز</h4>
            <a href="/ar/promo-code/">الرمز الترويجي MAX3000</a>
            <a href="/ar/payments/">المدفوعات</a>
            <a href="/ar/mirror/">المرايا والوصول</a>
          </div>
          <div class="footer-col">
            <h4>المعلومات</h4>
            <a href="/ar/about-stake/">عن Stake</a>
            <a href="/ar/reserves/">الاحتياطيات على السلسلة</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">WinnersClub هو النادي الداخلي الحصري للاعبي Stake. يُشغَّل Stake.com من قبل Medium Rare NV بموجب ترخيص كوراساو OGL/2024/1451/0918. Stake.us هي منصة سويبستيكس منفصلة تُشغَّلها Sweepsteaks Limited. هذا الموقع لأغراض إعلامية فحسب. القمار ينطوي على مخاطر. العب بمسؤولية. إذا كنت تعاني من مشكلة قمار أو تعرف شخصاً يعاني منها، تواصل مع GamCare أو جهة دعم محلية. للأعمار 18 سنة فما فوق.</p>
        <p class="footer-copyright">&copy; 2026 winnersclub.com. جميع الحقوق محفوظة.</p>
      </div>
    </div>
  </footer>'''


def rooms_grid():
    return '''<aside class="rooms-grid" aria-label="غرف أخرى في وينرز كلوب" style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);border:1px solid rgba(255,215,0,.12);border-radius:14px;"><h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#737378;margin:0 0 18px;font-weight:700;">غرف أخرى في وينرز كلوب</h3><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;"><li><a href="/ar/promo-code/">الرمز الترويجي لـ Stake</a></li><li><a href="/ar/casino/">كازينو Stake</a></li><li><a href="/ar/sports/">رياضة Stake</a></li><li><a href="/ar/poker/">بوكر Stake</a></li><li><a href="/ar/aviator/">أفياتور Stake</a></li><li><a href="/ar/reserves/">الاحتياطيات المُتحقَّق منها</a></li><li><a href="/ar/about-stake/">عن Stake</a></li><li><a href="/ar/payments/">مدفوعات العملات الرقمية</a></li><li><a href="/ar/mirror/">مواقع المرآة</a></li><li><a href="/ar/live-odds/">أوتار مباشرة</a></li><li><a href="/ar/originals/">Stake Originals</a></li><li><a href="/ar/vip/">برنامج VIP</a></li><li><a href="/ar/slots/">مكتبة السلوتس</a></li><li><a href="/ar/live-casino/">كازينو مباشر</a></li></ul></aside>'''


def head_common(title, description, canonical, og_image, extra_head=''):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><script>document.documentElement.classList.add("js-anim");</script>
  <meta charset="UTF-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
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
{extra_head}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap"><script type="application/ld+json" data-ld="org">{{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"النادي الداخلي للاعبي Stake. الرمز الترويجي MAX3000 يفتح مكافأة 200% تصل إلى $3,000 مع اشتراط رهان 40x."}}</script><meta name="twitter:image" content="{og_image}"><meta name="twitter:card" content="summary_large_image">
  <script src="/lang-redirect.js" defer></script>'''


def sticky_cta(text, btn_text='ادخل وسجّل الآن'):
    return f'''  <!-- STICKY CTA -->
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">{text}</div>
    <div class="sticky-cta-actions">
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">{btn_text} &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="إغلاق">&times;</button>
  </div>'''


def scripts():
    return '''  <script src="/script.min.js?v=20260618a" defer></script>
  <script src="/voice.js" defer></script>
<script src="/ga-events.js" defer></script>'''


def reserves_ticker():
    return '''  <div class="reserves-ticker"><div class="rt-inner"><span>Stake على السلسلة الآن: احتياطيات موسومة <bdi dir="ltr">$339.53M</bdi> &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; ترخيص كوراساو OGL/2024/1451/0918 &middot; المصدر: Arkham Intel عبر cryptotips.com &middot; لقطة 28 مايو 2026</span><span>Stake على السلسلة الآن: احتياطيات موسومة <bdi dir="ltr">$339.53M</bdi> &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; ترخيص كوراساو OGL/2024/1451/0918 &middot; المصدر: Arkham Intel عبر cryptotips.com &middot; لقطة 28 مايو 2026</span></div></div>'''


def promo_strip():
    return '''  <aside class="promo-strip" aria-label="الرمز الترويجي MAX3000"><div class="ps-inner"><span class="ps-label">الرمز الترويجي</span><span class="ps-code">MAX3000</span><span class="ps-bonus">200% تصل إلى <bdi dir="ltr">$3,000</bdi> &middot; اشتراط رهان 40x</span><a href="/ar/promo-code/" class="ps-cta">فتح صفحة الرمز &rarr;</a></div></aside>'''


#############################################
# PAGE GENERATORS
#############################################

def make_index():
    page_path = 'ar/'
    hrl = hreflang_block(page_path)
    jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000",
  "description": "النادي الداخلي الحصري للاعبي Stake.com. الرمز الترويجي MAX3000 يفتح مكافأة 200% تصل إلى $3,000 مع اشتراط رهان 40x على الإيداع والمكافأة معاً. GGR $4.7B، 21 مليون حساب، احتياطيات على السلسلة $339M. Medium Rare NV، كوراساو OGL/2024/1451/0918، تأسس 2017.",
  "url": "https://winnersclub.com/ar/"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "الرئيسية",
      "item": "https://winnersclub.com/ar/"
    }
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
      "name": "هل MAX3000 أكبر رمز مكافأة في Stake؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "نعم. مكافأة 200% تصل إلى $3,000 مع اشتراط رهان 40x على الإيداع والمكافأة معاً. معظم الرموز المتاحة للعموم تقف عند 100% و$1,000. MAX3000 هو الرمز الذي يقدمه النادي عند الباب."
      }
    },
    {
      "@type": "Question",
      "name": "هل Stake.com موثوق؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Stake يعمل بموجب ترخيص كوراساو OGL/2024/1451/0918 تحت Medium Rare NV منذ 2017. الاحتياطيات على السلسلة بلغت $339.53M بتاريخ 28 مايو 2026 ويمكن تتبعها علناً عبر Arkham. المؤسسان Ed Craven وBijan Tehrani يديران أيضاً منصة Kick."
      }
    },
    {
      "@type": "Question",
      "name": "كيف يمكنني التحقق من احتياطيات Stake؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "قم بزيارة صفحة الاحتياطيات على winnersclub.com/ar/reserves/. لقطة 28 مايو 2026 تُظهر $339.53M في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%، أرصدة عملات مستقرة بتسعة أرقام. قابل للتتبع عبر Arkham Intel من خلال cryptotips.com."
      }
    },
    {
      "@type": "Question",
      "name": "من أين يمكنني اللعب؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ترخيص كوراساو يغطي معظم الدول، غير أن Stake يفرض قيوداً ذاتية في الولايات المتحدة والمملكة المتحدة وبعض الدول الأخرى. قم بزيارة صفحة المرايا للعثور على النطاق المناسب لمنطقتك."
      }
    },
    {
      "@type": "Question",
      "name": "ما سرعة عمليات السحب؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "تكتمل عمليات سحب العملات الرقمية للمبالغ المعتادة في غضون 30 دقيقة إلى ساعة. TRX وXRP وSOL تُسوَّى في ثوانٍ إلى دقائق. السحوبات الكبيرة قد تستغرق 2-4 أيام عمل للمراجعة. سحوبات العملات الورقية عبر MoonPay تستغرق 1-5 أيام عمل."
      }
    }
  ]
}
</script>'''
    extra = jsonld + '\n' + hrl
    head = head_common(
        'وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000',
        'النادي الداخلي الحصري للاعبي Stake.com. الرمز الترويجي MAX3000 يفتح مكافأة 200% تصل إلى $3,000 مع اشتراط رهان 40x. GGR $4.7B، أكثر من 21 مليون حساب، احتياطيات على السلسلة $339M.',
        'https://winnersclub.com/ar/',
        'https://winnersclub.com/images/og/default.png',
        extra_head=extra
    )
    body = f'''<body>
{nav_block()}
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">إذا وجدت هذه الصفحة، فالحارس أعجبه ما رأى.</p>
        <h1 class="ch-title text-gradient-gold">الرمز الترويجي لـ Stake: <bdi dir="ltr">MAX3000</bdi><span class="h1-sub">مرحباً بك داخل النادي.</span></h1>
        <p class="ch-sub">الغرفة الخلفية الخاصة بلاعبي Stake. همس <span class="code-highlight">MAX3000</span> عند الباب يفتح لك <strong>مكافأة 200% تصل إلى <bdi dir="ltr">$3,000</bdi></strong> و<strong>اشتراط رهان 40x على الإيداع والمكافأة معاً</strong>. بعيداً كل البُعد عن الرموز الرخيصة المتاحة للعموم.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">احصل على 200% حتى <bdi dir="ltr">$3,000</bdi> على Stake.com</a>
          <a href="/ar/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">ماذا يفتح MAX3000</a>
        </div>
      </div>
    </div>
  </section>
{reserves_ticker()}
{promo_strip()}

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لماذا هذا <span class="text-gradient-gold">النادي</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>مكافأة بثقل حقيقي</h3><p>200% تصل إلى <bdi dir="ltr">$3,000</bdi> مع اشتراط رهان 40x على الإيداع والمكافأة معاً. سائر رموز Stake المتاحة على الإنترنت تقف عند 100% و<bdi dir="ltr">$1,000</bdi>. إذا لم تقدم <span class="code-highlight">MAX3000</span> للمتعامل خلال 24 ساعة من التسجيل، ستحصل على القائمة الرخيصة.</p></div>
        <div class="club-card"><h3>الأموال معلقة على الجدار للعيان</h3><p>احتياطيات Arkham الموسومة <bdi dir="ltr">$339.53M</bdi> بتاريخ 28 مايو 2026. لا ملفات PDF تقول "ثق بنا"، ولا عروض احتياطيات مسرحية. المحافظ مقروءة علناً، أي شخص بإمكانه مراجعتها طالما لديه اتصال بالإنترنت. <a href="/ar/reserves/" style="color:var(--gold);">نعرض الإيصالات.</a></p></div>
        <div class="club-card"><h3>للبيت وجه معروف</h3><p>Ed Craven (ملبورن، مواليد 1995) وBijan Tehrani. التقيا في RuneScape وأسسا Stake عام 2017، ثم أطلقا Kick عام 2022. صافي الثروة المُقدَّر مجتمعاً 5.6 مليار دولار وفق Forbes. ليسا شركة وهمية. إنهما رجلان لم يخسرا.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">خمس غرف، <span class="text-gradient-gold">رمز واحد</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">اختر بابك. MAX3000 ينطبق على الجميع. المتعامل لا يهتم أين تصرف مكافأتك.</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));"><a href="/ar/casino/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">كازينو</div></a><a href="/ar/sports/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-sports-2.avif') type('image/avif'), url('/images/girl-sports-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">الرياضة</div></a><a href="/ar/poker/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-poker-2.avif') type('image/avif'), url('/images/girl-poker-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">بوكر</div></a><a href="/ar/aviator/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-aviator-2.avif') type('image/avif'), url('/images/girl-aviator-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">أفياتور</div></a><a href="/ar/live-odds/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-lucky-drive-2.avif') type('image/avif'), url('/images/girl-lucky-drive-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">مباشر</div></a></div>
    </div>
  </section>
  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title"><bdi dir="ltr">$3,000</bdi>. <span class="text-gradient-gold">رهان 40x.</span> رمز واحد.</h2>
      <p class="girl-break-sub">همس <span class="code-highlight">MAX3000</span> للمتعامل عند التسجيل. الحسابات ستكون في صالحك قبل وصول أول مشروب.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">سلّم الرمز للمتعامل</a>
    </div>
  </section>
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">ما يعرفه <span class="text-gradient-gold">النادي</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">المؤسسان</div><div class="ic-value">Craven &amp; Tehrani</div><div class="ic-detail">Ed Craven (مواليد 1995، ملبورن) وBijan Tehrani. التقيا في RuneScape. أسسا Stake عام 2017. أطلقا Kick عام 2022.</div></div>
        <div class="intel-card"><div class="ic-label">الكيان التشغيلي</div><div class="ic-value">Medium Rare NV</div><div class="ic-detail">الكيان المرخَّص في كوراساو الذي يشغّل Stake.com. الشركة الأم: Easygo Group Holdings، إيرادات FY2025: A$970M. Stake.us كيان سويبستيكس منفصل.</div></div>
        <div class="intel-card"><div class="ic-label">الترخيص</div><div class="ic-value">كوراساو OGL/2024/1451/0918</div><div class="ic-detail">يغطي معظم الدول. انسحب من المملكة المتحدة في مارس 2025. الولايات المتحدة محجوبة (Stake.us متاح في 30+ ولاية كسويبستيكس). أكثر من 22 موقع مرآة مُتحقَّق منه.</div></div>
        <div class="intel-card"><div class="ic-label">الاحتياطيات</div><div class="ic-value"><bdi dir="ltr">$339.53M</bdi></div><div class="ic-detail">موسومة بـ Arkham بتاريخ 28 مايو 2026. Ethereum 74%، Solana 14%، أرصدة عملات مستقرة بتسعة أرقام. قابل للتتبع عبر cryptotips.com.</div></div>
      </div>
    </div>
  </section>
  <!-- STAKE.COM vs STAKE.US -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">بابان، <span class="text-gradient-gold">رمز واحد</span></h2>
        <p class="section-subtitle">MAX3000 يُقبَل في Stake.com وStake.us على حدٍّ سواء. الترحيب خلف كل باب مختلف. المتعامل سيرشدك إلى الباب المناسب بحسب بلد إقامتك.</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3>Stake.com - أموال حقيقية، عالمي</h3>
          <p>منصة أموال حقيقية تشغّلها Medium Rare NV بموجب كوراساو OGL/2024/1451/0918. عملات رقمية وورقية. رياضة وكازينو وأوريجينالز وبوكر. الرمز <span class="code-highlight">MAX3000</span> يفتح <strong>200% حتى <bdi dir="ltr">$3,000</bdi></strong>، رهان 40x على الإيداع والمكافأة، 30 يوماً، حد أدنى للإيداع <bdi dir="ltr">$10</bdi>. اطلبه عبر الدعم المباشر بعد الإيداع. يلزم KYC Level 3. متاح في معظم الدول باستثناء الولايات المتحدة والمملكة المتحدة.</p>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">افتح الباب العالمي</a>
        </div>
        <div class="club-card">
          <h3>Stake.us - سويبستيكس، الولايات المتحدة</h3>
          <p>منصة سويبستيكس أمريكية تشغّلها Sweepsteaks Limited. Gold Coins للعب، وStake Cash قابلة للاستبدال بعد 3x معدل اللعب. لا إيداع/سحب حقيقي، لا رياضة، كازينو فقط. الرمز <span class="code-highlight">MAX3000</span> يُقبَل أيضاً ويمنح <strong>560,000 GC + 56 SC + 3.5% ريكباك</strong>. متاح في 37 ولاية.</p>
          <a href="https://stake.us/?c=MAX3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">افتح الباب الأمريكي</a>
        </div>
      </div>
    </div>
  </section>
  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">الباب</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل MAX3000 أكبر رمز مكافأة في Stake؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. مكافأة 200% تصل إلى <bdi dir="ltr">$3,000</bdi> مع اشتراط رهان 40x على الإيداع والمكافأة معاً. معظم الرموز المتاحة للعموم تقف عند 100% و<bdi dir="ltr">$1,000</bdi>. MAX3000 هو الرمز الذي يقدمه النادي عند الباب.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل Stake.com موثوق؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Stake يعمل بموجب ترخيص كوراساو OGL/2024/1451/0918 تحت Medium Rare NV منذ 2017. الاحتياطيات على السلسلة <bdi dir="ltr">$339.53M</bdi> بتاريخ 28 مايو 2026 قابلة للتتبع علناً عبر Arkham. المؤسسان Ed Craven (مواليد 1995، ملبورن) وBijan Tehrani يديران Kick أيضاً. الشركة الأم Easygo Group Holdings أعلنت إيرادات FY2025 بلغت A$970M وصافي ربح A$257M.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">كيف يمكنني التحقق من احتياطيات Stake؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>قم بزيارة <a href='/ar/reserves/'>صفحة الاحتياطيات</a>. لقطة 28 مايو 2026 تُظهر <bdi dir="ltr">$339.53M</bdi> في محافظ Arkham الموسومة. Ethereum 74%، Solana 14%، أرصدة عملات مستقرة بتسعة أرقام. قابل للتتبع عبر <a href='https://cryptotips.com/on-chain/stake/' target='_blank' rel='noopener'>cryptotips.com</a> ببيانات Arkham Intel الأسبوعية.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">من أين يمكنني اللعب؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>ترخيص كوراساو يغطي معظم الدول، غير أن Stake يفرض قيوداً ذاتية في الولايات المتحدة والمملكة المتحدة وبعض الدول الأخرى. قم بزيارة <a href='/ar/mirror/'>صفحة المرايا</a> للعثور على النطاق المناسب لمنطقتك.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما سرعة عمليات السحب؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>تكتمل عمليات سحب العملات الرقمية للمبالغ المعتادة في غضون 30 دقيقة إلى ساعة. TRX وXRP وSOL تُسوَّى في ثوانٍ إلى دقائق. السحوبات الكبيرة قد تستغرق 2-4 أيام عمل للمراجعة الامتثالية. سحوبات العملات الورقية عبر MoonPay تستغرق 1-5 أيام عمل. راجع <a href='/ar/payments/'>صفحة المدفوعات</a> للتفاصيل الكاملة.</p></div>
        </div>
      </div>
    </div>
  </section>
  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر المتعامل أن وينرز كلوب أرسلك.</p>
    </div>
  </section>
{sticky_cta('الرمز هو <span class="code-highlight">MAX3000</span>. 200% حتى <bdi dir="ltr">$3,000</bdi>. باب Stake.com مفتوح')}
{footer_block()}
{scripts()}
{rooms_grid()}</body>
</html>'''
    return head + '\n' + body


def make_promo_code():
    page_path = 'ar/promo-code/'
    hrl = hreflang_block(page_path)
    jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "رمز Stake الترويجي MAX3000 - مكافأة 200% حتى $3,000 عند التسجيل",
  "description": "رمز Stake.com الترويجي MAX3000: مكافأة 200% على الإيداع الأول حتى $3,000، اشتراط رهان 40x على الإيداع والمكافأة، KYC Level 3 مطلوب. تم التحقق في يونيو 2026.",
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
  "name": "رمز Stake.com الترويجي MAX3000",
  "description": "مكافأة 200% على الإيداع في Stake.com حتى $3,000. الحد الأدنى للإيداع $10، الحد الأقصى المؤهِّل $1,500. اشتراط رهان 40x على الإيداع والمكافأة معاً. KYC Level 3 مطلوب. للعملاء الجدد فقط عند الإيداع الأول. يُصرَف الرمز خلال 24-48 ساعة من الإيداع الأول بعد تأكيد دعم Stake.",
  "areaServed": "عالمي (باستثناء الولايات المحظورة: الولايات المتحدة والمملكة المتحدة وأستراليا ومعظم أوروبا)",
  "url": "https://winnersclub.com/ar/promo-code/",
  "priceCurrency": "USD",
  "price": "0",
  "eligibleQuantity": {"@type": "QuantitativeValue", "value": 1},
  "seller": {"@type": "Organization", "name": "Stake.com"}
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "ما هو الرمز الترويجي لـ Stake.com؟", "acceptedAnswer": {"@type": "Answer", "text": "الرمز هو MAX3000. سجّل على Stake.com عبر رابط الشراكة، أكمل KYC Level 3، أودع ما بين $10 و$1,500 كإيداع أول، ثم افتح المحادثة المباشرة وأخبرهم بـ MAX3000. سيتحقق الدعم من أهليتك ويُضيف مكافأة 200% حتى $3,000 خلال 24-48 ساعة."}},
    {"@type": "Question", "name": "ما الحد الأقصى لمكافأة MAX3000؟", "acceptedAnswer": {"@type": "Answer", "text": "مكافأة 200% حتى $3,000 كحد أقصى. إيداع $1,500 يُحقق كامل $3,000. الحد الأدنى للإيداع المؤهِّل $10، والأقصى $1,500. الإيداعات التي تتجاوز $1,500 لا تزيد المكافأة."}},
    {"@type": "Question", "name": "ما اشتراط الرهان؟", "acceptedAnswer": {"@type": "Answer", "text": "40x على مجموع الإيداع والمكافأة. مثال: إيداع $500، مكافأة $1,000 = مجموع $1,500 × 40 = $60,000 رهاناً. ألعاب الكازينو ذات هامش البيت 4% فأكثر تُسهم بنسبة 100%، والرهانات الرياضية بنسبة 75%."}},
    {"@type": "Question", "name": "هل التحقق من الهوية مطلوب؟", "acceptedAnswer": {"@type": "Answer", "text": "نعم. يشترط Stake.com إتمام KYC Level 3 قبل صرف المكافأة الترحيبية. في الإعدادات &gt; التحقق، قدّم وثيقة هوية مصورة ومستند إثبات عنوان ووثيقة مصدر الأموال. لا تُصرَف المكافأة إلا بعد اجتياز Level 3."}},
    {"@type": "Question", "name": "هل هناك حد أدنى للإيداع؟", "acceptedAnswer": {"@type": "Answer", "text": "نعم، الحد الأدنى للإيداع المؤهِّل هو $10 أو ما يعادله بالعملات الرقمية. الحد الأقصى المؤهِّل هو $1,500 وهو ما يُحقق سقف المكافأة $3,000."}},
    {"@type": "Question", "name": "كيف تُصرَف مكافأة MAX3000؟", "acceptedAnswer": {"@type": "Answer", "text": "ليست رصيداً يُطبَّق تلقائياً، بل رصيد يُمنح يدوياً من المشغِّل. بعد تسوية الإيداع الأول افتح المحادثة المباشرة مع Stake وأخبرهم أنك سجّلت بـ MAX3000 واطلب المكافأة الترحيبية. بعد التحقق من اجتياز KYC Level 3 وكون هذا إيداعك الأول المؤهِّل، تُضاف مكافأة 200% للحساب خلال 24-48 ساعة."}}
  ]
}
</script>'''
    extra = jsonld + '\n' + hrl
    head = head_common(
        'رمز Stake الترويجي MAX3000 - مكافأة 200% حتى $3,000 عند التسجيل',
        'رمز Stake.com الترويجي MAX3000: مكافأة 200% على الإيداع الأول حتى $3,000، اشتراط رهان 40x، KYC Level 3 مطلوب. تم التحقق في يونيو 2026.',
        'https://winnersclub.com/ar/promo-code/',
        'https://winnersclub.com/images/og/promo-code.png',
        extra_head=extra
    )
    calc_script = '''  <script>
    (function(){
      var range = document.getElementById('depRange');
      var num = document.getElementById('depAmount');
      var bonusOut = document.getElementById('bonusOut');
      var wagerOut = document.getElementById('wagerOut');
      var totalOut = document.getElementById('totalOut');
      var effOut = document.getElementById('effOut');
      if(!range || !num) return;
      var fmt = function(n){ return '$' + Math.round(n).toLocaleString('en-US'); };
      function recalc(){
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
      }
      range.addEventListener('input', function(){ num.value = range.value; recalc(); });
      num.addEventListener('input', recalc);
      num.addEventListener('change', recalc);
      recalc();
    })();
  </script>'''
    body = f'''<body>
{nav_block()}
  <!-- HERO -->
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-promo-3.avif') type('image/avif'), url('/images/girl-promo-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">إذا وجدت هذه الصفحة، فقد وجدت الرمز.</p>
        <h1 class="ch-title text-gradient-gold">الرمز الترويجي لـ Stake.com: <bdi dir="ltr">MAX3000</bdi><span class="h1-sub">مكافأة 200% حتى <bdi dir="ltr">$3,000</bdi> على Stake.com.</span></h1>
        <p class="ch-sub">الرمز هو MAX3000. مكافأة 200% على الإيداع الأول حتى <bdi dir="ltr">$3,000</bdi>. رهان 40x على الإيداع والمكافأة معاً. KYC Level 3 مطلوب للصرف. اللاعبون الأمريكيون يستخدمون <a href="/ar/stake-us-bonus/" style="color:var(--gold);text-decoration:underline;">مكافأة Stake.us السويبستيكس</a> بنفس الرمز على منصة مختلفة.</p>
        <time datetime="2026-06-18" class="verified-stamp">آخر تحقق: 18 يونيو 2026</time>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">استخدم MAX3000 على Stake.com</a>
          <a href="#calculator" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">احسب مكافأتك</a>
        </div>
      </div>
    </div>
  </section>

  <!-- CODE CARD -->
  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">رمز النادي</div>
        <div class="code-display">MAX3000</div>
        <div class="code-meta">مكافأة 200% &middot; حتى <bdi dir="ltr">$3,000</bdi> &middot; حد أدنى للإيداع <bdi dir="ltr">$10</bdi> &middot; رهان 40x على الإيداع والمكافأة &middot; KYC Level 3 مطلوب &middot; للعملاء الجدد 18+</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAX3000">نسخ الرمز</button>
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">سلّم الرمز للمتعامل &rarr;</a>
        </div>
      </div>
    </div></section>

  <!-- BONUS CALCULATOR -->
  <section class="section" id="calculator">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">حاسبة مكافأة <span class="text-gradient-gold">Stake.com</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">حرّك المنزلق. الحسابات دقيقة: إيداع بين <bdi dir="ltr">$10</bdi> و<bdi dir="ltr">$1,500</bdi>، مكافأة 200% تصل تناسبياً حتى <bdi dir="ltr">$3,000</bdi>، رهان 40x على مجموع الإيداع والمكافأة.</p>
      </div>
      <div class="bonus-calc">
        <h3>مبلغ الإيداع الأول على Stake.com</h3>
        <div class="bonus-calc-input">
          <label for="depAmount">مبلغ الإيداع (USD)</label>
          <input type="range" id="depRange" min="10" max="1500" step="10" value="500">
          <input type="number" id="depAmount" min="10" max="1500" step="10" value="500">
        </div>
        <div class="bonus-calc-row">
          <div class="stat">
            <p class="stat-label">المكافأة الممنوحة</p>
            <p class="stat-value" id="bonusOut">$1,000</p>
            <p class="stat-sub">200% من الإيداع، سقف المكافأة <bdi dir="ltr">$3,000</bdi></p>
          </div>
          <div class="stat">
            <p class="stat-label">مبلغ الرهان المطلوب</p>
            <p class="stat-value" id="wagerOut">$60,000</p>
            <p class="stat-sub">(الإيداع + المكافأة) × 40، يشمل الكازينو والرياضة</p>
          </div>
          <div class="stat">
            <p class="stat-label">إجمالي الرصيد القابل للعب</p>
            <p class="stat-value" id="totalOut">$1,500</p>
            <p class="stat-sub">رصيد الحساب بعد الصرف: الإيداع + مكافأة المطابقة</p>
          </div>
          <div class="stat">
            <p class="stat-label">كفاءة المطابقة</p>
            <p class="stat-value" id="effOut">200%</p>
            <p class="stat-sub">تنخفض دون 200% إذا تجاوزت سقف الإيداع <bdi dir="ltr">$1,500</bdi></p>
          </div>
        </div>
        <p class="bonus-calc-footer"><strong style="color:var(--gold);">الحد الأقصى للمكافأة هو <bdi dir="ltr">$3,000</bdi>.</strong> إيداع <bdi dir="ltr">$1,500</bdi> يمنحك كامل <bdi dir="ltr">$3,000</bdi>. الإيداعات التي تتجاوز <bdi dir="ltr">$1,500</bdi> تُعالَج لكن المكافأة لا تزداد.</p>
        <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="bonus-calc-cta">اطلب MAX3000 على Stake.com &rarr;</a>
      </div>

      <div class="eligibility-grid">
        <div class="item"><strong>العمر</strong><span>18 سنة فأكثر (21+ في بعض المناطق)</span></div>
        <div class="item"><strong>نوع العميل</strong><span>عملاء جدد، الإيداع الأول فقط</span></div>
        <div class="item"><strong>الحد الأدنى للإيداع</strong><span>USD <bdi dir="ltr">$10</bdi> أو ما يعادله بالعملات الرقمية</span></div>
        <div class="item"><strong>الحد الأقصى للمكافأة</strong><span><bdi dir="ltr">$3,000</bdi> (يُحقَّق بإيداع <bdi dir="ltr">$1,500</bdi>)</span></div>
        <div class="item"><strong>KYC</strong><span>إتمام Level 3 مطلوب قبل الصرف</span></div>
        <div class="item"><strong>طريقة الصرف</strong><span>تواصل مع الدعم المباشر بعد الإيداع الأول</span></div>
        <div class="item"><strong>وقت الصرف</strong><span>24-48 ساعة بعد التحقق من الأهلية</span></div>
        <div class="item"><strong>تتبع التقدم</strong><span>يظهر تقدم الرهان في تبويب VIP</span></div>
      </div>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://help.stake.com/en/articles/4793505-what-is-the-welcome-bonus" target="_blank" rel="noopener">مساعدة Stake، المكافأة الترحيبية</a> · <a href="https://help.stake.com/en/articles/4793499-account-verification" target="_blank" rel="noopener">مساعدة Stake، مستويات KYC</a> · <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com، شروط MAX3000</a></p>
    </div>
  </section>

  <!-- COMPARISON TABLE -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مقارنة جميع رموز Stake <span class="text-gradient-gold">النشطة</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">سبعة رموز، فائز واحد. هذا هو سبب توصية النادي بـ MAX3000 فقط.</p></div>
      <table class="data-table" style="max-width:100%;overflow-x:auto;display:block;">
        <thead>
          <tr>
            <th>الرمز</th>
            <th>نسبة المطابقة</th>
            <th>الحد الأقصى للمكافأة</th>
            <th>لفات مجانية</th>
            <th>الحد الأدنى للإيداع</th>
            <th>ريكباك فقط</th>
            <th>ملاحظات</th>
          </tr>
        </thead>
        <tbody>
          <tr class="win">
            <td><strong>MAX3000</strong></td>
            <td>200%</td>
            <td><bdi dir="ltr">$3,000</bdi></td>
            <td>لا</td>
            <td><bdi dir="ltr">$10</bdi></td>
            <td>لا</td>
            <td>رمز النادي. الدعم المباشر يُضيف 200% يدوياً، رهان 40x على الإيداع والمكافأة.</td>
          </tr>
          <tr>
            <td>NEWBONUS</td>
            <td>200%</td>
            <td><bdi dir="ltr">$3,000</bdi></td>
            <td>لا</td>
            <td><bdi dir="ltr">$10</bdi></td>
            <td>لا</td>
            <td>رمز عام متاح، يعمل على جميع المرايا. بدون لفات.</td>
          </tr>
          <tr>
            <td>HELLA200</td>
            <td>200%</td>
            <td><bdi dir="ltr">$3,000</bdi></td>
            <td>لا</td>
            <td><bdi dir="ltr">$50</bdi></td>
            <td>لا</td>
            <td>حد أدنى للإيداع مرتفع. بدون لفات.</td>
          </tr>
          <tr>
            <td>STRAFECASVIP</td>
            <td>200%</td>
            <td><bdi dir="ltr">$2,000</bdi></td>
            <td>لا</td>
            <td><bdi dir="ltr">$10</bdi></td>
            <td>لا</td>
            <td>شراكة Strafe. السقف أقل بـ $1,000 من MAX3000.</td>
          </tr>
          <tr>
            <td>HELLAGOOD</td>
            <td>لا</td>
            <td>لا</td>
            <td>لا</td>
            <td>لا</td>
            <td>نعم (5%)</td>
            <td>ريكباك فقط. بدون مطابقة إيداع.</td>
          </tr>
          <tr>
            <td>HELLAFREE</td>
            <td>لا</td>
            <td><bdi dir="ltr">$1</bdi> بدون إيداع</td>
            <td>لا</td>
            <td>لا شيء</td>
            <td>لا</td>
            <td>$1 مجاناً بعد KYC. قيمة ضئيلة.</td>
          </tr>
        </tbody>
      </table>
      <p class="research-sources" style="font-size:12px;color:var(--text-muted);margin-top:16px;">المصادر: <a href="https://www.freetips.com/bonus-code/stake-promo-code/" target="_blank" rel="noopener">freetips.com دليل رموز Stake</a>، <a href="https://stake.com/promotions/welcome-offer" target="_blank" rel="noopener">شروط العرض الترحيبي من Stake</a></p>
    </div>
  </section>

  <!-- HOW TO REDEEM -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">خطوات <span class="text-gradient-gold">الصرف</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">تسجيل، توثيق، إيداع، إخبار الدعم المباشر بـ MAX3000. المكافأة تُمنح يدوياً من المشغِّل.</p></div>
      <div class="step-cards anim-stagger" id="redeem">
        <div class="step-card"><h3>1. افتح الباب</h3><p>اضغط على <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener">رابط الشراكة للدخول إلى Stake.com</a> واضغط تسجيل. البريد الإلكتروني، اسم المستخدم، كلمة المرور، تاريخ الميلاد.</p></div>
        <div class="step-card"><h3>2. أكمل التوثيق حتى Level 3</h3><p>Stake يشترط <strong>KYC Level 3</strong> قبل صرف المكافأة الترحيبية. ارفع وثيقة هوية مصورة ومستند إثبات عنوان ووثائق Level 3 الإضافية. العرض الترحيبي مشروط باجتياز هذه المرحلة.</p></div>
        <div class="step-card"><h3>3. أودع من <bdi dir="ltr">$10</bdi> فأكثر</h3><p>أودع ما بين <bdi dir="ltr">$10</bdi> و<bdi dir="ltr">$1,500</bdi>. مكافأة 200% تتصاعد تناسبياً حتى سقف <bdi dir="ltr">$3,000</bdi>. الإيداعات التي تتجاوز <bdi dir="ltr">$1,500</bdi> تُعالَج لكن المكافأة لا تزداد.</p></div>
        <div class="step-card"><h3>4. اطلب MAX3000 عبر الدعم المباشر</h3><p>بعد تسوية الإيداع أرسل رسالة لفريق دعم Stake المباشر وأخبرهم أنك سجّلت بـ <span class="code-highlight">MAX3000</span> وتريد المكافأة الترحيبية. بعد التحقق من أهليتك تُضاف مكافأة 200% خلال <strong>24-48 ساعة</strong>.</p></div>
      </div>
      <div class="club-body" style="margin-top:32px;padding:20px;background:var(--elevated);border-radius:10px;border-right:3px solid var(--gold);">
        <p style="margin:0;font-size:14px;color:var(--text-dim);"><strong style="color:var(--gold);">مهم:</strong> المكافأة الترحيبية في Stake.com ليست حقلاً لإدخال الرمز يُطبَّق تلقائياً، بل رصيد يُمنح يدوياً من المشغِّل. سجّل عبر رابط الشراكة، أكمل KYC Level 3، أودع، ثم افتح المحادثة المباشرة وأخبرهم بـ MAX3000. يمكنك تتبع تقدم الرهان (الإيداع + المكافأة) × 40 في تبويب <strong>VIP</strong> بعد التفعيل.</p>
      </div>
    </div>
  </section>

  <!-- GIRL BREAK -->
  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-promo-2.avif') type('image/avif'), url('/images/girl-promo-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">أكبر <span class="text-gradient-gold">رمز</span> في الصالة</h2>
      <p class="girl-break-sub">همس <span class="code-highlight">MAX3000</span> للمتعامل. 200% حتى <bdi dir="ltr">$3,000</bdi> على Stake.com، والدعم المباشر يتولى الباقي.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">سلّم الرمز للمتعامل</a>
    </div>
  </section>

  <!-- STAKE.US POINTER -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">هل تلعب من <span class="text-gradient-gold">الولايات المتحدة؟</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Stake.com محدود في الولايات المتحدة. الرمز MAX3000 يفتح أيضاً مكافأة ترحيبية على Stake.us السويبستيكس لكن بهيكل مختلف تماماً: Stake Cash وGold Coins مجاناً عند التسجيل، مع معدل لعب 3x قبل الاستبدال.</p>
      </div>
      <div class="club-body" style="max-width:720px;margin:0 auto;text-align:center;">
        <p>منصة مختلفة، عملة مختلفة، شروط مختلفة. خصصنا صفحة مستقلة بحاسبة وتفاصيل الأهلية.</p>
        <a href="/ar/stake-us-bonus/" class="btn btn-signup btn-gold-grad" style="margin-top:20px;display:inline-block;">فتح حاسبة مكافأة Stake.us &rarr;</a>
      </div>
    </div>
  </section>

  <!-- TERMS -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الشروط بلغة <span class="text-gradient-gold">عربية واضحة</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">بدون طباعة صغيرة مدفونة في PDF. إليك ما تنطوي عليه الشروط الفعلية.</p></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card">
          <h3>الرهان: 40x على الإيداع والمكافأة</h3>
          <p>معدل اللعب يُطبَّق على مجموع الإيداع والمكافأة معاً، لا على المكافأة وحدها. <bdi dir="ltr">$500</bdi> إيداع + <bdi dir="ltr">$1,000</bdi> مكافأة = <bdi dir="ltr">$1,500</bdi> × 40 = <bdi dir="ltr">$60,000</bdi> رهاناً. احسب قبل استهداف المكافأة الكاملة.</p>
        </div>
        <div class="club-card">
          <h3>KYC Level 3 إلزامي</h3>
          <p>Stake يعمل بتحقق متدرج. Level 1 يتيح الرهان، Level 2 يرفع حدود الإيداع، <strong>Level 3</strong> هو مرحلة التوثيق الوثائقي التي تفتح المكافأة الترحيبية والسحوبات الكبيرة. في الإعدادات &gt; التحقق، قدّم الهوية وإثبات العنوان ومصدر الأموال.</p>
        </div>
        <div class="club-card">
          <h3>نسبة مساهمة كل نوع لعبة</h3>
          <p>ألعاب الكازينو ذات هامش بيت 4% فأكثر تُسهم بـ 100%. الرهانات الرياضية 75%. ألعاب التاجر المباشر والسلوتس ذات RTP المرتفع (هامش بيت أقل من 4%) تُسهم بنسبة مخفضة أو 0%. ركّز على Stake Originals أو السلوتس ذات هامش بيت 4% فأكثر.</p>
        </div>
        <div class="club-card">
          <h3>طريقة الصرف</h3>
          <p>بعد الإيداع الأول تواصل مع الدعم المباشر وأخبرهم بـ MAX3000. بعد التحقق من KYC Level 3 تُضاف مكافأة 200% خلال <strong>24-48 ساعة</strong>. لا يوجد حقل لإدخال الرمز تلقائياً، المكافأة الترحيبية تُمنح يدوياً من المشغِّل.</p>
        </div>
        <div class="club-card">
          <h3>للعملاء الجدد فقط، الإيداع الأول</h3>
          <p>MAX3000 ينطبق فقط على الإيداع الأول المؤهِّل لحساب Stake.com جديد. الحسابات القائمة لا يمكنها الاسترداد بأثر رجعي، والإيداعات اللاحقة لا تُطابَق بموجب هذا العرض الترحيبي.</p>
        </div>
        <div class="club-card">
          <h3>الحد الأدنى والدول المحظورة</h3>
          <p>الحد الأدنى للإيداع المفعِّل هو <bdi dir="ltr">$10</bdi>، والحد الأقصى المؤهِّل <bdi dir="ltr">$1,500</bdi>. الولايات المتحدة والمملكة المتحدة (منذ مارس 2025) وأستراليا ومعظم أوروبا محجوبة على stake.com. اللاعبون الأمريكيون لديهم <a href="/ar/stake-us-bonus/" style="color:var(--gold);">مكافأة Stake.us</a> المخصصة، وغيرهم يجدون النطاقات المناسبة في <a href="/ar/mirror/" style="color:var(--gold);">صفحة المرايا</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ONGOING PROMOTIONS -->
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">العروض الدائمة: <span class="text-gradient-gold">أكثر من 700,000 دولار أسبوعياً</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">المكافأة الترحيبية مجرد بداية. Stake يوزع أكثر من 700 ألف دولار أسبوعياً على اللاعبين الحاليين.</p></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));">
        <div class="club-card">
          <h3>سباق يومي بـ 100,000 دولار</h3>
          <p>جميع اللاعبين المسجّلين يشاركون تلقائياً دون حاجة للتسجيل. الرهان على ألعاب الكازينو يجمع نقاط المتصدرين، وعند انتهاء فترة الأهلية البالغة 24 ساعة يتقاسم أفضل 5000 لاعب الجائزة البالغة 100,000 دولار. السباق يُعاد تشغيله بشكل متواصل.</p>
        </div>
        <div class="club-card">
          <h3>سحب أسبوعي بـ 75,000 دولار</h3>
          <p>تذكرة سحب لكل رهان بقيمة 1,000 دولار خلال فترة الأهلية. لا تسجيل مطلوب. الجائزة 75,000 دولار تُسحب مباشرة كل سبت في GMT 2 مساءً. لا يوجد سقف لتراكم التذاكر.</p>
        </div>
        <div class="club-card">
          <h3>فتح الكازينو بـ 50,000 دولار أسبوعياً</h3>
          <p>عروض مهمات أسبوعية على ألعاب مميزة جديدة. المكافأة الأسبوعية 50,000 دولار تتوزع على أكبر المراهنين والفائزين العشوائيين. أداة Stake الرئيسية لتحفيز المشاركة في الألعاب الجديدة.</p>
        </div>
        <div class="club-card">
          <h3>Pragmatic Drops &amp; Wins</h3>
          <p>Stake تُشغِّل برنامج Pragmatic Play الشهير للشبكة: Sweet Bonanza وGates of Olympus 1000 وSugar Rush وغيرها. الجوائز تسقط عشوائياً أثناء اللفات بأموال حقيقية. أكثر من 50,000 جائزة من مجموع الشبكة أسبوعياً. الشرط الوحيد هو الرهان بأموال حقيقية على الألعاب المؤهِّلة من Pragmatic.</p>
        </div>
        <div class="club-card">
          <h3>تأمين الرياضة</h3>
          <p>عروض تأمين حسب الحدث: سداد مبكر عند تقدم بـ هدفين في NHL، سداد مبكر في NBA عند تقدم بـ 12 نقطة في الشوط الأول، استرداد في MLB لـ 9 أشواط، تأمين الحكم المتقسم في UFC، سداد مبكر لـ Premier League، حماية باكيه Stake Shield، استرداد في بعض سباقات الخيل. تتغير حسب التقويم الرياضي.</p>
        </div>
        <div class="club-card">
          <h3>مكافأة إعادة شحن VIP</h3>
          <p>لاعبو VIP من مستوى Platinum فما فوق يحصلون على مكافآت إعادة الشحن: Platinum I كل 14 يوماً، Platinum IV بشكل مستمر. المبلغ يُرجَّح بالخسائر الأخيرة، فتأتي مكافأة أكبر في الفترات الأقل حظاً. مستويات VIP الأدنى يوم الجمعة هو يوم إعادة الشحن الافتراضي.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- BONUS DROP CODES -->
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">رموز المكافأة الفورية: <span class="text-gradient-gold">الميزة غير المعروفة</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">خارج نطاق العرض الترحيبي، Stake يُشغِّل رموزاً مجانية محدودة الوقت يُفوِّتها معظم اللاعبين.</p></div>
      <div class="club-body">
        <p>رموز المكافأة الفورية هي رموز أبجدية رقمية قصيرة تُنشَر على قناة Telegram الرسمية لـ Stake وحساباتها على منصات التواصل الاجتماعي. خلافاً للمكافأة الترحيبية لا يوجد اشتراط رهان، المبلغ المدفوع نقد مجاني. الشرط هو الرهان بمبلغ معين خلال 7 أيام السابقة وانتهاء سقف الاستبدال بسرعة.</p>
        <p>القيمة المعتادة <strong>دولار إلى 5 دولارات للرمز الواحد</strong> وتُنشَر عدة رموز يومياً عبر القنوات. ومجتمعةً لا يمكن تجاهلها. كبار VIP من الذهب فأكثر يتلقون رموزاً بفئات أكبر عبر البريد الإلكتروني وقنوات Telegram الخاصة.</p>
        <p><strong>طريقة الاستبدال:</strong> الإعدادات &gt; العروض &gt; حقل <em>استبدال رمز المكافأة</em> &gt; أدخل الرمز واضغط إرسال. لا يلزم إيداع.</p>
      </div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:32px;">
        <div class="club-card">
          <h3>@StakecomDailyDrops</h3>
          <p>قناة Telegram الرئيسية لرموز الإسقاط العامة. رموز متعددة يومياً. فعّل الإشعارات لأن الرمز يُغلَق فور استنفاد الاستبدال.</p>
        </div>
        <div class="club-card">
          <h3>@StakeCasino</h3>
          <p>الـ Telegram الرئيسي لـ Stake. إعلانات رسمية وبعض الرموز الترويجية الكبرى. يُنصَح بالاشتراك إلى جانب قناة الإسقاط.</p>
        </div>
        <div class="club-card">
          <h3>@Stakelivechallenges</h3>
          <p>تنبيهات التحدي المباشر ومكافآته المرتبطة. آلية مختلفة عن رموز الإسقاط لكنها في نفس فئة المكافآت منخفضة العتبة.</p>
        </div>
        <div class="club-card">
          <h3>@Stake (X/تويتر)</h3>
          <p>رموز إسقاط تظهر أحياناً على حساب Stake في X/Twitter خلال الترويجات الكبرى وبطولات الرياضة.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">الباب</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما هو الرمز الترويجي لـ Stake.com؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>الرمز هو <span class="code-highlight">MAX3000</span>. سجّل على Stake.com عبر رابط الشراكة، أكمل KYC Level 3، أودع ما بين <bdi dir="ltr">$10</bdi> و<bdi dir="ltr">$1,500</bdi> كإيداع أول، ثم أخبر الدعم المباشر بـ MAX3000. الأهلية تُتحقَّق منها وتُضاف مكافأة 200% حتى <bdi dir="ltr">$3,000</bdi> خلال 24-48 ساعة.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما الحد الأقصى لمكافأة MAX3000؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>مكافأة 200% <strong>حتى <bdi dir="ltr">$3,000</bdi></strong>. إيداع <bdi dir="ltr">$1,500</bdi> يُحقق الحد الأقصى <bdi dir="ltr">$3,000</bdi>. الحد الأدنى المؤهِّل <bdi dir="ltr">$10</bdi>، والأقصى <bdi dir="ltr">$1,500</bdi>. الإيداعات التي تتجاوز <bdi dir="ltr">$1,500</bdi> تُعالَج لكن المكافأة لا تزداد.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما اشتراط الرهان؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p><strong>40x على الإيداع والمكافأة معاً.</strong> إيداع <bdi dir="ltr">$500</bdi> يُولِّد مكافأة <bdi dir="ltr">$1,000</bdi>، مجموعهما <bdi dir="ltr">$1,500</bdi> × 40 = <bdi dir="ltr">$60,000</bdi> رهاناً مطلوباً. ألعاب الكازينو ذات هامش 4% فأكثر تُسهم بـ 100%، الرهانات الرياضية بـ 75%. التقدم يظهر في تبويب VIP.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل التحقق من الهوية مطلوب؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. Stake.com يشترط <strong>KYC Level 3</strong> قبل صرف المكافأة الترحيبية. في الإعدادات &gt; التحقق، قدّم وثيقة هوية مصورة ومستند إثبات عنوان ومستند مصدر الأموال. لا تُصرَف المكافأة إلا بعد اجتياز Level 3.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">كيف تُصرَف المكافأة؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>مكافأة MAX3000 الترحيبية في Stake.com ليست تلقائية، بل <strong>رصيد يُمنح يدوياً من المشغِّل</strong>. بعد تسوية الإيداع الأول افتح المحادثة المباشرة وأخبرهم بـ MAX3000 واطلب المكافأة الترحيبية. مكافأة 200% تُضاف للحساب خلال <strong>24-48 ساعة</strong>.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل يمكن استخدامها في الرياضة والكازينو معاً؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. مطابقة الإيداع تنطبق على الكازينو والرياضة والبوكر. الرهانات الرياضية تُسهم بـ 75% في متطلب الرهان، وألعاب الكازينو ذات هامش 4% فأكثر بـ 100%، والتاجر المباشر والسلوتس ذات RTP المرتفع بنسبة مخفضة أو 0%.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">للعملاء الجدد فحسب؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. MAX3000 ينطبق فقط على الإيداع الأول المؤهِّل لحساب Stake.com جديد. الحسابات القائمة لا يمكنها الاسترداد بأثر رجعي، غير أنهم لا يزالون يستطيعون استخدام رموز المكافأة الفورية التي تُنشَر على قناة Telegram لـ Stake والتي لا تشترط رهاناً.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">ما حد العمر؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>18 سنة فأكثر في معظم المناطق التي يعمل فيها Stake.com. بعض المناطق تشترط 21 سنة. منصة السويبستيكس <a href="/ar/stake-us-bonus/" style="color:var(--gold);">Stake.us</a> تشترط صراحةً 21 سنة فأكثر.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SIGNATURE -->
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر المتعامل أن وينرز كلوب أرسلك.</p>
    </div>
  </section>
{sticky_cta('الرمز هو <span class="code-highlight">MAX3000</span>. 200% حتى <bdi dir="ltr">$3,000</bdi> على Stake.com. أخبر الدعم المباشر بعد الإيداع الأول.')}
{footer_block()}
{scripts()}
{calc_script}
{rooms_grid()}</body>
</html>'''
    return head + '\n' + body


def make_casino():
    page_path = 'ar/casino/'
    hrl = hreflang_block(page_path)
    jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "كازينو Stake - أكثر من 3000 لعبة مع الرمز MAX3000",
  "description": "كازينو Stake.com: أكثر من 3000 لعبة، سلوتس، بلاك جاك، روليت، تاجر مباشر، أوريجينالز. الرمز MAX3000 يفتح مكافأة 200% حتى $3,000.",
  "url": "https://winnersclub.com/ar/casino/"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://winnersclub.com/ar/"},
    {"@type": "ListItem", "position": 2, "name": "كازينو", "item": "https://winnersclub.com/ar/casino/"}
  ]
}
</script>'''
    extra = jsonld + '\n' + hrl
    head = head_common(
        'كازينو Stake - أكثر من 3000 لعبة مع الرمز MAX3000',
        'كازينو Stake.com: أكثر من 3000 لعبة تشمل السلوتس والبلاك جاك والروليت والتاجر المباشر وألعاب Originals. الرمز MAX3000 يفتح 200% حتى $3,000.',
        'https://winnersclub.com/ar/casino/',
        'https://winnersclub.com/images/og/casino.png',
        extra_head=extra
    )
    body = f'''<body>
{nav_block()}
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-casino-3.avif') type('image/avif'), url('/images/girl-casino-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">الصالة الرئيسية مفتوحة.</p>
        <h1 class="ch-title text-gradient-gold">كازينو <bdi dir="ltr">Stake.com</bdi><span class="h1-sub">أكثر من 3000 لعبة. الرمز <bdi dir="ltr">MAX3000</bdi> يفتح <bdi dir="ltr">$3,000</bdi>.</span></h1>
        <p class="ch-sub">كازينو Stake مُصمَّم للعب الحقيقي. سلوتس من أفضل الموردين، بلاك جاك، روليت، باكارا، بوكر، تاجر مباشر في استوديوهات احترافية، وألعاب Originals الحصرية. الرمز <span class="code-highlight">MAX3000</span> يفتح <strong>200% حتى <bdi dir="ltr">$3,000</bdi></strong> على الإيداع الأول.</p>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">ادخل الكازينو مع MAX3000</a>
          <a href="/ar/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">تفاصيل الرمز الترويجي</a>
        </div>
      </div>
    </div>
  </section>
{reserves_ticker()}
{promo_strip()}

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مكتبة <span class="text-gradient-gold">الألعاب</span></h2><p class="section-subtitle">أكثر من 3000 لعبة من مزودين عالميين من الطراز الأول.</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>السلوتس</h3><p>مئات الألعاب من Pragmatic Play وHacksaw Gaming وNetEnt وNoLimit City وEvolution Gaming وغيرهم. Gates of Olympus 1000 وSweet Bonanza وDog House Megaways وBig Bass Bonanza تتصدر المكتبة. RTP يتراوح بين 94% و98% حسب اللعبة. Stake توفر معدلات بيت فعلية بشفافية كاملة.</p></div>
        <div class="club-card"><h3>الطاولات الكلاسيكية</h3><p>بلاك جاك بعشرات المتغيرات من بلاك جاك كلاسيكي إلى بلاك جاك VIP بحدود رهان عالية. رولة أمريكية وأوروبية وفرنسية. باكارا بقواعد ميسرة. بوكر بأشكاله المتعددة. Stake تُشغِّل طاولات خاصة بها بجانب ألعاب مزودي الطرف الثالث.</p></div>
        <div class="club-card"><h3>التاجر المباشر</h3><p>استوديوهات احترافية من Evolution Gaming وPragmatic Play Live وEzugi. بلاك جاك مباشر بـ 20+ طاولة في آنٍ واحد. رولة مباشرة. باكارا مباشر. Lightning Roulette وCrazy Time وMegaball من أشهر الألعاب. التدفق المباشر بجودة 4K متاح في معظم المناطق.</p></div>
        <div class="club-card"><h3>Stake Originals</h3><p>ألعاب حصرية طوّرتها Stake لا توجد في أي كازينو آخر: Plinko وMines وLimbo وDice وWheel وKeno وScarab وTower وCrash وHilo وVideoPoker. شفافية كاملة في المعادلات. RTP مُتحقَّق منه. هذه هي الألعاب التي تعمل عليها خوارزميات النادي الداخلي.</p></div>
        <div class="club-card"><h3>شبكة جوائز Pragmatic</h3><p>Stake تُشغِّل برنامج Drops &amp; Wins من Pragmatic Play، أكبر برنامج جوائز شبكي في صناعة الكازينو عبر الإنترنت. أكثر من 50,000 جائزة من مجموع الشبكة أسبوعياً تسقط عشوائياً في الألعاب المؤهِّلة أثناء اللفات بأموال حقيقية. Sweet Bonanza وGates of Olympus وSugar Rush من أكثر الألعاب المشاركة.</p></div>
        <div class="club-card"><h3>بلاك جاك البث المباشر</h3><p>Stake Casino Live تُشغِّل بلاك جاك بث مباشر على قناة Kick مع بعض المشاهير والمؤثرين في أوقات محددة. اللعبة في الوقت الفعلي أمام الجمهور. هذا النموذج جذب ملايين المشاهدين وأثّر في نمو قاعدة لاعبي Stake بشكل لافت.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أرقام <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">الألعاب</div><div class="ic-value">3,000+</div><div class="ic-detail">من Pragmatic وEvolution وHacksaw وNetEnt وNoLimit City وعشرات المزودين الآخرين. مضافة باستمرار.</div></div>
        <div class="intel-card"><div class="ic-label">GGR</div><div class="ic-value"><bdi dir="ltr">$4.7B</bdi></div><div class="ic-detail">إيرادات قمار إجمالية موثّقة تُرسّخ Stake كواحدة من أكبر منصات القمار عبر الإنترنت في العالم.</div></div>
        <div class="intel-card"><div class="ic-label">الحسابات</div><div class="ic-value">+21 مليون</div><div class="ic-detail">أكثر من 21 مليون حساب مُسجَّل. قاعدة لاعبين نشطة في أكثر من 100 دولة.</div></div>
        <div class="intel-card"><div class="ic-label">السحوبات</div><div class="ic-value">30 دقيقة</div><div class="ic-detail">معظم سحوبات العملات الرقمية تكتمل في 30-60 دقيقة. TRX وXRP وSOL في ثوانٍ إلى دقائق.</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المدفوعات في <span class="text-gradient-gold">كازينو Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>العملات الرقمية المدعومة</h3><p>Bitcoin وEthereum وLitecoin وRipple وSolana وTRON وBinance Coin وDogecoin وCardano وAvalanche وChainlink وPolygon وTether (TRC20) وUSD Coin. الإيداعات فورية. الحد الأدنى للإيداع صغير جداً ويختلف حسب العملة.</p></div>
        <div class="club-card"><h3>العملات الورقية عبر MoonPay</h3><p>Stake تدعم الإيداع بالعملات الورقية عبر شراكة MoonPay لبعض المناطق: بطاقات Visa وMastercard والتحويل البنكي وخدمات الدفع المحلية. رسوم معالجة MoonPay تُطبَّق بشفافية. السحب الورقي يستغرق 1-5 أيام عمل.</p></div>
        <div class="club-card"><h3>حدود الرهان</h3><p>الحدود تتفاوت بين اللعبة والمستوى. لاعبو المستوى الأساسي لديهم حدود دنيا وعليا محددة. لاعبو VIP يمكنهم الطلب بزيادة الحدود عبر مدير الحساب. سلوتس Stake Originals تسمح برهانات بحجم المشتبه بهم VIP بعقود دقيقة.</p></div>
        <div class="club-card"><h3>اشتراط KYC Level 3</h3><p>التسجيل الأساسي يُمكِّن من الرهان. لكن لاستلام المكافأة الترحيبية MAX3000 والسحوبات الكبيرة يلزم إتمام KYC Level 3. قدّم الهوية الوثائقية وإثبات العنوان ومصدر الأموال في قسم الإعدادات.</p></div>
      </div>
    </div>
  </section>

  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">3000 لعبة. <span class="text-gradient-gold">رمز واحد.</span></h2>
      <p class="girl-break-sub">الرمز <span class="code-highlight">MAX3000</span> يفتح 200% حتى <bdi dir="ltr">$3,000</bdi> عند الإيداع الأول.</p>
      <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">ادخل الكازينو الآن</a>
    </div>
  </section>

  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة الصالة <span class="text-gradient-gold">الشائعة</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">كم عدد الألعاب في كازينو Stake؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>أكثر من 3,000 لعبة من مزودين عالميين تشمل Pragmatic Play وEvolution Gaming وHacksaw Gaming وNetEnt وNoLimit City. بالإضافة إلى مكتبة Stake Originals الحصرية التي تضم Plinko وMines وCrash وLimbo والمزيد.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل كازينو Stake عادل؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. Stake Originals تستخدم نظام التحقق القابل للإثبات (Provably Fair) الذي يتيح للاعبين التحقق من عشوائية كل جولة بشكل مستقل. ألعاب الطرف الثالث مرخّصة ومُختبَرة من مختبرات معتمدة. معدلات RTP مُعلَنة للمكتبة الكاملة.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">هل يمكن اللعب بالعملات الرقمية في كازينو Stake؟
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>نعم. Stake.com منصة مخصصة للعملات الرقمية في الأساس وتدعم أكثر من 15 عملة رقمية منها BTC وETH وSOL وTRX وXRP وLTC وUSDT وغيرها. الإيداعات فورية وسحوبات العملات الرقمية تكتمل في 30-60 دقيقة للمبالغ المعتادة.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر المتعامل أن وينرز كلوب أرسلك.</p>
    </div>
  </section>
{sticky_cta('الرمز هو <span class="code-highlight">MAX3000</span>. ادخل كازينو Stake مع 200% حتى <bdi dir="ltr">$3,000</bdi>.')}
{footer_block()}
{scripts()}
{rooms_grid()}</body>
</html>'''
    return head + '\n' + body


# Mini page template for the remaining pages
def make_generic_page(slug, title_ar, desc_ar, h1_ar, h1_sub_ar, hero_img, content_sections, og_image='default.png', extra_jsonld='', faq_items=None):
    """Generic page builder for all remaining AR pages."""
    page_path = f'ar/{slug}/'
    hrl = hreflang_block(page_path)
    canonical = f'https://winnersclub.com/ar/{slug}/'
    
    jsonld = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{title_ar}",
  "description": "{desc_ar}",
  "url": "{canonical}"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "الرئيسية", "item": "https://winnersclub.com/ar/"}},
    {{"@type": "ListItem", "position": 2, "name": "{title_ar.split(' - ')[0]}", "item": "{canonical}"}}
  ]
}}
</script>'''
    if extra_jsonld:
        jsonld += '\n' + extra_jsonld
    
    extra = jsonld + '\n' + hrl
    head = head_common(
        title_ar,
        desc_ar,
        canonical,
        f'https://winnersclub.com/images/og/{og_image}',
        extra_head=extra
    )
    
    faq_html = ''
    if faq_items:
        items_html = ''
        for q, a in faq_items:
            items_html += f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{q}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{a}</p></div>
        </div>\n'''
        faq_html = f'''  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أسئلة <span class="text-gradient-gold">شائعة</span></h2></div>
      <div class="faq-list">
{items_html}      </div>
    </div>
  </section>'''
    
    body = f'''<body>
{nav_block()}
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/{hero_img}.avif') type('image/avif'), url('/images/{hero_img}.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">{h1_ar}<span class="h1-sub">{h1_sub_ar}</span></h1>
        <div class="ch-actions">
          <a href="https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">ادخل مع <bdi dir="ltr">MAX3000</bdi> واحصل على 200% حتى <bdi dir="ltr">$3,000</bdi></a>
        </div>
      </div>
    </div>
  </section>
{reserves_ticker()}
{promo_strip()}
{content_sections}
{faq_html}
  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">أخبر المتعامل أن وينرز كلوب أرسلك.</p>
    </div>
  </section>
{sticky_cta(f'الرمز هو <span class="code-highlight">MAX3000</span>. 200% حتى <bdi dir="ltr">$3,000</bdi>.')}
{footer_block()}
{scripts()}
{rooms_grid()}</body>
</html>'''
    return head + '\n' + body


def make_sports():
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الرياضة في <span class="text-gradient-gold">Stake</span></h2><p class="section-subtitle">25+ رياضة، مئات البطولات، رهانات حية، وعروض خاصة أسبوعياً.</p></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>الرياضات المتاحة</h3><p>كرة القدم من الدوري الإنجليزي الممتاز وإسباني وألماني وإيطالي وفرنسي وأوروبا وبطولات عالمية. كرة السلة NBA وEuroLeague. التنس ATP وWTA وGrand Slam. الهوكي NHL. الغولف PGA. رياضات eSports. MMA وUFC. بيسبول MLB. عشرات الخيارات الإضافية على مدار الساعة.</p></div>
        <div class="club-card"><h3>الرهانات الحية</h3><p>Stake توفر رهانات حية على آلاف الأحداث يومياً مع تحديث أوتار فوري. يمكنك الرهان على نتيجة الشوط الأول، عدد الأهداف، الورقة التالية، المباراة القائمة الآن. الواجهة سريعة الاستجابة والأوتار تتحرك في الوقت الفعلي.</p></div>
        <div class="club-card"><h3>البناء الذاتي لبطاقة الرهان</h3><p>يمكنك بناء رهانات متعددة Parlay بخياراتك، مع مضاعف أوتار مُحسَّب تلقائياً. خيارات المراهنة المباشرة (In-Game Betting) تتوسع لتشمل قرارات تكتيكية دقيقة كالركلة الرابعة عشرة في الدقيقة 73.</p></div>
        <div class="club-card"><h3>مساهمة الرياضة في الرهان</h3><p>الرهانات الرياضية تُسهم بنسبة 75% في استيفاء متطلب الرهان لمكافأة MAX3000. كازينو 100%، رياضة 75%. ضع هذا في حسبانك عند التخطيط لاستيفاء الـ 40x بسرعة: مزج الكازينو يُسرِّع الاستيفاء.</p></div>
        <div class="club-card"><h3>عروض التأمين الرياضي</h3><p>Stake تُشغِّل عروض تأمين دورية: سداد مبكر عند تقدم بهدفين في NHL، سداد عند تقدم بـ 12 نقطة في الشوط الأول في NBA، استرداد في MLB لـ 9 أشواط، تأمين الحكم المتقسم في UFC، سداد مبكر في الدوري الإنجليزي الممتاز، حماية باكيه Stake Shield. تتغير حسب التقويم الرياضي.</p></div>
        <div class="club-card"><h3>السحوبات والمدفوعات</h3><p>مكاسب الرهانات الرياضية تُسحب بنفس آلية الكازينو: عملات رقمية سريعة في 30-60 دقيقة للمبالغ المعتادة، عملات ورقية عبر MoonPay في 1-5 أيام عمل. لا حدود خاصة بالرياضة تختلف عن الكازينو.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">المراهنات الرياضية بالأرقام</h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">الرياضات</div><div class="ic-value">25+</div><div class="ic-detail">كرة القدم، كرة السلة، التنس، الهوكي، الغولف، eSports، MMA، بيسبول، والمزيد.</div></div>
        <div class="intel-card"><div class="ic-label">الأحداث اليومية</div><div class="ic-value">آلاف</div><div class="ic-detail">أحداث قبل المباراة وحية على مدار 24 ساعة طوال الأسبوع.</div></div>
        <div class="intel-card"><div class="ic-label">مساهمة في الرهان</div><div class="ic-value">75%</div><div class="ic-detail">الرهانات الرياضية تُسهم بـ 75% في متطلب رهان MAX3000 البالغ 40x.</div></div>
        <div class="intel-card"><div class="ic-label">هامش الكاشير</div><div class="ic-value">منخفض</div><div class="ic-detail">Stake تُقدِّم هوامش تنافسية في الأحداث الكبرى مقارنة بمنصات الرهان التقليدية.</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">اسبقستيكس الأسبوعية لـ <span class="text-gradient-gold">الرياضة</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>سحب أسبوعي بـ 75,000 دولار</h3><p>تذكرة لكل <bdi dir="ltr">$1,000</bdi> رهان. الرهانات الرياضية مؤهِّلة. السحب كل سبت في GMT 2 مساءً. لا سقف لتراكم التذاكر.</p></div>
        <div class="club-card"><h3>عروض التأمين الموسمية</h3><p>بالتزامن مع الدوريات الكبرى تُشغِّل Stake عروض تأمين حصرية: إذا فزت بـ X نقطة في الشوط الأول سيُدفع رهانك مبكراً. تفاصيل في قسم العروض على المنصة.</p></div>
        <div class="club-card"><h3>ريكباك لاعبي VIP</h3><p>لاعبو VIP من مستوى Platinum فما فوق يحصلون على ريكباك على خسائر الرهان الرياضي ضمن نظام إعادة الشحن المرجَّح بالخسارة الأخيرة.</p></div>
      </div>
    </div>
  </section>'''
    
    faq = [
        ('ما الرياضات المتاحة للرهان في Stake؟', 'أكثر من 25 رياضة تشمل كرة القدم وكرة السلة والتنس والهوكي والغولف وeSports وMMA والبيسبول والمزيد. آلاف الأحداث قبل المباراة والحية يومياً.'),
        ('هل الرهانات الرياضية تُحسَب في متطلب رهان MAX3000؟', 'نعم، بنسبة 75%. ألعاب الكازينو ذات هامش 4%+ تُسهم بـ 100%. دمج الكازينو والرياضة معاً هو الاستراتيجية المثلى لاستيفاء الـ 40x.'),
        ('هل هناك رهانات حية في Stake؟', 'نعم. Stake توفر رهانات حية مع تحديث أوتار في الوقت الفعلي على آلاف الأحداث يومياً عبر جميع الرياضات الكبرى.'),
    ]
    return make_generic_page(
        'sports',
        'Stake المراهنات الرياضية - 25+ رياضة مع الرمز MAX3000',
        'المراهنات الرياضية على Stake.com: أكثر من 25 رياضة، رهانات حية، عروض تأمين أسبوعية. الرمز MAX3000 يفتح 200% حتى $3,000.',
        'المراهنات الرياضية على <bdi dir="ltr">Stake</bdi>',
        'أكثر من 25 رياضة. رهانات حية. الرمز MAX3000 يفتح $3,000.',
        'girl-sports-3',
        content,
        og_image='sports.png',
        faq_items=faq
    )


def make_poker():
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">بوكر <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>أنواع البوكر المتاحة</h3><p>Texas Hold'em وOmaha وOmaha Hi-Lo وSeven-Card Stud وVideoPoker. طاولات نقدية بحدود متعددة من الحدود الدنيا للمبتدئين إلى طاولات High Stakes. بطولات منتظمة بجوائز ضخمة وبطولات تُشغَّل بشكل متواصل.</p></div>
        <div class="club-card"><h3>البوكر المباشر مع التاجر</h3><p>Evolution Gaming وPragmatic Play Live يوفران بوكر مع التاجر المباشر: Casino Hold'em وThree Card Poker وUltimate Texas Hold'em. بث مباشر بجودة عالية من استوديوهات احترافية. الحدود تتناسب مع مستوى جميع اللاعبين.</p></div>
        <div class="club-card"><h3>بوكر Stake Originals</h3><p>VideoPoker من مكتبة Stake Originals الحصرية. نظام التحقق القابل للإثبات يضمن عدالة التوزيع. RTP مُعلَن ومُتحقَّق منه. يُحسَب في متطلب رهان MAX3000.</p></div>
        <div class="club-card"><h3>استراتيجية الرهان</h3><p>ألعاب البوكر والطاولة في الكازينو عموماً ذات هامش بيت أقل من 4% وبالتالي تُسهم بنسبة مخفضة في متطلب الرهان. إذا كنت تسعى لاستيفاء الـ 40x بسرعة، Stake Originals وسلوتس هامش بيت 4%+ هي الخيار الأمثل. البوكر للمتعة والمهارة والرهانات الكبيرة.</p></div>
        <div class="club-card"><h3>بطولات البوكر</h3><p>Stake تُشغِّل بطولات دورية بهياكل مختلفة: Sit &amp; Go وMTT (Multi-Table Tournaments) وفاست بوكر. الجوائز تتراوح من عشرات الدولارات إلى آلاف. يمكن الدخول بالبيتكوين وعملات رقمية أخرى.</p></div>
        <div class="club-card"><h3>الرهان الرياضي مقابل البوكر</h3><p>البوكر الحقيقي (بلاعبين حقيقيين) ليس من الرياضات المعتادة في منصات الرهان. ما تُقدِّمه Stake هو كازينو بوكر وليس بوكر اللاعبين ضد بعضهم (P2P). الأوتار مُحسَّبة من المنصة والنتائج من خوارزميات مُتحقَّق منها.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أرقام <span class="text-gradient-gold">بوكر Stake</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">أنواع اللعب</div><div class="ic-value">5+</div><div class="ic-detail">Texas Hold'em وOmaha وOmaha Hi-Lo وVideoPoker والمزيد.</div></div>
        <div class="intel-card"><div class="ic-label">بوكر مباشر</div><div class="ic-value">متاح</div><div class="ic-detail">Casino Hold'em وThree Card Poker من Evolution وPragmatic بث مباشر.</div></div>
        <div class="intel-card"><div class="ic-label">مساهمة في الرهان</div><div class="ic-value">مخفضة</div><div class="ic-detail">ألعاب هامش 4%- تُسهم بنسبة أقل من 100%. تحقق من جدول المساهمة.</div></div>
        <div class="intel-card"><div class="ic-label">الحد الأدنى</div><div class="ic-value">صغير</div><div class="ic-detail">طاولات بحدود منخفضة متاحة للمبتدئين الذين يبنون مهاراتهم.</div></div>
      </div>
    </div>
  </section>'''
    
    faq = [
        ('هل يوجد بوكر حقيقي (P2P) في Stake؟', 'Stake تُقدِّم كازينو بوكر: ألعاب ضد المنزل بأوتار محسوبة مسبقاً وخوارزميات Provably Fair. ليس بوكراً بلاعبين ضد بعضهم (P2P Poker Room).'),
        ('هل البوكر يُحسَب في متطلب رهان MAX3000؟', 'ألعاب البوكر ذات هامش بيت أقل من 4% تُسهم بنسبة مخفضة. للتسريع في استيفاء الـ 40x، الأفضل استخدام Stake Originals أو سلوتس ذات هامش 4%+.'),
        ('ما هي حدود الرهان في بوكر Stake؟', 'تتراوح من حدود دنيا للمبتدئين إلى طاولات High Stakes لكبار اللاعبين. لاعبو VIP يمكنهم طلب زيادة الحدود عبر مدير الحساب.'),
    ]
    return make_generic_page(
        'poker',
        'بوكر Stake - Texas Hold\'em وأنواع متعددة مع الرمز MAX3000',
        'بوكر Stake.com: Texas Hold\'em وOmaha وVideoPoker وبوكر مباشر. الرمز MAX3000 يفتح مكافأة 200% حتى $3,000 على الإيداع الأول.',
        'بوكر <bdi dir="ltr">Stake</bdi>',
        'Texas Hold\'em والمزيد. الرمز MAX3000 يفتح $3,000.',
        'girl-poker-3',
        content,
        og_image='poker.png',
        faq_items=faq
    )


def make_aviator():
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">لعبة <span class="text-gradient-gold">أفياتور</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>كيف تعمل أفياتور</h3><p>الطائرة تقلع والمضاعف يرتفع من 1x. يجب أن تضغط "سحب" قبل أن تغادر الطائرة المشهد. إذا انتظرت أكثر حصلت على مضاعف أعلى. إذا تأخرت فقدت الرهان كاملاً. اللعبة تعتمد على Provably Fair RNG مع تحديث في كل جولة.</p></div>
        <div class="club-card"><h3>رهانات مزدوجة</h3><p>يمكنك وضع رهانين مستقلين في نفس الجولة. رهان الأول تسحبه عند مضاعف منخفض لتأمين ربح، والثاني تتركه ليواصل الصعود نحو مضاعفات أعلى. هذه الاستراتيجية تجمع بين الحماية وطموح المكسب الكبير.</p></div>
        <div class="club-card"><h3>Provably Fair ومعدل RTP</h3><p>أفياتور Spribe تستخدم نظام Provably Fair. يمكن التحقق من نتيجة كل جولة بشكل مستقل. معدل RTP نحو 97%. كل جولة مستقلة عن السابقة رياضياً، ولا أنماط تنبؤية مضمونة.</p></div>
        <div class="club-card"><h3>أفياتور في Stake Originals</h3><p>Stake تُشغِّل نسخة Crash الخاصة بها ضمن Originals تشبه أفياتور بمبدأ المضاعف المتصاعد. كلتاهما متاحتان على المنصة. Crash من Stake Originals مُتحقَّق من عدالتها بخوارزميات Stake المفتوحة.</p></div>
        <div class="club-card"><h3>استراتيجيات اللعب</h3><p>استراتيجية Martingale (مضاعفة بعد الخسارة) شائعة لكنها مجازفة عالية لطاولة رأس المال. استراتيجية الحد الثابت (السحب دوماً عند 2x مثلاً) تُوازن الأرباح المتوقعة. اللعب بمضاعفات عالية (50x+) ممكن لكن الاحتمالات تتناسب عكسياً.</p></div>
        <div class="club-card"><h3>الإحصاء والتاريخ</h3><p>كل لوحة أفياتور تعرض آخر 100 جولة مع المضاعفات التاريخية. هذا للتوثيق لا للتنبؤ لأن كل جولة مستقلة. يمكنك مشاهدة رهانات اللاعبين الآخرين في الوقت الفعلي ومتى سحب كل منهم.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أرقام <span class="text-gradient-gold">أفياتور</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">RTP</div><div class="ic-value">97%</div><div class="ic-detail">من أعلى معدلات العودة في الألعاب الحية. كل جولة مستقلة ومُتحقَّق منها.</div></div>
        <div class="intel-card"><div class="ic-label">المضاعف الأقصى</div><div class="ic-value">غير محدود نظرياً</div><div class="ic-detail">المضاعف يستمر في الارتفاع حتى تغادر الطائرة المشهد. سُجِّلت مضاعفات تجاوزت 1,000x.</div></div>
        <div class="intel-card"><div class="ic-label">الرهانات المتزامنة</div><div class="ic-value">2</div><div class="ic-detail">رهانان مستقلان في نفس الجولة. استراتيجية مزدوجة: تأمين + مخاطرة.</div></div>
        <div class="intel-card"><div class="ic-label">عادلة وقابلة للإثبات</div><div class="ic-value">نعم</div><div class="ic-detail">كل جولة مُتحقَّق منها بـ Provably Fair. Hash التحقق متاح بعد كل جولة.</div></div>
      </div>
    </div>
  </section>'''
    
    faq = [
        ('ما هي لعبة أفياتور في Stake؟', 'أفياتور لعبة Crash من Spribe متاحة على Stake.com. طائرة تقلع ومضاعف يرتفع من 1x. اضغط "سحب" قبل أن تغادر الطائرة للفوز بالمضاعف الحالي. Provably Fair ومعدل RTP 97%.'),
        ('هل مكافأة MAX3000 تُستخدَم في أفياتور؟', 'نعم. مكافأة MAX3000 تُطبَّق على رصيد الحساب الكامل. أفياتور وCrash في Stake Originals تُسهم في متطلب الرهان بنسبة تعتمد على معدل هامش البيت الفعلي.'),
        ('هل يمكن وضع رهانين في نفس الجولة؟', 'نعم. يمكنك وضع رهانين مستقلين في جولة واحدة. رهان الأول تسحبه عند مضاعف آمن والثاني تتركه يرتفع. هذه المرونة من أبرز مميزات أفياتور.'),
    ]
    return make_generic_page(
        'aviator',
        'أفياتور Stake - لعبة Crash المثيرة مع الرمز MAX3000',
        'أفياتور في Stake.com: لعبة Crash من Spribe بمعدل RTP 97% ونظام Provably Fair. الرمز MAX3000 يفتح 200% حتى $3,000.',
        'أفياتور <bdi dir="ltr">Stake</bdi>',
        'لعبة Crash الأكثر إثارة. الرمز MAX3000 يفتح $3,000.',
        'girl-aviator-3',
        content,
        og_image='aviator.png',
        faq_items=faq
    )


def make_live_casino():
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الكازينو المباشر في <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>مزودو التاجر المباشر</h3><p>Evolution Gaming القائد الصناعي العالمي، Pragmatic Play Live، وEzugi. كلهم يوفرون تدفقاً بجودة 4K من استوديوهات احترافية في أوروبا وآسيا. مئات الطاولات تعمل في آنٍ واحد على مدار 24 ساعة.</p></div>
        <div class="club-card"><h3>بلاك جاك مباشر</h3><p>أكثر من 20 طاولة بلاك جاك مباشر متاحة في آنٍ واحد بحدود متعددة. Blackjack Party لأجواء حيوية، وطاولات VIP Blackjack لأصحاب الحدود العالية، وBlackjack Gold Series لتجربة متميزة. نفس القواعد الكلاسيكية مع تفاعل مباشر مع التاجر.</p></div>
        <div class="club-card"><h3>رولة مباشرة</h3><p>European Roulette وAmerican Roulette وFrench Roulette في بثٍّ مباشر. Lightning Roulette من Evolution تُضيف مضاعفات عشوائية على الأرقام في كل جولة تصل إلى 500x. Immersive Roulette بزوايا كاميرا متعددة.</p></div>
        <div class="club-card"><h3>ألعاب شو</h3><p>Crazy Time وMegaball وDream Catcher وMonopoly Live وGonzo's Treasure Hunt. هذه الألعاب بين الكازينو والبرنامج الترفيهي بمضاعفات هائلة وجوائز عشوائية. Crazy Time تحظى بأعلى عدد مشاهدين مباشرين في تاريخ العاب الكازينو الإلكتروني.</p></div>
        <div class="club-card"><h3>باكارا مباشر</h3><p>Baccarat Squeeze وSpeed Baccarat وNo Commission Baccarat ومتغيرات أخرى. باكارا من أقل الألعاب في هامش البيت على الرهان على Banker (1.06%). تاجر مباشر بتعليق مباشر وكشف بطيء للبطاقات.</p></div>
        <div class="club-card"><h3>بوكر مباشر مع التاجر</h3><p>Casino Hold'em وThree Card Poker وUltimate Texas Hold'em. في هذه الألعاب تلعب ضد المنزل بقواعد بوكر مع تاجر حقيقي. Mississippi Stud وPai Gow متاحان كذلك في بعض الأوقات.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أرقام الكازينو <span class="text-gradient-gold">المباشر</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">الطاولات المتزامنة</div><div class="ic-value">100+</div><div class="ic-detail">مئات الطاولات المباشرة تعمل على مدار الساعة من Evolution وPragmatic وEzugi.</div></div>
        <div class="intel-card"><div class="ic-label">جودة البث</div><div class="ic-value">4K</div><div class="ic-detail">تدفق بجودة 4K من استوديوهات احترافية. دعم HD بشكل افتراضي.</div></div>
        <div class="intel-card"><div class="ic-label">التوافر</div><div class="ic-value">24/7</div><div class="ic-detail">الطاولات المباشرة متاحة على مدار 24 ساعة 7 أيام في الأسبوع.</div></div>
        <div class="intel-card"><div class="ic-label">هامش بلاك جاك</div><div class="ic-value">0.5%</div><div class="ic-detail">بلاك جاك بالاستراتيجية المثلى من أقل الألعاب في هامش البيت في الكازينو.</div></div>
      </div>
    </div>
  </section>'''
    faq = [
        ('هل الكازينو المباشر في Stake متاح 24 ساعة؟', 'نعم. مئات الطاولات المباشرة من Evolution وPragmatic وEzugi تعمل على مدار 24 ساعة 7 أيام.'),
        ('هل يمكن استخدام مكافأة MAX3000 في الكازينو المباشر؟', 'نعم، لكن ألعاب التاجر المباشر عموماً ذات هامش بيت أقل من 4% وبالتالي تُسهم بنسبة مخفضة في متطلب رهان الـ 40x. للسرعة في الاستيفاء استخدم Stake Originals أو سلوتس هامش 4%+.'),
        ('ما هو Lightning Roulette؟', 'لعبة رولة مباشرة من Evolution Gaming تُضيف مضاعفات عشوائية تصل إلى 500x على أرقام مختارة في كل جولة. فوز على رقم مضاعَف يمنحك ما بين 50x و500x بدلاً من 35x الكلاسيكي.'),
    ]
    return make_generic_page(
        'live-casino',
        'الكازينو المباشر في Stake - تاجر حقيقي مع الرمز MAX3000',
        'الكازينو المباشر في Stake.com: بلاك جاك ورولة وباكارا مع التاجر الحقيقي بث مباشر 4K. الرمز MAX3000 يفتح 200% حتى $3,000.',
        'الكازينو المباشر في <bdi dir="ltr">Stake</bdi>',
        'تاجر حقيقي. بث 4K. الرمز MAX3000 يفتح $3,000.',
        'girl-live-casino-3',
        content,
        og_image='live-casino.png',
        faq_items=faq
    )


def make_live_odds():
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الأوتار المباشرة <span class="text-gradient-gold">في Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>الرهانات الحية والأوتار</h3><p>Stake تُقدِّم رهانات حية على آلاف الأحداث يومياً مع أوتار تتحدث في الوقت الفعلي. الرهانات الحية تسمح بالتفاعل مع تطورات المباراة: الهدف التالي، بطاقة صفراء، ضربة حرة، رهانات بديلة لا حصر لها.</p></div>
        <div class="club-card"><h3>الأوتار المُعلَّقة</h3><p>في لحظات الانتظار (ركلة جزاء، مشادة، مراجعة VAR) تُعلِّق Stake الأوتار مؤقتاً. هذا يمنع الاستفادة من المعلومات المتأخرة. بعد انتهاء الموقف تعود الأوتار مُحدَّثة.</p></div>
        <div class="club-card"><h3>Cash Out المبكر</h3><p>يمكنك إغلاق رهانك مبكراً وقبل نهاية المباراة بقيمة مُحسَّبة في الوقت الفعلي بناءً على وضع المباراة والأوتار الحالية. Cash Out الجزئي متاح أيضاً: اسحب جزءاً من الرهان وأبقِ الباقي حياً.</p></div>
        <div class="club-card"><h3>بناء الرهانات المركّبة</h3><p>ادمج أحداثاً متعددة في Parlay لتضخيم الأوتار. رهان تجميعي من 4 مباريات بأوتار 2.0 يُعطيك 16x. المُضاعِف يتحرك تلقائياً كلما أضفت رهاناً. Stake لا تفرض حداً أقصى لعدد الرهانات في الباقة.</p></div>
        <div class="club-card"><h3>سباق أسبوعي بـ 75,000 دولار</h3><p>الرهانات الرياضية تُسهم في سباق التذاكر الأسبوعي: تذكرة واحدة لكل <bdi dir="ltr">$1,000</bdi> رهان. السحب كل سبت في GMT 2 مساءً. الجائزة 75,000 دولار موزعة على الفائزين العشوائيين.</p></div>
        <div class="club-card"><h3>Stake Edge</h3><p>مصطلح Stake Edge يشير إلى هامش المنصة المُدمَج في الأوتار. مقارنةً بوسطاء التقليديين هوامش Stake تنافسية في الأحداث الكبرى. يمكنك مقارنة الأوتار عبر خدمات مقارنة الأوتار للتحقق قبل الرهان.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">الأوتار المباشرة <span class="text-gradient-gold">بالأرقام</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">الأحداث الحية يومياً</div><div class="ic-value">آلاف</div><div class="ic-detail">رهانات حية عبر كرة القدم والسلة والتنس والهوكي وeSports والمزيد.</div></div>
        <div class="intel-card"><div class="ic-label">Cash Out</div><div class="ic-value">متاح</div><div class="ic-detail">إغلاق مبكر جزئي أو كلي بقيمة سوقية مُحسَّبة في الوقت الفعلي.</div></div>
        <div class="intel-card"><div class="ic-label">مساهمة في MAX3000</div><div class="ic-value">75%</div><div class="ic-detail">الرهانات الرياضية والأوتار المباشرة تُسهم بـ 75% في متطلب رهان الـ 40x.</div></div>
        <div class="intel-card"><div class="ic-label">Parlay</div><div class="ic-value">بلا حدٍّ أقصى</div><div class="ic-detail">دمج رهانات متعددة في باقة واحدة بمضاعف تجميعي غير محدود عدداً.</div></div>
      </div>
    </div>
  </section>'''
    faq = [
        ('هل الأوتار المباشرة في Stake تنافسية؟', 'نعم، Stake تُقدِّم أوتاراً تنافسية في الأحداث الكبرى مقارنةً بمنصات الرهان التقليدية. يمكنك مقارنة الأوتار عبر خدمات متخصصة قبل الرهان.'),
        ('ما Cash Out في Stake؟', 'ميزة تُتيح إغلاق رهانك قبل نهاية المباراة بقيمة مُحسَّبة في الوقت الفعلي. Cash Out جزئي أيضاً متاح: اسحب جزءاً وأبقِ الباقي حياً.'),
        ('هل الرهانات الحية تُحسَب في مكافأة MAX3000؟', 'نعم. الرهانات الرياضية بما فيها الحية تُسهم بـ 75% في متطلب رهان الـ 40x.'),
    ]
    return make_generic_page(
        'live-odds',
        'الأوتار المباشرة في Stake - رهانات حية مع الرمز MAX3000',
        'الأوتار المباشرة في Stake.com: رهانات حية على آلاف الأحداث، Cash Out، Parlay مرن. الرمز MAX3000 يفتح 200% حتى $3,000.',
        'الأوتار المباشرة في <bdi dir="ltr">Stake</bdi>',
        'رهانات حية. Cash Out. الرمز MAX3000 يفتح $3,000.',
        'girl-lucky-drive-3',
        content,
        og_image='live-odds.png',
        faq_items=faq
    )


def make_mirror():
    faq_jsonld = '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "ما هو موقع مرآة Stake؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "مواقع المرآة لـ Stake.com هي نطاقات بديلة تحمل محتوى المنصة نفسه وتُتيح الوصول في المناطق التي تواجه قيوداً على stake.com. المواقع المُتحقَّق منها: stake.ac وstake.bet وstake.games. الرمز MAX3000 يعمل على جميع النطاقات."
      }
    },
    {
      "@type": "Question",
      "name": "هل مواقع مرآة Stake آمنة؟",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "المواقع الرسمية المُتحقَّق منها (stake.ac وstake.bet وstake.games) آمنة وتحمل نفس ترخيص كوراساو OGL/2024/1451/0918. تأكد دوماً من أنك على الموقع الرسمي وليس موقعاً تصيداً."
      }
    }
  ]
}'''
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">مواقع المرآة <span class="text-gradient-gold">الرسمية لـ Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>stake.ac</h3><p>النطاق البديل الأساسي لـ Stake.com. نفس الواجهة ونفس الألعاب ونفس الحساب. يعمل في المناطق التي تجد stake.com محجوباً. الرمز MAX3000 يعمل هنا كما يعمل في الموقع الأصلي.</p></div>
        <div class="club-card"><h3>stake.bet</h3><p>نطاق مرآة ثانٍ رسمي من Stake. يُستخدَم في مناطق معينة قد تجد stake.ac محجوباً. بيانات اعتماد الحساب نفسها تعمل عبر جميع النطاقات الرسمية.</p></div>
        <div class="club-card"><h3>stake.games</h3><p>النطاق الثالث في قائمة المرايا الرسمية المُتحقَّق منها. المحتوى متطابق والحساب موحَّد. اختر النطاق الأسرع وصولاً من موقعك الجغرافي.</p></div>
        <div class="club-card"><h3>لماذا توجد مواقع مرآة؟</h3><p>بعض مزودي الإنترنت أو الحكومات في مناطق معينة تحجب النطاق الأصلي. المرايا تُتيح استمرارية الوصول دون تغيير الخادم أو استخدام VPN. النطاقات الرسمية مُعرَّضة للتغيير أو الإضافة بمرور الوقت.</p></div>
        <div class="club-card"><h3>هل الحساب مشترك؟</h3><p>نعم. حسابك على Stake.com يعمل عبر جميع النطاقات الرسمية (stake.com وstake.ac وstake.bet وstake.games). أرصدتك وسجل رهاناتك ومستوى KYC ووضع VIP كلها متزامنة فورياً.</p></div>
        <div class="club-card"><h3>تحذير: مواقع مزيفة</h3><p>هناك مواقع تنتحل اسم Stake وليست رسمية. لا تُدخل بيانات اعتمادك إلا على النطاقات الرسمية الأربعة: stake.com وstake.ac وstake.bet وstake.games. تحقق من شريط العنوان واتصال HTTPS.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">نطاقات المرآة <span class="text-gradient-gold">الرسمية</span></h2></div>
      <table class="data-table" style="max-width:100%;overflow-x:auto;display:block;">
        <thead><tr><th>النطاق</th><th>الحالة</th><th>الرمز MAX3000</th><th>ملاحظات</th></tr></thead>
        <tbody>
          <tr class="win"><td><bdi dir="ltr">stake.com</bdi></td><td>رئيسي</td><td>يعمل</td><td>النطاق الأصلي. محجوب في بعض المناطق.</td></tr>
          <tr><td><bdi dir="ltr">stake.ac</bdi></td><td>مرآة رسمية</td><td>يعمل</td><td>البديل الأول المُتحقَّق منه.</td></tr>
          <tr><td><bdi dir="ltr">stake.bet</bdi></td><td>مرآة رسمية</td><td>يعمل</td><td>البديل الثاني المُتحقَّق منه.</td></tr>
          <tr><td><bdi dir="ltr">stake.games</bdi></td><td>مرآة رسمية</td><td>يعمل</td><td>البديل الثالث المُتحقَّق منه.</td></tr>
          <tr><td><bdi dir="ltr">stake.us</bdi></td><td>منصة منفصلة</td><td>يعمل</td><td>سويبستيكس أمريكية. ليست مرآة، بل منصة مختلفة.</td></tr>
        </tbody>
      </table>
    </div>
  </section>'''
    faq = [
        ('ما هي مواقع مرآة Stake الرسمية؟', 'المواقع المُتحقَّق منها: stake.ac وstake.bet وstake.games. الرمز MAX3000 يعمل على جميعها. الحساب موحَّد عبر جميع النطاقات.'),
        ('هل MAX3000 يعمل على مواقع المرآة؟', 'نعم. الرمز MAX3000 يعمل على stake.com وstake.ac وstake.bet وstake.games بنفس الشروط: 200% حتى $3,000، رهان 40x، KYC Level 3 مطلوب.'),
        ('ما الفرق بين stake.com وstake.us؟', 'stake.com منصة أموال حقيقية عالمية. stake.us منصة سويبستيكس أمريكية منفصلة تشغّلها Sweepsteaks Limited. ليست مرآة بل منصة مستقلة بعملة مختلفة وقواعد مختلفة.'),
    ]
    return make_generic_page(
        'mirror',
        'موقع مرآة Stake - النطاقات البديلة الرسمية مع الرمز MAX3000',
        'مواقع مرآة Stake.com الرسمية: stake.ac وstake.bet وstake.games. الرمز MAX3000 يعمل على جميعها. 200% حتى $3,000.',
        'موقع مرآة <bdi dir="ltr">Stake</bdi>',
        'النطاقات البديلة الرسمية. الرمز MAX3000 يعمل على الجميع.',
        'girl-mirror-3',
        content,
        og_image='mirror.png',
        extra_jsonld=f'<script type="application/ld+json">{faq_jsonld}</script>',
        faq_items=faq
    )


def make_news():
    content = '''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">أخبار <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Easygo Group Holdings - FY2025</h3><p>أفصحت الشركة الأم Easygo Group Holdings عن نتائج FY2025 بإيرادات A$970M وصافي ربح A$257M. تُعزِّز هذه الأرقام Stake كإحدى أسرع منصات القمار نمواً في العالم. المؤسس Ed Craven واحد من أصغر المليارديرات الأستراليين.</p></div>
        <div class="club-card"><h3>الاحتياطيات على السلسلة - أحدث لقطة</h3><p>لقطة 28 مايو 2026 من Arkham Intel تُظهر <bdi dir="ltr">$339.53M</bdi> في محافظ Stake الموسومة. Ethereum 74%، Solana 14%، Tron USDT 5%، BNB Chain 6%. Stake أحد القلائل في الصناعة الذين يُفصحون عن احتياطيات على السلسلة قابلة للتتبع.</p></div>
        <div class="club-card"><h3>Kick.com - منصة البث الشريكة</h3><p>Ed Craven