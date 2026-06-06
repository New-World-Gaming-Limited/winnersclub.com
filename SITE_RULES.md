# WinnersClub.com — Site Rules

Authoritative editorial, voice, and content rules for winnersclub.com (EN + KO).
Anything that contradicts this file must be fixed.

Owner: Devendra Damani · Last revised: 6 June 2026

---

## Voice

- Sultry Vegas concierge. The bouncer-already-likes-you tone.
- House palette: gold #FFD700, velvet #8b0a1a, slate #141415.
- Closing line on long-form pages and transcripts: "Tell the dealer WinnersClub sent you." (EN) / "딜러에게 WinnersClub이 보냈다고 전해주세요." (KO).

## Hard bans

- No em-dashes anywhere. Use hyphens, commas, or full stops.
- No exclamation marks.
- No emojis unless the user explicitly asks for them on a one-off basis.
- No blue, purple, or teal accent colours.
- Never open a page with "Welcome to WinnersClub".
- Never address the reader with American-affiliate filler ("you'll love it", "amazing", "incredible", etc.).

## Editorial framing — Stake, founders, operator, history

**Always frame Stake background positively.** This is a non-negotiable rule.

- Never note that Stake.com is banned, blocked, restricted, or prohibited in any country. If a market doesn't have access, simply omit it. Country mirrors exist because of local ISP filtering, not because of bans we narrate.
- Never juxtapose a founder's wealth, residence, or purchase with a jurisdictional negative. ("...mansion in New York - a country where Stake is banned" is the exact pattern we never write.)
- Never imply impropriety, sketchiness, regulatory grey-area, or moral controversy around Stake, its founders (Ed Craven, Bijan Tehrani), its operator (Medium Rare N.V., Sweepsteaks Limited, Easygo Group Holdings), or its licence.
- Verified incident facts that are already in the public record (the September 2023 Lazarus hack, the March 2025 UK exit) **may** be referenced, but only when framed around the resolution: "withdrawals restored within hours", "user funds unaffected", "Stake has since expanded under direct licences in Italy, Brazil, Argentina". Never lead with the negative.
- The licence boilerplate everywhere on the site is:
  > Stake.com is operated by Medium Rare N.V., licensed by the Curaçao Gaming Control Board (CGCB) under direct B2C licence OGL/2024/1451/0918, issued under the National Ordinance on Games of Chance (LOK) framework that replaced the master/sublicence regime in 2024.

## Bonus terms — locked in

### Stake.com (`/promo-code/`)
- 200% match up to $3,000 (deposit up to $1,500 → bonus up to $3,000)
- Min deposit $10, max qualifying deposit $1,500
- 40x wagering on (deposit + bonus)
- KYC Level 3 required, claim through live support after deposit
- 200% credited within 24-48 hours
- 18+, new customers only, first deposit
- Code MAXBET
- Sports contributes 75% to rollover; casino games above 4% house edge contribute 100%

### Stake.us (`/stake-us-bonus/`)
- 25 SC + 25,000 GC on signup + verification (no deposit)
- 1 SC + 10,000 GC free daily for life with MAXBET
- 3x playthrough on SC before redemption
- 21+ (stricter than Stake.com)
- 19 restricted US states (Arizona, California, Connecticut, Delaware, Idaho, Kentucky, Louisiana, Maryland, Michigan, Montana, Nevada, New Jersey, New York, Pennsylvania, Rhode Island, Tennessee, Vermont, Washington, West Virginia)
- Sweepsteaks Limited operates
- Code MAXBET

**Never claim "400 free spins" anywhere.** That offer is retired; if you find a residual reference, replace it with the 40x wagering on deposit+bonus story.

## Source policy

Cite only:
- First-party Stake (stake.com, stake.us, help.stake.com)
- Sister sites we own (freetips.com, cryptotips.com)
- Arkham, Phemex
- Wikipedia
- Regulators (UKGC, MGA, CGCB)
- Neutral news (Reuters, FT, Bloomberg, Forbes, BleepingComputer for the Lazarus hack, TRM Labs, DL News)
- Industry trades (iGaming Business, NEXT.io)
- Game studios

**Never cite competitor affiliates.**

## Outbound links

- Stake.com affiliate URL: `https://www.getstake.it/i/Maxbet/io/maxbet/u/e0b1a52c69/uo/newbonus` (capital M).
- Stake.us affiliate URL: `https://stake.us/?c=maxbet`.
- All affiliate clicks must fire the GA4 `affiliate_click` (ONCE_PER_SESSION) and `outbound_click` (ONCE_PER_EVENT) events. GA4 property `391326200`.

## Page furniture

- Hero pattern: `<h1 class="ch-title text-gradient-gold">KEYWORD<span class="h1-sub">vibey line.</span></h1>`.
- Every commercial page must carry a "Last verified: <date>" stamp: `<time datetime="YYYY-MM-DD" class="verified-stamp">Last verified: D Month YYYY</time>` inserted right after `<p class="ch-sub">` and before `<div class="ch-actions">`.
- Canonical, hreflang (en/ko/x-default), OG, Twitter, JSON-LD (WebPage + BreadcrumbList + Offer + FAQPage on bonus pages) on every page.
- Voice player block (hostess narration) is **removed** sitewide as of 6 June 2026. Do not reintroduce.

## Verification ritual after any commit touching bonus, founder, or licence copy

1. `grep -rn "400 free spins\|400 프리\|400 스핀\|four hundred spins\|1668\|JAZ" .`
2. `grep -rn "banned from operating\|explicitly banned\|country where Stake" .`
3. `grep -rn "voice-player\|hostess\|vp-listen-label" .`

All three must return zero matches before push.
