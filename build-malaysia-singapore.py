#!/usr/bin/env python3
"""Build Malaysia and Singapore country pages from the India template."""

from pathlib import Path
import re

ROOT = Path(__file__).parent

MALAYSIA = {
    "country_slug": "malaysia",
    "country_name": "Malaysia",
    "currency": "MYR (Malaysian Ringgit)",
    "payment_methods": "Touch'n Go eWallet, Boost, GrabPay, Maybank2u, FPX, cryptocurrency",
    "primary_sports": "football, badminton, sepak takraw, Premier League, La Liga",
    "title": "1win Malaysia — Sportsbook & Casino | Promo Code XLBONUS",
    "meta_description": "Access 1win in Malaysia. Football and badminton betting, casino games, Aviator. Use promo code XLBONUS for a 600% bonus. Touch'n Go, FPX and Maybank2u accepted.",
    "hero_sub": "Malaysia's Premier League and La Liga betting, badminton markets, and premium casino — join 1win Malaysia with promo code XLBONUS.",
    "intro_para_1": "1win Malaysia gives Malaysian bettors access to a full international sportsbook and online casino, with deep coverage of European football leagues (Premier League, La Liga, Bundesliga, Serie A), Asian Cup qualifiers, the Malaysia Super League, regional badminton tournaments featuring Lee Zii Jia and the Aaron-Wooi Yik doubles pair, and Formula 1 (including the Sepang Circuit during its calendar appearances). The platform supports Malaysian Ringgit (MYR) and integrates with Touch'n Go eWallet, Boost, GrabPay, Maybank2u, and FPX — the everyday payment rails used by Malaysian players.",
    "intro_para_2": "New Malaysian players registering via the link on this page can claim a 600% welcome bonus by entering <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> during sign-up. This is one of the highest welcome offers available to Malaysian bettors and applies to sports betting, casino games, and the popular Aviator crash game. Registration takes under 90 seconds and can be completed via quick registration, phone number, or social media account.",
    "intro_para_3": "Beyond football and badminton, 1win Malaysia covers tennis (with strong Asian event coverage including the Malaysian Open in Kuala Lumpur), cricket via the regional T20 competitions, basketball via the NBA, MMA via ONE Championship (a homegrown Singapore-based promotion popular across Malaysia), and esports. The 1win casino is particularly active for Malaysian players, offering live dealer games and thousands of international slot titles. The mobile app works smoothly on both iOS and Android handsets common in Malaysia.",
    "how_to_para_1": "Click Register and select your preferred method. Choose Malaysia as your country and MYR as your currency. Phone or email registration are the most popular options for Malaysian players.",
    "how_to_para_2": "Go to the Cashier and select your preferred Malaysian payment method. The minimum deposit is RM equivalent of around 5 USDT, and your welcome bonus is credited immediately after the first qualifying deposit.",
    "deposit_para": "1win Malaysia offers the widest range of Malaysian payment methods of any international operator, including the most popular e-wallets and bank transfer rails used by Malaysian players daily.",
    "payment_cards": [
        ("Touch'n Go eWallet", "Malaysia's most popular e-wallet. Instant deposits via TnG QR code or linked card. Withdrawals back to TnG within minutes."),
        ("Boost", "Boost wallet deposits work instantly. A common choice for Malaysian mobile-first players who want fast top-ups."),
        ("Maybank2u / FPX", "Direct bank transfer from any Malaysian bank via FPX. Withdraw to your Maybank, CIMB, Public Bank or RHB account in 1–3 business days."),
        ("Cryptocurrency", "BTC, ETH, USDT TRC-20 and more. Fastest option — 5 minute deposits, no Bank Negara reporting required. Recommended for larger balances."),
    ],
    "promo_para_1": "The <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> is essential for new Malaysian players. Entering XLBONUS during registration triggers a 600% match on the first four deposits — directly applicable to Premier League betting, badminton markets, ONE Championship MMA, and casino games. No other code unlocks a higher welcome bonus on the platform for Malaysian players.",
    "promo_para_2": "Malaysian players who use the <a href=\"/en/promo-code\" style=\"color:var(--blue);\">1win promo code XLBONUS</a> also gain access to ongoing promotions including football reload bonuses during European league weekends, casino cashback, free spins on new slot releases, and VIP rewards. Enter XLBONUS at registration — it cannot be applied retroactively — and unlock the complete 1win Malaysia bonus ecosystem from your first deposit.",
    "girl_break_sub": "Join thousands of players in Malaysia already using 1win. Register now and enter promo code XLBONUS for a 600% bonus.",
    "deposit_subtitle": "Deposit and withdraw using trusted Malaysia payment methods.",
}

