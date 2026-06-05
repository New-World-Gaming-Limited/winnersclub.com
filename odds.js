/* Live odds widget — pulls /odds-data.json (refreshed server-side from odds-api.io)
   Every outbound click routes through the WinnersClub affiliate redirect. */
(function () {
  var w = document.getElementById('odds-widget');
  if (!w) return;
  var endpoint = w.getAttribute('data-endpoint') || '/odds-data.json';
  var poll = parseInt(w.getAttribute('data-poll') || '60000', 10);
  var AFF = 'https://www.getstake.it/i/maxbet/io/maxbet/u/maxbet/uo/maxbet';

  function fmtKick(iso) {
    try {
      var d = new Date(iso);
      var days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      var hh = String(d.getHours()).padStart(2, '0');
      var mm = String(d.getMinutes()).padStart(2, '0');
      return days[d.getDay()] + ' ' + hh + ':' + mm;
    } catch (e) { return iso || ''; }
  }

  function leagueShort(name) {
    if (!name) return '';
    return name.replace(/^International\s*-\s*/i, '').replace(/^[A-Z][a-z]+\s*-\s*/, function (m) { return m; });
  }

  function render(matches, meta) {
    if (!matches || !matches.length) {
      w.innerHTML = '<div class="odds-empty">No fixtures with live Stake prices right now. Tap the button above to open the sportsbook.</div>';
      return;
    }
    var rows = matches.map(function (m) {
      var aff = AFF; // every row routes through the same affiliate URL per club rules
      return '<tr>' +
        '<td class="oh-match"><strong>' + m.home + '</strong> <span class="vs">vs</span> <strong>' + m.away + '</strong><div class="oh-league">' + leagueShort(m.league) + '</div></td>' +
        '<td class="oh-kick">' + fmtKick(m.date) + '</td>' +
        '<td class="o"><a href="' + aff + '" target="_blank" rel="noopener" class="o-price">' + (m.home_odds || '-') + '</a></td>' +
        '<td class="o"><a href="' + aff + '" target="_blank" rel="noopener" class="o-price">' + (m.draw_odds || '-') + '</a></td>' +
        '<td class="o"><a href="' + aff + '" target="_blank" rel="noopener" class="o-price">' + (m.away_odds || '-') + '</a></td>' +
        '<td class="oh-bet"><a href="' + aff + '" target="_blank" rel="noopener" class="btn btn-gold-grad">Bet</a></td>' +
        '</tr>';
    }).join('');
    var stamp = meta && meta.generated_at ? new Date(meta.generated_at).toUTCString() : '';
    w.innerHTML =
      '<div class="odds-meta">Stake.com prices, refreshed ' + stamp + '. Click any price to take it.</div>' +
      '<div class="odds-scroll"><table class="odds-table">' +
      '<thead><tr><th>Match</th><th>Kick</th><th>1</th><th>X</th><th>2</th><th></th></tr></thead>' +
      '<tbody>' + rows + '</tbody></table></div>' +
      '<div class="odds-foot">Prices via Stake.com via odds-api.io. Use code <span class="code-highlight">MAXBET</span> on signup for the 200% welcome up to $3,000.</div>';
  }

  function load() {
    fetch(endpoint, { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var matches = Array.isArray(d) ? d : (d.matches || []);
        render(matches, d);
      })
      .catch(function () {
        w.innerHTML = '<div class="odds-empty">Couldn\'t load the live board. Open Stake.com to see the markets.</div>';
      });
  }
  load();
  setInterval(load, poll);
})();
