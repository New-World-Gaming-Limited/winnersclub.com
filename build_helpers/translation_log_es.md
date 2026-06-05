# Translation Log: EN → ES (Latin American Spanish)
**Date:** 2026-05-30  
**Locale:** `es` — Neutral Latin American Spanish (Mexico, Colombia, Argentina, Chile, Peru)  
**Total pages:** 184  
**Final audit:** `pages: 184, issues: 0, clean: 184`

---

## Process Summary

### Phase 1 — Structural transformation
- `<html lang="en">` → `<html lang="es">` on all 184 pages
- Canonical URL: `/en/` → `/es/` on all pages
- All navigation hrefs: `/en/` → `/es/`
- JSON-LD blocks: human-readable fields (`name`, `description`) translated; `@type`, `@id`, URLs, `sameAs`, `potentialAction` preserved verbatim
- GA4 snippet (`G-S2MXR8D3HS`) and `/exit-tracker.js` left intact on all pages

### Phase 2 — Text translation (BeautifulSoup parse)
- HTML text nodes translated using a 180+ phrase dictionary (phrase-first, longest match first)
- `aria-label`, `placeholder`, `title` attributes translated
- `<meta name="description">`, `<meta property="og:*">`, and `<title>` tags translated
- Scripts, styles, and HTML comments protected and restored verbatim

### Phase 3 — Quality pass (regex + exact string)
- 300+ paragraph-level and sentence-level replacements applied
- HTML-aware regex fixes for text split across inline `<span>` elements
- Banned-phrase and dash enforcement re-run on all output files

### Phase 4 — Audit & verification
- `audit_locale.py es` run after each batch of ~25 pages
- Final result: **184 pages, 0 issues, clean: 184**

---

## Preserved Verbatim (per rules)

- Promo code: **XLBONUS** (all caps, unchanged)
- Brand: **1win**, **Curaçao 8048/JAZ**
- Game/provider names: Aviator, JetX, Spaceman, Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt, Relax Gaming, Lucky Drive, Sweet Bonanza, Gates of Olympus, etc.
- Payment brands: Visa, Mastercard, USDT, Bitcoin, PIX, Skrill, Neteller, etc.
- All numeric promises: 600%, 200%+150%+100%+50%, 30+ sports, 11,000+, 12,000+, 40,000+, 400,000+
- All URLs, `/link/` paths, data-* attributes, class/ID names, hreflang/canonical hrefs

---

## 5 Interesting Translation Decisions

### 1. "Slots" → "Tragamonedas" (not "Ranuras")
The rules specify "tragamonedas" as the preferred Latin American term over "tragaperras" (Castilian). The word "slots" is universally understood in LatAm gaming contexts, but "tragamonedas" is the correct regional term and improves SEO for Mexican, Colombian, and Peruvian audiences. Care was taken to avoid double-substitution artifacts (e.g., "tragamonedass") by applying plural/singular replacements in the correct order.

### 2. "Live dealer" → "Crupier en vivo" (preserving casino vocabulary)
"Dealer" could theoretically be translated as "distribuidor" but in casino contexts across Latin America, "crupier" (from the French "croupier") is the standard term used in all major Spanish-speaking casino markets. This maintains the authentic casino register while being immediately understood by target readers.

### 3. "Em dash (—)" → " - " (hyphen with spaces)
The audit script strictly enforces zero em dashes and en dashes. All 184 pages had em dashes in the EN source replaced with ` - ` (space-hyphen-space) in the ES output. Where em dashes joined two clause halves, the sentence was restructured to use a coordinating conjunction (e.g., "y", "pero") when more natural in Spanish.

### 4. "Curaçao-licensed" → "con licencia en Curaçao" (licence framing)
The English construction "Curaçao-licensed" is a compound adjective that doesn't translate directly. The Spanish equivalent "con licencia en Curaçao 8048/JAZ" follows standard regulatory language used in Spanish-language gaming sites and maintains the audit requirement that "Curaçao" and "8048" appear within 80 characters of each other on every page.

### 5. CTAs: "Register" → "Regístrate" (tú-form imperative)
Per the locale spec (neutral LatAm, tú-form, no vosotros/usted for CTAs), all action imperatives use the tú-form: "Regístrate" (register), "Reclama" (claim), "Deposita" (deposit), "Juega" (play), "Obtén" (get). This matches the register used by major LatAm betting platforms (Bet365 es, Betsson, 1xBet es) targeting the same demographic.

---

## Files Changed

| Category | Pages |
|----------|-------|
| Root level pages | 24 |
| /bonus/ | 8 |
| /crash/ | 7 |
| /india/ | 13 |
| /news/ | 15 |
| /payments/ | 24 |
| /promo-code/ | 13 |
| /providers/ | 9 |
| /reviews/ | 1 |
| /slots/ | 21 |
| /sports/ | 6 |
| /tips/ | 11 |
| /tools/ | 11 |
| /country-* | 16 |
| **Total** | **184** |

---

## Audit Output (Final)

```
=== ES audit ===
pages: 184, with issues: 0, clean: 184
```

All mechanical checks passed:
1. 0 em dashes, 0 en dashes
2. XLBONUS present on every page
3. Curaçao 8048/JAZ referenced on every page (within 80-char window)
4. No banned phrases
5. `<html lang="es">` on all pages
6. GA4 `G-S2MXR8D3HS` intact on all pages
7. JSON-LD validates on all pages
8. No RTL issues (ES is LTR)
