"""
Sprint 7: Provider Hub Pages generator
Builds 8 provider pages + index in en/providers/
"""
import os, sys
sys.path.insert(0, '/home/user/workspace/1win-codes-repo')
from build_helpers.page_template import render_page

os.makedirs('en/providers', exist_ok=True)

# ─────────────────────────────────────────────
# 1. PRAGMATIC PLAY
# ─────────────────────────────────────────────

pp_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Pragmatic Play",
  "foundingDate": "2015",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "MT",
    "addressLocality": "Sliema"
  },
  "url": "https://www.pragmaticplay.com/",
  "description": "Pragmatic Play is a leading multi-product content provider to the iGaming industry, founded in 2015 and headquartered in Malta.",
  "sameAs": ["https://www.pragmaticplay.com/"]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When was Pragmatic Play founded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pragmatic Play was founded in 2015 and is headquartered in Sliema, Malta. The studio holds licenses from the Malta Gaming Authority (MGA), UK Gambling Commission (UKGC), and Gibraltar Regulatory Authority."
      }
    },
    {
      "@type": "Question",
      "name": "What is the RTP of Sweet Bonanza?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sweet Bonanza has a published RTP of 96.51% in its standard configuration. Some casinos use an alternative 96.48% or lower RTP version, so always check the in-game paytable before playing."
      }
    },
    {
      "@type": "Question",
      "name": "Does Pragmatic Play have live casino games?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Pragmatic Play runs a dedicated live casino studio producing game-show titles like Mega Wheel and Sweet Bonanza Candyland alongside standard live blackjack, roulette and baccarat tables."
      }
    },
    {
      "@type": "Question",
      "name": "What promo code unlocks the 1win welcome bonus for Pragmatic Play slots?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use promo code XLBONUS when registering at 1win to activate the welcome bonus applicable across Pragmatic Play's slot portfolio."
      }
    },
    {
      "@type": "Question",
      "name": "What certifications does Pragmatic Play hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pragmatic Play titles are certified by Gaming Laboratories International (GLI) and hold approvals from MGA Malta, UKGC, Gibraltar, Romania ONJN, and several other jurisdictions, making them among the most widely licensed products in regulated markets."
      }
    }
  ]
}
</script>
"""

pp_main = """
<section class="lede">
  <p>1win hosts over 600 Pragmatic Play titles under a Curaçao 8048/JAZ licence, and new players who register with promo code <span class="code-highlight">XLBONUS</span> unlock a welcome package that covers the studio's full slot and live casino catalogue.</p>
</section>

<section class="key-facts">
  <h2>About Pragmatic Play</h2>
  <p>Pragmatic Play launched in 2015 with offices in Sliema, Malta. Within a decade it grew from a startup into one of the highest-output studios in the industry, releasing up to seven new slot titles per month. The company holds a primary licence from the Malta Gaming Authority (MGA/B2B/187/2010), a production licence from the UK Gambling Commission (UKGC), and additional approvals across Romania, Gibraltar, and the Bahamas. GLI (Gaming Laboratories International) certifies its RNG independently.</p>
  <p>The studio produces slots, live casino, bingo, scratch cards, and virtual sports from a single API integration. In terms of market position, Pragmatic Play competes directly with NetEnt and Play'n GO for shelf space in regulated European markets while also holding strong distribution across Latam and emerging markets where 1win is active. Its live casino arm, launched in 2019, streams from studios in Romania and the Philippines.</p>
  <p>The Tumble mechanic (also called Cascading Reels) is the studio's signature engine: winning symbols are removed and replaced by new ones in a single spin, allowing consecutive wins from one bet. This mechanic drives the high-volatility profile of its flagship titles and is what distinguishes Pragmatic Play's math models from more conservative competitors.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>2015</td></tr>
    <tr><th>Headquarters</th><td>Sliema, Malta</td></tr>
    <tr><th>Primary licence</th><td>MGA Malta (B2B)</td></tr>
    <tr><th>Additional licences</th><td>UKGC, Gibraltar, Romania ONJN</td></tr>
    <tr><th>RNG certification</th><td>GLI (Gaming Laboratories International)</td></tr>
    <tr><th>Monthly release pace</th><td>Up to 7 new slots per month</td></tr>
    <tr><th>Portfolio size</th><td>600+ slots, live tables, scratch cards</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature Pragmatic Play games at 1win</h2>
  <p>The games below are among the most-played Pragmatic Play titles at 1win. RTPs shown are the standard configurations published by Pragmatic Play.</p>
  <ul>
    <li><strong>Sweet Bonanza</strong> (96.51% RTP, high volatility) -- The studio's most recognised slot. A 6x5 grid with a Tumble mechanic, Ante Bet option, and free spins triggered by scatter symbols. Multiplier bombs during free rounds can scale payouts significantly. Available at <a href="/en/slots/sweet-bonanza.html">1win Sweet Bonanza</a>.</li>
    <li><strong>Gates of Olympus</strong> (96.50% RTP, high volatility) -- Zeus-themed, 6x5 Tumble grid. Multipliers land anywhere on the grid during free spins. The "Buy Feature" option lets players access the bonus round directly at 100x bet. Linked at <a href="/en/slots/gates-of-olympus.html">1win Gates of Olympus</a>.</li>
    <li><strong>Sugar Rush</strong> (96.52% RTP, high volatility) -- Candy-grid layout (7x7) with cluster pays. Sugar multipliers accumulate and are added together before the free spins payouts, producing outsized variance. One of the studio's fastest-growing titles post-2022.</li>
    <li><strong>Big Bass Bonanza</strong> (96.71% RTP, medium-high volatility) -- Fishing theme, five-reel. The angler wild collects fish symbols worth coin values. Free spins with retrigger potential. A franchise that now spans six sequels.</li>
    <li><strong>Wolf Gold</strong> (96.01% RTP, medium volatility) -- Three progressive jackpots (Mini, Minor, Major). Moon symbols trigger Money Respin feature. One of Pragmatic Play's EGR award winners. Lower variance than the Tumble titles, suitable for longer sessions.</li>
    <li><strong>The Dog House</strong> (96.51% RTP, high volatility) -- Sticky wilds with multipliers in free spins. A 5x3 grid with 20 paylines. The Dog House Megaways sequel expands the grid to 117,649 ways.</li>
    <li><strong>Fruit Party</strong> (96.47% RTP, high volatility) -- 7x7 cluster-pays with a Tumble mechanic. Multiplier symbols persist across tumbles. Simpler visual theme than Olympus but comparable math model.</li>
    <li><strong>Buffalo King Megaways</strong> (96.52% RTP, high volatility) -- North American wildlife theme, up to 200,704 ways to win via BTG's Megaways licence. Free spins with unlimited progressive multiplier. Retrigger cap removed in some markets.</li>
    <li><strong>Mega Wheel (Live)</strong> -- A game-show live title: a spin wheel with 54 segments (1x to 500x) plus mystery multipliers that re-spin when activated. RTP ranges from 88.87% to 96.55% depending on which number you bet.</li>
    <li><strong>Sweet Bonanza Candyland (Live)</strong> -- Live adaptation of the slot. A physical candy-themed wheel with four bonus games (Pachinko, Bonus Spin, Free Spins, Super Game). Live RTP is around 95.51%.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics Pragmatic Play is known for</h2>
  <p>The Tumble feature (Cascading Reels) is present in most of the studio's high-volatility titles. When a winning combination lands, those symbols are removed and new ones fall from above -- repeating until no winning combination appears. This creates multi-win chains from a single bet, which is why titles like Gates of Olympus can produce four-figure multipliers from base bets during a single free spins round.</p>
  <p>Multiplier bombs are a related mechanic appearing in Sweet Bonanza, Olympus, and others. During free spins, random multiplier symbols land on the grid and their values sum together (rather than multiply with each other). A round that lands 2x + 5x + 10x will apply a 17x multiplier to that tumble's win -- an additive model that keeps peak payouts in the 5,000x-21,100x range.</p>
  <p>The Buy Feature (Ante Bet) option appears on most titles and allows players to pay 100x their bet to directly purchase a free spins round. This is disabled in the UK market due to UKGC regulations but active at 1win under Curaçao 8048/JAZ rules.</p>
  <p>Pragmatic Play also licences the Megaways mechanic from Big Time Gaming (BTG) for titles like Buffalo King Megaways and Gorilla Mayhem Megaways, adding dynamic reel modifiers that vary the number of symbols per reel each spin -- producing up to 200,704 combinations in a single spin.</p>
</section>

<section class="how-to">
  <h2>How to play Pragmatic Play games at 1win with XLBONUS</h2>
  <ol>
    <li>Open the registration page at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> in the promo code field during sign-up</li>
    <li>Complete account verification (name, email, date of birth)</li>
    <li>Make a qualifying deposit -- the welcome bonus applies to your first deposit</li>
    <li>Navigate to Casino, filter by provider "Pragmatic Play", and select your title</li>
    <li>Bonus funds and free spins (if included in the current promotion) appear in your account balance automatically</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>Pragmatic Play publishes default RTP values for every title in its official game library. The standard range across the slot portfolio runs from 96.00% to 96.71%. Some titles have an alternative lower-RTP configuration (typically around 94.00%) that operators can activate -- 1win operates the standard RTP settings. Always verify the active RTP by opening the game's paytable before wagering.</p>
  <p>Live casino titles (Mega Wheel, Sweet Bonanza Candyland) operate at lower and variable RTPs depending on your bet selection -- the per-number RTP on Mega Wheel ranges from 88.87% to 96.55%. This is standard for game-show formats where higher multiplier bets carry a higher house edge.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>When was Pragmatic Play founded?</summary>
    <p>Pragmatic Play was founded in 2015 and is headquartered in Sliema, Malta. The studio holds licences from the MGA, UKGC, and Gibraltar Regulatory Authority.</p>
  </details>
  <details>
    <summary>What is the RTP of Sweet Bonanza?</summary>
    <p>Sweet Bonanza has a published RTP of 96.51% in its standard configuration. Some operators use an alternative 96.48% or lower RTP build, so check the in-game paytable before playing.</p>
  </details>
  <details>
    <summary>Does Pragmatic Play have live casino games?</summary>
    <p>Yes. Pragmatic Play runs a dedicated live casino studio producing game-show titles like Mega Wheel and Sweet Bonanza Candyland alongside standard live blackjack, roulette and baccarat tables.</p>
  </details>
  <details>
    <summary>What promo code activates the 1win bonus for Pragmatic Play slots?</summary>
    <p>Use promo code <span class="code-highlight">XLBONUS</span> when registering at 1win to activate the welcome bonus applicable across the Pragmatic Play catalogue.</p>
  </details>
  <details>
    <summary>What certifications does Pragmatic Play hold?</summary>
    <p>Pragmatic Play titles are certified by GLI (Gaming Laboratories International) and hold regulatory approvals from MGA Malta, UKGC, Gibraltar, Romania ONJN, and several other jurisdictions.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/pragmatic-play',
    title='Pragmatic Play slots at 1win: top games and XLBONUS',
    description='Play 600+ Pragmatic Play slots and live casino games at 1win with promo code XLBONUS. Sweet Bonanza, Gates of Olympus, Mega Wheel and more under Curacao 8048/JAZ licence.',
    h1='Pragmatic Play slots at 1win',
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('Pragmatic Play', None)],
    main_html=pp_main,
    extra_schema=pp_schema,
)
open('en/providers/pragmatic-play.html', 'w').write(html)
print('Written: pragmatic-play.html')


