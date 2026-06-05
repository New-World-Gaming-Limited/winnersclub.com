"""
Sprint 9: Generate 12 India state pages + hub index for 1win.codes EN site.
Run from repo root: python build_helpers/gen_india_pages.py
"""
import os, sys

# Ensure repo root is on path
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from build_helpers.page_template import render_page

os.makedirs(os.path.join(REPO, 'en', 'india'), exist_ok=True)

def w(slug, title, description, h1, main_html, extra_schema=''):
    html = render_page(
        slug=slug,
        title=title,
        description=description,
        h1=h1,
        breadcrumbs=[
            ('Home', '/en/'),
            ('India', '/en/india/'),
            (h1, None),
        ],
        main_html=main_html,
        extra_schema=extra_schema,
    )
    path = os.path.join(REPO, 'en', slug + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  wrote {path}')

# ─── MAHARASHTRA ─────────────────────────────────────────────────────────────
MH_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Is 1win legal in Maharashtra?","acceptedAnswer":{"@type":"Answer","text":"1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in India is set at the state level and continues to evolve. Players in Maharashtra should review current local rules before registering."}},
    {"@type":"Question","name":"Which payment method is fastest for Mumbai players?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe or Google Pay typically processes deposits instantly, 24/7. IMPS is a solid fallback for bank-to-bank transfers."}},
    {"@type":"Question","name":"Can I bet on Mumbai Indians at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win carries 40,000+ pre-match and live markets during IPL season, including full coverage of Mumbai Indians fixtures across T20 formats."}},
    {"@type":"Question","name":"How do I claim the XLBONUS in Maharashtra?","acceptedAnswer":{"@type":"Answer","text":"Register at 1win using promo code XLBONUS, make your first deposit via UPI or any supported method, and the welcome bonus is credited to your account automatically."}},
    {"@type":"Question","name":"Does 1win have a mobile app for Android?","acceptedAnswer":{"@type":"Answer","text":"Yes. A dedicated APK is available for download directly from 1win.codes. iOS users can access the full platform via the mobile browser."}}
  ]
}
</script>"""

MH_MAIN = """
<section class="lede">
  <p>1win is one of the most active sports betting platforms available to Maharashtra players, holding a Curacao 8048/JAZ licence and giving access to 40,000+ live and pre-match betting markets. Use promo code <span class="code-highlight">XLBONUS</span> when you register to unlock the welcome bonus and get started on IPL, kabaddi, and casino markets from Mumbai or Pune.</p>
</section>

<section class="local-context">
  <h2>1win and Maharashtra: cricket, finance capital and more</h2>
  <p>Maharashtra is home to Mumbai, India's financial centre and the city that gave Indian cricket its greatest franchise, the Mumbai Indians. Five-time IPL champions, the Mumbai Indians command one of the largest supporter bases in the country, and during the IPL season the appetite for match betting and fantasy markets in the state peaks significantly. Pune, Maharashtra's second city and home to the Pune Supergiants legacy, adds a sizeable tech-savvy population that is comfortable with digital payments and online entertainment. Beyond cricket, kabaddi enjoys deep roots across rural Maharashtra, and 1win covers Pro Kabaddi League fixtures with dedicated markets throughout the season. The state's high urban density and strong smartphone penetration make it one of the most active online gaming regions in India.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Maharashtra</h2>
  <p>UPI dominates digital payments across Mumbai and Pune. PhonePe and Google Pay have near-universal adoption among urban Maharashtra users, making instant UPI deposits the preferred route into a 1win account. Paytm Wallet remains widely used by players who prefer to keep betting funds separate from their primary bank. IMPS (Immediate Payment Service) is the go-to for larger transfers where direct bank connectivity is needed; most Maharashtra-based banks support IMPS around the clock. Net banking via HDFC, ICICI, and Axis Bank is a reliable alternative for players who prefer browser-based transactions without a UPI app. Crypto deposits (USDT, BTC) have a growing user base in Mumbai's finance and tech communities; 1win supports USDT deposits with the same processing speed as traditional rails. Minimum deposit on all methods is low, keeping the entry barrier accessible for first-time players.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Maharashtra</h2>
  <p>Mumbai Indians fixtures attract peak traffic on 1win during the Indian Premier League, with markets spanning match winner, top batsman, total sixes, and ball-by-ball live betting. The full IPL schedule is available in the sports lobby from auction day through the final. Maharashtra also has a strong kabaddi culture; 1win lists Pro Kabaddi League games with raid points, tackle markets, and full match odds. Football betting is rising among younger Mumbai residents following the Mumbai City FC ISL run, and 1win carries ISL matches alongside the Premier League and UEFA Champions League. For casino fans, 1win's live tables include several Indian rupee-denominated rooms where Mumbai players can participate without currency conversion overhead.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Maharashtra</h2>
  <ol>
    <li><strong>Open the registration page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> and enter your email or phone number.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the bonus field to activate the welcome offer before your first deposit.</li>
    <li><strong>Choose UPI or PhonePe</strong> as your deposit method and set your preferred amount (minimum deposit applies).</li>
    <li><strong>Navigate to IPL or kabaddi markets</strong> in the sports lobby and add your first selection to the bet slip.</li>
    <li><strong>Confirm your bet</strong> and monitor live progress via the in-play tracker on desktop or the 1win mobile site.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Maharashtra players</h2>
  <p>Online gaming and sports betting regulation in India is determined at the state level and continues to develop. Maharashtra has not enacted a dedicated online gambling statute, but players should review current local rules and consult relevant authorities before participating. 1win operates under its Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Is 1win legal in Maharashtra?</summary><p>1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in India is set at the state level and continues to evolve. Players in Maharashtra should review current local rules before registering.</p></details>
  <details><summary>Which payment method is fastest for Mumbai players?</summary><p>UPI via PhonePe or Google Pay typically processes deposits instantly, 24/7. IMPS is a solid fallback for bank-to-bank transfers.</p></details>
  <details><summary>Can I bet on Mumbai Indians at 1win?</summary><p>Yes. 1win carries 40,000+ pre-match and live markets during IPL season, including full coverage of Mumbai Indians fixtures across T20 formats.</p></details>
  <details><summary>How do I claim the XLBONUS in Maharashtra?</summary><p>Register at 1win using promo code XLBONUS, make your first deposit via UPI or any supported method, and the welcome bonus is credited to your account automatically.</p></details>
  <details><summary>Does 1win have a mobile app for Android?</summary><p>Yes. A dedicated APK is available for download directly from 1win.codes. iOS users can access the full platform via the mobile browser.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/maharashtra',
  '1win Maharashtra: UPI deposits, IPL betting and XLBONUS',
  '1win Maharashtra gives Mumbai and Pune players 40,000+ IPL and kabaddi markets, instant UPI deposits, and the XLBONUS welcome offer. Curacao 8048/JAZ licensed.',
  '1win Maharashtra: IPL betting and UPI deposits',
  MH_MAIN, MH_FAQ_SCHEMA)

# ─── TAMIL NADU ──────────────────────────────────────────────────────────────
TN_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can players in Tamil Nadu use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win holds a Curacao 8048/JAZ licence. Tamil Nadu has enacted state-level online gaming regulations; players should check current local rules before registering."}},
    {"@type":"Question","name":"What deposit methods work best in Chennai?","acceptedAnswer":{"@type":"Answer","text":"UPI via Google Pay and PhonePe are the fastest options for Chennai players. Paytm Wallet and IMPS are reliable alternatives."}},
    {"@type":"Question","name":"Does 1win cover CSK matches?","acceptedAnswer":{"@type":"Answer","text":"Yes. Chennai Super Kings fixtures are listed with 40,000+ markets during IPL season, including live in-play betting on runs, wickets, and match outcome."}},
    {"@type":"Question","name":"How do I use promo code XLBONUS?","acceptedAnswer":{"@type":"Answer","text":"Enter XLBONUS in the promo field during registration at 1win.codes/en/register. The welcome bonus applies to your first qualifying deposit."}},
    {"@type":"Question","name":"Is the 1win site available in Tamil?","acceptedAnswer":{"@type":"Answer","text":"The main 1win interface is in English. The platform is accessible from Tamil Nadu via any modern browser on desktop or mobile."}}
  ]
}
</script>"""

TN_MAIN = """
<section class="lede">
  <p>1win brings Chennai Super Kings fans and Tamil Nadu sports enthusiasts access to 40,000+ betting markets, a Curacao 8048/JAZ licence for player protection, and the welcome promo code <span class="code-highlight">XLBONUS</span> to boost your opening deposit. From IPL season through year-round cricket and football, 1win is built for the engaged Tamil Nadu bettor.</p>
</section>

