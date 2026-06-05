#!/usr/bin/env python3
"""
Translate EN → AR (Modern Standard Arabic) for 1win.codes
Reads en/ files → writes ar/ files
Rules from TRANSLATION_RULES.md
RTL: adds dir="rtl" to <html>
All brand names, numerals, URLs stay LTR/ASCII
"""

import os
import re
import json
import sys

BASE = "/home/user/workspace/1win-codes-repo"
EN_DIR = os.path.join(BASE, "en")
AR_DIR = os.path.join(BASE, "ar")

# Full hreflang block - these are the 46 locales + x-default required by the audit
# For AR pages, we point each locale to its own root (script generates page-specific URLs for en and ar)
ALL_LOCALES = ['ar','bg','bn','cs','da','de','el','en','es','et','fa','fi','fr',
               'he','hi','hr','hu','id','it','ja','kk','ko','lo','lt','lv','mn',
               'ms','mt','nb','nl','pl','pt','ro','ru','sk','sl','sq','sr','sv',
               'th','tl','tr','uk','ur','uz','vi','zh']

def build_hreflang_block(rel_path: str) -> str:
    """Build the full 46-locale hreflang block for an AR page."""
    # Derive path suffix (remove .html or index.html for URL)
    # e.g. index.html -> "" (just locale root)
    # e.g. casino.html -> "casino"
    # e.g. bonus/index.html -> "bonus/"
    # e.g. slots/sweet-bonanza.html -> "slots/sweet-bonanza"
    
    path = rel_path
    if path == 'index.html':
        url_suffix = ''
    elif path.endswith('/index.html'):
        url_suffix = path[:-len('index.html')]  # keep trailing slash
    elif path.endswith('.html'):
        url_suffix = path[:-5]  # remove .html
    else:
        url_suffix = path
    
    lines = []
    for loc in ALL_LOCALES:
        locale_url = f"https://1win.codes/{loc}/{url_suffix}"
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{locale_url}" />')
    # x-default points to EN
    en_url = f"https://1win.codes/en/{url_suffix}"
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{en_url}" />')
    return '\n'.join(lines)

def fix_dashes(content: str) -> str:
    """Replace em dashes (—) and en dashes (–) outside script/style tags."""
    parts = re.split(r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)', content, flags=re.DOTALL)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # Inside script or style - preserve
            result.append(part)
        else:
            part = part.replace('\u2014', '-')  # em dash
            part = part.replace('\u2013', '-')  # en dash
            result.append(part)
    return ''.join(result)

def fix_jsonld_urls(content: str, rel_path: str) -> str:
    """Fix URLs in JSON-LD blocks: /en/ → /ar/"""
    def replacer(m):
        block = m.group(0)
        block = re.sub(r'("url"\s*:\s*"https://1win\.codes)/en/', r'\1/ar/', block)
        block = re.sub(r'("target"\s*:\s*"https://1win\.codes)/en/', r'\1/ar/', block)
        return block
    return re.sub(r'<script type="application/ld\+json"[^>]*>.*?</script>', replacer, content, flags=re.DOTALL)

def inject_curacaoo_if_missing(content: str) -> str:
    """Ensure Curaçao 8048/JAZ appears in the page body text."""
    if '8048/JAZ' in content or 'Curaçao 8048' in content:
        return content
    # Also check for Curacao 8048 (without cedilla)
    if 'Curacao 8048' in content:
        # Fix the spelling
        content = content.replace('Curacao 8048', 'Curaçao 8048')
        return content
    
    # Find first <p> after <body that mentions 1win and inject licence reference
    body_start = content.find('<body')
    if body_start < 0:
        return content
    body_section = content[body_start:]
    
    # Find first paragraph with 1win or XLBONUS
    m = re.search(r'(<p[^>]*>)(.*?)(</p>)', body_section, flags=re.DOTALL)
    if m:
        para_open = m.group(1)
        para_text = m.group(2)
        para_close = m.group(3)
        old = m.group(0)
        # Add licence reference
        new_text = para_text.rstrip() + ' 1win مرخصة من كوراساو 8048/JAZ.'
        new = para_open + new_text + para_close
        content = content[:body_start] + content[body_start:].replace(old, new, 1)
    
    return content

# ─── Main translation function ────────────────────────────────────────────────

def full_translate(en_content: str, rel_path: str) -> str:
    """Full EN → AR translation of one HTML page."""
    content = en_content
    
    # 1. Fix <html> tag: add lang="ar" dir="rtl"
    content = re.sub(r'<html\s+lang="en">', '<html lang="ar" dir="rtl">', content)
    content = re.sub(r'<html\s+lang="en"\s+dir="[^"]*">', '<html lang="ar" dir="rtl">', content)
    
    # 2. Fix canonical: /en/ → /ar/
    content = re.sub(r'(rel="canonical"\s+href="https://1win\.codes)/en/', r'\1/ar/', content)
    
    # 3. Replace hreflang block entirely with full 46-locale block
    # Remove existing hreflang lines
    content = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?\s*>\n?', '', content)
    # Also handle without trailing slash in self-closing
    content = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/>\n?', '', content)
    
    # Insert hreflang block right after canonical
    new_hreflang = build_hreflang_block(rel_path)
    content = re.sub(
        r'(<link rel="canonical"[^>]*>)',
        r'\1\n' + new_hreflang,
        content
    )
    
    # 4. Fix internal navigation hrefs: /en/ → /ar/
    content = re.sub(r'href="/en/', 'href="/ar/', content)
    
    # 5. Fix JSON-LD URLs
    content = fix_jsonld_urls(content, rel_path)
    
    # 6. Fix em/en dashes
    content = fix_dashes(content)
    
    # 7. Translate text content
    content = translate_segments(content, rel_path)
    
    # 8. Ensure Curaçao 8048/JAZ present
    content = inject_curacaoo_if_missing(content)
    
    return content


def translate_segments(content: str, rel_path: str) -> str:
    """Translate HTML text segments (preserving script/style)."""
    # Split on script/style blocks
    segments = re.split(r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)', content, flags=re.DOTALL)
    
    translated = []
    for i, seg in enumerate(segments):
        if i % 2 == 1:  # script/style block - preserve entirely
            translated.append(seg)
        else:
            seg = translate_html_segment(seg, rel_path)
            translated.append(seg)
    
    return ''.join(translated)


