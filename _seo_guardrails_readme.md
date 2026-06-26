# SEO deploy guardrails — winnersclub.com

These files exist to prevent the May 2026 bets.ng-class deindex bug.
Background: static sites on Cloudflare Pages soft-404 compound URLs at HTTP 200,
Googlebot recursion-crawls them, the site gets deindexed.
Full postmortem: `skills/user/seo-deploy-guardrails/references/the-may-2026-deindex-postmortem.md`.

## Files

| File | Purpose |
|---|---|
| `_worker.js` | Cloudflare Pages **Advanced Mode** worker. Owns the trap-410 logic (lines ~17-50) because Advanced Mode bypasses `functions/_middleware.js` entirely. Also handles geo-redirect, SG-crawler block, and locale cookie logic. |
| `functions/_middleware.js` | Synced fallback. Only runs if `_worker.js` is removed. Kept for documentation + defense-in-depth. |
| `404.html` | Branded 404 page with exactly one `<meta name="robots" content="noindex,follow">`. The 410 trap responses reuse this body. |
| `_redirects` | Cloudflare Pages routing. **Must never** contain `/* /index.html 200` (the original deindex bug). |
| `robots.txt` | Must declare `Sitemap:` line. |
| `seo_guard.py` | Pre-deploy offline guard. 15 checks. Exit 1 = block deploy. |
| `seo_verify_live.py` | Post-deploy live verifier. 7 hard traps (410+header), 1 soft trap (3xx), 11 real pages, sitemap shape, 404.html robots tag. Run with `--wait-seconds 90` after `git push`. |

## Workflow

```bash
cd /home/user/workspace/winnersclub.com

# Before any deploy:
python3 seo_guard.py
# exit 0 -> safe to deploy
# exit 1 -> DO NOT DEPLOY, fix the listed failures first

# After git push (Cloudflare Pages auto-deploys):
python3 seo_verify_live.py --wait-seconds 90
# exit 0 -> live site behaviour is correct
# exit 1 -> regression detected, escalate
```

## Recurring cron

Cron `4836b418` runs **Monday 02:00 UTC** (04:00 CEST). It:
1. Pulls `main`
2. Runs `seo_guard.py` (notifies if FAIL)
3. Runs `seo_verify_live.py` (notifies if FAIL)
4. Silent on success

To update, use `pplx-tool schedule_cron action=update cron_id=4836b418 ...`.

## When to update trap patterns

Edit `TRAP_PATTERNS` in `_worker.js` (and keep `functions/_middleware.js` in sync) if:
- A new top-level section is added (e.g. `/esports/` joins `casino`, `sports`, `poker`)
- Search Console shows a new compound-URL pattern being soft-404'd
- A new locale is added (extend the locale regex)

After any pattern change, re-run `seo_guard.py` and `seo_verify_live.py`.
