#!/usr/bin/env python3
"""Build country promo-code articles modeled on 1win.global's top-performing URL pattern."""

from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent

# All 11 countries — modeled on 1win.global's top earners
COUNTRIES = [
    {
        "slug": "malawi",
        "name": "Malawi",
        "demonym": "Malawian",
        "currency_code": "MWK",
        "currency_name": "Malawian Kwacha",
        "payment_methods": "Airtel Money, TNM Mpamba, M-Pesa, National Bank of Malawi, Standard Bank, cryptocurrency",
        "popular_sports": "football (Premier League, Flames national team), basketball, cricket, athletics",
        "top_league": "Malawi Premier League (Super League)",
        "national_team": "The Flames",
        "min_deposit_local": "K8,500",
        "min_deposit_usdt": "5 USDT",
        "language_note": "Malawi is English-speaking — registration and support is all in English.",
        "isp_block_note": "Some ISPs in Malawi may throttle international betting domains during peak hours. Use the mirror link or the 1win app for uninterrupted access.",
    },
    {
        "slug": "south-africa",
        "name": "South Africa",
        "demonym": "South African",
        "currency_code": "ZAR",
        "currency_name": "South African Rand",
        "payment_methods": "FNB eWallet, Capitec Pay, Standard Bank, ABSA, Nedbank, EasyEFT, Ozow, 1Voucher, cryptocurrency",
        "popular_sports": "rugby (Springboks), cricket (Proteas), football (Bafana Bafana, PSL), Formula 1 (when Kyalami is on the calendar)",
        "top_league": "DStv Premiership (PSL), URC for rugby, SA20 for cricket",
        "national_team": "Bafana Bafana (football) and Springboks (rugby)",
        "min_deposit_local": "R90",
        "min_deposit_usdt": "5 USDT",
        "language_note": "South Africa is English-speaking for betting purposes — registration and support is all in English.",
        "isp_block_note": "South African ISPs do not generally block 1win, but a VPN or the mobile app is recommended if your fiber provider (Vumatel, Openserve) experiences brief routing issues.",
    },
    {
        "slug": "tajikistan",
        "name": "Tajikistan",
        "demonym": "Tajik",
        "currency_code": "TJS",
        "currency_name": "Tajikistani Somoni",
        "payment_methods": "Korti Milli, ESKHATA, OXIR, Alif Mobi, Salom, cryptocurrency (USDT TRC-20 most common)",
        "popular_sports": "football (Tajikistan national team), wrestling, futsal, mixed martial arts",
        "top_league": "Tajikistan Higher League",
        "national_team": "Tajikistan national football team",
        "min_deposit_local": "55 TJS",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win is available in Tajik and Russian. Most Tajik players use the Russian-language version of the site.",
        "isp_block_note": "Tajikistan's main ISPs occasionally block international betting domains. The 1win mirror and the mobile app bypass these blocks automatically.",
    },
    {
        "slug": "tanzania",
        "name": "Tanzania",
        "demonym": "Tanzanian",
        "currency_code": "TZS",
        "currency_name": "Tanzanian Shilling",
        "payment_methods": "M-Pesa, Tigo Pesa, Airtel Money, Halotel HaloPesa, CRDB Bank, NMB Bank, cryptocurrency",
        "popular_sports": "football (Taifa Stars, Simba SC, Yanga SC), athletics, boxing, basketball",
        "top_league": "Tanzania Premier League (NBC Premier League)",
        "national_team": "Taifa Stars",
        "min_deposit_local": "12,500 TZS",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win supports English and Swahili for Tanzanian players. Most users prefer the English version which has full feature coverage.",
        "isp_block_note": "Tanzanian operators (Vodacom, Airtel) generally allow 1win access. If your network is slow, the 1win Android app delivers a faster experience than the mobile browser.",
    },
    {
        "slug": "indonesia",
        "name": "Indonesia",
        "demonym": "Indonesian",
        "currency_code": "IDR",
        "currency_name": "Indonesian Rupiah",
        "payment_methods": "DANA, OVO, GoPay, ShopeePay, LinkAja, BCA, Mandiri, BRI, BNI, cryptocurrency (USDT TRC-20 most popular)",
        "popular_sports": "football (Premier League, La Liga, Liga 1), badminton (Anthony Ginting, Apriyani Rahayu), Mixed Martial Arts (ONE Championship), motorcycle racing",
        "top_league": "Liga 1 Indonesia",
        "national_team": "Tim Garuda (Indonesia national football team)",
        "min_deposit_local": "Rp 80,000",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win is fully translated into Bahasa Indonesia. Registration, support, and the mobile app are all available in Bahasa.",
        "isp_block_note": "Indonesia's main ISPs (Telkomsel, Indihome, XL Axiata, Tri, Smartfren) periodically block international gambling domains following Kominfo directives. The 1win mirror at 1wvear.life and the Android app are the most reliable access methods. A VPN is not required for most players but can be a backup.",
    },
    {
        "slug": "kazakhstan",
        "name": "Kazakhstan",
        "demonym": "Kazakh",
        "currency_code": "KZT",
        "currency_name": "Kazakhstani Tenge",
        "payment_methods": "Kaspi.kz, Halyk Bank, Forte Bank, Jysan Bank, Visa, Mastercard, cryptocurrency",
        "popular_sports": "football (Kazakhstan national team, Kairat Almaty), boxing (Gennady Golovkin tradition), MMA, ice hockey, cycling (Astana Pro Team)",
        "top_league": "Kazakhstan Premier League",
        "national_team": "Kazakhstan national football team",
        "min_deposit_local": "2,500 KZT",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win is available in Russian and Kazakh. Most Kazakh players use the Russian-language version which has the most complete feature set.",
        "isp_block_note": "Kazakhstan's Ministry of Information periodically blocks international betting domains. The 1win mirror at 1wvear.life and the Android app bypass these blocks instantly.",
    },
    {
        "slug": "korea",
        "name": "Korea",
        "demonym": "Korean",
        "currency_code": "KRW",
        "currency_name": "Korean Won",
        "payment_methods": "KakaoPay, Toss, Naver Pay, KB Star, Shinhan, Woori Bank, cryptocurrency (USDT TRC-20 most popular for fast withdrawals)",
        "popular_sports": "football (Premier League — Son Heung-min, Tottenham; K League 1), baseball (KBO), esports (League of Legends, Faker, T1, Gen.G), volleyball, Taekwondo",
        "top_league": "K League 1",
        "national_team": "Taegeuk Warriors (South Korea national football team)",
        "min_deposit_local": "₩7,000",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win is fully translated into Korean. Registration and customer support are available in Korean 24/7.",
        "isp_block_note": "Major Korean ISPs (SKT, KT, LG U+) block international online gambling domains under the Game Industry Promotion Act. Use the 1win mirror (원윈 우회) at 1wvear.life or the 1win Android APK for reliable access. The mobile app bypasses ISP filters automatically.",
    },
    {
        "slug": "costa-rica",
        "name": "Costa Rica",
        "demonym": "Costa Rican",
        "currency_code": "CRC",
        "currency_name": "Costa Rican Colón",
        "payment_methods": "SINPE Móvil, BAC Credomatic, Banco Nacional, Banco de Costa Rica, BCR, Visa, Mastercard, cryptocurrency",
        "popular_sports": "football (La Sele, Liga FPD), basketball, baseball (Cuban league import), surfing competitions",
        "top_league": "Liga FPD (Primera División de Costa Rica)",
        "national_team": "La Sele (Costa Rica national football team)",
        "min_deposit_local": "₡2,600",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win is fully translated into Spanish for Costa Rican players. SINPE Móvil deposits clear instantly through any major Costa Rican bank.",
        "isp_block_note": "Costa Rican ISPs (Kölbi, Tigo, Claro) do not block 1win. Standard access works for almost all players — no mirror or VPN required.",
    },
    {
        "slug": "gambia",
        "name": "Gambia",
        "demonym": "Gambian",
        "currency_code": "GMD",
        "currency_name": "Gambian Dalasi",
        "payment_methods": "Africell Money, QMoney, Wave, Ecobank, Trust Bank, GTBank, cryptocurrency",
        "popular_sports": "football (Scorpions, GFA League), athletics, wrestling, basketball",
        "top_league": "GFA League First Division",
        "national_team": "The Scorpions (Gambia national football team)",
        "min_deposit_local": "D350",
        "min_deposit_usdt": "5 USDT",
        "language_note": "Gambia is English-speaking — 1win registration, support, and the mobile app are all in English.",
        "isp_block_note": "Gambian ISPs (Africell, Qcell, Comium) generally allow 1win access. Use the Android app for faster performance on 3G/4G networks.",
    },
    {
        "slug": "malaysia",
        "name": "Malaysia",
        "demonym": "Malaysian",
        "currency_code": "MYR",
        "currency_name": "Malaysian Ringgit",
        "payment_methods": "Touch'n Go eWallet, Boost, GrabPay, Maybank2u, FPX, CIMB Clicks, RHB Bank, cryptocurrency",
        "popular_sports": "football (Premier League, La Liga, Malaysian Super League), badminton (Lee Zii Jia, Aaron-Wooi Yik pair), MMA (ONE Championship), motorsport (Sepang International Circuit)",
        "top_league": "Liga Super Malaysia",
        "national_team": "Harimau Malaya (Malaysia national football team)",
        "min_deposit_local": "RM 21",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win supports English and Bahasa Melayu for Malaysian players. Most users prefer English which has full feature coverage.",
        "isp_block_note": "Malaysian ISPs (Unifi, Maxis, Celcom, Digi, U Mobile) occasionally restrict international gambling domains. The 1win mirror and Android app are the most reliable access methods.",
    },
    {
        "slug": "uzbekistan",
        "name": "Uzbekistan",
        "demonym": "Uzbek",
        "currency_code": "UZS",
        "currency_name": "Uzbekistani Som",
        "payment_methods": "Click, Payme, Uzcard, Humo, Apelsin, Beeline Pay, cryptocurrency (USDT TRC-20 most popular)",
        "popular_sports": "football (Uzbekistan national team, Pakhtakor), boxing (Bektemir Melikuziev), MMA, wrestling, taekwondo",
        "top_league": "Uzbekistan Super League",
        "national_team": "Uzbekistan national football team (White Wolves)",
        "min_deposit_local": "60,000 UZS",
        "min_deposit_usdt": "5 USDT",
        "language_note": "1win is available in Russian and Uzbek. Most Uzbek players use the Russian-language version which has the most complete feature set, though full Uzbek translation is also available.",
        "isp_block_note": "Uzbek ISPs periodically restrict international gambling domains. The 1win mirror and the Android app bypass these blocks. Cryptocurrency (USDT TRC-20) is also recommended to avoid bank-level friction.",
    },
]


