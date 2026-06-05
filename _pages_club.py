# -*- coding: utf-8 -*-
"""Page definitions for the 11 EN WinnersClub pages."""
from _build_club import (AFF, head, header, hero, voice_player, girl_break,
                         faq_section, signature, sticky_cta, footer, page, section,
                         jsonld_webpage, jsonld_breadcrumb, jsonld_faq)

CODE = '<span class="code-highlight">MAXBET</span>'
LIC = "Curaçao 1668/JAZ"
HOME = ("Home", "https://winnersclub.com/")

# ============================================================ HOMEPAGE
def build_home():
    path = ""
    title = "WinnersClub - Inside the Stake Club | Code MAXBET, 200% up to $3,000"
    desc = "The players' insider club for Stake. Use MAXBET at Stake.com for 200% up to $3,000 plus 400 free spins. Medium Rare NV, Curaçao 1668/JAZ licensed, since 2017."
    jl = [jsonld_webpage(title, desc, ""),
          jsonld_breadcrumb([HOME])]
    faqs = [
      ("Is MAXBET the biggest Stake bonus code?",
       "Yes. 200% match up to $3,000 plus 400 free spins. Most public codes max at 100% / $1,000. MAXBET is the code the club hands out at the door."),
      ("Is Stake.com legit?",
       "Stake holds a Curaçao 1668/JAZ licence under Medium Rare NV, operating since 2017. On-chain reserves sit around $320M, publicly traceable on Arkham. Founders Ed Craven and Bijan Tehrani also run Kick."),
      ("Can I see Stake's reserves?",
       "Yes, see <a href='/reserves/'>the reserves briefing</a>. Roughly $320M in publicly identifiable wallets, mostly ETH and stablecoins, all traceable on Arkham Intel."),
      ("Where can I play?",
       "The Curaçao licence covers most of the world, but Stake self-restricts the US, the UK, parts of Australia and a handful of others. Use <a href='/mirror/'>the mirrors page</a> to find your regional domain."),
      ("How fast are withdrawals?",
       "Crypto is instant to one hour. Bank transfers take up to 3 days. Cards 2 to 5 days. Full detail on <a href='/payments/'>the payments page</a>."),
    ]
    jl.append(jsonld_faq([(q, __import__('re').sub('<[^>]+>','',a)) for q,a in faqs]))

    h = head(title, desc, path, jsonld=jl)

    secs = []
    secs.append(hero(
        "girl-homepage-3.webp",
        "If you found this page, you found the club.",
        "inside the club.",
        f"The players' insider club for Stake. Whisper {CODE} to the dealer and the door's open. The club's been at Stake since 2017, licensed {LIC}.",
        "Claim 200% up to $3,000 at Stake.com", AFF,
        "Learn what MAXBET unlocks", "/promo-code/"))

    # reserves ticker
    ticker = ("Stake on-chain right now: $320M+ portfolio &middot; 86.7K ETH &middot; 59.3M USDT &middot; "
              "50.1M USDC &middot; 438K SOL &middot; Curaçao 1668/JAZ licensed &middot; Source: Arkham Intel &middot; Updated June 2026")
    secs.append(f'''  <div class="reserves-ticker"><div class="rt-inner"><span>{ticker}</span><span>{ticker}</span></div></div>
''')

    # why the club
    why = '''<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>A real bonus</h3><p>MAXBET beats every public code. 200% up to $3,000 plus 400 free spins. The codes you find elsewhere stop at 100% and a grand.</p></div>
        <div class="club-card"><h3>Verified solvency</h3><p>Around $320M in reserves you can trace yourself on Arkham. No proof-of-reserves theatre, the wallets are public.</p></div>
        <div class="club-card"><h3>Real owners</h3><p>Ed Craven and Bijan Tehrani founded Stake in 2017 and launched Kick in 2022. The house has a face, and it stays.</p></div>
      </div>'''
    secs.append(section('Why the <span class="text-gradient-gold">club</span>', why))

    # five verticals
    verts = [("Casino","girl-casino-2.webp","/casino/"),("Sportsbook","girl-sports-2.webp","/sports/"),
             ("Poker","girl-poker-2.webp","/poker/"),("Aviator","girl-aviator-2.webp","/aviator/"),
             ("Live","girl-lucky-drive-2.webp","/live-odds/")]
    cards = ""
    for name,img,href in verts:
        cards += f'''<a href="{href}" class="vertical-card"><div class="vc-bg" style="background-image:url('/images/{img}');"></div><div class="vc-ov"></div><div class="vc-label">{name}</div></a>'''
    secs.append(section('The five <span class="text-gradient-gold">verticals</span>',
        f'<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));">{cards}</div>',
        surface=True, sub="Five rooms, one code. Take your pick of the floor."))

    secs.append(girl_break("girl-homepage-2.webp",
        'Get your <span class="text-gradient-gold">200% up to $3,000</span>',
        f"Whisper {CODE} to the dealer at registration. The 200% on your first deposit, plus 400 free spins, is already yours."))

    # intel cards
    intel = '''<div class="intel-grid">
        <div class="intel-card"><div class="ic-label">Founders</div><div class="ic-value">Craven &amp; Tehrani</div><div class="ic-detail">Australian. Co-founded Stake in 2017. Launched Kick in 2022.</div></div>
        <div class="intel-card"><div class="ic-label">Operating entity</div><div class="ic-value">Medium Rare NV</div><div class="ic-detail">The Curaçao company behind Stake.com. Stake.us is separate.</div></div>
        <div class="intel-card"><div class="ic-label">Licence</div><div class="ic-value">Curaçao 1668/JAZ</div><div class="ic-detail">Issued under the Curaçao framework, covering most of the world.</div></div>
        <div class="intel-card"><div class="ic-label">Reserves</div><div class="ic-value">~$320M</div><div class="ic-detail">Publicly traceable on Arkham Intel. Mostly ETH and stablecoins.</div></div>
      </div>'''
    secs.append(section('What the club <span class="text-gradient-gold">knows</span>', intel))

    transcript = ("Welcome to the club. The dealer here will be Stake. The code is MAXBET. The bonus is 200% up to $3,000 "
                  "plus 400 free spins. The licence is Curaçao 1668/JAZ. The reserves are roughly $320 million, traceable "
                  "on-chain. The founders, Ed Craven and Bijan Tehrani, have been at Stake since 2017 and run Kick on the "
                  "side. Hand them MAXBET at the door and the bonus is yours. Tell the dealer WinnersClub sent you.")
    secs.append('  <section class="section"><div class="section-inner">' + voice_player(transcript) + '</div></section>\n')

    secs.append(faq_section(faqs))
    return page(path, h, secs)