# ─────────────────────────────────────────────
# 2. EVOLUTION GAMING
# ─────────────────────────────────────────────

evo_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Evolution Gaming",
  "foundingDate": "2006",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "SE",
    "addressLocality": "Stockholm"
  },
  "url": "https://www.evolution.com/",
  "description": "Evolution Gaming is the world's largest live casino provider, founded in 2006 in Stockholm, Sweden. It operates studios in Riga, Tallinn, Malta, Vancouver, New Jersey, and Georgia."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When was Evolution Gaming founded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Evolution Gaming was founded in 2006 in Stockholm, Sweden. Its primary production studios are based in Riga, Latvia, and Tallinn, Estonia. It is listed on Nasdaq Stockholm."
      }
    },
    {
      "@type": "Question",
      "name": "What is the RTP of Crazy Time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Crazy Time has a theoretical RTP of 96.08% when betting on the 1 segment. RTP varies per segment: the 2 segment returns 95.95%, the 5 returns 95.76%, the 10 returns 95.70%, and the four bonus game slots vary based on sub-game outcomes."
      }
    },
    {
      "@type": "Question",
      "name": "Does Evolution hold a UKGC licence?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Evolution holds a B2B licence from the UK Gambling Commission, along with licences from the Malta Gaming Authority, the Swedish Spelinspektionen, the Romanian ONJN, and multiple US state gaming boards."
      }
    },
    {
      "@type": "Question",
      "name": "How do I access Evolution live tables at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Register at 1win with promo code XLBONUS, navigate to the Live Casino section, and filter by provider Evolution to access Crazy Time, Lightning Roulette, Monopoly Live, and the full live table catalogue."
      }
    },
    {
      "@type": "Question",
      "name": "What makes Lightning Roulette different from standard live roulette?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lightning Roulette adds a RNG layer to standard European roulette: before each spin, 1 to 5 lucky numbers are struck by lightning and assigned multipliers of 50x, 100x, 200x, 300x, 400x, or 500x. Straight-up bets on a lucky number pay the multiplied amount if it wins."
      }
    }
  ]
}
</script>
"""

evo_main = """
<section class="lede">
  <p>1win brings the full Evolution Gaming live casino catalogue to players in 100+ countries under a Curaçao 8048/JAZ licence -- register with promo code <span class="code-highlight">XLBONUS</span> and access 300+ live dealer tables including Crazy Time, Lightning Roulette, and Funky Time from day one.</p>
</section>

<section class="key-facts">
  <h2>About Evolution Gaming</h2>
  <p>Evolution Gaming was incorporated in 2006 in Stockholm, Sweden by Fredrik Osterberg, Jens von Bahr, and Richard Hadida. The company's operational studios are anchored in Riga, Latvia, and Tallinn, Estonia -- cities chosen for their technical talent pools and regulatory proximity to EU markets. By 2020, Evolution had acquired NetEnt, Red Tiger, and later Nolimit City, consolidating it as the dominant supplier of both live casino and RNG slots to European-licensed operators.</p>
  <p>Regulation is a genuine differentiator here. Evolution holds B2B licences from the UK Gambling Commission (UKGC account number 39439), the Malta Gaming Authority (MGA/B2B/187/2010), the Swedish Spelinspektionen, Romanian ONJN, and seven US state gaming boards (New Jersey, Pennsylvania, Michigan, Connecticut, West Virginia, Delaware, and Rhode Island). Independent testing is conducted by BMM Testlabs and Technical Systems Testing (TST). In regulated markets like the UK, Evolution's live tables are among the few that operators can legally offer.</p>
  <p>The company is listed on Nasdaq Stockholm (ticker: EVO) and reported revenues of EUR 1.98 billion in 2023 -- making it by far the largest dedicated live casino provider. At 1win, Evolution tables operate under Curaçao licence rules, meaning the full game-show portfolio (including titles restricted in some European jurisdictions) is accessible.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>2006</td></tr>
    <tr><th>Headquarters</th><td>Stockholm, Sweden (studios: Riga, Tallinn, Malta)</td></tr>
    <tr><th>Listed</th><td>Nasdaq Stockholm (EVO)</td></tr>
    <tr><th>Primary licence</th><td>MGA Malta (B2B) + UKGC</td></tr>
    <tr><th>US presence</th><td>7 state gaming board approvals</td></tr>
    <tr><th>Acquisitions</th><td>NetEnt (2020), Red Tiger (2020), Nolimit City (2022)</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature Evolution games at 1win</h2>
  <p>Evolution's game-show titles are the primary draw. These are live productions combining a physical studio set, a human presenter, and an RNG layer that triggers bonus multipliers or bonus game rounds mid-show.</p>
  <ul>
    <li><strong>Crazy Time</strong> (RTP up to 96.08%) -- A large 64-segment money wheel with four bonus games: Cash Hunt, Pachinko, Coin Flip, and Crazy Time. The top multiplier in the Crazy Time bonus game has reached 20,000x in live production. Segments are distributed as: 1 (21 slots), 2 (13 slots), 5 (7 slots), 10 (4 slots), plus the four bonus game slots.</li>
    <li><strong>Lightning Roulette</strong> (RTP 97.30% for even money bets) -- European roulette with a pre-spin RNG lightning phase that strikes 1-5 numbers and applies 50x-500x multipliers. A 3x fee is embedded in straight-up bets (base 29:1 vs standard 35:1) to fund the multiplier pool.</li>
    <li><strong>Monopoly Live</strong> (RTP up to 96.23%) -- Money wheel with a Monopoly 3D bonus round. Mr Monopoly traverses a digital board collecting multipliers and free parking bonuses. One of Evolution's best-selling titles since its 2019 launch.</li>
    <li><strong>Crazy Coin Flip</strong> -- A faster game-show format: a coin flip with random multipliers (up to 200x) assigned to heads or tails before the flip. Lower production overhead than Crazy Time, targeting high-frequency bettors.</li>
    <li><strong>Funky Time</strong> -- A 64-segment wheel with five bonus games (Bar, Disco, Stayin Alive, VIP Disco, and a Top of the Pops round). The studio aesthetic is 1970s disco. Released 2023, one of Evolution's highest-profile launches of that year.</li>
    <li><strong>Lightning Storm</strong> -- An accelerated live roulette variant with 1-9 lucky numbers per spin and multipliers from 50x to 2,000x. Faster spin interval than Lightning Roulette, designed for mobile-first play sessions.</li>
    <li><strong>Immersive Roulette</strong> -- Multi-camera HD European roulette with slow-motion ball tracking replays. No RNG overlay; pure live roulette with 97.30% RTP.</li>
    <li><strong>Speed Baccarat</strong> -- Cards dealt in under 27 seconds per round, targeting experienced baccarat players who want a faster pace. Standard 98.94% banker RTP.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics Evolution is known for</h2>
  <p>Evolution's technical signature is the RNG-meets-live hybrid: a physical studio element (wheel, coin, card shoe) combined with a real-time RNG module that activates multipliers before the physical outcome is determined. The sequence matters -- the multiplier is assigned by RNG before the wheel spins, so the physical outcome determines which bets win at that multiplier, not the other way around.</p>
  <p>Lightning Roulette's lightning phase runs in parallel with the live croupier preparing to spin. When lightning strikes number 7 at 200x and number 7 then lands, all straight-up bets on 7 pay 200x (minus the 3x compression embedded in the base payout). This dual-track architecture is what allows Evolution to deliver multiplier-driven variance within a live regulated format.</p>
  <p>The Crazy Time top-level bonus game uses a physical giant wheel operated by a presenter in a dedicated studio room, with an RNG flapper that lands on a multiplier segment visible in the camera feed. The physical production removes any ambiguity about the RNG outcome -- the flapper position is verifiable by any viewer watching the live stream. This is Evolution's answer to provably fair: physical transparency rather than cryptographic verification.</p>
  <p>Evolution also holds several patents related to its live studio broadcast technology, multi-seat table management, and the RNG-integration architecture used in Lightning products.</p>
</section>