def translate_html_segment(seg: str, rel_path: str) -> str:
    """Apply AR translations to an HTML segment."""
    
    # ── aria-label attributes ──
    seg = seg.replace('aria-label="1win home"', 'aria-label="الصفحة الرئيسية لـ 1win"')
    seg = seg.replace('aria-label="Sign Up"', 'aria-label="سجّل"')
    seg = seg.replace('aria-label="Toggle menu"', 'aria-label="تبديل القائمة"')
    seg = seg.replace('aria-label="Language"', 'aria-label="اللغة"')
    seg = seg.replace('aria-label="Back to top"', 'aria-label="العودة إلى الأعلى"')
    seg = seg.replace('aria-label="Go to top"', 'aria-label="انتقل إلى الأعلى"')
    seg = seg.replace('aria-label="Close"', 'aria-label="إغلاق"')
    seg = seg.replace('aria-label="Search"', 'aria-label="بحث"')
    
    # ── lang option label ──
    seg = re.sub(r'>EN<(?=/option>|</)', '>AR<', seg)
    
    # ── Navigation links (text only, inside > < ) ──
    nav_replacements = [
        ('>Promo Code<', '>الرمز الترويجي<'),
        ('>All sports betting<', '>جميع المراهنات الرياضية<'),
        ('>Football<', '>كرة القدم<'),
        ('>Cricket<', '>الكريكيت<'),
        ('>Tennis<', '>التنس<'),
        ('>Basketball<', '>كرة السلة<'),
        ('>Esports<', '>الرياضات الإلكترونية<'),
        ('>Live streaming<', '>البث المباشر<'),
        ('>Casino home<', '>الكازينو<'),
        ('>Slot reviews<', '>مراجعات السلوت<'),
        ('>Game providers<', '>مزودو الألعاب<'),
        ('>Crash games<', '>ألعاب Crash<'),
        ('>Poker<', '>البوكر<'),
        ('>All bonuses<', '>جميع المكافآت<'),
        ('>First deposit 200%<', '>الإيداع الأول 200%<'),
        ('>Second deposit 150%<', '>الإيداع الثاني 150%<'),
        ('>Third deposit 150%<', '>الإيداع الثالث 150%<'),
        ('>Fourth deposit 100%<', '>الإيداع الرابع 100%<'),
        ('>Wagering rules<', '>شروط المراهنة<'),
        ('>Free spins today<', '>لفات مجانية اليوم<'),
        ('>Cashback<', '>استرداد نقدي<'),
        ('>VIP club<', '>نادي VIP<'),
        ('>Lucky Drive<', '>Lucky Drive<'),
        ('>All promotions<', '>جميع العروض<'),
        ('>All calculators<', '>جميع الآلات الحاسبة<'),
        ('>Odds converter<', '>محول الأوزان<'),
        ('>Parlay calculator<', '>حاسبة البارلاي<'),
        ('>Kelly criterion<', '>معيار Kelly<'),
        ('>Arbitrage<', '>المراجحة<'),
        ('>Hedge<', '>التحوط<'),
        ('>Each-way<', '>رهان المسار الزوجي<'),
        ('>Implied probability<', '>الاحتمالية الضمنية<'),
        ('>Bankroll<', '>إدارة رأس المال<'),
        ('>Surebet<', '>Surebet<'),
        ('>Matched bet<', '>الرهان المطابق<'),
        ('>Payment methods<', '>طرق الدفع<'),
        ('>Mobile app<', '>تطبيق الجوال<'),
        ('>India guides<', '>أدلة الهند<'),
        ('>Mirrors<', '>الروابط البديلة<'),
        ('>Login<', '>تسجيل الدخول<'),
        ('>Register<', '>سجّل<'),
        ('>Review<', '>المراجعة<'),
        ('>About 1win<', '>عن 1win<'),
        ('>FAQ<', '>الأسئلة الشائعة<'),
        ('>News<', '>الأخبار<'),
        ('>Home<', '>الرئيسية<'),
        # CTA buttons
        ('>Register at 1win<', '>سجّل في 1win<'),
        ('>Sign Up<', '>سجّل الآن<'),
        ('>Claim Promo Code →<', '>احصل على الرمز الترويجي →<'),
        ('>Access 1win Registration<', '>الوصول إلى تسجيل 1win<'),
        ('>Get Started<', '>ابدأ الآن<'),
        ('>Play Now<', '>العب الآن<'),
        ('>Claim Now<', '>احصل الآن<'),
        ('>Open Account<', '>افتح حساباً<'),
        ('>Deposit Now<', '>أودع الآن<'),
        ('>Learn more<', '>تعرف على المزيد<'),
        ('>See all<', '>عرض الكل<'),
        ('>Back to top<', '>العودة للأعلى<'),
        ('>Share<', '>مشاركة<'),
    ]
    
    for en_text, ar_text in nav_replacements:
        seg = seg.replace(en_text, ar_text)
    
    # Nav items with SVG chevron (dropdown toggles)
    seg = re.sub(r'>Sports(\s+<svg)', r'>الرياضات\1', seg)
    seg = re.sub(r'>Casino(\s+<svg)', r'>الكازينو\1', seg)
    seg = re.sub(r'>Bonuses(\s+<svg)', r'>المكافآت\1', seg)
    seg = re.sub(r'>Tools(\s+<svg)', r'>الأدوات\1', seg)
    seg = re.sub(r'>More(\s+<svg)', r'>المزيد\1', seg)
    seg = re.sub(r'>Aviator(\s*<)', r'>Aviator\1', seg)
    
    # ── Footer ──
    seg = seg.replace('>Quick Links<', '>روابط سريعة<')
    seg = seg.replace('>Legal<', '>قانوني<')
    seg = seg.replace('>Privacy Policy<', '>سياسة الخصوصية<')
    seg = seg.replace('>Terms of Service<', '>شروط الخدمة<')
    seg = seg.replace('>Responsible Gaming<', '>اللعب المسؤول<')
    seg = seg.replace('>Disclaimer<', '>إخلاء المسؤولية<')
    seg = seg.replace('>18+ only<', '>18+ فقط<')
    seg = seg.replace('>© 2026 1win.codes<', '>© 2026 1win.codes<')
    seg = seg.replace('>All Rights Reserved<', '>جميع الحقوق محفوظة<')
    seg = seg.replace('>All rights reserved<', '>جميع الحقوق محفوظة<')
    
    # ── Common stat bar / feature labels ──
    seg = seg.replace('>Bonus<', '>مكافأة<')
    seg = seg.replace('>Sports<', '>رياضات<')
    seg = seg.replace('>Games<', '>ألعاب<')
    seg = seg.replace('>Instant Crypto<', '>تشفير فوري<')
    
    # Table headers
    seg = seg.replace('>Feature<', '>الميزة<')
    seg = seg.replace('>Details<', '>التفاصيل<')
    seg = seg.replace('>Yes<', '>نعم<')
    seg = seg.replace('>No<', '>لا<')
    seg = seg.replace('>Available<', '>متاح<')
    seg = seg.replace('>Not available<', '>غير متاح<')
    
    # Misc UI
    seg = seg.replace('>Last updated<', '>آخر تحديث<')
    seg = seg.replace('>Reading time<', '>وقت القراءة<')
    seg = seg.replace('>min read<', '>دقيقة قراءة<')
    seg = seg.replace('>Table of Contents<', '>جدول المحتويات<')
    
    # ── Apply page-specific text translations ──
    seg = apply_body_translations(seg)
    
    return seg


# ─── Comprehensive body text translations ────────────────────────────────────

