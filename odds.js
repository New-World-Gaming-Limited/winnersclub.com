(function(){
  var w = document.getElementById('odds-widget');
  if (!w) return;
  var endpoint = w.getAttribute('data-endpoint');
  var poll = parseInt(w.getAttribute('data-poll') || '30000', 10);
  var stub = [
    {h:'Manchester Utd', a:'Arsenal', league:'EPL', odds:[2.10,3.40,3.20], kick:'Sat 17:30'},
    {h:'Real Madrid', a:'Barcelona', league:'La Liga', odds:[2.55,3.30,2.65], kick:'Sun 21:00'},
    {h:'Bayern', a:'Dortmund', league:'Bundesliga', odds:[1.65,3.90,4.80], kick:'Sat 18:30'},
    {h:'Inter', a:'Juventus', league:'Serie A', odds:[1.95,3.45,3.80], kick:'Sun 20:45'},
    {h:'PSG', a:'Marseille', league:'Ligue 1', odds:[1.55,4.20,5.50], kick:'Sun 21:00'},
    {h:'Liverpool', a:'Chelsea', league:'EPL', odds:[1.85,3.70,4.10], kick:'Sun 16:30'}
  ];
  function render(data){
    var aff='https://www.getstake.it/i/maxbet/io/maxbet/u/maxbet/uo/maxbet';
    w.innerHTML='<table class="odds-table"><thead><tr><th>Match</th><th>League</th><th>Kick</th><th>1</th><th>X</th><th>2</th><th></th></tr></thead><tbody>'+
      data.map(function(m){
        return '<tr><td><strong>'+m.h+'</strong> vs <strong>'+m.a+'</strong></td><td>'+m.league+'</td><td>'+m.kick+'</td>'+
          m.odds.map(function(o){return '<td class="o">'+o.toFixed(2)+'</td>';}).join('')+
          '<td><a href="'+aff+'" target="_blank" rel="noopener" class="btn btn-signup">Bet</a></td></tr>';
      }).join('')+'</tbody></table>';
  }
  function load(){
    if (!endpoint) { render(stub); return; }
    fetch(endpoint).then(function(r){return r.json();}).then(function(d){
      var items = Array.isArray(d) ? d : (d.matches || d.events || stub);
      render(items.length ? items : stub);
    }).catch(function(){ render(stub); });
  }
  load();
  if (endpoint) setInterval(load, poll);
})();
