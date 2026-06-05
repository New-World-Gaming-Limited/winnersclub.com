/* winnersclub.com exit-click tracker
 * Fires gtag('event','exit_click', {...}) on every outbound CTA.
 * Captures: destination, label, locale, page slug, position in page.
 * Loaded site-wide via /exit-tracker.js (deferred).
 */
(function () {
  'use strict';
  if (typeof window === 'undefined') return;

  // Hosts treated as "outbound" / affiliate clicks
  var OUTBOUND_HOSTS = [
    'winnersclub.com',          // internal redirect path /link/...
    'playstake.io',
    'stake.com',
    'stake.games',
    '1win.pro',
    '1win.online',
    '1win.com'
  ];

  function isOutbound(href) {
    if (!href) return false;
    // /link/ on our own host counts as affiliate redirect
    if (href.indexOf('/link/') === 0) return true;
    try {
      var u = new URL(href, window.location.origin);
      var host = u.hostname.replace(/^www\./, '');
      if (host === window.location.hostname.replace(/^www\./, '')) {
        // same host \u2014 only count /link/ path
        return u.pathname.indexOf('/link/') === 0;
      }
      for (var i = 0; i < OUTBOUND_HOSTS.length; i++) {
        if (host === OUTBOUND_HOSTS[i] || host.endsWith('.' + OUTBOUND_HOSTS[i])) {
          return true;
        }
      }
    } catch (e) { return false; }
    return false;
  }

  function pageSlug() {
    var p = window.location.pathname.replace(/^\//, '').replace(/\/$/, '');
    return p || 'home';
  }

  function pageLocale() {
    var seg = window.location.pathname.split('/').filter(Boolean)[0] || 'en';
    return seg.length === 2 || seg === 'pt-br' || seg === 'zh-tw' ? seg : 'en';
  }

  function ctaLabel(el) {
    var t = (el.textContent || '').replace(/\s+/g, ' ').trim();
    return t.slice(0, 80);
  }

  function ctaPosition(el) {
    // bucket position: hero, mid, footer
    var rect = el.getBoundingClientRect();
    var top = rect.top + window.scrollY;
    var doc = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
    var ratio = top / doc;
    if (ratio < 0.25) return 'hero';
    if (ratio > 0.75) return 'footer';
    return 'mid';
  }

  function fire(el, href) {
    var payload = {
      destination: href,
      cta_label: ctaLabel(el),
      cta_locale: pageLocale(),
      cta_page: pageSlug(),
      cta_position: ctaPosition(el)
    };
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'exit_click', payload);
    }
    // also push to dataLayer for GTM if present
    if (window.dataLayer && typeof window.dataLayer.push === 'function') {
      window.dataLayer.push(Object.assign({ event: 'exit_click' }, payload));
    }
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    if (!isOutbound(href)) return;
    fire(a, href);
    // do not preventDefault \u2014 let the navigation proceed
  }, true);
})();