<section class="how-to">
  <h2>How to play Evolution games at 1win with XLBONUS</h2>
  <ol>
    <li>Open registration at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> in the promo field</li>
    <li>Verify your account with name, email and date of birth</li>
    <li>Deposit and receive your welcome bonus</li>
    <li>Navigate to Live Casino and filter by Evolution to access all game-show and table titles</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>Evolution publishes per-bet-type RTP for every game. Standard live roulette (European single-zero) pays 97.30% on even-money bets. Crazy Time's RTP ranges from 95.70% (10 segment) to 96.08% (1 segment). Monopoly Live runs 96.23% on the 1 bet. Game-show titles with multiplier bonus rounds have variable RTPs because the bonus game payout distribution changes the overall theoretical return. The published RTPs assume infinite play and include the bonus game contributions.</p>
  <p>1win operates Evolution tables at the standard published RTP configurations. There is no operator-adjustable RTP on live casino games -- the live studio production is shared infrastructure, and table parameters are set globally by Evolution.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>When was Evolution Gaming founded?</summary>
    <p>Evolution Gaming was founded in 2006 in Stockholm, Sweden. Its primary production studios are in Riga, Latvia, and Tallinn, Estonia. It is listed on Nasdaq Stockholm (ticker: EVO).</p>
  </details>
  <details>
    <summary>What is the RTP of Crazy Time?</summary>
    <p>Crazy Time has a theoretical RTP of 96.08% when betting on the 1 segment. RTP varies by segment: the 10 segment returns 95.70%, and bonus game slots vary based on sub-game outcomes.</p>
  </details>
  <details>
    <summary>Does Evolution hold a UKGC licence?</summary>
    <p>Yes. Evolution holds a B2B licence from the UK Gambling Commission, along with MGA Malta, Swedish Spelinspektionen, Romanian ONJN, and multiple US state gaming board approvals.</p>
  </details>
  <details>
    <summary>How do I access Evolution live tables at 1win?</summary>
    <p>Register at 1win with promo code <span class="code-highlight">XLBONUS</span>, navigate to the Live Casino section, and filter by provider Evolution to access the full catalogue.</p>
  </details>
  <details>
    <summary>What makes Lightning Roulette different from standard live roulette?</summary>
    <p>Lightning Roulette adds a RNG phase before each spin: 1 to 5 lucky numbers are struck by lightning and assigned multipliers of 50x to 500x. Straight-up bets on a lightning number pay the multiplied amount if it wins.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/evolution-gaming',
    title='Evolution Gaming live casino at 1win with XLBONUS',
    description='Play 300+ Evolution Gaming live dealer tables at 1win. Crazy Time, Lightning Roulette, Monopoly Live and more. Register with promo code XLBONUS under Curacao 8048/JAZ licence.',
    h1='Evolution Gaming live casino at 1win',
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('Evolution Gaming', None)],
    main_html=evo_main,
    extra_schema=evo_schema,
)
open('en/providers/evolution-gaming.html', 'w').write(html)
print('Written: evolution-gaming.html')


# ─────────────────────────────────────────────
# 3. SPRIBE
# ─────────────────────────────────────────────

spribe_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Spribe",
  "foundingDate": "2018",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "GE",
    "addressLocality": "Tbilisi"
  },
  "url": "https://spribe.co/",
  "description": "Spribe is a Georgian iGaming developer founded in 2018, best known for creating Aviator, the crash game format that became one of the most-played casino titles globally."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who created Aviator?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Aviator was created by Spribe, a game development company founded in 2018 and headquartered in Tbilisi, Georgia. The game uses a provably fair algorithm based on client seed, server seed, and nonce, allowing players to verify each round's outcome."
      }
    },
    {
      "@type": "Question",
      "name": "What is the RTP of Spribe Aviator?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Aviator has a published RTP of 97%. This is higher than most slot games and reflects the crash game format where the house edge is embedded in the multiplier distribution rather than symbol combinations."
      }
    },
    {
      "@type": "Question",
      "name": "Is Spribe provably fair?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Spribe's crash and mini-game titles use a provably fair system. Each round's outcome is generated from a combination of a server seed (hashed before the round begins) and a client seed. Players can verify the fairness of any round after it concludes using the seed data disclosed post-game."
      }
    },
    {
      "@type": "Question",
      "name": "What licence does Spribe hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Spribe holds a B2B gaming licence from the Malta Gaming Authority (MGA). Aviator and its other titles are also approved and distributed under the Curacao 8048/JAZ framework used by operators like 1win."
      }
    },
    {
      "@type": "Question",
      "name": "What promo code should I use for Spribe games at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use promo code XLBONUS when registering at 1win. The welcome bonus applies to your account balance and can be wagered on Spribe's Aviator and mini-game titles."
      }
    }
  ]
}
</script>
"""

spribe_main = """
<section class="lede">
  <p>1win partners with Spribe to deliver Aviator and 6 additional crash and instant-win titles to 400,000+ registered players under a Curaçao 8048/JAZ licence -- use promo code <span class="code-highlight">XLBONUS</span> at registration to start with a bonus on your first deposit.</p>
</section>

<section class="key-facts">
  <h2>About Spribe</h2>
  <p>Spribe was founded in 2018 in Tbilisi, Georgia. The company built its reputation on a single title -- Aviator -- that launched in 2019 and became one of the fastest-adopted casino formats in iGaming history. By 2022, Aviator was active at over 2,000 operators globally and had generated over EUR 100 million in operator GGR annually according to industry tracking data.</p>
  <p>The studio holds a B2B gaming licence from the Malta Gaming Authority and has received additional approvals across Romania, Greece, and several African regulatory frameworks. Spribe's competitive advantage is provably fair technology: each game round's outcome is generated from a cryptographic seed system that players can audit after the fact, providing a level of transparency that standard RNG certificates from GLI or BMM do not offer.</p>
  <p>Beyond Aviator, Spribe produces a catalogue of mini-games targeting the instant-win segment. These titles (Mines, Plinko, Hilo, Dice, Goal, Mini Roulette) share the provably fair architecture and are designed for short-session, high-frequency play. The overall portfolio positions Spribe as the dominant supplier in the crash game and provably fair instant-win category.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>2018</td></tr>
    <tr><th>Headquarters</th><td>Tbilisi, Georgia</td></tr>
    <tr><th>Primary licence</th><td>MGA Malta (B2B)</td></tr>
    <tr><th>Key differentiator</th><td>Provably fair crash games</td></tr>
    <tr><th>Flagship title</th><td>Aviator (launched 2019)</td></tr>
    <tr><th>Operator count</th><td>2,000+ globally (Aviator)</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature Spribe games at 1win</h2>
  <ul>
    <li><strong>Aviator</strong> (97% RTP) -- The crash game that redefined a category. A plane takes off and a multiplier climbs from 1.00x. Players must cash out before the plane flies away -- if they do not, the bet is lost. Every round uses a provably fair algorithm; the crash point is predetermined by the cryptographic seed and cannot be altered after bets are placed. Two simultaneous bets are allowed per player. At 1win, Aviator is accessible via the dedicated <a href="/en/aviator.html">Aviator page</a>.</li>
    <li><strong>Mines</strong> -- A grid-based instant-win game. Players select cells on a 5x5 grid; some contain gems (wins), some contain mines (game over). The more cells you reveal safely, the higher the multiplier. Players set their own mine count (1-24), determining the risk-reward ratio. RTP adjusts dynamically based on mine count and cells revealed.</li>
    <li><strong>Plinko</strong> -- A ball-drop game. A ball is released from the top of a pegged pyramid and falls into one of several multiplier buckets at the bottom. Players select ball size (risk level), which changes the multiplier distribution. Higher risk concentrates larger multipliers at the edges with a low-payout center, and vice versa.</li>
    <li><strong>Hilo</strong> -- A card guessing game. A card is revealed; the player predicts whether the next card will be higher or lower. Correct predictions build a multiplier; the player can cash out at any point or press their luck for another card. A skip option is available for neutral cards.</li>
    <li><strong>Dice</strong> -- A simple under/over dice roll. Players set a target number and bet on the roll being above or below it. The probability and payout adjust automatically. A clean, fast-cycle provably fair title suitable for high-volume sessions.</li>
    <li><strong>Goal</strong> -- A penalty shootout format. Players choose a side (left, center, right) for each shot. Successful kicks accumulate a multiplier; three misses end the round. Designed around football themes, popular in markets where football betting is culturally dominant.</li>
    <li><strong>Mini Roulette</strong> -- A 13-number single-zero roulette wheel (0-12). Standard inside and outside bets are available at adjusted odds. The smaller wheel increases the frequency of hitting specific numbers compared to European roulette's 37-number layout.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics Spribe is known for</h2>
  <p>Provably fair is the defining mechanic across Spribe's catalogue. Each game round generates its outcome from three inputs: a server seed (hashed and committed before the round), a client seed (provided by the player or browser), and a nonce (round counter). After the round ends, Spribe discloses the server seed so players can hash the three values together and verify the crash point or game outcome themselves. This is a materially higher level of auditability than GLI certification alone provides.</p>
  <p>In Aviator specifically, the crash point multiplier is generated by the combined seed before any bets are placed. This means the operator (1win) and Spribe cannot change the crash point after players have committed funds -- the sequence of seed commitment, betting, and then crash execution is the trust mechanism. Players who want to verify any historical Aviator round can use Spribe's public verification tool at spribe.co with the round's seed data.</p>
  <p>The auto-cashout feature in Aviator is frequently used by players who want to remove reaction-time variance. Setting auto-cashout at, say, 1.50x locks in a cash-out if the multiplier reaches that point, regardless of whether the player is watching. Two simultaneous auto-cashout bets at different multiplier thresholds is a common strategy for managing risk across a session.</p>
</section>

<section class="how-to">
  <h2>How to play Spribe games at 1win with XLBONUS</h2>
  <ol>
    <li>Register at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter <span class="code-highlight">XLBONUS</span> in the promo code field</li>
    <li>Complete verification and make a qualifying deposit</li>
    <li>Find Aviator from the homepage quick links or search "Spribe" in the casino game finder</li>
    <li>For Mines, Plinko, Hilo, Dice, Goal and Mini Roulette: navigate to Instant Games or search by provider Spribe</li>
    <li>Use auto-cashout in Aviator to set your target multiplier before each round begins</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>Aviator publishes a 97% RTP, which is unusually high for a casino game and reflects the crash game's low house edge model. Mines, Plinko, Hilo, Dice, Goal, and Mini Roulette each have RTPs that vary dynamically based on the player's chosen risk parameters. Dice, for example, approaches 99% RTP at neutral settings because the margin is built purely into the payout odds on the selected number range. Spribe provides mathematical model sheets to licensed operators; 1win's Curaçao licence requires RTP disclosure on request.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>Who created Aviator?</summary>
    <p>Aviator was created by Spribe, founded in 2018 in Tbilisi, Georgia. The game uses a provably fair algorithm based on client seed, server seed, and nonce, so players can verify each round's outcome independently.</p>
  </details>
  <details>
    <summary>What is the RTP of Spribe Aviator?</summary>
    <p>Aviator has a published RTP of 97%, higher than most slot games. The house edge is embedded in the crash multiplier distribution rather than symbol combinations.</p>
  </details>
  <details>
    <summary>Is Spribe provably fair?</summary>
    <p>Yes. All Spribe titles use a provably fair system. Each round's outcome is generated from a server seed (hashed before the round) and a client seed. Players can verify any round after it concludes using the disclosed seed data.</p>
  </details>
  <details>
    <summary>What licence does Spribe hold?</summary>
    <p>Spribe holds a B2B gaming licence from the Malta Gaming Authority (MGA). Its titles are also distributed under the Curacao 8048/JAZ framework used by operators like 1win.</p>
  </details>
  <details>
    <summary>What promo code should I use for Spribe games at 1win?</summary>
    <p>Use promo code <span class="code-highlight">XLBONUS</span> when registering at 1win to activate the welcome bonus applicable across all Spribe titles.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/spribe',
    title='Spribe Aviator and crash games at 1win with XLBONUS',
    description='Play Spribe Aviator, Mines, Plinko, Hilo and more at 1win. Provably fair crash games with 97% RTP. Register with promo code XLBONUS under Curacao 8048/JAZ licence.',
    h1='Spribe games at 1win: Aviator and instant-win titles',
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('Spribe', None)],
    main_html=spribe_main,
    extra_schema=spribe_schema,
)
open('en/providers/spribe.html', 'w').write(html)
print('Written: spribe.html')


