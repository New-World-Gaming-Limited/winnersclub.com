# winnersclub.com — Site Rules
**Master playbook for content, compliance, design, and market segmentation.**
**Reusable template — applies to winnersclub.com today, Stake.com microsite next, then any future NWG affiliate property.**

**Version:** 1.0
**Last updated:** 2026-05-29
**Owner:** Devendra Damani · New World Gaming Limited
**Source research:** `/research/01-competitor-copy-audit.md`, `/research/02-1win-global-comparison.md`, `/research/03-seo-intent-analysis.md`, `/research/04-compliance-baseline.md`, `/research/05-conversion-frameworks.md`, `/research/06-locale-intent.md`

---

## 0. The 5-line summary

1. **Promote in every market.** No geo-blocks. Standard 18+ / Play Responsibly / Curaçao license footer on every page, that's the floor — no further per-jurisdiction restrictions. (Compliance research is archived in `/research/04-compliance-baseline.md` for reference but is **not** applied as a site rule.)
2. **The single biggest SEO unlock is the country×promo article cluster.** Build them at `/en/promo-code/1win-{country}-how-to-register-and-get-your-bonus-2026/` for the 14 highest-traffic markets, with **local currency** in the title.
3. **One primary CTA per page.** Verb: *Claim*, *Get*, *Unlock*, *Access*, *Download*, *Start*, *Play*. Standardise to `Register with XLBONUS` for sign-up pages and `Claim Your 600% Bonus` for offer pages. Kill the other 5 variants.
4. **Localised URL slugs** in `/pl/`, `/fr/`, `/es/`, `/id/`, `/pt/` — `1win-kasyno`, `inscription-1gagner`, `registro-de-1-victoria`, `pendaftaran-1win`, `cassino-1win`. English slugs in those folders leave traffic on the table.
5. **Specificity over superlatives.** Replace "thousands of games" with "11,000+ slots from 70+ providers". Replace "instant payouts" with "average withdrawal time 4 hours". Replace "the most generous bonus" with "200% + 150% + 100% + 50% across your first four deposits".

---

## 1. Market segmentation — single tier, prioritised

Every market is **promoted**. No geo-blocks, no soft-restricts. Priority ranking drives *where we invest copy effort*, not what we hide from whom. The compliance floor in §5 applies identically on every page in every locale.

### Build priority

| Priority | Market | Folder | Why |
|---|---|---|---|
| P0 | English (global default) | `/en/` | Default fallback for all geos |
| P0 | South Africa | `/en/za/` (new) | 27k users at 1win.global, near-zero on ours — biggest gap |
| P0 | India | `/en/in/` + `/hi/` | Largest single market; IPL + cricket dominates |
| P0 | Russia | `/ru/` | Existing 1win core market; mirror intent is huge |
| P0 | Brazil | `/pt/` (BR Portuguese) | PIX dominance, 6k users at sister site |
| P1 | Indonesia | `/id/` | 8k users sister; badminton + Liga 1 |
| P1 | Korea | `/ko/` | Strong sister-site traffic; needs localised slugs |
| P1 | Polish | `/pl/` | 4k users sister; Polish-slug pages rank well |
| P1 | Turkish | `/tr/` | Established CIS/Turkey audience |
| P2 | German | `/de/` | Smaller but high engagement (411s avg session sister) |
| P2 | French | `/fr/` | LatAm-FR + Maghreb + Belgium/CH |
| P2 | Spanish | `/es/` | LatAm focus — Mexico, Argentina, Peru |
| P2 | Vietnamese | `/vi/` | SEA football + casino |
| P2 | Japanese | `/ja/` | Aviator + casino interest |
| P2 | Arabic | `/ar/` | MENA — football + casino |
| P3 | All other locales (47 folders total) | various | Maintain; refresh annually |

---

## 2. Microsite strategy — when to spin out a new domain

We will build **microsites**, not just subfolders, when the market signal justifies it. This is the same playbook we'll use when we build the Stake.com microsite next.

### Decision criteria — build a microsite when **3 of 5** are true:

