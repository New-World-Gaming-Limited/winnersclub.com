"""
Sprint 7: Provider Hub Index page
Builds en/providers/index.html comparing all 8 providers
"""
import os, sys
sys.path.insert(0, '/home/user/workspace/1win-codes-repo')
from build_helpers.page_template import render_page

os.makedirs('en/providers', exist_ok=True)

index_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which is the oldest game provider at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "NetEnt, founded in 1996 in Stockholm, is the oldest game provider in the 1win catalogue. Play'n GO, founded in 1997, is the second oldest. Both are Swedish studios that helped build the European online slot market."
      }
    },
    {
      "@type": "Question",
      "name": "Which provider has the most live casino games at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Evolution Gaming is the dominant live casino provider at 1win, supplying 300+ live dealer tables including Crazy Time, Lightning Roulette, Monopoly Live, Funky Time, and a full range of standard live blackjack, roulette, and baccarat tables."
      }
    },
    {
      "@type": "Question",
      "name": "Which providers use provably fair technology at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Spribe and BGaming both use provably fair systems at 1win. Spribe's Aviator, Mines, Plinko, Hilo, Dice, Goal and Mini Roulette all include round-by-round seed verification. BGaming embeds provably fair verification directly inside the game client for Aviamasters and Plinko XY."
      }
    },
    {
      "@type": "Question",
      "name": "What promo code should I use for any provider at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use promo code XLBONUS when registering at 1win to activate the welcome bonus. The bonus applies across all providers including Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt and Relax Gaming."
      }
    },
    {
      "@type": "Question",
      "name": "Which provider has the highest maximum win potential at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dead or Alive 2 by NetEnt and Money Train 3/4 by Relax Gaming both publish maximum win potentials of 100,000x the bet, the highest of any title in the 1win provider catalogue. Hacksaw Gaming's Wanted Dead or a Wild reaches 50,000x."
      }
    }
  ]
}
</script>
"""

index_main = """
<section class="lede">
  <p>1win holds partnerships with 8 of the most-distributed game studios in regulated iGaming, all operating under a Curaçao 8048/JAZ licence -- register once with promo code <span class="code-highlight">XLBONUS</span> and your account accesses the combined catalogues of Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt, and Relax Gaming.</p>
</section>

<section class="key-facts">
  <h2>All 8 providers at a glance</h2>
  <p>The table below summarises key facts across the 1win provider lineup: founding year, headquarters country, primary regulatory licence, and the titles most associated with each studio.</p>
  <table class="facts-table">
    <thead>
      <tr>
        <th>Provider</th>
        <th>Founded</th>
        <th>HQ country</th>
        <th>Primary licence</th>
        <th>Signature games</th>
        <th>Hub page</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Pragmatic Play</strong></td>
        <td>2015</td>
        <td>Malta</td>
        <td>MGA + UKGC</td>
        <td>Sweet Bonanza, Gates of Olympus, Sugar Rush, Mega Wheel</td>
        <td><a href="/en/providers/pragmatic-play.html">Pragmatic Play hub</a></td>
      </tr>
      <tr>
        <td><strong>Evolution Gaming</strong></td>
        <td>2006</td>
        <td>Sweden (studios: Latvia, Estonia)</td>
        <td>MGA + UKGC</td>
        <td>Crazy Time, Lightning Roulette, Monopoly Live, Funky Time</td>
        <td><a href="/en/providers/evolution-gaming.html">Evolution hub</a></td>
      </tr>
      <tr>
        <td><strong>Spribe</strong></td>
        <td>2018</td>
        <td>Georgia</td>
        <td>MGA</td>
        <td>Aviator, Mines, Plinko, Hilo, Dice, Goal</td>
        <td><a href="/en/providers/spribe.html">Spribe hub</a></td>
      </tr>
      <tr>
        <td><strong>Hacksaw Gaming</strong></td>
        <td>2018</td>
        <td>Malta</td>
        <td>MGA</td>
        <td>Wanted Dead or a Wild, Chaos Crew, Le Bandit, Stockholm Syndrome</td>
        <td><a href="/en/providers/hacksaw-gaming.html">Hacksaw hub</a></td>
      </tr>
      <tr>
        <td><strong>BGaming</strong></td>
        <td>2018</td>
        <td>Estonia</td>
        <td>MGA</td>
        <td>Aviamasters, Plinko XY, Book of Cats, Lucky Lady's Clover</td>
        <td><a href="/en/providers/bgaming.html">BGaming hub</a></td>
      </tr>
      <tr>
        <td><strong>Play'n GO</strong></td>
        <td>1997</td>
        <td>Sweden</td>
        <td>MGA + UKGC + 20+ jurisdictions</td>
        <td>Book of Dead, Reactoonz, Fire Joker, Rise of Olympus, Gemix</td>
        <td><a href="/en/providers/playn-go.html">Play'n GO hub</a></td>
      </tr>
      <tr>
        <td><strong>NetEnt</strong></td>
        <td>1996</td>
        <td>Sweden</td>
        <td>MGA + UKGC + US state licences</td>
        <td>Starburst, Gonzo's Quest, Dead or Alive 2, Mega Fortune, Twin Spin</td>
        <td><a href="/en/providers/netent.html">NetEnt hub</a></td>
      </tr>
      <tr>
        <td><strong>Relax Gaming</strong></td>
        <td>2010</td>
        <td>Malta</td>
        <td>MGA</td>
        <td>Money Train 1/2/3/4, Snake Arena, Hellcatraz, Beast Mode</td>
        <td><a href="/en/providers/relax-gaming.html">Relax Gaming hub</a></td>
      </tr>
    </tbody>
  </table>
