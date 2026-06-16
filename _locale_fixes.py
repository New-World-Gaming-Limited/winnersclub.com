#!/usr/bin/env python3
"""Locale-level cleanup fixes."""
import os, re

ROOT = "/home/user/workspace/winnersclub.com"

# Labels in each locale's own language for the mobile language switcher
LANG_LABEL = {
    "ko": "언어",
    "zh": "语言",
    "vi": "Ngôn ngữ",
    "th": "ภาษา",
    "ms": "Bahasa",
    "pt": "Idioma",
    "ja": "言語",
}

def walk(loc):
    for root, dirs, files in os.walk(os.path.join(ROOT, loc)):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(root, f)

# ---- 1. zh lang attr -> zh-Hans ----
def fix_zh_lang():
    count = 0
    for p in walk("zh"):
        s = open(p, encoding="utf-8").read()
        if '<html lang="zh"' in s:
            s = s.replace('<html lang="zh"', '<html lang="zh-Hans"')
            open(p, "w", encoding="utf-8").write(s)
            count += 1
    print(f"zh lang attr fixed: {count} files")

# ---- 2. Mobile <label>Language</label> -> localized ----
def fix_lang_label():
    total = 0
    for loc, label in LANG_LABEL.items():
        n = 0
        for p in walk(loc):
            s = open(p, encoding="utf-8").read()
            if '<label>Language</label>' in s:
                s = s.replace('<label>Language</label>', f'<label>{label}</label>')
                open(p, "w", encoding="utf-8").write(s)
                n += 1
        total += n
        print(f"  {loc}: {n} files relabeled")
    print(f"Language label total: {total}")

# ---- 3. MS Taruhan -> Pertaruhan (only on standalone occurrences) ----
def fix_ms_taruhan():
    # Replace exact " Taruhan 40x" and "Taruhan 40x" tokens; safer than blanket replace
    patterns = [
        ("Taruhan 40x", "Pertaruhan 40x"),
        ("dengan Taruhan", "dengan Pertaruhan"),
        (", Taruhan", ", Pertaruhan"),
    ]
    n = 0
    for p in walk("ms"):
        s = open(p, encoding="utf-8").read()
        orig = s
        for old, new in patterns:
            s = s.replace(old, new)
        if s != orig:
            open(p, "w", encoding="utf-8").write(s)
            n += 1
    print(f"MS Taruhan->Pertaruhan: {n} files")

# ---- 4. JA ウェジャリング -> 賭け条件 ----
def fix_ja_wagering():
    n = 0
    for p in walk("ja"):
        s = open(p, encoding="utf-8").read()
        if "ウェジャリング" in s:
            s = s.replace("ウェジャリング", "賭け条件")
            open(p, "w", encoding="utf-8").write(s)
            n += 1
    print(f"JA wagering term fixed: {n} files")

# ---- 5. Add 'register/sign up' keyword to non-EN home titles (where it makes sense) ----
# Spanish phrasing equivalents are different per language; do safe, idiomatic versions
HOME_TITLE_RECRAFT = {
    # path: (old_title, new_title)
    "ko/index.html": (
        "<title>WinnersClub | Stake 코드 MAX3000 | 최대 $3,000 200%, 40배 베팅</title>",
        "<title>Stake 가입 코드 MAX3000 - 등록 시 최대 $3,000 200%</title>",
    ),
    "zh/index.html": (
        "<title>Stake 优惠码 MAX3000,200% 高达 $3,000,40倍流水</title>",
        "<title>Stake 注册优惠码 MAX3000 - 注册即享 200% 高达 $3,000</title>",
    ),
    "vi/index.html": (
        "<title>Mã Khuyến Mãi Stake MAX3000 - 200% lên đến $3,000, Cược 40x</title>",
        "<title>Mã Đăng Ký Stake MAX3000 - Đăng ký nhận 200% lên đến $3,000</title>",
    ),
    "th/index.html": (
        "<title>WinnersClub - โปรโมโค้ด Stake MAX3000: 200% สูงสุด $3,000</title>",
        "<title>โค้ดสมัคร Stake MAX3000 - สมัครรับ 200% สูงสุด $3,000</title>",
    ),
    "ms/index.html": (
        "<title>Kod Promo Stake MAX3000 - 200% hingga $3,000, Taruhan 40x</title>",
        "<title>Kod Daftar Stake MAX3000 - Daftar untuk 200% hingga $3,000</title>",
    ),
    "pt/index.html": (
        "<title>Código Promocional Stake MAX3000, 200% até $3.000, Rollover 40x</title>",
        "<title>Código de Cadastro Stake MAX3000 - Cadastre-se para 200% até $3.000</title>",
    ),
    "ja/index.html": (
        "<title>Stake プロモコード MAX3000, 200% 最大$3,000、40倍ウェジャリング</title>",
        "<title>Stake 登録コード MAX3000 - 登録で 200% 最大 $3,000</title>",
    ),
}
def fix_home_titles():
    n = 0
    for rel, (old, new) in HOME_TITLE_RECRAFT.items():
        p = os.path.join(ROOT, rel)
        s = open(p, encoding="utf-8").read()
        if old in s:
            s = s.replace(old, new)
            open(p, "w", encoding="utf-8").write(s)
            n += 1
            print(f"  {rel} title rewritten")
        else:
            # Check if already ja which contains 賭け条件 swap
            if "ウェジャリング" not in s and old.replace("ウェジャリング", "賭け条件") in s:
                s = s.replace(old.replace("ウェジャリング", "賭け条件"), new)
                open(p, "w", encoding="utf-8").write(s)
                n += 1
                print(f"  {rel} title rewritten (post-wagering-fix)")
            else:
                print(f"  {rel}: old title not matched (already updated?)")
    print(f"Home titles updated: {n}")

if __name__ == "__main__":
    fix_zh_lang()
    fix_lang_label()
    fix_ms_taruhan()
    fix_ja_wagering()
    fix_home_titles()