<section class="local-context">
  <h2>1win and Tamil Nadu: CSK cricket and Chennai's gaming culture</h2>
  <p>Tamil Nadu's relationship with cricket is intense and deeply personal. Chennai Super Kings, five-time IPL champions, carry a fanbase that is among the most passionate in the country. Match days at Chepauk see enormous engagement across sports media and digital platforms. Chennai itself is one of South India's leading technology hubs, meaning a large share of the city's population is digital-native and at ease with online platforms. Tamil Nadu has been an active policy environment for online gaming regulation; 1win users should remain aware of local rules, which this page outlines in the legal note section. Beyond cricket, the state has an established kabaddi culture and growing interest in football through the ISL's Chennai connection.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Tamil Nadu</h2>
  <p>Chennai and the broader Tamil Nadu urban belt rely heavily on UPI for daily transactions. Google Pay commands strong adoption in the state, driven by early user incentive programs; PhonePe follows closely. For 1win deposits, both options process instantly with no transaction fee on the platform side. Paytm Wallet offers a useful buffer layer for players who prefer not to link a bank account directly. IMPS is available for higher-value deposits through any UPI-enabled bank, including Indian Bank, Indian Overseas Bank, and City Union Bank, which have significant retail presence in Tamil Nadu. Net banking via Karur Vysya Bank and other regional banks is also supported. USDT deposits via TRC-20 are accepted for players comfortable with crypto, with conversions handled server-side at the prevailing rate.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Tamil Nadu</h2>
  <p>CSK fixtures dominate Tamil Nadu's betting calendar during the Indian Premier League. 1win lists full CSK match markets including toss winner, top run scorer, player of the match, total fours, and ball-by-ball live options. Chennai's football community follows the ISL calendar and has growing Premier League viewership; 1win carries both. Kabaddi attracts consistent interest through the Pro Kabaddi League, with Tamil Thalaivas fixtures receiving dedicated coverage. Formula 1 has a notable niche following in Chennai's engineering community; 1win offers F1 driver and constructor markets throughout the season. Casino markets including live blackjack and roulette are available in INR-compatible rooms for Chennai players seeking non-sports entertainment.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Tamil Nadu</h2>
  <ol>
    <li><strong>Go to the registration page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a>.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the designated field to activate your welcome bonus.</li>
    <li><strong>Select Google Pay or PhonePe</strong> as your deposit method and complete the UPI transaction.</li>
    <li><strong>Open the sports lobby</strong> and search for CSK or any active cricket fixture to place your first bet.</li>
    <li><strong>Check your account balance</strong> after the welcome bonus credits and proceed to explore live in-play markets.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Tamil Nadu players</h2>
  <p>Tamil Nadu has enacted state-level regulations governing online gaming; the legislative landscape continues to evolve. Players are encouraged to review the current statutory position under Tamil Nadu Online Gaming Authority rules before participating on any platform. 1win holds a Curacao 8048/JAZ licence. Nothing on this page constitutes legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can players in Tamil Nadu use 1win?</summary><p>1win holds a Curacao 8048/JAZ licence. Tamil Nadu has enacted state-level online gaming regulations; players should check current local rules before registering.</p></details>
  <details><summary>What deposit methods work best in Chennai?</summary><p>UPI via Google Pay and PhonePe are the fastest options for Chennai players. Paytm Wallet and IMPS are reliable alternatives.</p></details>
  <details><summary>Does 1win cover CSK matches?</summary><p>Yes. Chennai Super Kings fixtures are listed with 40,000+ markets during IPL season, including live in-play betting on runs, wickets, and match outcome.</p></details>
  <details><summary>How do I use promo code XLBONUS?</summary><p>Enter XLBONUS in the promo field during registration at 1win.codes/en/register. The welcome bonus applies to your first qualifying deposit.</p></details>
  <details><summary>Is the 1win site available in Tamil?</summary><p>The main 1win interface is in English. The platform is accessible from Tamil Nadu via any modern browser on desktop or mobile.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/tamil-nadu',
  '1win for Chennai players: CSK betting, UPI deposits and XLBONUS',
  'Chennai and Tamil Nadu players get 40,000+ CSK and IPL markets, instant UPI deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Tamil Nadu: CSK cricket markets and UPI deposits',
  TN_MAIN, TN_FAQ_SCHEMA)

# ─── KARNATAKA ───────────────────────────────────────────────────────────────
KA_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Is online betting open in Karnataka?","acceptedAnswer":{"@type":"Answer","text":"Karnataka has a relatively open regulatory stance on online skill gaming compared to some other Indian states. 1win operates under a Curacao 8048/JAZ licence. Players should verify current local rules before participating."}},
    {"@type":"Question","name":"Which UPI apps are popular with Bengaluru bettors?","acceptedAnswer":{"@type":"Answer","text":"PhonePe, which is headquartered in Bengaluru, has very high penetration in Karnataka. Google Pay and Paytm follow. All are accepted for 1win deposits."}},
    {"@type":"Question","name":"Can I bet on RCB at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. Royal Challengers Bengaluru fixtures are covered with 40,000+ markets including live ball-by-ball options throughout the IPL season."}},
    {"@type":"Question","name":"How do I activate the XLBONUS?","acceptedAnswer":{"@type":"Answer","text":"Enter XLBONUS in the promo code field when registering at 1win. The bonus is applied to your first qualifying deposit automatically."}},
    {"@type":"Question","name":"Does 1win support INR deposits from Karnataka?","acceptedAnswer":{"@type":"Answer","text":"Yes. INR deposits via UPI, IMPS, net banking, and wallets are all supported. Withdrawals are processed back to the same payment method."}}
  ]
}
</script>"""

KA_MAIN = """
<section class="lede">
  <p>Bengaluru's tech-forward population has found a natural home at 1win, a Curacao 8048/JAZ licensed platform with 40,000+ sports markets and the welcome promo code <span class="code-highlight">XLBONUS</span> that gives Karnataka players an instant deposit bonus when they register. From RCB IPL nights to year-round football and casino action, 1win is optimised for the connected Bengaluru bettor.</p>
</section>

<section class="local-context">
  <h2>1win and Karnataka: Bengaluru's tech crowd and RCB fever</h2>
  <p>Bengaluru is India's technology capital, and its 12 million-plus residents include a large proportion of young professionals who are digitally active across entertainment platforms. Royal Challengers Bengaluru command an enormously loyal fanbase that extends well beyond the city into the wider state. RCB match days are some of the highest-traffic moments on any sports betting platform serving South India. Karnataka's regulatory environment for online gaming has been relatively open compared to neighbouring states, making it one of the more accessible markets for licensed international platforms. Mysuru, Mangaluru, and Hubballi add significant user bases outside the capital. Football interest is also meaningful, particularly among younger Bengaluru residents following the ISL and European leagues.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Karnataka</h2>
  <p>PhonePe, headquartered in Bengaluru, is the dominant UPI provider across Karnataka. Its deep local roots mean very high adoption rates, and 1win deposits via PhonePe are credited in seconds. Google Pay is the strong second option, particularly popular in the tech-worker demographic. Paytm Wallet and IMPS via Canara Bank, which has its registered office in Bengaluru, are preferred by users seeking non-UPI rails. Net banking through HDFC, ICICI, and Axis is fully supported. Crypto adoption among Bengaluru's developer community is above the national average; USDT and BTC deposits are available with immediate confirmation. For withdrawals, the same methods apply, with most UPI withdrawals completing within a few hours of approval.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Karnataka</h2>
  <p>RCB fixtures are the headline draw for Karnataka bettors on 1win during the Indian Premier League, with deep markets on match outcome, Virat Kohli batting milestones, total boundaries, and ball-by-ball in-play. The Karnataka Premier League (KPL) domestic T20 events attract additional regional interest. Football markets covering the ISL, Premier League, La Liga, and Champions League serve Bengaluru's significant football audience. Badminton has niche but dedicated followers in Karnataka; 1win carries BWF Super Series and Thomas Cup markets when available. The casino section features live dealer rooms compatible with INR deposits, including baccarat and teen patti variants that resonate with Indian players.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Karnataka</h2>
  <ol>
    <li><strong>Visit the registration page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> from any browser.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the bonus code field during sign-up.</li>
    <li><strong>Deposit via PhonePe or Google Pay</strong> using UPI for an instant credit to your 1win wallet.</li>
    <li><strong>Find RCB or any IPL fixture</strong> in the sports section and build your bet slip.</li>
    <li><strong>Place your bet</strong> and track live progress using 1win's in-play stats overlay.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Karnataka players</h2>
  <p>Karnataka has maintained a relatively open stance on online skill gaming, though the broader regulatory environment across India continues to evolve. Players should review applicable state and central rules before participating. 1win operates under a Curacao 8048/JAZ licence. This page is informational only and does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Is online betting open in Karnataka?</summary><p>Karnataka has a relatively open regulatory stance on online skill gaming compared to some other Indian states. 1win operates under a Curacao 8048/JAZ licence. Players should verify current local rules before participating.</p></details>
  <details><summary>Which UPI apps are popular with Bengaluru bettors?</summary><p>PhonePe, which is headquartered in Bengaluru, has very high penetration in Karnataka. Google Pay and Paytm follow. All are accepted for 1win deposits.</p></details>
  <details><summary>Can I bet on RCB at 1win?</summary><p>Yes. Royal Challengers Bengaluru fixtures are covered with 40,000+ markets including live ball-by-ball options throughout the IPL season.</p></details>
  <details><summary>How do I activate the XLBONUS?</summary><p>Enter XLBONUS in the promo code field when registering at 1win. The bonus is applied to your first qualifying deposit automatically.</p></details>
  <details><summary>Does 1win support INR deposits from Karnataka?</summary><p>Yes. INR deposits via UPI, IMPS, net banking, and wallets are all supported. Withdrawals are processed back to the same payment method.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/karnataka',
  '1win Karnataka: RCB IPL betting, PhonePe deposits and XLBONUS',
  'Bengaluru and Karnataka players get 40,000+ RCB and IPL markets, PhonePe UPI deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Karnataka: RCB cricket markets and PhonePe deposits',
  KA_MAIN, KA_FAQ_SCHEMA)

# ─── DELHI ───────────────────────────────────────────────────────────────────
DL_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Delhi residents bet on 1win?","acceptedAnswer":{"@type":"Answer","text":"1win holds a Curacao 8048/JAZ licence. Online gaming regulation in Delhi and across India is evolving; players should review current applicable rules before registering."}},
    {"@type":"Question","name":"What is the fastest deposit method for Delhi players?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe or Google Pay is fastest, crediting your 1win account in seconds. IMPS via major Delhi-area banks is a strong alternative for larger amounts."}},
    {"@type":"Question","name":"Does 1win list Delhi Capitals IPL matches?","acceptedAnswer":{"@type":"Answer","text":"Yes. Delhi Capitals fixtures appear in the 1win sports lobby with 40,000+ markets covering match winner, top scorer, and live ball-by-ball options."}},
    {"@type":"Question","name":"How do I get the XLBONUS in Delhi?","acceptedAnswer":{"@type":"Answer","text":"Enter promo code XLBONUS during registration at 1win.codes/en/register. The welcome bonus is applied automatically to your first qualifying deposit."}},
    {"@type":"Question","name":"Is there a 1win app for Delhi Android users?","acceptedAnswer":{"@type":"Answer","text":"Yes. An Android APK is available for download from 1win.codes. The mobile browser version is also fully functional on iOS and Android."}}
  ]
}
</script>"""

DL_MAIN = """
<section class="lede">
  <p>Delhi and NCR players have access to 1win, a Curacao 8048/JAZ licensed platform with 40,000+ IPL, cricket, and casino markets. Register with promo code <span class="code-highlight">XLBONUS</span> to activate the welcome deposit bonus and start betting on Delhi Capitals and tournaments across the full sporting calendar.</p>
</section>

