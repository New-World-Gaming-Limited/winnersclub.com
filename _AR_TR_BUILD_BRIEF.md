# BUILD BRIEF — Arabic (/ar/) + Turkish (/tr/) refresh to KO quality

## Mission
1. **Build /ar/ from scratch**: 19 Arabic pages in Modern Standard Arabic (MSA), full RTL (dir="rtl"), matching the **Korean (/ko/) gold standard** for depth and structure.
2. **Refresh /tr/ to KO quality**: Many TR pages are ~50% the depth of KO equivalents. Expand them to match (translate the missing KO content into Turkish, preserve already-good TR content).

The site is at `/home/user/workspace/winnersclub.com/`. Cloudflare Pages auto-deploys on push to `main`.

## Quality bar (KO is the gold standard)
| Page | TR current | KO target | Action |
|------|-----------|-----------|--------|
| index.html | 4085w | 4195w | TR is fine, minor polish |
| about-stake | 2486w | **7416w** | TR needs ~5000 more words |
| aviator | 2559w | **5850w** | TR needs ~3300 more words |
| casino | 2294w | **7979w** | TR needs ~5700 more words |
| live-casino | 2880w | 3079w | Fine |
| live-odds | 2238w | 3048w | Add ~800 words |
| mirror | 2585w | **7779w** | TR needs ~5200 more words |
| news | 3009w | 3063w | Fine |
| originals | 3296w | 4059w | Add ~800 words |
| payments | 2278w | **6342w** | TR needs ~4000 more words |
| poker | 2247w | **5357w** | TR needs ~3100 more words |
| promo-code | 2502w | **6490w** | TR needs ~4000 more words |
| reserves | 2331w | **6028w** | TR needs ~3700 more words |
| responsible-gambling | 3401w | 3343w | Fine |
| slots | 2697w | 3479w | Add ~780 words |
| sports | 3283w | **6787w** | TR needs ~3500 more words |
| stake-engine | 2731w | 2989w | Fine |
| stake-us-bonus | 2252w | **5835w** | TR needs ~3500 more words |
| vip | 3142w | 3671w | Add ~530 words |

