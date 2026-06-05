"""Build all sport landing pages for en/sports/"""
import os, sys
sys.path.insert(0, '/home/user/workspace/1win-codes-repo')
from build_helpers.page_template import render_page

os.makedirs('en/sports', exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# 1. FOOTBALL
# ─────────────────────────────────────────────────────────────────────────────

football_main = """
<section class="lede">
  <p>1win covers global football betting across 40,000+ markets, giving you access to every tier of the beautiful game under a single account licensed by Curaçao 8048/JAZ. From a Premier League Saturday 3 pm kick-off to a Copa Libertadores quarter-final played under floodlights in Buenos Aires, every fixture is priced competitively and available for in-play wagering. Claim promo code <span class="code-highlight">XLBONUS</span> at registration to boost your opening deposit and start betting straight away.</p>
</section>

<section class="key-facts">
  <h2>Hero stats</h2>
  <table class="facts-table">
    <tr><th>Markets available</th><td>40,000+</td></tr>
    <tr><th>Welcome bonus code</th><td><span class="code-highlight">XLBONUS</span></td></tr>
    <tr><th>In-play streaming</th><td>Select matches, live throughout the day</td></tr>
    <tr><th>Cashout</th><td>24/7 full and partial cashout</td></tr>
    <tr><th>Licence</th><td>Curaçao 8048/JAZ</td></tr>
  </table>
</section>

<section class="competitions">
  <h2>Tournaments and competitions covered</h2>
  <p>1win prices fixtures across every major league and continental cup. Below is a breakdown of competitions you will find listed every week of the calendar year.</p>
  <ul>
    <li><strong>English Premier League</strong> - The most watched league on the planet, running August to May. Manchester City, Arsenal and Liverpool drive the title race while relegation battles add tension to every bottom-half fixture. 1win lists pre-match and in-play markets for all 380 games.</li>
    <li><strong>La Liga</strong> - Real Madrid and Barcelona dominate Spanish football, but Atletico Madrid and Athletic Club regularly challenge. Clásico fixtures attract the widest range of specials on 1win.</li>
    <li><strong>Bundesliga</strong> - Germany's top flight is one of the highest-scoring leagues globally. Bayern Munich set the pace, while Bayer Leverkusen's title-winning 2023-24 season showed that challengers are emerging.</li>
    <li><strong>Serie A</strong> - Italian football's tactical depth makes the market variety on 1win particularly rewarding. Inter Milan, Napoli and Juventus share title ambitions across the 2025-26 campaign.</li>
    <li><strong>Ligue 1</strong> - French football gains from Paris Saint-Germain's continental pull, though Marseille and Monaco provide consistent title pressure.</li>
    <li><strong>UEFA Champions League</strong> - Europe's premier club competition runs from September to the May final. Real Madrid, holders of the 2024 trophy, remain favourites to add another European Cup to their record tally.</li>
    <li><strong>UEFA Europa League and Conference League</strong> - The two secondary European tiers give mid-table clubs continental exposure and provide 1win bettors with an extended fixture list on Thursday evenings.</li>
    <li><strong>FIFA World Cup</strong> - The 2026 edition is jointly hosted by the USA, Canada and Mexico. 1win will price every group-stage fixture, knockout round and ultimately the final on 18 July 2026 in New York/New Jersey.</li>
    <li><strong>UEFA European Championship</strong> - England's 2024 final defeat to Spain at the Olympiastadion in Berlin set the stage for an intense cycle of qualifying that 1win covers from the first whistle.</li>
    <li><strong>Copa America</strong> - CONMEBOL's flagship national-team competition. Argentina, reigning world champions, defended their title in the 2024 edition and remain tournament favourites under Lionel Scaloni.</li>
    <li><strong>Africa Cup of Nations</strong> - AFCON draws enormous betting interest from West and North African markets. Morocco and Nigeria lead the contenders heading into the next cycle.</li>
    <li><strong>Copa Libertadores</strong> - South America's Champions League. Flamengo, River Plate and Boca Juniors generate the most market depth on 1win, with all-South-American finals particularly popular.</li>
    <li><strong>MLS</strong> - The American soccer league expands its global fanbase with marquee names. Inter Miami and LA Galaxy are consistently among the best-priced teams on the platform.</li>
    <li><strong>Saudi Pro League</strong> - Cristiano Ronaldo, Neymar and Karim Benzema attracted global attention to the Saudi top flight. Al-Nassr fixtures draw some of the highest pre-match betting volumes outside Europe.</li>
    <li><strong>A-League (Australia)</strong> - The Australian top tier runs October to May and provides late-night betting options for European and Asian bettors. Melbourne City and Sydney FC are the standard-bearers.</li>
  </ul>
</section>

<section class="markets">
  <h2>Most popular football betting markets</h2>
  <ul>
    <li><strong>Match winner (1X2)</strong> - The cornerstone market. Back home win, draw or away win on every fixture.</li>
    <li><strong>Asian handicap</strong> - Removes the draw option by applying fractional goal advantages. Ideal when one side is a heavy favourite.</li>
    <li><strong>Over/Under total goals</strong> - Bet on whether both teams combined will score above or below a stated line, most commonly 2.5 goals.</li>
    <li><strong>Both teams to score (BTTS)</strong> - A popular accumulator leg. Football at 1win carries BTTS on every top-flight game globally.</li>
    <li><strong>Correct score</strong> - Predict the exact scoreline. Higher odds reward precise forecasting.</li>
    <li><strong>First goalscorer</strong> - Back Erling Haaland, Kylian Mbappe or any listed player to open the scoring.</li>
    <li><strong>Anytime goalscorer</strong> - Broader version of first goalscorer; the player simply needs to score at any point.</li>
    <li><strong>Half-time/Full-time double result</strong> - Combine the half-time result with the full-time result for enhanced odds.</li>
    <li><strong>Cards and corners markets</strong> - Number of yellow cards, red cards, total corners, corner handicap.</li>
  </ul>
</section>

<section class="inplay">
  <h2>In-play and live football betting</h2>
  <p>1win's in-play interface updates odds continuously as play unfolds, giving you the chance to react to goals, red cards, penalty decisions and injury-time drama in real time. The platform streams select matches directly within the bet slip area, so you can watch and wager without switching tabs.</p>
  <p>Pre-match betting suits research-driven strategies: form tables, injury reports and head-to-head records all inform a well-placed 1X2 or Asian handicap before kick-off. In-play betting, by contrast, rewards reading the game live. If a match starts with one team dominating possession but failing to convert, the live odds on the underdog shift in your favour before they eventually equalise. Equally, a red card in the 30th minute is often a trigger for a well-timed cashout or a new in-play bet at superior odds.</p>
  <p>Key in-play markets: next goal scorer, next team to score, current match result at 15-minute intervals, number of remaining corners, and whether the next goal will be scored before or after a specific minute. 1win keeps the odds feed live even during VAR delays, adjusting prices the moment a decision is confirmed.</p>
</section>

<section class="cashout">
  <h2>Cashout and bet builder</h2>
  <p>1win's cashout feature operates 24/7 on eligible pre-match and in-play bets. Full cashout closes your position and returns a calculated sum before the event finishes. Partial cashout lets you secure a portion of the return while leaving the remainder active on the original selection. This is particularly useful in football accumulators: if the first three legs have won and the final leg is in progress, a partial cashout locks in profit regardless of the final result.</p>
  <p>The bet builder (also known as a same-game parlay) allows you to combine multiple markets from the same fixture into a single bet. For a Champions League match you might link: Real Madrid to win, Vinicius Jr. to score anytime, and over 2.5 goals total. The odds multiply, increasing the potential return significantly versus three separate singles.</p>
</section>

<section class="mobile">
  <h2>Mobile football betting with the 1win app</h2>
  <p>The 1win mobile app delivers the full sportsbook on Android and iOS. Every football market listed on desktop is available on the app, including in-play streaming where applicable. Download the APK directly from <a href="/en/app">1win.codes/en/app</a> or install via the App Store. The app supports push notifications for bet settlement, so you know the moment your goalscorer bet lands or your cashout request is processed.</p>
</section>

<section class="how-to">
  <h2>How to start betting on football at 1win</h2>
  <ol>
    <li><strong>Open your account</strong> - Visit the registration page and fill in your details. The process takes under two minutes.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> - Type XLBONUS in the promo field at registration to activate your welcome bonus on the first deposit.</li>
    <li><strong>Make your first deposit</strong> - 1win accepts cards, e-wallets, UPI, PIX, USDT and other payment methods. Your bonus is credited automatically.</li>
    <li><strong>Navigate to Football</strong> - Select Sports from the main menu, then choose Football. Filter by league or search for a specific fixture.</li>
    <li><strong>Place your first bet</strong> - Click any odds to add a selection to your bet slip, enter your stake, confirm the bet and watch the match unfold.</li>
  </ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>What football leagues does 1win cover?</summary>
    <p>1win covers all major domestic leagues including the English Premier League, La Liga, Bundesliga, Serie A and Ligue 1, plus continental competitions such as the Champions League, Europa League and Conference League, as well as the World Cup, European Championship, Copa America, Copa Libertadores, MLS, Saudi Pro League and A-League among others.</p>
  </details>
  <details>
    <summary>How many football markets are available?</summary>
    <p>1win offers 40,000+ markets across global football, covering match winner, handicap, totals, BTTS, correct score, goalscorer, cards, corners and many competition-specific specials.</p>
  </details>
  <details>
    <summary>Can I bet on football in play at 1win?</summary>
    <p>Yes. 1win's in-play betting platform covers all top-flight football with live odds that update continuously. Select fixtures also include live streaming so you can watch and bet simultaneously.</p>
  </details>
  <details>
    <summary>What is the XLBONUS promo code?</summary>
    <p>XLBONUS is the welcome promo code for new 1win accounts. Enter it at registration before your first deposit to unlock the welcome bonus offer currently available to new players.</p>
  </details>
  <details>
    <summary>Does 1win offer cashout on football bets?</summary>
    <p>Yes. Full and partial cashout is available 24/7 on eligible football bets, both pre-match and in-play, allowing you to secure returns or cut losses before a fixture finishes.</p>
  </details>
  <details>
    <summary>Is 1win licensed and safe to use?</summary>
    <p>1win operates under a Curaçao 8048/JAZ licence, which governs its sports betting and casino operations and sets standards for player fund security and fair play.</p>
  </details>
</section>
"""

football_faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What football leagues does 1win cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win covers all major domestic leagues including the English Premier League, La Liga, Bundesliga, Serie A and Ligue 1, plus continental competitions such as the Champions League, Europa League and Conference League, as well as the World Cup, European Championship, Copa America, Copa Libertadores, MLS, Saudi Pro League and A-League among others."
      }
    },
    {
      "@type": "Question",
      "name": "How many football markets are available?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win offers 40,000+ markets across global football, covering match winner, handicap, totals, BTTS, correct score, goalscorer, cards, corners and many competition-specific specials."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bet on football in play at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win's in-play betting platform covers all top-flight football with live odds that update continuously. Select fixtures also include live streaming so you can watch and bet simultaneously."
      }
    },
    {
      "@type": "Question",
      "name": "What is the XLBONUS promo code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "XLBONUS is the welcome promo code for new 1win accounts. Enter it at registration before your first deposit to unlock the welcome bonus offer currently available to new players."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win offer cashout on football bets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Full and partial cashout is available 24/7 on eligible football bets, both pre-match and in-play, allowing you to secure returns or cut losses before a fixture finishes."
      }
    },
    {
      "@type": "Question",
      "name": "Is 1win licensed and safe to use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win operates under a Curacao 8048/JAZ licence, which governs its sports betting and casino operations and sets standards for player fund security and fair play."
      }
    }
  ]
}
</script>
"""

html = render_page(
    slug='sports/football',
    title='1win football betting: 40,000+ markets with XLBONUS',
    description='Bet on EPL, Champions League, World Cup and 40,000+ football markets at 1win. Claim promo code XLBONUS on your first deposit. Curaçao 8048/JAZ licensed.',
    h1='1win football betting: 40,000+ markets worldwide',
    breadcrumbs=[('Home', '/en/'), ('Sports', '/en/sports/'), ('Football', None)],
    main_html=football_main,
    extra_schema=football_faq_schema,
)
open('en/sports/football.html', 'w').write(html)
print('football.html written')

# ─────────────────────────────────────────────────────────────────────────────
# 2. CRICKET
# ─────────────────────────────────────────────────────────────────────────────

cricket_main = """
<section class="lede">
  <p>1win is the betting platform of choice for cricket fans across South Asia, the Caribbean and beyond, offering access to 40,000+ markets that span the IPL, T20 World Cup, ODI World Cup and Test cricket under a Curaçao 8048/JAZ licence. Whether you are tracking Rohit Sharma's opening partnership in Mumbai or following a tense Ashes series at Lord's, 1win prices every delivery's outcome in real time. Use promo code <span class="code-highlight">XLBONUS</span> when you register to get a boosted first deposit and start your cricket betting straight away.</p>
