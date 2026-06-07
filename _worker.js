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

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const cookie = request.headers.get("cookie") || "";

    // Only redirect on root, and only if no cookie set, and not a bot/crawler
    const ua = request.headers.get("user-agent") || "";
    const isBot = /googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot|sogou|exabot|facebot|ia_archiver|applebot|petalbot/i.test(ua);

    if (path === "/" && !cookie.includes("wc_locale=") && !isBot) {
      const country = (request.cf && request.cf.country) || request.headers.get("cf-ipcountry") || "";
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
