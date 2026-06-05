# -*- coding: utf-8 -*-
import re
from _build_club import (AFF, head, hero, voice_player, girl_break, faq_section,
                         page, section, jsonld_webpage, jsonld_breadcrumb, jsonld_faq)
CODE = '<span class="code-highlight">MAXBET</span>'
LIC = "Curaçao 1668/JAZ"
HOME = ("Home", "https://winnersclub.com/")
def strip(a): return re.sub('<[^>]+>','',a)

# ============================================================ ABOUT STAKE
def build_about():
    path = "about-stake/"
    title = "Who Runs Stake - Founders, Entities, Licence | WinnersClub"
    desc = "The full intel on Stake: founders Ed Craven and Bijan Tehrani, operating entity Medium Rare NV, the Curaçao 1668/JAZ licence, and the Kick connection."
    faqs = [
      ("Who owns Stake?", "Ed Craven and Bijan Tehrani, two Australians who co-founded Stake in 2017. They also launched Kick in 2022."),
      ("What company runs Stake.com?", "Medium Rare NV, registered in Curaçao under licence 1668/JAZ. Stake.us is a separate sweepstakes operation under Sweepsteaks Limited."),
      ("Is Stake.us the same as Stake.com?", "No. Stake.us is a free-to-play sweepstakes platform for select US states only. Stake.com is the real-money international site."),
      ("Is Drake still involved with Stake?", "No. Drake was the public face from 2022 to 2025, then fell out with the team in 2025. He's no longer affiliated."),
      ("What is the Kick connection?", "Kick is the streaming platform launched by the same founders in 2022. Stake streams natively on Kick."),
      ("What does the Curaçao licence cover?", "Licence 1668/JAZ is issued under the Curaçao framework and permits online casino and sportsbook operation across most of the world, regulated by the CGCB."),
    ]
    jl = [jsonld_webpage(title, desc, path), jsonld_breadcrumb([HOME,("About Stake","https://winnersclub.com/about-stake/")]), jsonld_faq(faqs)]
    h = head(title, desc, path, jsonld=jl)
    secs = []
    secs.append(hero("girl-news-3.webp",
        "If you found this page, you wanted the full file.",
        "who runs Stake.",
        f"The full intel. Founders, entities, the {LIC} licence, the money. Whisper {CODE} when you've read enough.",
        "Open an account at Stake.com", AFF, "See the reserves", "/reserves/"))
    founders = '''<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));">
        <div class="club-card" style="text-align:center;"><div style="width:80px;height:80px;border-radius:50%;margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;font-family:var(--font-mono);background:linear-gradient(135deg,var(--gold),#ff9d00);color:#1a1308;">EC</div><h3>Ed Craven</h3><p>Australian co-founder of Stake, 2017. Also co-launched Kick in 2022. The product and growth side of the house.</p></div>
        <div class="club-card" style="text-align:center;"><div style="width:80px;height:80px;border-radius:50%;margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;font-family:var(--font-mono);background:linear-gradient(135deg,var(--gold),#ff9d00);color:#1a1308;">BT</div><h3>Bijan Tehrani</h3><p>Australian co-founder of Stake, 2017. Co-launched Kick alongside Craven. The operations and corporate side.</p></div>
      </div>'''
    secs.append(section('The <span class="text-gradient-gold">founders</span>', founders,
        sub="Two Australians. Co-founded Stake in 2017. Launched Kick in 2022."))
    entities = '''<div class="club-body">
        <p><strong>Stake.com</strong> is operated by <strong>Medium Rare NV</strong>, a Curaçao company holding licence ''' + LIC + '''. That's the real-money international house: casino, sportsbook, poker, the lot.</p>
        <p><strong>Stake.us</strong> is a different animal. It's a sweepstakes-only platform run by <strong>Sweepsteaks Limited</strong>, free-to-play, and available in select US states only. No crypto, no real-money wagering, separate company, separate rules.</p>
      </div>'''
    secs.append(section('The <span class="text-gradient-gold">entities</span>', entities, surface=True))
    lic = '''<div class="club-body">
        <p>The licence is <strong>Curaçao 1668/JAZ</strong>. It permits online casino and sportsbook operation and is recognised across most of the world, which is why Stake reaches so many markets from a single base.</p>
        <p>Curaçao licensing now sits under the <strong>CGCB</strong> (Curaçao Gaming Control Board), which took over from the old master-licence model. The licence does not cover jurisdictions that ring-fence their own gambling, so Stake self-restricts the US, the UK, and parts of Australia.</p>
      </div>'''
    secs.append(section('The <span class="text-gradient-gold">licence</span>', lic))
    secs.append(girl_break("girl-news-2.webp",
        'The money is <span class="text-gradient-gold">on-chain</span>',
        'Stake holds roughly $320M in publicly traceable reserves. <a href="/reserves/" style="color:var(--gold);">Full breakdown &rarr;</a>'))
    history = '''<div class="club-body">
        <p><strong>2017</strong> - Craven and Tehrani found Stake.</p>
        <p><strong>2020</strong> - First major sponsorship deals land.</p>
        <p><strong>2022</strong> - Drake partnership begins, Kick launches.</p>
        <p><strong>2024</strong> - Everton sleeve sponsorship in the Premier League.</p>
        <p><strong>2025</strong> - The Drake split. He's out, the house stays independent.</p>
        <p><strong>2026</strong> - Still independent, still owner-run.</p>
      </div>'''
    secs.append(section('The <span class="text-gradient-gold">history</span>', history, surface=True))
    kick = '''<div class="club-body"><p>Same founders, same world. <strong>Kick</strong> is the streaming side, launched in 2022 by Craven and Tehrani. Stake streams natively on Kick, which keeps the audience and the casino under one roof. If you've watched a Stake stream, you've already been in the building.</p></div>'''
    secs.append(section('The <span class="text-gradient-gold">Kick connection</span>', kick))
    transcript = ("Stake was founded in 2017 by Ed Craven and Bijan Tehrani, two Australians who also launched Kick in 2022. "
                  "Stake.com runs under Medium Rare NV in Curaçao, licence 1668/JAZ. Stake.us is a separate sweepstakes "
                  "platform under Sweepsteaks Limited. Drake was the public face from 2022 to 2025, then he split. The "
                  "money sits on-chain, around 320 million, traceable on Arkham. Tell the dealer WinnersClub sent you.")
    secs.append('  <section class="section"><div class="section-inner">' + voice_player(transcript) + '</div></section>\n')
    secs.append(faq_section(faqs))
    return page(path, h, secs)


