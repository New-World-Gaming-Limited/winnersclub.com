#!/usr/bin/env python3
"""Localize the rooms-grid aside that currently has English links on every non-EN page."""
import os, re

ROOT = "/home/user/workspace/winnersclub.com"

# Per-locale: (heading, list of (slug, label))
ROOMS = {
    "ko": ("클럽의 다른 방들", [
        ("promo-code", "Stake 프로모 코드"),
        ("casino", "Stake 카지노"),
        ("sports", "Stake 스포츠북"),
        ("poker", "Stake 포커"),
        ("aviator", "Stake 에비에이터"),
        ("reserves", "검증된 준비금"),
        ("about-stake", "Stake 소개"),
        ("payments", "암호화폐 결제"),
        ("mirror", "미러 사이트"),
        ("live-odds", "라이브 배당률"),
        ("originals", "Stake 오리지널"),
        ("vip", "VIP 프로그램"),
        ("slots", "슬롯 라이브러리"),
        ("live-casino", "라이브 카지노"),
    ]),
    "zh": ("俱乐部里的其他房间", [
        ("promo-code", "Stake 优惠码"),
        ("casino", "Stake 赌场"),
        ("sports", "Stake 体育"),
        ("poker", "Stake 扑克"),
        ("aviator", "Stake Aviator"),
        ("reserves", "已审计储备金"),
        ("about-stake", "关于 Stake.com"),
        ("payments", "加密支付"),
        ("mirror", "镜像站点"),
        ("live-odds", "实时赔率"),
        ("originals", "Stake Originals"),
        ("vip", "VIP 计划"),
        ("slots", "老虎机库"),
        ("live-casino", "真人赌场"),
    ]),
    "vi": ("Các phòng khác trong câu lạc bộ", [
        ("promo-code", "Mã khuyến mãi Stake"),
        ("casino", "Casino Stake"),
        ("sports", "Sportsbook Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Dự trữ đã kiểm toán"),
        ("about-stake", "Về Stake.com"),
        ("payments", "Thanh toán crypto"),
        ("mirror", "Trang web gương"),
        ("live-odds", "Tỷ lệ trực tiếp"),
        ("originals", "Stake Originals"),
        ("vip", "Chương trình VIP"),
        ("slots", "Thư viện slot"),
        ("live-casino", "Casino trực tiếp"),
    ]),
    "th": ("ห้องอื่นๆ ในคลับ", [
        ("promo-code", "โปรโมโค้ด Stake"),
        ("casino", "คาสิโน Stake"),
        ("sports", "สปอร์ตบุ๊ค Stake"),
        ("poker", "โป๊กเกอร์ Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "ทุนสำรองที่ตรวจสอบแล้ว"),
        ("about-stake", "เกี่ยวกับ Stake.com"),
        ("payments", "การชำระเงินคริปโต"),
        ("mirror", "ไซต์มิเรอร์"),
        ("live-odds", "ราคาสด"),
        ("originals", "Stake Originals"),
        ("vip", "โปรแกรม VIP"),
        ("slots", "ไลบรารีสล็อต"),
        ("live-casino", "คาสิโนสด"),
    ]),
    "ms": ("Bilik lain di kelab", [
        ("promo-code", "Kod promo Stake"),
        ("casino", "Kasino Stake"),
        ("sports", "Sportsbook Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Rizab diaudit"),
        ("about-stake", "Tentang Stake.com"),
        ("payments", "Pembayaran kripto"),
        ("mirror", "Tapak cermin"),
        ("live-odds", "Odds langsung"),
        ("originals", "Stake Originals"),
        ("vip", "Program VIP"),
        ("slots", "Perpustakaan slot"),
        ("live-casino", "Kasino langsung"),
    ]),
    "pt": ("Outras salas do clube", [
        ("promo-code", "Código promocional Stake"),
        ("casino", "Cassino Stake"),
        ("sports", "Sportsbook Stake"),
        ("poker", "Poker Stake"),
        ("aviator", "Aviator Stake"),
        ("reserves", "Reservas auditadas"),
        ("about-stake", "Sobre a Stake.com"),
        ("payments", "Pagamentos cripto"),
        ("mirror", "Sites espelho"),
        ("live-odds", "Odds ao vivo"),
        ("originals", "Stake Originals"),
        ("vip", "Programa VIP"),
        ("slots", "Biblioteca de slots"),
        ("live-casino", "Cassino ao vivo"),
    ]),
    "ja": ("クラブの他の部屋", [
        ("promo-code", "Stake プロモコード"),
        ("casino", "Stake カジノ"),
        ("sports", "Stake スポーツブック"),
        ("poker", "Stake ポーカー"),
        ("aviator", "Stake Aviator"),
        ("reserves", "監査済み準備金"),
        ("about-stake", "Stake.com について"),
        ("payments", "暗号通貨決済"),
        ("mirror", "ミラーサイト"),
        ("live-odds", "ライブオッズ"),
        ("originals", "Stake オリジナル"),
        ("vip", "VIP プログラム"),
        ("slots", "スロットライブラリ"),
        ("live-casino", "ライブカジノ"),
    ]),
}

ASIDE_RE = re.compile(
    r'<aside class="rooms-grid"[^>]*aria-label="Other rooms at WinnersClub"[^>]*>.*?</aside>',
    re.S,
)

def build_aside(loc, heading, items):
    lis = "".join(f'<li><a href="/{loc}/{slug}/">{label}</a></li>' for slug, label in items)
    return (
        f'<aside class="rooms-grid" aria-label="{heading}" '
        f'style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);'
        f'border:1px solid rgba(255,215,0,.12);border-radius:14px;">'
        f'<h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;'
        f'color:#737378;margin:0 0 18px;font-weight:700;">{heading}</h3>'
        f'<ul style="list-style:none;margin:0;padding:0;display:grid;'
        f'grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;">'
        f'{lis}</ul></aside>'
    )

def main():
    total = 0
    for loc, (heading, items) in ROOMS.items():
        new_block = build_aside(loc, heading, items)
        for r, ds, fs in os.walk(os.path.join(ROOT, loc)):
            for f in fs:
                if not f.endswith(".html"): continue
                p = os.path.join(r, f)
                s = open(p, encoding="utf-8").read()
                new_s, n = ASIDE_RE.subn(new_block, s)
                if n:
                    open(p, "w", encoding="utf-8").write(new_s)
                    total += 1
        print(f"  {loc}: localized rooms-grid")
    print(f"Total files updated: {total}")

if __name__ == "__main__":
    main()