def article_html(c: dict) -> str:
    name = c["name"]
    slug = c["slug"]
    today = "2026-05-28"
    title = f"1win {name} 2026 — How to Register and Get Your Bonus with Promo Code XLBONUS"
    description = (
        f"How to register at 1win in {name} 2026 step by step — use promo code XLBONUS to claim a 600% welcome bonus across "
        f"4 deposits. Local payment methods: {c['payment_methods'].split(',')[0]}, {c['payment_methods'].split(',')[1].strip()}, "
        f"and more. Read the full {c['demonym']} guide."
    )
    canonical = f"https://1win.codes/en/promo-code/1win-{slug}-how-to-register-and-get-your-bonus/"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="dns-prefetch" href="//fonts.googleapis.com">
  <link rel="dns-prefetch" href="//fonts.gstatic.com">
  <link rel="dns-prefetch" href="//1win.codes">
  <meta name="theme-color" content="#141415">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="/images/og-default.png">
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <link rel="stylesheet" href="/style.min.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "{description}",
  "datePublished": "{today}",
  "dateModified": "{today}",
  "author": {{
    "@type": "Organization",
    "name": "1win.codes"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "1win.codes",
    "url": "https://1win.codes/"
  }},
  "mainEntityOfPage": "{canonical}"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://1win.codes/"}},
    {{"@type": "ListItem", "position": 2, "name": "Promo Code", "item": "https://1win.codes/en/promo-code"}},
    {{"@type": "ListItem", "position": 3, "name": "1win {name} Registration", "item": "{canonical}"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "What is the 1win promo code for {name} players in 2026?", "acceptedAnswer": {{"@type": "Answer", "text": "The 1win promo code for {name} players in 2026 is XLBONUS. Enter it during registration to claim a 600% welcome bonus on your first four deposits, in {c['currency_code']} or USDT."}}}},
    {{"@type": "Question", "name": "How long does 1win registration take from {name}?", "acceptedAnswer": {{"@type": "Answer", "text": "Registration takes under 60 seconds. {c['demonym']} players can sign up via phone number, email, or a social account, choose {c['currency_code']} as their currency, and enter promo code XLBONUS before completing their first deposit."}}}},
    {{"@type": "Question", "name": "Which payment methods does 1win accept in {name}?", "acceptedAnswer": {{"@type": "Answer", "text": "1win accepts {c['payment_methods']} for {c['demonym']} players. Cryptocurrency (USDT TRC-20) is the fastest option, with deposits clearing in under 5 minutes."}}}},
    {{"@type": "Question", "name": "What is the minimum deposit at 1win for {name} players?", "acceptedAnswer": {{"@type": "Answer", "text": "The minimum deposit is approximately {c['min_deposit_local']} ({c['min_deposit_usdt']} equivalent) for {c['demonym']} players. Bonuses are credited within seconds once the deposit clears."}}}}
  ]
}}
</script>
  <script src="/lang-redirect.js" defer></script>
