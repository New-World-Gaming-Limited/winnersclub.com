// Language detection and redirect for winnersclub.com
// Strategy: First-visit only. Cloudflare IP geolocation + browser language tiebreaker.
(function() {
  'use strict';
  
  // Skip if user has already chosen a language (cookie set when they use the switcher or visit a non-English version)
  if (document.cookie.indexOf('lang_set=') !== -1) return;
  if (localStorage.getItem('lang_set')) return;
  
  // Skip if already on a non-English path (means they navigated there intentionally)
  var path = window.location.pathname;
  var supportedLangs = ['fr','de','es','pt','ru','tr','hi','bn','ar','ja','ko','zh','vi','th','nl','it','pl','ro','el','bg','uk','cs','da','fi','sv','nb','hu','sk','sl','hr','sr','sq','lt','lv','et','mt','ms','id','tl','mn','uz','fa','he','lo','ur','kk','en'];
  
  // Check if URL starts with a language code
  var pathLang = path.split('/')[1];
  if (supportedLangs.indexOf(pathLang) !== -1) {
    // User is already on a language page — remember their choice
    setLangCookie(pathLang);
    return;
  }
  
  // Skip on 404 page or special files
  if (path.match(/\.(xml|txt|json|html)$/) || path.indexOf('google') !== -1) return;
  
  // Country -> language mapping
  // Single-language countries map directly. Multi-language countries (IN, BD) handled with browser fallback.
  var countryToLang = {
    // Direct single-language mappings
    'FR':'fr','BE':'fr','CH':'fr','LU':'fr','MC':'fr','SN':'fr','CI':'fr','CM':'fr','MA':'fr','TN':'fr','DZ':'fr','HT':'fr',
    'DE':'de','AT':'de',
    'ES':'es','MX':'es','AR':'es','CO':'es','PE':'es','CL':'es','VE':'es','EC':'es','GT':'es','CU':'es','BO':'es','DO':'es','HN':'es','PY':'es','SV':'es','NI':'es','CR':'es','PA':'es','UY':'es',
    'PT':'pt','BR':'pt','AO':'pt','MZ':'pt',
    'RU':'ru','BY':'ru','KZ':'kk','KG':'ru','TJ':'ru','UZ':'uz',
    'TR':'tr','CY':'tr',
    'JP':'ja','KR':'ko','CN':'zh','TW':'zh','HK':'zh','SG':'zh',
    'VN':'vi','TH':'th','LA':'lo','MM':'lo',
    'NL':'nl',
    'IT':'it','SM':'it','VA':'it',
    'PL':'pl','RO':'ro','MD':'ro',
    'GR':'el',
    'BG':'bg','UA':'uk','CZ':'cs','SK':'sk','HU':'hu','SI':'sl','HR':'hr','RS':'sr','BA':'sr','ME':'sr','MK':'sr',
    'AL':'sq','XK':'sq',
    'LT':'lt','LV':'lv','EE':'et','MT':'mt','FI':'fi','SE':'sv','NO':'nb','DK':'da','IS':'da',
    'MY':'ms','BN':'ms','ID':'id','PH':'tl',
    'MN':'mn',
    'IR':'fa','AF':'fa','IL':'he','PS':'ar','PK':'ur',
    // Arabic countries
    'SA':'ar','AE':'ar','EG':'ar','IQ':'ar','JO':'ar','LB':'ar','OM':'ar','QA':'ar','KW':'ar','BH':'ar','YE':'ar','SY':'ar','LY':'ar','SD':'ar',
    // Multi-language: keep null, fall back to browser
    'IN':null,'BD':null
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
      var l = langs[i].toLowerCase().split('-')[0];
      // Map browser lang code to our supported codes
      if (l === 'no') l = 'nb';
      if (l === 'iw') l = 'he';
      if (l === 'in') l = 'id';
      if (l === 'ji') l = 'he';
      if (l === 'jw') l = 'id';
      if (supportedLangs.indexOf(l) !== -1) return l;
    }
    return 'en';
  }
  
  function redirectToLang(lang) {
    setLangCookie(lang);
    if (lang === 'en') return; // English is at root, no redirect
    
    // Redirect to /{lang}{current-path}
    var newPath = '/' + lang + (path === '/' ? '/' : path);
    // Avoid double slashes
    newPath = newPath.replace(/\/+/g, '/');
    window.location.replace(newPath);
  }
  
  // Try Cloudflare's geolocation endpoint
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
        if (lang === null) {
          // Multi-language country: use browser as tiebreaker
          lang = browserLangToSupported();
        }
      }
      
      if (!lang) lang = browserLangToSupported();
      
      redirectToLang(lang);
    })
    .catch(function() {
      // Cloudflare detection failed: fall back to browser language
      var lang = browserLangToSupported();
      redirectToLang(lang);
    });
})();