SINGAPORE = {
    "country_slug": "singapore",
    "country_name": "Singapore",
    "currency": "SGD (Singapore Dollar)",
    "payment_methods": "PayNow, DBS PayLah!, GrabPay, NETS, cryptocurrency",
    "primary_sports": "football, Formula 1, F1 Singapore Grand Prix, Premier League, NBA",
    "title": "1win Singapore — Sportsbook & Casino | Promo Code XLBONUS",
    "meta_description": "Access 1win in Singapore. Premier League football, F1 Singapore GP, casino and Aviator. Use promo code XLBONUS for a 600% bonus. PayNow and DBS PayLah accepted.",
    "hero_sub": "Singapore's Premier League and Formula 1 betting, F1 Singapore GP markets, and premium casino — join 1win Singapore with promo code XLBONUS.",
    "intro_para_1": "1win Singapore gives Singaporean bettors access to a full international sportsbook and online casino, with marquee coverage of the F1 Singapore Grand Prix at the Marina Bay Street Circuit, the Premier League (England's top flight remains the most-watched league in Singapore), the NBA, ATP and WTA tennis tournaments including the Singapore Tennis Open, ONE Championship MMA (founded in Singapore), and regional football including the Singapore Premier League. The platform supports Singapore Dollar (SGD) and integrates with PayNow, DBS PayLah!, GrabPay and NETS — the payment rails Singaporeans use every day.",
    "intro_para_2": "New Singaporean players registering via the link on this page can claim a 600% welcome bonus by entering <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> during sign-up. This is one of the highest welcome offers available to Singapore bettors and applies to sports betting, casino games, and the popular Aviator crash game. Registration takes under 90 seconds and can be completed via quick registration, phone number, or social media account.",
    "intro_para_3": "Beyond F1 and football, 1win Singapore covers golf (with strong coverage of the Asian Tour stops in Southeast Asia), basketball via the NBA, MMA via ONE Championship, badminton via the Singapore Open BWF tournament, and esports. The 1win casino is a particular draw for Singapore players, offering live dealer games and thousands of international slot titles. <em>Note: gambling laws in Singapore restrict locally-licensed online betting to specific operators; 1win operates as an international platform — please review the operator's terms and your local regulations before signing up.</em>",
    "how_to_para_1": "Click Register and select your preferred method. Choose Singapore as your country and SGD as your currency. Phone or email registration are the most popular options for Singaporean players.",
    "how_to_para_2": "Go to the Cashier and select your preferred Singapore payment method. The minimum deposit is the SGD equivalent of around 5 USDT, and your welcome bonus is credited immediately after the first qualifying deposit.",
    "deposit_para": "1win Singapore offers a range of payment methods used by Singaporean players, including the most popular e-wallets and bank rails. PayNow is the fastest option for instant SGD transfers.",
    "payment_cards": [
        ("PayNow", "Singapore's instant interbank transfer system. Deposits arrive in seconds via QR or mobile number. Withdrawals back to your linked bank account within minutes during business hours."),
        ("DBS PayLah!", "Singapore's most-used mobile wallet. Instant deposits via PayLah! QR code. A common choice for Singapore players who want to keep gambling balances separate from their main bank account."),
        ("GrabPay / NETS", "GrabPay deposits work instantly across Singapore. NETS provides direct bank-account top-ups via the NETS network used at ATMs and POS terminals across the country."),
        ("Cryptocurrency", "BTC, ETH, USDT TRC-20 and more. Fastest option overall — 5 minute deposits, maximum privacy, no MAS reporting required. Recommended for larger balances."),
    ],
    "promo_para_1": "The <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> is essential for new Singaporean players. Entering XLBONUS during registration triggers a 600% match on the first four deposits — directly applicable to Premier League betting, F1 Singapore GP markets, ONE Championship MMA, and casino games. No other code unlocks a higher welcome bonus on the platform for Singapore players.",
    "promo_para_2": "Singapore players who use the <a href=\"/en/promo-code\" style=\"color:var(--blue);\">1win promo code XLBONUS</a> also gain access to ongoing promotions including football reload bonuses during European league weekends, F1 Singapore GP weekend specials, casino cashback, free spins on new slot releases, and VIP rewards. Enter XLBONUS at registration — it cannot be applied retroactively — and unlock the complete 1win Singapore bonus ecosystem from your first deposit.",
    "girl_break_sub": "Join thousands of players in Singapore already using 1win. Register now and enter promo code XLBONUS for a 600% bonus.",
    "deposit_subtitle": "Deposit and withdraw using trusted Singapore payment methods.",
}