# ============================================================ RESERVES
def build_reserves():
    path = "reserves/"
    title = "Stake On-Chain Reserves - $320M Live Arkham Briefing | WinnersClub"
    desc = "Stake holds $320M+ in publicly traceable on-chain reserves. Live breakdown from Arkham Intel: ETH, USDT, USDC, SOL and more. Curaçao 1668/JAZ, Medium Rare NV."
    dataset = {"@context":"https://schema.org","@type":"Dataset","name":"Stake.com on-chain reserves",
               "description":"Publicly traceable cryptocurrency reserves held by Stake.com, sourced from Arkham Intel.",
               "url":"https://winnersclub.com/reserves/","creator":{"@type":"Organization","name":"Arkham Intel"},
               "temporalCoverage":"2026-06-05","keywords":["Stake","reserves","on-chain","Arkham","proof of reserves"]}
    faqs = [
      ("What is Arkham Intel?", "Arkham is an on-chain analytics platform that labels blockchain wallets by owner. It lets anyone trace a company's public crypto holdings."),
      ("What do these reserves mean?", "They're the publicly identifiable crypto wallets attributed to Stake. Roughly $320M, mostly ETH and stablecoins, that you can inspect yourself."),
      ("Does this prove Stake is solvent?", "It shows large, liquid, verifiable holdings, including around $117M in stablecoins. It's far stronger than a private audit claim, because the addresses are public."),
      ("Can the figure change?", "Yes. Crypto prices move and Stake moves funds. The number ticks with the market, which is why we label it live as of a date."),
      ("How do I verify it myself?", "Pull up the <a href='https://intel.arkm.com/explorer/entity/stake-com' target='_blank' rel='noopener'>Stake entity page on Arkham</a>. Don't take our word for it."),
    ]
    jl = [jsonld_webpage(title, desc, path), jsonld_breadcrumb([HOME,("Reserves","https://winnersclub.com/reserves/")]), dataset, jsonld_faq(faqs)]
    h = head(title, desc, path, jsonld=jl)
    secs = []
    secs.append(hero("girl-payments-3.webp",
        "If you found this page, you wanted proof.",
        "Stake on-chain.",
        f"$320M+ in traceable reserves, updated from Arkham Intel. The house licensed {LIC} doesn't hide the money. Whisper {CODE} when you're satisfied.",
        "Open an account at Stake.com", AFF, "Verify on Arkham", "https://intel.arkm.com/explorer/entity/stake-com"))
    # big number
    secs.append('''  <section class="section"><div class="section-inner" style="text-align:center;">
      <div class="big-number" data-flicker>$320,467,591</div>
      <p style="margin-top:18px;color:var(--text-dim);font-family:var(--font-mono);">Live as of June 5, 2026 &middot; <span style="color:var(--velvet);font-weight:700;">-2.04% 24h</span></p>
      <p style="margin-top:6px;font-size:13px;color:var(--text-dim);">Source: <a href="https://intel.arkm.com/explorer/entity/stake-com" target="_blank" rel="noopener" style="color:var(--gold);">Arkham Intel</a></p>
    </div></section>
''')
    # holdings table
    rows = [("ETH","86.72K","$145.15M"),("USDT","59.256M","$59.26M"),("USDC","50.129M","$50.13M"),
            ("SOL","438.677K","$29.05M"),("BSC-USD","7.877M","$7.88M"),("DAI","7.794M","$7.79M"),
            ("TRX","20.814M","$6.77M"),("WETH","2.369K","$3.96M"),("BNB","4.131K","$2.45M"),("LINK","129.156K","$981K")]
    tr = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td class='o'>{c}</td></tr>" for a,b,c in rows)
    secs.append(section('Top <span class="text-gradient-gold">holdings</span>',
        f'<table class="odds-table"><thead><tr><th>Asset</th><th>Amount</th><th>USD value</th></tr></thead><tbody>{tr}</tbody></table>',
        surface=True))
    # chain distribution
    bars = [("Ethereum (ETH + WETH)",60),("Stablecoin layer (USDT, USDC, DAI, BSC-USD)",35),("Solana",9),("TRON",2),("Others",1)]
    bhtml = ""
    for label,pct in bars:
        bhtml += f'''<div style="margin-bottom:18px;"><div style="display:flex;justify-content:space-between;font-size:14px;color:#cfcfcf;margin-bottom:6px;"><span>{label}</span><span style="color:var(--gold);font-family:var(--font-mono);">{pct}%</span></div><div style="height:10px;background:var(--elevated);border-radius:6px;overflow:hidden;"><div style="height:100%;width:{pct}%;background:linear-gradient(90deg,var(--gold),#ff9d00);"></div></div></div>'''
    secs.append(section('Chain <span class="text-gradient-gold">distribution</span>',
        f'<div style="max-width:720px;margin:0 auto;">{bhtml}<p style="font-size:12px;color:var(--text-dim);margin-top:10px;">Approximate, calculated from on-chain USD values. Layers overlap slightly across bridged assets.</p></div>'))
    # why matters
    why = '''<div class="club-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
        <div class="club-card"><h3>Solvency you verify</h3><p>You don't trust a press release. You open Arkham and look at the wallets yourself.</p></div>
        <div class="club-card"><h3>Liquid stablecoins</h3><p>Around $117M in USDT, USDC, DAI and BSC-USD covers player funds in instantly liquid form.</p></div>
        <div class="club-card"><h3>No theatre</h3><p>No proof-of-reserves stunt with a borrowed balance for a day. The addresses are public, all the time.</p></div>
      </div>'''
    secs.append(section('Why this <span class="text-gradient-gold">matters</span>', why, surface=True))
    secs.append(girl_break("girl-payments-2.webp",
        'Don\'t take our word <span class="text-gradient-gold">for it</span>',
        'Pull up <a href="https://intel.arkm.com/explorer/entity/stake-com" target="_blank" rel="noopener" style="color:var(--gold);">the live Arkham entity page</a> and check the money yourself.', "Open Stake.com"))
    verify = '''<div class="club-body"><p>Here's the whole point: you can check this without us. Open <a href="https://intel.arkm.com/explorer/entity/stake-com" target="_blank" rel="noopener" style="color:var(--gold);">the Stake entity page on Arkham Intel</a>, sort the holdings, and watch the same numbers we're quoting. The wallets are labelled, the balances are live, and nobody's asking you to trust a logo. Don't take our word for it. Pull it up yourself.</p></div>'''
    secs.append(section('How to verify <span class="text-gradient-gold">yourself</span>', verify))
    cp = [("All-time deposits","$99.09M","100% Stake.com"),("Total exchange volume","$1.33B","All counterparties"),
          ("Binance","$3.51M","<1%"),("Stake.us","$2.49M","<1%")]
    cphtml = "".join(f"<tr><td><strong>{a}</strong></td><td class='o'>{b}</td><td>{c}</td></tr>" for a,b,c in cp)
    secs.append(section('<span class="text-gradient-gold">Counterparties</span>',
        f'<table class="odds-table"><thead><tr><th>Flow</th><th>Value</th><th>Share</th></tr></thead><tbody>{cphtml}</tbody></table>', surface=True))
    transcript = ("Stake holds roughly 320 million dollars in reserves, and you can trace all of it on Arkham Intel. Most of "
                  "it is Ethereum, around 145 million, plus stablecoins, USDT, USDC and DAI, worth about 117 million combined. "
                  "There's Solana, TRON, and a handful of others. The point is simple: the wallets are public, so you don't "
                  "have to trust anyone. Open Arkham and look. Tell the dealer WinnersClub sent you.")
    secs.append('  <section class="section"><div class="section-inner">' + voice_player(transcript) + '</div></section>\n')
    secs.append(faq_section(faqs))
    return page(path, h, secs)