# ============================================================ PROMO CODE
def build_promo():
    path = "promo-code/"
    title = "MAXBET - Stake Promo Code | 200% up to $3,000 + 400 Spins"
    desc = "MAXBET is the biggest Stake promo code on the open market: 200% match up to $3,000 plus 400 free spins. Use it at Stake.com. Curaçao 1668/JAZ, Medium Rare NV."
    offer = {"@context":"https://schema.org","@type":"Offer","name":"Stake promo code MAXBET",
             "description":"200% deposit match up to $3,000 plus up to 400 free spins.",
             "url":"https://winnersclub.com/promo-code/","priceCurrency":"USD","price":"0",
             "eligibleQuantity":{"@type":"QuantitativeValue","value":1},
             "seller":{"@type":"Organization","name":"Stake.com"}}
    faqs = [
      ("What is the Stake promo code?", "It's MAXBET. Enter it in the promo field at registration to unlock 200% up to $3,000 plus 400 free spins."),
      ("How much is the MAXBET bonus worth?", "Up to $3,000 in matched funds at a 200% rate, plus up to 400 free spins. The biggest code the club hands out."),
      ("Is there a minimum deposit?", "Yes, $20 triggers the 200% match. Smaller deposits work but won't max the bonus."),
      ("What's the wagering requirement?", "40x on the bonus amount, which is typical for Stake's welcome offer. Clear it inside 7 days."),
      ("Does MAXBET expire?", "The code itself stays live. The bonus, once claimed, expires 7 days after it's credited if unwagered."),
      ("Can I use MAXBET on sports and casino?", "Yes. The match applies across the sportsbook, casino and poker. The 400 free spins are casino-side."),
      ("Do I have to be a new player?", "Yes, MAXBET is a welcome code for first-time Stake accounts only."),
      ("Where do I enter MAXBET?", "On the registration form there's a promo code field. Type MAXBET in uppercase before you finish signing up."),
    ]
    jl = [jsonld_webpage(title, desc, path), jsonld_breadcrumb([HOME,("Promo Code","https://winnersclub.com/promo-code/")]),
          offer, jsonld_faq(faqs)]
    h = head(title, desc, path, og_title=title, jsonld=jl)
    secs = []
    secs.append(hero("girl-promo-3.webp",
        "If you found this page, you found the code.",
        "the code is MAXBET.",
        f"200% up to $3,000 plus 400 free spins. The biggest Stake code on the open market, licensed {LIC}.",
        "Use MAXBET at Stake.com", AFF,
        "How to redeem", "#redeem"))
    # code card
    secs.append(f'''  <section class="section"><div class="section-inner">
      <div class="code-card">
        <div class="cc-shimmer"></div>
        <div class="ic-label" style="color:var(--text-dim);text-transform:uppercase;letter-spacing:2px;font-size:12px;">The club's code</div>
        <div class="code-display">MAXBET</div>
        <div class="code-meta">200% match &middot; $20 min deposit &middot; 40x wagering &middot; bonus expires after 7 days</div>
        <div class="code-actions">
          <button class="copy-btn" data-copy="MAXBET">Copy code</button>
          <a href="{AFF}" target="_blank" rel="noopener" class="btn btn-signup btn-gold-grad">Hand the dealer the code &rarr;</a>
        </div>
      </div>
    </div></section>
''')
    # comparison
    comp = '''<table class="comparison-table">
        <thead><tr><th>Code</th><th>Match %</th><th>Max bonus</th><th>Free spins</th><th>Exclusive</th></tr></thead>
        <tbody>
          <tr class="win"><td>MAXBET</td><td>200%</td><td>$3,000</td><td>400</td><td>Yes</td></tr>
          <tr><td>STAKE</td><td>100%</td><td>$1,000</td><td>100</td><td>No</td></tr>
          <tr><td>WELCOME</td><td>100%</td><td>$1,000</td><td>0</td><td>No</td></tr>
        </tbody>
      </table>'''
    secs.append(section('Why MAXBET <span class="text-gradient-gold">beats other codes</span>', comp, surface=True,
        sub="The public codes stop at a grand. MAXBET wins every row."))
    # redeem
    redeem = '''<div class="step-cards" id="redeem">
        <div class="step-card"><h3>1. Open the door</h3><p>Head to <a href="''' + AFF + '''" target="_blank" rel="noopener">getstake.it</a> and hit Register.</p></div>
        <div class="step-card"><h3>2. Register</h3><p>Enter your email and date of birth. Takes under a minute.</p></div>
        <div class="step-card"><h3>3. Enter MAXBET</h3><p>Type ''' + CODE + ''' in the promo code field before you finish.</p></div>
        <div class="step-card"><h3>4. Deposit $20+</h3><p>Your first deposit of $20 or more triggers the 200% match.</p></div>
      </div>'''
    secs.append(section('How to <span class="text-gradient-gold">redeem</span>', redeem))
    secs.append(girl_break("girl-promo-2.webp",
        'The biggest code <span class="text-gradient-gold">on the floor</span>',
        f"Whisper {CODE} to the dealer. The 200% up to $3,000 is already yours."))
    # terms
    terms = '''<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Wagering</h3><p>40x the bonus amount before withdrawal. Standard Stake welcome terms.</p></div>
        <div class="club-card"><h3>Eligible games</h3><p>Slots count fully. Table games and live dealer contribute less toward wagering.</p></div>
        <div class="club-card"><h3>Max bet rule</h3><p>While clearing the bonus, keep stakes modest. Oversized bets can void the offer.</p></div>
        <div class="club-card"><h3>Expiry</h3><p>The bonus expires 7 days after it's credited if you haven't wagered it.</p></div>
        <div class="club-card"><h3>Restricted countries</h3><p>The US, UK, and parts of Australia are off-limits. See <a href="/mirror/">the mirrors page</a>.</p></div>
        <div class="club-card"><h3>Min deposit</h3><p>$20 triggers the full 200% match. Smaller deposits scale down.</p></div>
      </div>'''
    secs.append(section('Terms in <span class="text-gradient-gold">plain English</span>', terms, surface=True))
    transcript = ("The code is MAXBET. Type it in the promo field when you register at Stake. It unlocks 200% on your "
                  "first deposit, up to three thousand dollars, plus four hundred free spins. Minimum deposit is twenty "
                  "dollars, wagering is forty times, and the bonus runs for seven days. That's the whole deal. "
                  "Tell the dealer WinnersClub sent you.")
    secs.append('  <section class="section"><div class="section-inner">' + voice_player(transcript) + '</div></section>\n')
    secs.append(faq_section(faqs))
    return page(path, h, secs)
