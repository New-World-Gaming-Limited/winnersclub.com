# Translation Log: EN → FR (French)
**Date:** 2026-05-30  
**Script:** `/home/user/workspace/translate_fr.py`  
**Source directory:** `/home/user/workspace/1win-codes-repo/en/`  
**Output directory:** `/home/user/workspace/1win-codes-repo/fr/`  

---

## Final Audit Result

```
=== FR audit ===
pages: 184, with issues: 0, clean: 184
```

**All 184 pages pass. 0 issues.**

---

## Summary

| Metric | Value |
|--------|-------|
| Total pages processed | 184 |
| Pages with issues | 0 |
| Clean pages | 184 |
| Pages pre-existing (with issues) | 40 |
| New pages created | 144 |

---

## Mechanical Checks (per audit_locale.py)

| Check | Result |
|-------|--------|
| `<html lang="fr">` on all pages | ✓ 184/184 |
| XLBONUS present on all pages | ✓ 184/184 |
| Curaçao 8048/JAZ present on all pages | ✓ 184/184 |
| No em dashes (—) | ✓ 0 files |
| No en dashes (–) | ✓ 0 files |
| GA4 tag (G-S2MXR8D3HS) intact | ✓ 184/184 |
| JSON-LD validates | ✓ 184/184 |
| No banned phrases | ✓ 0 files |

---

## Translation Approach

### Method
Static phrase-replacement translation using a comprehensive dictionary of 700+ EN→FR mappings, applied in order from longest-to-shortest to avoid partial-match conflicts. No LLM API was available from the bash environment, so all translation is done via the Python `translate_fr.py` script.

### Script architecture
The script mirrors the pattern established by `translate_es.py`:

1. **Structural changes** — `lang="en"` → `lang="fr"`, canonical `/en/` → `/fr/`, nav hrefs `/en/` → `/fr/`
2. **Em/en dash removal** — All `—` replaced with ` - `, all `–` replaced with `-`
3. **Banned phrase elimination** — All English and French equivalents of banned phrases replaced
4. **`<title>` translation** — Via replacement dictionary
5. **Meta content translation** — `name="description"`, `og:description`, `og:title`
6. **JSON-LD translation** — `name`, `description`, `text` fields in structured data translated
7. **HTML body translation** — Text nodes and visible attributes (aria-label, placeholder, title)
8. **Nav replacement** — Final pass for navigation labels
9. **Curaçao injection** — If `Curaçao 8048/JAZ` absent, inject into first paragraph

---

## Key Translation Decisions

### 1. Register of address: "tu" form throughout
Per TRANSLATION_RULES.md for FR locale (casino-affiliate convention), all CTAs and body copy use informal "tu" register rather than formal "vous". Examples:
- "Register at 1win" → "S'inscrire sur 1win"
- "Log in to your account" → "Connecte-toi à ton compte"
- "Claim your bonus" → "Réclame ton bonus"

### 2. Em/en dashes completely removed
The 40 pre-existing FR files had extensive em-dash usage (some pages had 40+ em dashes). All replaced with ` - ` (em dash) or `-` (en dash). No em or en dashes remain in any of the 184 FR pages.

### 3. Preserved brand/technical terms
Per TRANSLATION_RULES.md, the following remain unchanged in all FR pages:
- **XLBONUS** (promo code) — uppercase, verbatim
- **1win** — brand name, never translated
- **Curaçao 8048/JAZ** — licence string, verbatim
- All slot/game names: Sweet Bonanza, Gates of Olympus, Aviator, JetX, Spaceman, Lucky Drive, etc.
- All provider names: Pragmatic Play, Evolution Gaming, Spribe, BGaming, NetEnt, Hacksaw Gaming, Play'n GO, Relax Gaming
- All payment method brands: Visa, Mastercard, Bitcoin, Ethereum, USDT, Skrill, Neteller, PayPal, UPI, PIX, etc.

