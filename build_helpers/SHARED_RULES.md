# SHARED RULES for all new pages (read this first)

## Hard rules (must pass automated checks)

1. **No em dashes (—), no en dashes (–)** anywhere — body, title, meta, alt, JSON-LD
2. **Brand**: always lowercase `1win` in body copy (never `1WIN` or `1 win`)
3. **Promo code**: always `XLBONUS` in monospace `<span class="code-highlight">XLBONUS</span>`
4. **Curaçao 8048/JAZ** trust signal must appear in first 150 words of every page
5. **Specific numbers only**: "12,000+ slots", "40,000+ markets", "400,000+ players" — NEVER "thousands of", "hundreds of", "many"
6. **CTA verbs**: ONLY use → Register, Claim, Open, Start, Play, Access, Get. NEVER: Sign Up, Join, Bet, Watch, Explore, Enter, Use, Take, Visit, Read, View
7. **H2 case**: Sentence case (not ALL CAPS). Keep XLBONUS, VIP, FAQ, RTP, KYC, UPI, PIX, APK, USDT, NFT uppercase.
8. **Banned phrases** (case-insensitive): "HIT THE TABLES", "DOMINATE EVERY MATCH", "OUTPLAY EVERYONE", "no strings attached", "BET ANYWHERE WIN EVERYWHERE", "thousands of", "hundreds of", "many of", "world-class", "cutting-edge", "next-generation", "state-of-the-art"
9. **First paragraph rule**: brand + XLBONUS + one specific number + Curaçao 8048/JAZ — all four signals in opening paragraph
10. **External links**: any outbound link to a competitor or source needs `rel="nofollow noopener"` and opens in same tab unless data viz
11. **No fake reviews/ratings**: do NOT invent user counts, star ratings, "rated 4.8/5 by users" — use verifiable facts only
12. **Affiliate CTAs**: primary CTA always links to `https://winnersclub.com/en/register?promo=XLBONUS` (the on-site register page, not external)

## Page template usage

```python
from build_helpers.page_template import render_page
html = render_page(
    slug='...',          # path after /en/
    title='...',         # 50-65 chars, brand + benefit + XLBONUS
    description='...',   # 145-160 chars, includes XLBONUS and a number
    h1='...',            # Sentence case, mirrors title concept
    breadcrumbs=[('Home','/en/'), ('Section','/en/section/'), ('Current page', None)],
    main_html='...',     # body HTML, no <main>, no <h1> (template adds them)
    extra_head='',       # optional extra <head> tags
    extra_scripts='',    # optional inline JS
    extra_schema='',     # optional extra JSON-LD <script> blocks
)
open('en/<slug>.html','w').write(html)
```

## Body HTML structure (recommended)

```html
<section class="lede">
  <p>First paragraph with brand + <span class="code-highlight">XLBONUS</span> + specific number + Curaçao 8048/JAZ.</p>
</section>

<section class="key-facts">
  <h2>Key facts</h2>
  <table class="facts-table">...</table>
</section>

<section class="how-to">
  <h2>How to ...</h2>
  <ol>...</ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://winnersclub.com/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Question?</summary><p>Answer.</p></details>
</section>
```

## FAQ schema (add via `extra_schema=` param)

```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"...?","acceptedAnswer":{"@type":"Answer","text":"..."}}
  ]
}
</script>
```

## Word counts

- Calculator tool pages: 600-900 words intro/explainer below the tool
- Slot reviews: 1,000-1,400 words
- Crash game guides: 800-1,200 words
- Bonus-type pages: 700-1,000 words
- Sport landings: 1,200-1,800 words
- Payment method pages: 700-1,000 words
- Provider hub pages: 1,000-1,500 words
- India state pages: 700-1,000 words

## File locations

- Tools: `en/tools/odds-converter.html`, `en/tools/parlay-calculator.html` etc.
- Slots: `en/slots/sweet-bonanza.html`, `en/slots/gates-of-olympus.html` etc.
- Crash games: `en/crash/jetx.html`, `en/crash/spaceman.html` etc.
- Bonus pages: `en/bonus/second-deposit.html`, `en/bonus/free-spins-today.html` etc.
- Sport landings: `en/sports/football.html`, `en/sports/cricket.html` etc.
- Payment methods: `en/payments/upi.html`, `en/payments/pix.html`, `en/payments/usdt.html` etc.
- Provider hubs: `en/providers/pragmatic-play.html`, `en/providers/evolution.html` etc.
- India states: `en/india/maharashtra.html`, `en/india/tamil-nadu.html` etc.

CREATE THE DIRECTORY before writing files: `os.makedirs('en/tools', exist_ok=True)`

## Verification before reporting done

Each subagent MUST run before completing:

```python
import os, re, glob
files = glob.glob('en/<your-dir>/*.html')
for f in files:
    t = open(f).read()
    assert '—' not in t, f'em dash in {f}'
    assert '–' not in t, f'en dash in {f}'
    for b in ['HIT THE TABLES','DOMINATE EVERY MATCH','OUTPLAY EVERYONE','no strings attached','thousands of','hundreds of','world-class','cutting-edge']:
        assert b.lower() not in t.lower(), f'banned "{b}" in {f}'
    assert 'XLBONUS' in t, f'no XLBONUS in {f}'
    assert 'Curaçao' in t or 'Curacao' in t, f'no Curacao trust signal in {f}'
print(f'PASS {len(files)} files')
```