BODY_TRANSLATIONS = [
    # ── Index / Hero ──
    ("1win Promo Code XLBONUS, 600% Welcome Bonus (2026)",
     "رمز 1win الترويجي XLBONUS - مكافأة ترحيب 600% (2026)"),
    ("Get a 600% welcome bonus on your first four deposits at 1win with promo code XLBONUS.",
     "احصل على مكافأة ترحيب 600% على إيداعاتك الأربعة الأولى في 1win باستخدام الرمز الترويجي XLBONUS."),
    ("30+ sports, 11,000+ casino games, Aviator, crypto payouts in 4 hours average. Curaçao licensed.",
     "أكثر من 30 رياضة، أكثر من 11,000 لعبة كازينو، Aviator، ومدفوعات مشفرة في غضون 4 ساعات في المتوسط. مرخصة من كوراساو."),
    ("Use 1win promo code XLBONUS to unlock a 600% welcome bonus across your first 4 deposits.",
     "استخدم رمز 1win الترويجي XLBONUS للحصول على مكافأة ترحيب 600% على أول 4 إيداعات."),
    ("Sign up today and start winning on sports, casino, and Aviator.",
     "سجّل اليوم وابدأ الفوز في الرياضة والكازينو وAviator."),
    ("Claim Promo Code", "احصل على الرمز الترويجي"),
    ("600% Welcome Bonus", "مكافأة ترحيب 600%"),
    ("Welcome Bonus", "مكافأة الترحيب"),
    ("First Deposit Bonus", "مكافأة الإيداع الأول"),
    ("Second Deposit Bonus", "مكافأة الإيداع الثاني"),
    ("Third Deposit Bonus", "مكافأة الإيداع الثالث"),
    ("Fourth Deposit Bonus", "مكافأة الإيداع الرابع"),
    
    # ── Stats ──
    ("30+ Sports", "أكثر من 30 رياضة"),
    ("11,000+ Casino Games", "أكثر من 11,000 لعبة كازينو"),
    ("12,000+ Slots", "أكثر من 12,000 سلوت"),
    ("40,000+ Markets", "أكثر من 40,000 سوق"),
    ("400,000+ Players", "أكثر من 400,000 لاعب"),
    ("4-Hour Crypto", "تشفير 4 ساعات"),
    
    # ── Common phrases ──
    ("Curaçao 8048/JAZ", "Curaçao 8048/JAZ"),  # preserve
    ("Curacao 8048/JAZ", "Curaçao 8048/JAZ"),   # fix spelling
    ("Licensed by Curaçao", "مرخصة من كوراساو"),
    ("licensed by Curaçao 8048/JAZ", "مرخصة من كوراساو 8048/JAZ"),
    ("Curaçao licensed", "مرخصة من كوراساو 8048/JAZ"),
    ("Curacao licensed", "مرخصة من كوراساو 8048/JAZ"),
    ("18+ only. Gambling can be addictive. Play responsibly.",
     "18+ فقط. قد تكون المراهنة مدمنة. العب بمسؤولية."),
    ("18+ Gambling involves risk. Play responsibly.",
     "18+ المراهنة تنطوي على مخاطر. العب بمسؤولية."),
    ("Gambling involves risk. Play responsibly.",
     "المراهنة تنطوي على مخاطر. العب بمسؤولية."),
    ("Play responsibly.", "العب بمسؤولية."),
    ("Play responsibly", "العب بمسؤولية"),
    
    # ── Sports betting ──
    ("Sports Betting", "المراهنات الرياضية"),
    ("sports betting", "المراهنات الرياضية"),
    ("Football Betting", "المراهنة على كرة القدم"),
    ("Cricket Betting", "المراهنة على الكريكيت"),
    ("Basketball Betting", "المراهنة على كرة السلة"),
    ("Tennis Betting", "المراهنة على التنس"),
    ("Esports Betting", "المراهنة على الرياضات الإلكترونية"),
    ("Live Betting", "الرهان المباشر"),
    ("live betting", "الرهان المباشر"),
    ("In-Play Betting", "الرهان أثناء المباراة"),
    ("Pre-match", "قبل المباراة"),
    ("In-play", "أثناء اللعب"),
    ("Odds", "أوزان الرهان"),
    ("Markets", "الأسواق"),
    ("markets", "الأسواق"),
    
    # ── Casino ──
    ("Casino", "كازينو على الإنترنت"),
    ("Online Casino", "كازينو على الإنترنت"),
    ("Live Casino", "كازينو مباشر"),
    ("Slot", "سلوت"),
    ("Slots", "سلوت"),
    ("Table Games", "ألعاب الطاولة"),
    ("Roulette", "روليت"),
    ("Blackjack", "بلاك جاك"),
    ("Baccarat", "باكارا"),
    ("Game Providers", "مزودو الألعاب"),
    ("game providers", "مزودو الألعاب"),
    
    # ── Bonuses ──
    ("Promo Code", "الرمز الترويجي"),
    ("promo code", "الرمز الترويجي"),
    ("Promotional Code", "الرمز الترويجي"),
    ("Bonus Code", "رمز المكافأة"),
    ("bonus code", "رمز المكافأة"),
    ("Welcome Offer", "عرض الترحيب"),
    ("Deposit Bonus", "مكافأة الإيداع"),
    ("Free Spins", "لفات مجانية"),
    ("free spins", "لفات مجانية"),
    ("Cashback", "استرداد نقدي"),
    ("cashback", "استرداد نقدي"),
    ("Wagering Requirements", "شروط المراهنة"),
    ("wagering requirements", "شروط المراهنة"),
    ("wagering requirement", "شرط المراهنة"),
    ("Wagering Requirement", "شرط المراهنة"),
    ("Rollover", "شرط التحويل"),
    ("rollover", "شرط التحويل"),
    ("No Deposit", "بدون إيداع"),
    ("Min Deposit", "الحد الأدنى للإيداع"),
    ("Maximum Bonus", "الحد الأقصى للمكافأة"),
    ("Bonus Terms", "شروط المكافأة"),
    
    # ── Payments ──
    ("Payment Methods", "طرق الدفع"),
    ("payment methods", "طرق الدفع"),
    ("Deposit", "الإيداع"),
    ("Withdrawal", "السحب"),
    ("withdrawal", "السحب"),
    ("Crypto", "تشفير"),
    ("cryptocurrency", "عملة مشفرة"),
    ("Cryptocurrency", "عملة مشفرة"),
    ("Bitcoin", "Bitcoin"),
    ("Ethereum", "Ethereum"),
    ("USDT", "USDT"),
    ("Litecoin", "Litecoin"),
    ("Processing Time", "وقت المعالجة"),
    ("processing time", "وقت المعالجة"),
    ("Instant", "فوري"),
    ("instant", "فوري"),
    ("Hours", "ساعات"),
    ("hours", "ساعات"),
    ("Minutes", "دقائق"),
    ("minutes", "دقائق"),
    ("Fees", "رسوم"),
    ("No fees", "بدون رسوم"),
    ("Zero fees", "بدون رسوم"),
    
    # ── App ──
    ("Mobile App", "تطبيق الجوال"),
    ("mobile app", "تطبيق الجوال"),
    ("Download", "تنزيل"),
    ("download", "تنزيل"),
    ("Android", "Android"),
    ("iOS", "iOS"),
    ("APK", "APK"),
    
    # ── Register / Account ──
    ("Registration", "التسجيل"),
    ("registration", "التسجيل"),
    ("Sign Up", "سجّل"),
    ("sign up", "سجّل"),
    ("Login", "تسجيل الدخول"),
    ("Log In", "تسجيل الدخول"),
    ("Password", "كلمة المرور"),
    ("Email", "البريد الإلكتروني"),
    ("Username", "اسم المستخدم"),
    ("Account", "الحساب"),
    ("Verification", "التحقق"),
    
    # ── VIP ──
    ("VIP Club", "نادي VIP"),
    ("VIP Program", "برنامج VIP"),
    ("Points", "نقاط"),
    ("Loyalty", "الولاء"),
    ("Rank", "المرتبة"),
    
    # ── News ──
    ("News", "الأخبار"),
    ("Latest News", "آخر الأخبار"),
    ("Update", "تحديث"),
    ("announcement", "إعلان"),
    ("Announcement", "إعلان"),
    
    # ── Tools / Calculators ──
    ("Odds Converter", "محول الأوزان"),
    ("Parlay Calculator", "حاسبة البارلاي"),
    ("Kelly Criterion Calculator", "حاسبة معيار Kelly"),
    ("Arbitrage Calculator", "حاسبة المراجحة"),
    ("Hedge Calculator", "حاسبة التحوط"),
    ("Each-Way Calculator", "حاسبة المسار الزوجي"),
    ("Implied Probability Calculator", "حاسبة الاحتمالية الضمنية"),
    ("Bankroll Calculator", "حاسبة رأس المال"),
    ("Surebet Calculator", "حاسبة Surebet"),
    ("Matched Bet Calculator", "حاسبة الرهان المطابق"),
    ("Betting Tools", "أدوات الرهان"),
    ("Calculate", "احسب"),
    ("Result", "النتيجة"),
    ("Stake", "رهان"),
    ("Return", "العائد"),
    ("Profit", "الربح"),
    ("Total", "الإجمالي"),
    
    # ── Countries ──
    ("Bangladesh", "بنغلاديش"),
    ("Brazil", "البرازيل"),
    ("Ghana", "غانا"),
    ("India", "الهند"),
    ("Kenya", "كينيا"),
    ("Korea", "كوريا"),
    ("Malawi", "ملاوي"),
    ("Malaysia", "ماليزيا"),
    ("Pakistan", "باكستان"),
    ("Russia", "روسيا"),
    ("Singapore", "سنغافورة"),
    ("South Africa", "جنوب أفريقيا"),
    ("Tanzania", "تنزانيا"),
    ("Turkey", "تركيا"),
    ("Vietnam", "فيتنام"),
    ("Indonesia", "إندونيسيا"),
    ("Kazakhstan", "كازاخستان"),
    ("Gambia", "غامبيا"),
    ("Costa Rica", "كوستاريكا"),
    ("Tajikistan", "طاجيكستان"),
    ("Uzbekistan", "أوزبكستان"),
    
    # ── Crash Games ──
    ("Crash Games", "ألعاب Crash"),
    ("crash games", "ألعاب Crash"),
    ("Crash Game", "لعبة Crash"),
    
    # ── Common UI / descriptive ──
    ("How to", "كيفية"),
    ("Step by step", "خطوة بخطوة"),
    ("Step-by-step", "خطوة بخطوة"),
    ("Guide", "دليل"),
    ("guide", "دليل"),
    ("Review", "مراجعة"),
    ("review", "مراجعة"),
    ("Overview", "نظرة عامة"),
    ("FAQ", "الأسئلة الشائعة"),
    ("Frequently Asked Questions", "الأسئلة الشائعة"),
    ("Conclusion", "الخلاصة"),
    ("Summary", "الملخص"),
    ("Introduction", "المقدمة"),
    ("Key Features", "الميزات الرئيسية"),
    ("key features", "الميزات الرئيسية"),
    ("Benefits", "المزايا"),
    ("benefits", "المزايا"),
    ("Pros", "المزايا"),
    ("Cons", "العيوب"),
    ("Min", "الحد الأدنى"),
    ("Max", "الحد الأقصى"),
    ("Per day", "يومياً"),
    ("per day", "يومياً"),
    ("Per week", "أسبوعياً"),
    ("per week", "أسبوعياً"),
    ("Per month", "شهرياً"),
    ("per month", "شهرياً"),
    ("days", "أيام"),
    ("hours", "ساعات"),
    ("minutes", "دقائق"),
    ("seconds", "ثوان"),
    ("Read more", "اقرأ المزيد"),
    ("read more", "اقرأ المزيد"),
    ("See more", "شاهد المزيد"),
    ("Updated", "محدث"),
    ("updated", "محدث"),
    ("Published", "منشور"),
    ("published", "منشور"),
    ("Author", "الكاتب"),
    ("Category", "الفئة"),
    ("Tags", "وسوم"),
    ("Related", "ذات الصلة"),
    ("Next", "التالي"),
    ("Previous", "السابق"),
    ("Back", "رجوع"),
    ("Continue", "متابعة"),
    ("Submit", "إرسال"),
    ("Cancel", "إلغاء"),
    ("Close", "إغلاق"),
    ("Open", "افتح"),
    ("copy", "نسخ"),
    ("Copy", "نسخ"),
    ("Copied!", "تم النسخ!"),
    ("copied", "تم النسخ"),
    
    # ── Sports specific ──
    ("Premier League", "Premier League"),
    ("Champions League", "Champions League"),
    ("La Liga", "La Liga"),
    ("Serie A", "Serie A"),
    ("Bundesliga", "Bundesliga"),
    ("Ligue 1", "Ligue 1"),
    ("IPL", "IPL"),
    ("match", "مباراة"),
    ("Match", "مباراة"),
    ("tournament", "بطولة"),
    ("Tournament", "بطولة"),
    ("league", "دوري"),
    ("League", "دوري"),
    ("season", "موسم"),
    ("team", "فريق"),
    # ("player", "لاعب"),  # REMOVED: breaks player in compound words
    # ("goal", "هدف"),  # REMOVED: too generic
    # ("win", "فوز"),  # REMOVED: would break '1win' brand name!
    # ("draw", "تعادل"),  # REMOVED: too generic  
    # ("loss", "خسارة"),  # REMOVED: too generic
    
    # ── India states ──
    ("Andhra Pradesh", "آندهرا براديش"),
    ("Delhi", "دلهي"),
    ("Gujarat", "غوجارات"),
    ("Karnataka", "كارناتاكا"),
    ("Kerala", "كيرالا"),
    ("Maharashtra", "مهاراشترا"),
    ("Punjab", "البنجاب"),
    ("Rajasthan", "راجستان"),
    ("Tamil Nadu", "تاميل نادو"),
    ("Telangana", "تيلانغانا"),
    ("Uttar Pradesh", "أوتار براديش"),
    ("West Bengal", "بنغال الغربية"),
    
    # ── Meta descriptions / titles ──
    ("1win Promo Code", "رمز 1win الترويجي"),
    ("with promo code XLBONUS", "باستخدام الرمز الترويجي XLBONUS"),
    ("Use promo code XLBONUS", "استخدم الرمز الترويجي XLBONUS"),
    ("Enter promo code XLBONUS", "أدخل الرمز الترويجي XLBONUS"),
    ("Apply promo code XLBONUS", "طبّق الرمز الترويجي XLBONUS"),
    ("welcome bonus", "مكافأة الترحيب"),
    ("Welcome Bonus", "مكافأة الترحيب"),
    ("at registration", "عند التسجيل"),
    ("during registration", "أثناء التسجيل"),
    ("on registration", "عند التسجيل"),
    ("on your first deposit", "على إيداعك الأول"),
    ("on the first deposit", "على الإيداع الأول"),
    ("across 4 deposits", "على 4 إيداعات"),
    ("across your first 4 deposits", "على أول 4 إيداعات"),
    ("first 4 deposits", "أول 4 إيداعات"),
    ("4 deposits", "4 إيداعات"),
    ("35x wagering", "35 مرة متطلبات الرهان"),
    ("30 days", "30 يوماً"),
    ("per stage", "لكل مرحلة"),
    ("today", "اليوم"),
    ("Today", "اليوم"),
    ("now", "الآن"),
    ("Now", "الآن"),
    ("free", "مجاني"),
    ("Free", "مجاني"),
    ("new", "جديد"),
    ("New", "جديد"),
    ("best", "أفضل"),
    ("Best", "أفضل"),
    ("top", "أعلى"),
    ("Top", "أعلى"),
    ("latest", "أحدث"),
    ("Latest", "أحدث"),
    ("full", "كامل"),
    ("Full", "كامل"),
    ("complete", "كامل"),
    ("Complete", "كامل"),
    ("official", "رسمي"),
    ("Official", "رسمي"),
    ("exclusive", "حصري"),
    ("Exclusive", "حصري"),
    ("special", "خاص"),
    ("Special", "خاص"),
    ("limited", "محدود"),
    ("Limited", "محدود"),
    ("valid", "صالح"),
    ("Valid", "صالح"),
    ("expires", "ينتهي"),
    ("Expires", "ينتهي"),
    ("active", "نشط"),
    ("Active", "نشط"),
    ("verified", "موثق"),
    ("Verified", "موثق"),
    ("trusted", "موثوق"),
    ("Trusted", "موثوق"),
    ("safe", "آمن"),
    ("Safe", "آمن"),
    ("secure", "آمن"),
    ("Secure", "آمن"),
    ("fast", "سريع"),
    ("Fast", "سريع"),
    ("quick", "سريع"),
    ("Quick", "سريع"),
    ("easy", "سهل"),
    ("Easy", "سهل"),
    ("simple", "بسيط"),
    ("Simple", "بسيط"),
    ("available", "متاح"),
    ("Available", "متاح"),
    ("supported", "مدعوم"),
    ("Supported", "مدعوم"),
    ("required", "مطلوب"),
    ("Required", "مطلوب"),
    ("optional", "اختياري"),
    ("Optional", "اختياري"),
    ("minimum", "الحد الأدنى"),
    ("Minimum", "الحد الأدنى"),
    ("maximum", "الحد الأقصى"),
    ("Maximum", "الحد الأقصى"),
    ("per bet", "لكل رهان"),
    ("per spin", "لكل لفة"),
    ("winnings", "الأرباح"),
    ("earnings", "الأرباح"),
    ("balance", "الرصيد"),
    ("Balance", "الرصيد"),
    ("funds", "الأموال"),
    ("Funds", "الأموال"),
    ("amount", "المبلغ"),
    ("Amount", "المبلغ"),
    ("currency", "العملة"),
    ("Currency", "العملة"),
    
    # Specific page text patterns
    ("How to use the XLBONUS promo code at 1win",
     "كيفية استخدام الرمز الترويجي XLBONUS في 1win"),
    ("How to register at 1win",
     "كيفية التسجيل في 1win"),
    ("How to get your bonus",
     "كيفية الحصول على مكافأتك"),
    ("Step 1", "الخطوة 1"),
    ("Step 2", "الخطوة 2"),
    ("Step 3", "الخطوة 3"),
    ("Step 4", "الخطوة 4"),
    ("Step 5", "الخطوة 5"),
    ("Click here", "انقر هنا"),
    ("click here", "انقر هنا"),
    
    # Provider page headings (keep provider names)
    ("BGaming slots at 1win", "سلوت BGaming في 1win"),
    ("Evolution Gaming at 1win", "Evolution Gaming في 1win"),
    ("Hacksaw Gaming at 1win", "Hacksaw Gaming في 1win"),
    ("NetEnt slots at 1win", "سلوت NetEnt في 1win"),
    ("Play'n GO at 1win", "Play'n GO في 1win"),
    ("Pragmatic Play at 1win", "Pragmatic Play في 1win"),
    ("Relax Gaming at 1win", "Relax Gaming في 1win"),
    ("Spribe games at 1win", "ألعاب Spribe في 1win"),
    
    # Slot page headings
    ("Play", "العب"),
    ("play", "العب"),
    ("at 1win", "في 1win"),
    ("on 1win", "على 1win"),
    ("Return to Player", "العائد للاعب"),
    ("RTP", "RTP"),
    ("Volatility", "التقلب"),
    ("volatility", "التقلب"),
    ("High", "عالٍ"),
    ("Medium", "متوسط"),
    ("Low", "منخفض"),
    ("Paylines", "خطوط الدفع"),
    ("paylines", "خطوط الدفع"),
    ("Reels", "بكرات"),
    ("reels", "بكرات"),
    ("Wild", "Wild"),
    ("Scatter", "Scatter"),
    ("Bonus Round", "جولة المكافآت"),
    ("Free Spins Feature", "ميزة اللفات المجانية"),
    ("Jackpot", "جائزة كبرى"),
    ("jackpot", "جائزة كبرى"),
    ("Multiplier", "مضاعف"),
    ("multiplier", "مضاعف"),
    
    # sports tips pages
    ("Football Tips", "نصائح كرة القدم"),
    ("Cricket Tips", "نصائح الكريكيت"),
    ("Basketball Tips", "نصائح كرة السلة"),
    ("Tennis Tips", "نصائح التنس"),
    ("Esports Tips", "نصائح الرياضات الإلكترونية"),
    ("Today's Tips", "نصائح اليوم"),
    ("Today's Football", "كرة القدم اليوم"),
    ("Today's Cricket", "الكريكيت اليوم"),
    ("Today's Basketball", "كرة السلة اليوم"),
    ("Today's Tennis", "التنس اليوم"),
    ("Today's Esports", "الرياضات الإلكترونية اليوم"),
    ("Betting Tips", "نصائح الرهان"),
    ("betting tips", "نصائح الرهان"),
    ("Prediction", "توقع"),
    ("Predictions", "توقعات"),
    ("prediction", "توقع"),
    ("predictions", "توقعات"),
    ("Analysis", "تحليل"),
    ("analysis", "تحليل"),
    ("Pick", "اختيار"),
    ("Picks", "اختيارات"),
    
    # Live streaming
    ("Live Streaming", "البث المباشر"),
    ("live streaming", "البث المباشر"),
    ("stream", "بث"),
    ("Stream", "بث"),
    ("Watch", "شاهد"),
    ("watch", "شاهد"),
    ("broadcast", "بث"),
    
    # alternative link/mirror
    ("Alternative Link", "الرابط البديل"),
    ("alternative link", "الرابط البديل"),
    ("Mirror", "نسخة مرآة"),
    ("Mirrors", "الروابط البديلة"),
    ("Access", "الوصول"),
    ("access", "الوصول"),
    ("Blocked", "محجوب"),
    ("blocked", "محجوب"),
    ("Unblock", "إلغاء الحجب"),
    ("VPN", "VPN"),
    ("bypass", "تجاوز"),
    ("Bypass", "تجاوز"),
    
    # Common sentence structures
    ("1win is licensed by", "1win مرخصة من"),
    ("licensed under", "مرخصة بموجب"),
    ("operating under", "تعمل بموجب"),
    ("regulated by", "خاضعة لتنظيم"),
    
    # Poker
    ("Poker", "البوكر"),
    ("poker", "البوكر"),
    ("Freeroll", "بطولة مجانية"),
    ("freeroll", "بطولة مجانية"),
    ("Texas Hold'em", "Texas Hold'em"),
    ("Omaha", "Omaha"),
    ("Tournament", "بطولة"),
    ("tournament", "بطولة"),
    ("Buy-in", "رسوم الاشتراك"),
    
    # Promotions
    ("Promotions", "العروض"),
    ("promotions", "العروض"),
    ("promotion", "عرض"),
    ("Promotion", "عرض"),
    ("offer", "عرض"),
    ("Offer", "عرض"),
    ("deal", "صفقة"),
    ("Deal", "صفقة"),
    ("reward", "مكافأة"),
    ("Reward", "مكافأة"),
    ("loyalty", "الولاء"),
    ("Loyalty", "الولاء"),
    
    # ── Common body paragraph phrases ──
    ("Code XLBONUS stacks a 200% + 150% + 100% + 50% bonus across your first four deposits.",
     "الرمز XLBONUS يضم مكافأة 200% + 150% + 100% + 50% على إيداعاتك الأربعة الأولى."),
    ("1win covers 30+ sports and 11,000+ casino games. Curaçao-licensed (8048/JAZ). 600% total, auto-activated.",
     "1win تغطي أكثر من 30 رياضة و 11,000+ لعبة كازينو. مرخصة من كوراساو 8048/JAZ. 600% إجمالاً، تفعيل تلقائي."),
    ("1win covers 30+ sports with 1,000+ daily markets, live in-play betting with cash-out on every selection, and free streams on selected football and tennis matches. Curaçao-licensed (8048/JAZ), founded 2018.",
     "1win تغطي أكثر من 30 رياضة مع أكثر من 1,000 سوق يومي، ورهان مباشر مع خيار السحب على كل رهان، وبث مجاني لمباريات مختارة. مرخصة من كوراساو 8048/JAZ، تأسست 2018."),
    ("11,000+ casino games from 70+ providers including Pragmatic Play, Evolution, NetEnt and Spribe. Live dealer tables 24/7. Daily drops and tournaments worth $50,000+ a week.",
     "11,000+ لعبة كازينو من 70+ مزوداً بما فيهم Pragmatic Play وEvolution وNetEnt وSpribe. طاولات كازينو مباشر 24/7. جوائز يومية وبطولات بقيمة $50,000+ أسبوعياً."),
    ("Use promo code XLBONUS when registering to get the biggest available welcome bonus. Up to 600% across four deposits.",
     "استخدم الرمز الترويجي XLBONUS عند التسجيل للحصول على أكبر مكافأة ترحيب. حتى 600% على أربعة إيداعات."),
    ("1win is a globally accessible sportsbook and casino, operating under Curaçao licence 8048/JAZ.",
     "1win منصة مراهنات رياضية وكازينو متاحة عالمياً، تعمل بموجب ترخيص كوراساو 8048/JAZ."),
    ("New players use promo code XLBONUS to unlock a 600% welcome bonus across four deposits",
     "يستخدم اللاعبون الجدد الرمز الترويجي XLBONUS للحصول على مكافأة ترحيب 600% على أربعة إيداعات"),
    ("Register with the code to get one of the largest bonus offers found at any online betting site anywhere in the world!",
     "سجّل بالرمز للحصول على واحدة من أكبر عروض المكافآت في أي موقع مراهنات عبر الإنترنت!"),
    ("Fill in the short registration form. When asked if you have a promo code, type in the XLBONUS code.",
     "املأ نموذج التسجيل المختصر. عندما يُسأل عن الرمز الترويجي، اكتب XLBONUS."),
    ("Make your first deposit. A 130% first deposit bonus is available with XLBONUS, with further bonuses on deposits 2 to 4.",
     "أجرِ إيداعك الأول. مكافأة إيداع 130% متاحة مع XLBONUS، مع مكافآت إضافية على الإيداعات 2 إلى 4."),
    ("The first part of your 600% bonus package will be credited to your account. Start playing!",
     "سيُضاف الجزء الأول من حزمة مكافأت 600% إلى حسابك. ابدأ اللعب!"),
    ("Four deposits. Each one supercharged. Here's exactly how the 600% total bonus works with crypto deposits.",
     "أربعة إيداعات. كل واحدة مضاعفة. هكذا تعمل مكافأة 600% الإجمالية مع الإيداعات المشفرة."),
    ("18+ only. New customers only. Terms and conditions apply. Gamble responsibly.",
     "18+ فقط. للعملاء الجدد فقط. تسري الشروط والأحكام. العب بمسؤولية."),
    ("Sports Betting, Casino, Live Casino, Aviator, Poker, Lucky Drive, Games",
     "المراهنات الرياضية، كازينو، كازينو مباشر، Aviator، بوكر، Lucky Drive، ألعاب"),
    ("Fund your account with cards, e-wallets, or crypto. Fast, secure and borderless.",
     "موّل حسابك ببطاقات الدفع أو المحافظ الإلكترونية أو العملات المشفرة. سريع، آمن، وبدون حدود."),
    ("Exclusive tournaments, cash bonuses, and limited-time offers, updated regularly.",
     "بطولات حصرية ومكافآت نقدية وعروض لفترة محدودة، تُحدّث بانتظام."),
    ("1win is available in 15 languages. Bet on 30+ sports and play 11,000+ casino games from anywhere.",
     "1win متاحة بـ 15 لغة. راهن على 30+ رياضة والعب 11,000+ لعبة كازينو من أي مكان."),
    ("18+ | T&amp;C Apply | Play Responsibly.",
     "18+ | تسري الشروط | العب بمسؤولية."),
    ("18+ | T&C Apply | Play Responsibly.",
     "18+ | تسري الشروط | العب بمسؤولية."),
    ("Deposit and claim your free ticket daily. Monthly luxury car draws await.",
     "أودع واحصل على تذكرتك المجانية يومياً. سحبات سيارات فاخرة شهرية بانتظارك."),
    ("This is an unofficial fan site and is not affiliated with or endorsed by 1win.",
     "هذا موقع غير رسمي وليس تابعاً أو معتمداً من 1win."),
    ("Gambling involves risk, please play responsibly.",
     "المراهنة تنطوي على مخاطر، الرجاء اللعب بمسؤولية."),
    ("This site is for informational purposes only.",
     "هذا الموقع لأغراض معلوماتية فقط."),
    ("© 2026 1win.codes. All rights reserved.",
     "© 2026 1win.codes. جميع الحقوق محفوظة."),
    # Sports betting body text
    ("30+ sports. 1,000+ daily markets. Live in-play on every match with cash-out and free streaming on selected football and tennis fixtures. 1win is Curaçao-licensed (8048/JAZ). Welcome bonus 600% with co",
     "30+ رياضة. 1,000+ سوق يومي. رهان مباشر على كل مباراة مع سحب وبث مجاني. 1win مرخصة من كوراساو 8048/JAZ. مكافأة ترحيب 600%"),
    ("From the world's biggest leagues to underground fight cards, every sport, every market, every edge.",
     "من أكبر الدوريات العالمية إلى تصفيات الملاكمة السرية، كل رياضة وكل سوق وكل ميزة."),
    ("Create your 1win account in 30 seconds. Enter promo code XLBONUS for 600% bonus. Deposit with card or crypto.",
     "أنشئ حسابك في 1win خلال 30 ثانية. أدخل الرمز الترويجي XLBONUS للحصول على مكافأة 600%. أودع ببطاقة أو عملة مشفرة."),
    ("Browse 30+ sports, find your match, and select your market. Pre-match or live, the choice is yours.",
     "تصفح 30+ رياضة، ابحث عن مباراتك، واختر سوقك. قبل المباراة أو مباشرة، الخيار لك."),
    ("Enter your stake, confirm your bet, and watch the action. Cash out anytime or ride it to the final whistle.",
     "أدخل رهانك، أكد رهانك، وشاهد المجريات. اسحب في أي وقت أو انتظر حتى الصافرة الأخيرة."),
    # Common footer/disclaimer  
    ("1win.codes - independent affiliate review",
     "1win.codes - مراجعة شريك تسويق مستقلة"),
    ("All rights reserved.", "جميع الحقوق محفوظة."),
    ("All Rights Reserved.", "جميع الحقوق محفوظة."),
    # Casino body text
    ("Play 11,000+ slots, live dealer tables, and jackpots at 1win Casino.",
     "العب 11,000+ سلوت وطاولات كازينو مباشر وجوائز كبرى في كازينو 1win."),
    ("Enter promo code XLBONUS to collect your 600% welcome bonus and start winning today.",
     "أدخل الرمز الترويجي XLBONUS للحصول على مكافأة الترحيب 600% وابدأ الفوز اليوم."),
    ("Play casino games at 1win using promo code XLBONUS.",
     "العب ألعاب الكازينو في 1win باستخدام الرمز الترويجي XLBONUS."),
    # Activation steps
    ("How to activate XLBONUS", "كيفية تفعيل XLBONUS"),
    ("How to use XLBONUS", "كيفية استخدام XLBONUS"),
    ("Step 1: Register", "الخطوة 1: التسجيل"),
    ("Step 2: Enter Code", "الخطوة 2: إدخال الرمز"),
    ("Step 3: Deposit", "الخطوة 3: الإيداع"),
    ("Step 4: Play", "الخطوة 4: اللعب"),
    # Common headings  
    ("How it works", "كيف يعمل"),
    ("How It Works", "كيف يعمل"),
    ("Why choose 1win", "لماذا تختار 1win"),
    ("Why Choose 1win", "لماذا تختار 1win"),
    ("Why 1win", "لماذا 1win"),
    ("Key features", "الميزات الرئيسية"),
    ("Getting started", "البداية"),
    ("Getting Started", "البداية"),
    ("Quick start", "بداية سريعة"),
    ("Quick Start", "بداية سريعة"),
    ("Frequently Asked Questions", "الأسئلة الشائعة"),
    ("Responsible Gambling", "المراهنة المسؤولة"),
    ("Customer Support", "دعم العملاء"),
    ("Live Chat", "دردشة مباشرة"),
    ("live chat", "دردشة مباشرة"),
    ("24/7", "24/7"),
    ("available 24/7", "متاح 24/7"),
    ("Licensed and regulated", "مرخصة وخاضعة للتنظيم"),
    # Payment specific  
    ("Min deposit", "الحد الأدنى للإيداع"),
    ("Max withdrawal", "الحد الأقصى للسحب"),
    ("Processing fee", "رسوم المعالجة"),
    ("No fees", "بدون رسوم"),
    ("Supported countries", "الدول المدعومة"),
    ("Deposit methods", "طرق الإيداع"),
    ("Withdrawal methods", "طرق السحب"),
    ("How to deposit", "كيفية الإيداع"),
    ("How to withdraw", "كيفية السحب"),
    # Registration specific
    ("How to register at 1win with XLBONUS", "كيفية التسجيل في 1win باستخدام XLBONUS"),
    ("Click the Register button", "انقر زر التسجيل"),
    ("Choose your country", "اختر دولتك"),
    ("Enter your details", "أدخل بياناتك"),
    ("Confirm your account", "أكد حسابك"),
    # Bonus specific
    ("35x wagering requirement", "متطلب مراهنة 35×"),
    ("35x wagering", "35× متطلب الرهان"),
    ("Valid for 30 days", "صالح لمدة 30 يوماً"),
    ("Bonus credited instantly", "تُضاف المكافأة فوراً"),
    ("No bonus code needed", "لا يلزم رمز مكافأة"),
    ("Bonus expires in", "تنتهي صلاحية المكافأة خلال"),
    # VIP specific
    ("Become a VIP member", "كن عضوًا VIP"),
    ("Exclusive rewards", "مكافآت حصرية"),
    ("Personal manager", "مدير شخصي"),
    ("Higher limits", "حدود أعلى"),
    ("Faster withdrawals", "سحب أسرع"),
    # Lucky Drive
    ("Lucky Drive: Win a Lamborghini Urus SE", "Lucky Drive: افز سيارة Lamborghini Urus SE"),
    ("Win a car", "افز سيارة"),
    ("Car giveaway", "هبة سيارة"),
]


