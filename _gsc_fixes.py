#!/usr/bin/env python3
"""
GSC/GA-driven fixes:
1. Promote 'Stake Sign Up' / 'Stake Register' into home + /promo-code/ titles (en).
2. Add prominent promo-strip CTA below reserves-ticker on /ko/ and /ms/ index pages.
3. Add cross-link card on /reserves/ to /promo-code/ (en + all locales).
"""
import os, re

ROOT = "/home/user/workspace/winnersclub.com"

# ---- FIX 1: Title/meta tweaks for en root + en promo-code ----
def fix1():
    # EN home
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    s = s.replace(
        "<title>Stake Promo Code MAX3000 — 200% to $3,000, 40x Wagering</title>",
        "<title>Stake Sign Up Code MAX3000 - Register for 200% to $3,000</title>",
    )
    s = s.replace(
        '<meta name="description" content="Use Stake.com promo code MAX3000 for a 200% welcome up to $3,000 with 40x wagering on deposit plus bonus. Live odds, mirror domains, on-chain reserves — all on WinnersClub.">',
        '<meta name="description" content="Stake sign up with code MAX3000: register on Stake.com for a 200% welcome up to $3,000, 40x wagering. Live odds, mirror domains, on-chain reserves, all on WinnersClub.">',
    )
    # og:title
    s = re.sub(
        r'(<meta property="og:title" content=")Stake Promo Code MAX3000[^"]*(")',
        r'\1Stake Sign Up Code MAX3000 - Register for 200% to $3,000\2',
        s,
    )
    s = re.sub(
        r'(<meta name="twitter:title" content=")Stake Promo Code MAX3000[^"]*(")',
        r'\1Stake Sign Up Code MAX3000 - Register for 200% to $3,000\2',
        s,
    )
    open(p, "w", encoding="utf-8").write(s)
    print("FIX1 EN home: done")

    # EN promo-code
    p2 = os.path.join(ROOT, "promo-code/index.html")
    s2 = open(p2, encoding="utf-8").read()
    s2 = s2.replace(
        "<title>Stake.com Promo Code MAX3000: 200% up to $3,000 (June 2026)</title>",
        "<title>Stake Sign Up Code MAX3000: Register for 200% to $3,000</title>",
    )
    s2 = s2.replace(
        '<meta name="description" content="Stake.com promo code MAX3000: 200% match up to $3,000 on your first deposit, 40x wagering on deposit + bonus, KYC Level 3 required. Live calculator. Verified 6 June 2026.">',
        '<meta name="description" content="Stake sign up with code MAX3000 for a 200% match up to $3,000 on first deposit, 40x wagering on deposit + bonus, KYC Level 3 required. Register on Stake.com. Verified June 2026.">',
    )
    s2 = re.sub(
        r'(<meta property="og:title" content=")Stake\.com Promo Code MAX3000[^"]*(")',
        r'\1Stake Sign Up Code MAX3000: Register for 200% to $3,000\2',
        s2,
    )
    s2 = re.sub(
        r'(<meta name="twitter:title" content=")Stake\.com Promo Code MAX3000[^"]*(")',
        r'\1Stake Sign Up Code MAX3000: Register for 200% to $3,000\2',
        s2,
    )
    # H1 sub adds "Sign up" hook
    s2 = s2.replace(
        '<h1 class="ch-title text-gradient-gold">Stake.com Promo Code MAX3000<span class="h1-sub">200% up to $3,000 on Stake.com.</span></h1>',
        '<h1 class="ch-title text-gradient-gold">Stake.com Promo Code MAX3000<span class="h1-sub">Sign up, register, 200% up to $3,000.</span></h1>',
    )
    open(p2, "w", encoding="utf-8").write(s2)
    print("FIX1 EN promo-code: done")


# ---- FIX 2: KO + MS promo strip banner below reserves-ticker ----
KO_STRIP = '''  <aside class="promo-strip" aria-label="MAX3000 프로모 코드"><div class="ps-inner"><span class="ps-label">프로모 코드</span><span class="ps-code">MAX3000</span><span class="ps-bonus">최대 $3,000 200% &middot; 40배 베팅 조건</span><a href="/ko/promo-code/" class="ps-cta">코드 페이지 열기 &rarr;</a></div></aside>
'''

MS_STRIP = '''  <aside class="promo-strip" aria-label="Kod promo MAX3000"><div class="ps-inner"><span class="ps-label">Kod Promo</span><span class="ps-code">MAX3000</span><span class="ps-bonus">200% sehingga $3,000 &middot; Pertaruhan 40x</span><a href="/ms/promo-code/" class="ps-cta">Buka halaman kod &rarr;</a></div></aside>
'''

def fix2():
    for locale, strip in [("ko", KO_STRIP), ("ms", MS_STRIP)]:
        p = os.path.join(ROOT, locale, "index.html")
        s = open(p, encoding="utf-8").read()
        if "promo-strip" in s:
            print(f"FIX2 {locale}: already present, skipping")
            continue
        # Insert immediately after the closing </div></div> of reserves-ticker
        marker = '<div class="reserves-ticker">'
        idx = s.find(marker)
        if idx < 0:
            print(f"FIX2 {locale}: marker not found")
            continue
        # Find end of that ticker block (next </div></div>)
        end = s.find("</div></div>", idx)
        if end < 0:
            print(f"FIX2 {locale}: end not found")
            continue
        end += len("</div></div>")
        # Insert strip right after the ticker closing
        s = s[:end] + "\n" + strip + s[end:]
        open(p, "w", encoding="utf-8").write(s)
        print(f"FIX2 {locale}: inserted")


