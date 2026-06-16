# WinnersClub.com — 7-Locale Expansion Build Brief

## Mission
Add 7 new locale directories matching the quality bar of the existing `/ko/` and `/ja/` builds:
- `/es/` — LATAM Spanish (neutral, Mexico/Argentina/Colombia/Chile)
- `/pt-br/` — Brazilian Portuguese (NEW, **do NOT** modify existing `/pt/` which stays as-is)
- `/tr/` — Turkish (formal)
- `/id/` — Indonesian (Bahasa Indonesia)
- `/fr/` — French (international neutral, covers Quebec + Francophone Africa)
- `/ru/` — Russian
- `/hi/` — Hindi (Devanagari, transliterated brand terms allowed)

Each locale = **19 pages**: `index.html` (home) + 18 sub-pages mirroring this slug list:
about-stake, aviator, casino, live-casino, live-odds, mirror, news, originals, payments, poker, promo-code, reserves, responsible-gambling, slots, sports, stake-engine, stake-us-bonus, vip

Total: **7 × 19 = 133 new HTML files**

## Repo
- Workspace: `/home/user/workspace/winnersclub.com/`
- Already on `main` branch, latest pulled
- Push with `api_credentials=["github"]`
- Cloudflare Pages auto-deploys on push

## Reference locales to clone from
Use **`/ko/`** as your structural template (it's the most thoroughly translated and has the latest fixes including the GSC promo-strip).
- `ko/index.html` → template for all home pages
- `ko/promo-code/index.html` → template for promo-code pages
- `ko/about-stake/index.html` → template for about-stake
- etc.

## CRITICAL site-wide voice rules (active, preserve verbatim)

### BANNED across all locales
- **em dashes (—)** — replace with regular hyphen `-` or rephrase
- **en dashes (–)** — same
- **exclamation marks** — never used in WinnersClub voice
- **emojis** — never
- Phrase "Welcome to WinnersClub" or equivalent localised "welcome" greetings
- Blue/purple/teal colors (only #FFD700 gold + #8b0a1a velvet)

### Voice: sultry Vegas concierge
- Tone is insider, knowing, slightly seductive but never crass
- Korean/Japanese pages are the gold standard reference
- Treat the reader like a guest the bouncer just waved through
- Never say "Stake is banned in X" or note restrictions — frame Stake background positively

### Source policy (CRITICAL)
Only cite from these sources, NEVER competitor affiliates:
- First-party: stake.com, stake.us, help.stake.com
- Sister sites: freetips.com, cryptotips.com
- Trust: Arkham (arkhamintelligence.com), Phemex
- Wikipedia, regulators

### Required preserved tokens (DO NOT TRANSLATE)
- **MAX3000** (promo code) — always uppercase, always in `<span class="code-highlight">MAX3000</span>` for emphasis
- **Stake.com**, **Stake.us** — brand names verbatim
- **Medium Rare NV** — operator name
- **Curaçao OGL/2024/1451/0918** — licence string
- **Sweepsteaks Limited** — Stake.us operator
- **Ed Craven**, **Bijan Tehrani** — founder names
- **GGR $4.7B**, **$3,000**, **$339M**, **40x**, **200%** — keep numerals
- **Arkham Intel** — data source

### Affiliate URLs (verbatim, do not modify)
- Stake.com primary: `https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000`
- Stake.us: `https://stake.us/?c=MAX3000`

### Internal links
All internal links in `/es/` pages must use `/es/` prefix (e.g. `/es/promo-code/` not `/promo-code/`).
Same for every new locale.

## Page anatomy (study /ko/index.html line-by-line)

Each page has:
1. `<!DOCTYPE html>` + `<html lang="XX">` (use the BCP-47 code: `es`, `pt-BR`, `tr`, `id`, `fr`, `ru`, `hi`)
2. `<head>` with:
   - `<title>` 50-65 chars, includes "Stake" + "MAX3000" + benefit in target language
   - `<meta name="description">` 140-160 chars
   - canonical: `https://winnersclub.com/<locale>/<slug>/`
   - **9 + N hreflang alternates** (en, ko, zh-Hans, vi, th, ms, pt, ja PLUS new locales: es, pt-BR, tr, id, fr, ru, hi, x-default)
   - Open Graph + Twitter cards
   - JSON-LD blocks (Organization, WebSite, Breadcrumb, FAQPage where applicable)
   - `<link rel="stylesheet" href="/style.min.css?v=20260616c">` (current cache version)
3. Inline `<script>document.documentElement.classList.add("js-anim");</script>` in head (mobile animation gating, MANDATORY)
4. `<body>` with:
   - Header `<header class="site-header">` with nav (localized labels) + language switcher
   - `<section class="club-hero">` with `.ch-bg`, `.ch-overlay`, `.ch-content`
   - `<div class="reserves-ticker">` with on-chain reserve facts
   - Sections matching /ko/ home layout
   - `<aside class="promo-strip">` for home (KO/MS pattern — extend to ALL new locales' home pages)
   - Sticky CTA bar
   - Footer
5. `<script src="/script.min.js?v=20260616a" defer></script>`

## Hreflang block — full set after rollout

After this build the hreflang set across the WHOLE site becomes (15 entries including x-default):
```html
<link rel="alternate" hreflang="en" href="https://winnersclub.com/">
<link rel="alternate" hreflang="ko" href="https://winnersclub.com/ko/">
<link rel="alternate" hreflang="zh-Hans" href="https://winnersclub.com/zh/">
<link rel="alternate" hreflang="vi" href="https://winnersclub.com/vi/">
<link rel="alternate" hreflang="th" href="https://winnersclub.com/th/">
<link rel="alternate" hreflang="ms" href="https://winnersclub.com/ms/">
<link rel="alternate" hreflang="pt" href="https://winnersclub.com/pt/">
<link rel="alternate" hreflang="ja" href="https://winnersclub.com/ja/">
<link rel="alternate" hreflang="es" href="https://winnersclub.com/es/">
<link rel="alternate" hreflang="pt-BR" href="https://winnersclub.com/pt-br/">
<link rel="alternate" hreflang="tr" href="https://winnersclub.com/tr/">
<link rel="alternate" hreflang="id" href="https://winnersclub.com/id/">
<link rel="alternate" hreflang="fr" href="https://winnersclub.com/fr/">
<link rel="alternate" hreflang="ru" href="https://winnersclub.com/ru/">
<link rel="alternate" hreflang="hi" href="https://winnersclub.com/hi/">
<link rel="alternate" hreflang="x-default" href="https://winnersclub.com/">
```

Update all 152 EXISTING pages with the expanded hreflang block, AND emit it on all 133 new pages.

## Sitemap

After build, regenerate `/home/user/workspace/winnersclub.com/sitemap.xml` to include all 19 new pages × 7 locales = 133 new `<url>` entries, in the same XML structure as existing entries (with `<xhtml:link>` hreflang alternates inside each `<url>`).

## Language switcher

Each page contains TWO switchers in the header/nav:
- Desktop: inline list
- Mobile: `<div class="mobile-lang-block"><label>{LangLabel}</label><select>...</select></div>`

The current dropdown has 8 entries (en, ko, zh, vi, th, ms, pt, ja). Update to 15 entries:
```
<option value="">English</option>
<option value="/ko/">한국어 (Korean)</option>
<option value="/zh/">中文 (Chinese)</option>
<option value="/vi/">Tiếng Việt (Vietnamese)</option>
<option value="/th/">ไทย (Thai)</option>
<option value="/ms/">Bahasa Melayu (Malay)</option>
<option value="/pt/">Português (Portuguese)</option>
<option value="/ja/">日本語 (Japanese)</option>
<option value="/es/">Español (Spanish)</option>
<option value="/pt-br/">Português do Brasil (Portuguese - Brazil)</option>
<option value="/tr/">Türkçe (Turkish)</option>
<option value="/id/">Bahasa Indonesia (Indonesian)</option>
<option value="/fr/">Français (French)</option>
<option value="/ru/">Русский (Russian)</option>
<option value="/hi/">हिन्दी (Hindi)</option>
```

The `<label>` text (currently "Language" / "언어" / "言語" etc.) should be in the user's locale:
- es: `Idioma`
- pt-br: `Idioma`
- tr: `Dil`
- id: `Bahasa`
- fr: `Langue`
- ru: `Язык`
- hi: `भाषा`

Update the switcher across ALL 152 existing pages + 133 new pages.

## `lang-redirect.js` update

File: `/home/user/workspace/winnersclub.com/lang-redirect.js`
- Add new locales to `supportedLangs` array: `['en','ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi']`
- Add country→language mappings:
  - es: MX, AR, CO, CL, PE, BO, EC, GT, HN, NI, PA, PY, UY, VE, CR, DO, SV, US-Spanish-fallback (skip US since EN default)
  - pt-br: BR (Brazil only — NOT PT which stays mapped to /pt/ if existed)
  - tr: TR
  - id: ID
  - fr: FR, BE, CH, CA (Quebec is a complication — leave CA → EN), most Francophone Africa (SN, CI, ML, BF, NE, CD, GA, CM, TG, BJ, MG)
  - ru: RU, BY, KZ, KG, AM, AZ, TJ, UZ (CIS region)
  - hi: IN (India — currently routes to EN, but if hi/ exists serve hi to IN users)
- **IMPORTANT**: Check existing country mappings before adding. PT stays mapped to /pt/. BR is new → /pt-br/.

## Translation quality bar

Match the existing /ko/ and /ja/ pages — fluent, idiomatic, casino-aware. Specific notes:

### es (LATAM)
- Use "vos/tú" carefully — default to neutral Latin American Spanish (tú-form OK)
- Currency: keep $ (USD) — same as English
- Wagering = "requisito de apuesta" or "rollover" (rollover is common in LATAM casino lingo)
- Stake = "Stake" (do not translate brand)
- Mirror sites = "espejos" or "sitios espejo" (your GSC shows real demand for "stake espejo")
- Sign up = "registrarse" / "registro" / "regístrate"

### pt-br (Brazilian)
- Brazilian register: use "você", not "tu" (which is Portugal)
- Wagering = "rollover" (universal in BR casino) or "requisito de aposta"
- Currency notation: "$3.000" (period as thousand separator) — match current /pt/ but expect BR convention
- Numbers: "1,5" with comma for decimals in BR
- Sign up = "cadastre-se" / "cadastro" / "registre-se"
- Mirror = "espelho"
- Specifically include Brazil context where natural ("para jogadores brasileiros")

### tr (Turkish)
- Formal "siz" form
- Stake mirror = "Stake ayna" or just keep "mirror"
- Promo code = "Promosyon kodu" or "bonus kodu"
- Sign up = "kayıt ol" / "kayıt"
- Wagering = "çevrim şartı"
- Don't use Turkish-specific gambling slang

### id (Indonesian)
- Bahasa Indonesia standard (not Malay — your /ms/ is Malay, this is different)
- Sign up = "daftar"
- Wagering = "rollover" or "syarat taruhan"
- Promo code = "kode promo"
- Use "Anda" for "you" (formal)

### fr (French)
- International French (works for FR, BE, CH, Quebec, Francophone Africa)
- Sign up = "s'inscrire" / "inscription"
- Wagering = "exigence de mise" or "rollover"
- Promo code = "code promo"
- Use vous-form

### ru (Russian)
- Standard Russian, formal "вы" (you) 
- Sign up = "регистрация" / "зарегистрируйтесь"
- Wagering = "вейджер" or "отыгрыш"
- Promo code = "промокод"
- Brand names stay Latin: "Stake", "MAX3000"

### hi (Hindi)
- Devanagari script
- Use Hindi UX terms but keep brand names in Latin
- Sign up = "साइन अप" / "रजिस्टर करें"
- Wagering = "वेजरिंग" (transliterated) or "बेट टर्नओवर"
- Promo code = "प्रोमो कोड"
- Casino, bonus, sport etc. → use transliterated Hindi forms common in Indian betting affiliate sites

## Deliverable checklist

When done, the workspace must have:
- [ ] 7 new locale directories with 19 pages each (133 new files)
- [ ] All 152 existing pages updated with expanded 15-entry hreflang block
- [ ] All 152 existing pages updated with 15-entry language switcher dropdown
- [ ] `sitemap.xml` regenerated with all locales
- [ ] `lang-redirect.js` updated with new locale routing
- [ ] `_headers` file unchanged (already has security headers)
- [ ] Live verification: `curl https://winnersclub.com/es/` returns HTTP 200 with proper title
- [ ] Push to main, Cloudflare Pages auto-deploys

## Build approach

Recommended approach:
1. Write a Python generator `_build_locales.py` that:
   - Loads the EN page as input (use `/index.html`, `/promo-code/index.html`, etc.)
   - For each new locale, applies the translation dict + locale-specific tweaks
   - Writes to `<locale>/<slug>/index.html`
2. After generating, run a second pass to update hreflang block + language switcher across all 285 pages (152 existing + 133 new)
3. Regenerate sitemap.xml programmatically from filesystem walk
4. Update lang-redirect.js
5. Commit + push + verify

## Quality smoke tests (run before commit)
- `grep -r "—" es/ pt-br/ tr/ id/ fr/ ru/ hi/` → must return ZERO em-dashes
- `grep -r "!" es/index.html pt-br/index.html ...` → check for stray exclamation marks (some may be inside legitimate code/regex — visual check)
- `grep -c "MAX3000" <locale>/index.html` → must be ≥3 per home page
- `grep "winnersclub.com/es/" sitemap.xml | wc -l` → must equal 19
- `python3 -c "from xml.etree import ElementTree; ElementTree.parse('sitemap.xml')"` → must parse cleanly
- `curl -sI https://winnersclub.com/es/ | head -1` after push → HTTP 200

## Output back to parent
Once complete, report:
- Files added (count)
- Files modified (count)
- Commit SHA
- Live verification results (HTTP status of one URL per new locale)
- Any tricky decisions you made (translation choices, structural deviations)