def patch_country_page(src: Path, dst: Path, cfg: dict):
    """Patch India-template country page in place to localized country content."""
    text = src.read_text(encoding="utf-8")
    country_lower = cfg["country_slug"]
    country_name = cfg["country_name"]
    country_upper = country_name.upper()

    # Title + meta
    text = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", text, count=1)
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{cfg["meta_description"]}">',
        text, count=1,
    )
    text = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{cfg["title"]}">',
        text, count=1,
    )
    text = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{cfg["meta_description"]}">',
        text, count=1,
    )

    # Canonical (handle both root and /en/ paths)
    text = text.replace("country-india", f"country-{country_lower}")

    # JSON-LD name + description
    text = re.sub(r'"name": "1win India[^"]*"', f'"name": "1win {country_name} — Sportsbook & Casino"', text)
    text = text.replace(
        '"description": "Access 1win in India. Cricket betting, IPL, kabaddi and casino. Use promo code XLBONUS for a 600% bonus. UPI, Paytm, and PhonePe payments accepted here."',
        f'"description": "{cfg["meta_description"]}"',
    )
    text = re.sub(r'"name": "India"', f'"name": "{country_name}"', text)

    # Visible H1, hero sub, breadcrumb, CTAs
    text = text.replace('<span class="current">India</span>', f'<span class="current">{country_name}</span>')
    text = re.sub(
        r"India's IPL cricket betting, kabaddi markets, and premium casino — join 1win India with promo code XLBONUS\.",
        cfg["hero_sub"], text,
    )
    text = text.replace(">Join 1win India<", f">Join 1win {country_name}<")
    text = text.replace("1win India", f"1win {country_name}")
    text = text.replace("1WIN INDIA", f"1WIN {country_upper}")

    # Intro paragraphs (we replace the original 3 India intro paragraphs by anchoring on unique fragments)
    text = re.sub(
        r"1win India is built for the world's largest cricket market\.[^<]+",
        cfg["intro_para_1"], text,
    )
    text = re.sub(
        r"New Indian players registering via the link on this page can claim a massive 600% welcome bonus by entering <strong[^>]+>1win promo code XLBONUS</strong>[^<]+",
        cfg["intro_para_2"].replace('<strong style="color:var(--gold);">1win promo code XLBONUS</strong>', '@@PROMOTAG@@'),
        text,
    )
    text = text.replace('@@PROMOTAG@@', '<strong style="color:var(--gold);">1win promo code XLBONUS</strong>')
    text = re.sub(
        r"Beyond cricket, 1win India covers[^<]+",
        cfg["intro_para_3"], text,
    )

    # Info table: currency + payment methods
    text = re.sub(
        r"<td>INR \(Indian Rupee\)</td>",
        f"<td>{cfg['currency']}</td>", text,
    )
    text = re.sub(
        r"<td>UPI, Paytm, PhonePe, bank transfer, cryptocurrency</td>",
        f"<td>{cfg['payment_methods']}</td>", text,
    )

    # How-to paragraphs (India-specific lines)
    text = text.replace(
        "Click Register and select your preferred method. Choose India as your country and INR as your currency. Phone or email registration are the most popular options for Indian players.",
        cfg["how_to_para_1"],
    )
    text = re.sub(
        r"<h3>Deposit via UPI, Paytm, or PhonePe</h3>",
        f"<h3>Deposit via local {country_name} payment methods</h3>", text,
    )
    text = text.replace(
        "Go to the Cashier and select your preferred Indian payment method. The minimum deposit is low, and your welcome bonus is credited immediately after the first qualifying deposit.",
        cfg["how_to_para_2"],
    )

    # Promo paragraphs
    text = re.sub(
        r"The <strong[^>]+>1win promo code XLBONUS</strong> is essential for new Indian players\.[^<]+",
        cfg["promo_para_1"].replace('<strong style="color:var(--gold);">1win promo code XLBONUS</strong>', '@@P1@@').replace('<a href="/en/promo-code" style="color:var(--blue);">1win promo code XLBONUS</a>', '@@P2@@'),
        text,
    )
    text = re.sub(
        r"Indian players who use the <a[^>]+>1win promo code XLBONUS</a>[^<]+",
        cfg["promo_para_2"].replace('<a href="/en/promo-code" style="color:var(--blue);">1win promo code XLBONUS</a>', '@@P2@@'),
        text,
    )
    text = text.replace('@@P1@@', '<strong style="color:var(--gold);">1win promo code XLBONUS</strong>')
    text = text.replace('@@P2@@', '<a href="/en/promo-code" style="color:var(--blue);">1win promo code XLBONUS</a>')

    # Girl-break sub
    text = re.sub(
        r"Join thousands of players in India already using 1win\. Register now and enter promo code XLBONUS for 600% bonus\.",
        cfg["girl_break_sub"], text,
    )

    # Payment section subtitle + intro
    text = text.replace("Deposit and withdraw using trusted India payment methods.", cfg["deposit_subtitle"])
    text = text.replace(
        "1win India offers the widest range of Indian payment methods of any international operator, including the most popular UPI apps and digital wallets used by Indian players daily.",
        cfg["deposit_para"],
    )

    # Replace the four India payment cards (UPI, Paytm, PhonePe, bank transfer / crypto)
    # Be tolerant - we re-write them inline
    pay_cards_html = ""
    for h3_title, body in cfg["payment_cards"]:
        pay_cards_html += f'        <div class="payment-card anim-fade-up">\n          <h3>{h3_title}</h3>\n          <p>{body}</p>\n        </div>\n'

    # Strip the original India payment cards block (between the deposit intro and the next section)
    text = re.sub(
        r'(<h3>UPI</h3>.*?</div>\s*</section>)',
        lambda m: pay_cards_html + "      </div>\n    </section>",
        text, count=1, flags=re.DOTALL,
    )

    dst.write_text(text, encoding="utf-8")
    print(f"Wrote {dst}")