For **/ar/**: every page should match the KO word count target (the right-hand column).

## Hard rules (CRITICAL — never violate)

### Source authority (NEVER cite competitor affiliates)
ONLY cite: stake.com, stake.us, help.stake.com, freetips.com, cryptotips.com, Arkham, Phemex, Wikipedia, regulators (Curaçao OGL, GCB, etc.)

### Voice/style
- **BANNED everywhere**: em-dashes (—), en-dashes (–), exclamation marks, emojis, the phrase "Welcome to WinnersClub", blue/purple/teal colors
- Sultry Vegas concierge voice
- Always frame Stake positively, never call Stake.com "banned" or "restricted" anywhere
- Use Stake's own terminology (200% match, 40x wagering, KYC Level 3, on-chain reserves)

### Brand tokens (NEVER translate, NEVER change)
- `MAX3000` (always uppercase, wrap in `<span class="code-highlight">MAX3000</span>` for visual highlight)
- Stake.com, Stake.us, Medium Rare NV, Curaçao OGL/2024/1451/0918, Sweepsteaks Limited
- Ed Craven, Bijan Tehrani
- Arkham Intel, Phemex
- GGR $4.7B, 21M+ accounts, $339M on-chain reserves, 40x wagering, 200% match, $3,000 max
- KYC Level 3
- Stake.com affiliate URL: `https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000`
- Stake.us affiliate URL: `https://stake.us/?c=MAX3000`

### Arabic-specific RTL requirements
- `<html lang="ar" dir="rtl">`
- Numbers stay in **Western digits (0-9)**, NOT Eastern Arabic (٠-٩). Stake displays Western digits.
- Currencies: `$3,000` stays LTR. USD symbol stays $.
- URLs, brand names, code (`MAX3000`) stay LTR.
- Use `<bdi>` or `<span dir="ltr">` around LTR-island text inside Arabic flow (e.g. `<bdi dir="ltr">MAX3000</bdi>`)
- Wrap Latin-only tokens in `<span dir="ltr">` or use HTML entities so they don't break direction
- All punctuation should use Arabic forms where applicable: `،` (Arabic comma) instead of `,`, `؟` (Arabic question mark) instead of `?`, `؛` (Arabic semicolon) — BUT keep `.` (period) as-is, and keep `,` inside numbers like `$3,000`.

### CSS for RTL (you must add these overrides to `style.css`)
Add a block at the end of style.css that scopes RTL overrides to `[dir="rtl"]`:

```css
/* === RTL overrides for /ar/ locale === */
[dir="rtl"] .header-nav { flex-direction: row-reverse; }
[dir="rtl"] .header-inner { direction: rtl; }
[dir="rtl"] .header-actions { flex-direction: row-reverse; }
[dir="rtl"] body, [dir="rtl"] .hero-text, [dir="rtl"] main, [dir="rtl"] footer { text-align: right; }
[dir="rtl"] .breadcrumb { direction: rtl; }
[dir="rtl"] .rooms-grid { direction: rtl; }
[dir="rtl"] .code-highlight, [dir="rtl"] [dir="ltr"] { direction: ltr; display: inline-block; unicode-bidi: isolate; }
[dir="rtl"] .footer-cols, [dir="rtl"] .footer-bottom { direction: rtl; text-align: right; }
[dir="rtl"] .promo-strip { direction: rtl; }
[dir="rtl"] .hero-cta, [dir="rtl"] .cta-row { flex-direction: row-reverse; }
[dir="rtl"] table { direction: rtl; }
[dir="rtl"] table th, [dir="rtl"] table td { text-align: right; }
[dir="rtl"] ul, [dir="rtl"] ol { padding-right: 1.5em; padding-left: 0; }
[dir="rtl"] blockquote { border-right: 3px solid var(--gold); border-left: none; padding-right: 1em; padding-left: 0; }
[dir="rtl"] .card { text-align: right; }
[dir="rtl"] h1, [dir="rtl"] h2, [dir="rtl"] h3, [dir="rtl"] h4 { text-align: right; }
/* Number tokens always LTR */
[dir="rtl"] .code-highlight, [dir="rtl"] .num, [dir="rtl"] bdi { direction: ltr; unicode-bidi: bidi-override; }
```

Then run `cp style.css style.min.css` after editing.

## Approach (recommended)

### Step 1: Copy /ko/ as the template for /ar/
```bash
cp -r ko ar
```
Then iterate over every file in `/ar/`, replacing:
- `<html lang="ko">` → `<html lang="ar" dir="rtl">`
- All Korean text → Arabic (MSA) translations
- URL paths `/ko/` → `/ar/` (in canonical, og:url, breadcrumb JSON-LD, internal links)
- `lang="ko"` attributes → `lang="ar"`
- Title format: keep brand structure but translate body
- hreflang block: add `<link rel="alternate" hreflang="ar" href="https://winnersclub.com/ar/[path]">` to all 16 locales

### Step 2: Refresh /tr/ to match KO depth
For each underweight TR page (about-stake, aviator, casino, mirror, payments, poker, promo-code, reserves, sports, stake-us-bonus): pull the missing content sections from the equivalent KO page, translate to natural Turkish, and append/integrate into the existing TR page. **Preserve the existing TR header/footer/nav/promo strip — only rebuild the main content body.**

### Step 3: Update hreflang on ALL 285+ pages to include `ar`
Every page in the site (en, ko, zh, vi, th, ms, pt, ja, es, pt-br, tr, id, fr, ru, hi, ar) needs a 16-entry hreflang block + x-default = 17 link tags total.

### Step 4: Update language switcher on ALL pages to include AR
Desktop switcher (`<select class="lang-switcher">`):
```html
<option value="https://winnersclub.com/ar/">العربية</option>
```
Mobile switcher (`<div class="mobile-lang-block">`):
```html
<option value="/ar/">العربية (Arabic)</option>
```

### Step 5: Update sitemap.xml
Add all 19 /ar/ URLs.

### Step 6: Update lang-redirect.js
Add Arabic country mappings:
- ar: ['SA', 'AE', 'EG', 'IQ', 'JO', 'KW', 'LB', 'LY', 'MA', 'OM', 'PS', 'QA', 'SY', 'TN', 'YE', 'BH', 'DZ', 'SD', 'MR']

## Arabic translation guidance

### Tone
Use MSA. Keep it premium, slightly aspirational, technical-precise. Think Al Jazeera / The National (UAE) editorial register. NOT colloquial/spoken Arabic.

### Key terminology
- Promo code → **رمز ترويجي** (ramz tarweeji)
- Bonus → **مكافأة** (mukaafaa)
- Casino → **كازينو** (kazino) — direct transliteration, this is the standard
- Sports betting → **المراهنات الرياضية** (al-muraahanaat al-riyaadhiyya)
- Sign up → **التسجيل** (al-tasjeel) or **سجل** (sajjil)
- Welcome bonus → **مكافأة الترحيب** (mukaafaat al-tarheeb)
- Deposit → **إيداع** (eedaa3)
- Withdrawal → **سحب** (sahb)
- Wagering requirement → **متطلبات الرهان** (mutatallabat al-rihaan)
- Up to → **حتى** (hattaa)
- Mirror site → **موقع مرآة** (mawqi3 mir2aah) or **رابط بديل** (raabit badeel)
- Reserves → **الاحتياطيات** (al-ihtiyaatiyaat)
- VIP → **VIP** (keep Latin) or **كبار اللاعبين** (kibaar al-laa3ibeen)
- Crypto → **العملات الرقمية** (al-3umlaat al-raqmiyya)
- Live dealer → **موزع مباشر** (muwazzi3 mubaashir)
- Slots → **سلوتس** or **ماكينات القمار** (makaainat al-qimaar)
- Poker → **بوكر** (boker) — transliteration

### Sample Arabic title for promo-code page
"رمز Stake الترويجي MAX3000 - مكافأة 200% حتى $3,000 عند التسجيل"

### Sample Arabic title for home
"وينرز كلوب - النادي الداخلي للاعبي Stake | الرمز MAX3000"

### Sample Arabic title for casino
"كازينو Stake - أكثر من 3000 لعبة مع الرمز MAX3000"

## Deliverable checklist
- [ ] /ar/ folder with 19 HTML files (index + 18 subdirs each with index.html)
- [ ] All /ar/ pages have `<html lang="ar" dir="rtl">`
- [ ] All /ar/ pages have full 16+1 hreflang block
- [ ] All /ar/ pages have JSON-LD (WebPage, Organization, BreadcrumbList, FAQPage where relevant) with Arabic strings
- [ ] All /tr/ underweight pages expanded to match KO depth
- [ ] style.css has [dir="rtl"] overrides appended (and style.min.css = cp of style.css)
- [ ] sitemap.xml regenerated with /ar/ URLs (19 added)
- [ ] lang-redirect.js updated with Arabic country mappings
- [ ] ALL 285+ existing pages updated to include `ar` in hreflang block
- [ ] ALL 285+ existing pages updated to include `العربية` in desktop+mobile switcher
- [ ] Git commit (clean message), push to main
- [ ] Verify live: `curl -sL https://winnersclub.com/ar/ | grep -E "<title|dir="`

