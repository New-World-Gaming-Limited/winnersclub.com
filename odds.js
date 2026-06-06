/* Live odds widget — pulls /odds-data.json, refreshed hourly by GitHub Action.
   Every outbound click routes through the WinnersClub affiliate redirect.
   Filters out kickoffs already in the past; warns if the feed itself is stale. */
(function () {
  var w = document.getElementById('odds-widget');
  if (!w) return;
  var endpoint = w.getAttribute('data-endpoint') || '/odds-data.json';
  var poll = parseInt(w.getAttribute('data-poll') || '60000', 10);
  var STALE_MS = 2 * 60 * 60 * 1000; // 2h — flag the feed as stale beyond this
  var AFF = 'https://www.getstake.it/i/Maxbet/io/maxbet/u/e0b1a52c69/uo/newbonus';

  function fmtKick(iso) {
    try {
      var d = new Date(iso);
      var days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      var hh = String(d.getHours()).padStart(2, '0');
      var mm = String(d.getMinutes()).padStart(2, '0');
      return days[d.getDay()] + ' ' + hh + ':' + mm;
    } catch (e) { return iso || ''; }
  }

  function fmtRefreshed(iso) {
    try {
      var d = new Date(iso);
      var mins = Math.max(0, Math.round((Date.now() - d.getTime()) / 60000));
      if (mins < 1) return 'just now';
      if (mins < 60) return mins + ' min ago';
      var hrs = Math.round(mins / 60);
      return hrs + ' hr ago';
    } catch (e) { return iso || 'unknown'; }
  }

  function leagueShort(name) {
    if (!name) return '';
    return name.replace(/^International\s*-\s*/i, '');
  }

  function render(matches, meta) {
    // Drop kickoffs already in the past
    var now = Date.now();
    var live = (matches || []).filter(function (m) {
      var t = m && m.date ? new Date(m.date).getTime() : 0;
      return t && t > now - 5 * 60 * 1000; // 5-min grace for in-play
    });

    if (!live.length) {
      w.innerHTML = '<div class="odds-empty">No upcoming Stake markets in the feed right now. The board refreshes every hour — try again shortly, or tap the button above to open the sportsbook.</div>';
      return;
    }

    var rows = live.map(function (m) {
      return '<tr>' +
        '<td class="oh-match"><strong>' + m.home + '</strong> <span class="vs">vs</span> <strong>' + m.away + '</strong><div class="oh-league">' + leagueShort(m.league) + '</div></td>' +
        '<td class="oh-kick">' + fmtKick(m.date) + '</td>' +
        '<td class="o"><a href="' + AFF + '" target="_blank" rel="noopener" class="o-price">' + (m.home_odds || '-') + '</a></td>' +
        '<td class="o"><a href="' + AFF + '" target="_blank" rel="noopener" class="o-price">' + (m.draw_odds || '-') + '</a></td>' +
        '<td class="o"><a href="' + AFF + '" target="_blank" rel="noopener" class="o-price">' + (m.away_odds || '-') + '</a></td>' +
        '<td class="oh-bet"><a href="' + AFF + '" target="_blank" rel="noopener" class="btn btn-gold-grad">Bet</a></td>' +
        '</tr>';
    }).join('');

    var gen = meta && meta.generated_at ? new Date(meta.generated_at) : null;
    var stale = gen && (Date.now() - gen.getTime()) > STALE_MS;
    var stamp = gen ? fmtRefreshed(meta.generated_at) : 'unknown';
    var staleNote = stale ? ' <span class="odds-stale">(feed stale, refreshing)</span>' : '';

    w.innerHTML =
      '<div class="odds-meta">Stake.com prices, refreshed ' + stamp + staleNote + '. Click any price to take it.</div>' +
      '<div class="odds-scroll"><table class="odds-table">' +
      '<thead><tr><th>Match</th><th>Kick</th><th>1</th><th>X</th><th>2</th><th></th></tr></thead>' +
      '<tbody>' + rows + '</tbody></table></div>' +
      '<div class="odds-foot">Prices via Stake.com (sourced through odds-api.io), refreshed hourly. Use code <span class="code-highlight">MAXBET</span> on signup for the 200% welcome up to $3,000.</div>';
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
