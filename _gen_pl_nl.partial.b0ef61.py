#!/usr/bin/env python3
"""
Generator for /pl/ and /nl/ locales for winnersclub.com
Produces 18 more pages each (index.html already written for pl).
"""
import os

BASE = "/home/user/workspace/winnersclub.com"
STAKE_URL = "https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000"
STAKE_US_URL = "https://stake.us/?c=MAX3000"

HREFLANG = {
    "index": "",
    "about-stake": "about-stake/",
    "aviator": "aviator/",
    "casino": "casino/",
    "live-casino": "live-casino/",
    "live-odds": "live-odds/",
    "mirror": "mirror/",
    "news": "news/",
    "originals": "originals/",
    "payments": "payments/",
    "poker": "poker/",
    "promo-code": "promo-code/",
    "reserves": "reserves/",
    "responsible-gambling": "responsible-gambling/",
    "slots": "slots/",
    "sports": "sports/",
    "stake-engine": "stake-engine/",
    "stake-us-bonus": "stake-us-bonus/",
    "vip": "vip/",
}

def hreflang_block(slug_path):
    """slug_path like '' for index, 'casino/' for casino"""
    lines = []
    for lang, code in [("en", ""), ("ko", "ko/"), ("zh-Hans", "zh/"), ("vi", "vi/"),
                       ("th", "th/"), ("ms", "ms/"), ("pt", "pt/"), ("ja", "ja/"),
                       ("es", "es/"), ("pt-BR", "pt-br/"), ("tr", "tr/"), ("id", "id/"),
                       ("fr", "fr/"), ("ru", "ru/"), ("hi", "hi/"), ("ar", "ar/"),
                       ("pl", "pl/"), ("nl", "nl/"), ("x-default", "")]:
        href = f"https://winnersclub.com/{code}{slug_path}"
        lines.append(f'  <link rel="alternate" hreflang="{lang}" href="{href}">')
    return "\n".join(lines)

def switcher_options(locale, current_path=""):
    """Generate full language switcher options"""
    opts = [
        ("https://winnersclub.com/", "English"),
        ("https://winnersclub.com/ko/", "한국어"),
        ("https://winnersclub.com/zh/", "中文"),
        ("https://winnersclub.com/vi/", "Tieng Viet"),
        ("https://winnersclub.com/th/", "Thai"),
        ("https://winnersclub.com/ms/", "Bahasa Melayu"),
        ("https://winnersclub.com/pt/", "Portugues"),
        ("https://winnersclub.com/ja/", "Japanese"),
        ("https://winnersclub.com/es/", "Espanol"),
        ("https://winnersclub.com/pt-br/", "Portugues (BR)"),
        ("https://winnersclub.com/tr/", "Turkce"),
        ("https://winnersclub.com/id/", "Bahasa Indonesia"),
        ("https://winnersclub.com/fr/", "Francais"),
        ("https://winnersclub.com/ru/", "Russian"),
        ("https://winnersclub.com/hi/", "Hindi"),
        ("https://winnersclub.com/ar/", "Arabic"),
        ("https://winnersclub.com/pl/", "PL"),
        ("https://winnersclub.com/nl/", "NL"),
    ]
    parts = []
    for url, label in opts:
        selected = ' selected' if (locale == "pl" and label == "PL") or (locale == "nl" and label == "NL") else ''
        val = '' if ((locale == "pl" and label == "PL") or (locale == "nl" and label == "NL")) else url
        parts.append(f'<option value="{val}"{selected}>{label}</option>')
    return "".join(parts)

def mobile_switcher_options():
    opts_mobile = [
        ("", "English"),
        ("/ko/", "한국어 (Korean)"),
        ("/zh/", "中文 (Chinese)"),
        ("/vi/", "Tieng Viet (Vietnamese)"),
        ("/th/", "Thai"),
        ("/ms/", "Bahasa Melayu (Malay)"),
        ("/pt/", "Portugues (Portuguese)"),
        ("/ja/", "Japanese"),
        ("/es/", "Espanol (Spanish)"),
        ("/pt-br/", "Portugues do Brasil"),
        ("/tr/", "Turkce (Turkish)"),
        ("/id/", "Bahasa Indonesia"),
        ("/fr/", "Francais (French)"),
        ("/ru/", "Russian"),
        ("/hi/", "Hindi"),
        ("/ar/", "Arabic"),
        ("/pl/", "Polski (Polish)"),
        ("/nl/", "Nederlands (Dutch)"),
    ]
    return "".join(f'<option value="{v}">{l}</option>' for v, l in opts_mobile)

def page_head(lang, canonical, title, desc, og_image="default", og_url=None):
    if og_url is None:
        og_url = f"https://winnersclub.com/{canonical}"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head><script>document.documentElement.classList.add("js-anim");</script>
  <meta charset="UTF-8"><meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"><meta http-equiv="Pragma" content="no-cache"><meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://winnersclub.com/{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{og_url}">
  <meta property="og:image" content="https://winnersclub.com/images/og/{og_image}.png">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <meta name="theme-color" content="#8b0a1a">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,500;0,600;0,700;0,800;0,900;1,500;1,600&family=JetBrains+Mono:wght@500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.min.css?v=20260616d">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-WCFWWYWP7R"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-WCFWWYWP7R', {{anonymize_ip: true}});
  </script>
  <script src="/exit-tracker.js" defer></script>'''

def schema_webpage(name, desc, url):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{name}",
  "description": "{desc}",
  "url": "{url}"
}}
</script>'''

def schema_breadcrumb(items):
    """items: list of (name, url)"""
    elements = []
    for i, (name, url) in enumerate(items, 1):
        elements.append(f'{{"@type":"ListItem","position":{i},"name":"{name}","item":"{url}"}}')
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{",".join(elements)}]
}}
</script>'''

def schema_faq(items):
    """items: list of (question, answer)"""
    qs = []
    for q, a in items:
        qs.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{",".join(qs)}]
}}
</script>'''

def org_schema():
    return '<script type="application/ld+json" data-ld="org">{"@context":"https://schema.org","@type":"Organization","name":"WinnersClub","url":"https://winnersclub.com/","logo":"https://winnersclub.com/images/favicon.svg","sameAs":["https://winnersclub.com/"],"description":"The players back room for Stake. Promo code MAX3000 unlocks a 200% match up to $3,000 with 40x wagering."}</script>'

def header_pl(current_slug=""):
    return f'''<body>
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/pl/" class="header-logo" aria-label="WinnersClub Strona glowna">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        <a href="/pl/casino/" class="nav-link">Kasyno</a>
        <a href="/pl/sports/" class="nav-link">Sport</a>
        <a href="/pl/poker/" class="nav-link">Poker</a>
        <a href="/pl/aviator/" class="nav-link">Aviator</a>
        <a href="/pl/promo-code/" class="nav-link">Kod promocyjny</a>
        <a href="/pl/reserves/" class="nav-link">Rezerwy</a>
        <a href="/pl/about-stake/" class="nav-link">O Stake</a>
      <div class="mobile-lang-block"><label>Jezyk</label><select onchange="if(this.value)window.location.href=this.value" aria-label="Jezyk">{mobile_switcher_options()}</select></div></nav>
      <div class="header-actions"><select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="Jezyk">{switcher_options("pl")}</select>
        <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup" aria-label="Dolacz">Dolacz</a>
        <button class="hamburger" id="hamburger" aria-label="Otworz menu"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>'''

def header_nl(current_slug=""):
    return f'''<body>
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/nl/" class="header-logo" aria-label="WinnersClub Startpagina">
        <img src="/images/winners-club-logo.svg" alt="WinnersClub" width="200" height="38" style="display:block;height:38px;width:auto;">
      </a>
      <nav class="header-nav" id="mainNav">
        <a href="/nl/casino/" class="nav-link">Casino</a>
        <a href="/nl/sports/" class="nav-link">Sport</a>
        <a href="/nl/poker/" class="nav-link">Poker</a>
        <a href="/nl/aviator/" class="nav-link">Aviator</a>
        <a href="/nl/promo-code/" class="nav-link">Bonuscode</a>
        <a href="/nl/reserves/" class="nav-link">Reserves</a>
        <a href="/nl/about-stake/" class="nav-link">Over Stake</a>
      <div class="mobile-lang-block"><label>Taal</label><select onchange="if(this.value)window.location.href=this.value" aria-label="Taal">{mobile_switcher_options()}</select></div></nav>
      <div class="header-actions"><select class="lang-switcher" onchange="if(this.value)window.location.href=this.value" aria-label="Taal">{switcher_options("nl")}</select>
        <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup" aria-label="Aanmelden">Aanmelden</a>
        <button class="hamburger" id="hamburger" aria-label="Menu openen"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>'''

def ticker_pl():
    return '<div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain teraz: oznaczone rezerwy $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curacao OGL/2024/1451/0918 &middot; Zrodlo: Arkham Intel via cryptotips.com &middot; Snapshot 28 maja 2026</span><span>Stake on-chain teraz: oznaczone rezerwy $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curacao OGL/2024/1451/0918 &middot; Zrodlo: Arkham Intel via cryptotips.com &middot; Snapshot 28 maja 2026</span></div></div>'

def ticker_nl():
    return '<div class="reserves-ticker"><div class="rt-inner"><span>Stake on-chain nu: getagde reserves $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curacao OGL/2024/1451/0918 &middot; Bron: Arkham Intel via cryptotips.com &middot; Snapshot 28 mei 2026</span><span>Stake on-chain nu: getagde reserves $339.53M &middot; Ethereum 74% &middot; Solana 14% &middot; Tron USDT 5% &middot; BNB Chain 6% &middot; Curacao OGL/2024/1451/0918 &middot; Bron: Arkham Intel via cryptotips.com &middot; Snapshot 28 mei 2026</span></div></div>'

def footer_pl():
    return f'''  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub"><path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/><path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text></svg>
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">KLUB JEST NA STAKE OD 2017.</p>
          <div class="footer-badges"><span class="age-badge">18+</span><span class="cert-badge">GamCare</span><span class="cert-badge">SSL</span></div>
        </div>
        <div class="footer-links-grid anim-stagger">
          <div class="footer-col"><h4>Sala gier</h4><a href="/pl/casino/">Kasyno</a><a href="/pl/sports/">Sportsbook</a><a href="/pl/poker/">Poker</a><a href="/pl/aviator/">Aviator</a><a href="/pl/live-odds/">Kursy na zywo</a></div>
          <div class="footer-col"><h4>Kod</h4><a href="/pl/promo-code/">Kod promocyjny MAX3000</a><a href="/pl/payments/">Platnosci</a><a href="/pl/mirror/">Dostep i strony lustrzane</a></div>
          <div class="footer-col"><h4>Intel</h4><a href="/pl/about-stake/">O Stake</a><a href="/pl/reserves/">Rezerwy on-chain</a></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">WinnersClub to ekskluzywny klub graczy Stake. Stake.com jest prowadzony przez Medium Rare NV na podstawie licencji Curacao OGL/2024/1451/0918. Stake.us to odrebna platforma sweepstakes prowadzona przez Sweepsteaks Limited. Ta strona ma charakter wylacznie informacyjny. Hazard niesie ryzyko. Graj odpowiedzialnie. Jesli masz problem z hazardem, skontaktuj sie z GamCare lub lokalna organizacja pomocowa. Minimum 18 lat.</p>
        <p class="footer-copyright">&copy; 2026 winnersclub.com. Wszelkie prawa zastrzezone.</p>
      </div>
    </div>
  </footer>
  <script src="/script.min.js?v=20260616a" defer></script>
  <script src="/voice.js" defer></script>
<script src="/ga-events.js" defer></script><aside class="rooms-grid" aria-label="Inne sale w klubie" style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);border:1px solid rgba(255,215,0,.12);border-radius:14px;"><h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#737378;margin:0 0 18px;font-weight:700;">Inne sale w klubie</h3><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;"><li><a href="/pl/promo-code/">Stake kod promocyjny</a></li><li><a href="/pl/casino/">Stake kasyno</a></li><li><a href="/pl/sports/">Stake sportsbook</a></li><li><a href="/pl/poker/">Stake poker</a></li><li><a href="/pl/aviator/">Stake Aviator</a></li><li><a href="/pl/reserves/">Zweryfikowane rezerwy</a></li><li><a href="/pl/about-stake/">O Stake.com</a></li><li><a href="/pl/payments/">Platnosci krypto</a></li><li><a href="/pl/mirror/">Strony lustrzane</a></li><li><a href="/pl/live-odds/">Kursy na zywo</a></li><li><a href="/pl/originals/">Stake Originals</a></li><li><a href="/pl/vip/">Program VIP</a></li><li><a href="/pl/slots/">Biblioteka slotow</a></li><li><a href="/pl/live-casino/">Kasyno na zywo</a></li></ul></aside></body>
</html>'''

def footer_nl():
    return f'''  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <svg width="160" height="38" viewBox="0 0 200 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="WinnersClub"><path d="M20 4 L34 8 L34 22 C34 30 27 36 20 38 C13 36 6 30 6 22 L6 8 Z" fill="#1a1308" stroke="#FFD700" stroke-width="1.5"/><path d="M14 14 L17 26 L20 18 L23 26 L26 14" stroke="#FFD700" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="46" y="26" font-family="'Inter',system-ui,sans-serif" font-weight="900" font-size="18" letter-spacing="0.5" fill="#FFFFFF">Winners<tspan fill="#FFD700">Club</tspan></text></svg>
          <p style="font-size:14px;font-weight:800;color:var(--text-dim);letter-spacing:2px;margin:16px 0;text-transform:uppercase;">DE CLUB IS SINDS 2017 BIJ STAKE.</p>
          <div class="footer-badges"><span class="age-badge">18+</span><span class="cert-badge">GamCare</span><span class="cert-badge">SSL</span></div>
        </div>
        <div class="footer-links-grid anim-stagger">
          <div class="footer-col"><h4>Speelzaal</h4><a href="/nl/casino/">Casino</a><a href="/nl/sports/">Sportsbook</a><a href="/nl/poker/">Poker</a><a href="/nl/aviator/">Aviator</a><a href="/nl/live-odds/">Live odds</a></div>
          <div class="footer-col"><h4>Code</h4><a href="/nl/promo-code/">Bonuscode MAX3000</a><a href="/nl/payments/">Betalingen</a><a href="/nl/mirror/">Toegang en mirrors</a></div>
          <div class="footer-col"><h4>Intel</h4><a href="/nl/about-stake/">Over Stake</a><a href="/nl/reserves/">On-chain reserves</a></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-disclaimer">WinnersClub is de exclusieve spelerclub van Stake. Stake.com wordt beheerd door Medium Rare NV onder Curacao-licentie OGL/2024/1451/0918. Stake.us is een apart sweepstakes-platform beheerd door Sweepsteaks Limited. Deze site is uitsluitend informatief. Gokken brengt risico met zich mee. Speel verantwoord. Heb je een gokprobleem, neem dan contact op met GamCare of een lokale hulporganisatie. Minimaal 18 jaar.</p>
        <p class="footer-copyright">&copy; 2026 winnersclub.com. Alle rechten voorbehouden.</p>
      </div>
    </div>
  </footer>
  <script src="/script.min.js?v=20260616a" defer></script>
  <script src="/voice.js" defer></script>
<script src="/ga-events.js" defer></script><aside class="rooms-grid" aria-label="Andere kamers in de club" style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);border:1px solid rgba(255,215,0,.12);border-radius:14px;"><h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#737378;margin:0 0 18px;font-weight:700;">Andere kamers in de club</h3><ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;"><li><a href="/nl/promo-code/">Stake bonuscode</a></li><li><a href="/nl/casino/">Stake casino</a></li><li><a href="/nl/sports/">Stake sportsbook</a></li><li><a href="/nl/poker/">Stake poker</a></li><li><a href="/nl/aviator/">Stake Aviator</a></li><li><a href="/nl/reserves/">Geverifieerde reserves</a></li><li><a href="/nl/about-stake/">Over Stake.com</a></li><li><a href="/nl/payments/">Crypto betalingen</a></li><li><a href="/nl/mirror/">Spiegelsites</a></li><li><a href="/nl/live-odds/">Live odds</a></li><li><a href="/nl/originals/">Stake Originals</a></li><li><a href="/nl/vip/">VIP-programma</a></li><li><a href="/nl/slots/">Slotbibliotheek</a></li><li><a href="/nl/live-casino/">Live casino</a></li></ul></aside></body>
</html>'''

