// WinnersClub — Cloudflare Pages Worker
// Geo-redirect first-time visitors to their locale-specific landing page.
// Only triggers on the root URL "/" and only when no wc_locale cookie is set.
// Respects user's manual language choice via the wc_locale cookie (1 year).

const COUNTRY_LOCALE = {
  KR: "ko",            // South Korea
  CN: "zh", HK: "zh", TW: "zh", SG: "zh", MO: "zh",
  VN: "vi",
  TH: "th",
  MY: "ms", ID: "ms", BN: "ms",
  BR: "pt", PT: "pt", AO: "pt", MZ: "pt",
  JP: "ja",
};

const KNOWN_LOCALES = new Set(["ko","zh","vi","th","ms","pt","ja","en"]);

// SEO compound-URL trap patterns. Any request whose path matches one of these
// returns 410 (Gone) with header x-winnersclub-trap: 1, telling Google to
// drop it from the index. See functions/_middleware.js and seo_guard.py.
//
// IMPORTANT: this site uses Advanced-mode _worker.js. That mode disables
// functions/_middleware.js entirely, so the trap logic must live here.
const TRAP_PATTERNS = [
  /^\/__media__\//i,
  /^\/uploaded_attachments\//i,
  /\.html\/[^?#]+/i,
  /^\/(about-stake|aviator|live-casino|live-odds|mirror|originals|payments|poker|promo-code|reserves|responsible-gambling|slots|sports|stake-engine|stake-us-bonus|vip|news|casino)\/[^/]+\/[^/]+\/[^/]+/i,
  /^\/(ar|es|fr|hi|id|ja|ko|ms|pl|pt|pt-br|ru|th|tr|uz|vi)\/(about-stake|aviator|live-casino|live-odds|mirror|originals|payments|poker|promo-code|reserves|responsible-gambling|slots|sports|stake-engine|stake-us-bonus|vip|news|casino)\/[^/]+\/[^/]+/i,
  /^\/link\/[^/]+\/[^/]+\/[^/]+/i,
];

async function serveTrap410(request, env) {
  // Reuse the existing /404.html body for nice UX, but return 410.
  const trapUrl = new URL("/404.html", request.url);
  let body = "";
  try {
    const r = await env.ASSETS.fetch(new Request(trapUrl.toString(), { method: "GET" }));
    body = await r.text();
  } catch (e) {
    body = "<!doctype html><title>Gone</title><h1>410 Gone</h1>";
  }
  return new Response(body, {
    status: 410,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "cache-control": "public, max-age=3600",
      "x-winnersclub-trap": "1",
    },
  });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const cookie = request.headers.get("cookie") || "";

    // Only redirect on root, and only if no cookie set, and not a bot/crawler
    const ua = request.headers.get("user-agent") || "";
    const isBot = /googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot|sogou|exabot|facebot|ia_archiver|applebot|petalbot|ahrefsbot|semrushbot|mj12bot|seznambot|dotbot/i.test(ua);
    const country = (request.cf && request.cf.country) || request.headers.get("cf-ipcountry") || "";
    const asn = (request.cf && request.cf.asn) || 0;
    // Signature of the silent SG crawler that has been hammering every locale:
    //   - Country = SG
    //   - UA = Chrome on Windows (no mobile token)
    //   - No Accept-Language header OR very short value
    //   - No referrer
    // Block at the edge before assets are served.
    const accLang = request.headers.get("accept-language") || "";
    const referer = request.headers.get("referer") || "";
    const looksLikeSgCrawler =
      country === "SG" &&
      /Windows NT/i.test(ua) &&
      /Chrome\//i.test(ua) &&
      !/Mobile|Android|iPhone|iPad/i.test(ua) &&
      !/Edg\/|OPR\/|Vivaldi/i.test(ua) &&
      !referer &&
      accLang.length < 5;
    if (looksLikeSgCrawler) {
      return new Response("forbidden", { status: 403, headers: { "X-WC-Block": "sg-crawler", "Cache-Control": "private, no-store" } });
    }

    // SEO trap: return 410 for known compound-URL garbage paths so Google deindexes them.
    // Must run BEFORE locale handling so /ko/casino/foo/bar/baz traps even when the
    // user has a ko cookie. Bots benefit from the explicit Gone signal regardless.
    for (const re of TRAP_PATTERNS) {
      if (re.test(path)) {
        return serveTrap410(request, env);
      }
    }

    if (path === "/" && !cookie.includes("wc_locale=") && !isBot) {
      const locale = COUNTRY_LOCALE[country];
      if (locale && KNOWN_LOCALES.has(locale) && locale !== "en") {
        const target = "/" + locale + "/";
        return new Response(null, {
          status: 302,
          headers: {
            "Location": target,
            "Set-Cookie": `wc_locale=${locale}; Path=/; Max-Age=31536000; SameSite=Lax; Secure`,
            "Vary": "CF-IPCountry, Cookie",
            "Cache-Control": "private, no-store"
          }
        });
      }
      // Default — set en cookie so we don't recheck every visit
      const res = await env.ASSETS.fetch(request);
      const newRes = new Response(res.body, res);
      newRes.headers.append("Set-Cookie", "wc_locale=en; Path=/; Max-Age=31536000; SameSite=Lax; Secure");
      return newRes;
    }

    // If user navigates to /ko/, /zh/ etc., remember that choice
    const segMatch = path.match(/^\/([a-z]{2})\/?/);
    if (segMatch && KNOWN_LOCALES.has(segMatch[1])) {
      const res = await env.ASSETS.fetch(request);
      if (!cookie.includes(`wc_locale=${segMatch[1]}`)) {
        const newRes = new Response(res.body, res);
        newRes.headers.append("Set-Cookie", `wc_locale=${segMatch[1]}; Path=/; Max-Age=31536000; SameSite=Lax; Secure`);
        return newRes;
      }
      return res;
    }

    return env.ASSETS.fetch(request);
  }
};