</section>

<section class="key-facts">
  <h2>Hero stats</h2>
  <table class="facts-table">
    <tr><th>Markets available</th><td>40,000+</td></tr>
    <tr><th>Welcome bonus code</th><td><span class="code-highlight">XLBONUS</span></td></tr>
    <tr><th>In-play streaming</th><td>Select matches live</td></tr>
    <tr><th>Cashout</th><td>24/7 full and partial</td></tr>
    <tr><th>Licence</th><td>Curaçao 8048/JAZ</td></tr>
  </table>
</section>

<section class="competitions">
  <h2>Tournaments and competitions covered</h2>
  <p>Cricket at 1win spans all three formats and every major competition on the international and domestic calendar.</p>
  <ul>
    <li><strong>Indian Premier League (IPL)</strong> - The IPL is the biggest franchise cricket tournament on the planet, running March to May across ten cities in India. Mumbai Indians, Chennai Super Kings and Royal Challengers Bengaluru command the deepest betting markets on 1win, with every ball available for in-play wagering. Rohit Sharma's explosive starts at the top of the order and Jasprit Bumrah's death-overs bowling are key player prop targets.</li>
    <li><strong>ICC T20 World Cup</strong> - The flagship global T20 competition takes place every two years. India's 2024 triumph under Rohit Sharma at Barbados gave the tournament a new narrative entering the 2026 cycle. 1win lists full outright markets from the moment squads are announced.</li>
    <li><strong>ICC ODI World Cup</strong> - The 50-over World Cup remains cricket's most prestigious team event. The 2023 edition in India drew record global betting volumes. 1win covers group stages, Super 6 rounds and knockout fixtures with deep market selection.</li>
    <li><strong>Test cricket</strong> - The five-day format demands patience and rewards research. 1win covers England, Australia, India, Pakistan, South Africa, New Zealand, West Indies, Sri Lanka and Bangladesh in their bilateral series. The Ashes between England and Australia attracts the longest list of outright and series markets on the platform.</li>
    <li><strong>Big Bash League (BBL)</strong> - Australia's domestic T20 competition fills the December-January window. Eight franchises from Sydney, Melbourne, Brisbane, Adelaide, Perth and Hobart compete. The BBL is a popular in-play betting market during the Southern Hemisphere summer.</li>
    <li><strong>Pakistan Super League (PSL)</strong> - The PSL runs February to March and represents the leading T20 franchise competition in Pakistan. Lahore Qalandars and Karachi Kings generate the highest market depth on 1win.</li>
    <li><strong>Caribbean Premier League (CPL)</strong> - The West Indian franchise T20 tournament runs August to September. Trinbago Knight Riders are the competition's most decorated side and attract strong outright betting interest.</li>
    <li><strong>Bangladesh Premier League (BPL)</strong> - The BPL runs January to February and provides competitive T20 cricket from Dhaka, Chattogram and Sylhet. Growing market depth on 1win reflects the expanding South Asian betting audience.</li>
    <li><strong>The Hundred</strong> - England's 100-ball competition, launched in 2021, has attracted leading international players and a large television audience. Oval Invincibles and Manchester Originals are among the franchises regularly priced for outright and match markets on 1win.</li>
    <li><strong>County cricket (England)</strong> - The County Championship provides domestic Test-match cricket from April to September. Division One fixtures between Surrey, Nottinghamshire and Yorkshire feature handicap and result markets for the dedicated county fan.</li>
  </ul>
</section>

<section class="markets">
  <h2>Most popular cricket betting markets</h2>
  <ul>
    <li><strong>Match winner</strong> - Bet on which side wins the match. In T20 format, odds shift dramatically in-play as powerplay overs progress.</li>
    <li><strong>Tournament outright</strong> - Back a team to win the IPL, World Cup or any league before or during the tournament for the best available odds.</li>
    <li><strong>Top batter</strong> - Predict which player will score the most runs in the match or across the tournament. In the IPL, Virat Kohli and Suryakumar Yadav consistently attract the most wagers in this market.</li>
    <li><strong>Top bowler</strong> - Back Jasprit Bumrah, Shaheen Afridi or another frontline bowler to take the most wickets in a match or series.</li>
    <li><strong>Total runs in the match</strong> - Bet over or under a stated line for combined first-innings (or total match) runs. Particularly popular in T20 where 160-180 totals are common benchmarks.</li>
    <li><strong>Fall of next wicket (FONW)</strong> - A ball-by-ball in-play market: at what score will the next wicket fall? One of the most reactive live cricket markets on 1win.</li>
    <li><strong>Head-to-head (H2H)</strong> - Which of two specified batters will score more runs in the match? Available for most IPL and international fixtures.</li>
    <li><strong>Method of dismissal</strong> - Will the next wicket be caught, bowled, LBW, run out or stumped? A specialist market that rewards those who know the bowling matchups.</li>
    <li><strong>Player to score a half-century or century</strong> - Backed by many accumulator builders, this market covers individual batting milestones.</li>
  </ul>