# ─────────────────────────────────────────────
# 4. HACKSAW GAMING
# ─────────────────────────────────────────────

hacksaw_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Hacksaw Gaming",
  "foundingDate": "2018",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "MT",
    "addressLocality": "Sliema"
  },
  "url": "https://hacksawgaming.com/",
  "description": "Hacksaw Gaming is a Malta-based iGaming studio founded in 2018, producing high-volatility slots known for distinctive visual art direction and maximum win potentials above 50,000x."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When was Hacksaw Gaming founded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hacksaw Gaming was founded in 2018 in Sliema, Malta. The studio initially focused on scratch cards before pivoting to video slots, which now make up the majority of its catalogue."
      }
    },
    {
      "@type": "Question",
      "name": "What is the maximum win in Wanted Dead or a Wild?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wanted Dead or a Wild has a maximum win potential of 50,000x the bet. It is a high-volatility title with sticky wilds and a free spins feature that can extend through retriggering."
      }
    },
    {
      "@type": "Question",
      "name": "What licences does Hacksaw Gaming hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hacksaw Gaming holds a B2B licence from the Malta Gaming Authority (MGA). Its titles are also distributed under operator licences including Curacao 8048/JAZ, making them available at 1win."
      }
    },
    {
      "@type": "Question",
      "name": "Are Hacksaw slots high volatility?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most Hacksaw Gaming slots are rated high or very high volatility. The studio specifically targets the high-variance market with maximum win potentials typically ranging from 10,000x to 50,000x and free spins mechanics that rely on sticky wilds to build payouts."
      }
    },
    {
      "@type": "Question",
      "name": "How do I claim a bonus for Hacksaw games at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Register at 1win.codes with promo code XLBONUS. The welcome bonus applies to your account balance and can be used across all Hacksaw Gaming titles available in the 1win casino catalogue."
      }
    }
  ]
}
</script>
"""

hacksaw_main = """
<section class="lede">
  <p>1win carries the full Hacksaw Gaming portfolio under a Curaçao 8048/JAZ licence, including Wanted Dead or a Wild, Chaos Crew, and Le Bandit -- use promo code <span class="code-highlight">XLBONUS</span> at registration to activate a welcome bonus across all 50+ Hacksaw titles.</p>
</section>

<section class="key-facts">
  <h2>About Hacksaw Gaming</h2>
  <p>Hacksaw Gaming was founded in 2018 in Sliema, Malta. The studio launched initially as a scratch card developer before transitioning to video slots, which now represent the majority of its commercial output. The pivot proved strategically sound: Hacksaw's video slots quickly built a reputation for distinctive visual design and extreme volatility configurations, attracting attention from affiliate publishers and streamers who favoured high-variance content.</p>
  <p>The studio holds a primary B2B licence from the Malta Gaming Authority. Its titles pass GLI and BMM certification for RNG integrity. In 2023, Hacksaw Gaming won the EGR B2B Award for Slot Provider of the Year -- a notable achievement for a studio that had only been producing video slots for approximately four years at that point.</p>
  <p>Hacksaw's market position is that of a high-volatility specialist. The studio does not compete across all variance tiers: its slot catalogue skews strongly toward maximum win potentials of 10,000x to 50,000x, buy-feature mechanics, and free spin rounds built around sticky wild accumulation. This focus makes it a preferred choice for players who want the highest possible upside per session at the cost of longer dry runs between significant wins.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>2018</td></tr>
    <tr><th>Headquarters</th><td>Sliema, Malta</td></tr>
    <tr><th>Primary licence</th><td>MGA Malta (B2B)</td></tr>
    <tr><th>Speciality</th><td>High-volatility video slots</td></tr>
    <tr><th>EGR Award</th><td>Slot Provider of the Year 2023</td></tr>
    <tr><th>Max win range</th><td>10,000x to 50,000x bet</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature Hacksaw games at 1win</h2>
  <ul>
    <li><strong>Wanted Dead or a Wild</strong> (96.38% RTP, very high volatility, max win 50,000x) -- A western-theme slot with a 5x4 grid and 40 paylines. Sticky wilds land and hold during the free spins feature; the more sticky wilds on the grid, the higher the potential payout. The maximum win of 50,000x places it among the highest-ceiling titles in the Hacksaw catalogue.</li>
    <li><strong>Chaos Crew</strong> (96.33% RTP, high volatility, max win 11,000x) -- A comic-book heist theme. Five reels, expanding wilds that cover full reels in the free spins round. The crew character wilds have multiplier values that apply when they help form winning combinations. More accessible volatility than Wanted Dead or a Wild, but still firmly high-variance.</li>
    <li><strong>Le Bandit</strong> (96.35% RTP, very high volatility, max win 25,000x) -- A French gangster theme with an extended 8-reel layout. Respins triggered when specific bandit characters land. The unusual reel configuration produces combinations that do not appear in standard 5-reel slots, giving Le Bandit a distinct betting cadence.</li>
    <li><strong>Le Pharaoh</strong> (96.38% RTP, high volatility, max win 15,000x) -- An ancient Egypt theme, 5x4 grid. Sticky wilds accumulate during free spins, similar to the Wanted mechanic but in an Egyptian visual context. A companion title to Le Bandit in the Hacksaw French-titled series.</li>
    <li><strong>Stockholm Syndrome</strong> (96.50% RTP, very high volatility, max win 30,000x) -- A heist theme set in Stockholm. Expanding wilds during free spins with a hold-and-respin element. One of Hacksaw's longer free spins features, with retriggering possible up to a high maximum count.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics Hacksaw Gaming is known for</h2>
  <p>Sticky wild accumulation is the dominant mechanic in Hacksaw's flagship titles. During free spins in Wanted Dead or a Wild, wild symbols that land on the grid remain in place for the duration of the feature. As the spins progress, the grid fills incrementally with sticky wilds, which means the later spins of a free games round -- with more wilds held -- produce the largest wins. The potential payout scales steeply as wild coverage increases: a full or near-full wild grid on the final spin of a high-bet session can reach the maximum win cap.</p>
  <p>Hacksaw's buy feature (Bonus Buy) allows players to purchase direct access to the free spins round for 80x or 100x the bet, bypassing the base game. This is active at 1win under Curaçao 8048/JAZ rules. In markets where the buy feature is restricted (UKGC), the mechanic is disabled but the base game otherwise functions identically.</p>
  <p>Volatility design at Hacksaw is intentionally extreme. The studio's math models accept longer losing streaks in exchange for larger peak payouts than most competitors would publish. This creates a player experience that differs structurally from medium-volatility slots: sessions at Hacksaw titles are more likely to result in a significant down or a significant up, with fewer small wins filling the middle.</p>
</section>

<section class="how-to">
  <h2>How to play Hacksaw Gaming slots at 1win with XLBONUS</h2>
  <ol>
    <li>Register at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> during sign-up</li>
    <li>Complete verification and make a qualifying deposit</li>
    <li>Open the casino, search "Hacksaw" or filter by provider</li>
    <li>Start with Wanted Dead or a Wild or Chaos Crew, which are among the most-played Hacksaw titles at 1win</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>Hacksaw Gaming publishes standard RTP values in the range 96.33% to 96.50% across its main titles. The studio uses a single RTP configuration (no low-RTP alternative build is advertised to operators). Hit frequency on high-volatility Hacksaw titles is deliberately low -- the majority of spins in a session will return 0x, with payouts concentrated in the free spins feature rather than base game wins. This is the volatility tradeoff the math model is built around.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>When was Hacksaw Gaming founded?</summary>
    <p>Hacksaw Gaming was founded in 2018 in Sliema, Malta. The studio began with scratch cards before pivoting to video slots, which now form the core of its catalogue.</p>
  </details>
  <details>
    <summary>What is the maximum win in Wanted Dead or a Wild?</summary>
    <p>Wanted Dead or a Wild has a maximum win potential of 50,000x the bet. It is a very high volatility title with sticky wilds during free spins.</p>
  </details>
  <details>
    <summary>What licences does Hacksaw Gaming hold?</summary>
    <p>Hacksaw Gaming holds a B2B licence from the Malta Gaming Authority (MGA). Its titles are also distributed under operator licences including Curacao 8048/JAZ, making them available at 1win.</p>
  </details>
  <details>
    <summary>Are Hacksaw slots high volatility?</summary>
    <p>Most Hacksaw Gaming slots are rated high or very high volatility with maximum win potentials from 10,000x to 50,000x. The studio specifically targets the high-variance segment.</p>
  </details>
  <details>
    <summary>How do I claim a bonus for Hacksaw games at 1win?</summary>
    <p>Register at 1win.codes with promo code <span class="code-highlight">XLBONUS</span>. The welcome bonus applies to your account balance and can be used across all Hacksaw Gaming titles.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/hacksaw-gaming',
    title='Hacksaw Gaming slots at 1win: Wanted, Chaos Crew and XLBONUS',
    description='Play Hacksaw Gaming high-volatility slots at 1win. Wanted Dead or a Wild, Chaos Crew, Le Bandit and more. Register with XLBONUS under Curacao 8048/JAZ licence.',
    h1='Hacksaw Gaming slots at 1win',
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('Hacksaw Gaming', None)],
    main_html=hacksaw_main,
    extra_schema=hacksaw_schema,
)
open('en/providers/hacksaw-gaming.html', 'w').write(html)
print('Written: hacksaw-gaming.html')


# ─────────────────────────────────────────────
# 5. BGAMING
# ─────────────────────────────────────────────