<section class="local-context">
  <h2>1win and Delhi: capital market, Delhi Capitals and high-income bettors</h2>
  <p>Delhi is India's political capital and one of its wealthiest consumer markets. The National Capital Region, which extends into Gurugram and Noida, houses a dense professional population with above-average disposable income and strong smartphone usage. Delhi Capitals, the IPL franchise for the capital region, have developed a loyal following across the NCR belt. The city also hosts substantial cricket viewership for both domestic and international fixtures at the Arun Jaitley Stadium. Football has a growing fanbase in Delhi, particularly in younger demographics watching the Premier League and Champions League. The NCR tech corridor in Noida and Gurugram contributes a digitally confident user segment comfortable with online entertainment platforms.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Delhi</h2>
  <p>Delhi's high-income profile correlates with strong adoption of multiple UPI applications. PhonePe and Google Pay are the dominant apps in the NCR corridor. Paytm, founded with Delhi-NCR roots, retains strong brand recognition and wallet adoption across the capital. IMPS is popular for players who transfer from major banks including SBI, PNB, and HDFC, all of which have significant Delhi retail presence. Net banking is a preferred option among older players and professionals who manage finances through desktop banking portals. USDT crypto deposits attract Delhi's fintech and startup community, many of whom hold crypto as part of broader portfolios. All INR deposits are processed without additional platform-side fees, and withdrawals route back through the original payment channel.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Delhi</h2>
  <p>Delhi Capitals fixtures during the Indian Premier League are the primary draw for capital-region bettors. 1win provides full DC coverage with markets on toss, player innings totals, bowling figures, and live in-play betting. International cricket at the Arun Jaitley Stadium, including India home Tests and ODIs, receives deep market coverage with session-by-session lines. Football commands growing attention; 1win lists Premier League, Champions League, and ISL fixtures alongside Asian Cup and national team qualifying matches. For high-income casino players, 1win's VIP live tables provide access to high-limit blackjack, baccarat, and roulette rooms in INR. Motorsport, tennis, and golf round out the markets for the Delhi bettor looking beyond cricket.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Delhi</h2>
  <ol>
    <li><strong>Open the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> on mobile or desktop.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> to unlock the welcome bonus on your first deposit.</li>
    <li><strong>Select your deposit method</strong>: PhonePe, Google Pay, or IMPS via your Delhi-area bank account.</li>
    <li><strong>Go to the IPL section</strong> and find the Delhi Capitals next fixture to place your first bet.</li>
    <li><strong>Track live markets</strong> as the match progresses using the in-play dashboard for real-time odds updates.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Delhi players</h2>
  <p>Online gaming in India is governed by a combination of central and state-level frameworks that continue to evolve. Delhi does not have a standalone online gaming statute at the time of writing, but the regulatory environment across India is active. Players should review current rules before participating. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Delhi residents bet on 1win?</summary><p>1win holds a Curacao 8048/JAZ licence. Online gaming regulation in Delhi and across India is evolving; players should review current applicable rules before registering.</p></details>
  <details><summary>What is the fastest deposit method for Delhi players?</summary><p>UPI via PhonePe or Google Pay is fastest, crediting your 1win account in seconds. IMPS via major Delhi-area banks is a strong alternative for larger amounts.</p></details>
  <details><summary>Does 1win list Delhi Capitals IPL matches?</summary><p>Yes. Delhi Capitals fixtures appear in the 1win sports lobby with 40,000+ markets covering match winner, top scorer, and live ball-by-ball options.</p></details>
  <details><summary>How do I get the XLBONUS in Delhi?</summary><p>Enter promo code XLBONUS during registration at 1win.codes/en/register. The welcome bonus is applied automatically to your first qualifying deposit.</p></details>
  <details><summary>Is there a 1win app for Delhi Android users?</summary><p>Yes. An Android APK is available for download from 1win.codes. The mobile browser version is also fully functional on iOS and Android.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/delhi',
  '1win Delhi: Delhi Capitals IPL betting, UPI deposits and XLBONUS',
  'Delhi and NCR players get 40,000+ Delhi Capitals and cricket markets, instant UPI deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Delhi: Delhi Capitals markets and instant UPI deposits',
  DL_MAIN, DL_FAQ_SCHEMA)

# ─── UTTAR PRADESH ───────────────────────────────────────────────────────────
UP_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can players in Uttar Pradesh use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in UP continues to evolve under central and state frameworks. Players should verify applicable rules before registering."}},
    {"@type":"Question","name":"Which payment methods work for UP players?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay are available across Lucknow, Kanpur, and other UP cities. IMPS through SBI and Bank of Baroda branches is a popular fallback."}},
    {"@type":"Question","name":"Does 1win cover Lucknow Super Giants?","acceptedAnswer":{"@type":"Answer","text":"Yes. Lucknow Super Giants fixtures carry full market coverage on 1win, including live in-play betting on match outcome, top batsman, and total runs markets."}},
    {"@type":"Question","name":"How do I activate XLBONUS in Uttar Pradesh?","acceptedAnswer":{"@type":"Answer","text":"Register at 1win.codes/en/register and enter XLBONUS in the promo code field. The welcome bonus is credited after your first qualifying deposit."}},
    {"@type":"Question","name":"Is there Hindi language support on 1win?","acceptedAnswer":{"@type":"Answer","text":"The main 1win platform is in English. Customer support is accessible in multiple languages including Hindi via live chat."}}
  ]
}
</script>"""

UP_MAIN = """
<section class="lede">
  <p>As India's most populous state, Uttar Pradesh represents one of the largest untapped sports betting audiences in the country. 1win, licensed under Curacao 8048/JAZ, provides UP players access to 40,000+ markets across cricket, kabaddi, and casino games. Register with promo code <span class="code-highlight">XLBONUS</span> and start betting on Lucknow Super Giants and beyond from Lucknow, Kanpur, Agra, or anywhere across the state.</p>
</section>

<section class="local-context">
  <h2>1win and Uttar Pradesh: most populous state and Lucknow Super Giants</h2>
  <p>Uttar Pradesh is home to more than 220 million people, making it by far the largest state in India by population. Cricket is the dominant sport, with intense interest in both domestic T20 leagues and international fixtures. Lucknow Super Giants, established for the 2022 IPL season, gave the state its own IPL franchise for the first time and rapidly built a passionate local supporter base around the Ekana Cricket Stadium in Lucknow. Kanpur, Agra, Varanasi, and Prayagraj add further population density across the state's cricket-watching public. Kabaddi maintains a traditional following across rural UP, and the Pro Kabaddi League's UP Yoddhas provide a homegrown team to follow through the season. Smartphone penetration is rising rapidly across UP's tier-2 and tier-3 cities, expanding the digital sports audience.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Uttar Pradesh</h2>
  <p>UPI adoption has grown rapidly across Uttar Pradesh through government-linked initiatives and NPCI's Bharat QR rollout. PhonePe and Google Pay are the primary apps in Lucknow and other urban centres, offering instant deposits at 1win with no additional fee. IMPS via public sector banks including State Bank of India and Bank of Baroda is especially important in UP, where PSU bank accounts are more common than private-sector banks compared to metros. Paytm has strong recognition in the state as one of the earliest digital wallet platforms with significant UP user adoption. NEFT is available for players who prefer scheduled bank transfers rather than real-time payment. For rural areas with lower smartphone penetration, UPI123Pay (feature-phone UPI) is an emerging option, though 1win's standard UPI flow assumes a smartphone-compatible device.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Uttar Pradesh</h2>
  <p>Lucknow Super Giants fixtures top the batting order for UP bettors on 1win. Full LSG market coverage includes match result, top run scorer, highest partnership, and live ball-by-ball in-play markets throughout the IPL season. India home internationals, including Tests at Green Park Kanpur, receive dedicated market lines. The UP Yoddhas Pro Kabaddi League schedule is tracked with raid points, super tackle, and full-match outcome markets. Wrestling has a traditional cultural foothold in rural UP; 1win lists WWE and MMA events including UFC for fans of grappling sports. Casino options including Andar Bahar and Teen Patti live rooms appeal to players looking for India-native card game formats.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Uttar Pradesh</h2>
  <ol>
    <li><strong>Open the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> on your smartphone or desktop.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the promo field to unlock the welcome deposit bonus.</li>
    <li><strong>Deposit via UPI, PhonePe, or IMPS</strong> through your UP bank account. SBI and Bank of Baroda are both compatible.</li>
    <li><strong>Navigate to Lucknow Super Giants</strong> or any cricket fixture in the sports lobby to place your first bet.</li>
    <li><strong>Monitor live markets</strong> through the in-play tracker and adjust your bet slip as the match unfolds.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Uttar Pradesh players</h2>
  <p>Online gaming in Uttar Pradesh is subject to central government guidelines and evolving state-level frameworks. Players are advised to review current regulations before participating on any online platform. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can players in Uttar Pradesh use 1win?</summary><p>1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in UP continues to evolve under central and state frameworks. Players should verify applicable rules before registering.</p></details>
  <details><summary>Which payment methods work for UP players?</summary><p>UPI via PhonePe and Google Pay are available across Lucknow, Kanpur, and other UP cities. IMPS through SBI and Bank of Baroda branches is a popular fallback.</p></details>
  <details><summary>Does 1win cover Lucknow Super Giants?</summary><p>Yes. Lucknow Super Giants fixtures carry full market coverage on 1win, including live in-play betting on match outcome, top batsman, and total runs markets.</p></details>
  <details><summary>How do I activate XLBONUS in Uttar Pradesh?</summary><p>Register at 1win.codes/en/register and enter XLBONUS in the promo code field. The welcome bonus is credited after your first qualifying deposit.</p></details>
  <details><summary>Is there Hindi language support on 1win?</summary><p>The main 1win platform is in English. Customer support is accessible in multiple languages including Hindi via live chat.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/uttar-pradesh',
  '1win Uttar Pradesh: Lucknow Super Giants betting and XLBONUS',
  'UP players get 40,000+ Lucknow Super Giants and cricket markets, UPI and IMPS deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Uttar Pradesh: Lucknow Super Giants and cricket markets',
  UP_MAIN, UP_FAQ_SCHEMA)

# ─── WEST BENGAL ─────────────────────────────────────────────────────────────
WB_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Kolkata players bet at 1win?","acceptedAnswer":{"@type":"Answer","text":"1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in West Bengal continues to evolve; players should check current local rules before registering."}},
    {"@type":"Question","name":"What payment methods do West Bengal players use?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay is fastest. IMPS via UCO Bank and Bandhan Bank, which are based in Kolkata, are strong regional alternatives."}},
    {"@type":"Question","name":"Does 1win cover KKR matches?","acceptedAnswer":{"@type":"Answer","text":"Yes. Kolkata Knight Riders fixtures are fully listed with 40,000+ markets during IPL season, including live in-play and pre-match options."}},
    {"@type":"Question","name":"Does 1win support Bengali language users?","acceptedAnswer":{"@type":"Answer","text":"The main interface is in English. Bengali-speaking players can navigate the platform fully in English and access customer support via live chat."}},
    {"@type":"Question","name":"How do I claim the XLBONUS in West Bengal?","acceptedAnswer":{"@type":"Answer","text":"Register at 1win.codes/en/register with promo code XLBONUS. The welcome bonus is credited to your account after your first qualifying deposit."}}
  ]
}
</script>"""

WB_MAIN = """
<section class="lede">
  <p>West Bengal's sports culture blends cricket passion with one of India's deepest football traditions, and 1win serves both. Licensed under Curacao 8048/JAZ, 1win gives Kolkata players access to 40,000+ KKR cricket and football markets. Use promo code <span class="code-highlight">XLBONUS</span> at registration to unlock your welcome bonus and start betting on KKR, Mohun Bagan, and East Bengal fixtures from anywhere in West Bengal.</p>
