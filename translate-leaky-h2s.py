#!/usr/bin/env python3
"""
Translate leaky English H2 templates in non-English language folders.

Phrases targeted (in upper-case form):
  - POPULAR SPORTS BETTING IN
  - PAYMENT METHODS IN
  - BET ON
  - CLAIM YOUR  (and CLAIM YOUR 600% BONUS)
  - HOW TO
  - READY TO

Country names inside <span class="text-gradient">...</span> are also translated.
"""

import re
import os
from pathlib import Path

ROOT = Path(__file__).parent

# Translations per language for the H2 prefix templates (preserve case style)
# Each value is the translation of the English phrase. The country/object will follow.
# Extended template phrases (H2 prefixes that contain more than 2 words)
# These are applied as full-string substitutions on H2 prefix text.
EXTENDED = {
    "nl": {
        "1WIN MIRROR VS": "1WIN MIRROR VS",  # leave brand+technical
        "WHY USE A": "WAAROM EEN",
        "IS IT SAFE TO USE A": "IS HET VEILIG OM EEN",
        "WHAT'S ON THE": "WAT STAAT ER OP DE",
        "EXPLORE THE": "ONTDEK DE",
        "1WIN CASINO IN": "1WIN CASINO IN",
        "1WIN WEBSITE": "1WIN WEBSITE",
    },
    "tr": {
        "WHY USE A": "NEDEN BİR",
        "IS IT SAFE TO USE A": "BİR KULLANMAK GÜVENLİ Mİ",
        "WHAT'S ON THE": "NELER VAR",
        "EXPLORE THE": "KEŞFET",
        "1WIN CASINO IN": "1WIN CASINO",
        "1WIN WEBSITE": "1WIN WEBSİTESİ",
    },
    "de": {
        "WHY USE A": "WARUM EINEN",
        "IS IT SAFE TO USE A": "IST ES SICHER, EINEN",
        "WHAT'S ON THE": "WAS GIBT ES AUF DER",
        "EXPLORE THE": "ENTDECKE DIE",
        "1WIN CASINO IN": "1WIN CASINO IN",
        "1WIN WEBSITE": "1WIN WEBSITE",
    },
    "vi": {
        "WHY USE A": "TẠI SAO DÙNG",
        "IS IT SAFE TO USE A": "DÙNG CÓ AN TOÀN KHÔNG",
        "WHAT'S ON THE": "CÓ GÌ TRÊN",
        "EXPLORE THE": "KHÁM PHÁ",
        "1WIN CASINO IN": "1WIN CASINO TẠI",
        "1WIN WEBSITE": "WEBSITE 1WIN",
    },
    "id": {
        "WHY USE A": "MENGAPA MENGGUNAKAN",
        "IS IT SAFE TO USE A": "APAKAH AMAN MENGGUNAKAN",
        "WHAT'S ON THE": "APA YANG ADA DI",
        "EXPLORE THE": "JELAJAHI",
        "1WIN CASINO IN": "1WIN CASINO DI",
        "1WIN WEBSITE": "WEBSITE 1WIN",
    },
    "fr": {
        "WHY USE A": "POURQUOI UTILISER UN",
        "IS IT SAFE TO USE A": "EST-IL SÛR D'UTILISER UN",
        "WHAT'S ON THE": "QU'Y A-T-IL SUR LE",
        "EXPLORE THE": "EXPLOREZ LE",
        "1WIN CASINO IN": "1WIN CASINO EN",
        "1WIN WEBSITE": "SITE 1WIN",
    },
    "pt": {
        "WHY USE A": "POR QUE USAR UM",
        "IS IT SAFE TO USE A": "É SEGURO USAR UM",
        "WHAT'S ON THE": "O QUE TEM NO",
        "EXPLORE THE": "EXPLORE O",
        "1WIN CASINO IN": "1WIN CASINO NO",
        "1WIN WEBSITE": "SITE 1WIN",
    },
    "es": {
        "WHY USE A": "POR QUÉ USAR UN",
        "IS IT SAFE TO USE A": "ES SEGURO USAR UN",
        "WHAT'S ON THE": "QUÉ HAY EN EL",
        "EXPLORE THE": "EXPLORA EL",
        "1WIN CASINO IN": "1WIN CASINO EN",
        "1WIN WEBSITE": "SITIO 1WIN",
    },
    "ko": {
        "WHY USE A": "왜",
        "IS IT SAFE TO USE A": "안전한가요",
        "WHAT'S ON THE": "무엇이 있나요",
        "EXPLORE THE": "살펴보기",
        "1WIN MIRROR": "1WIN 미러",
        "1WIN WEBSITE": "1WIN 웹사이트",
        "1WIN CASINO IN": "1WIN 카지노",
    },
    "th": {
        "WHY USE A": "ทำไมต้องใช้",
        "IS IT SAFE TO USE A": "ปลอดภัยไหมที่จะใช้",
        "WHAT'S ON THE": "มีอะไรบ้างใน",
        "EXPLORE THE": "สำรวจ",
        "1WIN CASINO IN": "1WIN คาสิโน",
        "1WIN WEBSITE": "เว็บไซต์ 1WIN",
    },
    "hi": {
        "WHY USE A": "क्यों उपयोग करें",
        "IS IT SAFE TO USE A": "क्या उपयोग करना सुरक्षित है",
        "WHAT'S ON THE": "क्या है",
        "EXPLORE THE": "देखें",
        "1WIN CASINO IN": "1WIN कैसीनो",
        "1WIN WEBSITE": "1WIN वेबसाइट",
    },
    "it": {
        "WHY USE A": "PERCHÉ USARE UN",
        "IS IT SAFE TO USE A": "È SICURO USARE UN",
        "WHAT'S ON THE": "COSA C'È SU",
        "EXPLORE THE": "ESPLORA IL",
        "1WIN CASINO IN": "1WIN CASINO IN",
        "1WIN WEBSITE": "SITO 1WIN",
    },
    "fa": {
        "WHY USE A": "چرا استفاده کنید",
        "IS IT SAFE TO USE A": "آیا استفاده ایمن است",
        "WHAT'S ON THE": "چه چیزی هست",
        "EXPLORE THE": "کاوش کنید",
        "1WIN CASINO IN": "1WIN کازینو",
        "1WIN WEBSITE": "وب‌سایت 1WIN",
    },
    "pl": {
        "WHY USE A": "DLACZEGO UŻYWAĆ",
        "IS IT SAFE TO USE A": "CZY UŻYWANIE JEST BEZPIECZNE",
        "WHAT'S ON THE": "CO JEST NA",
        "EXPLORE THE": "ODKRYJ",
        "1WIN CASINO IN": "1WIN KASYNO",
        "1WIN WEBSITE": "STRONA 1WIN",
    },
    "uk": {
        "WHY USE A": "НАВІЩО ВИКОРИСТОВУВАТИ",
        "IS IT SAFE TO USE A": "ЧИ БЕЗПЕЧНО ВИКОРИСТОВУВАТИ",
        "WHAT'S ON THE": "ЩО Є НА",
        "EXPLORE THE": "ВІДКРИЙ",
        "1WIN CASINO IN": "1WIN КАЗИНО",
        "1WIN WEBSITE": "САЙТ 1WIN",
    },
}