SOUTH_AFRICA = {
    "country_slug": "south-africa",
    "country_name": "South Africa",
    "currency": "ZAR (South African Rand)",
    "payment_methods": "FNB eWallet, Capitec Pay, Standard Bank, ABSA, Nedbank, EasyEFT, Ozow, 1Voucher, cryptocurrency",
    "primary_sports": "rugby (Springboks), cricket (Proteas), football (PSL, Bafana Bafana), Aviator crash game",
    "title": "1win South Africa — Sportsbook & Casino | Promo Code XLBONUS",
    "meta_description": "Access 1win in South Africa. PSL football, Springboks rugby, Proteas cricket, Aviator and casino. Use promo code XLBONUS for a 600% bonus. FNB, Capitec, EasyEFT and Ozow accepted.",
    "hero_sub": "South Africa's PSL football, Springboks rugby and Proteas cricket betting plus the most-played Aviator crash game in SA — join 1win South Africa with promo code XLBONUS.",
    "intro_para_1": "1win South Africa gives South African bettors access to a complete international sportsbook and online casino, with marquee coverage of the DStv Premiership (PSL), the URC for the Bulls / Stormers / Sharks / Lions, the SA20 cricket tournament featuring the Proteas, Bafana Bafana qualifiers, and global football including the Premier League, La Liga and the Champions League. The platform supports Rand (ZAR) and integrates with FNB eWallet, Capitec Pay, Standard Bank, ABSA, Nedbank, EasyEFT and Ozow — the payment rails South Africans use every day.",
    "intro_para_2": "New South African players registering via the link on this page can claim a 600% welcome bonus by entering <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> during sign-up. This is one of the highest welcome offers available to SA bettors and applies to sports betting, casino games, and the wildly popular Aviator crash game (where South African players make up one of the largest user bases worldwide). Registration takes under 90 seconds and can be completed via quick registration, phone number, or social media account.",
    "intro_para_3": "Beyond PSL football and Springboks rugby, 1win South Africa covers F1 (with focused coverage when Kyalami is on the calendar), the Currie Cup, Nedbank Cup, basketball via the NBA, MMA via the UFC, and golf via the DP World Tour South African events. The 1win casino is a particular draw for SA players, offering live dealer games and thousands of international slots. South African players have especially deep engagement with the Aviator crash game.",
    "how_to_para_1": "Click Register and select your preferred method. Choose South Africa as your country and ZAR as your currency. Phone or email registration are the most popular options for South African players.",
    "how_to_para_2": "Go to the Cashier and select your preferred SA payment method. The minimum deposit is the ZAR equivalent of around 5 USDT (about R90), and your welcome bonus is credited immediately after the first qualifying deposit.",
    "deposit_para": "1win South Africa offers a deep range of SA payment methods including all four major banks, FNB eWallet, Capitec Pay, EasyEFT, Ozow and the prepaid 1Voucher. Cryptocurrency (USDT TRC-20) is the fastest option with deposits clearing in under 5 minutes.",
    "payment_cards": [
        ("FNB eWallet", "FNB eWallet deposits arrive instantly via the FNB app or USSD. A common choice for South African players who want to keep gambling funds separate from their main account."),
        ("Capitec Pay / EasyEFT", "Capitec Pay and EasyEFT both move ZAR from any South African bank to your 1win account within seconds. Withdrawals back to your linked account clear within 1-3 business days."),
        ("Ozow / 1Voucher", "Ozow gives instant SA-bank-to-1win transfers via secure direct EFT. 1Voucher prepaid vouchers can be bought at PEP, Shoprite, Checkers and Spar then redeemed instantly at 1win."),
        ("Cryptocurrency", "BTC, ETH, USDT TRC-20 and more. Fastest option for South African players — 5 minute deposits, no SARB reporting required, and ideal for larger balances. Recommended for serious bettors."),
    ],
    "promo_para_1": "The <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> is essential for new South African players. Entering XLBONUS during registration triggers a 600% match on the first four deposits — directly applicable to PSL betting, Springboks rugby markets, SA20 cricket, NBA, F1, and the Aviator crash game where South Africa has one of the world's most active player bases. No other code unlocks a higher welcome bonus on the platform for SA players.",
    "promo_para_2": "South African players who use the <a href=\"/en/promo-code\" style=\"color:var(--blue);\">1win promo code XLBONUS</a> also gain access to ongoing promotions including PSL match-day reload bonuses, Aviator-specific multiplier challenges, casino cashback, free spins on new slot releases, and VIP rewards. Enter XLBONUS at registration — it cannot be applied retroactively — and unlock the complete 1win South Africa bonus ecosystem from your first deposit.",
    "girl_break_sub": "Join thousands of players in South Africa already using 1win. Register now and enter promo code XLBONUS for a 600% bonus.",
    "deposit_subtitle": "Deposit and withdraw using trusted South Africa payment methods.",
}

