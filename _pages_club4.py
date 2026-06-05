# -*- coding: utf-8 -*-
from _build_club import (AFF, head, hero, voice_player, girl_break, faq_section,
                         page, section, jsonld_webpage, jsonld_breadcrumb, jsonld_faq)
CODE = '<span class="code-highlight">MAXBET</span>'
LIC = "Curaçao 1668/JAZ"
HOME = ("Home", "https://winnersclub.com/")

def card_grid(cards, minw=260):
    inner = "".join(f'<div class="club-card"><h3>{t}</h3><p>{p}</p></div>' for t,p in cards)
    return f'<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax({minw}px,1fr));">{inner}</div>'

def voice(t):
    return '  <section class="section"><div class="section-inner">' + voice_player(t) + '</div></section>\n'

def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<table class="odds-table" style="max-width:900px;"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

# ============================================================ MIRROR
def build_mirror():
    path="mirror/"
    title="Stake Access & Mirrors - Regional Domains | MAXBET | WinnersClub"
    desc="Stake's regional mirror domains and how to get in when your ISP plays games. VPN guidance, DNS tips, the app option. Curaçao 1668/JAZ, code MAXBET."
    faqs=[("Why does Stake have mirror domains?","Different regions get different domains so the door stays open even when a single address is blocked at the ISP level."),
      ("Which domain should I use?","Use the one that matches your region. If the main Stake.com is unreachable, a regional mirror usually is."),
      ("Is using a VPN against the rules?","It can breach Stake's terms in self-restricted countries, and that risks your account and any winnings. Be honest with yourself about the jurisdiction you're in."),
      ("Is there an app?","Yes, a native Android APK and an iOS build via TestFlight. See the cross-link below."),
      ("What if every domain is blocked?","Try DNS-over-HTTPS or a mobile-data fallback before anything heavier. Often it's just a DNS-level block."),
      ("Which VPNs are reliable?","Mullvad and ProtonVPN are the privacy-first picks. Again, weigh the terms-of-service implications first.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Mirror","https://winnersclub.com/mirror/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-mirror-3.webp","If you found this page, the door's already ajar.","door's open everywhere.",
        f"Stake's regional mirrors, and how to get in when your country's ISP plays games. Licensed {LIC}. Whisper {CODE} once you're through.",
        "Find the open door at Stake.com",AFF,"Get the app","/mirror/#app")]
    secs.append(section('Regional <span class="text-gradient-gold">domains</span>',
        table(["Domain","Targets"],[
          ["Stake.com","The flagship international domain"],
          ["Stake.bet","Backup mirror for blocked regions"],
          ["Stake.games","Alternate gateway, same house"],
          ["Stake.pet","Regional failover domain"],
          ["Stake.us","US sweepstakes only, separate entity"]]),
        sub="Same house, different doors. Use the one your region can reach."))
    secs.append(section('If you\'re <span class="text-gradient-gold">blocked</span>', card_grid([
        ("Try DNS first","Switch to DNS-over-HTTPS (Cloudflare or Google). Most blocks are just at the DNS layer."),
        ("VPN, with care","Mullvad and ProtonVPN are the privacy-first options. Know that VPN use can breach Stake's terms in restricted countries."),
        ("Mobile data fallback","Your mobile carrier often resolves what home broadband won't. A quick honest test.")]), surface=True))
    secs.append(girl_break("girl-mirror-2.webp",'The code travels <span class="text-gradient-gold">with you</span>',
        f"Whatever door you come through, {CODE} still unlocks 200% up to $3,000."))
    secs.append(section('The app <span class="text-gradient-gold">option</span>',
        '<div class="club-body" id="app"><p>If the web keeps getting blocked, the native app is the cleaner route. There\'s an <strong>Android APK</strong> for direct install and an <strong>iOS build via TestFlight</strong>. The app talks to Stake directly, which sidesteps a lot of clumsy domain blocking. Treat it as the steady door when the browser keeps closing on you.</p></div>'))
    secs.append(voice("The door's open everywhere if you know where to knock. Stake runs several domains, the flagship Stake-dot-com "
        "plus regional mirrors, so a single block doesn't shut you out. If you're stuck, try DNS-over-HTTPS first, then a privacy "
        "VPN like Mullvad or Proton, but know that can breach the terms in restricted countries. There's a native app too. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    return page(path,h,secs)

# ============================================================ PAYMENTS
def build_payments():
    path="payments/"
    title="Stake Deposits & Withdrawals - Crypto & Fiat | MAXBET | WinnersClub"
    desc="How money moves at Stake: crypto-first deposits from under $1, fiat where licensed, KYC tiers, withdrawal speeds. Code MAXBET, Curaçao 1668/JAZ."
    faqs=[("What's the minimum deposit?","Crypto minimums sit under a dollar for most coins. The MAXBET match wants $20 to trigger fully."),
      ("How fast are crypto withdrawals?","Instant to about an hour once your account is verified. Crypto is the fastest route in and out."),
      ("Can I use a card?","Yes, where you're in a licensed region. Card and bank methods take longer, 2 to 5 days, and aren't available everywhere."),
      ("What's the minimum withdrawal?","Around ₹500 or equivalent. There's no maximum."),
      ("What are the KYC tiers?","L1 to create an account, L2 for your first withdrawal, L3 for high volume or proof of address, L4 for source of funds."),
      ("Which crypto does Stake take?","BTC, ETH, LTC, USDT, USDC, SOL, DOGE, XRP, BCH and BNB, among others.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Payments","https://winnersclub.com/payments/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-payments-3.webp","If you found this page, you came to talk money.","money in, money out.",
        f"Crypto-first house. Fiat options where licensed. Minimums under $1. Licensed {LIC}. Whisper {CODE} and the 200% is waiting.",
        "Fund your seat at Stake.com",AFF,"See the promo code","/promo-code/")]
    secs.append(section('Crypto <span class="text-gradient-gold">methods</span>',
        table(["Coin","Min deposit","Network","Speed"],[
          ["BTC","0.00002504","Blockchain","~10 min"],
          ["ETH","0.001","Blockchain","~1 min"],
          ["LTC","0.01857","Blockchain","~2 min"],
          ["USDT","~$1","TRC20 / ERC20 / BSC","~1 min"],
          ["USDC","~$1","ERC20 / SOL","~1 min"],
          ["SOL","~$1","Solana","~30 sec"],
          ["DOGE","~$1","Blockchain","~2 min"],
          ["XRP","~$1","Ledger","~30 sec"],
          ["BCH","~$1","Blockchain","~2 min"],
          ["BNB","~$1","BSC","~30 sec"]]),
        sub="Crypto is the front door. Minimums under a dollar, settlement in minutes."))
    secs.append(section('Fiat <span class="text-gradient-gold">methods</span>',
        table(["Method","Speed","Note"],[
          ["Visa / Mastercard","2-5 days","Region-restricted"],
          ["Bank transfer","Up to 3 days","Region-restricted"],
          ["Neteller","A few hours","Where supported"],
          ["Skrill","A few hours","Where supported"],
          ["UPI","Minutes","India only"]]), surface=True)) 
    secs.append(section('Minimum <span class="text-gradient-gold">withdrawal</span>',
        '<div class="club-body"><p>The floor on a withdrawal is around <strong>₹500 or its equivalent</strong>, and there\'s <strong>no maximum</strong>. Crypto wallets clear fastest; fiat rails follow their own banking clocks.</p></div>'))
    secs.append(girl_break("girl-payments-2.webp",'In fast, out <span class="text-gradient-gold">faster</span>',
        f"Whisper {CODE}, deposit $20 in crypto, and the 200% lands before the kettle boils."))
    secs.append(section('KYC <span class="text-gradient-gold">tiers</span>', card_grid([
        ("L1 - Account","Email and date of birth. Enough to open the door and play."),
        ("L2 - First withdrawal","Basic identity check before your first cash-out clears."),
        ("L3 - High volume","Proof of address once you're moving real money."),
        ("L4 - Source of funds","For the biggest accounts, documentation on where the money comes from.")])))
    secs.append(section('Speed <span class="text-gradient-gold">table</span>',
        table(["Method","Withdrawal speed"],[
          ["Crypto","Instant to 1 hour"],
          ["E-wallet","A few hours"],
          ["Bank transfer","Up to 3 days"],
          ["Card","2-5 days"]]), surface=True))
    secs.append(voice("Money in, money out. This is a crypto-first house, minimums under a dollar, settlement in minutes. Bitcoin, "
        "Ethereum, Litecoin, the major stablecoins, Solana and more. Fiat works where you're licensed, but it's slower, two to "
        "five days on cards. Withdrawals run from instant on crypto to a few days on a bank. KYC climbs in four tiers. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    return page(path,h,secs)

# ============================================================ LIVE ODDS
def build_liveodds():
    path="live-odds/"
    title="Live Stake Odds - Top Markets Refreshed Every 30s | WinnersClub"
    desc="Live Stake odds on top markets, refreshed every 30 seconds. Click any market to claim with MAXBET at Stake.com. Curaçao 1668/JAZ."
    faqs=[("How often do the odds update?","The board polls every 30 seconds when a live feed is connected. Right now it shows a sample card."),
      ("Are these real odds?","The sample fixtures are illustrative. The live feed slots in here once connected; the format and the bet links are real."),
      ("How do I bet on a market?","Click the bet button on any row. It opens Stake with the club's code attached."),
      ("What does 1, X, 2 mean?","Home win, draw, away win. The three-way match result, the most common football market."),
      ("Does MAXBET apply here?","Yes. Every bet link carries the club's affiliate route, so the 200% welcome is in play."),
      ("Why only football right now?","The sample shows the six biggest European leagues. The live feed expands the board to the full sportsbook.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Live Odds","https://winnersclub.com/live-odds/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-sports-3.webp","If you found this page, the board's already live.","live Stake odds.",
        f"Top markets, refreshed every 30 seconds. Click any market to claim with {CODE}. Licensed {LIC}.",
        "Open the sportsbook at Stake.com",AFF,"See all sports","/sports/")]
    secs.append('''  <section class="section"><div class="section-inner">
      <div class="section-header"><h2 class="section-title">The <span class="text-gradient-gold">board</span></h2><p class="section-subtitle">Live as it moves. Click a row to take the price at Stake.</p></div>
      <div id="odds-widget" data-endpoint="" data-poll="30000"></div>
    </div></section>
''')
    secs.append(section('What odds <span class="text-gradient-gold">you see</span>',
        '<div class="club-body"><p>The board shows three-way match-result prices: <strong>1</strong> for the home win, <strong>X</strong> for the draw, <strong>2</strong> for the away win, plus the league and kick-off. When a live feed is connected, the whole board refreshes every 30 seconds; until then you\'re looking at a representative card of the six biggest European leagues. Every row links straight into Stake with the club\'s code attached, so the price you click is the price you take.</p></div>', surface=True))
    secs.append(girl_break("girl-sports-2.webp",'Take the price <span class="text-gradient-gold">at the table</span>',
        f"Whisper {CODE}, click a market, and the 200% welcome rides along with your first bet."))
    secs.append(voice("These are live Stake odds, the top markets refreshed every thirty seconds when the feed's connected. One, "
        "X, two, home, draw, away, with the league and kick-off beside them. Click any row and it opens Stake with the club's "
        "code already attached, so the price you see is the price you get. Hand the dealer MAXBET for the two hundred percent. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    extra = '  <script src="/odds.js" defer></script>'
    return page(path,h,secs,extra_scripts=extra)
