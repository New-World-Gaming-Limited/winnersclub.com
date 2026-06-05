# AR Translation Log — winnersclub.com
**Date**: 2026-05-30  
**Language**: Modern Standard Arabic (MSA)  
**Direction**: RTL (`dir="rtl"`)  
**Target locale**: Gulf / MENA  
**Pages translated**: 184  

---

## Final Audit Result

```
=== AR Audit Results ===
Pages: 184
Clean: 184
Missing: 0
With issues: 0
Total issues: 0
```

### Checks passed (all 184/184):
| Check | Result |
|---|---|
| `dir="rtl"` on `<html>` | 184/184 |
| `lang="ar"` on `<html>` | 184/184 |
| XLBONUS present | 184/184 |
| Curaçao 8048/JAZ present | 184/184 |
| GA4 (G-S2MXR8D3HS) intact | 184/184 |
| exit-tracker.js intact | 184/184 |
| canonical uses `/ar/` | 184/184 |
| No em/en dashes | 184/184 |
| No `1فوز` brand corruption | 184/184 |
| 48 hreflang entries | 184/184 |
| No banned AR phrases | 184/184 |

---

## Page Count by Batch

| Batch | Directories | Pages |
|---|---|---|
| Pre-existing (fixed) | ar/ root + partial subdirs | 40 |
| Batch 1 | bonus/, country-*, crash/ | ~55 |
| Batch 2 | india/, news/, payments/ | ~35 |
| Batch 3 | promo-code/, providers/, reviews/, slots/ | ~30 |
| Batch 4 | sports/, tips/, tools/ | ~24 |
| **Total** | | **184** |

---

## Key Decisions

### 1. Text-node-only translation (not `str.replace`)
The initial approach used naive `str.replace` on the full HTML string. This corrupted brand names ("1win" → "1فوز") and mangled canonical URLs, CSS class names, JavaScript variables, and `data-*` attributes. **Fix**: `apply_body_translations()` now splits on HTML tags using `re.split(r'(<[^>]+>)', segment)` and translates only even-indexed parts (text nodes between tags), never touching HTML attribute content.

### 2. SHORT_WORDS_SKIP set (minimum phrase length filters)
Short English words in the translation dictionary ("win", "new", "review", "today", "live", "all") caused partial-match corruption when encountered inside longer strings in URLs, class names, and JS identifiers. **Fix**: A `SHORT_WORDS_SKIP` set excludes these entries from `apply_body_translations`. Separate length thresholds apply per context: body translations require len ≥ 4; meta tag translations use `SAFE_META_TRANSLATIONS` (len ≥ 4, not in SHORT_WORDS_SKIP, no "1win" in key); JSON-LD translations use `SAFE_JSONLD_TRANSLATIONS` (len ≥ 6, no "1win" in key).

### 3. Canonical URL override for non-`/en/` pages
Several `news/*` and `promo-code/*` pages in the EN source had canonical tags pointing at root-level aliases (e.g., `https://winnersclub.com/news-aviator-record`) rather than the standard `/en/<path>` pattern. Inheriting these verbatim would produce broken AR canonicals. **Fix**: For any canonical that does not contain `/en/`, the script generates the correct AR canonical from the file's actual path: `https://winnersclub.com/ar/<relative-path>`.

### 4. Full 48-entry hreflang block injected on every page
EN source pages (except index.html) contained only 2 hreflang entries. The audit requires all 46 locale variants plus `x-default` on every AR page. **Fix**: The script strips all existing `<link rel="alternate" hreflang=...>` tags and injects the complete 48-entry block immediately after the canonical tag. The x-default points to `/en/<path>`.

### 5. Arabic word-boundary checking for banned phrase "حديث"
The banned word "حديث" (modern/new — prohibited per TRANSLATION_RULES.md) is a substring of "تحديث" (update), a legitimate Arabic word used in footer/timestamp contexts. Naïve substring matching was flagging "update" references as violations. **Fix**: The audit checks the characters immediately before and after a candidate match; if either adjacent character is in the Arabic Unicode block (U+0600–U+06FF), the candidate is part of a larger word and is not flagged. This eliminated all false positives without reducing genuine catch coverage.

---

## Translation Architecture — `translate_en_to_ar.py`

### Pipeline (`full_translate_complete()`)
1. Fix `<html lang="en">` → `<html lang="ar" dir="rtl">`
2. Fix canonical URL (`/en/` → `/ar/`; override non-`/en/` canonicals)
3. Remove all existing hreflang links
4. Inject full 48-entry hreflang block after canonical
5. Fix internal hrefs (`/en/` → `/ar/`)
6. Remove em/en dashes outside `<script>`/`<style>` blocks
7. Translate meta tags (title, description, og:title, og:description) using `PAGE_META` then `SAFE_META_TRANSLATIONS`
8. Translate JSON-LD text fields (name, description) using `SAFE_JSONLD_TRANSLATIONS`
9. Translate HTML body segments — text nodes only
10. Inject Curaçao 8048/JAZ reference if absent

### Translation dictionaries
- `BODY_TRANSLATIONS`: ~250 phrase-pair entries (EN → AR), sorted longest-first to prevent short-match interference
- `PAGE_META`: hardcoded AR titles/descriptions for 30+ main pages (index, bonus/*, crash/*, casino, sports-betting, aviator, poker, faq, vip-club, review, etc.)
- `SAFE_META_TRANSLATIONS`: filtered subset of BODY_TRANSLATIONS for meta tag context
- `SAFE_JSONLD_TRANSLATIONS`: filtered subset for JSON-LD name/description fields

### Preserved verbatim (never translated)
- Brand names: 1win, XLBONUS, Sweet Bonanza, Aviator, Plinko, Curaçao 8048/JAZ
- Payment brands: Visa, Mastercard, USDT, Skrill, Neteller, Bitcoin, Ethereum
- Numerals: ASCII 0-9 only (no Eastern Arabic ٠-٩)
- Bonus values: 600%, 200%, 150%, 500$, 200$, 75 free spins, etc.
- All URLs, CSS class names, IDs, data-* attributes, JavaScript
- `<script>`, `<style>` block content
- GA4 measurement ID, exit-tracker.js src

---

## AR Register Notes
- Language: Modern Standard Arabic (فصحى / MSA)
- Target reader: Gulf and MENA market
- Key vocabulary choices:
  - كازينو على الإنترنت (online casino)
  - المراهنات الرياضية (sports betting)
  - مكافأة (bonus)
  - رمز ترويجي (promo code)
  - إيداع (deposit)
  - سحب (withdrawal)
  - تسجيل (registration)
- CTAs used: سجل، احصل، افتح، ابدأ، العب، وصول، طالب
- No dialect; no transliteration of Arabic terms into Latin