PREFIX = {
    "nl": {  # Dutch
        "POPULAR SPORTS BETTING IN": "POPULAIRE SPORTWEDDENSCHAPPEN IN",
        "PAYMENT METHODS IN": "BETAALMETHODEN IN",
        "BET ON": "WED OP",
        "CLAIM YOUR": "CLAIM JE",
        "HOW TO": "HOE",
        "READY TO": "KLAAR OM TE",
    },
    "tr": {  # Turkish
        "POPULAR SPORTS BETTING IN": "POPÜLER SPOR BAHİSLERİ",
        "PAYMENT METHODS IN": "ÖDEME YÖNTEMLERİ",
        "BET ON": "BAHİS OYNA",
        "CLAIM YOUR": "TALEP ET",
        "HOW TO": "NASIL",
        "READY TO": "HAZIR MISIN",
    },
    "de": {  # German
        "POPULAR SPORTS BETTING IN": "BELIEBTE SPORTWETTEN IN",
        "PAYMENT METHODS IN": "ZAHLUNGSMETHODEN IN",
        "BET ON": "WETTE AUF",
        "CLAIM YOUR": "HOL DIR",
        "HOW TO": "SO",
        "READY TO": "BEREIT ZU",
    },
    "vi": {  # Vietnamese
        "POPULAR SPORTS BETTING IN": "CÁ CƯỢC THỂ THAO PHỔ BIẾN TẠI",
        "PAYMENT METHODS IN": "PHƯƠNG THỨC THANH TOÁN TẠI",
        "BET ON": "ĐẶT CƯỢC",
        "CLAIM YOUR": "NHẬN NGAY",
        "HOW TO": "CÁCH",
        "READY TO": "SẴN SÀNG",
    },
    "id": {  # Indonesian
        "POPULAR SPORTS BETTING IN": "TARUHAN OLAHRAGA POPULER DI",
        "PAYMENT METHODS IN": "METODE PEMBAYARAN DI",
        "BET ON": "TARUHAN DI",
        "CLAIM YOUR": "KLAIM",
        "HOW TO": "CARA",
        "READY TO": "SIAP UNTUK",
    },
    "fr": {  # French
        "POPULAR SPORTS BETTING IN": "PARIS SPORTIFS POPULAIRES EN",
        "PAYMENT METHODS IN": "MÉTHODES DE PAIEMENT EN",
        "BET ON": "PARIEZ SUR",
        "CLAIM YOUR": "RÉCLAMEZ VOTRE",
        "HOW TO": "COMMENT",
        "READY TO": "PRÊT À",
    },
    "pt": {  # Portuguese
        "POPULAR SPORTS BETTING IN": "APOSTAS ESPORTIVAS POPULARES NO",
        "PAYMENT METHODS IN": "MÉTODOS DE PAGAMENTO NO",
        "BET ON": "APOSTE EM",
        "CLAIM YOUR": "REIVINDIQUE SEU",
        "HOW TO": "COMO",
        "READY TO": "PRONTO PARA",
    },
    "es": {  # Spanish
        "POPULAR SPORTS BETTING IN": "APUESTAS DEPORTIVAS POPULARES EN",
        "PAYMENT METHODS IN": "MÉTODOS DE PAGO EN",
        "BET ON": "APUESTA EN",
        "CLAIM YOUR": "RECLAMA TU",
        "HOW TO": "CÓMO",
        "READY TO": "LISTO PARA",
    },
    "ko": {  # Korean (different word order in many cases — keep the H2 prefix readable)
        "POPULAR SPORTS BETTING IN": "인기 스포츠 베팅",
        "PAYMENT METHODS IN": "결제 수단",
        "BET ON": "베팅하기",
        "CLAIM YOUR": "받기",
        "HOW TO": "방법",
        "READY TO": "준비됐나요",
    },
    "th": {  # Thai
        "POPULAR SPORTS BETTING IN": "การพนันกีฬายอดนิยมใน",
        "PAYMENT METHODS IN": "วิธีการชำระเงินใน",
        "BET ON": "เดิมพันที่",
        "CLAIM YOUR": "รับ",
        "HOW TO": "วิธี",
        "READY TO": "พร้อม",
    },
    "hi": {  # Hindi
        "POPULAR SPORTS BETTING IN": "लोकप्रिय स्पोर्ट्स बेटिंग",
        "PAYMENT METHODS IN": "भुगतान विधियाँ",
        "BET ON": "बेट लगाएं",
        "CLAIM YOUR": "अपना दावा करें",
        "HOW TO": "कैसे",
        "READY TO": "तैयार हैं",
    },
    "it": {  # Italian
        "POPULAR SPORTS BETTING IN": "SCOMMESSE SPORTIVE POPOLARI IN",
        "PAYMENT METHODS IN": "METODI DI PAGAMENTO IN",
        "BET ON": "SCOMMETTI SU",
        "CLAIM YOUR": "RICHIEDI IL TUO",
        "HOW TO": "COME",
        "READY TO": "PRONTO A",
    },
    "fa": {  # Persian
        "POPULAR SPORTS BETTING IN": "شرط‌بندی ورزشی محبوب در",
        "PAYMENT METHODS IN": "روش‌های پرداخت در",
        "BET ON": "شرط‌بندی روی",
        "CLAIM YOUR": "دریافت",
        "HOW TO": "چگونه",
        "READY TO": "آماده‌اید",
    },
    "pl": {  # Polish
        "POPULAR SPORTS BETTING IN": "POPULARNE ZAKŁADY SPORTOWE W",
        "PAYMENT METHODS IN": "METODY PŁATNOŚCI W",
        "BET ON": "OBSTAW",
        "CLAIM YOUR": "ODBIERZ SWÓJ",
        "HOW TO": "JAK",
        "READY TO": "GOTOWY",
    },
    "uk": {  # Ukrainian
        "POPULAR SPORTS BETTING IN": "ПОПУЛЯРНІ СПОРТИВНІ СТАВКИ",
        "PAYMENT METHODS IN": "МЕТОДИ ОПЛАТИ",
        "BET ON": "СТАВКИ НА",
        "CLAIM YOUR": "ОТРИМАТИ",
        "HOW TO": "ЯК",
        "READY TO": "ГОТОВІ",
    },
}