# Short words that are too risky to translate globally (could break URLs/attrs)
SHORT_WORDS_SKIP = {
    'win', 'new', 'New', 'review', 'Review', 'today', 'Today', 'now', 'Now',
    'free', 'Free', 'top', 'Top', 'best', 'Best', 'match', 'Match',
    'pool', 'live', 'Live', 'open', 'Open', 'play', 'Play', 'draw',
    'loss', 'team', 'goal', 'next', 'Next', 'back', 'Back', 'fast', 'Fast',
    'easy', 'Easy', 'safe', 'Safe', 'copy', 'Copy', 'full', 'Full',
    'result', 'Result', 'total', 'Total', 'rank', 'Rank', 'min', 'Min',
    'max', 'Max', 'valid', 'Valid', 'active', 'Active', 'hours', 'Hours',
    'days', 'minutes', 'seconds', 'sport', 'Sport', 'score', 'Score',
    'player', 'Players', 'balance', 'Balance', 'profit', 'Profit',
    'season', 'League', 'league', 'stream', 'Stream', 'funds', 'Funds',
    'amount', 'Amount', 'currency', 'Currency', 'open', 'close', 'Close',
    'Poker', 'poker',  # keep in nav only via direct replacement
    'load', 'Load', 'broadcast', 'Watch', 'watch',
}

