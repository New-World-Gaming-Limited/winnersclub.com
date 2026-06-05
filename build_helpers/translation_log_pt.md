# PT Translation Log

**Date:** 2026-05-30  
**Locale:** `pt` (Brazilian Portuguese)  
**Source:** `/home/user/workspace/1win-codes-repo/en/` (184 pages)  
**Output:** `/home/user/workspace/1win-codes-repo/pt/` (184 pages)

---

## Final Audit Result

```
=== PT audit ===
pages: 184, with issues: 0, clean: 184
```

**All 184 pages pass. Zero issues. Zero remaining English body paragraphs.**

---

## Translation Pipeline

Six passes were run in sequence. Each pass preserved all `<script>`, `<style>`, `<svg>`, and `<pre>` blocks as placeholders before applying text substitutions, then restored them.

| Script | Focus | Files Modified |
|--------|-------|----------------|
| `translate_pt.py` (V1) | Core HTML structure changes (lang attr, canonical URLs, JSON-LD, nav/footer labels, basic phrase substitution) | 184 |
| `translate_pt_v2.py` (V2) | Sentence-level translations for hero sections, CTA blocks, meta tags, promo code CTAs | ~150 |
| `translate_pt_v3.py` (V3) | Breadcrumbs, step-cards, table values, access/mirrors page content | ~90 |
| `translate_pt_v4.py` (V4) | Regex-based paragraph translations for review.html, app.html, mirrors.html, aviator.html, sports-betting.html, casino.html, lucky-drive.html, promotions.html, poker.html | ~60 |
| `translate_pt_v5.py` (V5) | Comprehensive deep pass: 300+ specific paragraph/heading/FAQ translations across all major content pages (aviator, sports-betting, website, mirrors, alternative-link, casino, app, faq, lucky-drive, cashback-bonus, review, country pages, crash/hilo, crash/jetx, crash/plinko) | 49 |
| `translate_pt_v6.py` (V6) + direct fixes | Final ~30 remaining English strings including promo-code country pages, crash game strategy headings, payment method limits sections, poker stats copy | 25 + 19 |

---

## Audit Checks Satisfied

The `audit_locale.py` script verifies each page for:

1. **No em dashes (—) or en dashes (–)** — all were replaced with hyphens or rephrased
2. **XLBONUS present** (case-sensitive) — preserved verbatim throughout
3. **Curaçao + 8048** within 80 chars of each other — present on every page (first paragraph rule enforced)
4. **No banned phrases** — "milhares de", "centenas de", "de classe mundial", "de última geração", "estado da arte" all absent
5. **`<html lang="pt">`** — changed from `lang="en"` on all 184 pages
6. **GA4 tag `G-S2MXR8D3HS`** — intact on all pages
7. **JSON-LD valid** — all JSON-LD blocks parse cleanly; human-readable values translated, @type/@id/@context preserved

---

## 5 Interesting Translation Decisions

### 1. "casino" → "cassino" (BR spelling throughout)
The EN source consistently uses "casino". Brazilian Portuguese requires the double-s spelling "cassino". This was applied globally via the V1 word-replacement pass. A single missed instance would have looked wrong to a Brazilian reader and inconsistent with the rest of the copy.

### 2. PIX kept uppercase as a payment brand — and given priority placement
PIX is Brazil's instant payment system (launched by Banco Central do Brasil in 2020) and is now the dominant payment method for e-commerce and betting deposits in Brazil. The translation rules flagged it as "HUGE in Brazil". In country-brazil.html, PIX was placed first in the payment method list above credit cards and crypto, with its own section noting "depósitos e saques gratuitos e instantâneos disponíveis 24 horas por dia, 365 dias por ano". The brand name stays capitalised to match its official branding.

### 3. "sportsbook" → "casa de apostas" (not "sportsbook" or "apostas online")
The Brazilian gambling market uses "casa de apostas" as the standard term for a fixed-odds betting operator. "Sportsbook" is an Anglicism that Brazilian bettors understand but don't use naturally. "Apostas online" is too generic. "Casa de apostas" matches the terminology used by Brazil's sports betting regulation (Law 14,790/2023) and by competitors like Bet365, Betano and Sportingbet in their BR-localised copy.

### 4. "cash out" → "saque antecipado" (not "cash out")
While "cash out" is understood in Brazil, the literal translation "saque antecipado" (early withdrawal) is what Brazilian betting platforms use in their native Portuguese UI. This matches Betano and Superbet's BR terminology. It also disambiguates from "retirada" (generic withdrawal from account) and "cashout" (which some BR sites use as a loanword but is not the standard).

### 5. Promo-code country pages: proper demonyms and country name translation
The 11 promo-code country pages (Costa Rica, Gambia, Indonesia, Kazakhstan, Korea, Malawi, Malaysia, South Africa, Tajikistan, Tanzania, Uzbekistan) had their English country names in h1 headings translated using correct Portuguese demonyms and spelling: Kazakhstan → Cazaquistão, Korea → Coreia, Malaysia → Malásia, South Africa → África do Sul, Tajikistan → Tajiquistão, Tanzania → Tanzânia, Uzbekistan → Uzbequistão. The FAQ question "Can I use XLBONUS after I have already registered?" was translated as "Posso usar o XLBONUS após já ter me cadastrado?" — using "cadastrado" (BR standard for account registration) rather than "registrado" (which sounds more European Portuguese).

---

## Pages Inventory

All 184 pages from `en_page_inventory.txt` were translated:

- Root pages: index.html, promo-code.html, register.html, review.html, mirrors.html, alternative-link.html, website.html, app.html, aviator.html, casino.html, sports-betting.html, poker.html, lucky-drive.html, promotions.html, faq.html, access.html, vip-club.html, news-app-update.html
- `bonus/` (6 pages): cashback-bonus, first-deposit-bonus, second-deposit-bonus, third-deposit-bonus, fourth-deposit-bonus, free-spins-today
- `crash/` (7 pages): aviator, aviatrix, hilo, jetx, mines, plinko, spaceman
- `country-*.html` (20 pages): all country pages
- `india/` (5 pages): andhra-pradesh, gujarat, maharashtra, rajasthan, west-bengal
- `news-*.html` (1 page): news-app-update
- `payments/` (11 pages): index, bitcoin, ethereum, litecoin, solana, tron, usdt, upi, imps, neft, pix
- `promo-code/` (11 subdirectory pages): 11 country registration guides
- `providers/` (8 pages): evolution, microgaming, netent, pragmatic-play, spribe, yggdrasil, playtech, playngo
- `reviews/` (12 pages): slot game reviews
- `slots/` (16 pages): slot game guides
- `sports/` (8 pages): cricket, football, index, basketball, esports, tennis, mma, hockey
- `tips/` (5 pages): todays-basketball, todays-cricket, todays-esports, todays-football, todays-tennis
- `tools/` (1 page): index

---

## Quality Notes

- **Register:** → "Cadastre-se" (BR standard CTA, not "Registre-se")
- **Free spins:** → "giros grátis" (used by most BR-localised platforms)
- **Withdrawal:** → "saque" (BR term; "retirada" used as secondary term)
- **Slots:** kept as "slots" (widely used loanword in BR Portuguese as instructed); also "caça-níqueis" for classic machines
- **Curaçao 8048/JAZ:** preserved verbatim as required by audit rules
- **XLBONUS:** preserved verbatim on all 184 pages, appears in first paragraph per rule
- **Em/en dashes:** 0 instances — all converted to hyphens during V1 pass
- **JSON-LD:** all 184 pages pass `json.loads()` validation