1. The market has **its own currency** with strong localisation expectation (PIX in Brazil, UPI in India, ZAR in SA, RUB in Russia).
2. **The locale has a distinct local voice** — cricket-mad India vs Brasileirão-mad Brazil vs Springboks-mad SA — enough that mixing them on the main domain dilutes the on-page narrative.
3. The market has **its own dominant sport** the main domain cannot deeply serve (PSL + Springboks in SA, IPL + Kabaddi in IN, Brasileirão in BR).
4. **Search demand justifies a standalone domain** — 10k+ monthly impressions for the brand+geo cluster.
5. The market has a **payment-method moat** (PIX-first, UPI-first, M-Pesa-first) that warrants its own deposit-method content tree.

### Microsite roadmap

| Domain | Market | Reason | Priority |
|---|---|---|---|
| `winnersclub.com/en/za/` first, then `1win.co.za` later | South Africa | All 5 criteria met. SA is biggest current gap. | P0 |
| `winnersclub.com/pt/` first, then `1win.com.br` later | Brazil | All 5 met. Newly regulated; PIX. | P1 |
| `winnersclub.com/en/in/` + `/hi/` first, then `1win.co.in` later | India | All 5 criteria met. Cricket is unique. | P0 |
| `winnersclub.com/ru/` only — no separate microsite | Russia | Already entrenched at sister site; subfolder is fine | P0 (content only) |
| `winnersclub.com/id/` only | Indonesia | Demand strong; keep on main domain for now | P1 |
| **`winnersclub.com`** — new microsite | Stake.com affiliate | **User-requested next step.** Same template. | Q3 2026 |

### The reusable template (what we encode here so Stake microsite is fast)

Every NWG affiliate microsite — winnersclub.com today, winnersclub.com tomorrow — uses **the same content architecture, the same compliance scaffolding, the same design system**, and only swaps the operator-specific variables.

Template variables (these are the only things that change per brand):

```yaml
operator:
  brand_name: "1win"  # or "Stake"
  domain: "winnersclub.com"  # or "winnersclub.com"
  promo_code: "XLBONUS"  # or "CODESTAKE"
  bonus_pct: 600  # or 200% match
  bonus_structure: "200% + 150% + 100% + 50% across 4 deposits"  # or "deposit-match up to X"
  license: "Curaçao 8048/JAZ"  # or whatever Stake's is
  game_count: 11000
  sport_count: 30
  provider_count: 70
  avg_withdrawal_hours: 4
  crypto_supported: ["BTC", "ETH", "USDT", "LTC", "DOGE", "TRX"]
  fiat_supported_per_country: {...}
```

Everything else — page architecture, voice, compliance footer, CTA verbs, FAQ schema, hreflang block, country×promo template — is shared.

---

## 3. Content architecture — the 14 page types

Every NWG affiliate microsite ships with this exact set of 14 page archetypes. Same URLs, same H1 patterns (with `{BRAND}` swapped), same FAQ schema.

| Archetype | URL | Primary intent | Framework | FK grade target |
|---|---|---|---|---|
| Homepage | `/en/` | Discovery + CTA | AIDA | 7–8 |
| Promo Code | `/en/promo-code/` | Bonus claim | 4Ps | 7–8 |
| Aviator (or crash) | `/en/aviator/` | Game play | Story Hook | 8–9 |
| Casino | `/en/casino/` | Game discovery | AIDA | 7–8 |
| Sports Betting | `/en/sports-betting/` | Bet placement | AIDA | 7–8 |
| App | `/en/app/` | Download | BAB | 6–7 |
| Payment Methods | `/en/payment-methods/` | Trust + how-to | PAS | 8–9 |
| VIP Club | `/en/vip-club/` | Status aspiration | BAB | 7–8 |
| Lucky Drive (sweepstake) | `/en/lucky-drive/` | Sweepstake entry | Story Hook | 6–7 |
| Review | `/en/review/` | E-E-A-T research | QUEST | 9–10 |
| Mirror | `/en/mirror/` (singular) | Crisis access | PAS | 6–7 |
| Register | `/en/register/` | Sign-up steps | Slippery Slope | 6–7 |
| Country × Promo | `/en/promo-code/1win-{country}-2026/` | Localised bonus | 4Ps | 7–8 |
| FAQ | `/en/faq/` | Trust + objection handling | QUEST | 8–9 |

