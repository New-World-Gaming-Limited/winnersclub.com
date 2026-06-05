# Hindi (HI) Translation Log
**Date:** 2026-05-29  
**Locale:** `hi` (Hindi - Devanagari)  
**Source:** `/en/` (184 pages per `en_page_inventory.txt`)  
**Output:** `/hi/` (184 pages)  
**Script:** `scripts/translate_hi_v3.py`

---

## Final Audit Result

```
pages: 184, issues: 0, clean: 184
```

All 184 pages pass every mechanical rule check.

---

## Pages by Category

| Category | Count |
|----------|-------|
| root (top-level) | 45 |
| payments/ | 33 |
| slots/ | 21 |
| india/ | 13 |
| promo-code/ | 12 |
| tips/ | 11 |
| tools/ | 11 |
| providers/ | 9 |
| bonus/ | 8 |
| news/ | 7 |
| crash/ | 7 |
| sports/ | 6 |
| reviews/ | 1 |
| **Total** | **184** |

---

## Rule Compliance Checks (all pages)

| Rule | Status |
|------|--------|
| `<html lang="hi">` | ✓ All 184 pages |
| XLBONUS present | ✓ All 184 pages |
| Curaçao 8048/JAZ present | ✓ All 184 pages |
| Zero em dashes (—) | ✓ All 184 pages |
| Zero en dashes (–) | ✓ All 184 pages |
| canonical → `/hi/` | ✓ All 184 pages |
| Full hreflang block (48 entries: 47 locales + x-default) | ✓ All 184 pages |
| 1win brand name preserved (no "1जीत" corruption) | ✓ All 184 pages |
| XLBONUS uppercase preserved | ✓ All 184 pages |
| Banned Hindi words absent | ✓ All 184 pages |
| JSON-LD validates (json.loads) | ✓ All 184 pages |
| GA4 (G-S2MXR8D3HS) intact | ✓ All 184 pages |
| exit-tracker.js intact | ✓ All 184 pages |
| Nav URLs updated to /hi/ | ✓ All 184 pages |
| JSON-LD URLs updated to /hi/ | ✓ All 184 pages |

---

## Pre-existing Issues Fixed

The 40 previously existing `hi/` files had multiple violations:
- **Em dashes:** 8-29 em dashes per file (—)
- **Missing Curaçao:** 38 of 40 files missing "Curaçao 8048/JAZ"
- **Incomplete hreflang:** Only 2 hreflang entries (need 47)
- **Banned words:** "नवीनतम" in 3 files
- All 40 files were retranslated fresh from EN source.

---

## Translation Decisions

### 1. "1win" Brand Name Protection
The word "win" is a common English word. The translator applies **phrase-first** replacement (longest match first), meaning "1win" is processed as a whole token in multi-word phrases before any word-level replacement. Single-word replacements use `\b` regex word boundaries, which do not match "1win" since "1" is a non-word character acting as a prefix guard.

**Result:** "1win" preserved in all 184 pages. Zero "1जीत" corruptions.

### 2. Hindi Register for Casino Vocabulary
Per TRANSLATION_RULES.md §South Asian / hi:
- Casino terms use transliterated English with Hindi UX words: "ऑनलाइन कैसीनो", "स्पोर्ट्स बेटिंग", "बोनस", "प्रोमो कोड"
- CTAs use natural Hindi imperatives: "साइन अप करें", "रजिस्टर करें", "प्राप्त करें", "खेलें"
- Brand names stay Latin: 1win, Aviator, Sweet Bonanza, Lucky Drive
- Payment brands stay native uppercase: UPI, Paytm, PhonePe, GPay, USDT, Visa

### 3. India State Pages (12 pages)
The 12 India state pages (Maharashtra, Tamil Nadu, Karnataka, Delhi, UP, West Bengal, Gujarat, Rajasthan, Punjab, Kerala, AP, Telangana) receive special treatment:
- State name translated to Devanagari throughout: महाराष्ट्र, तमिलनाडु, कर्नाटक, दिल्ली, उत्तर प्रदेश, पश्चिम बंगाल, गुजरात, राजस्थान, पंजाब, केरल, आंध्र प्रदेश, तेलंगाना
- UPI, Paytm, PhonePe, IMPS, NEFT payment rail names preserved verbatim (uppercase)
- Local sport context preserved: IPL, Pro Kabaddi League, ISL references kept
- Curaçao 8048/JAZ appears 5-9 times per state page

### 4. Canonical Fix for Redirect Pages
9 news/article/review pages had EN canonicals pointing to a different URL (consolidation redirect pattern). These were updated to point to the `/hi/` equivalent of the EN canonical target:
- `news/1win-aviator-bonus-*` → `https://winnersclub.com/hi/news-aviator-record`
- `news/1win-tokens-*` → `https://winnersclub.com/hi/news-app-update`
- `news/374k-win-*` → `https://winnersclub.com/hi/news-aviator-record`
- `news/45x-aviamasters-*` → `https://winnersclub.com/hi/news-aviator-record`
- `news/free-poker-*` → `https://winnersclub.com/hi/news-poker-freeroll`
- `news/mancala-gaming-*` → `https://winnersclub.com/hi/news-new-slots`
- `news/sins-spins-*` → `https://winnersclub.com/hi/news-new-slots`
- `promo-code/1win-bonus-guide-*` → `https://winnersclub.com/hi/promo-code`
- `reviews/1win/` → `https://winnersclub.com/hi/review`

### 5. Hreflang Block Rebuild
All 184 pages had their hreflang block rebuilt from scratch with all 47 entries (46 locales + x-default). The EN source files had varying numbers of hreflang entries (some only 2). The HI output always has the complete set.

---

## Translation Quality Notes

- **Total Devanagari characters generated:** 165,589 across 184 files
- **Hreflang entries per page:** 48 (47 locales + x-default)
- **Partial translation artifacts fixed:** "बेटting" in 2 tool pages (matched-bet-calculator.html, tools/index.html) fixed post-processing to "बेटिंग"
- **No banned English phrases** present in any HI file (no em/en dashes, no "thousands of", no "world-class")

---

## Script

Translation performed by `scripts/translate_hi_v3.py` using:
1. **Structural fixes:** lang, canonical, hreflang, nav URLs, JSON-LD URLs
2. **Phrase-first dictionary:** 150+ multi-word EN→HI mappings (longest first)
3. **Word-boundary replacements:** Single UI terms with `\b` boundary protection
4. **Post-processing:** Banned word removal, Curaçao/XLBONUS presence guarantee

Run command:
```bash
cd /home/user/workspace/1win-codes-repo && python3 scripts/translate_hi_v3.py
```
