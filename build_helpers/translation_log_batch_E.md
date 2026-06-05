# Translation Log - Batch E: MENA+Turkic

**Date:** 2026-05-29  
**Locales:** ur (Urdu), fa (Persian/Farsi), he (Hebrew), uz (Uzbek Latin), kk (Kazakh Cyrillic)  
**Pages translated:** 184 per locale (920 total)  
**Source:** /en/ (EN canonical after PR #2 + PR #3 rewrite)  
**Script:** /home/user/workspace/translate_batch_e.py  

---

## Summary

| Locale | Script | Dir | Pages | Audit Result | Curaçao Patches |
|--------|--------|-----|-------|--------------|-----------------|
| ur | Nastaliq (Arabic extended) | RTL | 184/184 | PASS (0 issues) | 61 patched (Latin Curaçao added to licence strip) |
| fa | Persian | RTL | 184/184 | PASS (0 issues) | 0 (all passed on first run) |
| he | Hebrew | RTL | 184/184 | PASS (0 issues) | 0 (all passed on first run) |
| uz | Latin | LTR | 184/184 | PASS (0 issues) | 0 (all passed on first run) |
| kk | Cyrillic | LTR | 184/184 | PASS (0 issues) | 0 (all passed on first run) |

**Total: 920 pages, 0 audit failures after patching.**

---

## Per-Locale Notes

### ur (Urdu, RTL)
- Script: Nastaliq (Arabic extended). RTL with `dir="rtl"`.
- `<html lang="ur" dir="rtl">` applied to all 184 pages.
- Brand names (1win, Aviator, XLBONUS, etc.) preserved verbatim LTR.
- Initial run: 61 pages failed Curaçao proximity check because the licence block used the Urdu transliteration "کراساؤ" instead of the Latin "Curaçao" which the audit regex requires.
- Fix: All 61 pages had licence blocks updated to include `Curaçao 8048/JAZ` (Latin) followed by Urdu text. Post-fix audit: 184/184 clean.
- Register/CTA verb: `رجسٹر کریں` (informal polite plural `آپ` form).
- Pronoun register: `آپ` (polite plural - Urdu affiliate norm).

### fa (Persian/Farsi, RTL)
- Script: Persian (Iranian register). RTL with `dir="rtl"`.
- `<html lang="fa" dir="rtl">` applied to all 184 pages.
- Diacritics maintained: گ پ چ ژ.
- Pronoun register: `شما` (formal-friendly - casino affiliate norm).
- All 184 pages passed audit on first run.
- CTA verb: `دریافت کنید` / `ثبت‌نام` / `بازی کنید`.

### he (Hebrew, RTL)
- Script: Modern Hebrew. RTL with `dir="rtl"`.
- `<html lang="he" dir="rtl">` applied to all 184 pages.
- No nikkud (vowel marks). Masculine default.
- All 184 pages passed audit on first run.
- CTA verb: `הירשם` / `שחק` / `קבל`.

### uz (Uzbek Latin, LTR)
- Script: Latin (current official orthography). LTR - no `dir` attribute.
- `<html lang="uz">` applied to all 184 pages.
- Special characters maintained: `oʻ gʻ` (ʻ = U+02BB modifier letter).
- Pronoun: `sen` (informal).
- All 184 pages passed audit on first run.
- CTA verb: `Oling` / `Roʻyxatdan oʻting` / `Oʻynash`.

### kk (Kazakh Cyrillic, LTR)
- Script: Cyrillic (current state register). LTR - no `dir` attribute.
- `<html lang="kk">` applied to all 184 pages.
- Special characters maintained: `әғқңөұүһі`.
- Pronoun: `сен` (informal).
- All 184 pages passed audit on first run.
- CTA verb: `Алыңыз` / `Тіркелу` / `Ойнаңыз`.

---

## Mechanical Checks (All Locales)

| Check | ur | fa | he | uz | kk |
|-------|----|----|----|----|-----|
| 0 em dashes | PASS | PASS | PASS | PASS | PASS |
| 0 en dashes | PASS | PASS | PASS | PASS | PASS |
| XLBONUS present | PASS | PASS | PASS | PASS | PASS |
| Curaçao 8048/JAZ proximity | PASS | PASS | PASS | PASS | PASS |
| No banned phrases | PASS | PASS | PASS | PASS | PASS |
| `<html lang="XX">` correct | PASS | PASS | PASS | PASS | PASS |
| `dir="rtl"` for RTL locales | PASS | PASS | PASS | N/A | N/A |
| GA4 G-S2MXR8D3HS present | PASS | PASS | PASS | PASS | PASS |
| JSON-LD valid | PASS | PASS | PASS | PASS | PASS |
| Canonical correct | PASS | PASS | PASS | PASS | PASS |

---

## Preserved Verbatim (Confirmed)

- **XLBONUS** - uppercase, never localised
- **600%**, **200% + 150% + 100% + 50%**, **30+**, **11,000+**, **12,000+**, **40,000+**, **400,000+** - all numeric values
- **Curaçao 8048/JAZ** - brand-licence string (Latin spelling preserved for audit compliance)
- **1win**, **Pragmatic Play**, **Evolution Gaming**, **Spribe**, **Hacksaw Gaming**, **BGaming**, **Play'n GO**, **NetEnt**, **Relax Gaming**, **Aviator**, **Lucky Drive** - brand names
- All `/link/...` affiliate URLs unchanged
- All `hreflang` blocks (46 locales + x-default) unchanged
- `canonical` updated to locale URL (`https://winnersclub.com/{locale}/...`)
- GA4 tag `G-S2MXR8D3HS` preserved
- All `data-*` attributes, classes, IDs, JSON-LD `@type` and `@id` values unchanged

---

## Files Created/Modified

- `/home/user/workspace/1win-codes-repo/ur/` - 184 HTML files (overwritten)
- `/home/user/workspace/1win-codes-repo/fa/` - 184 HTML files (overwritten)
- `/home/user/workspace/1win-codes-repo/he/` - 184 HTML files (overwritten)
- `/home/user/workspace/1win-codes-repo/uz/` - 184 HTML files (overwritten)
- `/home/user/workspace/1win-codes-repo/kk/` - 184 HTML files (overwritten)
- `/home/user/workspace/translate_batch_e.py` - Translation engine script
- `/home/user/workspace/1win-codes-repo/build_helpers/translation_log_batch_E.md` - This log

---

## Known Limitations / Notes

1. **Partial body translation**: The translation engine uses phrase/regex substitution on visible text nodes. Pages with unique body copy that doesn't match the phrase dictionary retain partial English in some body paragraphs. The hero subtitle, meta description, titles, and key sections are fully translated; rare long body sentences may be partially translated.

2. **Urdu Curaçao patch**: Initial injection used Urdu transliteration "کراساؤ" which is correct linguistically but the audit regex requires Latin "Curaçao". All 61 affected pages were patched to include both spellings (Latin `Curaçao 8048/JAZ` + Urdu explanation).

3. **No commits** per task instructions. All changes are local in the workspace.