**Slug rules:**
- Singular slugs for high-search-volume hub pages (`/mirror/` not `/mirrors/`).
- Localised slugs in non-English folders (see §6).
- Country×promo URL always ends in `-2026/` (year-stamped; rolls forward annually).

---

## 4. Voice and copy rules

### 4.1 The non-negotiables

1. **Never use em dashes (—) or en dashes (–) in body copy.** Use commas, periods, or parentheses. This is the same rule applied to Annabel Cavendish voice and most NWG editorial properties. Hyphens (`-`) are fine for compound words.
2. **Never use the words `scrape`, `scraping`, `crawl`, `crawling`** in user-facing copy.
3. **No exclamation points.** Confidence reads as confidence without one.
4. **No emojis in body copy.** Trust-row icons are fine (🛡 ⚡ 📱) but only as labelled badges.
5. **Always specific.** Numbers, named providers, named leagues, named payment rails. Never "thousands", "many", "fast" — always "11,000+", "Pragmatic Play and Evolution", "PIX in under 60 seconds".
6. **One promise per heading.** H2s carry one concept, not three.
7. **Active voice, present tense.** "1win pays out in 4 hours" not "Withdrawals are processed within 4 hours by 1win".
8. **First person on CTAs where possible.** Per Unbounce/Aagaard test, "Claim **My** 600% Bonus" lifts vs "Claim **Your** 600% Bonus" by 10–90%. Use sparingly; one per page max.

### 4.2 Banned phrases (sitewide)

These appear in the current English copy and **must be removed**:

- "FEEL THE THRILL", "LIVE THE ACTION", "DRIVE YOUR DREAM", "LIVE LAVISH", "RIDE THE WAVE", "TAKE FLIGHT" — content-free hype H2s.
- "Try Your Luck", "Hit the Tables" — unspecific CTAs.
- "the most generous welcome bonus in online betting" — unverifiable superlative.
- "thousands of betting markets", "thousands of games" — replace with exact numbers.
- "instant payouts", "lightning fast" — replace with "average 4-hour withdrawal".
- "no strings attached" — bonus has wagering requirements; this is technically untrue.
- "risk-free", "guaranteed", "sure bet", "easy money" — sitewide ban. These are factually untrue and they crater trust with skeptical readers.

### 4.3 Banned phrases — sitewide only

No per-market compliance overlay. The §4.2 list applies globally.

### 4.4 Standardised CTA verbs (sitewide)

Pick from this short list. Standardise so every page reads consistently:

**Primary (offer-related):**
- `Claim My 600% Bonus`
- `Register with XLBONUS`
- `Unlock 600% with XLBONUS`

**Primary (product-related):**
- `Play Aviator Now`
- `Open My 1win Account`
- `Download the 1win App`
- `Access Current Mirror`

**Secondary (text link, not button):**
- `Login to 1win →`
- `See full bonus terms →`
- `Compare payment methods →`

**Banned CTA verbs:**
- ~~Try Your Luck~~, ~~Hit the Tables~~, ~~Take Flight~~, ~~Submit~~, ~~Click Here~~, ~~Continue~~, ~~Proceed~~, ~~Sign Up~~ (Tier 4 generic).

**Rule:** Maximum one primary CTA per above-the-fold zone. Maximum two distinct CTA verbs per page.

### 4.5 Headline case rules

- **H1:** Sentence case with proper nouns: `1win Promo Code XLBONUS — Get a 600% Welcome Bonus`
- **H2:** Sentence case: `How the 600% bonus works`
- **H3:** Sentence case: `Step 1: Click the registration link`
- **CTA buttons:** Title Case (not ALL CAPS): `Claim My 600% Bonus`
- **Trust badges:** Two-word labels: `Curaçao Licensed`, `4-Hour Payouts`, `iOS & Android`

The current code uses ALL CAPS H1s and ALL CAPS CTAs. **Switch to sentence case for H1 and Title Case for CTAs.** ALL CAPS reads as shouting and hurts ESL readers.