# Country/object name translations (uppercase, matching the gradient span)
COUNTRIES = {
    "nl": {
        "BANGLADESH": "BANGLADESH", "BRAZIL": "BRAZILIË", "BRASIL": "BRAZILIË",
        "GHANA": "GHANA", "INDIA": "INDIA", "KENYA": "KENIA", "KOREA": "KOREA",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "RUSLAND", "RUSIA": "RUSLAND",
        "TURKEY": "TURKIJE", "TURKI": "TURKIJE", "VIETNAM": "VIETNAM",
        "START?": "AAN DE SLAG?", "600% BONUS": "600% BONUS",
    },
    "tr": {
        "BANGLADESH": "BANGLADEŞ", "BRAZIL": "BREZİLYA", "BRASIL": "BREZİLYA",
        "GHANA": "GANA", "INDIA": "HİNDİSTAN", "KENYA": "KENYA", "KOREA": "KORE",
        "PAKISTAN": "PAKİSTAN", "RUSSIA": "RUSYA", "RUSIA": "RUSYA",
        "TURKEY": "TÜRKİYE", "TURKI": "TÜRKİYE", "VIETNAM": "VİETNAM",
        "START?": "BAŞLAYALIM?", "600% BONUS": "%600 BONUS",
    },
    "de": {
        "BANGLADESH": "BANGLADESCH", "BRAZIL": "BRASILIEN", "BRASIL": "BRASILIEN",
        "GHANA": "GHANA", "INDIA": "INDIEN", "KENYA": "KENIA", "KOREA": "KOREA",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "RUSSLAND", "RUSIA": "RUSSLAND",
        "TURKEY": "TÜRKEI", "TURKI": "TÜRKEI", "VIETNAM": "VIETNAM",
        "START?": "STARTEN?", "600% BONUS": "600% BONUS",
    },
    "vi": {
        "BANGLADESH": "BANGLADESH", "BRAZIL": "BRAZIL", "BRASIL": "BRAZIL",
        "GHANA": "GHANA", "INDIA": "ẤN ĐỘ", "KENYA": "KENYA", "KOREA": "HÀN QUỐC",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "NGA", "RUSIA": "NGA",
        "TURKEY": "THỔ NHĨ KỲ", "TURKI": "THỔ NHĨ KỲ", "VIETNAM": "VIỆT NAM",
        "START?": "BẮT ĐẦU?", "600% BONUS": "THƯỞNG 600%",
    },
    "id": {
        "BANGLADESH": "BANGLADESH", "BRAZIL": "BRASIL", "BRASIL": "BRASIL",
        "GHANA": "GHANA", "INDIA": "INDIA", "KENYA": "KENYA", "KOREA": "KOREA",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "RUSIA", "RUSIA": "RUSIA",
        "TURKEY": "TURKI", "TURKI": "TURKI", "VIETNAM": "VIETNAM",
        "START?": "MULAI?", "600% BONUS": "BONUS 600%",
    },
    "fr": {
        "BANGLADESH": "BANGLADESH", "BRAZIL": "BRÉSIL", "BRASIL": "BRÉSIL",
        "GHANA": "GHANA", "INDIA": "INDE", "KENYA": "KENYA", "KOREA": "CORÉE",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "RUSSIE", "RUSIA": "RUSSIE",
        "TURKEY": "TURQUIE", "TURKI": "TURQUIE", "VIETNAM": "VIETNAM",
        "START?": "COMMENCER?", "600% BONUS": "BONUS 600%",
    },
    "pt": {
        "BANGLADESH": "BANGLADESH", "BRAZIL": "BRASIL", "BRASIL": "BRASIL",
        "GHANA": "GANA", "INDIA": "ÍNDIA", "KENYA": "QUÉNIA", "KOREA": "COREIA",
        "PAKISTAN": "PAQUISTÃO", "RUSSIA": "RÚSSIA", "RUSIA": "RÚSSIA",
        "TURKEY": "TURQUIA", "TURKI": "TURQUIA", "VIETNAM": "VIETNAME",
        "START?": "COMEÇAR?", "600% BONUS": "BÔNUS 600%",
    },
    "es": {
        "BANGLADESH": "BANGLADÉS", "BRAZIL": "BRASIL", "BRASIL": "BRASIL",
        "GHANA": "GHANA", "INDIA": "INDIA", "KENYA": "KENIA", "KOREA": "COREA",
        "PAKISTAN": "PAKISTÁN", "RUSSIA": "RUSIA", "RUSIA": "RUSIA",
        "TURKEY": "TURQUÍA", "TURKI": "TURQUÍA", "VIETNAM": "VIETNAM",
        "START?": "EMPEZAR?", "600% BONUS": "BONO 600%",
    },
    "ko": {
        "BANGLADESH": "방글라데시", "BRAZIL": "브라질", "BRASIL": "브라질",
        "GHANA": "가나", "INDIA": "인도", "KENYA": "케냐", "KOREA": "한국",
        "PAKISTAN": "파키스탄", "RUSSIA": "러시아", "RUSIA": "러시아",
        "TURKEY": "터키", "TURKI": "터키", "VIETNAM": "베트남",
        "START?": "시작할까요?", "600% BONUS": "600% 보너스",
    },
    "th": {
        "BANGLADESH": "บังกลาเทศ", "BRAZIL": "บราซิล", "BRASIL": "บราซิล",
        "GHANA": "กานา", "INDIA": "อินเดีย", "KENYA": "เคนยา", "KOREA": "เกาหลี",
        "PAKISTAN": "ปากีสถาน", "RUSSIA": "รัสเซีย", "RUSIA": "รัสเซีย",
        "TURKEY": "ตุรกี", "TURKI": "ตุรกี", "VIETNAM": "เวียดนาม",
        "START?": "เริ่มเลย?", "600% BONUS": "โบนัส 600%",
    },
    "hi": {
        "BANGLADESH": "बांग्लादेश", "BRAZIL": "ब्राज़ील", "BRASIL": "ब्राज़ील",
        "GHANA": "घाना", "INDIA": "भारत", "KENYA": "केन्या", "KOREA": "कोरिया",
        "PAKISTAN": "पाकिस्तान", "RUSSIA": "रूस", "RUSIA": "रूस",
        "TURKEY": "तुर्की", "TURKI": "तुर्की", "VIETNAM": "वियतनाम",
        "START?": "शुरू?", "600% BONUS": "600% बोनस",
    },
    "it": {
        "BANGLADESH": "BANGLADESH", "BRAZIL": "BRASILE", "BRASIL": "BRASILE",
        "GHANA": "GHANA", "INDIA": "INDIA", "KENYA": "KENYA", "KOREA": "COREA",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "RUSSIA", "RUSIA": "RUSSIA",
        "TURKEY": "TURCHIA", "TURKI": "TURCHIA", "VIETNAM": "VIETNAM",
        "START?": "INIZIARE?", "600% BONUS": "BONUS 600%",
    },
    "fa": {
        "BANGLADESH": "بنگلادش", "BRAZIL": "برزیل", "BRASIL": "برزیل",
        "GHANA": "غنا", "INDIA": "هند", "KENYA": "کنیا", "KOREA": "کره",
        "PAKISTAN": "پاکستان", "RUSSIA": "روسیه", "RUSIA": "روسیه",
        "TURKEY": "ترکیه", "TURKI": "ترکیه", "VIETNAM": "ویتنام",
        "START?": "شروع کنیم؟", "600% BONUS": "بونس ۶۰۰٪",
    },
    "pl": {
        "BANGLADESH": "BANGLADESZ", "BRAZIL": "BRAZYLIA", "BRASIL": "BRAZYLIA",
        "GHANA": "GHANA", "INDIA": "INDIE", "KENYA": "KENIA", "KOREA": "KOREA",
        "PAKISTAN": "PAKISTAN", "RUSSIA": "ROSJA", "RUSIA": "ROSJA",
        "TURKEY": "TURCJA", "TURKI": "TURCJA", "VIETNAM": "WIETNAM",
        "START?": "ZACZNIJMY?", "600% BONUS": "BONUS 600%",
    },
    "uk": {
        "BANGLADESH": "БАНГЛАДЕШ", "BRAZIL": "БРАЗИЛІЯ", "BRASIL": "БРАЗИЛІЯ",
        "GHANA": "ГАНА", "INDIA": "ІНДІЯ", "KENYA": "КЕНІЯ", "KOREA": "КОРЕЯ",
        "PAKISTAN": "ПАКИСТАН", "RUSSIA": "РОСІЯ", "RUSIA": "РОСІЯ",
        "TURKEY": "ТУРЕЧЧИНА", "TURKI": "ТУРЕЧЧИНА", "VIETNAM": "В'ЄТНАМ",
        "START?": "ПОЧНІМО?", "600% BONUS": "БОНУС 600%",
    },
}