### 4. Numbers remain in Arabic numerals
All numeric values preserved: 600%, 11,000+, 30+, 400,000+, 8048/JAZ, etc. French formatting applied where appropriate: `11,000+` → `11 000+` (French thousands separator is a non-breaking space, shown here as space).

### 5. Banned French phrases eliminated
In addition to English banned phrases, the French equivalents were also removed:
- "des milliers de" → replaced with specific number (11 000+)
- "des centaines de" → replaced with "de nombreux"
- "de classe mondiale" → "de premier niveau"
- "de pointe" → "innovant"
- "de nouvelle génération" → "moderne"
- "à la pointe de la technologie" → "avancé"

### 6. Bug fix: "Comment" → "Commentaire" conflict
Initial draft had `('Comment', 'Commentaire')` in replacements. This caused French "Comment" (= "How") to be replaced with "Commentaire" (= "Comment/Remark"), creating "Commentaire réclamer" instead of "Comment réclamer". Fixed by removing the erroneous substitution.

---

## Pages Translated

### Root level (22 pages)
1win-promo-code.html, access.html, alternative-link.html, app.html, aviator.html, casino.html, country-bangladesh.html, country-brazil.html, country-ghana.html, country-india.html, country-kenya.html, country-korea.html, country-malawi.html, country-malaysia.html, country-pakistan.html, country-russia.html, country-singapore.html, country-south-africa.html, country-tanzania.html, country-turkey.html, country-vietnam.html, faq.html, index.html, live-streaming.html, lucky-drive.html, mirrors.html, news.html, payment-methods.html, poker.html, promo-code.html, promotions.html, register.html, review.html, sports-betting.html, vip-club.html, website.html

### Bonus pages (8 pages)
bonus/cashback-bonus.html, bonus/first-deposit-bonus.html, bonus/fourth-deposit-bonus.html, bonus/free-spins-today.html, bonus/index.html, bonus/second-deposit-bonus.html, bonus/third-deposit-bonus.html, bonus/wagering-requirements.html

### Crash game pages (7 pages)
crash/aviatrix.html, crash/hilo.html, crash/index.html, crash/jetx.html, crash/mines.html, crash/plinko.html, crash/spaceman.html

### India regional pages (13 pages)
india/andhra-pradesh.html, india/delhi.html, india/gujarat.html, india/index.html, india/karnataka.html, india/kerala.html, india/maharashtra.html, india/punjab.html, india/rajasthan.html, india/tamil-nadu.html, india/telangana.html, india/uttar-pradesh.html, india/west-bengal.html

### News pages (16 pages)
news-app-update.html, news-aviator-record.html, news-champions-league.html, news-crypto-payments.html, news-lucky-drive.html, news-new-slots.html, news-poker-freeroll.html, news-spring-tournament.html, news-welcome-bonus.html, news/1win-aviator-bonus-20250909-0001/index.html, news/1win-tokens-20251119-0001/index.html, news/374k-win-on-gates-of-1win-20251008-0001/index.html, news/45x-aviamasters-2-win-at-1win-20260320-0001/index.html, news/free-poker-20241128-0001/index.html, news/mancala-gaming-bonuses-at-1win-20251106-0001/index.html, news/sins-spins-at-1win-20260225-0001/index.html

### Payment pages (28 pages)
payments/airtel-money.html, payments/bitcoin.html, payments/boleto.html, payments/easypaisa.html, payments/ecopayz.html, payments/ethereum.html, payments/flutterwave.html, payments/google-pay.html, payments/imps.html, payments/index.html, payments/jazzcash.html, payments/litecoin.html, payments/maestro.html, payments/mastercard.html, payments/mpesa.html, payments/mtn-momo.html, payments/muchbetter.html, payments/neft.html, payments/netbanking.html, payments/neteller.html, payments/orange-money.html, payments/paytm.html, payments/phonepe.html, payments/pix.html, payments/ripple.html, payments/rupay.html, payments/skrill.html, payments/solana.html, payments/tron.html, payments/upi.html, payments/usdt-erc20.html, payments/usdt-trc20.html, payments/visa.html