</head>
<body>
  <header class="site-header" id="siteHeader">
    <div class="header-inner">
      <a href="/en/" class="header-logo" aria-label="1win.codes home">
        <svg width="120" height="32" viewBox="0 0 120 32" xmlns="http://www.w3.org/2000/svg"><text x="0" y="22" fill="#fff" font-family="Inter,sans-serif" font-size="20" font-weight="900">1win<tspan fill="#0075ff">.codes</tspan></text></svg>
      </a>
      <nav class="header-nav" id="headerNav">
        <a class="nav-link" href="/en/">Home</a>
        <a class="nav-link" href="/en/promo-code">Promo Code</a>
        <a class="nav-link" href="/en/register">Register</a>
        <a class="nav-link" href="/en/casino">Casino</a>
        <a class="nav-link" href="/en/mirrors">Mirrors</a>
        <a class="nav-link" href="/en/payment-methods">Payments</a>
      </nav>
      <div class="header-actions">
        <a href="https://1win.codes/link/9efea120200826065832/96/" target="_blank" rel="noopener" class="btn btn-signup">Join 1win</a>
      </div>
    </div>
  </header>

  <main style="padding-top:90px;">
    <article style="max-width:880px;margin:0 auto;padding:40px 24px;">
      <nav aria-label="Breadcrumb" style="margin-bottom:24px;color:var(--text-dim);font-size:14px;">
        <a href="/en/" style="color:inherit;">Home</a> &rsaquo; <a href="/en/promo-code" style="color:inherit;">Promo Code</a> &rsaquo; <span>1win {name} Registration</span>
      </nav>

      <h1 style="font-size:36px;font-weight:900;line-height:1.2;margin-bottom:16px;">1win {name}: How to Register and Get Your Bonus with Promo Code XLBONUS</h1>
      <p style="color:var(--text-dim);font-size:14px;margin-bottom:32px;">Updated {today} &middot; Reading time 6 min</p>

      <aside style="background:rgba(0,178,75,0.08);border-left:4px solid var(--green);padding:20px;border-radius:8px;margin-bottom:40px;">
        <strong>TL;DR for {c['demonym']} players:</strong> Register at <a href="https://1win.codes/link/9efea120200826065832/96/" target="_blank" rel="noopener" style="color:var(--blue);font-weight:700;">1win {name}</a> in under 60 seconds, choose {c['currency_code']} as your currency, deposit a minimum of <strong>{c['min_deposit_local']}</strong> via {c['payment_methods'].split(',')[0]} or {c['payment_methods'].split(',')[1].strip()}, enter promo code <strong style="color:var(--gold);">XLBONUS</strong>, and receive a <strong>600% welcome bonus across your first four deposits</strong>.
      </aside>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">Why 1win {name}?</h2>
      <p style="font-size:16px;line-height:1.8;color:var(--text);margin-bottom:16px;">{c['demonym']} bettors have growing options in 2026, but 1win remains the most accessible international platform for {name} players who want full sportsbook coverage of {c['popular_sports']} alongside a large online casino. The platform supports {c['currency_name']} ({c['currency_code']}) and integrates with {c['payment_methods'].split(',')[0]}, {c['payment_methods'].split(',')[1].strip()}, and the rest of the local payment ecosystem listed below.</p>
      <p style="font-size:16px;line-height:1.8;color:var(--text);margin-bottom:16px;">{c['language_note']} The headline reason most {c['demonym']} players choose 1win is the welcome bonus — a 600% match across four deposits when promo code <strong>XLBONUS</strong> is entered during registration. This is one of the highest welcome offers available to {c['demonym']} bettors and is the focus of this guide.</p>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">Step-by-step: 1win {name} Registration with XLBONUS</h2>
      <ol style="font-size:16px;line-height:1.8;color:var(--text);padding-left:24px;">
        <li style="margin-bottom:12px;"><strong>Open the 1win {name} registration page.</strong> Tap the green &quot;Join 1win&quot; button on this page. It opens the {name}-localized version of 1win with promo code XLBONUS already linked.</li>
        <li style="margin-bottom:12px;"><strong>Select your registration method.</strong> Phone number is fastest for most {c['demonym']} players; email and social options (Google, Telegram) also work.</li>
        <li style="margin-bottom:12px;"><strong>Choose your country as {name} and your currency as {c['currency_code']}.</strong> This unlocks the local payment methods and the local bonus currency display.</li>
        <li style="margin-bottom:12px;"><strong>Enter promo code <span style="color:var(--gold);font-weight:900;">XLBONUS</span></strong> in the dedicated &quot;Promo code&quot; field at the bottom of the registration form. <em>This step is essential — without it the 600% bonus is not applied retroactively.</em></li>
        <li style="margin-bottom:12px;"><strong>Complete email/phone verification.</strong> 1win will send a code via SMS or email; enter it to confirm.</li>
        <li style="margin-bottom:12px;"><strong>Make your first deposit (minimum {c['min_deposit_local']}).</strong> Choose any of the local payment methods listed below; deposits clear instantly except bank transfers (1–3 business days).</li>
        <li style="margin-bottom:12px;"><strong>Receive your 600% welcome bonus.</strong> Bonus funds appear in your 1win bonus balance within seconds. The 600% is split across your first four deposits in the breakdown below.</li>
      </ol>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">1win {name} Welcome Bonus Breakdown (XLBONUS)</h2>
      <table class="data-table" style="width:100%;margin-bottom:24px;">
        <thead><tr><th>Deposit</th><th>Bonus Match</th><th>Example ({c['currency_code']})</th></tr></thead>
        <tbody>
          <tr><td>First deposit</td><td>200%</td><td>Deposit {c['min_deposit_local']} &middot; get 3x back</td></tr>
          <tr><td>Second deposit</td><td>150%</td><td>Deposit {c['min_deposit_local']} &middot; get 2.5x back</td></tr>
          <tr><td>Third deposit</td><td>100%</td><td>Deposit {c['min_deposit_local']} &middot; get 2x back</td></tr>
          <tr><td>Fourth deposit</td><td>50%</td><td>Deposit {c['min_deposit_local']} &middot; get 1.5x back</td></tr>
          <tr><td><strong>Total</strong></td><td><strong>600%</strong></td><td><strong>Across four deposits</strong></td></tr>
        </tbody>
      </table>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">Payment Methods for 1win {name}</h2>
      <p style="font-size:16px;line-height:1.8;color:var(--text);margin-bottom:16px;">Accepted methods for {c['demonym']} players: <strong>{c['payment_methods']}</strong>. The fastest are cryptocurrency (USDT TRC-20, 5 minutes) and {c['payment_methods'].split(',')[0]} (instant). Card payments may take 1–3 business days for the first deposit while KYC is verified.</p>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">Top Sports for {c['demonym']} Players</h2>
      <p style="font-size:16px;line-height:1.8;color:var(--text);margin-bottom:16px;">1win {name} covers {c['popular_sports']}. The most-bet domestic competition is the <strong>{c['top_league']}</strong>, and {c['national_team']} matches consistently draw the highest betting volume from {c['demonym']} players. International coverage includes Premier League, La Liga, NBA, F1, ATP / WTA tennis, and major MMA promotions.</p>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">Accessing 1win in {name}</h2>
      <p style="font-size:16px;line-height:1.8;color:var(--text);margin-bottom:16px;">{c['isp_block_note']} For details see the <a href="/en/mirrors" style="color:var(--blue);">1win mirrors guide</a>.</p>

      <h2 style="font-size:26px;margin-top:40px;margin-bottom:16px;">Frequently Asked Questions</h2>
      <h3 style="font-size:18px;margin-top:24px;">What is the 1win promo code for {name} in 2026?</h3>
      <p style="font-size:16px;line-height:1.8;">The 1win promo code is <strong>XLBONUS</strong>. Enter it during registration to claim the 600% welcome bonus on your first four deposits.</p>

      <h3 style="font-size:18px;margin-top:24px;">Can I use XLBONUS after I have already registered?</h3>
      <p style="font-size:16px;line-height:1.8;">No — the promo code must be entered at the moment of registration. It cannot be applied retroactively to existing accounts. If you already registered without it, you can ask 1win support to apply manual promotions but the welcome bonus terms will be different.</p>

      <h3 style="font-size:18px;margin-top:24px;">Is 1win legal in {name}?</h3>
      <p style="font-size:16px;line-height:1.8;">1win operates as an international platform under a Curaçao license. {c['demonym']} players access 1win at their own discretion under local laws. Please check your local regulations before signing up. Gambling involves risk; play responsibly.</p>

      <h3 style="font-size:18px;margin-top:24px;">How fast are withdrawals at 1win {name}?</h3>
      <p style="font-size:16px;line-height:1.8;">Cryptocurrency withdrawals (USDT TRC-20, BTC, ETH) clear in under 5 minutes. {c['payment_methods'].split(',')[0]} and card withdrawals take 1–3 business days for the first withdrawal once KYC is completed.</p>

      <div style="background:linear-gradient(135deg,#0075ff 0%,#00d4ff 100%);padding:32px;border-radius:16px;margin-top:48px;text-align:center;">
        <h2 style="color:#fff;font-size:28px;margin-bottom:12px;">Ready to Join 1win {name}?</h2>
        <p style="color:#fff;font-size:16px;margin-bottom:24px;">Use promo code <span style="font-family:'JetBrains Mono';font-weight:700;background:rgba(0,0,0,0.3);padding:4px 10px;border-radius:6px;">XLBONUS</span> at registration for a 600% welcome bonus</p>
        <a href="https://1win.codes/link/9efea120200826065832/96/" target="_blank" rel="noopener" class="btn btn-gold btn-xl">Register at 1win {name} &rarr;</a>
      </div>

      <p style="margin-top:32px;font-size:14px;color:var(--text-muted);text-align:center;">Related: <a href="/en/promo-code" style="color:var(--blue);">XLBONUS promo code guide</a> &middot; <a href="/en/mirrors" style="color:var(--blue);">1win mirrors</a> &middot; <a href="/en/register" style="color:var(--blue);">1win registration</a> &middot; <a href="/en/payment-methods" style="color:var(--blue);">Payment methods</a></p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="footer-inner" style="max-width:1200px;margin:0 auto;padding:40px 24px;">
      <p class="footer-disclaimer" style="font-size:13px;color:var(--text-muted);">This is an unofficial fan site and is not affiliated with or endorsed by 1win. This site is for informational purposes only. Gambling involves risk &mdash; please play responsibly. If you or someone you know has a gambling problem, please contact GamCare or a local support organization.</p>
      <p class="footer-copyright" style="font-size:13px;color:var(--text-muted);margin-top:12px;">&copy; 2026 1win.codes. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""


def main():
    target_dir = ROOT / "en" / "promo-code"
    target_dir.mkdir(exist_ok=True)

    for c in COUNTRIES:
        slug = c["slug"]
        # Build canonical url-friendly directory (Google indexes either path/index.html or path.html)
        page_dir = target_dir / f"1win-{slug}-how-to-register-and-get-your-bonus"
        page_dir.mkdir(exist_ok=True)
        out = page_dir / "index.html"
        out.write_text(article_html(c), encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