# Common CTA button text — "CLAIM YOUR 600% BONUS"
CLAIM_BUTTON = {
    "nl": "CLAIM JE 600% BONUS",
    "tr": "%600 BONUSU TALEP ET",
    "de": "HOL DIR 600% BONUS",
    "vi": "NHẬN THƯỞNG 600%",
    "id": "KLAIM BONUS 600%",
    "fr": "RÉCLAMEZ VOTRE BONUS 600%",
    "pt": "RESGATE SEU BÔNUS 600%",
    "es": "RECLAMA TU BONO 600%",
    "ko": "600% 보너스 받기",
    "th": "รับโบนัส 600%",
    "hi": "अपना 600% बोनस लें",
    "it": "RICHIEDI IL TUO BONUS 600%",
    "fa": "بونس ۶۰۰٪ خود را دریافت کنید",
    "pl": "ODBIERZ BONUS 600%",
    "uk": "ОТРИМАТИ БОНУС 600%",
}


def patch_file(path: Path, lang: str) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = 0

    # 0. Translate extended template phrases (longer than 2 words) inside H2 prefix
    h2_re_full = re.compile(r"(<h2[^>]*>)([^<]+)(<span[^>]*>[^<]+</span>)([^<]*)(</h2>)")

    def h2_ext_sub(m):
        nonlocal changes
        opening, prefix_text, span, suffix, closing = m.groups()
        new_prefix = prefix_text
        new_suffix = suffix
        for en, native in EXTENDED.get(lang, {}).items():
            pattern = re.compile(re.escape(en), re.IGNORECASE)
            if pattern.search(new_prefix):
                new_prefix = pattern.sub(native, new_prefix)
            if pattern.search(new_suffix):
                new_suffix = pattern.sub(native, new_suffix)
        if new_prefix != prefix_text or new_suffix != suffix:
            changes += 1
        return f"{opening}{new_prefix}{span}{new_suffix}{closing}"

    text = h2_re_full.sub(h2_ext_sub, text)

    # 1. Translate H2 prefix templates inside <h2 ...>
    # We only touch H2s (not HTML comments) to be safe.
    h2_re = re.compile(r"(<h2[^>]*>)([^<]+)(<span[^>]*>[^<]+</span>)([^<]*)(</h2>)")

    def h2_sub(m):
        nonlocal changes
        opening, prefix_text, span, suffix, closing = m.groups()
        new_prefix = prefix_text
        for en, native in PREFIX[lang].items():
            # match the EN phrase if it appears at the start (case-insensitive)
            pattern = re.compile(re.escape(en), re.IGNORECASE)
            if pattern.search(new_prefix):
                new_prefix = pattern.sub(native, new_prefix)
        if new_prefix != prefix_text:
            changes += 1
        return f"{opening}{new_prefix}{span}{suffix}{closing}"

    text = h2_re.sub(h2_sub, text)

    # 2. Translate country names inside <span class="text-gradient">...</span> (in H2 context only)
    # Do this with a more targeted pattern that only touches gradient spans that follow our prefix templates.
    for en_country, native_country in COUNTRIES[lang].items():
        if en_country == native_country:
            continue
        gradient_pattern = re.compile(
            r'(<span class="text-gradient(?:-gold)?">)' + re.escape(en_country) + r'(</span>)'
        )
        new_text, n = gradient_pattern.subn(r"\g<1>" + native_country + r"\g<2>", text)
        if n > 0:
            text = new_text
            changes += n

    # 3. Translate the CLAIM YOUR 600% BONUS button text (CTA links)
    cta_pattern = re.compile(r'>CLAIM YOUR 600% BONUS<', re.IGNORECASE)
    text, n = cta_pattern.subn(f">{CLAIM_BUTTON[lang]}<", text)
    if n > 0:
        changes += n

    if text != original:
        path.write_text(text, encoding="utf-8")
    return changes


def main():
    total_files = 0
    total_changes = 0
    by_lang = {}
    for lang in PREFIX.keys():
        lang_dir = ROOT / lang
        if not lang_dir.is_dir():
            continue
        files = list(lang_dir.rglob("*.html"))
        lang_changes = 0
        lang_files = 0
        for f in files:
            n = patch_file(f, lang)
            if n > 0:
                lang_files += 1
                lang_changes += n
        by_lang[lang] = (lang_files, lang_changes)
        total_files += lang_files
        total_changes += lang_changes

    print(f"Total: {total_files} files patched, {total_changes} substitutions")
    for lang, (f, c) in sorted(by_lang.items()):
        print(f"  {lang}: {f} files, {c} changes")


if __name__ == "__main__":
    main()
