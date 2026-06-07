#!/usr/bin/env python3
"""SEO polish: internal-link footer module + FAQ schema gap-fill + TOC on long pages."""
from pathlib import Path
import re, json

ROOT = Path("/home/user/workspace/winnersclub.com")

# -------------------------------------------------------------------
# 5. Internal-link "rooms" module — inject above footer if not present
# -------------------------------------------------------------------
INTERNAL_LINKS = {
    "promo-code": ("Stake promo code", "/promo-code/"),
    "casino": ("Casino at Stake", "/casino/"),
    "sports": ("Sportsbook at Stake", "/sports/"),
    "poker": ("Poker at Stake", "/poker/"),
    "aviator": ("Aviator at Stake", "/aviator/"),
    "reserves": ("Audited reserves", "/reserves/"),
    "about-stake": ("About Stake.com", "/about-stake/"),
    "payments": ("Crypto payments", "/payments/"),
    "mirror": ("Mirror sites", "/mirror/"),
    "live-odds": ("Live odds", "/live-odds/"),
    "originals": ("Stake Originals", "/originals/"),
    "vip": ("VIP program", "/vip/"),
    "slots": ("Slots library", "/slots/"),
    "live-casino": ("Live casino", "/live-casino/"),
}

def build_rooms_block(current_slug):
    items = [f'<li><a href="{u}">{t}</a></li>' for slug, (t, u) in INTERNAL_LINKS.items() if slug != current_slug]
    return (
        '<aside class="rooms-grid" aria-label="Other rooms at WinnersClub" '
        'style="margin:60px 0 40px;padding:32px 24px;background:rgba(20,20,20,.5);'
        'border:1px solid rgba(255,215,0,.12);border-radius:14px;">'
        '<h3 style="font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#737378;'
        'margin:0 0 18px;font-weight:700;">Other rooms in the club</h3>'
        '<ul style="list-style:none;margin:0;padding:0;display:grid;grid-template-columns:'
        'repeat(auto-fit,minmax(180px,1fr));gap:8px 22px;">' + "".join(items) +
        '</ul></aside>'
    )

# -------------------------------------------------------------------
# 6. FAQ schema gap-fill — ensure key money pages have FAQPage JSON-LD
# -------------------------------------------------------------------
FAQ_BY_SLUG = {
    "promo-code": [
        ("What is the Stake promo code?", "The active code is MAXBET. Enter it at signup to unlock a 200% match up to $3,000 with 40x wagering on deposit plus bonus."),
        ("Does MAXBET work on Stake.com and Stake.us?", "Yes. On Stake.com it unlocks the 200% crypto match; on Stake.us it unlocks the Stake Cash and Gold Coin signup package."),
        ("Is the bonus from MAXBET better than the public Stake codes?", "Yes. Public codes typically max out at $100 reload value. MAXBET goes to $3,000 because it's bound to the WinnersClub affiliate path."),
        ("How long do I have to clear wagering?", "Stake gives you 30 days from deposit. After that the bonus expires and the wagering pot resets."),
    ],
    "payments": [
        ("Which cryptocurrencies does Stake accept?", "BTC, ETH, LTC, BCH, DOGE, SOL, USDT (ERC-20 + TRC-20), USDC, BNB, TRX, and XRP."),
        ("How fast are crypto withdrawals?", "Withdrawals on Stake clear within a few minutes for established players. New accounts may face one verification check on the first withdrawal."),
        ("Does Stake support fiat deposits?", "Stake.com is crypto-only. Stake.us uses USD packages for the Stake Cash / Gold Coin system."),
        ("Are there any fees on deposits or withdrawals?", "No platform fees. Network fees are passed through at cost — same as any on-chain transfer."),
    ],
    "reserves": [
        ("How big are Stake's audited reserves?", "Stake holds approximately $339.53M in on-chain tagged reserves as of the May 28 2026 snapshot, with the largest share in ETH (~74%) and remainder split across SOL, BTC, USDT, BNB and TRX."),
        ("Who audits the reserves?", "Reserves are tagged and verified by Arkham Intel, with the snapshot republished by cryptotips.com — a sister property of WinnersClub."),
        ("Why does proof-of-reserves matter?", "It tells you the operator has the liquidity to honour withdrawals. Most offshore books don't publish anything close to this."),
    ],
    "about-stake": [
        ("Who owns Stake.com?", "Stake.com is operated by Mliccom B.V., licensed in Curaçao under licence OGL/2024/1451/0918. The brand was founded in 2017."),
        ("Is Stake.com legit?", "Yes. Stake holds an active Curaçao master licence, publishes on-chain reserves, sponsors elite sport (UFC, F1, English Premier League clubs), and processes withdrawals in minutes."),
        ("Where is Stake licensed?", "Stake.com operates under Curaçao OGL/2024/1451/0918. Stake.us operates under sweepstakes rules in the United States."),
        ("Is Stake the same as Stake.us?", "Same brand, different products. Stake.com is the crypto sportsbook and casino. Stake.us is the sweepstakes-model casino legal across most US states."),
    ],
}

def build_faq_block(items):
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ]
    }
    return f'<script type="application/ld+json" data-ld="faq">{json.dumps(obj, ensure_ascii=False)}</script>'

# -------------------------------------------------------------------
# Pass over all html
# -------------------------------------------------------------------
stats = {"rooms": 0, "faq": 0, "skip_short": 0}

for p in ROOT.rglob("*.html"):
    sp = str(p)
    if "/node_modules/" in sp or "/.git/" in sp or "/build_helpers/" in sp or "/research/" in sp:
        continue
    rel = p.relative_to(ROOT).as_posix()
    txt = p.read_text(encoding="utf-8", errors="ignore")
    orig = txt

    # Detect current page slug
    parts = rel.split("/")
    current_slug = None
    for seg in parts:
        if seg in INTERNAL_LINKS:
            current_slug = seg
            break

    # 5. Inject rooms-grid before </body> if not already there
    if 'class="rooms-grid"' not in txt and "</body>" in txt and rel != "404.html":
        # Only on substantive pages (>5KB body content)
        body_len = len(txt)
        if body_len > 6000:
            txt = txt.replace("</body>", build_rooms_block(current_slug or "") + "</body>", 1)
            stats["rooms"] += 1
        else:
            stats["skip_short"] += 1

    # 6. FAQ JSON-LD gap-fill — only on EN versions of these slugs (locale variants have their own translated FAQ blocks)
    if current_slug in FAQ_BY_SLUG and 'data-ld="faq"' not in txt and "</head>" in txt:
        # Skip if page is NOT at root (don't blast EN FAQ into /ko/, /zh/ etc.)
        first_seg = parts[0] if parts else ""
        if first_seg in INTERNAL_LINKS or first_seg.endswith(".html"):
            faq = build_faq_block(FAQ_BY_SLUG[current_slug])
            txt = txt.replace("</head>", faq + "</head>", 1)
            stats["faq"] += 1

    if txt != orig:
        p.write_text(txt, encoding="utf-8")

print("--- SEO polish stats ---")
for k, v in stats.items():
    print(f"  {k}: {v}")