</section>

<section class="games">
  <h2>Choosing a provider: what differentiates each studio</h2>

  <h3>For slots with the highest output volume: Pragmatic Play</h3>
  <p>Pragmatic Play releases up to 7 new slot titles per month -- the highest production pace of any studio in this lineup. If you want regular new content, the Pragmatic Play filter in the 1win casino will always have recent releases. The studio's Tumble mechanic (Gates of Olympus, Sweet Bonanza) and 600+ title depth make it the most comprehensive slots provider in the catalogue. MGA + UKGC licences with GLI RNG certification.</p>

  <h3>For live casino game shows: Evolution Gaming</h3>
  <p>Evolution is the only provider here that produces dedicated live casino game shows at scale. Crazy Time, Lightning Roulette, Monopoly Live, and Funky Time are Evolution productions that do not exist at any other studio. If live dealer games are your focus, Evolution's 300+ table library is the anchor of the 1win live casino. Founded 2006, listed on Nasdaq Stockholm, UKGC + MGA licences.</p>

  <h3>For crash games and provably fair play: Spribe or BGaming</h3>
  <p>Spribe (founded 2018, Georgia, MGA) created the Aviator format and remains the market leader in crash games. BGaming (founded 2018, Estonia, MGA) produces Aviamasters as its crash title and embeds provably fair verification directly in the game client. Both studios publish 97% RTP for their flagship crash titles, which is materially higher than the 94%-96.5% range on most slot products.</p>

  <h3>For very high volatility slots: Hacksaw Gaming or Relax Gaming</h3>
  <p>Hacksaw (founded 2018, Malta, MGA) specialises in maximum wins from 10,000x to 50,000x. Wanted Dead or a Wild at 50,000x is the studio's current ceiling. Relax Gaming (founded 2010, Malta, MGA) goes higher: Money Train 3/4 and Dead or Alive 2 both publish 100,000x maximum win potentials. If you are comparing these two for pure upside ceiling, Relax has the edge. If you are comparing for visual design quality and mechanic diversity, both are competitive.</p>

  <h3>For the broadest regulatory approval record: Play'n GO or NetEnt</h3>
  <p>Play'n GO (founded 1997, Sweden) holds licences from over 20 jurisdictions globally -- the widest regulatory footprint of any studio in this list. NetEnt (founded 1996, Sweden, now part of Evolution Group) holds comparable European coverage plus US state gaming board approvals in New Jersey, Pennsylvania, and others. If regulatory transparency and jurisdiction diversity matter to you as a quality signal, these two studios have the longest track records and the most audited RNGs.</p>

  <h3>For crypto-native play: BGaming</h3>
  <p>BGaming was built in the crypto casino ecosystem and its titles are designed for operators accepting Bitcoin and stablecoins. At 1win, USDT and BTC deposits are accepted, and BGaming's in-game provably fair verification works without any additional setup. For players who prioritise on-chain auditability combined with a full slot catalogue (rather than just crash games), BGaming is the strongest option in this lineup.</p>
</section>