# ---- FIX 3: Cross-link card on /reserves/ to /promo-code/ ----
# We add a CTA card at the bottom of the reserves content section. Map per-locale.
RESERVES_CTA = {
    "":   ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">Verified the receipts? Now claim the code.</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           'On-chain reserves are why the house can honour MAX3000. Use the same code on Stake.com sign up for a 200% match up to $3,000, 40x wagering on deposit plus bonus.</p>'
           '<a href="/promo-code/" class="btn btn-signup btn-gold-grad">Open the MAX3000 code page</a>'
           '</div></section>\n'),
    "ko": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">영수증을 확인하셨다면, 이제 코드를 받으세요.</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           '온체인 준비금이 있기에 하우스가 MAX3000을 지킬 수 있습니다. Stake.com 가입 시 같은 코드로 최대 $3,000 200% 매치, 입금+보너스 합산 40배 베팅 조건.</p>'
           '<a href="/ko/promo-code/" class="btn btn-signup btn-gold-grad">MAX3000 코드 페이지 열기</a>'
           '</div></section>\n'),
    "ms": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">Sudah sahkan resit? Sekarang tuntut kod.</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           'Rizab on-chain inilah sebabnya rumah boleh memenuhi MAX3000. Guna kod yang sama semasa daftar di Stake.com untuk padanan 200% sehingga $3,000, pertaruhan 40x.</p>'
           '<a href="/ms/promo-code/" class="btn btn-signup btn-gold-grad">Buka halaman kod MAX3000</a>'
           '</div></section>\n'),
    "vi": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">Đã kiểm tra biên lai? Giờ nhận mã.</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           'Dự trữ on-chain là lý do nhà cái có thể giữ lời với MAX3000. Dùng cùng mã khi đăng ký Stake.com để nhận 200% tới $3,000, cược 40x trên tiền gửi cộng tiền thưởng.</p>'
           '<a href="/vi/promo-code/" class="btn btn-signup btn-gold-grad">Mở trang mã MAX3000</a>'
           '</div></section>\n'),
    "zh": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">看过收据了?现在领取代码。</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           '链上储备就是庄家能兑现 MAX3000 的原因。在 Stake.com 注册时使用相同代码,即可获得高达 $3,000 的 200% 匹配,存款加奖金 40 倍流水。</p>'
           '<a href="/zh/promo-code/" class="btn btn-signup btn-gold-grad">打开 MAX3000 代码页面</a>'
           '</div></section>\n'),
    "th": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">เช็คใบเสร็จแล้ว? ตอนนี้รับโค้ด</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           'เงินสำรองออนเชนคือเหตุผลที่บ้านสามารถรักษา MAX3000 ได้ ใช้โค้ดเดียวกันตอนสมัคร Stake.com เพื่อรับโบนัส 200% สูงสุด $3,000 พร้อมเทิร์น 40 เท่าของเงินฝากบวกโบนัส</p>'
           '<a href="/th/promo-code/" class="btn btn-signup btn-gold-grad">เปิดหน้าโค้ด MAX3000</a>'
           '</div></section>\n'),
    "pt": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">Conferiu os recibos? Agora pegue o código.</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           'As reservas on-chain são o motivo de a casa poder honrar o MAX3000. Use o mesmo código no cadastro da Stake.com para um match de 200% até $3,000, rollover de 40x sobre depósito mais bônus.</p>'
           '<a href="/pt/promo-code/" class="btn btn-signup btn-gold-grad">Abrir página do código MAX3000</a>'
           '</div></section>\n'),
    "ja": ('<section class="section reserves-cta"><div class="section-inner" style="text-align:center;padding:48px 20px;">'
           '<h2 class="section-title gold-underline" style="margin-bottom:12px;">レシートを確認しましたか?では、コードを手にしましょう。</h2>'
           '<p style="max-width:640px;margin:0 auto 20px;color:rgba(255,255,255,.8);">'
           'オンチェーン準備金があるからこそ、ハウスは MAX3000 を守れます。Stake.com 登録時に同じコードを使えば、最大 $3,000 の 200% マッチ、入金とボーナス合算で 40 倍の賭け条件です。</p>'
           '<a href="/ja/promo-code/" class="btn btn-signup btn-gold-grad">MAX3000 コードページを開く</a>'
           '</div></section>\n'),
}

def fix3():
    # EN reserves
    pairs = [("", "reserves/index.html")]
    for loc in ["ko", "ms", "vi", "zh", "th", "pt", "ja"]:
        pairs.append((loc, f"{loc}/reserves/index.html"))
    for loc, rel in pairs:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print(f"FIX3 {loc or 'en'}: missing {rel}")
            continue
        s = open(p, encoding="utf-8").read()
        if "reserves-cta" in s:
            print(f"FIX3 {loc or 'en'}: already present, skipping")
            continue
        cta = RESERVES_CTA.get(loc, RESERVES_CTA[""])
        # Insert before <footer
        idx = s.find("<footer")
        if idx < 0:
            print(f"FIX3 {loc or 'en'}: footer marker not found")
            continue
        s = s[:idx] + cta + s[idx:]
        open(p, "w", encoding="utf-8").write(s)
        print(f"FIX3 {loc or 'en'}: inserted")


if __name__ == "__main__":
    fix1()
    fix2()
    fix3()
