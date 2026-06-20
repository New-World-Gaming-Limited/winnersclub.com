#!/usr/bin/env python3
"""
Regenerate 19 OG images (1200x630 PNG) for winnersclub.com.

Brand: WinnersClub, sultry Vegas concierge.
Palette: gold #FFD700 + velvet #8b0a1a (deep velvet bg, gold type).
Code: MAX3000 (uppercase).
Zero em-dashes. Zero en-dashes. No "MAXBET".
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT = Path("/home/user/workspace/winnersclub.com/images/og")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630

# Palette
VELVET_DARK = (38, 6, 10)        # near-black velvet
VELVET = (89, 10, 24)             # #590a18-ish
VELVET_MID = (139, 10, 26)        # #8b0a1a
GOLD = (255, 215, 0)              # #FFD700
GOLD_SOFT = (212, 175, 55)        # #D4AF37
CREAM = (245, 232, 200)
INK = (20, 4, 6)

# Fonts
F_SERIF_BLACK = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Black.ttf"
F_SERIF = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Pages: filename -> (eyebrow, title, subtitle)
PAGES = {
    "default.png":             ("WINNERSCLUB",       "Welcome to the Back Room",    "200% match up to $3,000 with code MAX3000"),
    "about-stake.png":         ("THE HOUSE",         "Inside Stake",                "Who runs the floor, and why we play here"),
    "aviator.png":             ("HIGH ALTITUDE",     "Aviator",                     "Cash out before the plane disappears"),
    "casino.png":              ("THE CASINO FLOOR",  "Stake Casino",                "Slots, table games, and live dealers under one roof"),
    "live-casino.png":         ("AFTER HOURS",       "Live Casino",                 "Real dealers, real cards, real time"),
    "live-odds.png":           ("THE TICKER",        "Live Odds",                   "Lines that move the moment the play does"),
    "mirror.png":              ("SIDE DOORS",        "Stake Mirrors",               "Working backups when the front door is locked"),
    "news.png":                ("THE WIRE",          "Stake News",                  "Promotions, product drops, payout stories"),
    "originals.png":           ("HOUSE EXCLUSIVES",  "Stake Originals",             "Crash, Plinko, Mines, Limbo, and the rest"),
    "payments.png":            ("THE CAGE",          "Deposits and Withdrawals",    "Crypto, cards, and clean payouts"),
    "poker.png":               ("THE FELT",          "Poker on Stake",              "Cash games, tournaments, and weekend grinds"),
    "promo-code.png":          ("THE COMP",          "Promo Code MAX3000",          "200% match up to $3,000 on your first deposit"),
    "reserves.png":            ("THE VAULT",         "Stake Reserves",              "Proof of funds, on-chain and verified"),
    "responsible-gambling.png":("THE PIT BOSS",      "Play Responsibly",            "Limits, timeouts, and self-exclusion tools"),
    "slots.png":               ("THE REELS",         "Stake Slots",                 "Thousands of titles, all the big studios"),
    "sports.png":              ("THE BOOK",          "Stake Sportsbook",            "Every league, every market, every minute"),
    "stake-engine.png":        ("UNDER THE HOOD",    "Stake Engine",                "The infrastructure behind the floor"),
    "stake-us-bonus.png":      ("THE US FLOOR",      "Stake.us Bonus",              "Sweepstakes play with code MAX3000"),
    "vip.png":                 ("THE VIP ROOM",      "Stake VIP",                   "Rakeback, reloads, and a host who answers"),
}

assert len(PAGES) == 19


def _grad_bg():
    """Velvet radial gradient with vignette."""
    img = Image.new("RGB", (W, H), VELVET_DARK)
    px = img.load()
    cx, cy = W * 0.62, H * 0.45
    maxd = (W ** 2 + H ** 2) ** 0.5
    for y in range(H):
        for x in range(W):
            dx, dy = x - cx, y - cy
            d = (dx * dx + dy * dy) ** 0.5 / maxd
            t = min(1.0, d * 1.6)
            r = int(VELVET_MID[0] * (1 - t) + VELVET_DARK[0] * t * 0.85)
            g = int(VELVET_MID[1] * (1 - t) + VELVET_DARK[1] * t * 0.85)
            b = int(VELVET_MID[2] * (1 - t) + VELVET_DARK[2] * t * 0.85)
            px[x, y] = (r, g, b)
    return img


def _diamond_overlay(img):
    """Subtle diamond-quilt pattern over background."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    step = 60
    for y in range(-step, H + step, step):
        for x in range(-step, W + step, step * 2):
            ox = x + (step if (y // step) % 2 else 0)
            pts = [(ox, y - step // 2), (ox + step, y), (ox, y + step // 2), (ox - step, y)]
            d.polygon(pts, outline=(255, 215, 0, 14))
    img.alpha_composite(overlay) if img.mode == "RGBA" else img.paste(overlay, (0, 0), overlay)
    return img


def _draw_shield(draw, cx, cy, r):
    """Gold WC shield — diamond rotated square with WC monogram."""
    # outer diamond
    pts_outer = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    draw.polygon(pts_outer, fill=GOLD)
    # inner diamond inset
    ri = int(r * 0.78)
    pts_inner = [(cx, cy - ri), (cx + ri, cy), (cx, cy + ri), (cx - ri, cy)]
    draw.polygon(pts_inner, fill=VELVET_DARK)
    # WC monogram
    try:
        f = ImageFont.truetype(F_SERIF_BLACK, int(r * 0.85))
    except Exception:
        f = ImageFont.load_default()
    text = "WC"
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1] - 6), text, font=f, fill=GOLD)


def _fit_font(path, text, max_w, start_size, min_size=28):
    size = start_size
    while size > min_size:
        try:
            f = ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.load_default()
        bbox = f.getbbox(text)
        if (bbox[2] - bbox[0]) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(path, min_size)


def render(filename, eyebrow, title, subtitle):
    img = _grad_bg().convert("RGBA")
    img = _diamond_overlay(img)
    draw = ImageDraw.Draw(img)

    # Gold hairline frame
    margin = 28
    draw.rectangle([margin, margin, W - margin, H - margin], outline=GOLD_SOFT, width=2)
    inner = margin + 10
    draw.rectangle([inner, inner, W - inner, H - inner], outline=(212, 175, 55, 120), width=1)

    # Shield top-left
    _draw_shield(draw, cx=130, cy=130, r=58)

    # Wordmark next to shield
    f_brand = ImageFont.truetype(F_SERIF_BLACK, 38)
    draw.text((200, 88), "WINNERSCLUB", font=f_brand, fill=GOLD)
    f_brand_sub = ImageFont.truetype(F_SANS, 18)
    draw.text((202, 138), "The back room is open", font=f_brand_sub, fill=GOLD_SOFT)

    # Eyebrow
    f_eye = ImageFont.truetype(F_SANS_B, 22)
    eyebrow_text = eyebrow.upper()
    draw.text((80, 230), eyebrow_text, font=f_eye, fill=GOLD_SOFT)
    # gold underline
    eb_bbox = f_eye.getbbox(eyebrow_text)
    eb_w = eb_bbox[2] - eb_bbox[0]
    draw.line([(80, 264), (80 + eb_w, 264)], fill=GOLD, width=2)

    # Title — fit to width
    max_title_w = W - 160
    f_title = _fit_font(F_SERIF_BLACK, title, max_title_w, 92, min_size=46)
    draw.text((80, 290), title, font=f_title, fill=CREAM)

    # Subtitle (wrap if needed)
    f_sub = ImageFont.truetype(F_SANS, 28)
    # Simple wrap at ~60 chars
    words = subtitle.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if f_sub.getbbox(test)[2] <= W - 160:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    y_sub = 420
    for ln in lines[:2]:
        draw.text((80, y_sub), ln, font=f_sub, fill=(230, 220, 200))
        y_sub += 38

    # Promo chip bottom-right
    chip_text = "CODE: MAX3000"
    f_chip = ImageFont.truetype(F_SANS_B, 26)
    cb = f_chip.getbbox(chip_text)
    cw, ch = cb[2] - cb[0], cb[3] - cb[1]
    pad_x, pad_y = 22, 14
    chip_w = cw + pad_x * 2
    chip_h = ch + pad_y * 2 + 6
    x1 = W - 80 - chip_w
    y1 = H - 100 - chip_h
    x2 = x1 + chip_w
    y2 = y1 + chip_h
    # gold fill chip
    draw.rounded_rectangle([x1, y1, x2, y2], radius=8, fill=GOLD)
    draw.text((x1 + pad_x, y1 + pad_y - 2), chip_text, font=f_chip, fill=INK)

    # Domain footer
    f_dom = ImageFont.truetype(F_SANS_B, 22)
    draw.text((80, H - 80), "winnersclub.com", font=f_dom, fill=GOLD)

    # Save
    img.convert("RGB").save(OUT / filename, "PNG", optimize=True)
    print(f"  wrote {filename}")


for fn, (eb, t, s) in PAGES.items():
    # Guardrail: assert no em/en dash and no 'MAXBET'
    for v in (eb, t, s):
        assert "—" not in v and "–" not in v, f"dash in {fn}"
        assert "MAXBET" not in v.upper(), f"MAXBET in {fn}"
    render(fn, eb, t, s)

print("done.")