bgaming_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BGaming",
  "foundingDate": "2018",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "EE",
    "addressLocality": "Tallinn"
  },
  "url": "https://bgaming.com/",
  "description": "BGaming is an Estonia-based iGaming studio founded in 2018, known for provably fair games and a crypto-native slot portfolio including Aviamasters and Plinko XY."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where is BGaming based?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BGaming is headquartered in Tallinn, Estonia. The company was founded in 2018 and focuses on provably fair games and crypto-native casino content."
      }
    },
    {
      "@type": "Question",
      "name": "What is Aviamasters?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Aviamasters is BGaming's flagship crash game, similar in format to Aviator but with distinct visual theming and a proprietary provably fair implementation. Players control a pilot character and cash out before the plane crashes."
      }
    },
    {
      "@type": "Question",
      "name": "Does BGaming support cryptocurrency deposits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BGaming's games are designed to be crypto-native and integrate easily with bitcoin and stablecoin deposit systems. 1win supports USDT and other crypto deposits, making BGaming titles fully accessible to crypto depositors."
      }
    },
    {
      "@type": "Question",
      "name": "What is provably fair in BGaming games?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BGaming uses a cryptographic provably fair system where each game round's seed is hashed and committed before play begins. After the round, the server seed is revealed so players can independently verify the outcome using the disclosed hash inputs."
      }
    },
    {
      "@type": "Question",
      "name": "What promo code should I use for BGaming at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use promo code XLBONUS when registering at 1win to activate the welcome bonus, which applies to BGaming slots and crash games in the casino catalogue."
      }
    }
  ]
}
</script>
"""

bgaming_main = """
<section class="lede">
  <p>1win features BGaming's full provably fair catalogue under a Curaçao 8048/JAZ licence, including Aviamasters and Plinko XY -- register with promo code <span class="code-highlight">XLBONUS</span> and explore 100+ crypto-native BGaming titles from your first session.</p>
</section>

<section class="key-facts">
  <h2>About BGaming</h2>
  <p>BGaming was founded in 2018 in Tallinn, Estonia. The studio emerged from the crypto casino ecosystem, building its initial portfolio for operators that accepted Bitcoin and other digital currencies before those payment methods became mainstream in the broader iGaming industry. This origin shapes the studio's technical architecture: BGaming titles are built with on-chain verifiability in mind, and provably fair is a standard feature rather than an optional add-on.</p>
  <p>The company holds a Malta Gaming Authority (MGA) B2B licence and has expanded distribution to over 900 operators globally. Its catalogue now spans crash games, video slots, table games, and keno-style titles. BGaming's slot portfolio is notable for a broad thematic range -- ancient mythology titles, branded pop-culture themes (released under content licences), and crash game variants all sit within the same provider API.</p>
  <p>At 1win, BGaming content is accessible to crypto depositors without any additional setup. USDT, BTC, ETH, and other supported crypto assets can be wagered directly on BGaming titles, and the provably fair verification links work in-game without needing a separate tool. This positions BGaming as the preferred choice for crypto-native players who want game-by-game auditability alongside a slot library of meaningful depth.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>2018</td></tr>
    <tr><th>Headquarters</th><td>Tallinn, Estonia</td></tr>
    <tr><th>Primary licence</th><td>MGA Malta (B2B)</td></tr>
    <tr><th>Operator count</th><td>900+ globally</td></tr>
    <tr><th>Key differentiator</th><td>Provably fair + crypto-native design</td></tr>
    <tr><th>Portfolio breadth</th><td>Crash games, slots, table games, keno</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature BGaming games at 1win</h2>
  <ul>
    <li><strong>Aviamasters</strong> -- BGaming's flagship crash game. A pilot and plane theme with a multiplier that rises until the craft vanishes. Two simultaneous bet positions available per player. Provably fair with on-screen seed verification link. The visual design differentiates it from Spribe's Aviator while using a comparable crash format. Active at 1win with full bet history and auto-cashout support.</li>
    <li><strong>Plinko XY</strong> -- A two-axis Plinko variant. Unlike standard single-drop Plinko, Plinko XY allows players to drop multiple balls simultaneously and set both vertical (risk level) and horizontal (start position) parameters. The dual-axis design creates more payout surface area than conventional Plinko. Provably fair.</li>
    <li><strong>Lucky Lady's Clover</strong> (96.05% RTP) -- A three-reel, five-payline classic slot with a four-leaf clover theme. One of BGaming's highest-traffic titles in European markets. Simple mechanics with a gamble feature that offers double-or-nothing on any win.</li>
    <li><strong>Book of Cats</strong> (96.17% RTP) -- BGaming's entry in the expanding-symbol book slot genre. Free spins with one expanding symbol cover all three positions on any reel. Cat-themed, accessible volatility.</li>
    <li><strong>Aztec Magic Bonanza</strong> (96.12% RTP) -- A Megaways-inspired Aztec theme with cascading symbols and a free spins round with increasing multipliers. Sits in the medium-high volatility tier.</li>
    <li><strong>Joker Queen</strong> (96.00% RTP) -- A five-reel classic joker slot with a progressive jackpot mechanic. Five jokers on an active payline award the major jackpot prize. One of BGaming's jackpot titles that attracts players from traditional slot backgrounds.</li>
    <li><strong>Bonk</strong> -- An instant-win multiplier game with a physics-based visual concept. A simple mechanics set designed for rapid play cycles, targeting mobile-first sessions.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics BGaming is known for</h2>
  <p>BGaming's provably fair implementation works differently from Spribe's in one key way: the seed verification interface is embedded directly inside the game client rather than requiring a separate external tool. Players can view the current hashed server seed, input their own client seed, and see the verification link without leaving the game. This in-game integration reduces friction for players who want to audit results during an active session.</p>
  <p>Crypto-native design extends to the bet sizing interface. BGaming titles denominate stakes in fiat equivalents but also display crypto unit equivalents in real time, reducing confusion for players depositing in USDT or BTC whose in-wallet balance and on-screen bet amounts need to align. This is a small UX detail but one that matters at operators like 1win where crypto deposit volume is significant.</p>
  <p>On the slot side, BGaming uses a modular math model approach: the same core grid engine supports multiple volatility configurations per title, allowing operators to select the variance profile that matches their player demographics. At 1win under Curaçao 8048/JAZ, the standard configurations apply, which tend toward medium to medium-high volatility with RTP values clustered around 96%.</p>
</section>

<section class="how-to">
  <h2>How to play BGaming titles at 1win with XLBONUS</h2>
  <ol>
    <li>Register at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> during sign-up</li>
    <li>Deposit using USDT, BTC, or any supported fiat method</li>
    <li>Navigate to casino and filter by provider BGaming</li>
    <li>Select Aviamasters for the crash experience or Plinko XY for the instant-win format</li>
    <li>Use the in-game provably fair link to verify any round's outcome in real time</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>BGaming slot titles publish RTPs in the 96.00% to 96.52% range. Crash games (Aviamasters) and instant-win titles (Plinko XY, Bonk) have variable RTPs that depend on the player's selected parameters. BGaming lists RTP values for all titles in its official game catalogue, accessible at bgaming.com. 1win operates the standard published RTP builds for all BGaming content.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>Where is BGaming based?</summary>
    <p>BGaming is headquartered in Tallinn, Estonia. The company was founded in 2018 and specialises in provably fair games and crypto-native casino content.</p>
  </details>
  <details>
    <summary>What is Aviamasters?</summary>
    <p>Aviamasters is BGaming's flagship crash game. Players control a pilot character and must cash out before the plane crashes. It uses a provably fair algorithm and supports two simultaneous bet positions.</p>
  </details>
  <details>
    <summary>Does BGaming support cryptocurrency?</summary>
    <p>BGaming's games are designed to be crypto-native. 1win supports USDT, BTC, ETH, and other crypto deposits, making BGaming titles fully accessible to crypto-first players.</p>
  </details>
  <details>
    <summary>What is provably fair in BGaming games?</summary>
    <p>BGaming uses a cryptographic provably fair system where each round's seed is hashed and committed before play begins. The verification interface is embedded directly in the game client so players can audit results without leaving the game.</p>
  </details>
  <details>
    <summary>What promo code should I use for BGaming at 1win?</summary>
    <p>Use promo code <span class="code-highlight">XLBONUS</span> when registering at 1win. The welcome bonus applies to your balance and can be wagered on all BGaming titles.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/bgaming',
    title='BGaming games at 1win: Aviamasters, Plinko XY and XLBONUS',
    description='Play BGaming provably fair slots and crash games at 1win. Aviamasters, Plinko XY and 100+ crypto-native titles. Register with XLBONUS under Curacao 8048/JAZ licence.',
    h1='BGaming at 1win: provably fair and crypto-native',
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('BGaming', None)],
    main_html=bgaming_main,
    extra_schema=bgaming_schema,
)
open('en/providers/bgaming.html', 'w').write(html)
print('Written: bgaming.html')


# ─────────────────────────────────────────────
# 6. PLAY'N GO
# ─────────────────────────────────────────────

playngo_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Play'n GO",
  "foundingDate": "1997",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "SE",
    "addressLocality": "Vaxjo"
  },
  "url": "https://www.playngo.com/",
  "description": "Play'n GO is a Swedish iGaming studio founded in 1997, one of the oldest in the industry and creator of Book of Dead, Reactoonz, and the Rich Wilde adventure series."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When was Play'n GO founded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Play'n GO was founded in 1997 in Vaxjo, Sweden. It is one of the oldest slot studios in the industry and holds one of the broadest regulatory approval records, including UKGC, MGA, Swedish Spelinspektionen, and over 20 additional jurisdictions."
      }
    },
    {
      "@type": "Question",
      "name": "What is the RTP of Book of Dead?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Book of Dead has a published RTP of 96.21%. It is a high-volatility slot with a single expanding symbol in free spins that covers all three rows when it appears on any reel."
      }
    },
    {
      "@type": "Question",
      "name": "What licences does Play'n GO hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Play'n GO holds licences from the UK Gambling Commission (UKGC), Malta Gaming Authority (MGA), Swedish Spelinspektionen, Danish Spillemyndigheden, German regulators, Italian ADM, and over 20 other jurisdictions. Its RNGs are certified by Testing Laboratories International (iTech Labs)."
      }
    },
    {
      "@type": "Question",
      "name": "Is Reactoonz a high-volatility slot?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reactoonz is a high-volatility slot with a 7x7 grid and a cluster pays mechanic. The fluctuating reels, cascading wins, and Quantum features make it one of the more volatile titles in Play'n GO's catalogue, despite a relatively accessible visual style."
      }
    },
    {
      "@type": "Question",
      "name": "How do I access Play'n GO slots at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Register at 1win.codes with promo code XLBONUS, navigate to the casino section, and filter by provider Play'n GO. Book of Dead, Reactoonz, Fire Joker, and over 200 other Play'n GO titles are available."
      }
    }
  ]
}
</script>
"""

playngo_main = """
<section class="lede">
  <p>1win carries 200+ Play'n GO titles under a Curaçao 8048/JAZ licence -- one of the industry's oldest studios, founded in 1997 in Sweden -- and new players who register with promo code <span class="code-highlight">XLBONUS</span> unlock welcome funds applicable across the full Play'n GO catalogue including Book of Dead and Reactoonz.</p>
