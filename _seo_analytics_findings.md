# WinnersClub.com — GSC + GA Findings (May 8 – Jun 7, 2026)

## TL;DR
- **CTR is healthy on brand queries** ("winners club casino" 12.4%, "winnersclub" 11.3%) — keep the meta titles where they are.
- **CTR is collapsing on near-brand queries** like "winner casino online" (531 imp, 0 clicks at position 23) and "stake sign up" (411 imp, 0 clicks at position 31) — we're ranking but the title/description isn't compelling enough to beat competitors above us.
- **Bounce is high on /en/** (66%) and short on most money pages (/poker 4s avg, /aviator 11s, /sports 21s) — content depth is the problem, not traffic.
- **/ko/ is the conversion engine** — 228 sessions, low bounce, 84s avg duration. Korean visitors engage 12x harder than English ones.

## CTR optimization targets (high impressions, near-zero clicks)

| Query | Impressions | Avg Position | Action |
|---|---|---|---|
| winner casino | 1,832 | 29 | Brand confusion — we're showing for the wrong query. Add `noindex` on irrelevant pages or strengthen "WinnersClub" branding in title |
| winnerclub | 560 | 13.5 | Rewrite meta title to lead with "Winnerclub" (note the missing 's' — common misspelling) |
| winner casino online | 531 | 23.8 | We're never breaking page 1. Either ignore or accept it's not our brand |
| stake sign up | 411 | 31.3 | High value — write a dedicated `/stake-sign-up/` landing page. We have /promo-code but Google isn't matching it |
| winner casino login | 285 | 23.7 | Ignore — irrelevant brand confusion |

## Strong-CTR queries — protect these meta titles
- `winners club casino` — 12.4% CTR at position 3.1 ← our brand keyword, do not touch
- `winners club online casino` — 14.8% CTR at position 1.4
- `winnerclub crypto casino` — 10.6% CTR at position 1.3
- `winners club online casino login` — 18.4% CTR at position 1.5

## GA drop-off targets

### High bounce on landing pages
- **/en/** — 66% bounce on 236 sessions. The top landing page is leaking 2 in 3 visitors. Likely hero is too text-heavy, CTA buried, or no language match for visitor (we now have geo-redirect via `_worker.js`)
- **/en/casino/** — 52% bounce on 29 sessions
- **/en/mirror-sites/** — 56% bounce on 9 sessions, only 6s avg
- **/ko/casino/** — 0% bounce but 7s avg duration (people clicked away but didn't fully leave the site)

### Short duration = thin content
- **/poker/** — 4s avg (12 sessions). Page content is probably too short. Expand.
- **/aviator/** — 11s avg. Same — needs more depth.
- **/sports/** — 21s avg. Needs depth.
- **/en/stake-promo-codes/** — 8s. Confusing path — we already have /promo-code/, this duplicate is hurting us.
- **/ko/casino/** — 7s. Korean visitors bounce off the casino page within 7 seconds. Translation might be off, or load is slow.

### Healthy pages
- **/ko/** — 228 sessions, 84s avg duration, 35% bounce → keep doing whatever this does
- **/reserves/** — 248s avg duration on 12 sessions, 8% bounce → people love the proof-of-reserves data
- **/about-stake/** — 95s avg, 13% bounce → strong

## Concrete next actions

1. **Consolidate the /promo-code/ duplication** — Google sees both `/promo-code/` and `/en/stake-promo-codes/`. Pick one canonical and 301 the other.
2. **Write 500–800 more words on /poker/, /aviator/, /sports/** — currently too thin. Real strategy notes, market lists, odds explanations.
3. **Investigate /ko/casino/ 7s avg duration** — likely translation issue or layout broken at Korean text length.
4. **Build /stake-sign-up/ as a dedicated funnel page** — we have 411 impressions/month at position 31 for "stake sign up" with zero clicks. A purpose-built page can rank top 10 inside 60 days.
5. **Audit hero on /en/** — 66% bounce is the single biggest revenue leak. Test hero copy variants, add the trust shelf (license + reserves + last-verified pill).