def write_page(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    wc = len(content.split())
    print(f"  Written: {path} ({wc} words)")
    return wc

# ─────────────────────────────────────────────────────────
# POLISH PAGE BUILDERS
# ─────────────────────────────────────────────────────────

def build_pl_promo_code():
    slug = "promo-code"
    slug_path = f"{slug}/"
    bc_data = [("Strona glowna", "https://winnersclub.com/pl/"), ("Kod promocyjny", f"https://winnersclub.com/pl/{slug_path}")]
    faq_items = [
        ("Jak uzyc kodu MAX3000?", "Wejdz na stake.com przez link WinnersClub. Przy rejestracji lub w ustawieniach konta wpisz MAX3000 w polu kodu promocyjnego. Nastepnie wplac minimum $10. Skontaktuj sie z czatem na zywo i popros o aktywacje bonusu 200% do $3,000."),
        ("Kiedy bonus traci waznosc?", "Masz 30 dni od aktywacji na spelnienie warunku obrotu 40x. Warunek liczy sie od sumy depozytu i bonusu. Jesli wplates $500 i dostajesz $1,000 bonusu, warunek obrotu wynosi ($500 + $1,000) x 40 = $60,000."),
        ("Czy warunek obrotu jest trudny?", "40x liczone od sumy depozytu i bonusu to standard branzy. Bonus jest wyzszy niz wiekszosc publicznych ofert (100% do $1,000), co rekompensuje wyzszy wymog obrotu. Zaklady sportowe liczone sa jako 10-25% w zaleznosci od kursu."),
    ]
    content = page_head("pl", f"pl/{slug_path}", "Stake Kod Promocyjny MAX3000: 200% do $3,000 (Czerwiec 2026)", "Stake MAX3000: bonus 200% do $3,000, warunek obrotu 40x (depozyt i bonus), KYC poziom 3 wymagany. Zweryfikowany czerwiec 2026.", "promo-code")
    content += "\n" + schema_webpage("Stake Kod Promocyjny MAX3000: 200% do $3,000", "Stake MAX3000: 200% do $3,000, 40x obrot, KYC poziom 3. Czerwiec 2026.", f"https://winnersclub.com/pl/{slug_path}")
    content += "\n" + schema_breadcrumb(bc_data)
    content += "\n" + schema_faq(faq_items)
    content += "\n" + hreflang_block(slug_path)
    content += '\n  <script src="/lang-redirect.js" defer></script>\n'
    content += '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">\n'
    content += org_schema() + '\n'
    content += f'<script type="application/ld+json" data-ld="bc">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"}},{{"@type":"ListItem","position":2,"name":"PL","item":"https://winnersclub.com/pl/"}},{{"@type":"ListItem","position":3,"name":"Promo Code","item":"https://winnersclub.com/pl/{slug_path}"}}]}}</script>\n'
    content += '<meta name="twitter:image" content="https://winnersclub.com/images/og/promo-code.png"><meta name="twitter:card" content="summary_large_image"></head>\n'
    content += header_pl()
    content += f'''
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-promo-code-3.avif') type('image/avif'), url('/images/girl-promo-code-3.webp') type('image/webp'));background-size:cover;background-position:center;"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">Stake Kod Promocyjny <span class="code-highlight">MAX3000</span><span class="h1-sub">Kod otwierajacy skarbiec.</span></h1>
        <p class="ch-sub">Kod to <span class="code-highlight">MAX3000</span>. Zarejestruj sie, wplac od $10 do $1,500, zglosz przez czat na zywo. <strong>200% do $3,000</strong>, warunek obrotu 40x, 30 dni.</p>
        <div class="ch-actions">
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">MAX3000 &rarr;</a>
          <a href="/pl/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Szczegoly kodu</a>
        </div>
      </div>
    </div>
  </section>
  {ticker_pl()}
  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">Kod klubu</div>
        <div class="code-display">MAX3000</div>
        <div class="code-meta">200% dopasowanie &middot; Bonus do $3,000 &middot; Minimalna wplata $10 &middot; Warunek obrotu 40x (depozyt i bonus) &middot; KYC Poziom 3 wymagany &middot; 18+ nowi klienci</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAX3000">Kopiuj kod</button>
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Podaj kod dealerowi &rarr;</a>
        </div>
      </div>
    </div></section>

  <section class="section" id="calculator">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Kalkulator Bonusu <span class="text-gradient-gold">Stake.com</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Przesuwan suwak. Wplata od $10 do $1,500, dopasowanie 200% do $3,000 bonusu, warunek obrotu 40x od sumy.</p>
      </div>
      <div class="bonus-calc">
        <h3>Kwota pierwszej wplaty na Stake.com</h3>
        <div class="bonus-calc-input">
          <label for="depAmount">Kwota wplaty (USD)</label>
          <input type="range" id="depRange" min="10" max="1500" step="10" value="500">
          <input type="number" id="depAmount" min="10" max="1500" step="10" value="500">
        </div>
        <div class="bonus-calc-row">
          <div class="stat"><p class="stat-label">Bonus</p><p class="stat-value" id="bonusOut">$1,000</p><p class="stat-sub">200% do limitu $3,000</p></div>
          <div class="stat"><p class="stat-label">Wymagany obrot</p><p class="stat-value" id="wagerOut">$60,000</p><p class="stat-sub">(Depozyt + Bonus) x 40</p></div>
          <div class="stat"><p class="stat-label">Laczne saldo</p><p class="stat-value" id="totalOut">$1,500</p><p class="stat-sub">Saldo po aktywacji bonusu</p></div>
          <div class="stat"><p class="stat-label">Efektywnosc</p><p class="stat-value" id="effOut">200%</p><p class="stat-sub">Spada ponizej 200% powyzej $1,500</p></div>
        </div>
        <p class="bonus-calc-footer"><strong style="color:var(--gold);">Maksymalny bonus to $3,000.</strong> Wplac $1,500 i odbierz pelne $3,000. Wplaty powyzej $1,500 sa przetwarzane, ale bonus nie rosnie.</p>
        <a href="{STAKE_URL}" target="_blank" rel="noopener" class="bonus-calc-cta">Odbierz MAX3000 na Stake.com &rarr;</a>
      </div>
      <div class="eligibility-grid">
        <div class="item"><strong>Wiek</strong><span>18+ (w niektorych regionach 21+)</span></div>
        <div class="item"><strong>Typ klienta</strong><span>Nowy klient, tylko przy pierwszej wplacie</span></div>
        <div class="item"><strong>Minimalna wplata</strong><span>$10 lub rownowartosci w kryptowalucie</span></div>
        <div class="item"><strong>Maksymalna wplata z bonusem</strong><span>$1,500 (uzyskujesz pelne $3,000 bonusu)</span></div>
        <div class="item"><strong>Warunek obrotu</strong><span>40x (depozyt + bonus), 30 dni</span></div>
        <div class="item"><strong>KYC</strong><span>Poziom 3 wymagany przed wyplata bonusu</span></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Jak uzyc kodu <span class="text-gradient-gold">krok po kroku</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Krok 1: Rejestracja</h3><p>Przejdz na stake.com przez link WinnersClub. Kliknij "Zarejestruj sie". Wprowadz adres email, haslo, date urodzenia. Na tym etapie mozesz rowniez wpisac kod MAX3000 w polu "Kod polecenia" lub "Kod promocyjny". Potwierdz adres email, klikajac w link aktywacyjny.</p></div>
        <div class="club-card"><h3>Krok 2: Wplata</h3><p>Wplac minimum $10. Maksymalna kwota objeta bonusem to $1,500. Najlepsza metoda wplaty to kryptowaluty (BTC, ETH, USDT, BNB, TRX, XRP, SOL, DOGE i inne). Fiat dostepny przez Moonpay lub kartami bankowymi w wybranych regionach. Wplata pojawia sie na koncie w ciagu kilku minut.</p></div>
        <div class="club-card"><h3>Krok 3: Aktywacja bonusu</h3><p>Po wplacie otwierasz czat na zywo na stake.com. Napisz do supportu: "Chcę aktywowac bonus z kodem MAX3000". Support zweryfikuje twoje konto i aktywuje bonus. Bonus w wysokosci 200% od wplaconej kwoty (maks. $3,000) pojawi sie na koncie bonusowym.</p></div>
        <div class="club-card"><h3>Krok 4: Spelnienie warunku obrotu</h3><p>Masz 30 dni, zeby obrocic sume (depozyt + bonus) 40 razy. Wygrane z obrotu bonusu trafiaja najpierw na konto bonusowe. Po spelnieniu pelnego warunku saldo bonusowe zamienia sie w pieniadze dostepne do wyplaty. Sledzis postep w ustawieniach konta.</p></div>
      </div>
    </div>
  </section>

  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Pytania o <span class="text-gradient-gold">kod</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Jak uzyc kodu MAX3000?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Wejdz na stake.com przez link WinnersClub. Przy rejestracji lub w ustawieniach konta wpisz MAX3000. Nastepnie wplac minimum $10. Skontaktuj sie z czatem na zywo i popros o aktywacje bonusu 200% do $3,000.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Kiedy bonus traci waznosc?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Masz 30 dni od aktywacji na spelnienie warunku obrotu 40x. Warunek liczy sie od sumy depozytu i bonusu. Jesli wplates $500 i dostajesz $1,000 bonusu, wymagany obrot wynosi ($500 + $1,000) x 40 = $60,000.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Czy warunek obrotu jest trudny?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>40x liczone od sumy depozytu i bonusu to standard branzy. Bonus jest wyzszy niz wiekszosc ofert publicznych (100% do $1,000), co rekompensuje wyzszy wymog. Zaklady sportowe liczone sa jako 10-25% w zaleznosci od kursu.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Powiedz dealerowi, ze przysyla cie WinnersClub.</p>
    </div>
  </section>
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">Kod: <span class="code-highlight">MAX3000</span>. 200% do $3,000. Drzwi Stake.com sa otwarte</div>
    <div class="sticky-cta-actions"><a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Zajmij miejsce &rarr;</a></div>
    <button class="sticky-cta-close" aria-label="Zamknij">&times;</button>
  </div>
'''
    content += footer_pl()
    return content

def build_pl_casino():
    slug = "casino"
    slug_path = f"{slug}/"
    bc_data = [("Strona glowna", "https://winnersclub.com/pl/"), ("Kasyno", f"https://winnersclub.com/pl/{slug_path}")]
    faq_items = [
        ("Ile gier ma Stake Casino?", "Stake Casino oferuje ponad 3,000 do 4,000 slotow od ponad 15 dostawcow, 18 wlasnych Stake Originals z Provably Fair, Live Casino od Evolution Gaming oraz klasyczne gry stolowe."),
        ("Jak dzialaja Stake Originals?", "Stake Originals to gry wlasnosc platformy z systemem Provably Fair. Wlacza sie: Crash, Mines, Plinko, Dice, Keno, Limbo, Wheel i inne. Kazda gra pozwala na niezalezna weryfikacje uczciwosci wyniku."),
        ("Jakie RTP maja sloty na Stake?", "RTP poszczegolnych slotow jest dostepny w informacjach o grze. Sloty od renomowanych dostawcow jak Pragmatic Play czy NetEnt maja zazwyczaj RTP w przedziale 95-97%. Stake Originals maja oddzielnie publikowane wartosci edge."),
    ]
    content = page_head("pl", f"pl/{slug_path}", "Stake Kasyno | Ponad 4,000 Slotow, 18 Originals | MAX3000", "Kompletny przewodnik po Stake Casino: 18 Originals z Provably Fair, 3,000-4,000 slotow od 15+ dostawcow, live stoły Evolution. Kod MAX3000: 200% do $3,000.", "casino")
    content += "\n" + schema_webpage("Stake Kasyno | Ponad 4,000 Slotow, 18 Originals | MAX3000", "Kompletny przewodnik po kasynie Stake. Originals, sloty, live stoły. Kod MAX3000: 200% do $3,000.", f"https://winnersclub.com/pl/{slug_path}")
    content += "\n" + schema_breadcrumb(bc_data)
    content += "\n" + schema_faq(faq_items)
    content += "\n" + hreflang_block(slug_path)
    content += '\n  <script src="/lang-redirect.js" defer></script>\n'
    content += '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">\n'
    content += org_schema() + '\n'
    content += f'<script type="application/ld+json" data-ld="bc">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"}},{{"@type":"ListItem","position":2,"name":"PL","item":"https://winnersclub.com/pl/"}},{{"@type":"ListItem","position":3,"name":"Casino","item":"https://winnersclub.com/pl/{slug_path}"}}]}}</script>\n'
    content += '<meta name="twitter:image" content="https://winnersclub.com/images/og/casino.png"><meta name="twitter:card" content="summary_large_image"></head>\n'
    content += header_pl()
    content += f'''
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));background-size:cover;background-position:center;"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">Stake Kasyno<span class="h1-sub">Ponad 4,000 gier. Jeden kod.</span></h1>
        <p class="ch-sub">18 Stake Originals z Provably Fair, ponad 3,000 slotow, live stoły Evolution Gaming. Kod <span class="code-highlight">MAX3000</span> otwiera <strong>200% do $3,000 bonusu</strong> na start.</p>
        <div class="ch-actions">
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Wejdz do kasyna z MAX3000</a>
          <a href="/pl/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Szczegoly bonusu</a>
        </div>
      </div>
    </div>
  </section>
  {ticker_pl()}
  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Originals</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Crash</h3><p>Mnoznik startuje od 1x i rosnie. Musisz wyplacic przed krahem samolotu. Strategia: cashout na 1.5x daje dlugookresowy zwrot zblizona do RTP 99%. Mozliwe wygrane na poziomie 100x, 1000x i wyzej. Crash to najpopularniejsza gra Stake Originals z milionami gier dziennie.</p></div>
        <div class="club-card"><h3>Mines</h3><p>Plansza 5x5 z ukrytymi minami. Wybierasz liczbe min (1-24) i odkrywasz klejnoty. Kazde odkrycie klejnotu zwiekasza mnoznik. Wychodzisz kiedy chcesz lub wychodzi mina. Wyzsze ryzyko (wiecej min) to wieksze mnozniki. Provably Fair pozwala weryfikowac uklad min po grze.</p></div>
        <div class="club-card"><h3>Plinko</h3><p>Krazek spada przez pegs i laduje w przegrodce. Rozmiar planszy (8 do 16 rzedow) i ryzyko (Low, Medium, High) decyduja o rozkladzie wyplat. High risk na 16 rzedach oferuje maksymalne mnozniki. Gra oparta na rozkładzie dwumianowym.</p></div>
        <div class="club-card"><h3>Dice</h3><p>Klasyczny rzut koscia kryptograficzny. Wybierasz zakres liczb do wygrania. Szerzszy zakres to nizszy mnoznik, waski to wyzszy. House edge to 1%. Mozliwose automatycznego grania z ustawieniem stop-loss i take-profit.</p></div>
        <div class="club-card"><h3>Keno</h3><p>Wybierasz od 1 do 10 liczb na siatce 1-40. Losowane jest 20 liczb. Im wiecej trafien, tym wyzszy mnoznik. Keno Stake oferuje wariacje z roznym poziomem ryzyka i inne konfiguracje trafien.</p></div>
        <div class="club-card"><h3>Wheel</h3><p>Kolo fortuny z segmentami i roznymi mnoznikami. Wybierasz ryzyko i liczbe segmentow. Proste i szybkie. Popularne wsrod graczy preferujacych przejrzyste szanse.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Sloty i <span class="text-gradient-gold">Live Casino</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Biblioteka slotow</h3><p>Ponad 3,000 slotow od dostawcow takich jak Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming, BGaming, Nolimit City i ponad 15 innych. Filtrowac mozna po dostawcy, tematyce, RTP i zmiennosci. Nowe tytuly dodawane sa regularnie. Zakladka "Popularne" pokazuje aktualne hity wsrod graczy Stake.</p></div>
        <div class="club-card"><h3>Live Casino - Evolution Gaming</h3><p>Live stoły od Evolution Gaming: Blackjack, Roulette (European, American, Lightning), Baccarat, Poker (Casino Hold'em, Three Card Poker), Game Shows (Crazy Time, Monopoly Live, Deal or No Deal). Dealerzy na zywo z kamera, prawdziwe talie kart. Limity stalowe dostosowane do roznych budzetu.</p></div>
        <div class="club-card"><h3>RTP i uczciwosci</h3><p>RTP poszczegolnych slotow dostepne jest w opisie gry. Sloty renomowanych dostawcow maja zazwyczaj RTP 95-97%. Stake Originals maja publicznie dostepne wartosci edge. Gry zewnetrznych dostawcow sa certyfikowane przez laboratoria takie jak GLI i iTech Labs.</p></div>
      </div>
    </div>
  </section>

  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Pytania o <span class="text-gradient-gold">kasyno</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Ile gier ma Stake Casino?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Stake Casino oferuje ponad 3,000 do 4,000 slotow od ponad 15 dostawcow, 18 wlasnych Stake Originals z Provably Fair, Live Casino od Evolution Gaming oraz klasyczne gry stolowe.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Jak dzialaja Stake Originals?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Stake Originals to gry wlasne platformy z systemem Provably Fair. Obejmuja: Crash, Mines, Plinko, Dice, Keno, Limbo, Wheel i inne. Kazda gra pozwala na niezalezna weryfikacje uczciwosci wyniku po jego zakonczeniu.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Jakie RTP maja sloty na Stake?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>RTP poszczegolnych slotow jest dostepny w informacjach o grze. Sloty od renomowanych dostawcow jak Pragmatic Play czy NetEnt maja zazwyczaj RTP w przedziale 95-97%. Stake Originals maja oddzielnie publikowane wartosci edge.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Powiedz dealerowi, ze przysyla cie WinnersClub.</p>
    </div>
  </section>
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">Kod: <span class="code-highlight">MAX3000</span>. 200% do $3,000. Kasyno Stake czeka</div>
    <div class="sticky-cta-actions"><a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Wejdz do kasyna &rarr;</a></div>
    <button class="sticky-cta-close" aria-label="Zamknij">&times;</button>
  </div>
'''
    content += footer_pl()
    return content


def build_generic_pl(slug, title, desc, h1, h1sub, body_sections, faq_items, og_image="default"):
    slug_path = f"{slug}/"
    bc_data = [("Strona glowna", "https://winnersclub.com/pl/"), (h1, f"https://winnersclub.com/pl/{slug_path}")]
    content = page_head("pl", f"pl/{slug_path}", title, desc, og_image)
    content += "\n" + schema_webpage(title, desc, f"https://winnersclub.com/pl/{slug_path}")
    content += "\n" + schema_breadcrumb(bc_data)
    if faq_items:
        content += "\n" + schema_faq(faq_items)
    content += "\n" + hreflang_block(slug_path)
    content += '\n  <script src="/lang-redirect.js" defer></script>\n'
    content += '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">\n'
    content += org_schema() + '\n'
    content += f'<script type="application/ld+json" data-ld="bc">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"}},{{"@type":"ListItem","position":2,"name":"PL","item":"https://winnersclub.com/pl/"}},{{"@type":"ListItem","position":3,"name":"{h1}","item":"https://winnersclub.com/pl/{slug_path}"}}]}}</script>\n'
    content += f'<meta name="twitter:image" content="https://winnersclub.com/images/og/{og_image}.png"><meta name="twitter:card" content="summary_large_image"></head>\n'
    content += header_pl()
    content += f'''
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));background-size:cover;background-position:center;"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">{h1}<span class="h1-sub">{h1sub}</span></h1>
        <p class="ch-sub">Kod <span class="code-highlight">MAX3000</span> daje <strong>200% do $3,000 bonusu</strong> na Stake.com.</p>
        <div class="ch-actions">
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Dolacz z MAX3000</a>
          <a href="/pl/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Szczegoly bonusu</a>
        </div>
      </div>
    </div>
  </section>
  {ticker_pl()}
  {body_sections}
'''
    if faq_items:
        content += '''  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Najczesciej zadawane <span class="text-gradient-gold">pytania</span></h2></div>
      <div class="faq-list">
'''
        for q, a in faq_items:
            content += f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{q}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{a}</p></div>
        </div>
'''
        content += '''      </div>
    </div>
  </section>
'''
    content += f'''  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Powiedz dealerowi, ze przysyla cie WinnersClub.</p>
    </div>
  </section>
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">Kod: <span class="code-highlight">MAX3000</span>. 200% do $3,000. Drzwi Stake.com sa otwarte</div>
    <div class="sticky-cta-actions"><a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Zajmij miejsce &rarr;</a></div>
    <button class="sticky-cta-close" aria-label="Zamknij">&times;</button>
  </div>
'''
    content += footer_pl()
    return content


def build_generic_nl(slug, title, desc, h1, h1sub, body_sections, faq_items, og_image="default"):
    slug_path = f"{slug}/"
    bc_data = [("Startpagina", "https://winnersclub.com/nl/"), (h1, f"https://winnersclub.com/nl/{slug_path}")]
    content = page_head("nl", f"nl/{slug_path}", title, desc, og_image)
    content += "\n" + schema_webpage(title, desc, f"https://winnersclub.com/nl/{slug_path}")
    content += "\n" + schema_breadcrumb(bc_data)
    if faq_items:
        content += "\n" + schema_faq(faq_items)
    content += "\n" + hreflang_block(slug_path)
    content += '\n  <script src="/lang-redirect.js" defer></script>\n'
    content += '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap">\n'
    content += org_schema() + '\n'
    content += f'<script type="application/ld+json" data-ld="bc">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"}},{{"@type":"ListItem","position":2,"name":"NL","item":"https://winnersclub.com/nl/"}},{{"@type":"ListItem","position":3,"name":"{h1}","item":"https://winnersclub.com/nl/{slug_path}"}}]}}</script>\n'
    content += f'<meta name="twitter:image" content="https://winnersclub.com/images/og/{og_image}.png"><meta name="twitter:card" content="summary_large_image"></head>\n'
    content += header_nl()
    content += f'''
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));background-size:cover;background-position:center;"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <h1 class="ch-title text-gradient-gold">{h1}<span class="h1-sub">{h1sub}</span></h1>
        <p class="ch-sub">Code <span class="code-highlight">MAX3000</span> geeft <strong>200% bonus tot $3.000</strong> op Stake.com.</p>
        <div class="ch-actions">
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Aanmelden met MAX3000</a>
          <a href="/nl/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Bonusdetails</a>
        </div>
      </div>
    </div>
  </section>
  {ticker_nl()}
  {body_sections}
