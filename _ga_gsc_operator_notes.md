# Operator notes — GA4 + GSC follow-ups (2026-06-25)

Companion to `_ga_analysis_2026-06-25.md`. These are the one-time manual steps the agent cannot do for you.

## 1. GA4 — apply server-side bot filter (5 min)

The new `bot-shield.js` and the Cloudflare Worker block stop most bot traffic, but GA4 also lets you exclude already-collected sessions and harden against the next crawler. Do this once.

**Path: GA4 → Admin → Data Streams → web stream → Configure tag settings → Show all → Define internal traffic**

Add three filters:

| Filter name        | Type    | Pattern                                                           | traffic_type label |
| ------------------ | ------- | ----------------------------------------------------------------- | ------------------ |
| sg-crawler         | regex   | `Singapore` (match against `geo_country`)                         | `bot_suspect`      |
| dev-cachebusters   | regex   | `[?&](cb|nocache|v|ver)=` (match against `page_location`)         | `internal`         |
| office-ip          | IP      | your home + office IP                                             | `internal`         |

Then **Admin → Data Settings → Data Filters** → create a filter:
- Name: `Exclude bot_suspect and internal`
- Operation: **Exclude**
- Parameter: `traffic_type`
- Value: `bot_suspect|internal`
- State: **Active**

Once active, all sessions tagged by `bot-shield.js` (or by the rules above) are dropped from reports going forward. Historic data is unaffected (GA4 has no retro-filter).

## 2. Cloudflare WAF — add a permanent SG-crawler rule (3 min)

The Worker block handles the request, but adding a WAF rule means the crawler doesn't even consume a Worker invocation.

**Path: Cloudflare dashboard → winnersclub.com → Security → WAF → Custom rules → Create rule**

- Name: `block-sg-silent-crawler`
- Expression:
  ```
  (ip.geoip.country eq "SG"
    and http.user_agent contains "Windows NT"
    and http.user_agent contains "Chrome/"
    and not http.user_agent contains "Mobile"
    and not http.user_agent contains "Edg/"
    and len(http.request.headers["accept-language"][0]) lt 5
    and len(http.referer) eq 0)
  ```
- Action: **Block**

If your home Singapore VPN matches, swap the rule from `Block` to `Managed Challenge` instead.

## 3. GSC — service account role escalation (2 min)

The Pipedream connector currently fails with `Access denied` because the service account only has `Restricted` access. Fix it once.

**Path: Search Console → Settings → Users and permissions**

1. Find the service account email (looks like `pipedream-xxxx@gserviceaccount.com` or similar).
2. Change role from **Restricted** to **Owner** (or at minimum **Full**).
3. Re-run any query that previously failed — no reconnect needed.

If you can't find the email, check the Pipedream connection screen for the principal name we authorized.

## 4. KO indexing — submit 19 URLs (10 min, requires GSC access)

Once #3 above is fixed, ping me with "submit ko URLs to GSC" and I'll run the URL Inspection submissions. Alternatively, do it manually:

**Path: Search Console → URL Inspection → paste URL → Request Indexing**

URLs to submit (from earlier session):
- `https://winnersclub.com/ko/`
- `https://winnersclub.com/ko/about-stake/`
- `https://winnersclub.com/ko/aviator/`
- `https://winnersclub.com/ko/casino/`
- `https://winnersclub.com/ko/live-casino/`
- `https://winnersclub.com/ko/live-odds/`
- `https://winnersclub.com/ko/mirror/`
- `https://winnersclub.com/ko/news/`
- `https://winnersclub.com/ko/originals/`
- `https://winnersclub.com/ko/payments/`
- `https://winnersclub.com/ko/poker/`
- `https://winnersclub.com/ko/promo-code/`
- `https://winnersclub.com/ko/reserves/`
- `https://winnersclub.com/ko/responsible-gambling/`
- `https://winnersclub.com/ko/slots/`
- `https://winnersclub.com/ko/sports/`
- `https://winnersclub.com/ko/stake-engine/`
- `https://winnersclub.com/ko/stake-us-bonus/`
- `https://winnersclub.com/ko/vip/`

GSC throttles to ~10 requests per day, so this takes two sittings.

## Notes on findings that turned out to be non-issues

- **/ko/promo-code/ 18% engagement** — investigated, false alarm. The page is healthy, the corpus is just 17 sessions (13 mobile + 4 desktop). Small-N noise. KO core page (`/ko/`) sits at 43% mobile bounce / 37% desktop bounce, which is great.
- **Desktop 72% bounce** — mostly US dev cache-buster sessions (`?cb=*`, `?v=*`) plus the SG crawler. After the filters and shield above land, expect desktop bounce to drop to roughly Germany-level (17–35%) once a new 28-day window rolls.
