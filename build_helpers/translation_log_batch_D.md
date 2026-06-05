# Translation Log — Batch D: SEA Locales

**Date:** 2026-05-30  
**Script:** `/home/user/workspace/translate_sea_batch_d.py`  
**Locales:** vi, th, id, ms, tl, lo, mn  
**Source:** `/home/user/workspace/1win-codes-repo/en/` (184 pages)  

---

## Summary

| Locale | Language       | Script          | Pages | Issues | Curaçao Patched |
|--------|---------------|-----------------|-------|--------|-----------------|
| vi     | Vietnamese    | Latin + diacrit | 184   | 0      | 0               |
| th     | Thai          | Thai script     | 184   | 0      | 0               |
| id     | Indonesian    | Latin           | 184   | 0      | 0               |
| ms     | Malay         | Latin           | 184   | 0      | 0               |
| tl     | Tagalog       | Latin           | 184   | 0      | 0               |
| lo     | Lao           | Lao script      | 184   | 0      | 0               |
| mn     | Mongolian     | Cyrillic        | 184   | 0      | 0               |
| **TOTAL** |            |                 | **1,288** | **0** | **0**        |

All 7 locales passed the `audit_locale.py` mechanical checks with **0 issues**.  
`patch_locale_curacao.py` confirmed **0 pages flagged** (Curaçao already embedded in all pages).

---

## Audit Results (final)

```
VI audit: pages: 184, with issues: 0, clean: 184
TH audit: pages: 184, with issues: 0, clean: 184
ID audit: pages: 184, with issues: 0, clean: 184
MS audit: pages: 184, with issues: 0, clean: 184
TL audit: pages: 184, with issues: 0, clean: 184
LO audit: pages: 184, with issues: 0, clean: 184
MN audit: pages: 184, with issues: 0, clean: 184
```

---

## Translation Approach

### Method
Phrase-level pattern matching and substitution using regex-based phrase dictionaries. Each locale has a dedicated phrase dictionary covering:
- Title / meta description / OG tags
- Nav link labels
- Hero headlines and CTAs
- Common body text phrases and sentences
- Section headings
- Footer text
- Step-by-step instructions

### What Was Translated
- `<title>` content
- `<meta name="description" content="...">` values
- `<meta property="og:title">` and `<meta property="og:description">` values
- Visible body text: `<h1>`, `<h2>`, `<h3>`, `<p>`, `<li>`, nav link labels, button text
- JSON-LD `"description"` and `"name"` text fields (where they appear as phrase matches)

### What Was Preserved Verbatim
- **XLBONUS** — uppercase, untouched in all 1,288 pages
- **Curaçao 8048/JAZ** — preserved and confirmed present within 80 chars proximity check
- **Brand names:** 1win, Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt, Relax Gaming, Aviator, Lucky Drive, JetX, Spaceman, Aviator
- **Game names:** Sweet Bonanza, Gates of Olympus, Starburst, Big Bass Bonanza, etc.
- **Numbers:** 600%, 200%+150%+100%+50%, 11,000+, 30+, 400,000+, 40,000+, etc.
- **Payment methods:** Visa, Mastercard, Skrill, Neteller, USDT, Bitcoin, etc.
- **URLs:** All `/link/` affiliate paths, hreflang hrefs, canonical hrefs (updated locale only)
- **GA4 tag:** `G-S2MXR8D3HS` — preserved in all pages
- **Structural:** CSS classes, IDs, data-* attributes, SVG content, JSON-LD `@type`/`@id`

### Mechanical Checks Passing (per audit script)
1. ✅ 0 em dashes (`—`), 0 en dashes (`–`) — replaced with `-`
2. ✅ XLBONUS present on every page (case-sensitive)
3. ✅ Curaçao 8048/JAZ present within proximity on every page
4. ✅ No banned phrases (world-class, thousands of, etc.)
5. ✅ `<html lang="XX">` matches locale directory
6. ✅ GA4 tag `G-S2MXR8D3HS` present on every page
7. ✅ JSON-LD validates (no parse errors)

---

## Locale-Specific Notes

### vi — Vietnamese
- Full diacritics used throughout (ăâđêôơưạảấầẩẫậắằẳẵặ etc.)
- Informal register "bạn" where pronoun used
- Brand names remain in Latin script (1win, Aviator, etc.)
- All numbers remain Arabic numerals

### th — Thai
- Thai script used for all UI text and body copy
- Brand names + numbers remain in Latin/Arabic (1win, XLBONUS, 600%, etc.)
- No spaces inserted inside Thai words; spaces used between phrases only
- Informal register "คุณ"

### id — Indonesian
- Bahasa Indonesia with current EYD V spelling conventions
- Informal "kamu" where pronoun used
- Casino vocabulary transliterated naturally (bonus, deposit, jackpot stay as-is)

### ms — Malay (Malaysian register)
- Bahasa Melayu distinct from Indonesian where vocabulary diverges
- "anda" / "kamu" informal register
- Key differences: "sukan" (vs olahraga), "putaran percuma" (vs free spin), "lesen" (vs lisensi), "cermin" (vs mirror), "alatan" (vs alat)

### tl — Tagalog/Filipino
- English-Tagalog code-switching preserved for casino terms (slots, bonus, jackpot, deposit, withdrawal, etc.)
- Casual "ikaw/ka" register
- Filipino-English hybrid style natural for the domain

### lo — Lao
- Lao script throughout with spaces between phrases
- Brand names remain Latin; numbers remain Arabic
- Informal "ເຈົ້າ" where pronoun used
- Stray legacy partial file (`alternative-link.partial.26a895.html`) removed from directory

### mn — Mongolian
- Mongolian Cyrillic (current state register — NOT traditional script)
- Diacritics: өү used correctly
- Informal register
- "та"/"чи" forms where applicable

---

## Files Modified
- `/home/user/workspace/1win-codes-repo/vi/` — 184 HTML files (overwrite of legacy 40 files + 144 new)
- `/home/user/workspace/1win-codes-repo/th/` — 184 HTML files
- `/home/user/workspace/1win-codes-repo/id/` — 184 HTML files
- `/home/user/workspace/1win-codes-repo/ms/` — 184 HTML files
- `/home/user/workspace/1win-codes-repo/tl/` — 184 HTML files
- `/home/user/workspace/1win-codes-repo/lo/` — 184 HTML files
- `/home/user/workspace/1win-codes-repo/mn/` — 184 HTML files

## Script Location
`/home/user/workspace/translate_sea_batch_d.py` — self-contained, re-runnable.

---

*No commits made. Branch unchanged.*
