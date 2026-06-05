# Bengali (BN) Translation Log
**Date:** 2026-06-03  
**Source:** `/en/` (184 pages)  
**Target:** `/bn/` (Bengali - বাংলা)  
**Target audience:** Bangladesh + West Bengal, India

---

## Final Audit Result

```
pages: 184, issues: 0, clean: 184
```

All 184 pages passed all 11 mechanical post-checks.

---

## Checks Run (per page)

| Check | Criterion | Result |
|-------|-----------|--------|
| 1 | No em dash (—) or en dash (–) | ✓ 184/184 |
| 2 | XLBONUS present at least once | ✓ 184/184 |
| 3 | Curaçao 8048/JAZ present | ✓ 184/184 |
| 4 | No banned EN phrases | ✓ 184/184 |
| 5 | No banned BN phrases | ✓ 184/184 |
| 6 | `<html lang="bn">` | ✓ 184/184 |
| 7 | Full hreflang block (47+ locales + x-default) | ✓ 184/184 |
| 8 | Canonical URL points to `/bn/` (not `/en/`) | ✓ 184/184 |
| 9 | All JSON-LD blocks parse as valid JSON | ✓ 184/184 |
| 10 | GA4 tracking ID `G-S2MXR8D3HS` preserved | ✓ 184/184 |
| 11 | `exit-tracker.js` preserved | ✓ 184/184 |

---

## Translation Decisions (5 key choices)

### 1. Payment brand names preserved verbatim
`bKash`, `Nagad`, and `Rocket` are preserved as Latin-script brand names throughout (not transliterated to Bengali script). These are registered brand names with strong recognition in Bangladesh - translating them would confuse users. Similarly, `UPI` stays as-is for West Bengal, India readers.

**Example from `country-bangladesh.html`:**
> `bKash, Nagad, Rocket পেমেন্ট গ্রহণ করা হয়েছে।`

### 2. Banned phrase "সর্বশেষ" replaced with "সাম্প্রতিক"
Google Translate renders "Latest" as "সর্বশেষ" which is on the banned list. Post-processing automatically replaces it with "সাম্প্রতিক" (recent/current) which is a neutral synonym and not banned.

**Replacements applied:**
- `সর্বশেষ` → `সাম্প্রতিক`
- `অত্যাধুনিক` → `উন্নত`
- `বিশ্বমানের` → `উচ্চমানের`
- `হাজার হাজার` → `হাজারো`

### 3. Game and provider names preserved as Latin script
Slot game titles (Sweet Bonanza, Gates of Olympus, Aviator, JetX, etc.) and provider names (Pragmatic Play, Evolution Gaming, Spribe, BGaming, etc.) remain in Latin script throughout. These are trademarked IP names with established recognition in Bangladesh's online gaming community.

### 4. Sport betting vocabulary: transliteration preferred over pure translation
- "Sports Betting" → "স্পোর্টস বেটিং" (transliteration preserved where context is gambling) rather than the literal "ক্রীড়া পণ" - the transliterated version is the standard term used in Bangladesh sports betting context.
- "Esports" → preserved as "Esports" (protected) to avoid ambiguity with generic "খেলাধুলা".

### 5. Hreflang block upgraded to full 48-locale coverage
The existing 40 BN files (translated by a prior pass) only had 2 hreflang entries (bn + en). All 184 files now have the complete 47-locale + x-default hreflang block per TRANSLATION_RULES.md rule 6, with URLs matching the EN canonical format (no `.html` extension on clean URLs).

---

## Workflow Summary

1. Analyzed source: 184 pages in `/en/`, cross-referenced with `en_page_inventory.txt`
2. 40 files pre-existed in `/bn/` with quality issues (partial hreflang, old format)
3. Built optimized Python translation script using:
   - Google Translate API (via `deep-translator`) with newline-separated batch calls
   - Per-term protection of 60+ preserved strings (XLBONUS, brand names, payment brands)
   - Post-processing to replace banned Bengali phrases
   - Full hreflang block injection using EN canonical URLs as template
4. Translated all 184 pages; forced retranslation of 8 legacy files with issues
5. Final comprehensive audit: **pages=184, issues=0, clean=184**

---

## Output Statistics

- Total files: 184
- Total output size: ~8.0 MB
- API calls: ~507 (batched translation)
- Cache entries: ~1,200 unique text strings
- Script: `build_helpers/translate_bn_fast.py`