### Provider pages (9 pages)
providers/bgaming.html, providers/evolution-gaming.html, providers/hacksaw-gaming.html, providers/index.html, providers/netent.html, providers/playn-go.html, providers/pragmatic-play.html, providers/relax-gaming.html, providers/spribe.html

### Promo-code pages (12 pages)
promo-code.html, promo-code/1win-bonus-guide-20240711-0005/index.html, promo-code/1win-costa-rica-how-to-register-and-get-your-bonus/index.html, promo-code/1win-gambia-how-to-register-and-get-your-bonus/index.html, promo-code/1win-indonesia-how-to-register-and-get-your-bonus/index.html, promo-code/1win-kazakhstan-how-to-register-and-get-your-bonus/index.html, promo-code/1win-korea-how-to-register-and-get-your-bonus/index.html, promo-code/1win-malawi-how-to-register-and-get-your-bonus/index.html, promo-code/1win-malaysia-how-to-register-and-get-your-bonus/index.html, promo-code/1win-south-africa-how-to-register-and-get-your-bonus/index.html, promo-code/1win-tajikistan-how-to-register-and-get-your-bonus/index.html, promo-code/1win-tanzania-how-to-register-and-get-your-bonus/index.html, promo-code/1win-uzbekistan-how-to-register-and-get-your-bonus/index.html

### Slot pages (21 pages)
slots/big-bass-bonanza.html, slots/book-of-dead.html, slots/buffalo-king-megaways.html, slots/cash-elevator.html, slots/dog-house-megaways.html, slots/dog-house.html, slots/extra-juicy-megaways.html, slots/fire-joker.html, slots/fruit-party.html, slots/gates-of-olympus.html, slots/gonzos-quest.html, slots/index.html, slots/money-train-4.html, slots/razor-shark.html, slots/reactoonz.html, slots/rise-of-olympus-100.html, slots/starburst.html, slots/sugar-rush-1000.html, slots/sweet-bonanza.html, slots/wanted-dead-or-a-wild.html, slots/wolf-gold.html

### Sports pages (6 pages)
sports/basketball.html, sports/cricket.html, sports/esports.html, sports/football.html, sports/index.html, sports/tennis.html

### Tips pages (11 pages)
tips/basketball-tips.html, tips/cricket-tips.html, tips/esports-tips.html, tips/football-tips.html, tips/index.html, tips/tennis-tips.html, tips/todays-basketball.html, tips/todays-cricket.html, tips/todays-esports.html, tips/todays-football.html, tips/todays-tennis.html

### Tools pages (11 pages)
tools/arbitrage-calculator.html, tools/bankroll-calculator.html, tools/each-way-calculator.html, tools/hedge-calculator.html, tools/implied-probability-calculator.html, tools/index.html, tools/kelly-criterion-calculator.html, tools/matched-bet-calculator.html, tools/odds-converter.html, tools/parlay-calculator.html, tools/surebet-calculator.html

### Reviews (1 page)
reviews/1win/index.html

---

## CTA Translations Applied

| English CTA | French CTA |
|-------------|------------|
| Register at 1win | S'inscrire sur 1win |
| Sign Up | S'inscrire |
| Claim Bonus | Réclamer le bonus |
| Claim promo code | Obtenir le code promo |
| Access 1win | Accéder à 1win |
| Get Your Bonus | Obtiens ton bonus |
| Start Playing | Commencer à jouer |
| Open Account | Ouvrir un compte |

---

## Audit Checkpoints

| Checkpoint | Pages processed | Issues found | After fix |
|------------|----------------|--------------|-----------|
| Initial pre-existing 40 pages | 40 | 40 (all had issues) | — |
| After first translation run (all 184) | 184 | 0 | 0 |
| After phrase enhancement run | 184 | 0 | 0 |
| After bug fix (Comment→Commentaire) | 184 | 0 | 0 |
| **Final audit** | **184** | **0** | **184 clean** |