## CRITICAL gotchas (from previous build)
1. **Don't strip diacritics!** Arabic must keep all its diacritics (شدة، فتحة، كسرة) — but Arabic written content typically omits short vowels (تشكيل) and that's correct. The issue is don't accidentally remove letter dots or hamza. Test with `grep -oE 'إ|أ|ؤ|ئ|ء|ى|ة' ar/index.html` and ensure these appear.
2. **Cache buster**: bump CSS to `v=20260618a` and JS to `v=20260618a` on /ar/ pages (or all pages if convenient).
3. **rooms-grid section** at bottom of pages must be localized to Arabic (translate "Other rooms at WinnersClub" → "غرف أخرى في وينرز كلوب").
4. **Footer must be localized** including disclaimer, RG text, "Be Gamble Aware" → "كن واعيًا بالقمار" or similar.
5. **Pull before commit**: `git pull --no-rebase --no-edit origin main`
6. **Push with creds**: `api_credentials=["github"]`

## File locations & infra
- Repo: `https://git-agent-proxy.perplexity.ai/New-World-Gaming-Limited/winnersclub.com.git`
- Workspace: `/home/user/workspace/winnersclub.com/`
- GitHub creds: `api_credentials=["github"]`
- Cloudflare Pages: auto-deploys on push to main
- Existing CSS at: style.css (and style.min.css)
- Existing JS at: lang-redirect.js, exit-tracker.js
- Sitemap at: sitemap.xml

## Translation key facts for content
- Promo code: **MAX3000**
- Match: **200% deposit match**
- Max bonus: **$3,000**
- Min qualifying deposit: **$10**
- Max qualifying deposit: **$1,500** (deposit $1,500 to hit the full $3,000 bonus)
- Wagering: **40x** on (deposit + bonus)
- Time to credit: **24-48 hours** after first qualifying deposit via Stake live chat
- KYC: **Level 3 required** (photo ID + proof of address + source of funds)
- Stake.com facts: Founded 2017 by Ed Craven and Bijan Tehrani; Medium Rare NV; Curaçao OGL/2024/1451/0918; GGR $4.7B; 21M+ accounts; $339M on-chain reserves; available in 100+ countries
- Stake.us facts: Sweepstakes model (Gold Coins + Stake Cash); operated by Sweepsteaks Limited; 21+; not real-money gambling; US-only
- Mirror domains (Stake.com only): stake.ac, stake.bet, stake.games
