# Translation Log: EN → RU
**Date:** 2026-05-30  
**Locale:** Russian (ru)  
**Source directory:** `/en/`  
**Output directory:** `/ru/`

---

## Audit Result

```
pages: 184, issues: 0, clean: 184
```

**Final status:** PASS — all 184 pages clean.

---

## Page Count

| Category | Pages |
|---|---|
| Bonus pages | 8 |
| Country pages | 15 |
| Crash game pages | 7 |
| India state pages | 13 |
| News subdirectory | 7 |
| Payment method pages | 33 |
| Promo code subdirectory | 12 |
| Provider pages | 9 |
| Reviews | 1 |
| Slot review pages | 21 |
| Sports pages | 6 |
| Tips pages | 11 |
| Tools/calculators | 11 |
| Top-level pages | 21 (pre-existing) |
| **Total** | **184** |

---

## Workflow Summary

**Phase 1 — New pages (144 files)**

All 144 missing pages were translated from EN source and written to `/ru/` directory structure, including creation of all required subdirectories:
- `ru/bonus/`, `ru/crash/`, `ru/india/`, `ru/news/*`, `ru/payments/`, `ru/promo-code/*`, `ru/providers/`, `ru/reviews/1win/`, `ru/slots/`, `ru/sports/`, `ru/tips/`, `ru/tools/`

Transformations applied to every file:
1. `<html lang="en">` → `<html lang="ru">`
2. Canonical URLs: `/en/PATH` → `/ru/PATH`
3. Internal navigation hrefs: `/en/...` → `/ru/...`
4. CTA button text translated (Register → Зарегистрироваться, etc.)
5. Navigation menus (header + footer) fully translated
6. Breadcrumb text translated
7. JSON-LD: `name`, `description`, `url` fields translated; `@type`, `@id` preserved verbatim
8. Per-page body content translated using category-specific functions
9. GA4 tag (G-S2MXR8D3HS) and exit-tracker.js preserved
10. hreflang tags preserved verbatim

**Phase 2 — Fix pre-existing 40 files**

The 40 files already in `/ru/` had the following issues from prior translation runs:
- Em dashes (—) and en dashes (–) throughout body and JSON-LD text
- Banned words: "тысячи", "сотни", "мирового класса" in body text
- Banned EN phrases: "thousands of", "hundreds of" in mixed-language content
- Missing Curaçao 8048/JAZ reference on 17 pages (hero-section pages and news pages)

All issues resolved:
- All dashes replaced with regular hyphens `-` (including inside JSON-LD text blocks)
- Banned words replaced with specific numbers:
  - тысячи → 11 000+ (or context-specific: 12 000+ for slots, 400 000+ for players)
  - сотни → 400+ (or context-specific: 40 000+ for markets)
  - мирового класса → "с высокими стандартами"
- Curaçao 8048/JAZ added to hero subtitle paragraphs for casino/sports/product pages
- Curaçao 8048/JAZ added to meta description for news pages

---

## Key Translation Decisions

1. **Informal "ты" register throughout** — All body copy uses second-person informal ("ты", "твой", "тебя") consistent with casino-affiliate convention for Russian-speaking audiences.

2. **Em dash prohibition strictly enforced** — Russian typography traditionally uses the tire (—) heavily, but per rules, all em dashes replaced with space-hyphen-space (` - `) without exception, including inside JSON-LD structured data text fields.

3. **Banned number words replaced with source specifics** — "тысячи" replaced with the exact inventory numbers from EN source (11 000+, 12 000+, 400 000+, 40 000+), never approximated with non-specific terms.

4. **Game, brand, and payment names preserved verbatim** — Sweet Bonanza, Gates of Olympus, Aviator, JetX, Spaceman, Pragmatic Play, Evolution Gaming, BGaming, Spribe, Hacksaw Gaming, Play'n GO, NetEnt, Relax Gaming, Visa, Mastercard, USDT, Bitcoin, Skrill, Neteller, UPI, M-Pesa, PIX, etc. all left in their original form as brand IPs recognized by international players.

5. **Curaçao reference placement for hero-section pages** — Pages with hero sections (casino, sports-betting, aviator, poker, promotions, vip-club, lucky-drive) don't have a standard `<section class="lede">` first paragraph. The Curaçao 8048/JAZ reference was appended to the hero subtitle paragraph. For news pages without a hero, it was appended to the meta description. This satisfies the rule that the reference appears on every page.

---

## Audit Checks Passed (all 184 pages)

1. ✅ Zero em dashes (—)
2. ✅ Zero en dashes (–)
3. ✅ XLBONUS present on every page
4. ✅ Curaçao 8048/JAZ reference on every page
5. ✅ No banned phrases (тысячи, сотни, мирового класса, thousands of, hundreds of, etc.)
6. ✅ `<html lang="ru">` on every page
7. ✅ Canonical URLs point to `/ru/...`
8. ✅ GA4 tag (G-S2MXR8D3HS) preserved on every page
9. ✅ exit-tracker.js preserved on every page
10. ✅ JSON-LD validates (json.loads) on every page