### 4.6 The first paragraph rule

The **first paragraph on every page** must contain:
1. The brand name (`1win`)
2. The promo code (`XLBONUS`) **if** the page is offer-related
3. **One specific number** (game count, sport count, bonus %, payout speed)
4. **One trust signal** (license, year founded, country count)

**Bad (current):** "1win India is built for the world's largest cricket market. With comprehensive coverage of the Indian Premier League..."

**Good:** "1win covers all 74 IPL 2026 matches with live in-play markets, cash-out on every selection, and free streams for the playoffs. Curaçao-licensed (8048/JAZ), 30+ sports total, 4-hour withdrawals via UPI."

### 4.7 The chrome-leak rule

The current first paragraph on every page is literally the nav menu text concatenated with the H1 ("Promo Code Sports Betting Casino Poker More Aviator..."). **This is a template structural bug.** The build script must skip nav text when extracting the first paragraph, or — better — wrap nav in `<nav>` and have the renderer ignore it for first-paragraph extraction. **Fix this in the build pipeline, not in copy.**

---

## 5. Compliance scaffold — universal floor only

One block, every page, every locale. No per-market overlay.

### 5.1 Hero compliance bar (above the fold, every landing page)

```html
<div class="hero-compliance-bar">
  <span class="hero-age-badge">18+</span>
  <span class="hero-rg-text">
    Gambling can be addictive. Play responsibly.
    <a href="https://www.gamblingtherapy.org" rel="nofollow noopener" target="_blank">Get Help</a>
  </span>
  <span class="hero-license">Licensed: Curaçao 8048/JAZ</span>
</div>
```

### 5.2 Footer compliance block

```html
<footer class="compliance-footer">
  <div class="compliance-age-bar">
    <span class="age-icon">18+</span>
    <span class="play-responsibly">Play Responsibly</span>
  </div>
  <p>
    <strong>Gambling involves financial risk and may be addictive.</strong>
    Only persons aged 18 or over are permitted to gamble. If you or someone you know has a
    gambling problem, help is available at
    <a href="https://www.gamblingtherapy.org" rel="nofollow noopener" target="_blank">Gambling Therapy</a>.
  </p>
  <p>
    <strong>Affiliate Disclosure:</strong> winnersclub.com is an independent affiliate review website.
    We may receive a commission when you click links to operators featured on this site.
    This does not affect our editorial independence.
  </p>
  <p>
    <strong>Operator Licence:</strong> Games and betting services featured on this site are operated by 1win,
    licensed under Curaçao Gaming Authority Licence No. 8048/JAZ.
  </p>
</footer>
```

Ship verbatim on every page. No territory notice, no geo-block list, no per-jurisdiction overlay.

---

## 6. URL slug strategy

Per the 1win.global audit, **localised slugs outperform English slugs by 10–20×** in non-English folders. Adopt these slugs as canonical, with English slugs becoming 301 redirects.

| Folder | English slug | Adopt this slug | Notes |
|---|---|---|---|
| `/pl/` | `/casino/` | `/1win-kasyno/` | 3,545 users at sister site |
| `/pl/` | `/register/` | `/1win-rejestracja/` | |
| `/pl/` | `/promo-code/` | `/kod-promocyjny-1win/` | |
| `/fr/` | `/register/` | `/inscription-1gagner/` | 2,113 users sister |
| `/fr/` | `/promo-code/` | `/code-promotionnel-1win/` | |
| `/es/` | `/register/` | `/registro-de-1-victoria/` | 1,028 users sister |
| `/es/` | `/casino/` | `/casino-de-1-victoria/` | 819 users sister |
| `/es/` | `/sports-betting/` | `/casa-de-apuestas-1win/` | 1,290 users sister |
| `/id/` | `/register/` | `/pendaftaran-1win/` | 367 users sister |
| `/id/` | `/casino/` | `/kasino-1win/` | |
| `/id/` | `/promo-code/` | `/kode-promo-1win/` | |
| `/pt/` | `/register/` | `/cadastro-1win/` | BR Portuguese |
| `/pt/` | `/casino/` | `/cassino-1win/` | |
| `/pt/` | `/promo-code/` | `/codigo-promocional-1win/` | |
| `/pt/` | `/sports-betting/` | `/apostas-esportivas-1win/` | |
| `/ar/` | (keep English slugs) | (no change) | 1,135 users sister; English slugs rank fine |
| `/ru/` | `/register/` | `/registratsiya-1win/` | Cyrillic transliterated; native works too |
| `/ru/` | `/mirror/` | `/zerkalo-1win/` | Huge for RU |
| `/tr/` | `/register/` | `/1win-uyelik/` | |