def apply_body_translations(seg: str) -> str:
    """Apply body text translations to an HTML segment, only within text nodes."""
    # Split seg into HTML-tag and text-node alternating parts
    # Pattern: text_node(<tag>text_node<tag>...)
    # We only translate the text nodes (even-indexed parts after split on tags)
    
    # Sort translations: longer phrases first to avoid partial replacements
    sorted_trans = sorted(
        [(e, a) for (e, a) in BODY_TRANSLATIONS if e not in SHORT_WORDS_SKIP],
        key=lambda x: len(x[0]), reverse=True
    )
    
    # Split on HTML tags to get alternating [text, tag, text, tag, ...]
    parts = re.split(r'(<[^>]+>)', seg)
    
    result_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # text node (between tags)
            for en_text, ar_text in sorted_trans:
                if en_text in part:
                    part = part.replace(en_text, ar_text)
            result_parts.append(part)
        else:  # HTML tag - do NOT translate content (only safe attr translations done in translate_html_segment)
            result_parts.append(part)
    
    return ''.join(result_parts)


# ─── Page-specific meta translations ─────────────────────────────────────────

# Map of rel_path → (AR title, AR description)
PAGE_META = {
    'index.html': (
        "رمز 1win الترويجي XLBONUS - مكافأة ترحيب 600% (2026)",
        "استخدم الرمز الترويجي XLBONUS من 1win للحصول على مكافأة ترحيب 600% على أول 4 إيداعات. 30+ رياضة، 11,000+ لعبة كازينو، Aviator، ومدفوعات مشفرة فورية. مرخصة من كوراساو 8048/JAZ."
    ),
    'promo-code.html': (
        "رمز 1win الترويجي XLBONUS 2026 - دليل المكافأة الكاملة",
        "فعّل الرمز الترويجي XLBONUS من 1win واحصل على مكافأة 600% على إيداعك الأول. دليلنا خطوة بخطوة لأكبر عرض ترحيبي من 1win. مرخصة من كوراساو 8048/JAZ."
    ),
    '1win-promo-code.html': (
        "رمز 1win الترويجي XLBONUS 2026 - الدليل الكامل لمكافأة 600%",
        "استخدم رمز 1win الترويجي XLBONUS للحصول على مكافأة ترحيب 600%. دليل شامل لتفعيل الرمز الترويجي والحصول على المكافآت في 1win. مرخصة من كوراساو 8048/JAZ."
    ),
    'casino.html': (
        "كازينو 1win على الإنترنت - 11,000+ لعبة مع XLBONUS",
        "العب في كازينو 1win مع 11,000+ لعبة بما فيها السلوت، الكازينو المباشر، والبوكر. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'sports-betting.html': (
        "المراهنات الرياضية في 1win - 30+ رياضة مع XLBONUS",
        "راهن على 30+ رياضة في 1win مع 40,000+ سوق. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. كرة القدم، الكريكيت، كرة السلة والمزيد. مرخصة من كوراساو 8048/JAZ."
    ),
    'aviator.html': (
        "Aviator في 1win - العب مع رمز XLBONUS الترويجي",
        "العب Aviator في 1win واستخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. معدل عائد 97%. رياضة إلكترونية مثيرة مع خيار مضاعف. مرخصة من كوراساو 8048/JAZ."
    ),
    'poker.html': (
        "بوكر 1win على الإنترنت - ألعاب البوكر مع XLBONUS",
        "العب البوكر في 1win مع بطولات مجانية ومكافآت. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. Texas Hold'em وأكثر. مرخصة من كوراساو 8048/JAZ."
    ),
    'register.html': (
        "التسجيل في 1win - كيفية إنشاء حساب مع XLBONUS",
        "سجّل في 1win خطوة بخطوة واحصل على مكافأة 600% باستخدام الرمز الترويجي XLBONUS. تحقق وأودع ابدأ اللعب. مرخصة من كوراساو 8048/JAZ."
    ),
    'review.html': (
        "مراجعة 1win 2026 - كازينو ومراهنات موثوقة",
        "مراجعة شاملة لمنصة 1win: المكافآت، الرياضة، الكازينو، طرق الدفع، وأكثر. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'faq.html': (
        "الأسئلة الشائعة عن 1win - إجابات شاملة",
        "إجابات على الأسئلة الشائعة عن 1win: التسجيل، المكافآت، الرمز الترويجي XLBONUS، طرق الدفع والمزيد. مرخصة من كوراساو 8048/JAZ."
    ),
    'vip-club.html': (
        "نادي VIP في 1win - المكافآت والامتيازات الحصرية",
        "انضم إلى نادي 1win VIP واحصل على مكافآت حصرية وأموال مسترجعة وخدمة مميزة. استخدم الرمز الترويجي XLBONUS. مرخصة من كوراساو 8048/JAZ."
    ),
    'lucky-drive.html': (
        "Lucky Drive في 1win - لعبة سباق السيارات الحصرية",
        "العب Lucky Drive في 1win، لعبة سباق السيارات الحصرية بمضاعفات مثيرة. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'news.html': (
        "أخبار 1win - آخر التحديثات والعروض",
        "آخر أخبار 1win: تحديثات المنصة، العروض الجديدة، والرمز الترويجي XLBONUS. 11,000+ لعبة و30+ رياضة. مرخصة من كوراساو 8048/JAZ."
    ),
    'app.html': (
        "تطبيق 1win للجوال - تنزيل للأندرويد و iOS",
        "نزّل تطبيق 1win على الأندرويد أو iOS وراهن من أي مكان. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'access.html': (
        "الوصول إلى 1win - الروابط البديلة والمرايا",
        "اصل إلى 1win من أي مكان عبر الروابط البديلة والمرايا المحدّثة. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'alternative-link.html': (
        "الرابط البديل لـ 1win - الوصول بدون قيود",
        "استخدم الرابط البديل الرسمي لـ 1win للوصول إلى المنصة دون قيود. الرمز الترويجي XLBONUS لمكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'mirrors.html': (
        "مرايا 1win - روابط بديلة محدّثة 2026",
        "قائمة مرايا 1win البديلة المحدّثة للوصول إلى المنصة. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'payment-methods.html': (
        "طرق الدفع في 1win - إيداع وسحب سريع",
        "جميع طرق الدفع في 1win: بطاقات، محافظ إلكترونية، وعملات مشفرة. سحب خلال 4 ساعات. استخدم الرمز الترويجي XLBONUS. مرخصة من كوراساو 8048/JAZ."
    ),
    'live-streaming.html': (
        "البث المباشر في 1win - شاهد المباريات وراهن",
        "شاهد المباريات مباشرة في 1win وراهن أثناء البث. 30+ رياضة مع الرمز الترويجي XLBONUS لمكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'promotions.html': (
        "عروض 1win 2026 - مكافآت وأكواد ترويجية",
        "جميع عروض 1win: مكافأة الترحيب 600%، استرداد نقدي، لفات مجانية والمزيد. استخدم الرمز الترويجي XLBONUS. مرخصة من كوراساو 8048/JAZ."
    ),
    'website.html': (
        "موقع 1win - دليل شامل للمنصة",
        "دليل شامل لموقع 1win: الكازينو، الرياضة، الرمز الترويجي XLBONUS، طرق الدفع والمزيد. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/index.html': (
        "دليل مكافآت 1win - عرض ترحيب 600% مع XLBONUS",
        "دليل كامل لمكافآت 1win: مكافأة ترحيب 600% على 4 إيداعات، لفات مجانية، استرداد نقدي. استخدم XLBONUS عند التسجيل. شروط مراهنة 35x، 30 يوماً لكل مرحلة. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/first-deposit-bonus.html': (
        "مكافأة الإيداع الأول في 1win - 200% مع XLBONUS",
        "احصل على مكافأة 200% على إيداعك الأول في 1win مع الرمز الترويجي XLBONUS. شروط المراهنة 35x خلال 30 يوماً. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/second-deposit-bonus.html': (
        "مكافأة الإيداع الثاني في 1win - 150% مع XLBONUS",
        "احصل على مكافأة 150% على إيداعك الثاني في 1win مع الرمز الترويجي XLBONUS. شروط المراهنة 35x خلال 30 يوماً. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/third-deposit-bonus.html': (
        "مكافأة الإيداع الثالث في 1win - 150% مع XLBONUS",
        "احصل على مكافأة 150% على إيداعك الثالث في 1win مع الرمز الترويجي XLBONUS. شروط المراهنة 35x خلال 30 يوماً. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/fourth-deposit-bonus.html': (
        "مكافأة الإيداع الرابع في 1win - 100% مع XLBONUS",
        "احصل على مكافأة 100% على إيداعك الرابع في 1win مع الرمز الترويجي XLBONUS. أكمل الحزمة الكاملة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/cashback-bonus.html': (
        "مكافأة استرداد نقدي في 1win - استرجع خسائرك",
        "احصل على استرداد نقدي أسبوعي في 1win. استخدم الرمز الترويجي XLBONUS للحصول على مكافأة ترحيب 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/free-spins-today.html': (
        "لفات مجانية اليوم في 1win - أحدث العروض",
        "احصل على لفات مجانية اليوم في 1win مع الرمز الترويجي XLBONUS. أحدث عروض السلوت المجانية محدّثة يومياً. مرخصة من كوراساو 8048/JAZ."
    ),
    'bonus/wagering-requirements.html': (
        "شروط المراهنة في 1win - دليل شامل",
        "شروط مراهنة مكافآت 1win: 35x، مدة 30 يوماً لكل مرحلة. دليل كامل لكيفية تحقيق شروط المراهنة. الرمز XLBONUS. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/index.html': (
        "ألعاب Crash في 1win - Aviator وJetX والمزيد",
        "العب ألعاب Crash الأفضل في 1win: Aviator، JetX، Spaceman، Aviatrix والمزيد. استخدم XLBONUS للحصول على مكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/aviatrix.html': (
        "Aviatrix في 1win - دليل اللعبة والاستراتيجية",
        "العب Aviatrix في 1win مع الرمز الترويجي XLBONUS. دليل كامل لاستراتيجيات لعبة Aviatrix ومضاعفاتها. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/hilo.html': (
        "HiLo في 1win - لعبة أعلى أم أدنى",
        "العب HiLo في 1win وتوقع إذا كانت البطاقة التالية أعلى أم أدنى. استخدم XLBONUS لمكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/jetx.html': (
        "JetX في 1win - لعبة الطائرة النفاثة",
        "العب JetX في 1win مع الرمز الترويجي XLBONUS. دليل لعبة JetX والاستراتيجيات الفعّالة. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/mines.html': (
        "Mines في 1win - لعبة حقل الألغام",
        "العب Mines في 1win وتجنب الألغام للفوز بمضاعفات كبيرة. استخدم XLBONUS لمكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/plinko.html': (
        "Plinko في 1win - لعبة الكرة المتقافزة",
        "العب Plinko في 1win وشاهد الكرة تقفز نحو جوائز كبيرة. استخدم XLBONUS لمكافأة 600%. مرخصة من كوراساو 8048/JAZ."
    ),
    'crash/spaceman.html': (
        "Spaceman في 1win - لعبة الفضاء المثيرة",
        "العب Spaceman في 1win مع الرمز الترويجي XLBONUS. دليل لعبة Spaceman ونصائح الفوز. مرخصة من كوراساو 8048/JAZ."
    ),
}