</section>

<section class="local-context">
  <h2>1win and West Bengal: KKR cricket and Kolkata's football legacy</h2>
  <p>Kolkata occupies a unique position in Indian sports culture as the only major city where football rivals cricket for public passion. The Kolkata Derby between Mohun Bagan and East Bengal is one of the oldest and most fiercely contested club football rivalries in Asia, drawing massive crowds to the Salt Lake Stadium. On the cricket side, Kolkata Knight Riders, two-time IPL champions and one of the competition's most globally supported franchises, provide the city with a top-tier team to back each season. Bengali sports culture is deeply informed, with match analysis, commentary, and discussion taking place in both English and Bengali. The state's urban centres in Kolkata, Howrah, and Asansol represent a sizeable and engaged sports-watching audience across both sports.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in West Bengal</h2>
  <p>UPI via PhonePe and Google Pay covers the majority of digital transactions in Kolkata and West Bengal's urban belt. IMPS is particularly significant in West Bengal because two major banking institutions with national reach, UCO Bank and Bandhan Bank, are headquartered in Kolkata; their customers make up a substantial share of the IMPS user base in the state. Net banking via these regional banks is a reliable 1win deposit route for players who prefer traditional bank interfaces. Paytm Wallet retains strong recognition among older demographics in Kolkata, offering an accessible intermediary layer. Crypto deposits including USDT are accepted for players in Kolkata's tech and finance communities who hold digital assets. All deposit and withdrawal transactions are processed in INR without currency conversion fees for Indian players.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to West Bengal</h2>
  <p>KKR fixtures dominate West Bengal's cricket betting calendar at 1win during the IPL season. Markets cover match result, player performance, live in-play runs per over, and fielding outcomes. Football is where West Bengal truly distinguishes itself from other Indian states. 1win lists Indian Super League matches including those involving Mohun Bagan Super Giant (the ISL-playing entity), as well as the I-League, Premier League, Bundesliga, and Champions League. The Kolkata Derby, when scheduled, appears in the sports lobby as a featured match. Pro Kabaddi League coverage adds a third major sport, with the Bengal Warriors franchise representing the state. Casino rooms including live baccarat and Andar Bahar provide non-sports entertainment in a format familiar to Kolkata card game enthusiasts.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from West Bengal</h2>
  <ol>
    <li><strong>Go to the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> from your Kolkata-based device.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> to activate the welcome bonus before your first deposit.</li>
    <li><strong>Deposit via UPI or IMPS</strong> using PhonePe, Google Pay, UCO Bank, or Bandhan Bank net banking.</li>
    <li><strong>Choose your sport</strong>: KKR cricket in the IPL section or Mohun Bagan in the football tab.</li>
    <li><strong>Place your bet and follow live markets</strong> as they update in real time during your chosen match.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for West Bengal players</h2>
  <p>Online gaming regulation in West Bengal and across India continues to develop. Players should review current central and state-level rules before participating on any platform. 1win holds a Curacao 8048/JAZ licence and is accessible to players in West Bengal subject to local law compliance. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Kolkata players bet at 1win?</summary><p>1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in West Bengal continues to evolve; players should check current local rules before registering.</p></details>
  <details><summary>What payment methods do West Bengal players use?</summary><p>UPI via PhonePe and Google Pay is fastest. IMPS via UCO Bank and Bandhan Bank, which are based in Kolkata, are strong regional alternatives.</p></details>
  <details><summary>Does 1win cover KKR matches?</summary><p>Yes. Kolkata Knight Riders fixtures are fully listed with 40,000+ markets during IPL season, including live in-play and pre-match options.</p></details>
  <details><summary>Does 1win support Bengali language users?</summary><p>The main interface is in English. Bengali-speaking players can navigate the platform fully in English and access customer support via live chat.</p></details>
  <details><summary>How do I claim the XLBONUS in West Bengal?</summary><p>Register at 1win.codes/en/register with promo code XLBONUS. The welcome bonus is credited to your account after your first qualifying deposit.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/west-bengal',
  '1win Kolkata: KKR cricket, football betting and XLBONUS',
  'West Bengal players get 40,000+ KKR cricket and Kolkata football markets, UPI and IMPS deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win West Bengal: KKR cricket and football markets',
  WB_MAIN, WB_FAQ_SCHEMA)

# ─── GUJARAT ─────────────────────────────────────────────────────────────────
GJ_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Gujarat players use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win operates under a Curacao 8048/JAZ licence. Gujarat players should review current state and central online gaming regulations before registering."}},
    {"@type":"Question","name":"What deposit methods are popular in Ahmedabad?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay leads in Ahmedabad. IMPS through Gujarat-based banks including Bank of Baroda, headquartered in Vadodara, is a widely used alternative."}},
    {"@type":"Question","name":"Can I bet on Gujarat Titans at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. Gujarat Titans IPL fixtures are listed with 40,000+ markets including live in-play, top batsman, and match winner options."}},
    {"@type":"Question","name":"How do I use the XLBONUS in Gujarat?","acceptedAnswer":{"@type":"Answer","text":"Enter XLBONUS during registration at 1win.codes/en/register. The bonus activates on your first qualifying deposit."}},
    {"@type":"Question","name":"Does 1win accept deposits from Gujarat cooperative banks?","acceptedAnswer":{"@type":"Answer","text":"IMPS and net banking transfers from most scheduled commercial banks are supported. Verify your specific cooperative bank's IMPS availability before depositing."}}
  ]
}
</script>"""

GJ_MAIN = """
<section class="lede">
  <p>Gujarat Titans IPL fans and Ahmedabad sports bettors can access 1win, a Curacao 8048/JAZ licensed platform with 40,000+ cricket, kabaddi, and casino markets. Register with promo code <span class="code-highlight">XLBONUS</span> to start with a welcome bonus on your first deposit, whether you are in Ahmedabad, Surat, Vadodara, or Rajkot.</p>
</section>

<section class="local-context">
  <h2>1win and Gujarat: Gujarat Titans, Ahmedabad and an affluent market</h2>
  <p>Gujarat is one of India's wealthiest states, with Ahmedabad serving as a major commercial and textile hub and Surat as a global diamond trading centre. The state's high per-capita income and strong entrepreneurial culture create a consumer base with significant disposable income for entertainment including digital sports betting. Gujarat Titans, crowned IPL champions in their debut 2022 season, play at the Narendra Modi Stadium in Ahmedabad, the largest cricket ground in the world by capacity. This gives the state an immediate connection to top-level IPL cricket at home. Gujarat also hosts the Sabarmati Derby in football and has a meaningful audience for kabaddi through the Gujarat Fortune Giants in the Pro Kabaddi League.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Gujarat</h2>
  <p>UPI dominates digital payments in Gujarat's urban belt. PhonePe and Google Pay have near-universal smartphone-user adoption in Ahmedabad and Surat. IMPS via Bank of Baroda, headquartered in Vadodara, is a highly trusted route for Gujarat players making larger 1win deposits. The State Bank of India and HDFC Bank have extensive Gujarat branch networks; net banking through these institutions works seamlessly with the 1win deposit flow. Paytm Wallet is less dominant here than in North India but retains a user base among older demographics. Cooperative banks, while prominent in Gujarat's rural economy, may have variable IMPS support; players should confirm capability before choosing that route. Crypto deposits in USDT are accepted and popular among Gujarat's business community who hold crypto as a treasury asset.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Gujarat</h2>
  <p>Gujarat Titans matches are the top cricket betting events for Gujarat-based 1win users during the Indian Premier League season. Full GT fixture coverage includes pre-match winner markets, player-specific batting and bowling lines, and live ball-by-ball in-play options at the Narendra Modi Stadium or away venues. India international fixtures at Ahmedabad, including the historic home Tests, receive premium market depth. The Gujarat Fortune Giants in the Pro Kabaddi League carry a dedicated following; 1win lists PKL fixtures with raid and tackle outcome markets. Cricket aside, Gujarat's affluent Ahmedabad market includes casino users; 1win's live dealer section offers INR-compatible tables for baccarat, blackjack, and roulette in high and standard limit rooms.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Gujarat</h2>
  <ol>
    <li><strong>Access the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> from your device in Gujarat.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the bonus field to activate the welcome offer.</li>
    <li><strong>Deposit via UPI, PhonePe, or Bank of Baroda IMPS</strong> to fund your account instantly.</li>
    <li><strong>Open the sports lobby</strong> and search for Gujarat Titans or any live cricket match.</li>
    <li><strong>Place your first bet</strong> and explore in-play markets as they update during the match.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Gujarat players</h2>
  <p>Online gaming regulation in Gujarat is subject to applicable state and central law, which continues to evolve. Players should review current rules before participating on any online platform. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Gujarat players use 1win?</summary><p>1win operates under a Curacao 8048/JAZ licence. Gujarat players should review current state and central online gaming regulations before registering.</p></details>
  <details><summary>What deposit methods are popular in Ahmedabad?</summary><p>UPI via PhonePe and Google Pay leads in Ahmedabad. IMPS through Gujarat-based banks including Bank of Baroda, headquartered in Vadodara, is a widely used alternative.</p></details>
  <details><summary>Can I bet on Gujarat Titans at 1win?</summary><p>Yes. Gujarat Titans IPL fixtures are listed with 40,000+ markets including live in-play, top batsman, and match winner options.</p></details>
  <details><summary>How do I use the XLBONUS in Gujarat?</summary><p>Enter XLBONUS during registration at 1win.codes/en/register. The bonus activates on your first qualifying deposit.</p></details>
  <details><summary>Does 1win accept deposits from Gujarat cooperative banks?</summary><p>IMPS and net banking transfers from most scheduled commercial banks are supported. Verify your specific cooperative bank's IMPS availability before depositing.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/gujarat',
  '1win Gujarat: Gujarat Titans IPL markets, UPI deposits and XLBONUS',
  'Ahmedabad and Gujarat players get 40,000+ Gujarat Titans and IPL markets, UPI and IMPS deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Gujarat: Gujarat Titans IPL betting and UPI deposits',
  GJ_MAIN, GJ_FAQ_SCHEMA)