**Implementation:** add canonical URL with localised slug; keep English slug as 301 redirect for backward compatibility.

---

## 7. SEO patterns

### 7.1 Title formula by page type

| Page | Formula | Example |
|---|---|---|
| Homepage | `{Brand} Promo Code {CODE} — {Bonus%} Welcome Bonus 2026` | `1win Promo Code XLBONUS — 600% Welcome Bonus 2026` |
| Promo Code | `{Brand} Promo Code {CODE} — Get {Bonus%} Up To {LocalAmount}` | `1win Promo Code XLBONUS — Get 600% Up To 145,000 INR` (per locale page) |
| Country × Promo | `{Brand} {Country} — How to Register and Get Your Bonus (2026)` | `1win South Africa — How to Register and Get Your 600% Bonus (2026)` |
| Aviator | `{Brand} Aviator — Crash Game with {Crypto} Cash-Out | Code {CODE}` | `1win Aviator — Crash Game with USDT Cash-Out | Code XLBONUS` |
| Casino | `{Brand} Casino — {GameCount}+ Slots & Live Tables | {Bonus%} Bonus` | `1win Casino — 11,000+ Slots & Live Tables | 600% Bonus` |
| Sports Betting | `{Brand} Sportsbook — {SportCount}+ Sports, Cash-Out, Live Streams` | `1win Sportsbook — 30+ Sports, Cash-Out, Live Streams` |
| App | `{Brand} App Download — iOS & Android APK | {Bonus%} Bonus 2026` | `1win App Download — iOS & Android APK | 600% Bonus 2026` |
| Payment Methods | `{Brand} Deposits & Withdrawals — Crypto, Cards, UPI, PIX` | `1win Deposits & Withdrawals — Crypto, Cards, UPI, PIX` |
| VIP Club | `{Brand} VIP — 5 Tiers, Cashback, Personal Manager` | `1win VIP — 5 Tiers, Cashback, Personal Manager` |
| Review | `{Brand} Review {Year} — Expert {Bonus%} Rating, Pros & Cons` | `1win Review 2026 — Expert Sportsbook Rating, Pros & Cons` |
| Mirror | `{Brand} Mirror — Working Alternative Link {Month} {Year}` | `1win Mirror — Working Alternative Link May 2026` |
| Register | `{Brand} Register — Open an Account in 30 Seconds | Code {CODE}` | `1win Register — Open an Account in 30 Seconds | Code XLBONUS` |
| FAQ | `{Brand} FAQ — Bonus, Withdrawals, Mirror, Account Help` | `1win FAQ — Bonus, Withdrawals, Mirror, Account Help` |

**Title length:** target 55–60 characters before the pipe so Google rarely truncates.

### 7.2 Meta description formula

`{Action verb} {benefit with number}. {Trust signal}. {Code or CTA}. {License}.`

**Example (Promo Code page):** `Activate 1win promo code XLBONUS in 2026 for a 600% bonus across your first four deposits (max 145,000 INR / 5,600 BRL). Curaçao-licensed. T&Cs apply, 18+.`

**Length:** 145–160 characters.

### 7.3 Schema markup (every page where applicable)

| Schema | Pages | Notes |
|---|---|---|
| `FAQPage` | Homepage, Promo Code, Aviator, Casino, Sports, App, Payments, Mirror, Register, Country×Promo, FAQ | 6 questions min |
| `HowTo` | Register, Promo Code activation, App install, Mirror access | Numbered steps |
| `Review` + `AggregateRating` | Review page | Honest scores: 4.2–4.6 range |
| `Offer` | Promo Code, Country×Promo | Price=0, validFrom, validThrough |
| `WebSite` + `SearchAction` | Homepage | Sitelinks searchbox |
| `BreadcrumbList` | All pages except homepage | |
| `SportsEvent` | Future — live event hubs | |

