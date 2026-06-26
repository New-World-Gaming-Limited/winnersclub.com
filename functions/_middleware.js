// Cloudflare Pages middleware for winnersclub.com
// Purpose: return HTTP 410 (Gone) for known soft-404 compound URL traps so
// Google deindexes them faster than the default 404.
//
// Background: when a static site on Cloudflare Pages serves index.html with
// status 200 for any unmatched path, Googlebot crawls recursive garbage paths
// and the site gets soft-404'd. _redirects with status 410 does not work
// reliably with splat rules in Cloudflare Pages (the 404.html static fallback
// wins first), so we explicitly intercept here.
//
// Falls through to static assets and the auto-served 404.html for anything
// not matching a trap pattern.
//
// See seo-deploy-guardrails skill / the-may-2026-deindex-postmortem.md.

const TRAP_PATTERNS = [
  // 1. Spam directories we 410 elsewhere too
  /^\/__media__\//i,
  /^\/uploaded_attachments\//i,

  // 2. Compound URLs under a real .html page (any path that contains .html/ in the middle)
  //    e.g. /promo-code/index.html/casino/stake/foo
  //    e.g. /index.html/anything
  /\.html\/[^?#]+/i,

  // 3. Compound URLs deep under known top-level sections that should not have
  //    grandchildren (any path > 3 segments under these single-page sections)
  /^\/(about-stake|aviator|live-casino|live-odds|mirror|originals|payments|poker|promo-code|reserves|responsible-gambling|slots|sports|stake-engine|stake-us-bonus|vip|news|casino)\/[^/]+\/[^/]+\/[^/]+/i,

  // 4. Same pattern but under any locale prefix (ar, es, fr, hi, id, ja, ko,
  //    ms, pl, pt, pt-br, ru, th, tr, uz, vi)
  /^\/(ar|es|fr|hi|id|ja|ko|ms|pl|pt|pt-br|ru|th|tr|uz|vi)\/(about-stake|aviator|live-casino|live-odds|mirror|originals|payments|poker|promo-code|reserves|responsible-gambling|slots|sports|stake-engine|stake-us-bonus|vip|news|casino)\/[^/]+\/[^/]+/i,

  // 5. Affiliate-redirector spam paths that show up in logs but were never real
  //    /link/<token>/<id>/<extra> with more than the canonical two segments
  /^\/link\/[^/]+\/[^/]+\/[^/]+/i,
];

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const path = url.pathname;

  for (const re of TRAP_PATTERNS) {
    if (re.test(path)) {
      // Serve the 404.html body with a 410 status so the page has proper UX
      // and Google sees an explicit Gone signal.
      const body = await context.env.ASSETS.fetch(new URL("/404.html", url)).then(r => r.text());
      return new Response(body, {
        status: 410,
        headers: {
          "content-type": "text/html; charset=utf-8",
          "cache-control": "public, max-age=3600",
          "x-winnersclub-trap": "1",
        },
      });
    }
  }

  // Not a trap; let static assets and Cloudflare Pages default handling run.
  return context.next();
}