</section>

<section class="inplay">
  <h2>In-play and live cricket betting</h2>
  <p>Cricket is uniquely suited to live betting because the game offers natural breaks between overs, innings changes and drinks intervals where odds reset and new positions open up. 1win's in-play cricket platform refreshes pricing after every ball in T20 and ODI formats, giving you opportunities to react to a dropped catch, a batter's acceleration in the final five overs, or a bowling change that upends the expected run rate.</p>
  <p>Pre-match betting works well when you have done the research: pitch reports, team announcements, head-to-head records and weather forecasts all feed into a well-structured outright or match-winner bet placed the evening before. In-play betting, by contrast, rewards real-time reading. In an IPL match where a team has lost two wickets in the powerplay, the live over/under line for the first ten overs will compress sharply, offering value if you believe the remaining set batter can accelerate. Similarly, when a spinner takes two wickets in an over during a Test, in-play odds on an innings result can swing 20-30 points in seconds.</p>
  <p>Select IPL and international fixtures are available with live streaming direct in the 1win platform, so you can watch and bet from the same screen.</p>
</section>

<section class="cashout">
  <h2>Cashout and bet builder</h2>
  <p>1win's cashout function is available on cricket bets throughout matches and tournaments. During an IPL final, if your pre-match outright selection is batting second and chasing comfortably, the cashout value will reflect the favourable position before the match concludes. Partial cashout lets you ring-fence a guaranteed return while keeping a live stake active, giving you the best of both outcomes if the chase gets tight in the final over.</p>
  <p>The bet builder is excellent for cricket: combine a team to win with the top batter market and an over/under total into a single slip for a boosted combined price. Bet builders are available for featured IPL and international matches, with more fixtures being added as the offering expands.</p>
</section>

<section class="mobile">
  <h2>Mobile cricket betting with the 1win app</h2>
  <p>The 1win app is the primary tool for cricket betting on the move. Download the Android APK from <a href="/en/app">1win.codes/en/app</a> or get the iOS version from the App Store. The app replicates the full desktop experience including in-play ball-by-ball markets, streaming for eligible fixtures and push notifications when bets settle. UPI deposits and withdrawals are fully supported in the app, making it ideal for Indian bettors who want to fund and cashout without leaving the mobile interface.</p>
</section>

<section class="how-to">
  <h2>How to start betting on cricket at 1win</h2>
  <ol>
    <li><strong>Register your account</strong> - Go to the registration page and complete the quick sign-up form with your name, email and preferred currency.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> - Add XLBONUS in the promo code field before confirming registration to activate your first-deposit bonus.</li>
    <li><strong>Deposit funds</strong> - 1win accepts UPI, cards, e-wallets, USDT and other methods. Your bonus funds appear after the deposit clears.</li>
    <li><strong>Open cricket markets</strong> - Go to Sports, select Cricket, then pick your competition from the A-Z menu or the featured matches carousel.</li>
    <li><strong>Place your bet</strong> - Select odds, enter your stake in the bet slip, confirm and you are live. Track your bet via My Bets or the in-play tracker.</li>
  </ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>Does 1win cover IPL cricket betting?</summary>
    <p>Yes. 1win offers full market coverage for every IPL match, including in-play ball-by-ball markets, outright winner, top batter, top bowler and many more across all ten franchise fixtures.</p>
  </details>
  <details>
    <summary>Can I bet on Test cricket at 1win?</summary>
    <p>Yes. 1win covers all major Test series including the Ashes, India vs Pakistan, and home series for all ICC Full Member nations. Markets include match result, series winner, top run-scorer and innings betting.</p>
  </details>
  <details>
    <summary>What is the fall of next wicket market?</summary>
    <p>Fall of next wicket (FONW) is an in-play market where you bet on the run total at which the next wicket will fall. It updates ball-by-ball and is one of the most engaging live cricket markets on 1win.</p>
  </details>
  <details>
    <summary>Does 1win support UPI deposits for cricket betting?</summary>
    <p>Yes. 1win accepts UPI payments for deposits and withdrawals, making it straightforward for Indian players to fund their accounts and start betting on the IPL or any other cricket competition.</p>
  </details>
  <details>
    <summary>What promo code should I use for cricket betting?</summary>
    <p>Use promo code XLBONUS at registration to claim 1win's welcome bonus on your first deposit. The bonus applies to sports betting including cricket.</p>
  </details>
  <details>
    <summary>Is 1win licensed for cricket betting?</summary>
    <p>1win operates under a Curaçao 8048/JAZ licence, providing a regulated environment for all sports betting including cricket markets across IPL, T20 World Cup, ODI World Cup and Test cricket.</p>
  </details>
</section>
"""

cricket_faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does 1win cover IPL cricket betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win offers full market coverage for every IPL match, including in-play ball-by-ball markets, outright winner, top batter, top bowler and many more across all ten franchise fixtures."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bet on Test cricket at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win covers all major Test series including the Ashes, India vs Pakistan, and home series for all ICC Full Member nations. Markets include match result, series winner, top run-scorer and innings betting."
      }
    },
    {
      "@type": "Question",
      "name": "What is the fall of next wicket market?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Fall of next wicket (FONW) is an in-play market where you bet on the run total at which the next wicket will fall. It updates ball-by-ball and is one of the most engaging live cricket markets on 1win."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win support UPI deposits for cricket betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win accepts UPI payments for deposits and withdrawals, making it straightforward for Indian players to fund their accounts and start betting on the IPL or any other cricket competition."
      }
    },
    {
      "@type": "Question",
      "name": "What promo code should I use for cricket betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use promo code XLBONUS at registration to claim 1win's welcome bonus on your first deposit. The bonus applies to sports betting including cricket."
      }
    },
    {
      "@type": "Question",
      "name": "Is 1win licensed for cricket betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win operates under a Curacao 8048/JAZ licence, providing a regulated environment for all sports betting including cricket markets across IPL, T20 World Cup, ODI World Cup and Test cricket."
      }
    }
  ]
}
</script>
"""

html = render_page(
    slug='sports/cricket',
    title='1win cricket betting: IPL, T20 World Cup and XLBONUS',
    description='Bet on IPL, T20 World Cup, ODI World Cup and Test cricket at 1win with 40,000+ markets. Use promo code XLBONUS for your welcome bonus. Curaçao 8048/JAZ licensed.',
    h1='1win cricket betting: IPL, T20 World Cup and every format covered',
    breadcrumbs=[('Home', '/en/'), ('Sports', '/en/sports/'), ('Cricket', None)],
    main_html=cricket_main,
    extra_schema=cricket_faq_schema,
)
open('en/sports/cricket.html', 'w').write(html)
print('cricket.html written')

# ─────────────────────────────────────────────────────────────────────────────
# 3. TENNIS
# ─────────────────────────────────────────────────────────────────────────────