</section>

<section class="key-facts">
  <h2>About Play'n GO</h2>
  <p>Play'n GO was founded in 1997 in Vaxjo, Sweden, making it one of the longest-operating slot studios in the industry. The company began as a B2B software provider for land-based operators before pivoting to online in 2005. Its regulatory portfolio is among the most extensive of any slot studio: UKGC, MGA, Swedish Spelinspektionen, Danish Spillemyndigheden, Italian ADM, German regulators, Portuguese SRIJ, Spanish DGOJ, and over 20 additional jurisdictions. RNG certification is conducted by iTech Labs.</p>
  <p>The studio's commercial landmark is Book of Dead, released in 2016. The title became the most-played slot in the UK market for multiple consecutive years and established Rich Wilde as the industry's most recognisable slot character. The success of Book of Dead led to a franchise: Rich Wilde and the Amulet of Dead, Rich Wilde and the Tome of Madness, and Pearls of India all extend the same character universe.</p>
  <p>Play'n GO is privately held, based in Sweden, and operates production studios in multiple countries. It competes with NetEnt and Pragmatic Play for regulated European market distribution but has a distinctly wider regulatory approval footprint than most competitors, making it accessible to the broadest range of licensed operators globally.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>1997</td></tr>
    <tr><th>Headquarters</th><td>Vaxjo, Sweden</td></tr>
    <tr><th>Primary licences</th><td>UKGC, MGA, Swedish Spelinspektionen</td></tr>
    <tr><th>Additional licences</th><td>20+ jurisdictions globally</td></tr>
    <tr><th>RNG certification</th><td>iTech Labs</td></tr>
    <tr><th>Flagship series</th><td>Rich Wilde (Book of Dead franchise)</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature Play'n GO games at 1win</h2>
  <ul>
    <li><strong>Book of Dead</strong> (96.21% RTP, high volatility, max win 5,000x) -- A five-reel, 10-payline Egyptian adventure slot. Rich Wilde is the scatter and wild symbol simultaneously. Free spins trigger with three Book scatters; one symbol is randomly selected to expand and cover all three rows on any reel it lands, generating full-reel wins across multiple lines simultaneously. The most-played Play'n GO title at 1win and at most European operators.</li>
    <li><strong>Reactoonz</strong> (96.51% RTP, high volatility, max win 4,570x) -- A 7x7 grid with cluster pays (5+ connected symbols). Cascading wins remove matching clusters and replace them with new symbols. The Quantumeter charges with each cascade and releases one of four Quantum features: Implosion (destroys non-matching symbols), Demolition (removes all instances of the lowest-value symbol), Alteration (transforms one symbol type into another), or Incision (draws a cross of one symbol type). A gooey alien creature appears as the highest-value symbol.</li>
    <li><strong>Fire Joker</strong> (96.15% RTP, high volatility, max win 800x) -- A three-reel classic slot with a joker wild and a "Wheel of Fire" respin mechanic. When two reels show the same symbol, the third reel respins. Low maximum win by modern standards, but the mechanic produces frequent small-to-medium wins, making it a durable favourite with traditional slot players.</li>
    <li><strong>Rise of Olympus</strong> (96.29% RTP, high volatility, max win 5,000x) -- Three Greek gods (Zeus, Poseidon, Hades) each have a distinct power that activates during the free spins round. Zeus removes low-value symbols; Poseidon transforms symbols; Hades destroys symbols and shuffles. Hand of God feature grants an extra power use. One of Play'n GO's highest-reviewed titles post-2018.</li>
    <li><strong>Gemix</strong> (96.77% RTP, medium volatility, max win 1,500x) -- A gem-matching cluster pays slot on a 7x7 grid. Crystal charges release one of four powers per charge: nova blast, nova strike, crystal warp, prism strike. More accessible volatility than most Play'n GO titles, suitable for players who prefer consistent action over infrequent large wins.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics Play'n GO is known for</h2>
  <p>The expanding symbol mechanic in the Book of Dead series is Play'n GO's most commercially successful mechanic. During free spins, one pre-selected symbol expands to cover all three rows on any reel where it appears -- and since paying symbols count wherever they land on active paylines, a full-reel expansion on reels 1, 2, and 3 simultaneously produces a line win across all 10 paylines for that symbol. This creates the possibility of very large single-spin payouts when the expansion triggers on adjacent reels.</p>
  <p>Cascade mechanics (also called tumbling reels or avalanche reels) appear in several Play'n GO titles including Reactoonz and Gemix. In Reactoonz's implementation, clusters of 5 or more connected matching symbols disappear after winning, and new symbols fall from above to fill the gaps. Each cascade recharges the Quantumeter, which releases random feature modifiers when it reaches certain thresholds. The Quantumeter design means longer cascading chains produce both direct wins (from each cascade) and accumulated bonus power effects.</p>
    <p>Play'n GO was an early adopter of the cluster pays mechanic (Gemix, Reactoonz) as an alternative to traditional payline structures. Cluster pays award wins for groups of 5 or more connected symbols of the same type, regardless of their position on the grid. This produces a different betting rhythm than payline slots: wins are less frequent but come from anywhere on the grid simultaneously, and cascade chains can generate multiple separate wins from a single spin.</p>
</section>

<section class="how-to">
  <h2>How to play Play'n GO slots at 1win with XLBONUS</h2>
  <ol>
    <li>Register at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> during sign-up</li>
    <li>Complete verification and make your first qualifying deposit</li>
    <li>Open Casino and filter by provider Play'n GO</li>
    <li>Start with Book of Dead for the classic expanding-symbol experience, or Reactoonz for the cluster-pays grid format</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>Play'n GO publishes RTP values for every title in its official portfolio. The standard range across the slot catalogue runs from 94.00% (some jackpot titles) to 96.77% (Gemix). Book of Dead is fixed at 96.21%; there is no documented low-RTP alternative build for this title. Play'n GO's extensive regulatory footprint (UKGC, MGA, Spelinspektionen) means most of its titles have been independently audited in multiple jurisdictions, and the published RTPs are consistently verified by iTech Labs. At 1win, the standard Play'n GO RTPs apply.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>When was Play'n GO founded?</summary>
    <p>Play'n GO was founded in 1997 in Vaxjo, Sweden. It is one of the oldest slot studios in the industry and holds licences from over 20 jurisdictions including UKGC, MGA, and Swedish Spelinspektionen.</p>
  </details>
  <details>
    <summary>What is the RTP of Book of Dead?</summary>
    <p>Book of Dead has a published RTP of 96.21%. It is a high-volatility slot where free spins feature a single expanding symbol that covers full reels.</p>
  </details>
  <details>
    <summary>What licences does Play'n GO hold?</summary>
    <p>Play'n GO holds licences from the UKGC, MGA, Swedish Spelinspektionen, Danish Spillemyndigheden, Italian ADM, and over 20 other jurisdictions. RNGs are certified by iTech Labs.</p>
  </details>
  <details>
    <summary>Is Reactoonz a high-volatility slot?</summary>
    <p>Reactoonz is a high-volatility slot (96.51% RTP) with a 7x7 cluster pays grid. The Quantum features and cascade mechanics make it one of the more volatile Play'n GO titles despite its accessible visual style.</p>
  </details>
  <details>
    <summary>How do I access Play'n GO slots at 1win?</summary>
    <p>Register at 1win.codes with promo code <span class="code-highlight">XLBONUS</span>, navigate to the casino, and filter by provider Play'n GO. Over 200 titles are available including Book of Dead and Reactoonz.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/playn-go',
    title="Play'n GO slots at 1win: Book of Dead, Reactoonz and XLBONUS",
    description="Play 200+ Play'n GO slots at 1win including Book of Dead and Reactoonz. Sweden's oldest slot studio with UKGC and MGA licences. Register with XLBONUS under Curacao 8048/JAZ.",
    h1="Play'n GO slots at 1win",
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ("Play'n GO", None)],
    main_html=playngo_main,
    extra_schema=playngo_schema,
)
open('en/providers/playn-go.html', 'w').write(html)
print('Written: playn-go.html')


# ─────────────────────────────────────────────
# 7. NETENT
# ─────────────────────────────────────────────

netent_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "NetEnt",
  "foundingDate": "1996",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "SE",
    "addressLocality": "Stockholm"
  },
  "url": "https://www.netent.com/",
  "description": "NetEnt is a Swedish iGaming studio founded in 1996, creator of Starburst, Gonzo's Quest, and Dead or Alive. Acquired by Evolution Gaming in 2020, NetEnt remains a distinct brand within the Evolution Group."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When was NetEnt founded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "NetEnt was founded in 1996 in Stockholm, Sweden. It was acquired by Evolution Gaming in 2020 and continues to operate as a distinct brand within the Evolution Group, producing new titles while maintaining its legacy portfolio."
      }
    },
    {
      "@type": "Question",
      "name": "What is the RTP of Starburst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Starburst has a published RTP of 96.09% in its standard configuration. The Starburst XXXtreme variant (released 2021) has a higher published RTP of 96.26% and adds a streak respin mechanic with multipliers."
      }
    },
    {
      "@type": "Question",
      "name": "What licences does NetEnt hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "NetEnt holds licences from the UK Gambling Commission (UKGC), Malta Gaming Authority (MGA), Swedish Spelinspektionen, Danish Spillemyndigheden, Italian ADM, New Jersey Division of Gaming Enforcement, and numerous other jurisdictions. As part of Evolution Group, it benefits from Evolution's extensive regulatory footprint."
      }
    },
    {
      "@type": "Question",
      "name": "Is Dead or Alive high volatility?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dead or Alive 2 (the sequel) is rated very high volatility with a maximum win of 100,000x the bet -- one of the highest win potentials ever published by a regulated studio. The original Dead or Alive is high volatility with a lower maximum win. Both feature sticky wilds during free spins."
      }
    },
    {
      "@type": "Question",
      "name": "How do I access NetEnt games at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Register at 1win.codes with promo code XLBONUS, navigate to the casino section, and filter by provider NetEnt. Starburst, Gonzo's Quest, Dead or Alive, Mega Fortune and the full legacy catalogue are available."
      }
    }
  ]
}
</script>
"""

netent_main = """
<section class="lede">
  <p>1win carries the full NetEnt catalogue under a Curaçao 8048/JAZ licence -- a legacy portfolio built over 28 years since the studio's founding in 1996 in Stockholm -- and players who register with promo code <span class="code-highlight">XLBONUS</span> access Starburst, Gonzo's Quest, and Dead or Alive 2 from their first session.</p>
