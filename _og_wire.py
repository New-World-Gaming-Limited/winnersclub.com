#!/usr/bin/env python3
"""Wire each page to its specific OG image based on URL path."""
import re
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")

PAGE_OG = {
    "promo-code": "promo-code.png", "casino": "casino.png", "sports": "sports.png",
    "poker": "poker.png", "aviator": "aviator.png", "reserves": "reserves.png",
    "about-stake": "about-stake.png", "payments": "payments.png", "mirror": "mirror.png",
    "live-odds": "live-odds.png", "originals": "originals.png", "stake-engine": "stake-engine.png",
    "vip": "vip.png", "slots": "slots.png", "live-casino": "live-casino.png",
    "responsible-gambling": "responsible-gambling.png", "news": "news.png",
    "stake-us-bonus": "stake-us-bonus.png",
}

og_img_re = re.compile(r'<meta property="og:image" content="[^"]*"\s*/?>')
twitter_img_re = re.compile(r'<meta name="twitter:image" content="[^"]*"\s*/?>')

count = 0
for p in ROOT.rglob("*.html"):
    s = str(p)
    if "/node_modules/" in s or "/.git/" in s or "/build_helpers/" in s or "/research/" in s:
        continue
    rel = p.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    # Find the page slug — last meaningful segment
    page_slug = None
    for seg in parts:
        if seg in PAGE_OG:
            page_slug = seg
            break
    og_file = PAGE_OG.get(page_slug, "default.png") if page_slug else "default.png"
    # Home pages of locales also get default.png
    og_url = f"https://winnersclub.com/images/og/{og_file}"
    txt = p.read_text(encoding="utf-8", errors="ignore")
    orig = txt
    txt = og_img_re.sub(f'<meta property="og:image" content="{og_url}">', txt)
    if 'twitter:image' in txt:
        txt = twitter_img_re.sub(f'<meta name="twitter:image" content="{og_url}">', txt)
    else:
        # Inject if missing — add before </head>
        if 'og:image' in txt and 'twitter:image' not in txt and '</head>' in txt:
            txt = txt.replace('</head>', f'<meta name="twitter:image" content="{og_url}"><meta name="twitter:card" content="summary_large_image"></head>', 1)
    if txt != orig:
        p.write_text(txt, encoding="utf-8")
        count += 1

print(f"Updated OG images on {count} files")