tennis_main = """
<section class="lede">
  <p>Tennis runs 52 weeks a year across every surface, and 1win prices every ATP and WTA tour match from first-round qualifiers to Grand Slam finals, offering 40,000+ markets on a platform licensed by Curaçao 8048/JAZ. Novak Djokovic pursuing a record 25th Grand Slam title at Wimbledon, Jannik Sinner defending his Australian Open crown or Iga Swiatek's pursuit of a sixth Roland Garros title: all of these are live-bet opportunities at 1win. Register with promo code <span class="code-highlight">XLBONUS</span> to unlock your welcome bonus and start backing the tour.</p>
</section>

<section class="key-facts">
  <h2>Hero stats</h2>
  <table class="facts-table">
    <tr><th>Markets available</th><td>40,000+</td></tr>
    <tr><th>Welcome bonus code</th><td><span class="code-highlight">XLBONUS</span></td></tr>
    <tr><th>In-play streaming</th><td>Select matches live</td></tr>
    <tr><th>Cashout</th><td>24/7 full and partial</td></tr>
    <tr><th>Licence</th><td>Curaçao 8048/JAZ</td></tr>
  </table>
</section>

<section class="competitions">
  <h2>Tournaments and competitions covered</h2>
  <p>1win follows professional tennis from the first ATP250 of January through to the Davis Cup and BJK Cup finals in November.</p>
  <ul>
    <li><strong>Australian Open</strong> - The first Grand Slam of the year, played on hard courts at Melbourne Park in January. Jannik Sinner won the 2024 and 2025 editions, cementing his status as the season-opening favourite heading into 2026. 1win lists full draw markets from the moment the bracket is released.</li>
    <li><strong>Roland Garros (French Open)</strong> - Clay's most prestigious event runs May-June in Paris. Rafael Nadal's 14 titles shaped the narrative for a generation; now Carlos Alcaraz and Sinner contest the clay-court throne. Iga Swiatek's record on clay makes her the consistent outright selection for the women's draw.</li>
    <li><strong>Wimbledon</strong> - The grass-court major played at the All England Club in late June and July is the sport's most iconic tournament. Djokovic's seven titles and the women's draw volatility on fast grass create a unique betting environment. 1win covers every match from qualifying through the final.</li>
    <li><strong>US Open</strong> - New York's hard-court major in August-September closes the Grand Slam calendar. The open draw and the physical demands of the American summer produce frequent upsets, rewarding in-play bettors who track fitness and serving percentages in real time.</li>
    <li><strong>ATP Masters 1000</strong> - Nine elite events sit directly below the Slams: Indian Wells, Miami, Monte Carlo, Madrid, Rome, Canada, Cincinnati, Shanghai and Paris-Bercy. Masters titles count heavily in the race for the ATP Finals and attract the strongest fields outside the four Slams.</li>
    <li><strong>ATP Finals</strong> - The season-ending championship in Turin brings together the eight highest-ranked singles and doubles players of the year. A round-robin group stage followed by knockouts provides an unusual betting format that 1win covers comprehensively.</li>
    <li><strong>WTA Tour</strong> - Every WTA 1000 and WTA 500 tournament is listed on 1win alongside the Slams. Aryna Sabalenka, Coco Gauff and Swiatek lead the standings through the 2025-26 cycle.</li>
    <li><strong>ATP Challenger and ITF</strong> - Lower-tier events give punters a chance to identify emerging talent before they break into the top 50. 1win lists match-winner markets for Challenger fixtures on most circuits.</li>
    <li><strong>Davis Cup</strong> - The 100-year-old national team competition now uses a Finals format in Malaga each November. Teams of three singles players and a doubles pair compete across ties, with outright and tie-winner markets available.</li>
    <li><strong>Billie Jean King Cup (BJK Cup)</strong> - The women's equivalent of the Davis Cup, also using a Finals format. 1win covers the qualifying rounds and the Finals in full.</li>
  </ul>
</section>

<section class="markets">
  <h2>Most popular tennis betting markets</h2>
  <ul>
    <li><strong>Match winner</strong> - Back either player to win the match. The foundation market, available from qualifying to finals on every tour event.</li>
    <li><strong>Set winner</strong> - Bet on which player wins a specific set (Set 1, Set 2, etc.) rather than the overall match. Useful in-play as momentum shifts after a tight set.</li>
    <li><strong>Set betting (correct set score)</strong> - Predict the exact scoreline in sets: 2-0, 2-1 for best-of-three; 3-0, 3-1, 3-2 for Grand Slams. Enhanced odds reward precise forecasting.</li>
    <li><strong>Total games (over/under)</strong> - Will the total number of games played exceed or fall below a stated line? A competitive match between Djokovic and Alcaraz often goes deep into a deciding set, pushing totals above 40 games.</li>
    <li><strong>Total sets</strong> - Will the match be decided in 2 sets or go to 3 (best-of-three), or reach 4 or 5 in a Grand Slam? Pre-match form data on sets won drives this market.</li>
    <li><strong>Handicap (game handicap)</strong> - One player is given a game advantage or disadvantage. If Djokovic is -4.5 games, he needs to win by 5 or more net games across the match.</li>
    <li><strong>To win first set and match</strong> - A double-result combination popular with accumulators. Taking the more likely set winner and match winner at combined odds adds value versus two separate markets.</li>
  </ul>
</section>

<section class="inplay">
  <h2>In-play and live tennis betting</h2>
  <p>Tennis is one of the best sports for live betting because the score resets at the start of every game, creating constant odds movement. 1win's in-play tennis interface updates within seconds of each point, letting you react to a break of serve, a mid-match injury timeout or a sudden shift in momentum that is visible before the bookmaker recalibrates fully.</p>
  <p>Pre-match research is essential: surface win rate, head-to-head record, recent form on the tour and serving statistics (first serve percentage, aces per match, double faults) all inform a well-placed pre-match selection. In-play betting, however, is where tennis delivers its greatest edge. When Djokovic loses the first set at Wimbledon, live odds on his recovery often over-correct relative to his career comeback rate, presenting value for the in-play bettor who knows his historical second-set records.</p>
  <p>Key in-play markets at 1win include: next game winner, current set winner, next set score, number of aces in the next game and whether the current game will go to deuce. Select ATP and WTA matches are live-streamed on the platform.</p>
</section>

<section class="cashout">
  <h2>Cashout and bet builder</h2>
  <p>1win's cashout is highly effective in tennis because a single break of serve can swing the value of an active bet significantly. If you have backed a player to win and they lead 5-2 in the final set, cashout locks in near-full value before the match concludes. Partial cashout is equally useful: secure half the return after a two-set lead while leaving the remainder live in case the opponent breaks back unexpectedly.</p>
  <p>The bet builder lets you combine markets from the same match. For a Wimbledon quarter-final you might link: Djokovic to win, total games under 38.5 and Djokovic to win the first set. Combined odds amplify the return from a well-researched single-match analysis.</p>
</section>

<section class="mobile">
  <h2>Mobile tennis betting with the 1win app</h2>
  <p>The 1win app covers the full ATP and WTA schedule on Android and iOS. Live score updates and in-play odds refresh continuously, giving you the same real-time edge on mobile as on desktop. Download the Android APK from <a href="/en/app">1win.codes/en/app</a>. Push notifications alert you when set scores change, giving you a prompt to check in-play odds without having to monitor the app continuously through a long match.</p>
</section>

<section class="how-to">
  <h2>How to start betting on tennis at 1win</h2>
  <ol>
    <li><strong>Create your account</strong> - Complete the registration form on 1win.codes with your email, name and password. The sign-up takes under two minutes.</li>
    <li><strong>Enter <span class="code-highlight">XLBONUS</span> at registration</strong> - Type XLBONUS in the promo code field to activate your first-deposit welcome bonus.</li>
    <li><strong>Make a deposit</strong> - 1win accepts cards, e-wallets, USDT, UPI and multiple other methods. Funds appear in your balance instantly for most payment types.</li>
    <li><strong>Navigate to Tennis</strong> - Click Sports in the main menu, then select Tennis from the sidebar. Browse by ATP, WTA, Grand Slams or Challenger events.</li>
    <li><strong>Select your market and place your bet</strong> - Click any odds to open the bet slip, enter your stake, confirm and your bet is live. Track it in My Bets.</li>
  </ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>Does 1win cover all four Grand Slams?</summary>
    <p>Yes. 1win provides full market coverage for the Australian Open, Roland Garros, Wimbledon and the US Open, including outright winner, match winner, set betting, game handicap and in-play options from qualifying through to the final.</p>
  </details>
  <details>
    <summary>What tennis markets are available at 1win?</summary>
    <p>1win offers match winner, set winner, set betting, total games over/under, total sets, game handicap and in-play point-by-point markets on ATP, WTA, Challenger and ITF fixtures.</p>
  </details>
  <details>
    <summary>Can I bet on tennis in play at 1win?</summary>
    <p>Yes. In-play tennis markets at 1win update after every point, covering next game winner, set winner, total games and more. Select matches also carry live streaming within the platform.</p>
  </details>
  <details>
    <summary>How does the cashout work on tennis bets?</summary>
    <p>Cashout is available 24/7 on eligible tennis bets. You can take full cashout to close a position before the match ends, or use partial cashout to secure part of the return while leaving a stake live on the outcome.</p>
  </details>
  <details>
    <summary>Does 1win cover Davis Cup and Billie Jean King Cup?</summary>
    <p>Yes. Both the Davis Cup Finals and the BJK Cup Finals are fully listed on 1win, with outright winner, tie winner and individual match markets available throughout the competition.</p>
  </details>
  <details>
    <summary>What is the XLBONUS code for tennis betting?</summary>
    <p>XLBONUS is the welcome promo code for new 1win players. Enter it at registration before your first deposit to claim the current welcome bonus, which can be used across tennis and all other sports on the platform.</p>
  </details>
</section>
"""

