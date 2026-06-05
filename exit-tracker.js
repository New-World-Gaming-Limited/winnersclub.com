/* winnersclub.com exit-click tracker — v2 (2026-06-05)
 *
 * Fires two GA4 events on outbound clicks:
 *   - affiliate_click  → revenue path (stake.com, getstake.it, stake.us, stakeengine.com, /link/)
 *   - outbound_click   → citations / regulators / news / other 3rd-party hosts
 *
 * Both events also push to dataLayer for GTM compatibility.
 *
 * Reliability:
 *   - transport_type: 'beacon'  → uses sendBeacon so the event flushes even
 *                                 when the browser is mid-navigation.
 *   - listens on 'mousedown' (capture) so the event is queued *before* the
 *     click handler triggers navigation. Falls back to 'click' for keyboard /
 *     touch-only paths and for middle-click / cmd-click new-tab opens.
 *
 * Payload (per event):
 *   destination      full href
 *   destination_host hostname only (easier to pivot on in GA4)
 *   cta_label        visible text of the link, truncated to 80 chars
 *   cta_locale       'en' or 'ko' (extend as new locales ship)
 *   cta_page         page slug, e.g. 'promo-code', 'home'
 *   cta_position     'hero' | 'mid' | 'footer'
 *   cta_id           value of data-cta-id if present, else ''
 *   link_target      '_blank' or '_self'
 */
(function () {
  'use strict';
  if (typeof window === 'undefined') return;

  // Hosts that count as your revenue path → fire affiliate_click
  var AFFILIATE_HOSTS = [
    'getstake.it',
    'stake.com',
    'stake.us',
    'stake.games',
    'stake.bet.br',
    'stakeengine.com'
  ];

  // Known locale prefixes (extend when new translations ship)
  var KNOWN_LOCALES = ['en', 'ko'];

  // De-dupe guard so mousedown + click for the same user action don't double-fire
  var fired = new WeakMap();

  function normalizeHost(host) {
    return (host || '').replace(/^www\./, '').toLowerCase();
  }

  function classify(href) {
    if (!href) return null;
    // /link/ on our own host = internal affiliate redirect
    if (href.indexOf('/link/') === 0) return { kind: 'affiliate', host: window.location.hostname };
    try {
      var u = new URL(href, window.location.origin);
      var host = normalizeHost(u.hostname);
      var selfHost = normalizeHost(window.location.hostname);
      if (host === selfHost) {
        // same host — only count /link/ path
        return u.pathname.indexOf('/link/') === 0
          ? { kind: 'affiliate', host: host }
          : null;
      }
      for (var i = 0; i < AFFILIATE_HOSTS.length; i++) {
        var ah = AFFILIATE_HOSTS[i];
        if (host === ah || host.endsWith('.' + ah)) {
          return { kind: 'affiliate', host: host };
        }
      }
      // 3rd-party but not affiliate → citation / outbound
      // Skip pure analytics / asset hosts to keep noise down
      if (/^(www\.)?(google-analytics|googletagmanager|gstatic|googleapis|fonts\.googleapis|fonts\.gstatic|cloudflareinsights)\./.test(host)) {
        return null;
      }
      return { kind: 'outbound', host: host };
    } catch (e) {
      return null;
    }
  }

  function pageSlug() {
    var p = window.location.pathname.replace(/^\//, '').replace(/\/$/, '');
    // strip leading locale segment for cleaner slug
    var parts = p.split('/');
    if (parts.length && KNOWN_LOCALES.indexOf(parts[0]) !== -1) parts.shift();
    return parts.join('/') || 'home';
  }

  function pageLocale() {
    var seg = window.location.pathname.split('/').filter(Boolean)[0] || '';
    return KNOWN_LOCALES.indexOf(seg) !== -1 ? seg : 'en';
  }

  function ctaLabel(el) {
    var t = (el.getAttribute('aria-label') || el.textContent || '').replace(/\s+/g, ' ').trim();
    return t.slice(0, 80);
  }

  function ctaPosition(el) {
    var rect = el.getBoundingClientRect();
    var top = rect.top + window.scrollY;
    var doc = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight, 1);
    var ratio = top / doc;
    if (ratio < 0.25) return 'hero';
    if (ratio > 0.75) return 'footer';
    return 'mid';
  }

  function fire(el, href, info) {
    if (fired.get(el)) return;
    fired.set(el, true);
    // re-arm after 500ms so subsequent clicks on the same persistent button still register
    setTimeout(function () { fired.delete(el); }, 500);

    var eventName = info.kind === 'affiliate' ? 'affiliate_click' : 'outbound_click';
    var payload = {
      destination: href,
      destination_host: info.host,
      cta_label: ctaLabel(el),
      cta_locale: pageLocale(),
      cta_page: pageSlug(),
      cta_position: ctaPosition(el),
      cta_id: el.getAttribute('data-cta-id') || '',
      link_target: el.getAttribute('target') || '_self',
      // ensure the event flushes before navigation
      transport_type: 'beacon'
    };

    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, payload);
    }
    if (window.dataLayer && typeof window.dataLayer.push === 'function') {
      window.dataLayer.push(Object.assign({ event: eventName }, payload));
    }
  }

  function handle(e) {
    var a = e.target && e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    var info = classify(href);
    if (!info) return;
    fire(a, href, info);
  }

  // mousedown fires *before* the browser starts navigating — best chance
  // for the beacon to leave the tab on same-window clicks.
  document.addEventListener('mousedown', handle, true);
  // click catches keyboard activation, touch, and middle/cmd-click new-tab.
  document.addEventListener('click', handle, true);
  // auxclick catches middle-click specifically on some browsers.
  document.addEventListener('auxclick', handle, true);
})();