'''
    if faq_items:
        content += '''  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Veelgestelde <span class="text-gradient-gold">vragen</span></h2></div>
      <div class="faq-list">
'''
        for q, a in faq_items:
            content += f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">{q}
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>{a}</p></div>
        </div>
'''
        content += '''      </div>
    </div>
  </section>
'''
    content += f'''  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Vertel de dealer dat WinnersClub je stuurt.</p>
    </div>
  </section>
  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">Code: <span class="code-highlight">MAX3000</span>. 200% tot $3.000. De deur van Stake.com staat open</div>
    <div class="sticky-cta-actions"><a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Kies je plek &rarr;</a></div>
    <button class="sticky-cta-close" aria-label="Sluiten">&times;</button>
  </div>
'''
    content += footer_nl()
    return content


# ─────────────────────────────────────────────────────────
# BUILD ALL PL PAGES
# ─────────────────────────────────────────────────────────

def build_all_pl():
    pages = {}

    # about-stake
    pages["about-stake"] = build_generic_pl(
        "about-stake",
        "Kto prowadzi Stake | Zalozyciele, Easygo, GGR $4.7B | WinnersClub",
        "Pelne informacje o Stake.com: Ed Craven i Bijan Tehrani, historia Easygo, GGR $4.7B, rezerwy $339M, licencja Curacao. Kod MAX3000: 200% do $3,000.",
        "O Stake",
        "Kto stoi za platforma.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Historia i <span class="text-gradient-gold">zalozyciele</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">Ed Craven</div><div class="ic-value">Wspolzalozyciel</div><div class="ic-detail">Urodzony w 1995 roku w Melbourne. Poznal Bijana Tehraniego przy graniu w RuneScape. W 2017 roku wspolnie zalozyli Stake. W 2022 roku uruchomili platforme streamingowa Kick jako konkurencje dla Twitch. Wedlug Forbes szacowany majatek Ed Cravena wynosi US$3B.</div></div>
        <div class="intel-card"><div class="ic-label">Bijan Tehrani</div><div class="ic-value">Wspolzalozyciel</div><div class="ic-detail">Urodzony w Australii. Wspolzalozyciel Stake i Kick. Swietnie uzupelnia Cravena pod wzgledem technicznym i biznesowym. Lacznie z Cravenem szacowany majatek obu zalozycieli wedlug Forbes to US$5.6B w 2024 roku.</div></div>
        <div class="intel-card"><div class="ic-label">Medium Rare NV</div><div class="ic-value">Operator Stake.com</div><div class="ic-detail">Spolka zarejestrowana na Curacao, operator platformy Stake.com. Spolka macierzysta: Easygo Group Holdings. Przychody FY2025 wyniosly A$970M, zysk netto A$257M. Stake.us prowadzi odrebna spolka Sweepsteaks Limited.</div></div>
        <div class="intel-card"><div class="ic-label">Easygo Group Holdings</div><div class="ic-value">Spolka macierzysta</div><div class="ic-detail">Australijska spolka holdingowa kontrolujaca Stake.com i Kick. Wykazana w australijskim rejestrze handlowym. Przychody FY2025: A$970M. Zysk netto FY2025: A$257M. GGR Stake szacowany na $4.7B rocznie.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Liczby, ktore <span class="text-gradient-gold">nie klamia</span></h2></div>
      <div class="intel-grid">
        <div class="intel-card"><div class="ic-label">GGR</div><div class="ic-value">$4.7B</div><div class="ic-detail">Szacowany roczny Gross Gaming Revenue Stake. Plasuje platforme w scislej czolowce kasyn internetowych na swiecie.</div></div>
        <div class="intel-card"><div class="ic-label">Konta</div><div class="ic-value">21 mln</div><div class="ic-detail">Ponad 21 milionow zarejestrowanych kont na Stake.com. Silna baza graczy w Azji, Ameryce Lacinscej i Europie Wschodniej.</div></div>
        <div class="intel-card"><div class="ic-label">Rezerwy</div><div class="ic-value">$339.53M</div><div class="ic-detail">Rezerwy on-chain oznaczone przez Arkham, snapshot 28 maja 2026. Ethereum 74%, Solana 14%, stablecoiny dziewieciocyfrowe.</div></div>
        <div class="intel-card"><div class="ic-label">Licencja</div><div class="ic-value">OGL/2024/1451/0918</div><div class="ic-detail">Curacao OGL/2024/1451/0918. Obejmuje wiekszosc jurysdykcji. Osobna regulacja dla Stake.us w USA.</div></div>
      </div>
    </div>
  </section>''',
        [
            ("Kto jest wlascicielem Stake?", "Stake jest wspolwlasnoscia Eda Cravena i Bijana Tehraniego za posrednictwem Easygo Group Holdings. Stake.com prowadzi Medium Rare NV, spolka zarejestrowana na Curacao."),
            ("Jak duzy jest Stake?", "Stake generuje szacowany GGR $4.7B rocznie i ma ponad 21 milionow zarejestrowanych kont. Spolka macierzysta Easygo wykazala przychody A$970M w FY2025."),
            ("Czy Stake jest regulowany?", "Tak. Stake.com dziala na podstawie licencji Curacao OGL/2024/1451/0918, wystawionej na Medium Rare NV. Stake.us podlega odrebnym regulacjom stanow USA jako platforma sweepstakes."),
        ],
        "about-stake"
    )

    # aviator
    pages["aviator"] = build_generic_pl(
        "aviator",
        "Stake Aviator | Przewodnik po Grze Crash | MAX3000",
        "Crash gra na Stake: jak grac, strategia, RTP, kiedy wyplacac. Kod MAX3000: 200% do $3,000 bonusu na start.",
        "Stake Aviator",
        "Kiedy wyplacac, zanim samolot upadnie.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Jak dziala <span class="text-gradient-gold">Crash</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Mechanika gry</h3><p>Mnoznik startuje od 1x i rosnie w nieregularnych odstepach. Musisz kliknac "Wypłać" zanim wartosc wróci do zera ("krah"). Jesli wypłacisz przed krahem, wygrywasz zaklad pomnozony przez aktualny mnoznik. Jezeli nie zdążysz, tracisz caly zaklad. Gra jest Provably Fair, co oznacza, ze wynik mozna zweryfikowac po zakonczeniu rundy.</p></div>
        <div class="club-card"><h3>Strategia cashout na 1.5x</h3><p>Wypłata na 1.5x przy kazdej rundzie daje oczekiwany zwrot zblizona do 99% RTP. Statystycznie krah nastepuje przed 1.5x w okolo 33% rund. Dlugie serie krahow sa mozliwe, ale srednia dlugoterminowa jest faworyzujaca przy tej strategii. Nie jest to gwarancja zysku, ale najbardziej konserwatywne podejscie.</p></div>
        <div class="club-card"><h3>Podwojny zaklad</h3><p>Stake Crash pozwala na dwa rownoczesne zaklady. Mozesz postawi jeden zaklad na automatyczny cashout na 1.2x (bezpieczenstwo) i drugi na czekanie na wyzsza wartosc (ryzyko). Strategia zdywersyfikowana moze zmniejszyc wariancje przy zachowaniu szansy na duze wygrane.</p></div>
        <div class="club-card"><h3>Prowably Fair - weryfikacja</h3><p>Przed kazda runda Stake generuje hash (SHA256) wynikowego seeda serwera. Po zakonczeniu rundy mozesz sprawdzic hash, wpisujac seed serwera i client seed w weryfikatorze na stronie Stake. Jesli hash sie zgadza, wynik nie zostal zmieniony po zakladzeniu zakladu.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Statystyki i <span class="text-gradient-gold">czestotliwosc krahow</span></h2></div>
      <div class="intel-grid">
        <div class="intel-card"><div class="ic-label">House Edge</div><div class="ic-value">1%</div><div class="ic-detail">Stake Crash ma house edge 1%. Oznacza to, ze dlugookresowy zwrot dla graczy wynosi okolo 99%.</div></div>
        <div class="intel-card"><div class="ic-label">Krah przed 1.5x</div><div class="ic-value">ok. 33%</div><div class="ic-detail">Statystycznie okolo 1 na 3 rundy konczy sie krahem przed osiagnieciem 1.5x. Przy cashout na 1.5x wygrywasz w 67% rund.</div></div>
        <div class="intel-card"><div class="ic-label">Krah przed 2x</div><div class="ic-value">ok. 50%</div><div class="ic-detail">Polowa rund konczy sie krahem przed osiagnieciem 2x. Oczekiwany zwrot przy cashout na 2x wynosi rowniez okolo 99%.</div></div>
        <div class="intel-card"><div class="ic-label">Maksymalny mnoznik</div><div class="ic-value">Do 1,000,000x</div><div class="ic-detail">Teoretycznie mnoznik moze rosna nieograniczenie. Rekordowe wygrane na Stake Crash przekraczaja 1000x.</div></div>
      </div>
    </div>
  </section>''',
        [
            ("Jaka jest najlepsza strategia w Crash?", "Nie ma jednej universalnej strategii. Najnizsze ryzyko oferuje cashout na 1.2x do 1.5x. Wyzsze cashout daja wiekszy zysk przy sukces, ale krah zdaza sie statystycznie czeszciej. Kluczowe jest zarzadzanie bankrollem i ustawienie stop-loss."),
            ("Czy Crash na Stake jest fair?", "Tak. Crash jest Provably Fair. Kazda runda ma opublikowany hash SHA256 wyniku przed zakladem. Po rundzie mozna samodzielnie obliczyc wynik z dostarczonego seeda serwera i klienta."),
            ("Ile wynosi house edge w Crash?", "House edge Crash na Stake wynosi 1%. Oznacza to dlugoterminowy zwrot dla gracza na poziomie okolo 99%, co jest wyzszym RTP niz w wiekszosci tradycyjnych gier kasynowych."),
        ],
        "aviator"
    )

    # live-casino
    pages["live-casino"] = build_generic_pl(
        "live-casino",
        "Stake Live Casino | Evolution, Blackjack, Roulette | MAX3000",
        "Stake Live Casino: stoły Evolution Gaming, Lightning Roulette, Crazy Time, Blackjack na zywo. Kod MAX3000: 200% do $3,000.",
        "Stake Live Casino",
        "Prawdziwi dealerzy. Prawdziwe karty.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Live stoły <span class="text-gradient-gold">Evolution Gaming</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Blackjack na zywo</h3><p>Evolution Gaming dostarcza Stake dziesiatki stołow Blackjacka na zywo z limitami od $1 do $25,000+. Warianty: Classic Blackjack, Infinite Blackjack (nieograniczona liczba graczy przy jednym stole), Speed Blackjack (szybsze rozdanie), Free Bet Blackjack (bezplatne doublingi na 9, 10, 11). Wszystkie stoły z profesjonalnymi dealerami w studio.</p></div>
        <div class="club-card"><h3>Roulette</h3><p>Europejska (jeden zero, house edge 2.7%), Amerykanska (dwa zera, house edge 5.26%), Lightning Roulette (mnozniki do 500x na wybrane liczby), Immersive Roulette (wiele kamer z slow motion), Speed Roulette (8-sekunda runda). Lightning Roulette to jeden z najpopularniejszych tytułow Stake Live.</p></div>
        <div class="club-card"><h3>Game Shows</h3><p>Crazy Time: kolo fortuny z czterema bonusowymi rundami (Cash Hunt, Pachinko, Coin Flip, Crazy Time), mnozniki do 20,000x. Monopoly Live: prowadzony przez aktora w stroju Top Hat, rzut koscia z bonusami 3D. Deal or No Deal: symulacja teleturnieju z kaskami i ofertami brokera. Dreamcatcher: podstawowe kolo fortuny.</p></div>
        <div class="club-card"><h3>Poker i inne</h3><p>Casino Hold'em: gra z dealerem przy jednym stole, celem jest lepsza kombinacja niz dealer. Three Card Poker: szybka forma pokera z trzema kartami. Baccarat: klasyczny i Speed Baccarat. Dragon Tiger: porownanie jednej karty z dealerem. Wszystkie dostepne na Stake z dealerami na zywo przez cala dobe.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Jakie stoły live są dostepne na Stake?", "Stake oferuje szeroką gamę stołow live od Evolution Gaming: Blackjack (Classic, Infinite, Speed, Free Bet), Roulette (European, Lightning, Immersive), Game Shows (Crazy Time, Monopoly Live, Deal or No Deal), Baccarat, Poker i Dragon Tiger."),
            ("Jakie sa limity stołow live?", "Limity varuja w zaleznosci od stolu. Blackjack od $1 do $25,000+, Roulette od $0.20 do $10,000+. Stoły VIP maja wyzsze limity dostepne dla graczy o wyzszym statusie na platformie."),
        ],
        "live-casino"
    )

    # live-odds
    pages["live-odds"] = build_generic_pl(
        "live-odds",
        "Stake Live Odds | Zakłady Na Zywo | MAX3000",
        "Stake Sports live betting: kursy na zywo, cash out, zaklady in-play na ponad 60 dyscyplin sportowych. Kod MAX3000: 200% do $3,000.",
        "Stake Live Odds",
        "Zaklady w czasie rzeczywistym.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Zaklady na <span class="text-gradient-gold">zywo</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Zaklady In-Play</h3><p>Stake oferuje zaklady in-play na ponad 60 dyscyplin sportowych. Kursy aktualizowane sa w czasie rzeczywistym na podstawie przebiegu meczu. Dostepne rynki: wynik meczu, nastepny gol, handicap, over/under bramki na calkowita gre i polowe, zaklady na zawodnikow i wiele innych. Mecze na zywo ze statystykami w czasie rzeczywistym.</p></div>
        <div class="club-card"><h3>Cash Out</h3><p>Funkcja Cash Out pozwala zakonczyc zaklad przed zakonczeniem meczu. Dostepna jako Cash Out pelny (odbierasz cała kwote), Cash Out czesciowy (odbierasz czesc, reszta gra dalej) i Auto Cash Out (ustawiasz prog, system wykonuje automatycznie). Cash Out dostepny na wiekszosci rynkow live.</p></div>
        <div class="club-card"><h3>Najpopularniejsze sporty</h3><p>Pilka nozna (UEFA Champions League, Premier League, La Liga, Bundesliga, Serie A, Ekstraklasa i inne), koszykowka (NBA, Eurocup), tenis (ATP, WTA), esports (CS2, Dota 2, League of Legends, Valorant), kryket, rugby. Stake pokrywa rowniez mniej popularne dyscypliny jak dart, hokej i snooker.</p></div>
        <div class="club-card"><h3>Kursy i formaty</h3><p>Dostepne formaty kursow: dziesietny (europejski), ulamkowy (brytyjski), amerykanski (moneyline). Zmiana formatu w ustawieniach konta. Stake regularnie oferuje boosty kursow na popularne mecze. Minimum zakladu: zazwyczaj $0.01. Maksymalny zaklad zalezy od dyscypliny i rynku.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Ile dyscyplin sportowych ma Stake?", "Stake Sports obejmuje ponad 60 dyscyplin sportowych, w tym pilke nozna, koszykowke, tenis, esports, kryket, rugby, dart i hokej. Dostepne sa zarowno zaklady pre-match jak i in-play."),
            ("Czy sa zaklady na Ekstraklase?", "Tak, Stake obejmuje polskie rozgrywki, w tym PKO BP Ekstraklase. Dostepne sa zaklady pre-match i in-play na mecze Ekstraklasy w sezonie."),
            ("Jak dziala Cash Out?", "Cash Out pozwala zakonczyc zaklad przed koncem meczu. Kwota wypłaty Cash Out jest kalkulowana na podstawie aktualnych kursow i zostalego czasu. Czesc kasyn pobiera niewielka prowizje od Cash Out."),
        ],
        "live-odds"
    )

    # mirror
    pages["mirror"] = build_generic_pl(
        "mirror",
        "Stake Mirror | Adresy Alternatywne i Dostep | MAX3000",
        "Stake mirror sites: ponad 22 potwierdzone adresy alternatywne dla roznych regionow. Jak znalezc dzialajacy adres Stake. Kod MAX3000: 200% do $3,000.",
        "Stake Mirror Sites",
        "Dostep bez ograniczen regionalnych.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Czym sa <span class="text-gradient-gold">strony lustrzane</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Co to jest mirror site?</h3><p>Mirror site (strona lustrzana) to alternatywny adres URL prowadzacy do tej samej platformy. Stake utrzymuje ponad 22 potwierdzone adresy alternatywne dla roznych regionow geograficznych. Glowny adres stake.com dziala w wiekszosci krajow. Jezeli stake.com jest niedostepny w twoim regionie, mozesz sprobowac adresow alternatywnych. Zawsze sprawdz, czy adres prowadzi do oryginalnej platformy.</p></div>
        <div class="club-card"><h3>Jak znalezc aktualny mirror</h3><p>Stake regularnie aktualizuje liste adresow alternatywnych. Najlepszym sposobem jest: 1) Uzycie linku z WinnersClub (https://www.getstake.it/i/MAX3000), ktory zawsze prowadzi do dzialajacego adresu. 2) Sprawdzenie emaila od Stake (jesli jestes juz zarejestrowany). 3) Skontaktowanie sie z czatem na zywo Stake. Nie szukaj adresow na niezweryfikowanych forach.</p></div>
        <div class="club-card"><h3>Stake.us dla graczy z USA</h3><p>Gracze z USA nie moga korzystac ze Stake.com z powodu regulacji. Dla graczy z USA dostepny jest Stake.us, odrebna platforma sweepstakes prowadzona przez Sweepsteaks Limited. Stake.us dziala legalnie w 37 stanach USA. Kod MAX3000 odblokowuje 560K Gold Coins i 56 Stake Cash przy rejestracji na Stake.us.</p></div>
        <div class="club-card"><h3>Bezpieczne korzystanie z mirror</h3><p>Uzyj tylko zweryfikowanych adresow od Stake. Sprawdz certyfikat SSL (zamknieta kłodka w przegladarce). Nie loguj sie na stronach, ktore nie maja certyfikatu SSL lub wyglada podejrzanie. Fałszywe strony to poważne zagrożenie - prowadza do kradziezy danych logowania.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Dlaczego Stake.com jest niedostepny?", "Stake stosuje wlasne ograniczenia geograficzne w niektorych jurysdykcjach, niezaleznie od tego, czy dana jurysdykcja reguluje hazard. W takich przypadkach mozna sprobowac uzyc VPN lub poszukac dostepnego adresu alternatywnego."),
            ("Czy VPN jest dozwolony na Stake?", "Stake generalnie nie zaleca korzystania z VPN w celu obejscia blokad geograficznych. Konto moze zostac zawieszone za naruszenie warunkow korzystania z uslugi, jesli Stake stwierdzi, ze uzywasz VPN do dostepu z zablokowanego regionu."),
        ],
        "mirror"
    )

    # news
    pages["news"] = build_generic_pl(
        "news",
        "Stake Aktualnosci | Nowosci Platformy i Sportowe | WinnersClub",
        "Aktualne wiadomosci ze Stake.com: nowe gry, promocje, wyniki sportowe, aktualnosci platformy. Kod MAX3000: 200% do $3,000.",
        "Stake Aktualnosci",
        "Najnowsze ze swiata Stake.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Co nowego na <span class="text-gradient-gold">Stake</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Nowe gry i dostawcy (2026)</h3><p>Stake regularnie dodaje nowe sloty i gry od uznanych dostawcow. W 2026 roku do biblioteki dolaczyli dostawcy z naciskiem na high-volatility sloty i live casino. Hacksaw Gaming, Nolimit City i Relax Gaming to dostawcy, ktorzy systematycznie dodaja nowe tytuly. Stake Originals takze regularnie otrzymuja aktualizacje i nowe warianty.</p></div>
        <div class="club-card"><h3>Turnieje i promocje</h3><p>Stake organizuje regularne turnieje z pulami nagrod. Tygodniowe Challenges pozwalaja zdobyc dodatek Stake Cash. Daily Races to codzienne wyniki z nagrodami do $75,000. Slot Races z dedykowanymi pulami dla wybranych slotow. Weekly Raffles do ktore mozna zdobyc bilety grajac. Szczegoly biezacych promocji dostepne na stronie Promotions w aplikacji Stake.</p></div>
        <div class="club-card"><h3>Aktualnosci sportowe</h3><p>Stake Sports Betting pokrywa biezace sezony Ekstraklasy, Ligi Mistrzow UEFA, Premier League, La Liga i innych. Stake dostosowuje oferte zakladow do aktualnego kalendarza rozgrywek. Boosted odds na kluczowe mecze pojawiaja sie regularnie w zakladce Sports na stronie glownej.</p></div>
        <div class="club-card"><h3>Aktualizacje platformy</h3><p>Stake.com w 2026 roku wprowadzil szereg usprawnien interfejsu uzytkownika, szybsze przetwarzanie transakcji kryptowalutowych i rozszerzone opcje platnosci. Aplikacja mobilna na iOS i Androida jest regularnie aktualizowana. Czat spolecznosciowy w grach jest aktywny przez cala dobe z moderatorami.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Jak sledzie aktualnosci Stake?", "Aktualnosci Stake mozna sledzic przez sekcje Promotions na stronie, czat spolecznosciowy, lub newslettera Stake. WinnersClub.com takze publikuje wazne aktualnosci zwiazane z platforma."),
            ("Czy Stake ma program VIP?", "Tak. Program VIP Stake oferuje rakeback, bonusy urodzinowe, boosted withdrawals i dedykowanego menadzera VIP. Wiecej szczegolow na stronie VIP WinnersClub."),
        ],
        "news"
    )

    # originals
    pages["originals"] = build_generic_pl(
        "originals",
        "Stake Originals | Provably Fair | Crash, Mines, Plinko | MAX3000",
        "Wszystkie Stake Originals z Provably Fair: Crash, Mines, Plinko, Dice, Keno, Limbo, Wheel i inne. Przewodnik, house edge, strategie. Kod MAX3000: 200% do $3,000.",
        "Stake Originals",
        "18 gier. Kazda weryfikowalna.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Wszystkie <span class="text-gradient-gold">Stake Originals</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Crash, Mines, Plinko</h3><p>Crash: mnoznik rosnie do momentu krachu, trzeba wyplacic w odpowiednim momencie. House edge 1%, RTP ok. 99%. Mines: plansza 5x5, wybierasz klejnoty i unikasz min, mnoznik rosnie przy kazdym klejnocie. Plinko: krazek spada przez pegs, rozne konfiguracje ryzyka, nawiazanie do klasycznej gry telewizyjnej.</p></div>
        <div class="club-card"><h3>Dice, Keno, Limbo</h3><p>Dice: wybierasz zakres liczbowy, rzut generuje wynik w zakresie 0-99.99. House edge 1%. Keno: wybierasz od 1 do 10 liczb z siatki 1-40, losowanych jest 20 liczb, wygrana zalezi od trafien. Limbo: ustawiasz mnoznik docelowy, gra losuje wynik, wygrywasz jesli losowy mnoznik jest rowny lub wiekszy od twojego celu.</p></div>
        <div class="club-card"><h3>Wheel, Diamond Poker, Blackjack</h3><p>Wheel: kolo fortuny z segmentami o roznych mnoznikach, proste i szybkie. Diamond Poker: uproszczona forma pokera z 7 kartami. Blackjack Originals: wariant blackjacka z Provably Fair, klasyczne zasady 21. Hilo: obstawiasz, czy nastepna karta bedzie wyzsza czy nizsza, mnoznik akumuluje sie z kazdym trafionym zakladem.</p></div>
        <div class="club-card"><h3>Baccarat, Video Poker, Slide</h3><p>Baccarat Originals: Gracz kontra Banker, prost zasady, house edge 1%. Video Poker: klasyczne Jacks or Better z Provably Fair. Slide: wersja Crash ze znormalizowanym rozkladem - mniej krahow ponizej 1x, ale ograniczone maksymalne mnozniki. Blue Samurai: japonskoinspirowna gra z mnoznikami.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">System <span class="text-gradient-gold">Provably Fair</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Jak weryfikowac wynik</h3><p>Kazda gra Stake Originals generuje seed serwera (hash SHA256 jest publikowany przed runda). Gracz moze ustawic wlasny client seed. Po rundzie serwer ujawnia oryginalny seed. Uzywajac opublikowanego algorytmu na stronie Stake, kazdy moze samodzielnie obliczyc wynik i potwierdzic, ze nie zostal zmanipulowany.</p></div>
        <div class="club-card"><h3>Weryfikacja on-site</h3><p>Stake ma wbudowany weryfikator na stronie Fairness. Wystarczy wkleic server seed, client seed i nonce z historii gry. Weryfikator pokazuje czy wynik jest zgodny z obliczonym przez algorytm. Mozna tez uzyc zewnetrznych kalkulatorow open-source dostepnych na GitHub.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Czym sa Stake Originals?", "Stake Originals to wlasne gry platformy Stake z systemem Provably Fair. Obejmuja Crash, Mines, Plinko, Dice, Keno, Limbo, Wheel, Baccarat, Blackjack i inne. Kazda gra pozwala na niezalezna weryfikacje uczciwosci wyniku."),
            ("Jaki jest house edge Stake Originals?", "Wiekszosc Stake Originals ma house edge 1%, co przekłada sie na RTP okolo 99%. To wyzszy zwrot niz wiekszosc tradycyjnych gier kasynowych i slotow."),
            ("Czy moge zmieniac client seed?", "Tak. Mozesz zmienic client seed w dowolnym momencie. Zmiana seeda generuje nowa serie wynikow dla kolejnych rund. Aktualny server seed (w postaci hasha) jest zawsze pokazywany przed runda."),
        ],
        "originals"
    )

    # payments
    pages["payments"] = build_generic_pl(
        "payments",
        "Stake Platnosci | Kryptowaluty, Fiat, Wyplaty | MAX3000",
        "Metody platnosci Stake: BTC, ETH, USDT, DOGE, TRX, XRP, SOL, BNB i inne. Czas wyplat, limity, MoonPay fiat. Kod MAX3000: 200% do $3,000.",
        "Stake Platnosci",
        "Kryptowaluty i fiat. Szybko.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Dostepne <span class="text-gradient-gold">metody platnosci</span></h2></div>
      <div class="intel-grid">
        <div class="intel-card"><div class="ic-label">Bitcoin (BTC)</div><div class="ic-value">Glowna kryptowaluta</div><div class="ic-detail">Wplaty potwierdzane po 1 bloku (ok. 10 min). Wyplaty: 30-60 min. Brak opłat po stronie Stake, opłata sieciowa pobierana z kwoty transakcji.</div></div>
        <div class="intel-card"><div class="ic-label">Ethereum (ETH)</div><div class="ic-value">i tokeny ERC-20</div><div class="ic-detail">ETH, USDT (ERC-20), USDC dostepne. Wplaty: 12 potwierdzen (ok. 3-5 min). Wyplaty: 30-60 min. Gaz pobierany z kwoty transakcji.</div></div>
        <div class="intel-card"><div class="ic-label">Szybkie sieci</div><div class="ic-value">TRX, XRP, SOL</div><div class="ic-detail">Tron (TRX, USDT TRC-20), Ripple (XRP), Solana (SOL). Rozliczenia w sekundach do 1 minuty. Minimalne oplaty sieciowe. Idealne do malych i srednich transakcji.</div></div>
        <div class="intel-card"><div class="ic-label">Inne</div><div class="ic-value">BNB, DOGE, LTC i inne</div><div class="ic-detail">BNB (BEP-20), Dogecoin, Litecoin rowniez dostepne. Pełna lista walut w sekcji Wallet na Stake.com.</div></div>
        <div class="intel-card"><div class="ic-label">MoonPay (fiat)</div><div class="ic-value">Karta / bank</div><div class="ic-detail">Zakup kryptowalut kartą lub przelewem bankowym przez MoonPay. Opłata 1-4% po stronie MoonPay. Dostepnosc zalezna od kraju. Standardowy czas dostarczenia: 1-5 dni roboczych.</div></div>
        <div class="intel-card"><div class="ic-label">Wyplaty</div><div class="ic-value">30 min do 5 dni</div><div class="ic-detail">Krypto: 30-60 min normalnie. Duze kwoty (zazwyczaj powyzej $10,000): 2-4 dni robocze compliance. MoonPay fiat: 1-5 dni roboczych.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">KYC i <span class="text-gradient-gold">weryfikacja</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>KYC Poziom 1</h3><p>Wymagany przy rejestracji: adres email i potwierdzenie wieku (18+). Pozwala na depozyt i gre bez wyplatm az do określonego limitu.</p></div>
        <div class="club-card"><h3>KYC Poziom 2</h3><p>Numer telefonu i kraj zamieszkania. Odblokowuje wyzsze limity transakcji i dostep do niektorych bonusow.</p></div>
        <div class="club-card"><h3>KYC Poziom 3</h3><p>Dokument tozsamosci (paszport lub dowod osobisty) i dowod adresu zamieszkania. Wymagany do odblokowania bonusu MAX3000 i do wyplat powyzej okreslonych limitow. Zazwyczaj weryfikacja trwa od kilku godzin do 2 dni roboczych.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Jakie kryptowaluty sa dostepne na Stake?", "Stake przyjmuje BTC, ETH, USDT (ERC-20 i TRC-20), USDC, TRX, XRP, SOL, BNB, DOGE, LTC i inne. Pełna lista dostepna w sekcji Wallet na Stake.com."),
            ("Jak szybkie sa wyplaty kryptowalut?", "Standardowe wyplaty kryptowalut realizowane sa w ciagu 30 do 60 minut. TRX, XRP i SOL rozliczane sa w sekundach. Kwoty powyzej $10,000 moga wymagac 2 do 4 dni roboczych weryfikacji compliance."),
            ("Czy moge wplacic w PLN?", "Bezposredni depozyt w PLN nie jest dostepny. Mozesz zakupic kryptowaluty za PLN przez zewnetrzne giełdy lub przez MoonPay kartą kredytową/debetowa. Nastepnie wyslij kryptowalute na adres depozytowy Stake."),
        ],
        "payments"
    )

    # poker
    pages["poker"] = build_generic_pl(
        "poker",
        "Stake Poker | Video Poker, Casino Hold'em | MAX3000",
        "Stake Poker: Video Poker z Provably Fair, Casino Hold'em, Three Card Poker. Zasady, strategie, RTP. Kod MAX3000: 200% do $3,000.",
        "Stake Poker",
        "Blef, kalkulacja, przewaga.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Formy pokera <span class="text-gradient-gold">na Stake</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Video Poker - Provably Fair</h3><p>Stake Originals Video Poker oparty jest na Jacks or Better z systemem Provably Fair. Wygrywasz przy parze dziatek lub wyzszej kombinacji. Strategia optymalna daje RTP okolo 99.54% w klasycznym Jacks or Better. Inne warianty: Double Down Stud, Deuces Wild. Automatyczna gra z ustawionym stop-loss i take-profit.</p></div>
        <div class="club-card"><h3>Casino Hold'em (Live)</h3><p>Evolution Gaming Casino Hold'em: gra jeden-na-jeden z dealerem. Obaj dostajecie dwie karty, siec spoleczna to 5 kart wspólnych. Cel: lepsza kombinacja niz dealer z 7 kart. Mozliwosc zakladu AA+ Bonus (wypłaca przy parze asow lub lepszej w pierwszych 5 kartach). House edge dla optymalnej strategii: ok. 2.16%.</p></div>
        <div class="club-card"><h3>Three Card Poker (Live)</h3><p>Tylko 3 karty. Grasz przeciwko dealerowi. Dwie mozliwosci: obstawic tylko Ante (gra z dealerem) lub dodac Pair Plus (zakład niezalezny na pare lub lepsza). Dealer kwalifikuje sie przy krolowej lub wyzszej. Pair Plus wyplaca niezaleznie od tego, czy dealer sie kwalifikuje. House edge: ok. 2.3% przy optymalnej grze.</p></div>
        <div class="club-card"><h3>Strategia podstawowa - Jacks or Better</h3><p>Trzymaj: Roj Krolewski, Poker, Full, Kolor, Strit, Trojka, Dwie pary, Para J/Q/K/A. Szukaj: Czwórka do Roju, Czwórka do Koloru (z asem), Trzy do Roju Krolewskiego. Discarduj: pare 2-10 jesli masz 4 do Roju Krolewskiego lub Strita. Nigdy nie roz para, chyba ze masz 4 do Roju Krolewskiego.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Czy na Stake sa turnieje pokerowe?", "Stake.com nie oferuje tradycyjnych turniejow Texas Hold'em z innymi graczami. Dostepne sa formy gry jeden na jeden z dealerem (Casino Hold'em, Three Card Poker) oraz Video Poker z Provably Fair."),
            ("Jaki jest RTP Video Pokera na Stake?", "Jacks or Better na Stake Originals ma RTP okolo 99.54% przy optymalnej strategii. To jeden z wyzszych RTP wsrod gier kasynowych."),
        ],
        "poker"
    )

    # reserves
    pages["reserves"] = build_generic_pl(
        "reserves",
        "Stake Rezerwy On-Chain | $339.53M Zweryfikowane | WinnersClub",
        "Stake rezerwy on-chain: $339.53M w portfelach oznaczonych przez Arkham (28 maja 2026). Ethereum 74%, Solana 14%. Jak weryfikowac. Kod MAX3000: 200% do $3,000.",
        "Stake Rezerwy On-Chain",
        "339 milionow. Publicznie widoczne.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Snapshot <span class="text-gradient-gold">28 maja 2026</span></h2></div>
      <div class="intel-grid">
        <div class="intel-card"><div class="ic-label">Rezerwy lacznie</div><div class="ic-value">$339.53M</div><div class="ic-detail">Wartosc w USD wedlug cen z 28 maja 2026. Portfele oznaczone przez Arkham Intel jako należace do Stake.</div></div>
        <div class="intel-card"><div class="ic-label">Ethereum</div><div class="ic-value">74%</div><div class="ic-detail">ETH i tokeny ERC-20 stanowia 74% rezerw. Największa pozycja w portfelu.</div></div>
        <div class="intel-card"><div class="ic-label">Solana</div><div class="ic-value">14%</div><div class="ic-detail">SOL i tokeny SPL stanowia 14% rezerw. Silna ekspozycja na ekosystem Solana.</div></div>
        <div class="intel-card"><div class="ic-label">BNB Chain</div><div class="ic-value">6%</div><div class="ic-detail">BNB i tokeny BEP-20 stanowia 6% rezerw. Uzywane glownie do płatności BNB Chain.</div></div>
        <div class="intel-card"><div class="ic-label">Tron USDT</div><div class="ic-value">5%</div><div class="ic-detail">USDT TRC-20 stanowi 5% rezerw. Dziewieciocyfrowe salda stablecoinow na Tron.</div></div>
        <div class="intel-card"><div class="ic-label">Inne</div><div class="ic-value">1%</div><div class="ic-detail">Pozostałe kryptowaluty, w tym BTC, DOGE, LTC i inne w mniejszych pozycjach.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Jak samodzielnie <span class="text-gradient-gold">zweryfikowac</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Arkham Intelligence</h3><p>Arkham Intel to platforma do analizy on-chain, ktora taguje portfele należace do znanych podmiotów, w tym Stake. Wejdz na platform.arkhamintelligence.com i wyszukaj "Stake" w zakladce Entities. Zobaczysz wszystkie portfele przypisane do Stake z historią transakcji i biezacym saldem.</p></div>
        <div class="club-card"><h3>cryptotips.com</h3><p>cryptotips.com agreguje dane Arkham i regularnie aktualizuje raport rezerw Stake. To najszybszy sposob na sprawdzenie biezacych rezerw bez koniecznosci konfiguracji konta na Arkham. Dane sa odswiezane cotygodniowo i zawieraja historyczny wykres rezerw.</p></div>
        <div class="club-card"><h3>Bezposrednia weryfikacja</h3><p>Mając adresy portfeli Stake (dostepne przez Arkham), mozna je bezposrednio sprawdzic na eksplorerach blockchain: Etherscan.io dla ETH, Solscan.io dla SOL, bscscan.com dla BNB Chain, tronscan.org dla TRX. Kazdy adres jest publicznie widoczny bez potrzeby logowania.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Skad pochodza dane o rezerwach?", "Dane o rezerwach Stake pochodza z platformy Arkham Intelligence, ktora taguje portfele blockchain należace do Stake. Biezace dane mozna sprawdzic takze na cryptotips.com. Snapshot z 28 maja 2026 pokazal $339.53M."),
            ("Czy rezerwy pokrywaja zobowiazania wobec graczy?", "Dane o rezerwach on-chain pokazuja salda portfeli Stake, ale Stake nie publikuje pełnego raportu o aktywach i zobowiazaniach (tzw. proof of liabilities). Mozemy potwierdzic, ze rezerwy sa substantialne i publicznie weryfikowalne."),
            ("Jak czesto aktualizowane sa rezerwy?", "Blockchain jest aktualizowany w czasie rzeczywistym. Agregatory takie jak cryptotips.com i Arkham pokazuja biezace salda. WinnersClub publikuje cotygodniowe snapshoty dla historycznego porownania."),
        ],
        "reserves"
    )

    # responsible-gambling
    pages["responsible-gambling"] = build_generic_pl(
        "responsible-gambling",
        "Odpowiedzialny Hazard na Stake | Narzedzia i Pomoc | WinnersClub",
        "Odpowiedzialny hazard na Stake.com: limity depozytu, samowykluczenie, przerwy w grze. Organizacje pomocowe. Hazard powinien byc rozrywka.",
        "Odpowiedzialny Hazard",
        "Graj madrzej. Graj bezpieczniej.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Narzedzia <span class="text-gradient-gold">odpowiedzialnej gry</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Limity depozytu</h3><p>Stake umozliwia ustawienie dziennych, tygodniowych i miesiecznych limitow depozytu. Po ustawieniu limitu nie mozna go zwiekszyc natychmiast - obowiazuje 24-72 godzinny okres oczekiwania. Limit zmniejsza sie natychmiast. Mozesz go znalezc w ustawieniach konta pod zakładka Responsible Gambling.</p></div>
        <div class="club-card"><h3>Przerwa w grze</h3><p>Mozesz ustawic przerwe w grze (cooling-off period) na 24 godziny, 7 dni lub 30 dni. Podczas przerwy nie mozna logowac sie na konto ani dokonywac wplat. Przerwa nie moze byc anulowana przed uplywem wybranego okresu.</p></div>
        <div class="club-card"><h3>Samowykluczenie</h3><p>Samowykluczenie (self-exclusion) to trwala lub dlugookresowa blokada konta. Mozna wybrac okres od 6 miesiecy do 5 lat lub trwale. W czasie samowykluczenia konto jest zablokowane i nie mozna sie zalogowac. Skontaktuj sie z supportem Stake, aby zainicjowac samowykluczenie.</p></div>
        <div class="club-card"><h3>Limit sesji i straty</h3><p>Limit straty pozwala ustawic maksymalna kwote, ktora mozesz stracic w danym okresie. Limit sesji ogranicza czas jednorazowej sesji gry. Po przekroczeniu limitu system automatycznie konczy sesje lub blokuje dalsze zaklady.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Pomoc i <span class="text-gradient-gold">organizacje wsparcia</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>GamCare</h3><p>GamCare oferuje wsparcie, porady i pomoc dla osob z problemem hazardowym. Telefon zaufania: 0808 8020 133 (UK, bezpłatny). Chat online: gamcare.org.uk. Dostepne rowniez wsparcie dla rodzin i bliskich osób z problemem hazardowym.</p></div>
        <div class="club-card"><h3>Goraca Linia dla Graczy w Polsce</h3><p>W Polsce dziala Telefoniczne Centrum Wsparcia dla uzaleznionych od hazardu: 801 889 880. Urzad ds. Gier Hazardowych (KSAL) prowadzi liste miejsc pomocy. Anonimowi Hazardzisci (AH) rowniez dzialaja w Polsce z regularnymi spotkaniami grupowymi.</p></div>
        <div class="club-card"><h3>Recognize the Signs</h3><p>Oznaki problemu z hazardem: gra za wiecej niz mozesz stracic, pozkyczanie pieniedzy na hazard, zaniedbywanie obowiazków, ukrywanie gry, nerwowość bez hazardu, powracanie do hazardu zeby odgrac straty. Jesli rozpoznajesz te objawy u siebie lub kogoś bliskiego, szukaj pomocy.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Jak ustawic limit depozytu na Stake?", "Wejdz w ustawienia konta na Stake.com, zakładka Responsible Gambling. Znajdziesz tam opcje ustawienia dziennych, tygodniowych i miesiecznych limitow depozytu, limitow straty i przerw w grze."),
            ("Co robic, jesli hazard staje sie problemem?", "Skontaktuj sie z GamCare (gamcare.org.uk) lub polskim Telefonicznym Centrum Wsparcia (801 889 880). Na Stake.com mozesz natychmiast ustawic przerwe lub samowykluczenie przez ustawienia konta lub kontakt z supportem."),
        ],
        "responsible-gambling"
    )

    # slots
    pages["slots"] = build_generic_pl(
        "slots",
        "Stake Sloty | Ponad 3,000 Gier, Pragmatic, NetEnt | MAX3000",
        "Biblioteka slotow Stake: ponad 3,000 tytułow od Pragmatic Play, NetEnt, Play'n GO, Hacksaw, BGaming. Filtrowanie po RTP, dostawcy, zmiennosci. Kod MAX3000: 200% do $3,000.",
        "Stake Biblioteka Slotow",
        "Trzy tysiace okien. Jedno wejscie.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Dostawcy i <span class="text-gradient-gold">popularne sloty</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Pragmatic Play</h3><p>Jeden z najwiekszych dostawcow na Stake. Popularne tytuly: Gates of Olympus (RTP 96.5%, zmiennosc wysoka, maks. wygrana 5,000x), Sweet Bonanza (96.51%, megaways z cukierkami, maks. 21,100x), Big Bass Bonanza (96.71%, rybacy z funkcja Buy Bonus), Starlight Princess (96.5%, anime styl z high volatility). Pragmatic regularnie wydaje nowe tytuly dodawane do Stake.</p></div>
        <div class="club-card"><h3>Hacksaw Gaming i Nolimit City</h3><p>Hacksaw Gaming specjalizuje sie w high-volatility slotach: Wanted Dead or a Wild (maks. 12,500x), Chaos Crew 2. Nolimit City: xWays Hoarder (maks. 21,175x), San Quentin (24,000x), Evil Goblins (72,500x). Oba dostawcy to czolowka jesli chodzi o ekstremalne maxwiny. Dostepni na Stake z pelna biblioteka tytułow.</p></div>
        <div class="club-card"><h3>NetEnt i Play'n GO</h3><p>NetEnt: Book of Dead (96.21%, egipt, high-vol), Starburst (96.09%, klasyczny, low-vol), Dead or Alive 2 (96.8%, western, maks 100,000x). Play'n GO: Reactoonz (96.51%), Moon Princess (96.51%), Book of Dead. Obie firmy to legendy branzy z dluga historia certyfikowanych RTP.</p></div>
        <div class="club-card"><h3>BGaming i inne</h3><p>BGaming: Book of Cats (96.54%), Joker Queen. Relax Gaming: Money Train 2 (96.4%, maks. 50,000x), Money Train 3 (maks. 100,000x). Elk Studios: Nitropolis 3. Push Gaming: Jammin' Jars 2 (maks. 20,000x). Ponad 15 dostawcow w sumie dostepnych na Stake z ponad 3,000 tytułami.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">RTP, zmiennosc i <span class="text-gradient-gold">jak wybrac slot</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Return to Player (RTP)</h3><p>RTP to procentowy zwrot do gracza w dlugim okresie. Slot z RTP 96% zwraca srednie $96 na kazde $100 zakładow (w milionach obrotow). Wyzszy RTP jest korzystniejszy dla gracza. Sprawdz RTP w opisie gry lub w dokumentacji dostawcy.</p></div>
        <div class="club-card"><h3>Zmiennosc (Volatility)</h3><p>Niska zmiennosc: czeste male wygrane, wolno wyczerpuje bankroll, niskie maksymalne wygrane. Wysoka zmiennosc: rzadkie wygrane, duze skoki, maks. wygrane siegajace tysiecy x zakladu. Dobierz zmiennosc do swojego stylu i wielkosci bankrollu.</p></div>
        <div class="club-card"><h3>Buy Bonus (Feature Buy)</h3><p>Wiele slotow Pragmatic i Hacksaw oferuje mozliwosc kupienia rundy bonusowej bezposrednio. Koszt: zazwyczaj 50x do 200x stawki bazowej. Kupiony bonus ma czesto wyzsze RTP w rundzie bonusowej. Stake obsluguje Feature Buy tam, gdzie jest dostepny.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Ile slotow ma Stake?", "Stake oferuje ponad 3,000 do 4,000 slotow od ponad 15 dostawcow, w tym Pragmatic Play, NetEnt, Play'n GO, Hacksaw Gaming, BGaming, Nolimit City, Relax Gaming i innych."),
            ("Jakie sloty maja najwyzsza maks. wygrana?", "Sloty z najwyzszymi maksymalnymi wygranymi na Stake: Evil Goblins xWays (72,500x), San Quentin (24,000x), Money Train 3 (100,000x), xWays Hoarder (21,175x). Sprawdz szczegoly w grze."),
            ("Czy moge filtrowac sloty po RTP?", "Tak. Stake oferuje filtry po dostawcy, tematyce i RTP. Mozesz wybrac sloty z RTP powyzej 96% przez filtry w zakładce Slots lub Casino na stronie Stake."),
        ],
        "slots"
    )

    # sports
    pages["sports"] = build_generic_pl(
        "sports",
        "Stake Sports | Zaklady Sportowe, 60+ Dyscyplin | MAX3000",
        "Stake Sports Betting: pilka nozna, koszykowka, tenis, esports. Zaklady live, cash out, boosted odds. Kod MAX3000: 200% do $3,000 na start.",
        "Stake Sportsbook",
        "Ponad 60 dyscyplin. Kursy w czasie rzeczywistym.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Sport i <span class="text-gradient-gold">rynki zakladow</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Pilka nozna</h3><p>Stake pokrywa wszystkie najwazniejsze ligi europejskie: Premier League, La Liga, Bundesliga, Serie A, Ligue 1, a takze PKO BP Ekstraklase, rozgrywki UEFA (Champions League, Europa League, Conference League) i reprezentacje narodowe. Rynki: 1X2, handicap, over/under bramki na polowe i pelny mecz, obstawianie zawodnikow (scorerzy, asyty, kartki), specjalne rynki na mecze.</p></div>
        <div class="club-card"><h3>Koszykowka i tenis</h3><p>NBA, EuroLeague, ACB dostepne cały sezon z zakladami pre-match i live. Rynki: wynik, over/under punktow, handicap (spread), wyniki polowek i kwartalow, zaklady na zawodnikow (punkty, zbiorki, asysty). Tenis: ATP, WTA, Challengers. Zaklady na gemy, sety, break pointy. Live betting z aktualizowanymi kursami w czasie rzeczywistym.</p></div>
        <div class="club-card"><h3>Esports</h3><p>Counter-Strike 2, Dota 2, League of Legends, Valorant, Overwatch 2 dostepne na Stake. Rynki: wynik meczu, wynik mapowy, handicap na mapy, totale rund/zabojstw. Stake jest jednym z wiodacych bukmacherow esportowych ze wzgledu na szerokosc oferty i ciagle aktualizowane kursy dla turniejow tier-1.</p></div>
        <div class="club-card"><h3>Inne dyscypliny</h3><p>Kryket (IPL, Big Bash, Test matches), rugby (rugby union, rugby league), hokej (NHL, KHL), dart (PDC Premier League, World Championship), snooker (World Snooker Championship), baseball (MLB). Ponad 60 dyscyplin lacznie z mozliwoscia zakladow pre-match i live na wiekszosci z nich.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Czy Stake oferuje zaklady na Ekstraklase?", "Tak. Stake Sports obejmuje PKO BP Ekstraklase z zakladami pre-match i in-play. Dostepne rynki: 1X2, over/under bramki, handicap i zaklady na zawodnikow."),
            ("Jaki format kursow jest dostepny?", "Stake oferuje trzy formaty kursow: dziesietny (europejski), ulamkowy (brytyjski) i amerykanski (moneyline). Mozesz zmienic format w ustawieniach konta."),
            ("Jak dziala Cash Out na Stake?", "Cash Out pozwala zakonczyc zaklad przed koncem meczu po aktualnym kursie. Dostepny jako pelny, czesciowy lub automatyczny (Auto Cash Out przy wybranym progu kwoty)."),
        ],
        "sports"
    )

    # stake-engine
    pages["stake-engine"] = build_generic_pl(
        "stake-engine",
        "Stake Engine | Technologia Platformy i Provably Fair | MAX3000",
        "Jak dziala Stake: Provably Fair, bezpieczenstwo konta, RNG, infrastruktura platformy. Kod MAX3000: 200% do $3,000.",
        "Stake Engine",
        "Technologia za kulisami platformy.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Provably Fair: <span class="text-gradient-gold">jak weryfikowac?</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>System Provably Fair</h3><p>Stake Originals korzysta z kryptograficznego systemu Provably Fair. Przed kazda runda serwer generuje seed i publikuje jego hash (SHA256). Gracz moze wprowadzic wlasny client seed. Po rundzie serwer ujawnia oryginalny seed. Gracz moze samodzielnie obliczyc wynik uzywajac opublikowanego algorytmu. Ten mechanizm uniemozliwia Stake manipulacje wynikami po zakonczeniu rundy.</p></div>
        <div class="club-card"><h3>RNG dla gier zewnetrznych</h3><p>Gry od zewnetrznych dostawcow (Pragmatic Play, Evolution i inne) korzystaja z wlasnych generatorow liczb losowych (RNG), certyfikowanych przez niezalezne laboratoria takie jak GLI, iTech Labs i BMM. Certyfikaty RTP i RNG sa regularnie odnawiane i dostepne w dokumentacji dostawcow.</p></div>
        <div class="club-card"><h3>Bezpieczenstwo konta</h3><p>Stake wymaga weryfikacji email przy rejestracji. Dwuetapowa weryfikacja (2FA) jest dostepna i zalecana dla wszystkich kont. Google Authenticator lub SMS jako metody 2FA. KYC (Know Your Customer) jest wymagany przed wyplatami. Wszystkie dane osobowe sa szyfrowane zgodnie ze standardami branzy.</p></div>
        <div class="club-card"><h3>Infrastruktura i dostepnosc</h3><p>Stake utrzymuje infrastrukture z geograficznie rozproszonych serwerow. Platforma jest dostepna przez przegladarke webowa (stake.com) oraz przez aplikacje mobilna na iOS i Androida. API Stake obsluguje miliony zakładow dziennie z minimalnym opoznieniem. Dostepnosc platformy to regularnie ponad 99.9% uptime.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Jak dziala Provably Fair na Stake?", "Przed kazda runda serwer generuje hash (SHA256) wyniku. Gracz moze sprawdzic hash po rundzie, uzywajac opublikowanego seeda serwera i klienta. Dzieki temu mozliwa jest niezalezna weryfikacja, ze wynik nie zostal zmieniony przez Stake."),
            ("Czy Stake ma aplikacje mobilna?", "Tak. Stake ma aplikacje mobilna na iOS i Androida. Mozna ja pobrac przez stake.com. Aplikacja oferuje pelna funkcjonalnosc platformy."),
            ("Jakie certyfikaty ma Stake?", "Stake dziala na podstawie licencji Curacao OGL/2024/1451/0918. Gry zewnetrznych dostawcow sa certyfikowane przez GLI, iTech Labs, BMM i inne laboratoria audytowe."),
        ],
        "stake-engine"
    )

    # stake-us-bonus
    pages["stake-us-bonus"] = build_generic_pl(
        "stake-us-bonus",
        "Stake.us Bonus MAX3000 | 560K Gold Coins | Sweepstakes USA",
        "Stake.us z kodem MAX3000: 560,000 Gold Coins, 56 Stake Cash, 3.5% rakeback. Platforma sweepstakes dla USA w 37 stanach.",
        "Stake.us Bonus",
        "560K GC i 56 SC. Dla graczy z USA.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake.us: <span class="text-gradient-gold">jak to dziala?</span></h2></div>
      <p style="color:var(--text-dim);max-width:700px;margin:0 auto 24px;">Stake.us to odrebna platforma sweepstakes dla graczy z USA, prowadzona przez Sweepsteaks Limited. Platforma sweepstakes nie wymaga prawdziwych depozytow. Zamiast tego gracze uzywaja Gold Coins (GC) do gry i Stake Cash (SC), wirtualnej waluty, ktora po spelnieniu warunkow mozna wymienic na nagrody. Stake.us jest legalny w 37 stanach USA.</p>
      <div class="intel-grid">
        <div class="intel-card"><div class="ic-label">Kod</div><div class="ic-value">MAX3000</div><div class="ic-detail">Wpisz MAX3000 przy rejestracji na stake.us, aby odblokowac powitalne GC i SC.</div></div>
        <div class="intel-card"><div class="ic-label">Gold Coins</div><div class="ic-value">560,000 GC</div><div class="ic-detail">Gold Coins sa waluta do gry bez wartosci pienieznej. Uzywane wylacznie do grania w gry na Stake.us.</div></div>
        <div class="intel-card"><div class="ic-label">Stake Cash</div><div class="ic-value">56 SC</div><div class="ic-detail">Stake Cash po 3-krotnym obrocie mozna wymienic na nagrody. 1 SC = $1 przy wymianie.</div></div>
        <div class="intel-card"><div class="ic-label">Rakeback</div><div class="ic-value">3.5%</div><div class="ic-detail">Staly rakeback 3.5% od wszystkich zakładow na Stake.us przy aktywacji kodu MAX3000.</div></div>
        <div class="intel-card"><div class="ic-label">Dostepnosc</div><div class="ic-value">37 stanow</div><div class="ic-detail">Dostepny we wszystkich stanach USA z wyjatkiem Idaho, Michigan, Nevada, New York i Washington.</div></div>
        <div class="intel-card"><div class="ic-label">Gry</div><div class="ic-value">Tylko kasyno</div><div class="ic-detail">Brak zakladow sportowych na Stake.us. Dostepne gry kasynowe, wlacznie ze Stake Originals i slotami.</div></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake.com kontra <span class="text-gradient-gold">Stake.us</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Stake.com (globalny)</h3><p>Prawdziwe pieniadze, kryptowaluty i fiat. Dostepny globalnie poza USA i UK. Bonus 200% do $3,000 z kodem MAX3000. Kasyno, sportsbook, poker, Originals. Wymaga KYC poziom 3.</p><a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Stake.com z MAX3000</a></div>
        <div class="club-card"><h3>Stake.us (USA)</h3><p>Platforma sweepstakes bez prawdziwych depozytow. Gold Coins i Stake Cash. Dostepna w 37 stanach. Kod MAX3000: 560K GC, 56 SC, 3.5% rakeback. Tylko kasyno, brak sportu.</p><a href="{STAKE_US_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Stake.us z MAX3000</a></div>
      </div>
    </div>
  </section>''',
        [
            ("Czym sa Gold Coins?", "Gold Coins (GC) to waluta do gry na Stake.us bez wartosci pienieznej. Uzywane wylacznie do grania w gry kasynowe. Nie mozna ich wymienic na pieniadze."),
            ("Czym jest Stake Cash?", "Stake Cash (SC) to wirtualna waluta, ktora po 3-krotnym obrocie mozna wymienic na nagrody (1 SC = $1). Stake Cash mozna zdobyc przez codzienne logowanie, zakup pakietow GC lub przez kod MAX3000 przy rejestracji."),
            ("W ktorych stanach USA dziala Stake.us?", "Stake.us jest dostepny w 37 stanach USA. Niedostepny w: Idaho, Michigan, Nevada, New York i Washington. Przed rejestracją sprawdz, czy twoj stan jest na liscie dozwolonych."),
        ],
        "stake-us-bonus"
    )

    # vip
    pages["vip"] = build_generic_pl(
        "vip",
        "Stake VIP Program | Rakeback, Bonusy, Menedzer VIP | MAX3000",
        "Program VIP Stake: jak dziala rakeback, nagrody za poziomy VIP, bonusy urodzinowe, dedykowany menedzer. Kod MAX3000: 200% do $3,000 przy rejestracji.",
        "Stake VIP Program",
        "Elita kasyna kryptowalutowego.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Program <span class="text-gradient-gold">VIP Stake</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Rakeback</h3><p>Stake VIP oparty jest na systemie rakeback. Im wiecej grasz, tym wyzszy procent zwrotu z kazdego zakladu. Rakeback dostepny jest przez Promotions na stronie Stake lub przez dedykowanego menadzera VIP. Stawka rakeback rosnie wraz z poziomem VIP i historycznym wolumenem gry.</p></div>
        <div class="club-card"><h3>Poziomy VIP</h3><p>Stake ma wielopoziomowy system VIP: Bronze, Silver, Gold, Platinum, Diamond. Kazdy poziom odblokowuje wyzszy rakeback, wieksze bonusy przeladowania konta, szybsze wyplaty i priorytetowy support. Diamond VIP ma dostep do ekskluzywnych wydarzen i najwyzszych limitow wypłat.</p></div>
        <div class="club-card"><h3>Bonusy VIP</h3><p>Bonus urodzinowy: jednorazowy bonus w miesiacu urodzin. Bonus tygodniowy: na podstawie wolumenu gry z poprzedniego tygodnia. Bonus miesieczny: na podstawie miesiac-na-miesiac. Wszystkie bonusy VIP sa negocjowane indywidualnie z menedzerem VIP i zaleza od poziomu aktywnosci.</p></div>
        <div class="club-card"><h3>Dedykowany menedzer VIP</h3><p>Gracze na wyzszych poziomach VIP (Gold i powyzej) dostaja dedykowanego menadzera VIP dostepnego przez czat lub Telegram. Menedzer moze rozwiazywac problemy priorytetowo, negocjowac bonusy i zapewnic dostep do ekskluzywnych ofert niedostepnych publicznie.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Jak dolaczyc do programu VIP Stake?", "Program VIP Stake nie ma formalnego procesu aplikacji. Stake monitoruje aktywnosc graczy i zaprasza do programu VIP na podstawie wolumenu gry. Kod MAX3000 przy rejestracji zapewnia dostep do systemu bazowego rakeback."),
            ("Ile wynosi rakeback VIP?", "Stawki rakeback sa indywidualnie negocjowane z menedzerem VIP i nie sa publicznie ogłaszane. Im wyzszy poziom VIP i wolumen gry, tym wyzszy rakeback. Standardowo bazowy rakeback dostepny jest przez Promotions na stronie Stake."),
            ("Czy mozna stracic status VIP?", "Status VIP moze sie zmniejszyc, jesli aktywnosc gracza spadnie przez dluzszy czas. Szczegolowe warunki programu VIP sa ustalane indywidualnie z menedzerem VIP."),
        ],
        "vip"
    )

    return pages


# ─────────────────────────────────────────────────────────
# BUILD ALL NL PAGES
# ─────────────────────────────────────────────────────────

def build_nl_index():
    slug_path = ""
    bc_data = [("Startpagina", "https://winnersclub.com/nl/")]
    faq_items = [
        ("Is MAX3000 de grootste Stake bonuscode?", "Ja. 200% bonus tot $3.000 met een inzeteis van 40x berekend over stortingsbedrag plus bonus. De meeste publieke codes stoppen bij 100% tot $1.000. MAX3000 is de code die de club bij de ingang uitreikt."),
        ("Is Stake.com betrouwbaar?", "Stake opereert sinds 2017 onder Curacao-licentie OGL/2024/1451/0918, uitgegeven aan Medium Rare NV. On-chain reserves bedroegen $339.53M per 28 mei 2026, publiek te volgen via Arkham. Oprichters Ed Craven (geb. 1995, Melbourne) en Bijan Tehrani runnen ook Kick. Moederbedrijf Easygo Group Holdings rapporteerde A$970M omzet in FY2025."),
        ("Hoe verifieer ik de Stake-reserves?", "Snapshot van 28 mei 2026 toont $339.53M in door Arkham getagde wallets. Ethereum 74%, Solana 14%, negendicijferige stablecoin-saldi. Alles te volgen op cryptotips.com via Arkham Intel."),
        ("Waar kan ik spelen?", "De Curacao-licentie dekt de meeste landen, maar Stake hanteert eigen beperkingen in de VS, het VK, Australie en enkele andere jurisdicties. Gebruik de spiegelpagina om het juiste domein voor jouw regio te vinden."),
        ("Hoe snel zijn uitbetalingen?", "Crypto-opnames worden doorgaans binnen 30 tot 60 minuten verwerkt. TRX, XRP en SOL worden binnen seconden verrekend. Grote bedragen kunnen 2 tot 4 werkdagen compliance-review vereisen. MoonPay fiat-opnames duren 1 tot 5 werkdagen.")
    ]
    content = page_head("nl", "nl/", "Stake Bonuscode MAX3000 - 200% tot $3.000 Welkomstbonus", "Stake.com exclusieve spelerclub. Code MAX3000: 200% bonus tot $3.000, inzeteis 40x (storting plus bonus). GGR $4.7B, 21 mln accounts, on-chain reserves $339.53M. Curacao OGL/2024/1451/0918, opgericht 2017.", "default")
    content += "\n" + schema_webpage("WinnersClub - Stake Club | Code MAX3000, 200% tot $3.000", "Stake.com exclusieve spelerclub. Code MAX3000: 200% tot $3.000, inzeteis 40x. GGR $4.7B, reserves $339.53M.", "https://winnersclub.com/nl/")
    content += "\n" + schema_breadcrumb(bc_data)
    content += "\n" + schema_faq(faq_items)
    content += "\n" + hreflang_block(slug_path)
    content += '\n  <script src="/lang-redirect.js" defer></script>\n'
    content += '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&display=swap"><link rel="preload" as="image" href="/images/girl-homepage-3.avif" type="image/avif" fetchpriority="high">\n'
    content += org_schema() + '\n'
    content += '<script type="application/ld+json" data-ld="website">{"@context":"https://schema.org","@type":"WebSite","url":"https://winnersclub.com/","name":"WinnersClub","potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://winnersclub.com/?q={search_term_string}"},"query-input":"required name=search_term_string"}}</script>\n'
    content += '<script type="application/ld+json" data-ld="bc">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://winnersclub.com/"},{"@type":"ListItem","position":2,"name":"NL","item":"https://winnersclub.com/nl/"}]}</script>\n'
    content += '<meta name="twitter:image" content="https://winnersclub.com/images/og/default.png"><meta name="twitter:card" content="summary_large_image"></head>\n'
    content += header_nl()
    content += f'''
  <section class="club-hero">
    <div class="ch-bg" style="background-image:image-set(url('/images/girl-homepage-3.avif') type('image/avif'), url('/images/girl-homepage-3.webp') type('image/webp'));"></div>
    <div class="ch-overlay"></div>
    <div class="ch-content">
      <div class="ch-text">
        <p class="ch-tease">Als je deze pagina hebt gevonden, heeft de uitsmijter je al goedgekeurd.</p>
        <h1 class="ch-title text-gradient-gold">Stake Bonuscode MAX3000<span class="h1-sub">De club in.</span></h1>
        <p class="ch-sub">De exclusieve achterkamer voor Stake-spelers. Fluister <span class="code-highlight">MAX3000</span> bij de ingang en ontvang <strong>200% bonus tot $3.000</strong> met een <strong>inzeteis van 40x berekend over storting plus bonus</strong>. Goedkope publieke codes halen dit niet. Een andere plek geeft je $100 en een handdruk.</p>
        <div class="ch-actions">
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-xl btn-gold-grad">Ontvang 200% tot $3.000 op Stake.com</a>
          <a href="/nl/promo-code/" class="btn btn-primary" style="background:transparent;border:1px solid rgba(255,215,0,.4);color:var(--gold);">Wat MAX3000 opent</a>
        </div>
      </div>
    </div>
  </section>
  {ticker_nl()}
  <aside class="promo-strip" aria-label="MAX3000 Bonuscode"><div class="ps-inner"><span class="ps-label">Bonuscode</span><span class="ps-code">MAX3000</span><span class="ps-bonus">200% tot $3.000 &middot; Inzeteis 40x</span><a href="/nl/promo-code/" class="ps-cta">Open codepagina &rarr;</a></div></aside>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Waarom deze <span class="text-gradient-gold">club</span></h2></div>
      <div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Een bonus met gewicht</h3><p>200% tot $3.000 met een inzeteis van 40x berekend over storting plus bonus. Andere publiek beschikbare Stake-codes stoppen bij 100% en $1.000. Als je de code <span class="code-highlight">MAX3000</span> niet binnen 24 uur na registratie aan de dealer geeft, val je terug op het goedkope menu. Minimum storting $10, maximaal premiumwaardig is $1.500. De bonus verschijnt na storting en aanvraag via live chat. Je hebt 30 dagen om aan de inzeteis te voldoen.</p></div>
        <div class="club-card"><h3>Geld hangt aan de muur</h3><p>On-chain reserves getagd door Arkham: $339.53M per snapshot van 28 mei 2026. Geen PDF met het verzoek om te vertrouwen, geen reservetheater. Wallets zijn publiek leesbaar, iedereen met wifi kan een eigen audit uitvoeren. <a href="/nl/reserves/" style="color:var(--gold);">Bonnen, alstublieft.</a> Ethereum is 74% van de portefeuille, Solana 14%, en negendicijferige stablecoin-saldi bevestigen de operationele liquiditeit.</p></div>
        <div class="club-card"><h3>Het huis heeft een gezicht</h3><p>Ed Craven (Melbourne, geb. 1995) en Bijan Tehrani. Ze ontmoetten elkaar bij RuneScape, richtten in 2017 Stake op en lanceerden in 2022 Kick. Geschat gecombineerd vermogen volgens Forbes: US$5,6 miljard. Dit is geen lege shell company. Twee mensen die nog niet hebben verloren.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Vijf zalen, <span class="text-gradient-gold">een code</span></h2><p class="section-subtitle anim anim-fade-up anim-delay-1">Kies een deur. MAX3000 werkt in alle vijf zalen. De dealer vraagt niet waar je de bonus wilt gebruiken.</p></div>
      <div class="club-grid anim-stagger" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));"><a href="/nl/casino/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-casino-2.avif') type('image/avif'), url('/images/girl-casino-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">Casino</div></a><a href="/nl/sports/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-sports-2.avif') type('image/avif'), url('/images/girl-sports-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">Sport</div></a><a href="/nl/poker/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-poker-2.avif') type('image/avif'), url('/images/girl-poker-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">Poker</div></a><a href="/nl/aviator/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-aviator-2.avif') type('image/avif'), url('/images/girl-aviator-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">Aviator</div></a><a href="/nl/live-odds/" class="vertical-card"><div class="vc-bg" style="background-image:image-set(url('/images/girl-lucky-drive-2.avif') type('image/avif'), url('/images/girl-lucky-drive-2.webp') type('image/webp'));"></div><div class="vc-ov"></div><div class="vc-label">Live</div></a></div>
    </div>
  </section>

  <section class="girl-break girl-right anim anim-fade-up">
    <div class="girl-break-bg" style="background: image-set(url('/images/girl-homepage-2.avif') type('image/avif'), url('/images/girl-homepage-2.webp') type('image/webp')) center 15% / cover no-repeat;"></div>
    <div class="girl-break-overlay"></div>
    <div class="girl-break-content">
      <h2 class="girl-break-title">Drieduizend. <span class="text-gradient-gold">Veertig keer inzet.</span> Een code.</h2>
      <p class="girl-break-sub">Fluister <span class="code-highlight">MAX3000</span> bij registratie. De wiskunde is in jouw voordeel voordat de eerste drankjes worden gebracht.</p>
      <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Geef de code aan de dealer</a>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Wat de club <span class="text-gradient-gold">weet</span></h2></div>
      <div class="intel-grid anim-stagger">
        <div class="intel-card"><div class="ic-label">Oprichters</div><div class="ic-value">Craven en Tehrani</div><div class="ic-detail">Ed Craven (geb. 1995, Melbourne) en Bijan Tehrani. Ontmoetten elkaar bij RuneScape. Richtten samen Stake op in 2017. Lanceerden Kick in 2022.</div></div>
        <div class="intel-card"><div class="ic-label">Operator</div><div class="ic-value">Medium Rare NV</div><div class="ic-detail">Curacao-bedrijf dat Stake.com beheert. Moederbedrijf: Easygo Group Holdings, omzet FY2025 A$970M. Stake.us is een apart sweepstakes-bedrijf.</div></div>
        <div class="intel-card"><div class="ic-label">Licentie</div><div class="ic-value">Curacao OGL/2024/1451/0918</div><div class="ic-detail">Dekt de meeste landen. VK vertrokken in maart 2025. VS geblokkeerd (Stake.us sweepstakes beschikbaar in 30+ staten). Meer dan 22 bevestigde spiegelsites.</div></div>
        <div class="intel-card"><div class="ic-label">Reserves</div><div class="ic-value">$339.53M</div><div class="ic-detail">Getagd door Arkham, snapshot 28 mei 2026. Ethereum 74%, Solana 14%, negendicijferige stablecoin-saldi. Te volgen op cryptotips.com.</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Twee deuren, <span class="text-gradient-gold">een code</span></h2>
        <p class="section-subtitle">MAX3000 wordt geaccepteerd op zowel Stake.com als Stake.us. Elke deur biedt een andere ontvangst. De dealer stuurt je naar de juiste deur op basis van je woonplaats.</p>
      </div>
      <div class="club-grid anim-stagger">
        <div class="club-card">
          <h3>Stake.com - Echt Geld, Wereldwijd</h3>
          <p>Platform voor echt geld beheerd door Medium Rare NV onder Curacao OGL/2024/1451/0918. Crypto en fiat. Sport, casino, Originals, poker. Code <span class="code-highlight">MAX3000</span>: <strong>200% tot $3.000</strong>, inzeteis 40x over storting plus bonus, 30 dagen, minimum storting $10. Stort en claim via live chat. KYC niveau 3 vereist. Beschikbaar in de meeste landen buiten de VS en VK. Meer dan 3.000 slots, live casino met Evolution, sportweddenschappen op meer dan 60 disciplines.</p>
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Open de wereldwijde deur</a>
        </div>
        <div class="club-card">
          <h3>Stake.us - Sweepstakes, VS</h3>
          <p>Sweepstakes-platform van Sweepsteaks Limited voor Amerikaanse spelers. Gold Coins om mee te spelen, Stake Cash in te wisselen na drievoudig inzetten. Geen echte stortingen of opnames, geen sport, alleen casino. Code <span class="code-highlight">MAX3000</span> ontgrendelt <strong>560K GC, 56 SC en 3,5% rakeback</strong>. Beschikbaar in 37 Amerikaanse staten.</p>
          <a href="{STAKE_US_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad" style="margin-top:12px;display:inline-block;">Open de Amerikaanse deur</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-faq" id="faq">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Vragen bij <span class="text-gradient-gold">de ingang</span></h2></div>
      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Is MAX3000 de grootste Stake bonuscode?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Ja. 200% bonus tot $3.000 met een inzeteis van 40x berekend over storting plus bonus. De meeste publieke codes stoppen bij 100% tot $1.000. MAX3000 is de code die de club bij de ingang uitreikt.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Is Stake.com betrouwbaar?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Stake opereert sinds 2017 onder Curacao OGL/2024/1451/0918. On-chain reserves bedroegen $339.53M per 28 mei 2026, publiek te volgen via Arkham. Oprichters Ed Craven en Bijan Tehrani runnen ook Kick. Moederbedrijf Easygo Group Holdings rapporteerde A$970M omzet en A$257M nettowinst in FY2025.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Hoe verifieer ik de Stake-reserves?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Bekijk het <a href='/nl/reserves/'>reserverapport</a>. Snapshot van 28 mei 2026 toont $339.53M in door Arkham getagde wallets. Ethereum 74%, Solana 14%, negendicijferige stablecoin-saldi. Alles wekelijks te volgen op <a href='https://cryptotips.com/on-chain/stake/' target='_blank' rel='noopener'>cryptotips.com</a> via Arkham Intel.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Waar kan ik spelen?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>De Curacao-licentie dekt de meeste landen, maar Stake hanteert eigen beperkingen in de VS, het VK, Australie en enkele andere jurisdicties. Gebruik de <a href='/nl/mirror/'>spiegelpagina</a> om het juiste adres voor jouw regio te vinden.</p></div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">Hoe snel zijn uitbetalingen?
            <svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="faq-answer"><p>Crypto-opnames worden doorgaans binnen 30 tot 60 minuten verwerkt. TRX, XRP en SOL binnen seconden. Grote bedragen kunnen 2 tot 4 werkdagen compliance-review vereisen. MoonPay fiat-opnames duren 1 tot 5 werkdagen. Meer details op de <a href='/nl/payments/'>betalingspagina</a>.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding:60px 0;">
    <div class="section-inner" style="text-align:center;">
      <div class="section-divider"></div>
      <p style="font-style:italic;font-size:20px;color:var(--gold);margin-top:28px;">Vertel de dealer dat WinnersClub je stuurt.</p>
    </div>
  </section>

  <div class="sticky-cta" id="stickyCta">
    <div class="sticky-cta-text">Code: <span class="code-highlight">MAX3000</span>. 200% tot $3.000. De deur van Stake.com staat open</div>
    <div class="sticky-cta-actions">
      <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Kies je plek &rarr;</a>
    </div>
    <button class="sticky-cta-close" aria-label="Sluiten">&times;</button>
  </div>