def translate_meta(content: str, rel_path: str) -> str:
    """Translate title and meta description using page-specific mappings."""
    if rel_path in PAGE_META:
        ar_title, ar_desc = PAGE_META[rel_path]
        # Replace title
        content = re.sub(r'<title>[^<]*</title>', f'<title>{ar_title}</title>', content)
        # Replace meta description
        content = re.sub(
            r'(<meta\s+name="description"\s+content=")[^"]*(")',
            f'\\g<1>{ar_desc}\\g<2>',
            content
        )
        # Replace og:title
        content = re.sub(
            r'(<meta\s+property="og:title"\s+content=")[^"]*(")',
            f'\\g<1>{ar_title}\\g<2>',
            content
        )
        # Replace og:description
        content = re.sub(
            r'(<meta\s+property="og:description"\s+content=")[^"]*(")',
            f'\\g<1>{ar_desc}\\g<2>',
            content
        )
    return content


def generate_ar_meta_from_en(content: str, rel_path: str) -> str:
    """
    For pages without a specific meta entry, do a best-effort translation
    of the title and meta description.
    """
    # Safe translations for meta content (exclude short/dangerous words)
    SAFE_META_TRANSLATIONS = sorted(
        [(e, a) for (e, a) in BODY_TRANSLATIONS 
         if e not in SHORT_WORDS_SKIP and len(e) >= 4 and '1win' not in e],
        key=lambda x: len(x[0]), reverse=True
    )
    
    # Extract EN title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        en_title = title_match.group(1)
        # Only translate if still in English (no Arabic chars)
        if not re.search(r'[\u0600-\u06FF]', en_title):
            ar_title = en_title
            # Apply safe translations to title
            for en_text, ar_text in SAFE_META_TRANSLATIONS:
                if en_text in ar_title:
                    ar_title = ar_title.replace(en_text, ar_text)
            if ar_title != en_title:
                content = content.replace(f'<title>{en_title}</title>', f'<title>{ar_title}</title>')
                # Also update og:title
                content = re.sub(
                    r'(<meta\s+property="og:title"\s+content=")[^"]*(")',
                    f'\\g<1>{ar_title}\\g<2>',
                    content
                )
    
    # Extract EN description
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content)
    if desc_match:
        en_desc = desc_match.group(1)
        if not re.search(r'[\u0600-\u06FF]', en_desc):
            ar_desc = en_desc
            for en_text, ar_text in SAFE_META_TRANSLATIONS:
                if en_text in ar_desc:
                    ar_desc = ar_desc.replace(en_text, ar_text)
            # Ensure Curaçao 8048/JAZ in description
            if '8048/JAZ' not in ar_desc and '8048' not in ar_desc:
                ar_desc = ar_desc.rstrip('.') + '. مرخصة من كوراساو 8048/JAZ.'
            if ar_desc != en_desc:
                content = re.sub(
                    r'(<meta\s+name="description"\s+content=")[^"]*(")',
                    f'\\g<1>{ar_desc}\\g<2>',
                    content
                )
                content = re.sub(
                    r'(<meta\s+property="og:description"\s+content=")[^"]*(")',
                    f'\\g<1>{ar_desc}\\g<2>',
                    content
                )
    
    return content


