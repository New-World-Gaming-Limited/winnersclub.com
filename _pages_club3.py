# -*- coding: utf-8 -*-
import re
from _build_club import (AFF, head, hero, voice_player, girl_break, faq_section,
                         page, section, jsonld_webpage, jsonld_breadcrumb, jsonld_faq)
CODE = '<span class="code-highlight">MAXBET</span>'
LIC = "Curaçao 1668/JAZ"
HOME = ("Home", "https://winnersclub.com/")

def card_grid(cards, minw=260):
    inner = "".join(f'<div class="club-card"><h3>{t}</h3><p>{p}</p></div>' for t,p in cards)
    return f'<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax({minw}px,1fr));">{inner}</div>'

def tiles(items, minw=160):
    inner = "".join(f'<div class="club-card" style="text-align:center;padding:18px;"><h3 style="font-size:15px;margin:0;">{i}</h3></div>' for i in items)
    return f'<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax({minw}px,1fr));gap:12px;">{inner}</div>'

def voice(t):
    return '  <section class="section"><div class="section-inner">' + voice_player(t) + '</div></section>\n'

# ============================================================ CASINO
def build_casino():
    path="casino/"
    title="Stake Casino - 4,000+ Slots, Live Dealer | Code MAXBET | WinnersClub"
    desc="The Stake casino floor: 4,000+ slots, 50+ live-dealer tables, 100+ providers. MAXBET unlocks 200% up to $3,000 plus 400 free spins. Curaçao 1668/JAZ."
    faqs=[("How many games does Stake have?","Over 4,000 slots, 50+ live-dealer tables and 100+ providers including Pragmatic Play, Evolution, Hacksaw and Nolimit City."),
      ("What's the casino bonus with MAXBET?","200% up to $3,000 plus 400 free spins. The free spins are casino-side, landing on selected slots."),
      ("Are Stake's RTPs public?","Yes. Stake Originals publish their RTPs, typically 99% on Dice, 99% on Plinko and 98.74% on Crash."),
      ("Is there a live dealer section?","Yes, powered by Evolution and Pragmatic Live, streaming 24/7 with a wide range of bet limits."),
      ("Can I play table games?","Blackjack, roulette, baccarat and game shows all sit on the floor, alongside the slot library."),
      ("Do free spins have wagering?","Yes, spins winnings carry the standard 40x wagering tied to the welcome bonus.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Casino","https://winnersclub.com/casino/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-casino-3.webp","If you found this page, you found the floor.","the casino floor.",
        f"Thousands of slots, table games and live-dealer rooms. {CODE} unlocks 200% up to $3,000 plus 400 spins, licensed {LIC}.",
        "Take a seat at Stake.com",AFF,"See the promo code","/promo-code/")]
    secs.append(section('The <span class="text-gradient-gold">library</span>', card_grid([
        ("4,000+ slots","From classic three-reel to megaways and cluster pays, refreshed weekly."),
        ("50+ live tables","Real dealers, real cards, streamed around the clock."),
        ("100+ providers","Pragmatic Play, Evolution, Hacksaw, Nolimit City, Push Gaming, NetEnt, Play'n GO and more.")]),
        sub="The numbers behind the floor."))
    secs.append(section('Top <span class="text-gradient-gold">categories</span>',
        tiles(["Slots","Live Dealer","Blackjack","Roulette","Baccarat","Game Shows"]), surface=True))
    secs.append(section('The house edge <span class="text-gradient-gold">talk</span>',
        '<div class="club-body"><p>The club doesn\'t pretend the house edge isn\'t real. Stake Originals publish their RTPs in the open: Dice runs at 99%, Plinko at 99%, and Crash at 98.74%. That\'s thinner than almost anything on a Vegas floor. Third-party slots vary by provider, but the Originals are the most transparent bets in the room. Play them with eyes open.</p></div>'))
    secs.append(girl_break("girl-casino-2.webp",'400 free spins <span class="text-gradient-gold">waiting</span>',
        f"Whisper {CODE} at the door and the casino welcome is yours: 200% up to $3,000 plus 400 spins."))
    secs.append(section('Live dealer <span class="text-gradient-gold">specifics</span>',
        '<div class="club-body"><p>The live floor runs on <strong>Evolution</strong> and <strong>Pragmatic Live</strong> integrations, streaming 24/7. You\'ll find blackjack from small-stakes tables up to high-roller rooms, immersive roulette, baccarat, and the full run of game shows like Crazy Time and Lightning Roulette. Bet limits scale from a dollar or two up to five-figure hands depending on the table.</p></div>', surface=True))
    secs.append(voice("Welcome to the casino floor. Over four thousand slots, fifty live-dealer tables, more than a hundred providers. "
        "The Stake Originals publish their RTPs, Dice at ninety-nine percent, Plinko at ninety-nine, Crash at ninety-eight point "
        "seven four. Hand the dealer MAXBET and the welcome is yours, two hundred percent up to three thousand plus four hundred spins. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    return page(path,h,secs)

# ============================================================ SPORTS
def build_sports():
    path="sports/"
    title="Stake Sportsbook - 25+ Sports, Live In-Play | Code MAXBET | WinnersClub"
    desc="The Stake sportsbook: 25+ sports, in-play live odds, build-a-bet, 4,000+ live events monthly. MAXBET unlocks 200% up to $3,000. Curaçao 1668/JAZ."
    faqs=[("How many sports can I bet on?","More than 25, from soccer and the big US leagues to cricket, MMA, F1, esports and politics."),
      ("How many markets per game?","Big fixtures carry 250+ markets, covering match result, BTTS, Asian handicaps, player props, corners, cards and bet builders."),
      ("Is there live in-play betting?","Yes. Over 4,000 live events a month with sub-second odds updates and cash-out on most singles."),
      ("Can I watch matches?","Yes. Over 100,000 matches a year stream in-account, mostly tier 2/3 leagues plus tennis and esports."),
      ("What's the sports bonus with MAXBET?","The same welcome offer: 200% up to $3,000. It applies across the sportsbook just like the casino."),
      ("Is cash-out available?","On most singles, yes. You can lock in a return before the final whistle.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Sports","https://winnersclub.com/sports/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-sports-3.webp","If you found this page, you found the book.","the sportsbook.",
        f"25+ sports, in-play live odds, build-a-bet. {CODE} unlocks the same 200% up to $3,000, licensed {LIC}.",
        "Place your first bet at Stake.com",AFF,"See live odds","/live-odds/")]
    sports=["Soccer","NFL","NBA","MLB","NHL","Tennis","Cricket","Boxing","MMA","F1","Golf","CS2","LoL","Dota 2","Valorant","Rugby","Aussie Rules","Darts","Snooker","Cycling","Volleyball","Handball","Table Tennis","Badminton","Politics"]
    secs.append(section('25+ <span class="text-gradient-gold">sports</span>', tiles(sports,140),
        sub="Soccer to esports to politics. If it moves, there's a market."))
    secs.append(section('Markets <span class="text-gradient-gold">per game</span>',
        '<div class="club-body"><p>Take a marquee fixture - <strong>Manchester Utd vs Arsenal</strong> - and you\'ll find <strong>250+ markets</strong> on a single match. Match result, both teams to score, Asian handicap, player shots, corners, cards, and full prop builders where you stack your own selections into one price. The deeper the fixture, the deeper the book.</p></div>', surface=True))
    secs.append(section('Live <span class="text-gradient-gold">in-play</span>', card_grid([
        ("4,000+ live events / month","In-play markets across every major sport, all month long."),
        ("Sub-second odds","Prices update in real time as the play unfolds."),
        ("Cash-out","Lock in a return on most singles before the final whistle.")])))
    secs.append(girl_break("girl-sports-2.webp",'Same code, <span class="text-gradient-gold">same 200%</span>',
        f"Whisper {CODE} and the sportsbook welcome is yours: 200% up to $3,000."))
    secs.append(section('Live <span class="text-gradient-gold">streaming</span>',
        '<div class="club-body"><p>Over <strong>100,000 matches a year</strong> stream right in your account, mostly tier 2 and tier 3 leagues plus tennis and esports. It\'s built for the in-play bettor who wants the picture in front of them. See the <a href="/live-odds/" style="color:var(--gold);">live odds board</a> for what\'s on now.</p></div>', surface=True))
    secs.append(voice("Welcome to the sportsbook. More than twenty-five sports, deep markets, two hundred and fifty of them on the "
        "big fixtures. Over four thousand live events a month with sub-second odds and cash-out on most singles. A hundred thousand "
        "matches a year stream in your account. Hand the dealer MAXBET for two hundred percent up to three thousand. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    return page(path,h,secs)

# ============================================================ POKER
def build_poker():
    path="poker/"
    title="Stake Poker Room - Cash, Tournaments, Rakeback | MAXBET | WinnersClub"
    desc="The Stake poker room: Hold'em, Omaha, Short Deck, a $50K Sunday flagship and VIP rakeback up to 25%. MAXBET applies to poker too. Curaçao 1668/JAZ."
    faqs=[("What poker games can I play?","No-Limit and Pot-Limit Hold'em, Pot-Limit Omaha (4 and 5 card) and Short Deck."),
      ("What stakes are available?","From micro at $0.01/$0.02 all the way up to high stakes at $25/$50."),
      ("Is there a big weekly tournament?","Yes, the Sunday flagship carries a $50K guarantee, with daily $10K rebuys and micro hyper-turbos every five minutes."),
      ("How does rakeback work?","Stake's VIP tiers return rake from 5% at Bronze up to 25% at Diamond."),
      ("Does MAXBET apply to poker?","Yes. The 200% up to $3,000 match applies to poker, and rake counts toward clearing it."),
      ("Are there sit-and-gos?","Yes, single-table and multi-table sit-and-gos run around the clock alongside the scheduled events.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Poker","https://winnersclub.com/poker/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-poker-3.webp","If you found this page, you found the back room.","the poker room.",
        f"Cash tables, sit-and-gos, Sunday tournaments. {CODE} applies to poker rake too, licensed {LIC}.",
        "Pull up a chair at Stake.com",AFF,"See the promo code","/promo-code/")]
    secs.append(section('Game <span class="text-gradient-gold">types</span>', card_grid([
        ("Texas Hold'em","No-Limit and Pot-Limit, the core of every session."),
        ("Omaha","Pot-Limit Omaha in both 4-card and 5-card."),
        ("Short Deck","Faster, looser, the 36-card variant for action players.")]),
        sub="Three families, every texture of game."))
    secs.append(section('Stake <span class="text-gradient-gold">structure</span>',
        '<div class="club-body"><p>The room runs the full ladder: <strong>micro</strong> at $0.01/$0.02 for grinders finding their feet, climbing through low and mid stakes, up to <strong>high</strong> at $25/$50 where the serious money sits. Whatever your bankroll, there\'s a table that fits.</p></div>', surface=True))
    secs.append(section('Weekly <span class="text-gradient-gold">schedule</span>', card_grid([
        ("Sunday flagship","$50K guaranteed, the marquee event of the week."),
        ("Daily $10K rebuys","A guaranteed pool every day with rebuys to keep you in."),
        ("Micro hyper-turbos","Fast sit-and-gos firing every five minutes, day and night.")])))
    secs.append(girl_break("girl-poker-2.webp",'Rake counts <span class="text-gradient-gold">too</span>',
        f"Whisper {CODE} and the 200% match clears against your poker rake as well as the felt."))
    secs.append(section('<span class="text-gradient-gold">Rakeback</span>',
        '<div class="club-body"><p>Stake\'s VIP programme pays rake back on a sliding scale: <strong>Bronze 5%</strong>, rising through Silver, Gold and Platinum, up to <strong>Diamond at 25%</strong>. The more you play, the more of your rake comes home. For a regular, that quietly turns a break-even week into a winning one.</p></div>', surface=True))
    secs.append(voice("Welcome to the poker room. Hold'em, Omaha, Short Deck. Stakes from a penny up to twenty-five fifty. "
        "The Sunday flagship guarantees fifty thousand, daily rebuys guarantee ten, and the hyper-turbos fire every five minutes. "
        "VIP rakeback runs from five percent up to twenty-five at Diamond, and MAXBET clears against your rake. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    return page(path,h,secs)

# ============================================================ AVIATOR
def build_aviator():
    path="aviator/"
    title="Stake Aviator - Spribe Crash Game, 97% RTP | MAXBET | WinnersClub"
    desc="The Stake Aviator room: Spribe's crash game, min $0.10, max $100/round, auto-cashout and two parallel bets. Provably fair, 97% RTP. Curaçao 1668/JAZ."
    faqs=[("How does Aviator work?","Each round lasts about 30 seconds. A multiplier climbs from 1.00x and the plane flies off at a random point. Cash out before it does."),
      ("What are the bet limits?","Minimum $0.10, maximum $100 per round. You can run two bets at once."),
      ("Is Aviator provably fair?","Yes. Every round's seed is public, so you can verify the result wasn't tampered with."),
      ("What's the RTP?","97%, so the house edge is 3%. No betting system changes that math."),
      ("What's the two-bet feature?","You place two stakes in the same round, each with its own auto-cashout point, to hedge or chase separately."),
      ("Is there a winning strategy?","Honestly, no system beats a 97% RTP over time. The disciplined players bet small and cash out consistently around 1.10x to 1.30x.")]
    jl=[jsonld_webpage(title,desc,path),jsonld_breadcrumb([HOME,("Aviator","https://winnersclub.com/aviator/")]),jsonld_faq(faqs)]
    h=head(title,desc,path,jsonld=jl)
    secs=[hero("girl-aviator-3.webp","If you found this page, you found the runway.","the Aviator room.",
        f"Spribe's crash game. Min $0.10, max $100 a round, auto-cashout, two parallel bets. Licensed {LIC}. Whisper {CODE} before you board.",
        "Board at Stake.com",AFF,"See the promo code","/promo-code/")]
    secs.append(section('How Aviator <span class="text-gradient-gold">works</span>',
        '<div class="club-body"><p>Rounds run about 30 seconds. The multiplier starts at <strong>1.00x</strong> and climbs as the plane takes off. At a random point, it flies away. Your job is simple and brutal: cash out before it goes. Cash out at 2x and you double your stake; wait too long and you get nothing. Every round is <strong>provably fair</strong>, the seed is public, so nothing is hidden.</p></div>'))
    secs.append(section('The two-bet <span class="text-gradient-gold">feature</span>',
        '<div class="club-body"><p>You can place <strong>two stakes per round</strong>, each with its own auto-cashout point. The common play is one safe bet that cashes early to bank a small profit, and one runner left to chase a bigger multiplier. It lets you hedge without leaving the round.</p></div>', surface=True))
    secs.append(section('Strategy <span class="text-gradient-gold">talk</span>',
        '<div class="club-body"><p>The club won\'t sell you a system. Aviator runs at a <strong>97% RTP</strong>, which means a <strong>3% house edge</strong>, and no martingale, no pattern, no hot streak beats that over time. The players who last bet small and cash out consistently around <strong>1.10x to 1.30x</strong>, treating it as a grind, not a lottery. Anyone promising more is selling something.</p></div>'))
    secs.append(girl_break("girl-aviator-2.webp",'97% RTP, <span class="text-gradient-gold">no fairy tales</span>',
        f"Whisper {CODE} and the welcome bonus is yours. The math stays the math."))
    secs.append(section('Live Aviator <span class="text-gradient-gold">stats</span>',
        '<div class="club-body"><p>Every round\'s multiplier is logged in-game, so you can scroll the recent history right at the table. It won\'t predict the next flight - it can\'t, it\'s random - but it gives you the feel of the room. Pull up the live multiplier history when you board at Stake.</p></div>', surface=True))
    secs.append(voice("Welcome to the Aviator room. Spribe's crash game. The multiplier climbs from one, the plane flies off at a "
        "random point, and you cash out before it does. Minimum ten cents, maximum a hundred a round, two bets at once. It's "
        "provably fair, ninety-seven percent RTP, three percent edge. No system beats that. Bet small, cash out often. "
        "Tell the dealer WinnersClub sent you."))
    secs.append(faq_section(faqs))
    return page(path,h,secs)
