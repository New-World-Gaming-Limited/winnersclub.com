# ZH Translation Log — winnersclub.com (zh-CN rollout)

**Date:** 2026-05  
**Source:** `/en/` (184 pages)  
**Target:** `/zh/` (Simplified Chinese, zh-CN)  
**Final Audit:** `pages: 184, issues: 0, clean: 184`

---

## Audit Result

```
pages: 184, issues: 0, clean: 184
```

All 184 pages pass the mechanical post-checks:
1. ✓ 0 em dashes (—), 0 en dashes (–) on every page
2. ✓ XLBONUS appears at least once on every page (uppercase)
3. ✓ "Curaçao 8048/JAZ" appears at least once on every page
4. ✓ No banned phrases (数百个/数千个, 世界级, 尖端, 下一代, 最先进)
5. ✓ `<html lang="zh">` on all pages
6. ✓ hreflang block preserved intact on all pages
7. ✓ canonical points to `/zh/...` URLs
8. ✓ JSON-LD validates (json.loads passes) on all pages
9. ✓ GA4 tracker (G-S2MXR8D3HS) preserved
10. ✓ exit-tracker.js preserved

---

## Translation Decisions

1. **"Curaçao 8048/JAZ" normalization:** The LLM occasionally rendered this as "Curaçao 执照 (8048/JAZ)" or "Curaçao 执照 8048/JAZ". Post-processing regex normalizes all variants to the exact required string `Curaçao 8048/JAZ`.

2. **Banned phrase false positives corrected:** The audit initially flagged "数千倍" (thousands-of-times multiplier, a legitimate slot RTP concept) and "乘数百搭符号" (multiplier wild symbol) as banned phrases. The audit rule was refined to only flag "数百/数千" when followed by count units (名, 个, 种, 款, etc.) indicating vague quantities. "数百万" (millions), "数千倍" (multiplier), and "百搭" (wild) are allowed.

3. **Navigation links:** All internal `/en/` hrefs in navigation, footer, and body links are changed to `/zh/`. The hreflang alternate links pointing to all 46 locales (including `hreflang="en" href="..."`) are preserved verbatim.

4. **CTA vocabulary:** "Register" → 立即注册, "Claim" → 领取, "Play Now" → 立即游戏, "Access" → 访问, "Get" → 获取. Game names (Aviator, Sweet Bonanza, JetX, etc.) kept in Latin script per rules.

5. **First paragraph compliance:** Every page opens with a paragraph containing "1win" + "XLBONUS" + a specific number (600%, 11,000+, etc.) + "Curaçao 8048/JAZ". The LLM handled this reliably once the instruction was specified; post-processing verified compliance.

---

## Pages Translated (184 total)

### Root pages (40)
1win-promo-code.html, access.html, alternative-link.html, app.html, aviator.html, casino.html, country-bangladesh.html, country-brazil.html, country-ghana.html, country-india.html, country-kenya.html, country-korea.html, country-malawi.html, country-malaysia.html, country-pakistan.html, country-russia.html, country-singapore.html, country-south-africa.html, country-tanzania.html, country-turkey.html, country-vietnam.html, faq.html, index.html, live-streaming.html, lucky-drive.html, mirrors.html, news-app-update.html, news-aviator-record.html, news-champions-league.html, news-crypto-payments.html, news-lucky-drive.html, news-new-slots.html, news-poker-freeroll.html, news-spring-tournament.html, news-welcome-bonus.html, news.html, payment-methods.html, poker.html, promo-code.html, promotions.html, register.html, review.html, sports-betting.html, vip-club.html, website.html

### bonus/ (8 pages)
cashback-bonus.html, first-deposit-bonus.html, fourth-deposit-bonus.html, free-spins-today.html, index.html, second-deposit-bonus.html, third-deposit-bonus.html, wagering-requirements.html

### crash/ (7 pages)
aviatrix.html, hilo.html, index.html, jetx.html, mines.html, plinko.html, spaceman.html

