#!/usr/bin/env python3
"""Generate unique OG cards (1200x630) per page with brand-correct typography."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re

ROOT = Path("/home/user/workspace/winnersclub.com")
OG_DIR = ROOT / "images" / "og"
OG_DIR.mkdir(parents=True, exist_ok=True)

# Find Inter + Playfair fonts in workspace
FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts",
    "/usr/share/fonts/opentype",
]
def find_font(name):
    for d in FONT_DIRS:
        for root, _, files in __import__("os").walk(d):
            for f in files:
                if name.lower() in f.lower():
                    return __import__("os").path.join(root, f)
    return None

font_bold = find_font("DejaVuSans-Bold") or find_font("Bold") or None
font_reg = find_font("DejaVuSans") or None

def make_og(title, subtitle, out_path):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), (10, 10, 11))
    d = ImageDraw.Draw(img)
    # Gold radial gradient simulation — concentric darker rings
    for i in range(300, 0, -10):
        alpha = int(60 * (1 - i/300))
        d.ellipse([W/2 - i*2, H/2 - i*1.5, W/2 + i*2, H/2 + i*1.5], fill=(20+alpha//4, 13+alpha//6, 8))
    # Velvet stripe at top
    d.rectangle([0, 0, W, 12], fill=(139, 10, 26))
    # Velvet stripe at bottom
    d.rectangle([0, H-12, W, H], fill=(139, 10, 26))
    # Gold W shield (simplified)
    shield_x, shield_y = 80, 80
    sx, sy = 110, 120
    d.polygon([(shield_x, shield_y), (shield_x + sx, shield_y), (shield_x + sx, shield_y + sy*0.7),
               (shield_x + sx/2, shield_y + sy), (shield_x, shield_y + sy*0.7)],
              fill=(255, 215, 0))
    d.polygon([(shield_x+15, shield_y+15), (shield_x+sx-15, shield_y+15), (shield_x+sx-15, shield_y+sy*0.65),
               (shield_x+sx/2, shield_y+sy-12), (shield_x+15, shield_y+sy*0.65)],
              fill=(10, 10, 11))
    # "W" letter
    try:
        f_w = ImageFont.truetype(font_bold, 70) if font_bold else ImageFont.load_default()
        d.text((shield_x+33, shield_y+22), "W", fill=(255, 215, 0), font=f_w)
    except Exception:
        pass
    # Brand wordmark right of shield
    try:
        f_brand = ImageFont.truetype(font_bold, 44) if font_bold else ImageFont.load_default()
        d.text((shield_x + sx + 30, shield_y + 30), "WinnersClub", fill=(255, 255, 255), font=f_brand)
        f_tag = ImageFont.truetype(font_reg, 18) if font_reg else ImageFont.load_default()
        d.text((shield_x + sx + 32, shield_y + 82), "the players' back room", fill=(255, 215, 0), font=f_tag)
    except Exception:
        pass
    # Title block
    try:
        f_title = ImageFont.truetype(font_bold, 76) if font_bold else ImageFont.load_default()
        f_sub = ImageFont.truetype(font_reg, 28) if font_reg else ImageFont.load_default()
        # Wrap title to 2 lines if needed
        lines = []
        words = title.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            bbox = d.textbbox((0,0), test, font=f_title)
            if bbox[2] - bbox[0] > 1050:
                lines.append(line); line = w
            else:
                line = test
        if line: lines.append(line)
        lines = lines[:3]
        y0 = 280
        for ln in lines:
            d.text((80, y0), ln, fill=(255, 215, 0), font=f_title)
            y0 += 86
        d.text((80, y0 + 6), subtitle, fill=(200, 200, 205), font=f_sub)
    except Exception as e:
        print("font err:", e)
    # Code chip bottom right
    try:
        f_code_label = ImageFont.truetype(font_reg, 16) if font_reg else ImageFont.load_default()
        f_code = ImageFont.truetype(font_bold, 38) if font_bold else ImageFont.load_default()
        d.text((W-280, H-110), "PROMO CODE", fill=(150, 150, 155), font=f_code_label)
        # Gold pill
        d.rounded_rectangle([W-280, H-85, W-80, H-35], radius=8, fill=(255, 215, 0))
        d.text((W-260, H-78), "MAXBET", fill=(26, 19, 8), font=f_code)
    except Exception:
        pass
    img.save(out_path, "PNG", optimize=True)

# Map of page → (title, subtitle)
PAGES = {
    "default": ("Stake Promo Code MAXBET", "200% match up to $3,000 — the back room is open"),
    "promo-code": ("MAXBET unlocks the back room", "200% match up to $3,000 at Stake.com"),
    "casino": ("Casino floor at Stake", "Slots, originals, live tables — and the Stake edge"),
    "sports": ("Stake sportsbook", "Boosted odds, parlays, and live in-play"),
    "poker": ("Poker at Stake", "Cash games, MTTs, and the rake-back nobody talks about"),
    "aviator": ("Aviator at Stake", "Multiplier rises until it crashes — cash before it does"),
    "reserves": ("Reserves audited at $339M", "On-chain proof of solvency — Arkham verified"),
    "about-stake": ("About Stake.com", "The platform behind the MAXBET code"),
    "payments": ("Stake crypto payments", "BTC, ETH, SOL, USDT, BNB, TRX — instant in, instant out"),
    "mirror": ("Stake mirror sites", "Official alternate access points"),
    "live-odds": ("Live odds at Stake", "Real-time markets across every sport"),
    "originals": ("Stake Originals", "Plinko, Mines, Crash, Limbo — the house games"),
    "stake-engine": ("Stake Engine", "What powers Stake's odds and proof-of-fairness"),
    "vip": ("VIP at Stake", "Tiered rewards, weekly boosts, account managers"),
    "slots": ("Slots at Stake", "Thousands of titles — sorted by RTP, not noise"),
    "live-casino": ("Live casino at Stake", "Roulette, blackjack, baccarat — real dealers, real time"),
    "responsible-gambling": ("Play responsibly at Stake", "Limits, cool-offs, self-exclusion tools"),
    "news": ("WinnersClub news", "What's moving at Stake this week"),
    "stake-us-bonus": ("Stake.us promo code MAXBET", "Free SC + Gold Coin package for US players"),
}

count = 0
for slug, (t, s) in PAGES.items():
    out = OG_DIR / f"{slug}.png"
    make_og(t, s, out)
    count += 1
    print(f"  + {out.name}")

# Default at root og-default.png + og-default-2026.png
make_og(PAGES["default"][0], PAGES["default"][1], ROOT / "images" / "og-default.png")
print(f"\nGenerated {count + 1} OG cards")