TANZANIA = {
    "country_slug": "tanzania",
    "country_name": "Tanzania",
    "currency": "TZS (Tanzanian Shilling)",
    "payment_methods": "M-Pesa, Tigo Pesa, Airtel Money, Halotel HaloPesa, CRDB Bank, NMB Bank, cryptocurrency",
    "primary_sports": "football (Taifa Stars, Simba SC, Yanga SC), athletics, boxing, basketball",
    "title": "1win Tanzania — Sportsbook & Casino | Promo Code XLBONUS",
    "meta_description": "Access 1win in Tanzania. NBC Premier League football, Taifa Stars, casino and Aviator. Use promo code XLBONUS for a 600% bonus. M-Pesa, Tigo Pesa and Airtel Money accepted.",
    "hero_sub": "Tanzania's NBC Premier League and Taifa Stars betting, plus Simba SC vs Yanga SC derby markets and premium casino — join 1win Tanzania with promo code XLBONUS.",
    "intro_para_1": "1win Tanzania gives Tanzanian bettors access to a complete international sportsbook and online casino, with deep coverage of the NBC Premier League (the Tanzanian top flight), the historic Simba SC vs Yanga SC derby, Taifa Stars AFCON qualifiers, regional CAF Champions League fixtures, and global football including the Premier League and La Liga. The platform supports Tanzanian Shilling (TZS) and integrates with M-Pesa, Tigo Pesa, Airtel Money, Halotel HaloPesa, CRDB Bank and NMB Bank — the mobile money and banking rails used by Tanzanian players every day.",
    "intro_para_2": "New Tanzanian players registering via the link on this page can claim a 600% welcome bonus by entering <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> during sign-up. This is one of the highest welcome offers available to Tanzanian bettors and applies to sports betting, casino games, and the popular Aviator crash game. Registration takes under 90 seconds and can be completed via quick registration, phone number, or social media account.",
    "intro_para_3": "Beyond domestic football, 1win Tanzania covers athletics (Tanzania has a strong distance-running tradition), boxing, basketball via the NBA, MMA via the UFC, and the East African Cup. The 1win casino is a particular draw for Tanzanian players, offering live dealer games and thousands of international slots, with mobile-optimized performance for the 3G/4G networks common across East Africa. The mobile app works smoothly on Android handsets popular in Tanzania.",
    "how_to_para_1": "Click Register and select your preferred method. Choose Tanzania as your country and TZS as your currency. Phone or email registration are the most popular options for Tanzanian players.",
    "how_to_para_2": "Go to the Cashier and select your preferred Tanzanian payment method. The minimum deposit is the TZS equivalent of around 5 USDT (about 12,500 TZS), and your welcome bonus is credited immediately after the first qualifying deposit.",
    "deposit_para": "1win Tanzania offers a deep range of Tanzanian payment methods including all four major mobile money providers and the leading banks. M-Pesa is the fastest option for TZS-denominated deposits.",
    "payment_cards": [
        ("M-Pesa", "M-Pesa deposits arrive instantly via Vodacom mobile money. Tanzania's most-used payment method. Withdrawals back to M-Pesa clear in minutes during business hours."),
        ("Tigo Pesa / Airtel Money", "Tigo Pesa and Airtel Money give instant deposits via mobile-network-agnostic transfers. Common choices for Tanzanian players outside the Vodacom network."),
        ("CRDB Bank / NMB Bank", "Direct bank transfer from any Tanzanian bank account via CRDB or NMB. Suitable for larger deposits. Withdrawals back to your account clear in 1-3 business days."),
        ("Cryptocurrency", "BTC, ETH, USDT TRC-20 and more. Fastest option overall — 5 minute deposits, no Bank of Tanzania reporting required. Recommended for larger balances."),
    ],
    "promo_para_1": "The <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> is essential for new Tanzanian players. Entering XLBONUS during registration triggers a 600% match on the first four deposits — directly applicable to NBC Premier League betting, Simba SC and Yanga SC derby markets, Taifa Stars qualifiers, and the Aviator crash game. No other code unlocks a higher welcome bonus on the platform for Tanzanian players.",
    "promo_para_2": "Tanzanian players who use the <a href=\"/en/promo-code\" style=\"color:var(--blue);\">1win promo code XLBONUS</a> also gain access to ongoing promotions including football reload bonuses during Simba/Yanga derby weekends, casino cashback, free spins on new slot releases, and VIP rewards. Enter XLBONUS at registration — it cannot be applied retroactively — and unlock the complete 1win Tanzania bonus ecosystem from your first deposit.",
    "girl_break_sub": "Join thousands of players in Tanzania already using 1win. Register now and enter promo code XLBONUS for a 600% bonus.",
    "deposit_subtitle": "Deposit and withdraw using trusted Tanzania payment methods.",
}