<section class="mechanics">
  <h2>Portfolio size comparison</h2>
  <table class="facts-table">
    <thead>
      <tr>
        <th>Provider</th>
        <th>Approx. titles at 1win</th>
        <th>Primary category</th>
        <th>Max win potential</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Pragmatic Play</td>
        <td>600+</td>
        <td>Slots + live casino</td>
        <td>21,100x (Gates of Olympus)</td>
      </tr>
      <tr>
        <td>Evolution Gaming</td>
        <td>300+ live tables</td>
        <td>Live casino + game shows</td>
        <td>Unlimited (live game shows)</td>
      </tr>
      <tr>
        <td>Spribe</td>
        <td>7 titles</td>
        <td>Crash games + instant-win</td>
        <td>Variable (crash format)</td>
      </tr>
      <tr>
        <td>Hacksaw Gaming</td>
        <td>50+</td>
        <td>High-volatility slots</td>
        <td>50,000x</td>
      </tr>
      <tr>
        <td>BGaming</td>
        <td>100+</td>
        <td>Slots + crash + provably fair</td>
        <td>Variable (crash format)</td>
      </tr>
      <tr>
        <td>Play'n GO</td>
        <td>200+</td>
        <td>Slots</td>
        <td>5,000x (Book of Dead)</td>
      </tr>
      <tr>
        <td>NetEnt</td>
        <td>200+ (legacy + new)</td>
        <td>Slots + jackpots</td>
        <td>100,000x (Dead or Alive 2)</td>
      </tr>
      <tr>
        <td>Relax Gaming</td>
        <td>80+</td>
        <td>High-volatility slots</td>
        <td>100,000x (Money Train 3/4)</td>
      </tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to access all providers at 1win with XLBONUS</h2>
  <ol>
    <li>Open registration at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> in the promo code field</li>
    <li>Complete account verification (name, email, date of birth)</li>
    <li>Make a qualifying first deposit to activate the welcome bonus</li>
    <li>In the casino section, use the provider filter to select any studio from the list above</li>
    <li>For live casino, navigate to the Live section and filter by Evolution Gaming</li>
    <li>For crash games, navigate to the Instant Games or Crash section and filter by Spribe or BGaming</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP overview across all 8 providers</h2>
  <p>RTP (Return to Player) is a theoretical figure calculated over millions of game rounds. Published RTPs are the most accurate comparison point between providers, assuming the operator is running the standard configuration. At 1win under Curaçao 8048/JAZ, all providers run their standard published RTPs. The ranges below reflect each studio's main portfolio:</p>
  <ul>
    <li><strong>Pragmatic Play</strong>: 96.00%-96.71% (slots); 88.87%-96.55% (live game shows, per bet type)</li>
    <li><strong>Evolution Gaming</strong>: 95.70%-97.30% (per segment/bet type on live titles)</li>
    <li><strong>Spribe</strong>: 97% (Aviator); variable on mini-games based on player parameters</li>
    <li><strong>Hacksaw Gaming</strong>: 96.33%-96.50%</li>
    <li><strong>BGaming</strong>: 96.00%-96.52% (slots); variable on crash and instant-win titles</li>
    <li><strong>Play'n GO</strong>: 94.00%-96.77%</li>
    <li><strong>NetEnt</strong>: 95.97%-96.92% (standard builds)</li>
    <li><strong>Relax Gaming</strong>: 96.00%-97.04%</li>
  </ul>
  <p>Each provider's hub page contains per-title RTP details and links to the provider's official RTP disclosure documentation.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>Which is the oldest game provider at 1win?</summary>
    <p>NetEnt, founded in 1996 in Stockholm, is the oldest game provider in the 1win catalogue. Play'n GO, founded in 1997, is the second oldest. Both are Swedish studios with over 25 years of regulatory history.</p>
  </details>
  <details>
    <summary>Which provider has the most live casino games at 1win?</summary>
    <p>Evolution Gaming is the dominant live casino provider at 1win, supplying 300+ live dealer tables including Crazy Time, Lightning Roulette, Monopoly Live, Funky Time, and a full range of standard live blackjack, roulette, and baccarat tables.</p>
  </details>
  <details>
    <summary>Which providers use provably fair technology at 1win?</summary>
    <p>Spribe and BGaming both use provably fair systems. Spribe's Aviator, Mines, Plinko, Hilo, Dice, Goal and Mini Roulette include round-by-round seed verification. BGaming embeds provably fair verification inside the game client for Aviamasters and Plinko XY.</p>
  </details>
  <details>
    <summary>What promo code works across all providers at 1win?</summary>
    <p>Use promo code <span class="code-highlight">XLBONUS</span> when registering at 1win. The welcome bonus applies across all 8 providers: Pragmatic Play, Evolution Gaming, Spribe, Hacksaw Gaming, BGaming, Play'n GO, NetEnt, and Relax Gaming.</p>
  </details>
  <details>
    <summary>Which provider has the highest maximum win potential?</summary>
    <p>Dead or Alive 2 by NetEnt and Money Train 3/4 by Relax Gaming both publish maximum win potentials of 100,000x the bet -- the highest of any title in the 1win provider catalogue.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/',
    title='Game providers at 1win: 8 studios compared with XLBONUS',
    description='Compare 8 game providers at 1win: Pragmatic Play, Evolution, Spribe, Hacksaw, BGaming, Play\'n GO, NetEnt and Relax Gaming. Founding year, licences, RTP and top games. Use XLBONUS.',
    h1='Game providers at 1win: compare all 8 studios',
    breadcrumbs=[('Home', '/en/'), ('Providers', None)],
    main_html=index_main,
    extra_schema=index_schema,
)
open('en/providers/index.html', 'w').write(html)
print('Written: en/providers/index.html')
print('Index page complete.')