# ─── RAJASTHAN ───────────────────────────────────────────────────────────────
RJ_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Rajasthan players use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win holds a Curacao 8048/JAZ licence. Online gaming regulation in Rajasthan is subject to evolving central and state-level frameworks. Players should review applicable rules before registering."}},
    {"@type":"Question","name":"What payment methods work in Jaipur?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay is the fastest option in Jaipur. IMPS through Bank of Rajasthan (now ICICI merged) and SBI is a widely used alternative."}},
    {"@type":"Question","name":"Can I bet on Rajasthan Royals at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. Rajasthan Royals fixtures carry full 1win market coverage including pre-match and live in-play options across all IPL rounds."}},
    {"@type":"Question","name":"How do I claim the XLBONUS in Rajasthan?","acceptedAnswer":{"@type":"Answer","text":"Register at 1win.codes/en/register with promo code XLBONUS. The welcome bonus is applied to your first qualifying deposit automatically."}},
    {"@type":"Question","name":"Is 1win accessible in Jodhpur and Udaipur?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win is accessible from any internet-connected device across Rajasthan, including Jaipur, Jodhpur, Udaipur, and Kota."}}
  ]
}
</script>"""

RJ_MAIN = """
<section class="lede">
  <p>Rajasthan Royals fans and sports bettors across Jaipur, Jodhpur, and Udaipur can register at 1win, a Curacao 8048/JAZ licensed platform offering 40,000+ cricket and sports markets. Use promo code <span class="code-highlight">XLBONUS</span> at sign-up to activate a welcome bonus on your first deposit and access the full IPL betting lobby from anywhere in Rajasthan.</p>
</section>

<section class="local-context">
  <h2>1win and Rajasthan: Royals cricket and a growing digital market</h2>
  <p>Rajasthan Royals, winners of the inaugural IPL in 2008, carry a storied franchise history that commands loyalty across the state. The team plays home games at the Sawai Mansingh Stadium in Jaipur, one of cricket's most atmospheric venues. Jaipur itself, the Pink City and state capital, is evolving rapidly as a tech and startup hub, with IT parks drawing a digitally active young workforce. Jodhpur and Udaipur, major tourism and trade cities, add further population to Rajasthan's growing online entertainment market. Kabaddi has a strong traditional following across rural Rajasthan, supplemented by growing interest in the Jaipur Pink Panthers Pro Kabaddi League franchise. The state's overall online gaming user base is expanding steadily as smartphone and affordable data access improve across tier-2 cities.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Rajasthan</h2>
  <p>UPI via PhonePe and Google Pay covers the majority of digital transactions in Jaipur and other Rajasthan cities. IMPS through SBI, which has an extensive branch network across rural and urban Rajasthan, is a key option for players making larger deposits. Paytm Wallet has strong brand recognition in Rajasthan, where it was one of the first digital payment apps to gain rural adoption during the post-demonetisation period. Net banking via HDFC and ICICI is favoured by Jaipur's professional class. NEFT is an option for scheduled transactions with slightly longer processing but higher limit flexibility. Crypto deposits in USDT or BTC are accepted for Jaipur's growing startup and fintech community, who are increasingly comfortable with digital asset holdings.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Rajasthan</h2>
  <p>Rajasthan Royals IPL fixtures are the premier market for Rajasthan bettors on 1win. Full coverage spans pre-match odds, live in-play markets at Sawai Mansingh Stadium, player batting and bowling performance lines, and toss winner markets. India internationals held in Jaipur, including ODIs and T20Is, are listed with full market depth. The Jaipur Pink Panthers in the Pro Kabaddi League give Rajasthan fans a team to back in India's second-biggest sports league; 1win tracks all PKL fixtures. Football interest exists in Rajasthan's student population and urban centres, with Premier League and Champions League coverage available in the sports lobby. Casino users in Rajasthan can access 1win's live table games including Teen Patti and Andar Bahar in INR-compatible rooms.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Rajasthan</h2>
  <ol>
    <li><strong>Open the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> on your smartphone or computer.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the bonus field to secure the welcome offer before depositing.</li>
    <li><strong>Deposit via UPI, Paytm, or SBI IMPS</strong> to fund your account instantly.</li>
    <li><strong>Find Rajasthan Royals fixtures</strong> in the IPL section and add your selections to the bet slip.</li>
    <li><strong>Track live odds</strong> as the match progresses using the 1win in-play dashboard.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Rajasthan players</h2>
  <p>Online gaming in Rajasthan is governed by evolving central and state-level rules. Players should review current regulations before participating. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Rajasthan players use 1win?</summary><p>1win holds a Curacao 8048/JAZ licence. Online gaming regulation in Rajasthan is subject to evolving central and state-level frameworks. Players should review applicable rules before registering.</p></details>
  <details><summary>What payment methods work in Jaipur?</summary><p>UPI via PhonePe and Google Pay is the fastest option in Jaipur. IMPS through SBI is a widely used alternative.</p></details>
  <details><summary>Can I bet on Rajasthan Royals at 1win?</summary><p>Yes. Rajasthan Royals fixtures carry full 1win market coverage including pre-match and live in-play options across all IPL rounds.</p></details>
  <details><summary>How do I claim the XLBONUS in Rajasthan?</summary><p>Register at 1win.codes/en/register with promo code XLBONUS. The welcome bonus is applied to your first qualifying deposit automatically.</p></details>
  <details><summary>Is 1win accessible in Jodhpur and Udaipur?</summary><p>Yes. 1win is accessible from any internet-connected device across Rajasthan, including Jaipur, Jodhpur, Udaipur, and Kota.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/rajasthan',
  '1win Rajasthan: Royals IPL betting, Jaipur markets and XLBONUS',
  'Jaipur and Rajasthan players access 40,000+ Rajasthan Royals IPL markets, UPI deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Rajasthan: Rajasthan Royals IPL markets and UPI deposits',
  RJ_MAIN, RJ_FAQ_SCHEMA)

# ─── PUNJAB ──────────────────────────────────────────────────────────────────
PB_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Punjab players bet at 1win?","acceptedAnswer":{"@type":"Answer","text":"1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in Punjab evolves under central frameworks. Players should verify current applicable rules before registering."}},
    {"@type":"Question","name":"What payment methods do Punjab players prefer?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay is fastest. NEFT via Punjab National Bank, headquartered in New Delhi with major Punjab operations, is widely used for larger transfers."}},
    {"@type":"Question","name":"Can I bet on Punjab Kings IPL matches at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. Punjab Kings fixtures are listed with 40,000+ markets including live in-play and full pre-match coverage throughout the IPL season."}},
    {"@type":"Question","name":"How do I activate the XLBONUS in Punjab?","acceptedAnswer":{"@type":"Answer","text":"Enter XLBONUS in the promo code field when registering at 1win.codes/en/register. The bonus is credited after your first qualifying deposit."}},
    {"@type":"Question","name":"Does 1win cover kabaddi for Punjab fans?","acceptedAnswer":{"@type":"Answer","text":"Yes. Pro Kabaddi League fixtures are listed on 1win with full market coverage. Kabaddi has deep traditional roots in Punjab and the PKL season runs from July to November."}}
  ]
}
</script>"""

PB_MAIN = """
<section class="lede">
  <p>Punjab has one of India's most established sports betting cultures, and 1win, licensed under Curacao 8048/JAZ, brings this tradition to a digital platform with 40,000+ markets spanning IPL, kabaddi, and casino games. Register with promo code <span class="code-highlight">XLBONUS</span> and start betting on Punjab Kings and kabaddi from Chandigarh, Ludhiana, or Amritsar.</p>
</section>

<section class="local-context">
  <h2>1win and Punjab: Punjab Kings, kabaddi culture and a sporting state</h2>
  <p>Punjab's relationship with sport is embedded in its culture. Traditional village-level sports including wrestling, kabaddi, and athletics have been part of Punjabi life for generations, and that competitive spirit translates directly into enthusiasm for modern sports betting. Punjab Kings in the IPL play home matches at IS Bindra Stadium, Mohali, which sits within the Chandigarh tricity. Chandigarh, the shared capital of Punjab and Haryana, is a well-planned and prosperous city with high consumer spending and strong digital adoption. Ludhiana, Amritsar, and Jalandhar add further population density in the state. Kabaddi's pro circuit through the Pro Kabaddi League resonates particularly strongly in Punjab, where rural kabaddi tournaments predate the professional era by decades.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Punjab</h2>
  <p>UPI via PhonePe and Google Pay handles the bulk of everyday digital transactions in Punjab's urban centres. NEFT is disproportionately popular in Punjab relative to some other Indian states, partly because Punjab National Bank, one of India's largest lenders, has deep retail roots in the state despite being headquartered in Delhi. NEFT transfers from PNB accounts are a standard route for larger deposits into 1win. IMPS via PNB and other regional branches is available 24/7 for instant transfers when NEFT schedules are inconvenient. Paytm has maintained above-average adoption in Punjab through the Paytm Payments Bank rollout. Crypto deposits in USDT are accepted and used by Chandigarh's growing tech and startup community. Withdrawals process through the same payment channel as the deposit, typically completing within 24 hours.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Punjab</h2>
  <p>Punjab Kings IPL fixtures are the headline market for Punjab bettors on 1win, with full pre-match and live in-play coverage from the IS Bindra Stadium. Kabaddi is where Punjab truly differentiates its betting profile; 1win carries the full Pro Kabaddi League schedule with markets on raid points, total tackles, and match outcome. The state's strong wrestling culture finds an outlet in 1win's MMA and UFC markets, as well as any WFI-affiliated events that receive sports betting coverage. Football interest in Punjab is growing among younger demographics; Premier League and Champions League are fully listed. Hockey, with its deep Punjab roots as one of India's most successful hockey-producing states, receives dedicated market coverage when FIH Pro League and Hockey India League fixtures are scheduled.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Punjab</h2>
  <ol>
    <li><strong>Register at</strong> <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> from your Chandigarh, Ludhiana, or Amritsar device.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the bonus field to claim the welcome deposit offer.</li>
    <li><strong>Fund your account</strong> via UPI, NEFT through PNB, or IMPS for immediate credit.</li>
    <li><strong>Open IPL or kabaddi markets</strong> in the sports section and select your Punjab Kings or PKL fixture.</li>
    <li><strong>Confirm your bet</strong> and monitor live odds via the in-play tracker throughout the match.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Punjab players</h2>
  <p>Online gaming in Punjab is subject to applicable central government regulations and any state-level orders in force at the time of play. The regulatory environment for online gaming across India continues to evolve. Players are encouraged to review current rules before participating. 1win holds a Curacao 8048/JAZ licence. This page is informational only and does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Punjab players bet at 1win?</summary><p>1win operates under a Curacao 8048/JAZ licence. Online gaming regulation in Punjab evolves under central frameworks. Players should verify current applicable rules before registering.</p></details>
  <details><summary>What payment methods do Punjab players prefer?</summary><p>UPI via PhonePe and Google Pay is fastest. NEFT via Punjab National Bank, with major Punjab operations, is widely used for larger transfers.</p></details>
  <details><summary>Can I bet on Punjab Kings IPL matches at 1win?</summary><p>Yes. Punjab Kings fixtures are listed with 40,000+ markets including live in-play and full pre-match coverage throughout the IPL season.</p></details>
  <details><summary>How do I activate the XLBONUS in Punjab?</summary><p>Enter XLBONUS in the promo code field when registering at 1win.codes/en/register. The bonus is credited after your first qualifying deposit.</p></details>
  <details><summary>Does 1win cover kabaddi for Punjab fans?</summary><p>Yes. Pro Kabaddi League fixtures are listed on 1win with full market coverage. Kabaddi has deep traditional roots in Punjab and the PKL season runs from July to November.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/punjab',
  '1win Punjab: Punjab Kings IPL betting, kabaddi markets and XLBONUS',
  'Chandigarh and Punjab players get 40,000+ Punjab Kings IPL and kabaddi markets, UPI and NEFT deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Punjab: Punjab Kings IPL and kabaddi markets',
  PB_MAIN, PB_FAQ_SCHEMA)