</section>

<section class="key-facts">
  <h2>About NetEnt</h2>
  <p>NetEnt (Net Entertainment) was founded in 1996 in Stockholm, Sweden, making it the oldest major slot studio still producing commercial titles. The company built the European regulated online slot market alongside Microgaming in the late 1990s and 2000s, establishing technical standards for RNG implementation that influenced the industry's regulatory certification process. NetEnt went public on Nasdaq Stockholm in 2007.</p>
  <p>In 2020, Evolution Gaming acquired NetEnt for approximately SEK 19.6 billion (roughly EUR 1.9 billion at the time), consolidating the two largest names in European online gaming under one corporate umbrella. NetEnt continues to operate as a distinct brand within the Evolution Group, releasing new titles and maintaining its legacy portfolio. The acquisition gave Evolution access to NetEnt's extensive regulatory licences, including the New Jersey Division of Gaming Enforcement approval that took NetEnt into the US market.</p>
  <p>NetEnt's regulatory footprint includes UKGC, MGA, Swedish Spelinspektionen, Danish Spillemyndigheden, Italian ADM, New Jersey DGE, Pennsylvania Gaming Control Board, and 25+ additional jurisdictions. GLI and BMM Testlabs provide independent RNG certification. At 1win under Curaçao 8048/JAZ, the full NetEnt catalogue is accessible including older titles and high-variance variants that may be restricted in some European markets.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>1996</td></tr>
    <tr><th>Headquarters</th><td>Stockholm, Sweden</td></tr>
    <tr><th>Acquired by</th><td>Evolution Gaming (2020)</td></tr>
    <tr><th>Primary licences</th><td>UKGC, MGA, Swedish Spelinspektionen</td></tr>
    <tr><th>US presence</th><td>New Jersey DGE, Pennsylvania GCB</td></tr>
    <tr><th>RNG certification</th><td>GLI + BMM Testlabs</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature NetEnt games at 1win</h2>
  <ul>
    <li><strong>Starburst</strong> (96.09% RTP, low volatility) -- A five-reel, 10-payline gem slot with expanding wilds that cover the full reel and trigger a respin. Pays both ways (left-to-right and right-to-left). The most-distributed slot title in the history of online gambling by operator count; its low volatility and simple mechanic make it the standard free-spins bonus delivery vehicle at most European operators. The XXXtreme variant (96.26% RTP) adds multiplier streaks.</li>
    <li><strong>Gonzo's Quest</strong> (95.97% RTP, medium volatility, max win 2,500x) -- The title that popularised the Avalanche/cascade mechanic in 2011. Falling stone blocks form wins; winning blocks explode and are replaced by new ones from above. Multipliers increase with each consecutive cascade (1x, 2x, 3x, 5x in the base game; 3x, 6x, 9x, 15x in free falls). One of the first slots to use 3D character animation.</li>
    <li><strong>Dead or Alive 2</strong> (96.82% RTP, very high volatility, max win 100,000x) -- The sequel to NetEnt's classic western slot. Three free spin modes: Train Heist (sticky wilds), High Noon Saloon (random wilds each spin), or Old Saloon (6 free spins, sticky wilds that reset game on retrigger). The 100,000x maximum win is among the highest published by any regulated studio. Buy feature active at 1win.</li>
    <li><strong>Mega Fortune</strong> (96.00% RTP, medium volatility) -- A luxury-themed progressive jackpot slot with three networked jackpots (Rapid, Major, Mega). The Mega jackpot has historically paid in the EUR millions range. Wheel-of-fortune bonus round determines jackpot tier. The longest-running progressive jackpot network in NetEnt's portfolio.</li>
    <li><strong>Twin Spin</strong> (96.60% RTP, medium-high volatility) -- A classic-meets-video hybrid. At the start of each spin, two adjacent reels are "twinned" and display identical symbols; the twin mechanic can expand to cover 3, 4, or all 5 reels during a spin. No free spins; the twin expansion is the primary variance driver.</li>
    <li><strong>Hotline</strong> (96.92% RTP, high volatility) -- A Miami Vice-inspired slot with expanding wilds across three hotline rows. Each hotline expands the designated row into a full wild strip. Nudge mechanic in the base game offers additional chances to complete winning lines. One of NetEnt's highest published RTP titles.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics NetEnt is known for</h2>
  <p>The Avalanche mechanic (cascade mechanic) was NetEnt's 2011 contribution to the slot industry via Gonzo's Quest. It replaced spinning reels with blocks that fall into position, and winning blocks disintegrate to allow new ones to fall from above. The multiplier-per-cascade progression (1x through 5x in the base game) meant that long cascade chains produced outsized payouts relative to the initial bet, which is the mathematical root of high-variance play at low average stake.</p>
  <p>NetEnt's expanding wild mechanic in Starburst and its variants is a simpler but commercially successful approach: a wild symbol expands to cover an entire reel, which triggers a re-spin so players can collect the expanded wild win. The re-spin is not a free spin; it is a feature triggered within the base game flow, which matters for bonus wagering terms at many operators including 1win.</p>
  <p>Dead or Alive 2's sticky wild mechanic during Train Heist mode accumulates wilds across all 5 reels and 9 rows over 9 free spins. The maximum configuration (all 45 positions wild) cannot be reached in a single free spins round, but partial coverage of 15-20 wild positions can produce wins in the five-to-six-figure range at adequate bet sizes. This specific mechanic is why DoA2 has the highest maximum win cap (100,000x) of any NetEnt slot.</p>
</section>

<section class="how-to">
  <h2>How to play NetEnt slots at 1win with XLBONUS</h2>
  <ol>
    <li>Register at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> during sign-up</li>
    <li>Complete verification and deposit to activate your welcome package</li>
    <li>Open Casino and search "NetEnt" or filter by provider</li>
    <li>Starburst is typically featured on the homepage; Dead or Alive 2 and Gonzo's Quest are in the high-variance section</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>NetEnt publishes standard RTP values for every title. The range across the active catalogue spans 94.00% to 96.92%. Starburst is fixed at 96.09%; Gonzo's Quest at 95.97%; Dead or Alive 2 at 96.82%; Hotline at 96.92%. Some NetEnt titles have documented low-RTP alternative configurations (typically 89.00%-92.00%) used in markets where operators pay high tax rates. At 1win, standard RTPs apply. NetEnt has historically been transparent about its math models, partly due to regulatory requirements from UKGC and Swedish Spelinspektionen which mandate public RTP disclosure at the game level.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>When was NetEnt founded?</summary>
    <p>NetEnt was founded in 1996 in Stockholm, Sweden. It was acquired by Evolution Gaming in 2020 and continues operating as a distinct brand within the Evolution Group.</p>
  </details>
  <details>
    <summary>What is the RTP of Starburst?</summary>
    <p>Starburst has a published RTP of 96.09%. The Starburst XXXtreme variant has a higher RTP of 96.26% and adds a streak respin mechanic with multipliers.</p>
  </details>
  <details>
    <summary>What licences does NetEnt hold?</summary>
    <p>NetEnt holds licences from UKGC, MGA, Swedish Spelinspektionen, Danish Spillemyndigheden, Italian ADM, New Jersey DGE, and 25+ additional jurisdictions. RNG certification is from GLI and BMM Testlabs.</p>
  </details>
  <details>
    <summary>Is Dead or Alive 2 high volatility?</summary>
    <p>Dead or Alive 2 is rated very high volatility with a maximum win of 100,000x the bet, one of the highest ever published by a regulated studio. It features sticky wilds during free spins with three selectable mode variants.</p>
  </details>
  <details>
    <summary>How do I access NetEnt games at 1win?</summary>
    <p>Register at 1win.codes with promo code <span class="code-highlight">XLBONUS</span>, navigate to the casino, and filter by provider NetEnt. Starburst, Gonzo's Quest, Dead or Alive 2 and the full legacy catalogue are available.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/netent',
    title='NetEnt slots at 1win: Starburst, Gonzo and XLBONUS',
    description="Play NetEnt slots at 1win including Starburst, Gonzo's Quest and Dead or Alive 2. Founded 1996, UKGC and MGA licensed. Register with promo code XLBONUS under Curacao 8048/JAZ.",
    h1="NetEnt slots at 1win: 28 years of iGaming",
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('NetEnt', None)],
    main_html=netent_main,
    extra_schema=netent_schema,
)
open('en/providers/netent.html', 'w').write(html)
print('Written: netent.html')


# ─────────────────────────────────────────────
# 8. RELAX GAMING
# ─────────────────────────────────────────────