def translate_jsonld_text(content: str, rel_path: str) -> str:
    """Translate text fields within JSON-LD blocks."""
    def translate_jsonld_block(m):
        block_text = m.group(0)
        try:
            # Find the JSON part
            json_match = re.search(r'(<script[^>]*>)(.*?)(</script>)', block_text, re.DOTALL)
            if not json_match:
                return block_text
            
            pre = json_match.group(1)
            json_str = json_match.group(2)
            post = json_match.group(3)
            
            data = json.loads(json_str)
            
            # Translate name and description fields
            # Use only safe translations (not short words that could corrupt brand names like 1win)
            SAFE_JSONLD_TRANSLATIONS = sorted(
                [(e, a) for (e, a) in BODY_TRANSLATIONS if len(e) >= 6 and '1win' not in e],
                key=lambda x: len(x[0]), reverse=True
            )
            def translate_value(v, key=''):
                if isinstance(v, str):
                    if key in ('name', 'description', 'headline', 'alternateName'):
                        # Apply safe translations only (preserves brand names like 1win)
                        for en_text, ar_text in SAFE_JSONLD_TRANSLATIONS:
                            if en_text in v:
                                v = v.replace(en_text, ar_text)
                        # Fix dashes
                        v = v.replace('\u2014', '-').replace('\u2013', '-')
                    elif key == 'url':
                        v = v.replace('/en/', '/ar/')
                    elif key == 'target':
                        v = v.replace('/en/', '/ar/')
                    return v
                elif isinstance(v, dict):
                    return {k: translate_value(val, k) for k, val in v.items()}
                elif isinstance(v, list):
                    return [translate_value(item, key) for item in v]
                return v
            
            translated_data = translate_value(data)
            translated_json = json.dumps(translated_data, ensure_ascii=False, indent=2)
            return pre + '\n' + translated_json + '\n' + post
        except Exception:
            # If JSON parsing fails, return original
            return block_text
    
    content = re.sub(
        r'<script type="application/ld\+json"[^>]*>.*?</script>',
        translate_jsonld_block,
        content,
        flags=re.DOTALL
    )
    return content