# ─── KERALA ──────────────────────────────────────────────────────────────────
KL_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Kerala players use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win holds a Curacao 8048/JAZ licence. Online gaming regulation in Kerala is subject to evolving central and state frameworks. Players should check current applicable rules before registering."}},
    {"@type":"Question","name":"Does 1win cover football for Kerala fans?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win lists Premier League, Champions League, La Liga, Kerala Blasters ISL fixtures, and FIFA international matches with 40,000+ markets including live in-play options."}},
    {"@type":"Question","name":"Are crypto deposits available for Kerala players?","acceptedAnswer":{"@type":"Answer","text":"Yes. USDT and BTC deposits are accepted at 1win. Kerala has above-average crypto adoption driven by high English literacy and NRI remittance familiarity with digital finance."}},
    {"@type":"Question","name":"How do I claim XLBONUS in Kerala?","acceptedAnswer":{"@type":"Answer","text":"Register at 1win.codes/en/register using promo code XLBONUS. The welcome bonus is applied to your first qualifying deposit."}},
    {"@type":"Question","name":"What is the fastest deposit method in Kochi?","acceptedAnswer":{"@type":"Answer","text":"UPI via Google Pay or PhonePe is fastest for Kochi players, crediting your 1win account instantly. IMPS is a reliable backup for larger amounts."}}
  ]
}
</script>"""

KL_MAIN = """
<section class="lede">
  <p>Kerala stands apart from most Indian states: football rivals and often surpasses cricket in local passion. 1win, licensed under Curacao 8048/JAZ, carries 40,000+ football and cricket markets for Kerala players, alongside casino and live dealer options. Register with promo code <span class="code-highlight">XLBONUS</span> and start betting on the Premier League, Kerala Blasters, and FIFA tournaments from Kochi, Thiruvananthapuram, or Kozhikode.</p>
</section>

<section class="local-context">
  <h2>1win and Kerala: football-mad state with high English literacy</h2>
  <p>Kerala's sports culture is genuinely distinct within India. While cricket is followed, football commands a level of grassroots passion that is closer to South American football culture than to other Indian states. The Santosh Trophy, district-level tournaments, and club rivalries run deep. Kerala Blasters in the ISL draw enormous support, and the Jawaharlal Nehru International Stadium in Kochi is routinely one of the best-attended ISL grounds. Kerala also has the highest English literacy rate among Indian states, at over 95%, making English-language betting platforms like 1win naturally accessible to the population. The NRI diaspora from Gulf countries, which includes millions of Keralites, adds a segment that is comfortable with digital finance tools including crypto wallets and international transfer systems.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Kerala</h2>
  <p>UPI via Google Pay and PhonePe covers most digital payment needs in Kochi, Thiruvananthapuram, and Kozhikode. Crypto deposits are more popular in Kerala than in most other Indian states. The state's large NRI community is accustomed to cross-border digital finance, and USDT via TRC-20 is a convenient option for players who receive remittances in crypto or hold digital assets. IMPS through Federal Bank and South Indian Bank, both headquartered in Kerala, is the preferred bank-transfer route for larger 1win deposits. Paytm Wallet usage is moderate; the platform is known but faces strong UPI competition. Net banking via Federal Bank and Dhanlaxmi Bank covers players who prefer browser-based banking transactions. Withdrawal processing typically completes within a few hours for UPI and within one business day for bank transfers.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Kerala</h2>
  <p>Football is the primary market segment for Kerala players on 1win. Premier League coverage spans all 380 fixtures per season with full pre-match and live in-play markets. Champions League group stage through the final carries deep market depth including goalscorer, correct score, and corner count lines. La Liga and Bundesliga are fully listed for fans who follow Keralite players abroad or simply prefer European club football. Kerala Blasters ISL home and away fixtures are trackable in the sports lobby throughout the ISL season. FIFA World Cup qualifying and tournament fixtures receive premium market coverage. Cricket remains available for Kerala players who follow the IPL casually; all 10 IPL franchises are listed. Casino options include live blackjack and baccarat rooms compatible with INR, appealing to Kerala's entertainment-savvy audience.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Kerala</h2>
  <ol>
    <li><strong>Open the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> in your browser.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the bonus field to activate the welcome deposit offer.</li>
    <li><strong>Deposit via Google Pay, Federal Bank IMPS, or USDT</strong> depending on your preferred payment method.</li>
    <li><strong>Go to the football section</strong> and find the Premier League, Champions League, or Kerala Blasters fixture.</li>
    <li><strong>Place your bet</strong> and follow in-play markets with live stats as the match progresses.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Kerala players</h2>
  <p>Online gaming in Kerala is governed by applicable central and state legislation, which continues to evolve. Players should review current rules before participating on any platform. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Kerala players use 1win?</summary><p>1win holds a Curacao 8048/JAZ licence. Online gaming regulation in Kerala is subject to evolving central and state frameworks. Players should check current applicable rules before registering.</p></details>
  <details><summary>Does 1win cover football for Kerala fans?</summary><p>Yes. 1win lists Premier League, Champions League, La Liga, Kerala Blasters ISL fixtures, and FIFA international matches with 40,000+ markets including live in-play options.</p></details>
  <details><summary>Are crypto deposits available for Kerala players?</summary><p>Yes. USDT and BTC deposits are accepted at 1win. Kerala has above-average crypto adoption driven by high English literacy and NRI remittance familiarity with digital finance.</p></details>
  <details><summary>How do I claim XLBONUS in Kerala?</summary><p>Register at 1win.codes/en/register using promo code XLBONUS. The welcome bonus is applied to your first qualifying deposit.</p></details>
  <details><summary>What is the fastest deposit method in Kochi?</summary><p>UPI via Google Pay or PhonePe is fastest for Kochi players, crediting your 1win account instantly. IMPS is a reliable backup for larger amounts.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/kerala',
  '1win Kerala: Premier League and Kerala Blasters betting with XLBONUS',
  'Kerala players get 40,000+ football and cricket markets, UPI and crypto deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Kerala: football and Premier League markets',
  KL_MAIN, KL_FAQ_SCHEMA)

# ─── ANDHRA PRADESH ──────────────────────────────────────────────────────────
AP_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Andhra Pradesh players use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win holds a Curacao 8048/JAZ licence. Andhra Pradesh has enacted state-level online gaming regulations; players should review current local rules before registering."}},
    {"@type":"Question","name":"Does 1win list Sunrisers Hyderabad matches?","acceptedAnswer":{"@type":"Answer","text":"Yes. Sunrisers Hyderabad IPL fixtures are fully covered with 40,000+ markets including live in-play options at Rajiv Gandhi International Cricket Stadium."}},
    {"@type":"Question","name":"What payment methods work in Visakhapatnam?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay is the fastest route. IMPS through Andhra Bank (merged with Union Bank) and Indian Bank are reliable alternatives."}},
    {"@type":"Question","name":"How do I get the XLBONUS in Andhra Pradesh?","acceptedAnswer":{"@type":"Answer","text":"Enter XLBONUS in the promo code field during registration at 1win.codes/en/register. The welcome bonus is credited after your first qualifying deposit."}},
    {"@type":"Question","name":"Is cricket the main sport for Andhra Pradesh bettors?","acceptedAnswer":{"@type":"Answer","text":"Cricket, especially IPL, dominates. Kabaddi through the Telugu Titans and football via local ISL interest also have dedicated follower bases in the state."}}
  ]
}
</script>"""

AP_MAIN = """
<section class="lede">
  <p>Andhra Pradesh players, from Visakhapatnam's port city to the new state capital Amaravati, can access 1win, a Curacao 8048/JAZ licensed platform carrying 40,000+ markets across IPL cricket, kabaddi, and casino games. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to claim the welcome bonus and start betting on Sunrisers Hyderabad and other major cricket events from anywhere in the state.</p>
</section>

