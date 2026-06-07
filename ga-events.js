/* GA4 CTA event tracking — 2026-06-07 */
(function(){
  if(typeof gtag!=='function')return;
  function track(name,params){try{gtag('event',name,params||{})}catch(e){}}
  document.addEventListener('click',function(e){
    var t=e.target.closest('a,button');
    if(!t)return;
    var label=(t.getAttribute('aria-label')||t.textContent||'').trim().slice(0,80);
    var href=t.getAttribute('href')||'';
    // Stake affiliate clicks
    if(/getstake\.it|stake\.us|stake\.com/i.test(href)){
      track('affiliate_click',{cta_label:label,destination:href,location:window.location.pathname});
    }
    // CTA buttons (primary signup/claim)
    if(t.classList.contains('btn-signup')||t.classList.contains('btn-gold-grad')||/claim|step inside|take your seat/i.test(label)){
      track('cta_click',{cta_label:label,location:window.location.pathname});
    }
    // Lang switch
    if(t.closest('.lang-switcher,.mobile-lang-block')){
      track('lang_switch',{to:href||label});
    }
  },{passive:true});
  // Scroll depth
  var depths=[25,50,75,90],fired={};
  window.addEventListener('scroll',function(){
    var d=Math.round(((window.scrollY+window.innerHeight)/document.body.scrollHeight)*100);
    depths.forEach(function(p){if(d>=p&&!fired[p]){fired[p]=1;track('scroll',{percent:p})}});
  },{passive:true});
})();