### india/ (13 pages)
andhra-pradesh.html, delhi.html, gujarat.html, index.html, karnataka.html, kerala.html, maharashtra.html, punjab.html, rajasthan.html, tamil-nadu.html, telangana.html, uttar-pradesh.html, west-bengal.html

### news/ (7 pages)
1win-aviator-bonus-20250909-0001/index.html, 1win-tokens-20251119-0001/index.html, 374k-win-on-gates-of-1win-20251008-0001/index.html, 45x-aviamasters-2-win-at-1win-20260320-0001/index.html, free-poker-20241128-0001/index.html, mancala-gaming-bonuses-at-1win-20251106-0001/index.html, sins-spins-at-1win-20260225-0001/index.html

### payments/ (34 pages)
airtel-money.html, bitcoin.html, boleto.html, easypaisa.html, ecopayz.html, ethereum.html, flutterwave.html, google-pay.html, imps.html, index.html, jazzcash.html, litecoin.html, maestro.html, mastercard.html, mpesa.html, mtn-momo.html, muchbetter.html, neft.html, netbanking.html, neteller.html, orange-money.html, paytm.html, phonepe.html, pix.html, ripple.html, rupay.html, skrill.html, solana.html, tron.html, upi.html, usdt-erc20.html, usdt-trc20.html, visa.html

### promo-code/ (12 pages)
1win-bonus-guide-20240711-0005/index.html, 1win-costa-rica-how-to-register-and-get-your-bonus/index.html, 1win-gambia-how-to-register-and-get-your-bonus/index.html, 1win-indonesia-how-to-register-and-get-your-bonus/index.html, 1win-kazakhstan-how-to-register-and-get-your-bonus/index.html, 1win-korea-how-to-register-and-get-your-bonus/index.html, 1win-malawi-how-to-register-and-get-your-bonus/index.html, 1win-malaysia-how-to-register-and-get-your-bonus/index.html, 1win-south-africa-how-to-register-and-get-your-bonus/index.html, 1win-tajikistan-how-to-register-and-get-your-bonus/index.html, 1win-tanzania-how-to-register-and-get-your-bonus/index.html, 1win-uzbekistan-how-to-register-and-get-your-bonus/index.html

### providers/ (9 pages)
bgaming.html, evolution-gaming.html, hacksaw-gaming.html, index.html, netent.html, playn-go.html, pragmatic-play.html, relax-gaming.html, spribe.html

### reviews/ (1 page)
1win/index.html

### slots/ (21 pages)
big-bass-bonanza.html, book-of-dead.html, buffalo-king-megaways.html, cash-elevator.html, dog-house-megaways.html, dog-house.html, extra-juicy-megaways.html, fire-joker.html, fruit-party.html, gates-of-olympus.html, gonzos-quest.html, index.html, money-train-4.html, razor-shark.html, reactoonz.html, rise-of-olympus-100.html, starburst.html, sugar-rush-1000.html, sweet-bonanza.html, wanted-dead-or-a-wild.html, wolf-gold.html

### sports/ (5 pages)
basketball.html, cricket.html, esports.html, football.html, index.html, tennis.html

### tips/ (11 pages)
basketball-tips.html, cricket-tips.html, esports-tips.html, football-tips.html, index.html, tennis-tips.html, todays-basketball.html, todays-cricket.html, todays-esports.html, todays-football.html, todays-tennis.html

### tools/ (11 pages)
arbitrage-calculator.html, bankroll-calculator.html, each-way-calculator.html, hedge-calculator.html, implied-probability-calculator.html, index.html, kelly-criterion-calculator.html, matched-bet-calculator.html, odds-converter.html, parlay-calculator.html, surebet-calculator.html

---

## Tool Used

- `pplx llm extract` with `sonar` model (default)
- Post-processing: em/en dash removal, Curaçao 8048/JAZ normalization, canonical and internal link `/en/` → `/zh/` rewrite
- Script: `/home/user/workspace/1win-codes-repo/build_helpers/translate_zh_v2.py`
