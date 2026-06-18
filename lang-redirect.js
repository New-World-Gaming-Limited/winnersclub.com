// Language detection and redirect for winnersclub.com
// Strategy: First-visit only. Cloudflare IP geolocation + browser language tiebreaker.
// Only redirects to languages the site actually ships.
(function() {
  'use strict';

  // Skip if user has already chosen a language
  if (document.cookie.indexOf('lang_set=') !== -1) return;
  if (localStorage.getItem('lang_set')) return;

  var path = window.location.pathname;

  // The 15 locales we actually have on disk.
  var supportedLangs = ['en','ko','zh','vi','th','ms','pt','ja','es','pt-br','tr','id','fr','ru','hi','ar'];

  // If user is already on a language path, remember it and exit
  var pathLang = path.split('/')[1];
  if (supportedLangs.indexOf(pathLang) !== -1) {
    setLangCookie(pathLang);
    return;
  }

  // Skip on special files
  if (path.match(/\.(xml|txt|json|html)$/) || path.indexOf('google') !== -1) return;

  // Country -> language mapping. Only languages we ship.
  // Countries that map to languages we don't have stay null -> fall through to English.
  var countryToLang = {
    // Korean
    'KR':'ko',
    // Chinese (Simplified target; we ship zh-Hans)
    'CN':'zh','HK':'zh','MO':'zh','TW':'zh',
    // Vietnamese
    'VN':'vi',
    // Thai
    'TH':'th',
    // Malay (Malaysia, Brunei, Singapore)
    'MY':'ms','BN':'ms','SG':'ms',
    // Portuguese (Portugal + lusophone Africa - NOT Brazil, which gets pt-br)
    'PT':'pt','AO':'pt','MZ':'pt','CV':'pt','GW':'pt','ST':'pt','TL':'pt',
    // Japanese
    'JP':'ja',
    // Spanish (LATAM)
    'MX':'es','AR':'es','CO':'es','CL':'es','PE':'es','BO':'es','EC':'es',
    'GT':'es','HN':'es','NI':'es','PA':'es','PY':'es','UY':'es','VE':'es',
    'CR':'es','DO':'es','SV':'es','CU':'es','PR':'es',
    // Brazilian Portuguese
    'BR':'pt-br',
    // Turkish
    'TR':'tr',
    // Indonesian (now gets id instead of ms)
    'ID':'id',
    // French (France + Francophone countries)
    'FR':'fr','BE':'fr','SN':'fr','CI':'fr','ML':'fr','BF':'fr','NE':'fr',
    'CD':'fr','GA':'fr','CM':'fr','TG':'fr','BJ':'fr','MG':'fr','GN':'fr',
    'CF':'fr','CG':'fr','DJ':'fr','KM':'fr','RE':'fr','MQ':'fr','GP':'fr',
    // Russian (CIS region)
    'RU':'ru','BY':'ru','KZ':'ru','KG':'ru','AM':'ru','AZ':'ru','TJ':'ru','UZ':'ru',
    // Hindi (India)
    'IN':'hi',
    // Arabic (Arab world)
    'SA':'ar','AE':'ar','EG':'ar','IQ':'ar','JO':'ar','KW':'ar','LB':'ar',
    'LY':'ar','MA':'ar','OM':'ar','PS':'ar','QA':'ar','SY':'ar','TN':'ar',
    'YE':'ar','BH':'ar','DZ':'ar','SD':'ar','MR':'ar',
  };

  function setLangCookie(lang) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (365 * 24 * 60 * 60 * 1000));
    document.cookie = 'lang_set=' + lang + ';expires=' + expires.toUTCString() + ';path=/;SameSite=Lax';
    try { localStorage.setItem('lang_set', lang); } catch(e) {}
  }

  function browserLangToSupported() {
    var langs = navigator.languages || [navigator.language || navigator.userLanguage || 'en'];
    for (var i = 0; i < langs.length; i++) {
      var l = langs[i].toLowerCase();
      // Handle pt-BR specifically
      if (l === 'pt-br' || l === 'pt_br') return 'pt-br';
      var base = l.split('-')[0];
      if (supportedLangs.indexOf(base) !== -1) return base;
      if (supportedLangs.indexOf(l) !== -1) return l;
    }
    return 'en';
  }

  function redirectToLang(lang) {
    setLangCookie(lang);
    if (lang === 'en') return; // EN is at root
    var newPath = '/' + lang + (path === '/' ? '/' : path);
    newPath = newPath.replace(/\/+/g, '/');
    // Sanity check: only redirect if target lang dir is known
    if (supportedLangs.indexOf(lang) === -1) return;
    window.location.replace(newPath);
  }

  // Use Cloudflare geolocation
  fetch('/cdn-cgi/trace', { cache: 'no-store' })
    .then(function(r) {
      if (!r.ok) throw new Error('CF unavailable');
      return r.text();
    })
    .then(function(text) {
      var match = text.match(/loc=([A-Z]{2})/);
      var country = match ? match[1] : null;
      var lang = null;

      if (country && country in countryToLang) {
        lang = countryToLang[country];
      }
      if (!lang) lang = browserLangToSupported();
      redirectToLang(lang);
    })
    .catch(function() {
      var lang = browserLangToSupported();
      redirectToLang(lang);
    });
})();