<section class="local-context">
  <h2>1win and Andhra Pradesh: Sunrisers Hyderabad and Vizag's cricket base</h2>
  <p>Andhra Pradesh shares the Sunrisers Hyderabad IPL franchise with the newly formed state of Telangana; the team's home ground, Rajiv Gandhi International Cricket Stadium, sits in Hyderabad but draws its fanbase equally from both states. Visakhapatnam, Andhra's largest city and a major port and industrial hub, hosts international cricket at Dr. Y.S. Rajasekhara Reddy ACA-VDCA Stadium and has an intensely cricket-following public. The state's coastal geography, IT parks in the Vizag tech corridor, and a large student population in Vijayawada and Guntur contribute to a sizeable and digitally active sports audience. The Telugu Titans Pro Kabaddi League franchise represents the state on a national stage beyond cricket. Andhra Pradesh has enacted specific online gaming legislation; players should review current requirements before participating.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Andhra Pradesh</h2>
  <p>UPI adoption in Andhra Pradesh is very high, driven partly by a strong Aadhaar-linked banking infrastructure and state government digital payments initiatives. PhonePe and Google Pay are the dominant apps across Visakhapatnam and Vijayawada. IMPS via Andhra Bank, which merged into Union Bank of India, and Indian Bank, which absorbed Allahabad Bank, are reliable routes for players making larger 1win deposits from Andhra-based accounts. Canara Bank, with strong Andhra Pradesh operations, also supports IMPS. Net banking is favoured by the IT-sector workforce in Vizag's tech parks. Paytm retains moderate adoption in smaller towns. Crypto deposits via USDT are accepted for tech workers in the Vizag Special Economic Zone who hold digital assets as part of investment portfolios.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Andhra Pradesh</h2>
  <p>Sunrisers Hyderabad IPL fixtures are the top draw for Andhra Pradesh bettors on 1win, with coverage spanning pre-match winner markets, live ball-by-ball in-play, player performance lines including Bhuvneshwar Kumar bowling figures, and total boundaries. International fixtures at the Vizag ACA-VDCA ground receive full market listings when India plays there. The Telugu Titans Pro Kabaddi League schedule is tracked with raid outcome, tackle, and match result markets throughout the PKL season. Football coverage through the ISL and European leagues serves Andhra's student and urban market. Casino options including live Teen Patti and baccarat are available in INR-compatible rooms, providing non-sports entertainment alternatives.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Andhra Pradesh</h2>
  <ol>
    <li><strong>Access the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> from your device in AP.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> to activate the welcome bonus before making your deposit.</li>
    <li><strong>Deposit via UPI, Union Bank IMPS, or Canara Bank net banking</strong> for instant account credit.</li>
    <li><strong>Open the IPL section</strong> and find Sunrisers Hyderabad or any active cricket match to build your bet slip.</li>
    <li><strong>Place your bet and follow live</strong> using 1win's in-play tracker and real-time odds updates.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Andhra Pradesh players</h2>
  <p>Andhra Pradesh has enacted state-level legislation regulating online gaming. The legislative and regulatory environment continues to evolve, and players are strongly advised to review current applicable rules before participating on any platform. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Andhra Pradesh players use 1win?</summary><p>1win holds a Curacao 8048/JAZ licence. Andhra Pradesh has enacted state-level online gaming regulations; players should review current local rules before registering.</p></details>
  <details><summary>Does 1win list Sunrisers Hyderabad matches?</summary><p>Yes. Sunrisers Hyderabad IPL fixtures are fully covered with 40,000+ markets including live in-play options at Rajiv Gandhi International Cricket Stadium.</p></details>
  <details><summary>What payment methods work in Visakhapatnam?</summary><p>UPI via PhonePe and Google Pay is the fastest route. IMPS through Union Bank of India and Indian Bank are reliable alternatives.</p></details>
  <details><summary>How do I get the XLBONUS in Andhra Pradesh?</summary><p>Enter XLBONUS in the promo code field during registration at 1win.codes/en/register. The welcome bonus is credited after your first qualifying deposit.</p></details>
  <details><summary>Is cricket the main sport for Andhra Pradesh bettors?</summary><p>Cricket, especially IPL, dominates. Kabaddi through the Telugu Titans and football via local ISL interest also have dedicated follower bases in the state.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/andhra-pradesh',
  '1win Andhra Pradesh: Sunrisers Hyderabad betting, UPI and XLBONUS',
  'AP players from Visakhapatnam to Vijayawada get 40,000+ SRH and cricket markets, UPI deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Andhra Pradesh: Sunrisers Hyderabad and cricket markets',
  AP_MAIN, AP_FAQ_SCHEMA)

# ─── TELANGANA ───────────────────────────────────────────────────────────────
TG_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can Telangana players use 1win?","acceptedAnswer":{"@type":"Answer","text":"1win operates under a Curacao 8048/JAZ licence. Telangana has enacted state-level online gaming regulations; players should review current local rules before registering."}},
    {"@type":"Question","name":"What deposit methods work best in Hyderabad?","acceptedAnswer":{"@type":"Answer","text":"UPI via PhonePe and Google Pay is fastest for Hyderabad's tech-worker demographic. Crypto deposits via USDT are popular in the city's startup community."}},
    {"@type":"Question","name":"Does 1win cover Sunrisers Hyderabad matches?","acceptedAnswer":{"@type":"Answer","text":"Yes. Sunrisers Hyderabad IPL fixtures are listed with 40,000+ pre-match and live in-play markets throughout the IPL season."}},
    {"@type":"Question","name":"How do I get the XLBONUS in Telangana?","acceptedAnswer":{"@type":"Answer","text":"Register at 1win.codes/en/register and enter XLBONUS in the promo code field. The welcome bonus is credited after your first qualifying deposit."}},
    {"@type":"Question","name":"Is 1win popular with Hyderabad IT workers?","acceptedAnswer":{"@type":"Answer","text":"Yes. Hyderabad's large tech-worker population is a strong demographic for 1win, with high digital literacy, UPI adoption, and familiarity with online entertainment platforms."}}
  ]
}
</script>"""

TG_MAIN = """
<section class="lede">
  <p>Hyderabad's tech-worker demographic and Telangana's cricket-passionate public have a natural home at 1win, a Curacao 8048/JAZ licensed platform with 40,000+ IPL, kabaddi, and casino markets. Register with promo code <span class="code-highlight">XLBONUS</span> and start betting on Sunrisers Hyderabad and the full sporting calendar from Hyderabad, Warangal, or Nizamabad.</p>
</section>

<section class="local-context">
  <h2>1win and Telangana: Hyderabad metro, SRH and high tech-worker demographic</h2>
  <p>Telangana was carved from Andhra Pradesh in 2014 and has built a distinct identity anchored on Hyderabad, one of India's four major IT metros alongside Bengaluru, Pune, and Chennai. HITEC City, Cyberabad, and the Gachibowli corridor house the Indian operations of global tech giants including Microsoft, Google, Amazon, and Meta, as well as major domestic IT firms. This creates one of India's densest concentrations of high-income, digitally fluent young professionals, a demographic at ease with online platforms, UPI payments, and even crypto. Sunrisers Hyderabad, representing the city in the IPL, enjoy passionate Telangana support at the Rajiv Gandhi International Cricket Stadium. The state's strong student and professional population in Warangal and Karimnagar adds further coverage outside Hyderabad.</p>
</section>

<section class="payments">
  <h2>Payment methods popular in Telangana</h2>
  <p>UPI adoption in Hyderabad is among the highest in India, reflecting the city's tech-worker demographic who are early adopters of digital financial tools. PhonePe and Google Pay are the primary apps, with near-universal adoption among working professionals. Crypto deposits are more popular in Hyderabad than in most Indian cities. Telangana's IT sector employees frequently hold USDT or ETH as part of investment portfolios, and 1win accepts USDT deposits with immediate on-chain confirmation via TRC-20. IMPS through HDFC, ICICI, and State Bank of Hyderabad (now merged with SBI) is the standard bank-transfer option for larger deposits. Net banking through major private and PSU banks is fully supported. Paytm has moderate but declining market share in Hyderabad relative to UPI-native apps. Withdrawals route through the original deposit method, with UPI withdrawals typically processing within a few hours.</p>
</section>

<section class="sports-markets">
  <h2>Sports markets relevant to Telangana</h2>
  <p>Sunrisers Hyderabad IPL fixtures are the flagship market for Telangana bettors on 1win, with comprehensive pre-match and ball-by-ball live in-play coverage throughout the season. Hyderabad's HITEC City audience also drives demand for non-cricket markets. Football is well-followed in the city's young professional community; 1win lists Premier League, Champions League, Europa League, and ISL fixtures with full market depth. Esports betting, while nascent in the Indian regulatory context, is an emerging interest among Hyderabad's gaming developer community; 1win monitors this segment. Casino markets including live blackjack, roulette, and baccarat in INR-compatible high-limit rooms are popular with Hyderabad's high-income earner segment. Kabaddi via the Telangana Draavida franchise in the PKL provides a homegrown team market throughout the season.</p>
</section>

<section class="how-to">
  <h2>How to start betting at 1win from Telangana</h2>
  <ol>
    <li><strong>Open the register page</strong> at <a href="https://1win.codes/en/register?promo=XLBONUS">1win.codes/en/register</a> on your Hyderabad device.</li>
    <li><strong>Enter promo code <span class="code-highlight">XLBONUS</span></strong> in the promo field to secure the welcome deposit bonus.</li>
    <li><strong>Deposit via PhonePe UPI, USDT, or HDFC net banking</strong> for instant account funding.</li>
    <li><strong>Find the Sunrisers Hyderabad fixture</strong> in the IPL section or browse football and kabaddi markets.</li>
    <li><strong>Confirm your bet</strong> and use the live in-play tracker to follow odds in real time during the match.</li>
  </ol>
</section>

<section class="legal-note">
  <h2>Legal note for Telangana players</h2>
  <p>Telangana has enacted state-level online gaming regulations and the framework continues to evolve. Players are encouraged to review current local rules before participating. 1win holds a Curacao 8048/JAZ licence. This page does not constitute legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Can Telangana players use 1win?</summary><p>1win operates under a Curacao 8048/JAZ licence. Telangana has enacted state-level online gaming regulations; players should review current local rules before registering.</p></details>
  <details><summary>What deposit methods work best in Hyderabad?</summary><p>UPI via PhonePe and Google Pay is fastest for Hyderabad's tech-worker demographic. Crypto deposits via USDT are popular in the city's startup community.</p></details>
  <details><summary>Does 1win cover Sunrisers Hyderabad matches?</summary><p>Yes. Sunrisers Hyderabad IPL fixtures are listed with 40,000+ pre-match and live in-play markets throughout the IPL season.</p></details>
  <details><summary>How do I get the XLBONUS in Telangana?</summary><p>Register at 1win.codes/en/register and enter XLBONUS in the promo code field. The welcome bonus is credited after your first qualifying deposit.</p></details>
  <details><summary>Is 1win popular with Hyderabad IT workers?</summary><p>Yes. Hyderabad's large tech-worker population is a strong demographic for 1win, with high digital literacy, UPI adoption, and familiarity with online entertainment platforms.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>
"""

w('india/telangana',
  '1win Hyderabad: SRH IPL betting for Telangana players with XLBONUS',
  'Hyderabad and Telangana players get 40,000+ SRH IPL markets, PhonePe UPI and USDT deposits, and the XLBONUS welcome offer at 1win. Curacao 8048/JAZ licensed.',
  '1win Telangana: Sunrisers Hyderabad markets and USDT deposits',
  TG_MAIN, TG_FAQ_SCHEMA)

# ─── INDEX PAGE ──────────────────────────────────────────────────────────────
INDEX_FAQ_SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Does 1win operate in India?","acceptedAnswer":{"@type":"Answer","text":"1win holds a Curacao 8048/JAZ licence and is accessible to Indian players across most states. Online gaming regulation in India is set at the state level and continues to evolve."}},
    {"@type":"Question","name":"Which Indian states are covered in 1win's state guides?","acceptedAnswer":{"@type":"Answer","text":"1win provides dedicated guides for Maharashtra, Tamil Nadu, Karnataka, Delhi, Uttar Pradesh, West Bengal, Gujarat, Rajasthan, Punjab, Kerala, Andhra Pradesh, and Telangana."}},
    {"@type":"Question","name":"What is the XLBONUS promo code?","acceptedAnswer":{"@type":"Answer","text":"XLBONUS is 1win's welcome promo code for new players. Enter it during registration to activate the welcome deposit bonus."}},
    {"@type":"Question","name":"Which payment methods does 1win support for Indian players?","acceptedAnswer":{"@type":"Answer","text":"1win supports UPI (PhonePe, Google Pay), Paytm Wallet, IMPS, NEFT, net banking through major Indian banks, and crypto deposits including USDT."}},
    {"@type":"Question","name":"Does 1win cover IPL betting?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win carries 40,000+ IPL markets across all 10 franchises, including live in-play betting, pre-match lines, and player performance markets throughout the season."}}
  ]
}
</script>"""

