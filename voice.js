(function(){
  document.querySelectorAll('.voice-player').forEach(function(p){
    var btn = p.querySelector('.vp-btn');
    var transcriptToggle = p.querySelector('.vp-transcript');
    if (btn) btn.addEventListener('click', function(){
      var src = p.getAttribute('data-audio');
      if (!src) { p.setAttribute('data-open', p.getAttribute('data-open')==='true' ? 'false' : 'true'); return; }
      var audio = p._audio || (p._audio = new Audio(src));
      if (audio.paused) { audio.play(); btn.innerHTML='&#9208;'; } else { audio.pause(); btn.innerHTML='&#9658;'; }
    });
    if (transcriptToggle) transcriptToggle.addEventListener('click', function(){
      p.setAttribute('data-open', p.getAttribute('data-open')==='true' ? 'false' : 'true');
    });
  });
  // Sticky CTA close
  document.querySelectorAll('.sticky-cta-close').forEach(function(c){
    c.addEventListener('click', function(){ c.parentElement.classList.add('hidden'); });
  });
  // Copy buttons
  document.querySelectorAll('.copy-btn').forEach(function(b){
    b.addEventListener('click', function(){
      var t = b.getAttribute('data-copy') || 'MAXBET';
      navigator.clipboard.writeText(t).then(function(){
        b.classList.add('copied'); b.textContent='COPIED \u2713';
        setTimeout(function(){ b.classList.remove('copied'); b.textContent='Copy code'; }, 2000);
      });
    });
  });
  // Reserves big-number live flicker (feel only, no API)
  var bn = document.querySelector('[data-flicker]');
  if (bn) {
    var base = '320,467,5';
    var vals = ['91','73','88','64','79','92'];
    var i = 0;
    setInterval(function(){
      i = (i + 1) % vals.length;
      bn.textContent = '$' + base + vals[i];
    }, 4000);
  }
})();
