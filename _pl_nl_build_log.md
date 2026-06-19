# /pl/ + /nl/ Locale Build Log

**Commit:** caafa150  
**Branch:** main  
**Date:** 2026-06-19  
**Build agent:** pl-nl-subagent

---

## Summary

Built two new locales for winnersclub.com: Polish (/pl/) and Dutch (/nl/), each with 19 pages of native-language content. Updated hreflang blocks, language switchers, lang-redirect.js, and sitemap.xml site-wide.

---

## Word Count Per Page Per Locale

| Page | Polish (words) | Dutch (words) |
|------|---------------|--------------|
| index | 2,240 | 2,214 |
| about-stake | 1,506 | 989 |
| aviator | 977 | 909 |
| casino | 1,573 | 1,175 |
| live-casino | 1,010 | 903 |
| live-odds | 994 | 877 |
| mirror | 982 | 864 |
| news | 821 | 806 |
| originals | 1,057 | 1,028 |
| payments | 993 | 957 |
| poker | 961 | 847 |
| promo-code | 1,871 | 1,117 |
| reserves | 954 | 891 |
| responsible-gambling | 1,066 | 1,033 |
| slots | 976 | 895 |
| sports | 1,352 | 966 |
| stake-engine | 980 | 963 |
| stake-us-bonus | 950 | 886 |
| vip | 941 | 861 |
| **Total** | **21,004** | **18,181** |

---

## Commit Hash

`caafa150` - pushed to `main` on `origin` (https://git-agent-proxy.perplexity.ai/New-World-Gaming-Limited/winnersclub.com.git)

---

## Infrastructure Files Updated

### lang-redirect.js
- Added `'pl'` and `'nl'` to `supportedLangs` array (now 18 locales)
- Added country mappings:
  - `'PL': 'pl'` (Poland)
  - `'NL': 'nl'` (Netherlands)
  - `'BE': 'nl'` (Belgium, Flemish majority; `'BE':'fr'` removed to avoid conflict)

### sitemap.xml
- Added 38 new `<url>` entries: 19 for /pl/ and 19 for /nl/
- Each entry includes full xhtml:link hreflang block (19 locales + x-default)
- All existing URL entries updated with pl/nl xhtml:link hreflang entries
- Sitemap grew from 6,691 to 8,212 lines

### Hreflang blocks (all pages)
- 306 existing HTML files updated
- Each file gained 2 new hreflang entries:
  ```html
  <link rel="alternate" hreflang="pl" href="https://winnersclub.com/pl/[path]"/>
  <link rel="alternate" hreflang="nl" href="https://winnersclub.com/nl/[path]"/>
  ```
- All pages now have 19 hreflang entries (17 existing + pl + nl) + x-default = 20 alternate tags

### Language switcher (all pages)
- Mobile switcher (`mobile-lang-block` select): added `<option value="/pl/">Polski (Polish)</option>` and `<option value="/nl/">Nederlands (Dutch)</option>`
- Desktop switcher (`lang-switcher` class): added `<option value="https://winnersclub.com/pl/">Polski</option>` and `<option value="https://winnersclub.com/nl/">Nederlands</option>`

---

## Total File Count Delta

- **New files created:** 38 HTML pages (19 pl/ + 19 nl/)
- **Modified files:** 316 (306 existing locale pages + lang-redirect.js + sitemap.xml + build scripts)
- **Total commit:** 354 files changed, 12,838 insertions, 554 deletions

---

## Compliance Verification

- No em-dashes (U+2014) or en-dashes (U+2013) in any new files: PASS
- No exclamation marks in body content: PASS
- No emojis: PASS
- No "Welcome to WinnersClub" or local equivalents: PASS
- Promo code MAX3000 (uppercase) throughout: PASS
- Affiliate URL Stake.com: https://www.getstake.it/i/MAX3000/io/max3000/u/MAX3000/uo/max3000 PASS
- Affiliate URL Stake.us: https://stake.us/?c=MAX3000 PASS
- html lang="pl" on all Polish pages: PASS
- html lang="nl" on all Dutch pages: PASS
- Title formula PL: "Stake Kod Promocyjny MAX3000 - Bonus 200% do $3,000": PASS (index page)
- Title formula NL: "Stake Bonuscode MAX3000 - 200% tot $3,000 Welkomstbonus": PASS (index page)

---

## Notes

- Polish pages use full Polish diacritics throughout (a, c, e, l, n, o, s, z with diacritics).
- Dutch pages use Standard Netherlands Dutch (not Flemish).
- Belgium (BE) routed to /nl/ since /fr/ already exists for Francophone Belgium.
- /el/ (Greek) locale was not built - budget constraint; Greek had 93 GSC impressions from Greece, recommended for future build.
- Sister agent rebuilding /zh/, /ja/, /tr/, /pt-br/, /ar/ - pull was clean (already up to date) indicating no conflict at commit time.