tennis_faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does 1win cover all four Grand Slams?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win provides full market coverage for the Australian Open, Roland Garros, Wimbledon and the US Open, including outright winner, match winner, set betting, game handicap and in-play options from qualifying through to the final."
      }
    },
    {
      "@type": "Question",
      "name": "What tennis markets are available at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win offers match winner, set winner, set betting, total games over/under, total sets, game handicap and in-play point-by-point markets on ATP, WTA, Challenger and ITF fixtures."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bet on tennis in play at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. In-play tennis markets at 1win update after every point, covering next game winner, set winner, total games and more. Select matches also carry live streaming within the platform."
      }
    },
    {
      "@type": "Question",
      "name": "How does the cashout work on tennis bets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cashout is available 24/7 on eligible tennis bets. You can take full cashout to close a position before the match ends, or use partial cashout to secure part of the return while leaving a stake live on the outcome."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win cover Davis Cup and Billie Jean King Cup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Both the Davis Cup Finals and the BJK Cup Finals are fully listed on 1win, with outright winner, tie winner and individual match markets available throughout the competition."
      }
    },
    {
      "@type": "Question",
      "name": "What is the XLBONUS code for tennis betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "XLBONUS is the welcome promo code for new 1win players. Enter it at registration before your first deposit to claim the current welcome bonus, which can be used across tennis and all other sports on the platform."
      }
    }
  ]
}
</script>
"""

html = render_page(
    slug='sports/tennis',
    title='1win tennis betting: ATP, WTA and Grand Slams with XLBONUS',
    description='Bet on all four Grand Slams, ATP Masters 1000, WTA Tour and Challenger events at 1win. Claim promo code XLBONUS on your first deposit. Curaçao 8048/JAZ licensed.',
    h1='1win tennis betting: Grand Slams, ATP, WTA and more',
    breadcrumbs=[('Home', '/en/'), ('Sports', '/en/sports/'), ('Tennis', None)],
    main_html=tennis_main,
    extra_schema=tennis_faq_schema,
)
open('en/sports/tennis.html', 'w').write(html)
print('tennis.html written')

# ─────────────────────────────────────────────────────────────────────────────
# 4. BASKETBALL
# ─────────────────────────────────────────────────────────────────────────────

basketball_main = """
<section class="lede">
  <p>Basketball at 1win spans the full global circuit from the NBA to the EuroLeague, FIBA World Cup and beyond, with 40,000+ markets available on a platform licensed by Curaçao 8048/JAZ. The Los Angeles Lakers chasing a playoff berth under a new head coach, Real Madrid marching through the EuroLeague Final Four, or Australia's NBL competing during the North American off-season: every competition is priced in real time at 1win. Register now with promo code <span class="code-highlight">XLBONUS</span> to claim your welcome bonus and get on the court.</p>
</section>

<section class="key-facts">
  <h2>Hero stats</h2>
  <table class="facts-table">
    <tr><th>Markets available</th><td>40,000+</td></tr>
    <tr><th>Welcome bonus code</th><td><span class="code-highlight">XLBONUS</span></td></tr>
    <tr><th>In-play streaming</th><td>Select games live</td></tr>
    <tr><th>Cashout</th><td>24/7 full and partial</td></tr>
    <tr><th>Licence</th><td>Curaçao 8048/JAZ</td></tr>
  </table>
</section>

<section class="competitions">
  <h2>Tournaments and competitions covered</h2>
  <p>1win covers professional basketball across five continents, giving bettors a live fixture at almost any hour of the day.</p>
  <ul>
    <li><strong>NBA</strong> - The premier basketball league in the world runs October to June. The Boston Celtics, defending 2024 champions, face perennial title contenders in the Golden State Warriors, Phoenix Suns and Oklahoma City Thunder. The Los Angeles Lakers and their roster built around LeBron James and Anthony Davis attract the highest individual game betting volumes on 1win. Every regular-season game, playoff series and the Finals are fully priced.</li>
    <li><strong>EuroLeague</strong> - Europe's top club competition brings together 18 teams from 10 countries across a 34-game regular season before playoff series and a Final Four weekend. Real Madrid's record eight EuroLeague titles make them the default favourite each season. Fenerbahce, Olympiacos and CSKA Moscow (when eligible) are among the historical powers sharing market depth on 1win.</li>
    <li><strong>NCAA March Madness</strong> - The US college basketball tournament runs across three weekends in March and April, producing iconic upsets that drive enormous live-betting engagement. 1win lists all 63 bracket games from the Round of 64 through to the national championship.</li>
    <li><strong>FIBA Basketball World Cup</strong> - The 32-team global championship held every four years. The 2023 edition in the Philippines delivered a breakthrough for Germany, who claimed their first world title. The 2027 edition begins a new betting cycle with outright markets opening the moment the host nation is confirmed.</li>
    <li><strong>Olympic Basketball</strong> - The 12-team men's and women's tournament at every Summer Olympics is a standout betting event. The USA men's team returned to gold in Paris 2024, with Serbia and France reaching the final. 1win covers full group stage and knockout markets.</li>
    <li><strong>ACB Liga Endesa (Spain)</strong> - The Spanish top flight is one of Europe's strongest domestic leagues outside the EuroLeague. Barcelona and Real Madrid's domestic rivalry mirrors their football counterpart, drawing consistent cross-sport betting audiences on 1win.</li>
    <li><strong>Serie A (Italy)</strong> - Italian basketball features clubs like Olimpia Milano, Virtus Bologna and Brescia Pallacanestro, with Olimpia Milano's dual EuroLeague and domestic commitments making them the most covered Italian team on the platform.</li>
    <li><strong>Turkish Super League (BSL)</strong> - Turkey's domestic league feeds the EuroLeague with clubs like Fenerbahce Beko, Anadolu Efes and Galatasaray. The Istanbul derbies attract significant in-play betting volumes on 1win.</li>
    <li><strong>NBL Australia</strong> - The National Basketball League runs October to February, providing off-season basketball for NBA fans. The Perth Wildcats, Melbourne United and Sydney Kings are the most prominent teams on the platform.</li>
  </ul>
</section>

<section class="markets">
  <h2>Most popular basketball betting markets</h2>
  <ul>
    <li><strong>Moneyline (match winner)</strong> - Straight bet on which team wins the game. The simplest and most popular basketball market on 1win.</li>
    <li><strong>Point spread (handicap)</strong> - The favourite must win by more than the spread; the underdog must lose by fewer points than the spread, or win outright. The spread levels the field and keeps odds close to even on both sides.</li>
    <li><strong>Total points (over/under)</strong> - Bet whether combined final score will exceed or fall below a stated total. NBA totals regularly sit in the 220-230 point range for high-pace teams.</li>
    <li><strong>Quarter and half betting</strong> - Bet on the result or total for a specific quarter or half. NBA first quarters are popular because starting five lineups are known and substitution patterns are predictable.</li>
    <li><strong>Player props</strong> - Back LeBron James to score over 25.5 points, Anthony Davis to grab 12+ rebounds, or any listed player for points, rebounds, assists, three-pointers or steals. NBA player props are the fastest-growing segment of basketball betting on 1win.</li>
    <li><strong>Series winner (playoffs)</strong> - NBA and EuroLeague playoff series generate series-winner markets where you bet on the team that wins the best-of-seven or best-of-five format. Available from the start of each series.</li>
    <li><strong>Tournament outright</strong> - Back a team to win the NBA Finals, EuroLeague, FIBA World Cup or any other championship before or during the competition.</li>
  </ul>
</section>

<section class="inplay">
  <h2>In-play and live basketball betting</h2>
  <p>Basketball is a natural in-play sport. With scoring every 30 seconds on average in the NBA, live odds shift constantly and offer rapid-fire opportunities. 1win's live basketball interface updates quarter scores, individual player stats and team totals in real time, giving you a complete picture before placing each in-play bet.</p>
  <p>Pre-match research guides your initial position: rest advantage, back-to-back game fatigue, injury reports released 90 minutes before tip-off, and pace-of-play statistics are all relevant. In-play, the picture evolves quickly. If a starter exits early with a foul problem in the first quarter, the in-play spread often adjusts slower than the tactical reality warrants, creating short windows of value for those monitoring the game closely. Similarly, when an NBA team falls 15 points behind in the first half, live totals for the remaining half frequently overprice both sides because analysts apply the first-half scoring rate to a game that will inevitably feature defensive adjustments.</p>
  <p>1win offers live streaming on select NBA and EuroLeague games, allowing you to watch and bet from the same screen without switching between apps.</p>
</section>

<section class="cashout">
  <h2>Cashout and bet builder</h2>
  <p>1win's cashout is available 24/7 on eligible basketball bets including pre-match and in-play selections. If you have backed a team on the spread and they lead by 12 points heading into the fourth quarter, a full cashout secures your position before any late-game comeback materialises. Partial cashout works well for NBA playoff series bets: if you backed a team to win a series at 3-0 up, a partial cashout covers the series return while leaving a live stake for the unlikely event of a reversal.</p>
  <p>The bet builder combines multiple markets from the same game into one slip. For a Lakers playoff fixture you might link: Lakers to win, LeBron James over 26.5 points and total game points over 218.5. The combined odds reward careful research across three closely correlated outcomes.</p>
</section>