'''
    content += footer_nl()
    return content


def build_all_nl():
    pages = {}

    pages["promo-code"] = build_generic_nl(
        "promo-code",
        "Stake Bonuscode MAX3000: 200% tot $3.000 (Juni 2026)",
        "Stake MAX3000: 200% bonus tot $3.000, inzeteis 40x (storting plus bonus), KYC niveau 3 vereist. Geverifieerd juni 2026.",
        "Stake Bonuscode MAX3000",
        "De code die de kluis opent.",
        f'''  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">De clubcode</div>
        <div class="code-display">MAX3000</div>
        <div class="code-meta">200% match &middot; Bonus tot $3.000 &middot; Minimum storting $10 &middot; Inzeteis 40x (storting plus bonus) &middot; KYC Niveau 3 vereist &middot; 18+ nieuwe klanten</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAX3000">Code kopieren</button>
          <a href="{STAKE_URL}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Geef de code aan de dealer &rarr;</a>
        </div>
      </div>
    </div></section>

  <section class="section" id="calculator">
    <div class="section-inner">
      <div class="section-header">
        <h2 class="section-title anim anim-rise gold-underline">Stake.com Bonus <span class="text-gradient-gold">Calculator</span></h2>
        <p class="section-subtitle anim anim-fade-up anim-delay-1">Versleep de schuif. Storting van $10 tot $1.500, 200% match tot $3.000 bonus, inzeteis 40x over totaal.</p>
      </div>
      <div class="bonus-calc">
        <h3>Bedrag eerste storting op Stake.com</h3>
        <div class="bonus-calc-input">
          <label for="depAmount">Stortingsbedrag (USD)</label>
          <input type="range" id="depRange" min="10" max="1500" step="10" value="500">
          <input type="number" id="depAmount" min="10" max="1500" step="10" value="500">
        </div>
        <div class="bonus-calc-row">
          <div class="stat"><p class="stat-label">Bonus</p><p class="stat-value" id="bonusOut">$1.000</p><p class="stat-sub">200% match, max $3.000 bonuslimiet</p></div>
          <div class="stat"><p class="stat-label">Inzetvereiste</p><p class="stat-value" id="wagerOut">$60.000</p><p class="stat-sub">(Storting + Bonus) x 40</p></div>
          <div class="stat"><p class="stat-label">Totaal speelsaldo</p><p class="stat-value" id="totalOut">$1.500</p><p class="stat-sub">Saldo na activatie bonus</p></div>
          <div class="stat"><p class="stat-label">Efficiëntie</p><p class="stat-value" id="effOut">200%</p><p class="stat-sub">Daalt onder 200% boven $1.500</p></div>
        </div>
        <p class="bonus-calc-footer"><strong style="color:var(--gold);">Maximale bonus is $3.000.</strong> Stort $1.500 en ontvang het volledige bedrag van $3.000. Stortingen boven $1.500 worden verwerkt maar de bonus groeit niet mee.</p>
        <a href="{STAKE_URL}" target="_blank" rel="noopener" class="bonus-calc-cta">Claim MAX3000 op Stake.com &rarr;</a>
      </div>
      <div class="eligibility-grid">
        <div class="item"><strong>Leeftijd</strong><span>18+ (in sommige regio's 21+)</span></div>
        <div class="item"><strong>Klanttype</strong><span>Nieuwe klant, alleen bij eerste storting</span></div>
        <div class="item"><strong>Minimum storting</strong><span>USD $10 of equivalent in crypto</span></div>
        <div class="item"><strong>Maximale premiumstorting</strong><span>$1.500 (ontvangt volledige $3.000 bonus)</span></div>
        <div class="item"><strong>Inzetvereiste</strong><span>40x (storting plus bonus), 30 dagen</span></div>
        <div class="item"><strong>KYC</strong><span>Niveau 3 vereist voor opname van bonus</span></div>
      </div>
    </div>
  </section>

  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Hoe gebruik je de code <span class="text-gradient-gold">stap voor stap</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Stap 1: Registratie</h3><p>Ga naar stake.com via de WinnersClub-link. Klik op "Registreren". Voer e-mailadres, wachtwoord en geboortedatum in. Voer bij het veld "Referral Code" of "Promo Code" de code MAX3000 in. Bevestig je e-mailadres via de activatielink.</p></div>
        <div class="club-card"><h3>Stap 2: Storting</h3><p>Stort minimaal $10. Het maximale premiumbedrag is $1.500. Beste stortingsmethode: cryptocurrency (BTC, ETH, USDT, BNB, TRX, XRP, SOL, DOGE en meer). Fiat beschikbaar via Moonpay of bankkaarten in geselecteerde regio's. De storting verschijnt binnen enkele minuten op je account.</p></div>
        <div class="club-card"><h3>Stap 3: Bonusactivatie</h3><p>Na de storting open je de live chat op stake.com. Schrijf naar support: "Ik wil de bonus activeren met code MAX3000". Support verifieert je account en activeert de bonus. De bonus van 200% van het gestorte bedrag (max. $3.000) verschijnt op je bonusaccount.</p></div>
        <div class="club-card"><h3>Stap 4: Inzetvereiste halen</h3><p>Je hebt 30 dagen om het totaal (storting plus bonus) 40 keer in te zetten. Winsten van de bonusinzet gaan eerst naar het bonusaccount. Na het volledig halen van de eis converteert het bonussaldo naar opneembaar geld. Je volgt de voortgang in de accountinstellingen.</p></div>
      </div>
    </div>
  </section>''',
        [
            ("Hoe gebruik ik de code MAX3000?", "Ga naar stake.com via de WinnersClub-link. Voer MAX3000 in bij registratie of in de accountinstellingen. Stort vervolgens minimaal $10. Neem contact op met live chat en vraag om activering van de 200% bonus tot $3.000."),
            ("Wanneer verloopt de bonus?", "Je hebt 30 dagen na activering om de inzeteis van 40x te halen. De eis wordt berekend over storting plus bonus. Als je $500 stort en $1.000 bonus ontvangt, is de vereiste inzet ($500 + $1.000) x 40 = $60.000."),
            ("Is de inzeteis moeilijk te halen?", "40x berekend over storting plus bonus is industriestandaard. De bonus is hoger dan de meeste publieke aanbiedingen (100% tot $1.000), wat de hogere inzeteis compenseert. Sportweddenschappen tellen voor 10-25% afhankelijk van de odds."),
        ],
        "promo-code"
    )

    pages["casino"] = build_generic_nl(
        "casino",
        "Stake Casino | 4.000+ Slots, 18 Originals | MAX3000",
        "Complete gids voor Stake Casino: 18 Originals met Provably Fair, 3.000-4.000 slots van 15+ aanbieders, live Evolution-tafels. Code MAX3000: 200% tot $3.000.",
        "Stake Casino",
        "Meer dan 4.000 spellen. Een code.",
        f'''  <section class="section">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Stake <span class="text-gradient-gold">Originals</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Crash</h3><p>De vermenigvuldiger start bij 1x en stijgt. Je moet uitbetalen voor de crash. Strategie: cashout op 1,5x geeft een langetermijnrendement van bijna 99%. Mogelijke winsten van 100x, 1.000x en hoger. Crash is een van de populairste Stake Originals met miljoenen spellen per dag.</p></div>
        <div class="club-card"><h3>Mines</h3><p>Een 5x5-veld met verborgen mijnen. Je kiest het aantal mijnen (1-24) en ontdekt edelstenen. Elke gevonden edelsteen vergroot de vermenigvuldiger. Je stapt uit wanneer je wilt of er een mijn explodeert. Hogere risico (meer mijnen) betekent grotere vermenigvuldigers. Provably Fair laat je de positie van mijnen verifiëren na afloop.</p></div>
        <div class="club-card"><h3>Plinko</h3><p>Een schijf valt door pegs en landt in een vakje. Bordgrootte (8 tot 16 rijen) en risico (Laag, Medium, Hoog) bepalen de uitbetalingsverdeling. Hoog risico op 16 rijen biedt maximale vermenigvuldigers. Spel gebaseerd op binomiale verdeling.</p></div>
        <div class="club-card"><h3>Dice, Keno, Limbo</h3><p>Dice: kies een getallenreeks, huis edge 1%. Keno: kies 1 tot 10 nummers op een 1-40-rooster, er worden 20 nummers getrokken. Limbo: stel een doelvermenigvuldiger in, win als de willekeurige uitkomst gelijk is aan of hoger is dan jouw doel. Alle drie Provably Fair met huis edge van 1%.</p></div>
      </div>
    </div>
  </section>
  <section class="section" style="background:var(--surface);">
    <div class="section-inner">
      <div class="section-header"><h2 class="section-title anim anim-rise gold-underline">Slots en <span class="text-gradient-gold">Live Casino</span></h2></div>
      <div class="club-grid">
        <div class="club-card"><h3>Slotbibliotheek</h3><p>Meer dan 3.000 slots van aanbieders zoals Pragmatic Play, NetEnt