STATES = [
    ('Maharashtra', 'maharashtra', 'Mumbai, Pune', 'Mumbai Indians'),
    ('Tamil Nadu', 'tamil-nadu', 'Chennai', 'Chennai Super Kings'),
    ('Karnataka', 'karnataka', 'Bengaluru', 'Royal Challengers Bengaluru'),
    ('Delhi', 'delhi', 'Delhi NCR', 'Delhi Capitals'),
    ('Uttar Pradesh', 'uttar-pradesh', 'Lucknow, Kanpur', 'Lucknow Super Giants'),
    ('West Bengal', 'west-bengal', 'Kolkata', 'Kolkata Knight Riders'),
    ('Gujarat', 'gujarat', 'Ahmedabad, Surat', 'Gujarat Titans'),
    ('Rajasthan', 'rajasthan', 'Jaipur, Jodhpur', 'Rajasthan Royals'),
    ('Punjab', 'punjab', 'Chandigarh, Ludhiana', 'Punjab Kings'),
    ('Kerala', 'kerala', 'Kochi, Thiruvananthapuram', 'Kerala Blasters (ISL / football focus)'),
    ('Andhra Pradesh', 'andhra-pradesh', 'Visakhapatnam, Vijayawada', 'Sunrisers Hyderabad'),
    ('Telangana', 'telangana', 'Hyderabad', 'Sunrisers Hyderabad'),
]

state_cards_html = '\n'.join(
    f'''    <article class="state-card">
      <h2><a href="/en/india/{slug}/">{name}</a></h2>
      <p class="state-meta">{cities}</p>
      <p class="state-team">IPL / sport: {team}</p>
      <a class="btn btn-secondary" href="/en/india/{slug}/">Open guide</a>
    </article>'''
    for name, slug, cities, team in STATES
)

map_html = '''
<section class="india-map-visual" aria-label="India state coverage map">
  <div class="map-container">
    <svg viewBox="0 0 400 420" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" class="india-outline">
      <!-- Schematic India outline blocks representing regional coverage -->
      <!-- North -->
      <rect x="140" y="30" width="80" height="50" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="180" y="60" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Punjab / Delhi</text>
      <!-- North-West -->
      <rect x="60" y="80" width="80" height="60" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="100" y="114" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Rajasthan</text>
      <!-- North-East center -->
      <rect x="200" y="80" width="80" height="60" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="240" y="114" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Uttar Pradesh</text>
      <!-- East -->
      <rect x="290" y="100" width="80" height="60" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="330" y="134" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">West Bengal</text>
      <!-- West -->
      <rect x="50" y="150" width="80" height="60" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="90" y="184" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Gujarat</text>
      <!-- Centre West -->
      <rect x="120" y="150" width="100" height="70" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="170" y="189" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Maharashtra</text>
      <!-- South Deccan -->
      <rect x="190" y="220" width="100" height="60" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="240" y="254" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Telangana / AP</text>
      <!-- South West -->
      <rect x="100" y="290" width="80" height="50" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="140" y="319" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Karnataka</text>
      <!-- Tamil Nadu -->
      <rect x="190" y="300" width="80" height="50" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="230" y="329" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Tamil Nadu</text>
      <!-- Kerala -->
      <rect x="100" y="350" width="70" height="50" rx="6" fill="var(--c-accent)" opacity="0.18"/>
      <text x="135" y="379" text-anchor="middle" font-size="11" fill="var(--c-accent)" font-family="sans-serif">Kerala</text>
    </svg>
    <p class="map-note">Schematic coverage map. Select a state card below for the full guide.</p>
  </div>
</section>
'''

INDEX_MAIN = f"""
<section class="lede">
  <p>1win is a Curacao 8048/JAZ licensed sports betting and casino platform serving Indian players across 12 states with 40,000+ markets on IPL cricket, football, kabaddi, and live casino games. Use promo code <span class="code-highlight">XLBONUS</span> when you register to unlock the welcome bonus and start betting in minutes from your state.</p>
</section>

<section class="india-overview">
  <h2>India state betting guides</h2>
  <p>Select your state below to find local payment methods, your IPL team's markets, and a step-by-step guide to claiming your <span class="code-highlight">XLBONUS</span> welcome offer at 1win.</p>
</section>

{map_html}

<section class="state-grid">
  <h2>Choose your state</h2>
  <div class="state-cards">
{state_cards_html}
  </div>
</section>

<section class="india-payments">
  <h2>Payment methods across India</h2>
  <p>1win supports all major Indian payment methods: UPI (PhonePe, Google Pay), Paytm Wallet, IMPS, NEFT, net banking via SBI, HDFC, ICICI, Axis, and regional banks including Federal Bank, UCO Bank, and Bandhan Bank. Crypto deposits via USDT (TRC-20) are also accepted. Minimum deposit requirements apply. Withdrawals route through the same channel used for the deposit, with UPI withdrawals typically processing within hours and bank transfers within one business day.</p>
</section>

<section class="india-ipl">
  <h2>IPL coverage at 1win</h2>
  <p>During the Indian Premier League, 1win carries full coverage of all 10 franchises across 74 matches per season. Markets include pre-match winner, toss, top run scorer, top wicket taker, most fours, most sixes, player of the match, and ball-by-ball live in-play markets that update in real time. Each state page links directly to that state's IPL team coverage. All IPL markets are accessible with a single 1win account regardless of which state you are in.</p>
</section>

<section class="legal-note">
  <h2>Legal note for Indian players</h2>
  <p>Online gaming and sports betting in India is regulated at the state level, with the central government providing a framework under the IT Act. The landscape continues to evolve, with several states enacting or amending their own online gaming statutes. Players should review current local rules applicable to their state before registering. 1win holds a Curacao 8048/JAZ licence. Nothing on this page or any linked state page constitutes legal advice.</p>
</section>

<section class="faq">
  <h2>FAQ</h2>
  <details><summary>Does 1win operate in India?</summary><p>1win holds a Curacao 8048/JAZ licence and is accessible to Indian players across most states. Online gaming regulation in India is set at the state level and continues to evolve.</p></details>
  <details><summary>Which Indian states are covered in 1win's state guides?</summary><p>1win provides dedicated guides for Maharashtra, Tamil Nadu, Karnataka, Delhi, Uttar Pradesh, West Bengal, Gujarat, Rajasthan, Punjab, Kerala, Andhra Pradesh, and Telangana.</p></details>
  <details><summary>What is the XLBONUS promo code?</summary><p>XLBONUS is 1win's welcome promo code for new players. Enter it during registration to activate the welcome deposit bonus.</p></details>
  <details><summary>Which payment methods does 1win support for Indian players?</summary><p>1win supports UPI (PhonePe, Google Pay), Paytm Wallet, IMPS, NEFT, net banking through major Indian banks, and crypto deposits including USDT.</p></details>
  <details><summary>Does 1win cover IPL betting?</summary><p>Yes. 1win carries 40,000+ IPL markets across all 10 franchises, including live in-play betting, pre-match lines, and player performance markets throughout the season.</p></details>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<style>
.state-cards {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1.25rem;
  margin-top: 1rem;
}}
.state-card {{
  border: 1px solid var(--c-border, #e2e8f0);
  border-radius: 10px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}}
.state-card h2 {{ margin: 0; font-size: 1.1rem; }}
.state-card h2 a {{ text-decoration: none; color: inherit; }}
.state-meta, .state-team {{ margin: 0; font-size: 0.875rem; color: var(--c-muted, #64748b); }}
.state-card .btn-secondary {{
  margin-top: auto;
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  background: transparent;
  border: 1px solid currentColor;
  text-decoration: none;
  font-size: 0.875rem;
  text-align: center;
}}
.india-map-visual {{ margin: 2rem 0; text-align: center; }}
.map-container {{ display: inline-block; max-width: 420px; width: 100%; }}
.india-outline {{ width: 100%; height: auto; display: block; margin: 0 auto; }}
.map-note {{ font-size: 0.8rem; color: var(--c-muted, #64748b); margin-top: 0.5rem; }}
</style>
"""

# Index page uses different breadcrumbs
def w_index():
    html = render_page(
        slug='india/index',
        title='1win India: state-by-state betting guides, UPI deposits and XLBONUS',
        description='1win India hub: 12 state guides covering IPL cricket, football, kabaddi markets, UPI and USDT deposits, and the XLBONUS welcome offer. Curacao 8048/JAZ licensed.',
        h1='1win India: state betting guides and IPL markets',
        breadcrumbs=[
            ('Home', '/en/'),
            ('India', None),
        ],
        main_html=INDEX_MAIN,
        extra_schema=INDEX_FAQ_SCHEMA,
    )
    path = os.path.join(REPO, 'en', 'india', 'index.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  wrote {path}')

w_index()

print('\nAll pages written. Running verification...\n')

import re, glob as _glob

files = _glob.glob(os.path.join(REPO, 'en', 'india', '*.html'))
assert len(files) == 13, f'expected 13, got {len(files)}: {files}'
titles = set()
for f in files:
    t = open(f, encoding='utf-8').read()
    assert '\u2014' not in t, f'em dash in {f}'   # —
    assert '\u2013' not in t, f'en dash in {f}'   # –
    for b in ['HIT THE TABLES','DOMINATE EVERY MATCH','OUTPLAY EVERYONE','no strings attached','thousands of','hundreds of','world-class','cutting-edge']:
        assert b.lower() not in t.lower(), f'banned "{b}" in {f}'
    assert 'XLBONUS' in t, f'no XLBONUS in {f}'
    assert 'Cura\u00e7ao' in t or 'Curacao' in t, f'no Curacao trust signal in {f}'
    tm = re.search(r'<title>(.*?)</title>', t)
    assert tm, f'no <title> in {f}'
    title_val = tm.group(1)
    assert title_val not in titles, f'duplicate title: {title_val}'
    titles.add(title_val)
    wc = len(t.split())
    print(f'  OK  {os.path.basename(f):30s}  {wc} words  title={title_val[:55]}')

print(f'\nPASS {len(files)} files, {len(titles)} unique titles')