<section class="mobile">
  <h2>Mobile basketball betting with the 1win app</h2>
  <p>The 1win mobile app delivers the full basketball sportsbook on Android and iOS. NBA night games start late for European bettors, making the mobile app essential for accessing in-play markets and live streams from anywhere. Download the Android APK from <a href="/en/app">1win.codes/en/app</a> or install via the App Store. Push notifications alert you to bet settlements, quarter scores and cashout opportunities the moment they arise.</p>
</section>

<section class="how-to">
  <h2>How to start betting on basketball at 1win</h2>
  <ol>
    <li><strong>Register your account</strong> - Go to the 1win registration page and enter your details. The process is complete in under two minutes.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> - Add XLBONUS to the promo field at sign-up to activate your welcome bonus on the first deposit.</li>
    <li><strong>Deposit funds</strong> - Choose from cards, e-wallets, USDT, UPI and other payment methods. Your bonus is credited automatically after the deposit.</li>
    <li><strong>Open basketball markets</strong> - Select Sports from the main menu and choose Basketball. Filter by NBA, EuroLeague, NCAA or any other league.</li>
    <li><strong>Place your first bet</strong> - Click the odds you want, enter a stake, confirm the bet and track it through My Bets or the in-play dashboard.</li>
  </ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>Does 1win cover NBA betting?</summary>
    <p>Yes. 1win covers all 82 regular-season NBA games per team plus the full playoff bracket and NBA Finals, with markets including moneyline, spread, totals, quarter/half betting and player props.</p>
  </details>
  <details>
    <summary>What is point spread betting in basketball?</summary>
    <p>A point spread is a handicap applied to balance a game between two unequal teams. The favourite must win by more than the spread for a spread bet on them to win; the underdog must lose by fewer points than the spread, or win outright.</p>
  </details>
  <details>
    <summary>Can I bet on player props in the NBA at 1win?</summary>
    <p>Yes. 1win offers player prop markets including points, rebounds, assists, three-pointers and steals for all starting and bench players in listed NBA games. Props are available pre-match and in-play.</p>
  </details>
  <details>
    <summary>Does 1win cover the EuroLeague?</summary>
    <p>Yes. All 18 EuroLeague regular-season games per team, plus the playoff series and Final Four, are fully listed on 1win with match winner, spread, totals and outright markets.</p>
  </details>
  <details>
    <summary>Is cashout available on basketball bets?</summary>
    <p>Yes. Full and partial cashout is available 24/7 on eligible basketball bets at 1win, covering both pre-match and in-play selections across NBA, EuroLeague and other listed competitions.</p>
  </details>
  <details>
    <summary>What promo code should I use for basketball betting at 1win?</summary>
    <p>Use XLBONUS at registration to receive 1win's welcome bonus on your first deposit. The bonus is valid across all sports betting including basketball markets.</p>
  </details>
</section>
"""

basketball_faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does 1win cover NBA betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win covers all 82 regular-season NBA games per team plus the full playoff bracket and NBA Finals, with markets including moneyline, spread, totals, quarter/half betting and player props."
      }
    },
    {
      "@type": "Question",
      "name": "What is point spread betting in basketball?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A point spread is a handicap applied to balance a game between two unequal teams. The favourite must win by more than the spread for a spread bet on them to win; the underdog must lose by fewer points than the spread, or win outright."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bet on player props in the NBA at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win offers player prop markets including points, rebounds, assists, three-pointers and steals for all starting and bench players in listed NBA games. Props are available pre-match and in-play."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win cover the EuroLeague?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. All 18 EuroLeague regular-season games per team, plus the playoff series and Final Four, are fully listed on 1win with match winner, spread, totals and outright markets."
      }
    },
    {
      "@type": "Question",
      "name": "Is cashout available on basketball bets?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Full and partial cashout is available 24/7 on eligible basketball bets at 1win, covering both pre-match and in-play selections across NBA, EuroLeague and other listed competitions."
      }
    },
    {
      "@type": "Question",
      "name": "What promo code should I use for basketball betting at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use XLBONUS at registration to receive 1win's welcome bonus on your first deposit. The bonus is valid across all sports betting including basketball markets."
      }
    }
  ]
}
</script>
"""

html = render_page(
    slug='sports/basketball',
    title='1win basketball betting: NBA, EuroLeague and XLBONUS',
    description='Bet on NBA, EuroLeague, NCAA and FIBA basketball at 1win with 40,000+ markets. Enter promo code XLBONUS at registration. Curaçao 8048/JAZ licensed sportsbook.',
    h1='1win basketball betting: NBA, EuroLeague and global hoops',
    breadcrumbs=[('Home', '/en/'), ('Sports', '/en/sports/'), ('Basketball', None)],
    main_html=basketball_main,
    extra_schema=basketball_faq_schema,
)
open('en/sports/basketball.html', 'w').write(html)
print('basketball.html written')

# ─────────────────────────────────────────────────────────────────────────────
# 5. ESPORTS
# ─────────────────────────────────────────────────────────────────────────────