relax_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Relax Gaming",
  "foundingDate": "2010",
  "foundingLocation": {
    "@type": "Place",
    "addressCountry": "MT",
    "addressLocality": "Sliema"
  },
  "url": "https://relax-gaming.com/",
  "description": "Relax Gaming is a Malta-based iGaming aggregator and slot studio founded in 2010, creator of the Money Train franchise and known for high-volatility titles with maximum wins above 50,000x."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When was Relax Gaming founded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Relax Gaming was founded in 2010 in Sliema, Malta. The company operates both as a standalone slot studio and as an aggregation platform, distributing third-party content alongside its own proprietary titles."
      }
    },
    {
      "@type": "Question",
      "name": "What is the maximum win in Money Train 4?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Money Train 4 has a maximum win potential of 100,000x the bet. The Money Train franchise (1 through 4) is known for its Bonus Collector mechanic, where collector symbols accumulate the values of other symbols they land on during the Bonus Train feature."
      }
    },
    {
      "@type": "Question",
      "name": "What licences does Relax Gaming hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Relax Gaming holds a B2B licence from the Malta Gaming Authority (MGA). Its titles are also distributed under operator licences including Curacao 8048/JAZ, making them available at 1win."
      }
    },
    {
      "@type": "Question",
      "name": "Are Relax Gaming slots high volatility?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most Relax Gaming proprietary slots are rated high or very high volatility. The Money Train series, Snake Arena, Hellcatraz, and Beast Mode all feature maximum win potentials above 50,000x and are designed for players comfortable with extended losing streaks between large wins."
      }
    },
    {
      "@type": "Question",
      "name": "How do I play Money Train at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Register at 1win.codes with promo code XLBONUS, navigate to the casino section, search Money Train, and select your preferred title from the franchise (Money Train 1 through 4). All four are available under the Relax Gaming provider filter."
      }
    }
  ]
}
</script>
"""

relax_main = """
<section class="lede">
  <p>1win stocks the complete Relax Gaming portfolio under a Curaçao 8048/JAZ licence, including all four Money Train titles and Snake Arena -- use promo code <span class="code-highlight">XLBONUS</span> at registration to access this Malta studio's high-variance catalogue from your first deposit.</p>
</section>

<section class="key-facts">
  <h2>About Relax Gaming</h2>
  <p>Relax Gaming was founded in 2010 in Sliema, Malta. The company operates on a dual model: it produces proprietary slot titles under its own brand, and it also functions as a content aggregator distributing third-party game studios through its Silver Bullet and Powered by Relax partner programs. This aggregator-plus-studio model is uncommon among slot developers and allows Relax to offer operators a single API connection to both its own titles and a library of partner studios' content.</p>
  <p>The studio holds a primary B2B licence from the Malta Gaming Authority and distributes its content under operator licences globally, including Curaçao 8048/JAZ at 1win. Relax Gaming was acquired by Kindred Group (then Unibet's parent company) in 2018, which gave it access to Kindred's player data and a captive distribution channel across Kindred's 11 brands. In 2021, Kindred divested its Relax stake to Eurazeo, and Relax has operated independently since.</p>
  <p>In terms of market positioning, Relax is the primary competitor to Nolimit City in the very-high-volatility slot segment. Both studios target players who want maximum win potentials above 50,000x, buy feature access, and mechanic complexity in the bonus rounds. Relax's Money Train franchise is its commercial anchor, while Nolimit City competes with xWays and xNudge titles.</p>
  <table class="facts-table">
    <tr><th>Founded</th><td>2010</td></tr>
    <tr><th>Headquarters</th><td>Sliema, Malta</td></tr>
    <tr><th>Primary licence</th><td>MGA Malta (B2B)</td></tr>
    <tr><th>Business model</th><td>Proprietary studio + content aggregator</td></tr>
    <tr><th>Flagship franchise</th><td>Money Train (1-4)</td></tr>
    <tr><th>Max win range</th><td>50,000x to 100,000x bet</td></tr>
  </table>
</section>

<section class="games">
  <h2>Signature Relax Gaming games at 1win</h2>
  <ul>
    <li><strong>Money Train 2</strong> (96.40% RTP, very high volatility, max win 50,000x) -- The sequel that cemented the franchise. A wild west train robbery theme with a 5x4 grid. The Bonus Train feature activates a persistent mechanic where Collector symbols accumulate the coin values of adjacent symbol types. Payer symbols pay each spin; Collector symbols add adjacent values to their total. The combination of multiple Collector and Payer symbols on the grid simultaneously can produce compound win multipliers well above 1,000x.</li>
    <li><strong>Money Train 3</strong> (96.00% RTP, very high volatility, max win 100,000x) -- The third instalment doubled the maximum win and added the Persistent Collector mechanic: Collector symbols keep their accumulated value across multiple spins within the bonus feature rather than resetting. Added environmental zone symbols (Wasteland, Desert, Forest) that interact with Collector symbol types during the bonus.</li>
    <li><strong>Money Train 4</strong> (96.00% RTP, very high volatility, max win 100,000x) -- The current flagship title. Introduces a dual-phase bonus train feature: Phase 1 charges multiplier tokens, Phase 2 activates them. New symbol types (Necromancer, Shaman) add interactions within the bonus that were not present in earlier instalments.</li>
    <li><strong>Money Train 1</strong> (97.04% RTP, high volatility, max win 6,144x) -- The original. Lower maximum win than sequels but higher published RTP. The foundational Collector/Payer mechanic in its simplest form. Useful for players learning the Money Train format before committing to the more complex later versions.</li>
    <li><strong>Snake Arena</strong> (96.16% RTP, very high volatility, max win 50,000x) -- A snake-themed grid slot where snake symbols traverse the grid during the bonus round. As snakes grow by eating other symbols, they create longer win chains. One of Relax's most distinctive visual concepts outside the Money Train franchise.</li>
    <li><strong>Iron Bank</strong> (96.16% RTP, very high volatility, max win 50,000x) -- A bank heist theme with an Iron Bank free spins round featuring sticky wilds and multiplier progression. One of Relax's earlier high-variance titles, released before the Money Train sequels established the franchise's dominance.</li>
    <li><strong>Hellcatraz</strong> (96.30% RTP, very high volatility, max win 66,666x) -- A prison escape theme set in an Alcatraz-inspired setting. The Escape Room bonus has multiple chambers, each adding a multiplier as players progress. One of Relax's highest-reviewed titles for pure bonus round complexity.</li>
    <li><strong>Beast Mode</strong> (96.25% RTP, very high volatility, max win 75,000x) -- A sports-theme slot where win multipliers accumulate across a bonus feature with retrigger potential. One of Relax's more recent titles targeting the high-variance sports betting crossover audience.</li>
  </ul>
</section>

<section class="mechanics">
  <h2>Game mechanics Relax Gaming is known for</h2>
  <p>The Collector/Payer mechanic in the Money Train series is Relax's defining technical contribution. In the Bonus Train feature, Payer symbols hold a base coin value. Collector symbols accumulate coin values from any Payer symbol of the same type that also appears on the grid. If a Collector and Payer of the same type are on the grid simultaneously at the end of a spin, the Collector adds the Payer's value to its own running total. Each spin that fires the bonus, all active Collector symbols pay out their accumulated total. When multiple Collector/Payer pairs of different types interact simultaneously, the resulting payout can combine across all active pairs in a single spin.</p>
  <p>The Persistent Collector in Money Train 3 and 4 extends this by carrying accumulated values forward across spins rather than resetting each spin. A Collector that reaches the grid in spin 1 and stays through spin 8 has accumulated values from 7 additional spins. In combination with Necromancer or Shaman symbols (which extend the bonus or multiply accumulated values), the compound effect is what allows the 100,000x cap to be theoretically reached.</p>
  <p>Relax Gaming's buy feature (Train Ticket) allows direct bonus access at 100x the bet for most Money Train titles. This is active at 1win under Curaçao 8048/JAZ rules. The buy feature does not change the math model of the bonus round; it simply removes the wait for natural bonus triggering via scatter symbols.</p>
</section>

<section class="how-to">
  <h2>How to play Relax Gaming slots at 1win with XLBONUS</h2>
  <ol>
    <li>Register at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a></li>
    <li>Enter promo code <span class="code-highlight">XLBONUS</span> during sign-up</li>
    <li>Complete verification and deposit to activate your welcome package</li>
    <li>Open Casino, filter by provider Relax Gaming</li>
    <li>Start with Money Train 2 for the core Collector/Payer mechanic, or jump to Money Train 4 for the current flagship</li>
  </ol>
</section>

<section class="rtp">
  <h2>RTP transparency</h2>
  <p>Relax Gaming publishes standard RTP values for all titles. Money Train 1 stands at 97.04%; Money Train 2 at 96.40%; Money Train 3 and 4 at 96.00%. The drop from MT1 to MT3/4 reflects the trade-off between RTP and maximum win potential: higher caps require more of the theoretical return to be concentrated in the tail of the payout distribution, which lowers average return. Snake Arena, Iron Bank, Hellcatraz, and Beast Mode are all in the 96.16%-96.30% range. 1win operates standard RTP configurations for all Relax Gaming content.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>When was Relax Gaming founded?</summary>
    <p>Relax Gaming was founded in 2010 in Sliema, Malta. The company operates as both a standalone slot studio and a content aggregator platform.</p>
  </details>
  <details>
    <summary>What is the maximum win in Money Train 4?</summary>
    <p>Money Train 4 has a maximum win potential of 100,000x the bet. The Money Train franchise uses a Collector/Payer mechanic where Collector symbols accumulate values from Payer symbols over multiple bonus spins.</p>
  </details>
  <details>
    <summary>What licences does Relax Gaming hold?</summary>
    <p>Relax Gaming holds a B2B licence from the Malta Gaming Authority (MGA). Its titles are distributed under operator licences including Curacao 8048/JAZ at 1win.</p>
  </details>
  <details>
    <summary>Are Relax Gaming slots high volatility?</summary>
    <p>Most Relax Gaming proprietary slots are rated very high volatility with maximum win potentials of 50,000x to 100,000x. The Money Train series, Snake Arena, Hellcatraz, and Beast Mode are all in the very-high-variance tier.</p>
  </details>
  <details>
    <summary>How do I play Money Train at 1win?</summary>
    <p>Register at 1win.codes with promo code <span class="code-highlight">XLBONUS</span>, navigate to the casino, search "Money Train", and select your preferred title. All four Money Train titles are available under the Relax Gaming provider filter.</p>
  </details>
</section>
"""

html = render_page(
    slug='providers/relax-gaming',
    title='Relax Gaming at 1win: Money Train franchise and XLBONUS',
    description='Play Relax Gaming slots at 1win including Money Train 1-4, Snake Arena and Hellcatraz. Very high volatility titles with up to 100,000x max win. Register with XLBONUS under Curacao 8048/JAZ.',
    h1='Relax Gaming slots at 1win: Money Train and beyond',
    breadcrumbs=[('Home', '/en/'), ('Providers', '/en/providers/'), ('Relax Gaming', None)],
    main_html=relax_main,
    extra_schema=relax_schema,
)
open('en/providers/relax-gaming.html', 'w').write(html)
print('Written: relax-gaming.html')

print('All 8 provider pages written.')
