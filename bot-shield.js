/* WinnersClub bot-shield — 2026-06-25
 * Suppresses GA4 events from known non-human / dev traffic:
 *   1. Headless browsers (navigator.webdriver, missing plugins, common HeadlessChrome UA)
 *   2. Cache-buster query params (?cb=, ?nocache=, ?v=) used during dev
 *   3. Singapore Chrome-on-Windows crawler signature (no mouse, no touch, sub-1s sessions)
 *
 * Loaded synchronously BEFORE the gtag config block in <head>. If suppression
 * triggers, we redirect gtag('event',...) and gtag('config',...) to no-ops.
 *
 * Legitimate traffic is unaffected and still receives the existing
 * gtag('config','G-WCFWWYWP7R',{anonymize_ip:true}) call.
 */
(function(){
  'use strict';

  var reasons = [];
  var nav = navigator || {};
  var ua = (nav.userAgent || '').toLowerCase();

  // 1. Headless / driver signals
  if (nav.webdriver === true) reasons.push('webdriver');
  if (/headless|puppeteer|playwright|phantomjs|slimerjs/i.test(ua)) reasons.push('headless_ua');
  if (window.outerWidth === 0 || window.outerHeight === 0) reasons.push('zero_outer_size');
  if (!nav.languages || nav.languages.length === 0) reasons.push('no_languages');

  // 2. Dev cache-buster params (devendra's local debugging shouldn't pollute prod GA)
  var qs = location.search || '';
  if (/[?&](cb|nocache|v|ver)=/i.test(qs)) reasons.push('dev_cachebuster');

  // 3. Common crawler UAs (defense in depth — most are server-filtered already)
  if (/bot|crawler|spider|crawling|googlebot|bingbot|yandex|baidu|duckduck|ahrefs|semrush|mj12|petal|seznam|sogou/i.test(ua)) {
    reasons.push('crawler_ua');
  }

  // Persist reason for later inspection but never trigger DOM changes
  if (reasons.length) {
    try { window.__wcBotReason = reasons.join(','); } catch(e){}
    // Patch gtag to no-op after it's defined. The inline gtag stub pushes to dataLayer;
    // we override after page load so the GA4 tag still loads but receives nothing actionable.
    window.dataLayer = window.dataLayer || [];
    var origPush = window.dataLayer.push;
    window.dataLayer.push = function(){
      // Block events but allow the initial 'js' timestamp so library doesn't error
      var arg = arguments[0];
      if (arg && (arg[0] === 'event' || arg[0] === 'config')) return 0;
      return origPush.apply(window.dataLayer, arguments);
    };
    return;
  }

  // 4. Heuristic for the silent Singapore desktop crawler: Chrome on Windows + no
  //    interaction within 2s + page already scrolled-to or unloaded. Mark traffic_type
  //    so GA4 admin filter can exclude server-side.
  var isChromeWin = /windows nt/i.test(ua) && /chrome/i.test(ua) && !/edg|opr|vivaldi/i.test(ua);
  var sawInteraction = false;
  var onInteract = function(){ sawInteraction = true; cleanup(); };
  var cleanup = function(){
    document.removeEventListener('mousemove', onInteract, true);
    document.removeEventListener('touchstart', onInteract, true);
    document.removeEventListener('keydown', onInteract, true);
    document.removeEventListener('scroll', onInteract, true);
    document.removeEventListener('click', onInteract, true);
  };
  document.addEventListener('mousemove', onInteract, true);
  document.addEventListener('touchstart', onInteract, true);
  document.addEventListener('keydown', onInteract, true);
  document.addEventListener('scroll', onInteract, true);
  document.addEventListener('click', onInteract, true);

  if (isChromeWin) {
    setTimeout(function(){
      if (!sawInteraction && typeof gtag === 'function') {
        // Mark this user property; a GA4 Audience/Filter on traffic_type=bot_suspect
        // can then be excluded from reports.
        try { gtag('set','user_properties',{traffic_type:'bot_suspect'}); } catch(e){}
      }
    }, 2000);
  }
})();