esports_main = """
<section class="lede">
  <p>1win is one of the most comprehensive esports betting platforms available, covering CS2, Dota 2, League of Legends, Valorant, Rainbow Six Siege and Mobile Legends across 40,000+ markets under a Curaçao 8048/JAZ licence. From Natus Vincere facing Team Spirit in a CS2 Major semi-final to Team Liquid pushing for a Valorant Champions title, every tier of competitive play is priced and available for in-play wagering at 1win. Register with promo code <span class="code-highlight">XLBONUS</span> to get your welcome bonus and start betting on the games you know inside out.</p>
</section>

<section class="key-facts">
  <h2>Hero stats</h2>
  <table class="facts-table">
    <tr><th>Markets available</th><td>40,000+</td></tr>
    <tr><th>Welcome bonus code</th><td><span class="code-highlight">XLBONUS</span></td></tr>
    <tr><th>In-play streaming</th><td>Select matches live via Twitch/YouTube integration</td></tr>
    <tr><th>Cashout</th><td>24/7 full and partial</td></tr>
    <tr><th>Licence</th><td>Curaçao 8048/JAZ</td></tr>
  </table>
</section>

<section class="competitions">
  <h2>Tournaments and competitions covered</h2>
  <p>1win follows the esports calendar from regional qualifiers through to the biggest global championship events, covering each title's most prestigious tournaments.</p>
  <ul>
    <li><strong>CS2 Majors</strong> - Valve's flagship CS2 Majors are the pinnacle of Counter-Strike. The Copenhagen Major 2024 drew record viewership, with Natus Vincere (NaVi) and FaZe Clan producing the most-bet matches on 1win. The 2025-26 cycle continues with Majors in multiple regions. 1win lists full tournament outright, stage-winner and match-level markets from the qualifier stage.</li>
    <li><strong>ESL Pro League (CS2)</strong> - ESL Pro League Season runs twice yearly and is the leading third-party CS2 league. Sixteen teams across two conferences compete for prize pools exceeding $1,000,000. Team Vitality, Heroic and G2 Esports are the most bet teams on 1win within the league's group stage and playoffs.</li>
    <li><strong>IEM (Intel Extreme Masters)</strong> - IEM Katowice, IEM Cologne and IEM Rio are marquee CS2 events with some of the highest live-betting volumes in esports. 1win carries full in-play map-by-map markets throughout these events.</li>
    <li><strong>The International (Dota 2)</strong> - Valve's annual Dota 2 World Championship is one of the largest prize pools in esports history. Team Spirit's back-to-back titles in 2021 and 2023 established Eastern European dominance, while Chinese and Southeast Asian teams push back each cycle. 1win covers group stage, main event and grand final with deep market selection.</li>
    <li><strong>Dota Pro Circuit (DPC)</strong> - Regional Dota 2 leagues across Europe, North America, Southeast Asia, China, South America and CIS feed into Major events. 1win lists DPC regional results and Majors as part of its year-round Dota 2 coverage.</li>
    <li><strong>League of Legends Worlds (LoL)</strong> - Riot Games' annual World Championship is the largest esport event by peak viewership. T1 led by Faker have won four Worlds titles; South Korea and China dominate the bracket each year. 1win prices all group stage games, knockouts and the grand final at Worlds and at the Mid-Season Invitational (MSI).</li>
    <li><strong>League of Legends regional leagues</strong> - LCK (Korea), LPL (China), LEC (Europe) and LCS (North America) each run split seasons that feed into Worlds. 1win covers all four major regions weekly throughout the year.</li>
    <li><strong>VCT (Valorant Champions Tour)</strong> - Riot's global Valorant ecosystem splits teams across three international leagues (Americas, EMEA, Pacific) with an annual Champions grand final. Sentinels, NRG and Team Liquid Americas have been among the most-bet clubs on 1win. The Champions event in Seoul 2024 attracted strong global wagering interest.</li>
    <li><strong>Rainbow Six Siege (R6)</strong> - Ubisoft's competitive FPS features the Six Invitational as its World Championship. Teams from Europe, North America, Brazil and Asia-Pacific compete with 1win covering all stages of the SI and the regional Six Majors.</li>
    <li><strong>Mobile Legends: Bang Bang (MLBB)</strong> - The M-Series World Championship is the largest MLBB event of the year, drawing massive viewership from Southeast Asia and beyond. Philippine teams like Echo and AP Bren attract the strongest mobile esports betting volumes on 1win.</li>
  </ul>
</section>

<section class="markets">
  <h2>Most popular esports betting markets</h2>
  <ul>
    <li><strong>Match winner</strong> - Back one team to win the series (best-of-1, best-of-3, or best-of-5). The foundation market for all esports titles on 1win.</li>
    <li><strong>Map winner (CS2/Valorant)</strong> - Bet on the winner of a specific map within a series. Because teams have known map preferences, map-winner markets offer strong value for those who study map pools.</li>
    <li><strong>Map handicap</strong> - In a best-of-3 series, backing the underdog at +1.5 maps means they need to win only one map. A common accumulator building block in CS2 and Valorant.</li>
    <li><strong>Total rounds (over/under)</strong> - In CS2, a map runs to 24 rounds maximum in regulation. Betting over or under a stated line (e.g. 25.5 rounds including overtime) rewards knowledge of individual team defensive and offensive styles.</li>
    <li><strong>First map winner</strong> - Which team wins Map 1? Often priced differently from the overall series winner if one side has a clear advantage on their chosen map but is weaker across the full veto.</li>
    <li><strong>Correct score (series)</strong> - Predict the exact series scoreline: 2-0 or 2-1 in a best-of-3, or 3-0, 3-1, 3-2 in a best-of-5. Higher odds reward precise forecasting.</li>
    <li><strong>Tournament outright</strong> - Back NaVi, T1, Team Spirit or any team to win the Major, The International or Worlds before the tournament begins for maximum odds.</li>
  </ul>
</section>

<section class="inplay">
  <h2>In-play and live esports betting</h2>
  <p>Esports delivers some of the most dynamic in-play betting in the industry. In CS2, a single clutch round can swing a map from 12-3 to a close 15-12 scoreline, and 1win's live odds update after every round, reflecting the shifting momentum in real time. A team that wins the pistol round in the second half of a map frequently converts that advantage to a round lead, creating a measurable betting signal for in-play bettors who track these patterns.</p>
  <p>Pre-match analysis should focus on: head-to-head records in the last 30 days, map win rates broken down by side (CT vs T in CS2, attacking vs defending in Valorant), roster stability and patch version because balance changes in Dota 2 and LoL can radically shift which heroes and champions are viable. A newly buffed support hero at The International can make previously reliable picks redundant overnight.</p>
  <p>In-play live streams for many esports events are accessible via linked Twitch and YouTube channels. 1win provides direct links from the bet slip, so you can follow the action without leaving the platform.</p>
</section>

<section class="cashout">
  <h2>Cashout and bet builder</h2>
  <p>Cashout is available on eligible esports bets at 1win, including during live series. If you backed NaVi to win a CS2 Major and they lead 2-0 in a best-of-3 after two dominant map performances, cashout locks in nearly the full return before the third map is played. Partial cashout is useful mid-series: secure a portion of your return after Map 1 while leaving the remainder live on the series result.</p>
  <p>The bet builder for esports lets you link multiple markets from the same match. You might combine: Team Spirit to win, total maps in the series to go over 2.5, and the first map to go over 27.5 rounds. The combined odds amplify the payout from a well-researched Dota 2 or CS2 read.</p>
</section>

<section class="mobile">
  <h2>Mobile esports betting with the 1win app</h2>
  <p>Major esports events often run late into the night across different time zones, making the 1win mobile app essential. The Android APK is available from <a href="/en/app">1win.codes/en/app</a> and the iOS version is on the App Store. All in-play markets are available on mobile, and push notifications keep you updated on round results, map scores and bet settlements without needing to watch the stream continuously.</p>
</section>

<section class="how-to">
  <h2>How to start betting on esports at 1win</h2>
  <ol>
    <li><strong>Create your 1win account</strong> - Go to the registration page and complete sign-up with your email and basic details. Takes under two minutes.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> - Fill in XLBONUS in the promo code field at registration to activate your first-deposit welcome bonus.</li>
    <li><strong>Fund your account</strong> - Deposit via cards, e-wallets, USDT, UPI or other supported methods. Bonus funds appear immediately after the deposit clears.</li>
    <li><strong>Navigate to Esports</strong> - Click Sports, then select Esports from the sidebar. Browse by game title: CS2, Dota 2, LoL, Valorant, Rainbow Six or MLBB.</li>
    <li><strong>Pick your market and bet</strong> - Click any odds to add to your bet slip, set your stake, confirm and track the result live through My Bets or the in-play console.</li>
  </ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>What esports titles does 1win cover?</summary>
    <p>1win covers CS2, Dota 2, League of Legends, Valorant, Rainbow Six Siege and Mobile Legends: Bang Bang, plus additional titles across shooter, MOBA and battle royale genres.</p>
  </details>
  <details>
    <summary>Can I bet on CS2 Majors at 1win?</summary>
    <p>Yes. 1win covers all CS2 Majors from the qualifier stage through the grand final, with outright winner, stage winner, match winner, map winner, round totals and in-play markets throughout each event.</p>
  </details>
  <details>
    <summary>What is a map handicap bet in CS2?</summary>
    <p>A map handicap in CS2 adjusts the number of maps won by each team for betting purposes. Backing the underdog at +1.5 maps in a best-of-3 means your bet wins if they win at least one map, regardless of the overall series result.</p>
  </details>
  <details>
    <summary>Does 1win offer in-play betting on esports?</summary>
    <p>Yes. 1win's in-play esports markets update after every round in CS2 and Valorant and after every game in LoL and Dota 2, with live odds reflecting current scorelines and momentum.</p>
  </details>
  <details>
    <summary>Is cashout available on esports bets at 1win?</summary>
    <p>Yes. Full and partial cashout is available on eligible esports bets, including live in-series betting. You can close or reduce your position at any point during a live series while cashout is offered.</p>
  </details>
  <details>
    <summary>What is the XLBONUS code for esports betting?</summary>
    <p>XLBONUS is the welcome promo code for new 1win registrations. Enter it before your first deposit to unlock the welcome bonus, which can be used on esports and all other sports markets on the platform.</p>
  </details>
</section>
"""

esports_faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What esports titles does 1win cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win covers CS2, Dota 2, League of Legends, Valorant, Rainbow Six Siege and Mobile Legends: Bang Bang, plus additional titles across shooter, MOBA and battle royale genres."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bet on CS2 Majors at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win covers all CS2 Majors from the qualifier stage through the grand final, with outright winner, stage winner, match winner, map winner, round totals and in-play markets throughout each event."
      }
    },
    {
      "@type": "Question",
      "name": "What is a map handicap bet in CS2?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A map handicap in CS2 adjusts the number of maps won by each team for betting purposes. Backing the underdog at +1.5 maps in a best-of-3 means your bet wins if they win at least one map, regardless of the overall series result."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win offer in-play betting on esports?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win's in-play esports markets update after every round in CS2 and Valorant and after every game in LoL and Dota 2, with live odds reflecting current scorelines and momentum."
      }
    },
    {
      "@type": "Question",
      "name": "Is cashout available on esports bets at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Full and partial cashout is available on eligible esports bets, including live in-series betting. You can close or reduce your position at any point during a live series while cashout is offered."
      }
    },
    {
      "@type": "Question",
      "name": "What is the XLBONUS code for esports betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "XLBONUS is the welcome promo code for new 1win registrations. Enter it before your first deposit to unlock the welcome bonus, which can be used on esports and all other sports markets on the platform."
      }
    }
  ]
}
</script>
"""

html = render_page(
    slug='sports/esports',
    title='1win esports betting: CS2, Dota 2, LoL and XLBONUS',
    description='Bet on CS2, Dota 2, League of Legends, Valorant and more at 1win with 40,000+ markets. Claim promo code XLBONUS on your first deposit. Curaçao 8048/JAZ licensed.',
    h1='1win esports betting: CS2, Dota 2, LoL, Valorant and more',
    breadcrumbs=[('Home', '/en/'), ('Sports', '/en/sports/'), ('Esports', None)],
    main_html=esports_main,
    extra_schema=esports_faq_schema,
)
open('en/sports/esports.html', 'w').write(html)
print('esports.html written')

# ─────────────────────────────────────────────────────────────────────────────
# 6. HUB: en/sports/index.html
# ─────────────────────────────────────────────────────────────────────────────

hub_main = """
<section class="lede">
  <p>1win's sportsbook covers 40,000+ markets across every major sport under a Curaçao 8048/JAZ licence, giving you access to football, cricket, tennis, basketball and esports from one account. Whether you are following the EPL on a Saturday afternoon, tracking an IPL T20 late at night or watching a CS2 Major unfold in real time, 1win has pre-match odds, in-play markets and 24/7 cashout ready for you. Register with promo code <span class="code-highlight">XLBONUS</span> to start with a boosted first deposit.</p>