MALAWI = {
    "country_slug": "malawi",
    "country_name": "Malawi",
    "currency": "MWK (Malawian Kwacha)",
    "payment_methods": "Airtel Money, TNM Mpamba, M-Pesa, National Bank of Malawi, Standard Bank, cryptocurrency",
    "primary_sports": "football (Flames, Super League), basketball, cricket, athletics",
    "title": "1win Malawi — Sportsbook & Casino | Promo Code XLBONUS",
    "meta_description": "Access 1win in Malawi. Super League football, Flames national team, Aviator and casino. Use promo code XLBONUS for a 600% bonus. Airtel Money, TNM Mpamba and M-Pesa accepted.",
    "hero_sub": "Malawi's Super League football and Flames national team betting plus a premium casino — join 1win Malawi with promo code XLBONUS.",
    "intro_para_1": "1win Malawi gives Malawian bettors access to a complete international sportsbook and online casino, with coverage of the Malawi Premier League (Super League), Flames national team AFCON qualifiers, the TNM Super League playoffs, and global football including the Premier League and La Liga. The platform supports Malawian Kwacha (MWK) and integrates with Airtel Money, TNM Mpamba, M-Pesa, National Bank of Malawi and Standard Bank Malawi — the mobile money and banking rails used by Malawian players every day.",
    "intro_para_2": "New Malawian players registering via the link on this page can claim a 600% welcome bonus by entering <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> during sign-up. This is one of the highest welcome offers available to Malawian bettors and applies to sports betting, casino games, and the popular Aviator crash game. Registration takes under 90 seconds and can be completed via quick registration, phone number, or social media account.",
    "intro_para_3": "Beyond domestic football, 1win Malawi covers athletics, basketball via the NBA, MMA via the UFC, and tennis. The 1win casino is a particular draw for Malawian players, offering live dealer games and thousands of international slots, with mobile-optimized performance for the 3G/4G networks common across Malawi. The Android app works smoothly even on entry-level handsets.",
    "how_to_para_1": "Click Register and select your preferred method. Choose Malawi as your country and MWK as your currency. Phone or email registration are the most popular options for Malawian players.",
    "how_to_para_2": "Go to the Cashier and select your preferred Malawian payment method. The minimum deposit is the MWK equivalent of around 5 USDT (about K8,500), and your welcome bonus is credited immediately after the first qualifying deposit.",
    "deposit_para": "1win Malawi offers a deep range of Malawian payment methods including Airtel Money, TNM Mpamba, M-Pesa, and the leading banks. Airtel Money is the fastest option for MWK-denominated deposits.",
    "payment_cards": [
        ("Airtel Money", "Airtel Money deposits arrive instantly via the Airtel mobile money platform. Malawi's most-used payment method. Withdrawals back to Airtel Money clear in minutes during business hours."),
        ("TNM Mpamba / M-Pesa", "TNM Mpamba and M-Pesa Malawi give instant deposits via mobile money. Common choices for Malawian players outside the Airtel network."),
        ("National Bank / Standard Bank", "Direct bank transfer from any Malawian bank account via National Bank of Malawi or Standard Bank. Suitable for larger deposits. Withdrawals clear in 1-3 business days."),
        ("Cryptocurrency", "BTC, ETH, USDT TRC-20 and more. Fastest option overall — 5 minute deposits, no Reserve Bank of Malawi reporting required. Recommended for larger balances."),
    ],
    "promo_para_1": "The <strong style=\"color:var(--gold);\">1win promo code XLBONUS</strong> is essential for new Malawian players. Entering XLBONUS during registration triggers a 600% match on the first four deposits — directly applicable to Super League betting, Flames national team markets, and the Aviator crash game. No other code unlocks a higher welcome bonus on the platform for Malawian players.",
    "promo_para_2": "Malawian players who use the <a href=\"/en/promo-code\" style=\"color:var(--blue);\">1win promo code XLBONUS</a> also gain access to ongoing promotions including football reload bonuses, casino cashback, free spins on new slot releases, and VIP rewards. Enter XLBONUS at registration — it cannot be applied retroactively — and unlock the complete 1win Malawi bonus ecosystem from your first deposit.",
    "girl_break_sub": "Join thousands of players in Malawi already using 1win. Register now and enter promo code XLBONUS for a 600% bonus.",
    "deposit_subtitle": "Deposit and withdraw using trusted Malawi payment methods.",
}

def main():
    src_root = ROOT / "country-india.html"
    src_en = ROOT / "en" / "country-india.html"
    for cfg in (MALAYSIA, SINGAPORE, SOUTH_AFRICA, TANZANIA, MALAWI):
        country = cfg["country_slug"]
        patch_country_page(src_root, ROOT / f"country-{country}.html", cfg)
        patch_country_page(src_en, ROOT / "en" / f"country-{country}.html", cfg)


if __name__ == "__main__":
    main()