# ─── Main translation pipeline ────────────────────────────────────────────────

def full_translate_complete(en_content: str, rel_path: str) -> str:
    """Complete EN → AR translation pipeline."""
    content = en_content
    
    # 1. Fix <html> tag
    content = re.sub(r'<html\s+lang="en"[^>]*>', '<html lang="ar" dir="rtl">', content)
    
    # 2. Fix canonical URL: Always set to the correct AR URL for this page
    # First try /en/ → /ar/ substitution
    content = re.sub(r'(rel="canonical"\s+href="https://1win\.codes)/en/', r'\1/ar/', content)
    # For pages without /en/ in canonical (e.g. news/* pointing to /news-aviator-record),
    # override with the actual AR page URL
    ar_canonical_url = 'https://1win.codes/ar/' + ('' if rel_path == 'index.html' 
                        else rel_path[:-len('index.html')] if rel_path.endswith('/index.html')
                        else rel_path[:-5] if rel_path.endswith('.html')
                        else rel_path)
    # Check if canonical still lacks /ar/
    canon_m = re.search(r'rel="canonical"\s+href="([^"]+)"', content)
    if canon_m and '/ar/' not in canon_m.group(1):
        old_canon = canon_m.group(0)
        new_canon = f'rel="canonical" href="{ar_canonical_url}"'
        content = content.replace(old_canon, new_canon, 1)
    
    # 3. Remove all existing hreflang links
    content = re.sub(r'[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*"\s*/?>\n?', '', content)
    
    # 4. Insert full hreflang block after canonical
    new_hreflang = build_hreflang_block(rel_path)
    content = re.sub(
        r'(<link rel="canonical"[^>]*>)',
        r'\1\n' + new_hreflang,
        content
    )
    
    # 5. Fix internal navigation hrefs: /en/ → /ar/
    content = re.sub(r'href="/en/', 'href="/ar/', content)
    
    # 6. Fix em/en dashes (outside scripts/styles)
    content = fix_dashes(content)
    
    # 7. Translate meta tags (title, description, og tags)
    content = translate_meta(content, rel_path)
    content = generate_ar_meta_from_en(content, rel_path)
    
    # 8. Translate JSON-LD text fields + fix URLs in JSON-LD
    content = translate_jsonld_text(content, rel_path)
    content = fix_jsonld_urls(content, rel_path)
    
    # 9. Translate HTML segments (nav, body, footer)
    content = translate_segments(content, rel_path)
    
    # 10. Ensure Curaçao 8048/JAZ present in body
    content = inject_curacaoo_if_missing(content)
    
    return content


# ─── File processing ──────────────────────────────────────────────────────────

def process_file(rel_path: str) -> tuple[bool, str]:
    """Process one file: read EN, translate, write AR."""
    en_path = os.path.join(EN_DIR, rel_path)
    ar_path = os.path.join(AR_DIR, rel_path)
    
    if not os.path.exists(en_path):
        return False, f"EN file not found: {en_path}"
    
    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    ar_content = full_translate_complete(en_content, rel_path)
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(ar_path) if os.path.dirname(ar_path) else AR_DIR, exist_ok=True)
    
    with open(ar_path, 'w', encoding='utf-8') as f:
        f.write(ar_content)
    
    return True, ""


def read_inventory() -> list[str]:
    inv_path = os.path.join(BASE, "build_helpers/en_page_inventory.txt")
    with open(inv_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == '__main__':
    pages = read_inventory()
    print(f"Processing {len(pages)} pages EN → AR...")
    
    errors = []
    for i, rel_path in enumerate(pages):
        ok, err = process_file(rel_path)
        if not ok:
            errors.append((rel_path, err))
            print(f"  ERROR [{i+1}]: {err}")
        else:
            print(f"  OK [{i+1}/{len(pages)}]: {rel_path}")
    
    print(f"\nDone: {len(pages) - len(errors)}/{len(pages)} files processed")
    if errors:
        print("ERRORS:")
        for p, e in errors:
            print(f"  {p}: {e}")