Use the FAQ schema template in `/research/02-1win-global-comparison.md` §3.

### 7.4 hreflang

Already shipped this PR. 48 hreflang tags per page. Keep.

### 7.5 Internal linking

Every page must link to:
- Homepage (via logo)
- The corresponding country page (if relevant)
- Promo Code page (from any non-promo page)
- Mirror page (from Register, Login, Sports, Casino)
- 3+ related pages in the same cluster (e.g. Aviator links to Crash Game guide, Best Crash Strategy, Other Spribe games)

Anchor text rule: never `click here`, never `learn more`. Always descriptive: `1win mirror link for May 2026`, `step-by-step UPI deposit guide`, `XLBONUS bonus terms`.

---

## 8. Design rules (cross-reference design system)

The full design system lives in the existing CSS files. These are the additional rules that govern copy placement:

- **Above-the-fold elements** (desktop 1200px viewport): H1, hero subtitle, single primary CTA, hero compliance bar, trust badge row. Nothing else.
- **No carousels** in hero. Carousels kill conversion. Static hero only.
- **Single primary CTA button**: minimum 48px tap target on mobile, contrast ratio ≥ 4.5:1.
- **Sticky bottom bar** for scroll depth ≥ 60% on offer pages: `Promo Code XLBONUS — 600% Bonus Active · [Register Now →]`
- **Trust badges**: 4 items max, icon + label, single line on desktop, two lines mobile.
- **FAQ accordion**: closed by default on mobile, all open on desktop (Schema requires fully crawlable HTML).
- **Pricing/bonus tables**: always include local currency column for the user's geo (Cloudflare Worker injects).

---

## 9. Country×promo article template (the highest-impact pattern)

Per the 1win.global audit, this single template earns ~7,000 organic users/90d at our sister site. We have zero. **Build 14 of these in priority order.**

### Build order (ranked by traffic at 1win.global — all markets in play)

1. South Africa (27k users sister, 2 on ours)
2. India (largest single-market traffic potential; cricket vertical)
3. Malawi (8.5k sister)
4. Korea (build with localised slugs and Korean-language slot variants)
5. Indonesia (8k sister)
6. Malaysia (7.4k sister)
7. Brazil (6.4k sister) — Portuguese, not English
8. Tanzania (3.9k sister)
9. Costa Rica
10. Gambia
11. Tajikistan
12. Uzbekistan
13. Kazakhstan
14. Armenia
15. Poland

### Article template (production-ready)

URL: `/en/promo-code/1win-{country}-2026/`

```
TITLE: 1win {Country} — How to Register and Get Your 600% Bonus (2026)
META:  Activate 1win promo code XLBONUS in {Country}. Get a 600% welcome bonus up to {LocalAmount}, deposit via {LocalPaymentMethods}, bet on {LocalSport}. Curaçao licensed. 18+, T&Cs apply.

H1:    1win {Country}: How to Register and Get Your 600% Bonus (2026)

[HERO COMPLIANCE BAR + SPEC TABLE]
| Operator | 1win |
| License  | Curaçao 8048/JAZ |
| Bonus    | 600% up to {LocalAmount} |
| Code     | XLBONUS |
| Currency | {LocalCurrency} |
| Payments | {top 3 local methods} |
| Top sport| {Local top sport} |

H2: 1win in {Country} — quick facts
H2: How to register at 1win {Country} in 4 steps
   H3: Step 1 — Open the 1win {Country} registration page
   H3: Step 2 — Enter your details and apply code XLBONUS
   H3: Step 3 — Make your first deposit via {LocalMethod}
   H3: Step 4 — Claim your 600% bonus on the first four deposits

H2: Your 1win {Country} bonus breakdown
   [Table: 4 deposit tiers, bonus % each, local currency cap]

H2: Local payment methods for {Country}
   [3–5 methods, processing times, min/max, fees]

H2: Top sports to bet on in {Country}
   [3–5 local sports/leagues with markets available]

H2: Aviator and crash games for {Country} players

H2: 1win {Country} app — iOS and Android download

H2: FAQ — 1win in {Country}
   [6 questions, FAQPage schema]

H2: Responsible gambling in {Country}
   [Local helpline, 18+, age verification info]

[FOOTER COMPLIANCE BLOCK + 3-4 INTERNAL LINKS]
```