</section>

<section class="sport-router">
  <h2>What sport do you want to bet on?</h2>
  <p>Select your game below and go straight to the full guide for that sport.</p>
  <div class="sport-grid">
    <a class="sport-card" href="/en/sports/football">
      <span class="sport-icon">&#9917;</span>
      <strong>Football</strong>
      <span>EPL, Champions League, World Cup and 15+ leagues</span>
    </a>
    <a class="sport-card" href="/en/sports/cricket">
      <span class="sport-icon">&#127944;</span>
      <strong>Cricket</strong>
      <span>IPL, T20 World Cup, ODI World Cup and Test cricket</span>
    </a>
    <a class="sport-card" href="/en/sports/tennis">
      <span class="sport-icon">&#127931;</span>
      <strong>Tennis</strong>
      <span>All 4 Grand Slams, ATP Masters 1000, WTA and Davis Cup</span>
    </a>
    <a class="sport-card" href="/en/sports/basketball">
      <span class="sport-icon">&#127936;</span>
      <strong>Basketball</strong>
      <span>NBA, EuroLeague, NCAA, FIBA and NBL Australia</span>
    </a>
    <a class="sport-card" href="/en/sports/esports">
      <span class="sport-icon">&#127918;</span>
      <strong>Esports</strong>
      <span>CS2, Dota 2, LoL, Valorant, Rainbow Six and MLBB</span>
    </a>
  </div>
</section>

<section class="sportsbook-overview">
  <h2>What makes 1win's sportsbook stand out</h2>
  <p>1win is built for bettors who follow sport seriously. Below is a summary of what separates the platform from generic bookmakers.</p>
  <ul>
    <li><strong>40,000+ markets across all sports</strong> - From the English Premier League to Challenger tennis and regional esports leagues, the depth of market coverage is a primary differentiator. You will not reach the bottom of the list on a busy Saturday.</li>
    <li><strong>In-play betting with live streaming</strong> - Select matches across football, cricket, tennis, basketball and esports carry live video streams within the 1win platform. Watch and bet without switching apps.</li>
    <li><strong>24/7 cashout on eligible bets</strong> - Full cashout and partial cashout are available any time, giving you active control over open positions. Lock in profit early, cut a losing position at reduced loss, or ride the risk with the remainder: the decision is yours.</li>
    <li><strong>Bet builder (same-game parlay)</strong> - Combine multiple markets from the same fixture into one bet slip. A football parlay might link match winner, both teams to score and a goalscorer. Cricket might combine top batter, match winner and total runs. The combined odds multiply the potential return.</li>
    <li><strong>XLBONUS welcome offer</strong> - New players who register with promo code <span class="code-highlight">XLBONUS</span> receive a boosted first deposit. The bonus applies across sports, giving you additional funds to explore multiple markets on arrival.</li>
    <li><strong>Fast deposits and withdrawals</strong> - 1win accepts UPI, PIX, cards, e-wallets, USDT and multiple other payment methods. Deposits are processed instantly for most methods. Withdrawals follow a transparent KYC process before the first payout.</li>
    <li><strong>Full mobile experience</strong> - The 1win app for Android and iOS carries every feature from the desktop sportsbook, including in-play streaming and cashout. Download at <a href="/en/app">1win.codes/en/app</a>.</li>
    <li><strong>Curaçao 8048/JAZ licence</strong> - 1win operates under a Curaçao licence, which provides a regulatory framework for player fund protection, responsible gambling tools and fair-play standards.</li>
  </ul>
</section>

<section class="how-to">
  <h2>How to start betting at 1win in 5 steps</h2>
  <ol>
    <li><strong>Register</strong> - Open your account at 1win.codes. Enter your email, choose a password and complete basic details in under two minutes.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> - Add XLBONUS in the promo field before confirming registration to activate the first-deposit welcome bonus.</li>
    <li><strong>Make a deposit</strong> - Select your preferred payment method, enter the amount and confirm. Bonus funds are credited immediately after the deposit.</li>
    <li><strong>Choose your sport</strong> - Navigate to Sports in the main menu and select from the sidebar: football, cricket, tennis, basketball, esports or any other listed sport.</li>
    <li><strong>Place your first bet</strong> - Click any odds to open the bet slip, set your stake and confirm. Track live bets through the My Bets panel.</li>
  </ol>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details>
    <summary>How many sports does 1win cover?</summary>
    <p>1win covers more than 30 sports globally including football, cricket, tennis, basketball, esports, American football, rugby, boxing, MMA, volleyball, table tennis and more, with 40,000+ markets available at any given time.</p>
  </details>
  <details>
    <summary>What is the XLBONUS promo code?</summary>
    <p>XLBONUS is the welcome promo code for new 1win players. Enter it at registration before making your first deposit to receive the current welcome bonus, which applies across all sports betting markets on the platform.</p>
  </details>
  <details>
    <summary>Does 1win have in-play betting?</summary>
    <p>Yes. 1win's in-play sportsbook covers football, cricket, tennis, basketball, esports and more with live odds that update continuously throughout each event. Select matches also carry live streaming within the platform.</p>
  </details>
  <details>
    <summary>Is cashout available at 1win?</summary>
    <p>Yes. Full and partial cashout is available 24/7 on eligible pre-match and in-play bets. You can close or reduce positions on football, cricket, basketball, tennis and esports bets at any time while cashout is offered.</p>
  </details>
  <details>
    <summary>Is 1win a licensed sportsbook?</summary>
    <p>1win operates under a Curaçao 8048/JAZ licence, which governs its sports betting and casino operations and requires adherence to responsible gambling and player protection standards.</p>
  </details>
  <details>
    <summary>Can I bet on my phone at 1win?</summary>
    <p>Yes. The 1win app for Android and iOS includes the full sportsbook, in-play betting, live streaming and cashout. Download the Android APK from 1win.codes/en/app or install the iOS version from the App Store.</p>
  </details>
</section>

<style>
.sport-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.sport-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  padding: 1.2rem 1rem;
  border: 1px solid var(--border, #e2e8f0);
  border-radius: 8px;
  text-align: center;
  text-decoration: none;
  color: inherit;
  transition: box-shadow 0.15s, border-color 0.15s;
}
.sport-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  border-color: var(--accent, #0ea5e9);
}
.sport-icon {
  font-size: 2rem;
  line-height: 1;
}
.sport-card strong {
  font-size: 1rem;
  font-weight: 700;
}
.sport-card span:last-child {
  font-size: 0.82rem;
  opacity: 0.7;
  line-height: 1.3;
}
</style>
"""

hub_faq_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How many sports does 1win cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win covers more than 30 sports globally including football, cricket, tennis, basketball, esports, American football, rugby, boxing, MMA, volleyball, table tennis and more, with 40,000+ markets available at any given time."
      }
    },
    {
      "@type": "Question",
      "name": "What is the XLBONUS promo code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "XLBONUS is the welcome promo code for new 1win players. Enter it at registration before making your first deposit to receive the current welcome bonus, which applies across all sports betting markets on the platform."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win have in-play betting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win's in-play sportsbook covers football, cricket, tennis, basketball, esports and more with live odds that update continuously throughout each event. Select matches also carry live streaming within the platform."
      }
    },
    {
      "@type": "Question",
      "name": "Is cashout available at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Full and partial cashout is available 24/7 on eligible pre-match and in-play bets. You can close or reduce positions on football, cricket, basketball, tennis and esports bets at any time while cashout is offered."
      }
    },
    {
      "@type": "Question",
      "name": "Is 1win a licensed sportsbook?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win operates under a Curacao 8048/JAZ licence, which governs its sports betting and casino operations and requires adherence to responsible gambling and player protection standards."
      }
    },
    {
      "@type": "Question",
      "name": "Can I bet on my phone at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The 1win app for Android and iOS includes the full sportsbook, in-play betting, live streaming and cashout. Download the Android APK from 1win.codes/en/app or install the iOS version from the App Store."
      }
    }
  ]
}
</script>
"""

html = render_page(
    slug='sports',
    title='1win sports betting hub: football, cricket, tennis and XLBONUS',
    description='Bet on football, cricket, tennis, basketball and esports at 1win with 40,000+ markets. Use promo code XLBONUS on your first deposit. Curaçao 8048/JAZ licensed.',
    h1='1win sports betting: 40,000+ markets across every major sport',
    breadcrumbs=[('Home', '/en/'), ('Sports', None)],
    main_html=hub_main,
    extra_schema=hub_faq_schema,
)
open('en/sports/index.html', 'w').write(html)
print('index.html (hub) written')

print('\nAll 6 files written successfully.')