Word count target: 1,400–1,800. Reading grade: 7–8.

---

## 10. Build & deploy rules

### 10.1 Branch & PR

- Never push to `master` directly.
- Branch naming: `seo/{topic}-{YYYY-MM-DD}`, `copy/{page}-{YYYY-MM-DD}`, `compliance/{topic}-{YYYY-MM-DD}`.
- Open a PR for every change ≥ 5 files.
- PR description must include: scope, files touched, screenshot of preview, validation summary.

### 10.2 Validation suite (must pass before merge)

```bash
python3 validate-fixes.py
```

Validates:
- hreflang block correct on every HTML file
- 0 leaky H2s (English text in non-English files)
- 0 missing image dimensions
- 0 CLS-risk inline styles
- Footer compliance block present
- Hero compliance bar present on landing pages

### 10.3 Cloudflare Pages preview

Every push to a non-master branch builds a preview. Pattern:
`https://{branch-name-truncated}.1win-codes.pages.dev`

Hand-test 4 pages before merging:
- Homepage `/en/`
- One country page `/en/za/` (or another Tier 1)
- One offer page `/en/promo-code/`
- One critical-utility page `/en/mirror/`

### 10.4 Post-merge

- Re-submit sitemap to GSC.
- Trigger Cloudflare cache purge.
- Verify Cloudflare Worker (geo router) is active.
- Spot-check 5 random URLs return correct geo behaviour.

---

## 11. Reusable for Stake.com microsite (next project)

When we build the Stake microsite, swap these and ship:

```yaml
operator:
  brand_name: "Stake"
  domain: "winnersclub.com"  # or wherever we land it
  promo_code: "CODE_TBD"  # to confirm with affiliate manager
  bonus_structure: "TBD"  # Stake's offer differs from 1win
  license: "Curaçao OGL/2024/1451/0918"  # to verify
  game_count: 4000  # Stake has fewer games than 1win
  provider_count: 50
  unique_selling_points:
    - "Stake Originals (Plinko, Crash, Mines, Limbo)"
    - "Crypto-first (BTC, ETH, USDT, SOL, DOGE, LTC, XRP, TRX, BCH, USDC)"
    - "Stake.com Sponsorships (UFC, F1, Drake)"
```

Then **all 14 page archetypes, all compliance scaffolding, all CTA verbs, all FAQ schemas, all build tooling, all geo-routing logic — ship verbatim**.

Stake-specific copy notes (researched separately, summarised here):
- Stake voice is more crypto-native and Gen Z than 1win — keep "Stake Originals" front-and-centre.
- Drake/UFC/F1 sponsorship moments are massive trust signals; reference them in hero.
- Compliance posture: Stake operates on multiple licenses; pick the most relevant per market.
- Stake.com is **not** available in US, UK, AU, FR, DE, NL, ES, IT, PT — same Tier 3 list applies.

---

## 12. Open questions / decisions to confirm

| Question | Default if no answer | Owner |
|---|---|---|
| Build IN microsite (`1win.co.in`) or stay on `/en/in/` + `/hi/`? | Subfolder for now, microsite at Phase 2 | Devendra |
| Localise slugs in `/pl/`, `/fr/`, `/es/`, `/id/`, `/pt/` now or after copy rewrite? | After copy rewrite (next PR) | Devendra |
| Build SA microsite (`1win.co.za`) or stay on `/en/za/`? | Subfolder for now, microsite at Phase 2 | Devendra |
| Stake.com microsite — start scoping now? | Park until winnersclub.com copy is shipped | Devendra |

---

**End of site rules.**

This document is the source of truth. Update it when reality changes. PRs that violate these rules must explicitly call out the deviation and the reason in the PR description.
