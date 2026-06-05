"""
Generate Crypto payment method pages for 1win.codes
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_helpers.page_template import render_page

os.makedirs('en/payments', exist_ok=True)

def crypto_page(slug, coin, ticker, network, min_dep, min_dep_usd, confirmations, deposit_time, withdrawal_time, fee_note, extra_lede, extra_body, title, description, h1, alt_methods):
    faq_schema = f"""<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {{"@type":"Question","name":"What is the minimum {coin} deposit at 1win?","acceptedAnswer":{{"@type":"Answer","text":"Minimum {coin} deposit at 1win is {min_dep} {ticker} (approximately {min_dep_usd} USD at current rates). The minimum changes if {ticker} price moves significantly; always check the cashier for the current minimum."}}}},
    {{"@type":"Question","name":"How long does a {coin} deposit take to confirm?","acceptedAnswer":{{"@type":"Answer","text":"{deposit_time} {coin} deposits require {confirmations} network confirmations before crediting to your 1win wallet."}}}},
    {{"@type":"Question","name":"Does 1win charge a fee for {coin} deposits or withdrawals?","acceptedAnswer":{{"@type":"Answer","text":"1win does not charge a deposit fee. For withdrawals, 1win deducts a network fee from the withdrawal amount to cover the blockchain transaction cost. {fee_note}"}}}},
    {{"@type":"Question","name":"Can I use {coin} to avoid geographic restrictions on local banking?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {ticker} deposits and withdrawals are geographic-agnostic. Players in India, Pakistan, Africa, and other regions where local banking options are limited can use {ticker} without RBI, SBP, or local bank restrictions."}}}},
    {{"@type":"Question","name":"My {coin} deposit has not arrived. What should I do?","acceptedAnswer":{{"@type":"Answer","text":"First, confirm the transaction has {confirmations} confirmations on the {network} blockchain explorer using your transaction hash (TXID). If confirmed, contact 1win live-chat with the TXID. If not yet confirmed, wait for the network to process it."}}}}
  ]
}}
</script>"""

    main = f"""
<section class="lede">
  <p>{extra_lede} 1win accepts {coin} ({ticker}) on the {network} network for deposits and withdrawals, with no geographic restrictions, no chargebacks, and processing that depends only on blockchain confirmation times. The platform holds a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus on your first {ticker} deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: {coin} at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>{min_dep} {ticker} (approx. {min_dep_usd} USD)</td></tr>
    <tr><td>Network</td><td>{network}</td></tr>
    <tr><td>Network confirmations required</td><td>{confirmations}</td></tr>
    <tr><td>Deposit processing time</td><td>{deposit_time}</td></tr>
    <tr><td>Withdrawal processing time</td><td>{withdrawal_time}</td></tr>
    <tr><td>1win deposit fee</td><td>None</td></tr>
    <tr><td>1win withdrawal fee</td><td>Network fee deducted from amount</td></tr>
    <tr><td>Supported currencies</td><td>{ticker} (converted to USD equivalent in wallet)</td></tr>
    <tr><td>Geographic availability</td><td>Global (no country restrictions)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit {coin} at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select {coin} ({ticker}) from the cryptocurrency deposit options.</strong> Ensure you select the correct network: {network}. Sending {ticker} on the wrong network results in permanent loss of funds.</li>
    <li><strong>Copy the 1win {ticker} deposit address.</strong> A unique wallet address is generated for you. Do not share this address with others. For added safety, scan the QR code instead of manually typing the address.</li>
    <li><strong>Send {ticker} from your crypto wallet or exchange.</strong> Open your wallet (Binance, Coinbase, Trust Wallet, MetaMask, etc.), paste the 1win deposit address, enter the amount (minimum {min_dep} {ticker}), and confirm the transaction. Double-check the address and network before confirming.</li>
    <li><strong>Wait for blockchain confirmations.</strong> The {network} network requires {confirmations} confirmations. Track the transaction on a blockchain explorer using the TXID. Once confirmed, 1win credits your wallet automatically. {deposit_time}</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw {coin} from 1win</h2>
  <ol>
    <li><strong>Complete KYC if required.</strong> 1win may require identity verification before large crypto withdrawals.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose {coin} ({ticker}).</strong></li>
    <li><strong>Enter your {ticker} wallet address.</strong> This must be an address on the {network} network. Double-check the address character by character; crypto transfers are irreversible.</li>
    <li><strong>Enter the withdrawal amount.</strong> 1win deducts a network fee from the amount to cover on-chain transaction costs. The fee is shown before you confirm.</li>
    <li><strong>Submit and track the transaction.</strong> 1win broadcasts the transaction to the {network} network. You receive the TXID to track on a blockchain explorer. Withdrawal processing takes {withdrawal_time} after submission.</li>
  </ol>
</section>

{extra_body}

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>{coin} ({ticker}) deposits are available globally. There are no country-level restrictions on using {ticker} at 1win. This makes it particularly useful for players in India (where local bank transfers may be declined by some banks due to gaming MCC codes), Pakistan, African countries, or anywhere that local fiat payment options are restricted or unreliable.</p>
  <p>1win converts {ticker} deposits to USD equivalent for wallet display and bonus calculations. When you withdraw, 1win sends the requested USD-equivalent amount back in {ticker} at the current exchange rate at the time of withdrawal.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
{alt_methods}
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: {coin} at 1win</h2>
  <details><summary>What is the minimum {coin} deposit at 1win?</summary><p>Minimum {coin} deposit at 1win is {min_dep} {ticker} (approximately {min_dep_usd} USD at current rates). The minimum changes if {ticker} price moves significantly; always check the cashier for the current minimum.</p></details>
  <details><summary>How long does a {coin} deposit take to confirm?</summary><p>{deposit_time} {coin} deposits require {confirmations} network confirmations before crediting to your 1win wallet.</p></details>
  <details><summary>Does 1win charge a fee for {coin} deposits or withdrawals?</summary><p>1win does not charge a deposit fee. For withdrawals, 1win deducts a network fee from the withdrawal amount to cover the blockchain transaction cost. {fee_note}</p></details>
  <details><summary>Can I use {coin} to avoid geographic restrictions on local banking?</summary><p>Yes. {ticker} deposits and withdrawals are geographic-agnostic. Players in India, Pakistan, Africa, and other regions where local banking options are limited can use {ticker} without RBI, SBP, or local bank restrictions.</p></details>
  <details><summary>My {coin} deposit has not arrived. What should I do?</summary><p>First, confirm the transaction has {confirmations} confirmations on the {network} blockchain explorer using your transaction hash (TXID). If confirmed, contact 1win live-chat with the TXID. If not yet confirmed, wait for the network to process it.</p></details>
</section>
"""
    html = render_page(
        slug=f'payments/{slug}',
        title=title,
        description=description,
        h1=h1,
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), (coin, None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open(f'en/payments/{slug}.html','w').write(html)


def make_bitcoin():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for Bitcoin deposits and withdrawals</h2>
  <p>Bitcoin confirmations take on average 10 minutes per block on the Bitcoin network. 1win requires 3 confirmations, so expect 20 to 40 minutes for a standard deposit to credit. During periods of network congestion, blocks may take longer; track your transaction on mempool.space using your TXID.</p>
  <p>The Bitcoin network fee (miner fee) is set by market demand for block space. In low-congestion periods, fees can be as low as a few satoshis per byte (under $1 USD total). During high congestion (bull markets or after halving events), fees can spike to $5 to $50+ per transaction. Use a wallet that allows you to set a custom fee: higher fee = faster confirmation.</p>
  <p>There is no 1win-imposed maximum on Bitcoin deposits. The practical limits are the size of your holdings and the Bitcoin network's own processing capacity.</p>
</section>"""
    crypto_page(
        slug='bitcoin', coin='Bitcoin', ticker='BTC', network='Bitcoin',
        min_dep='0.0001', min_dep_usd='~$6',
        confirmations='3', deposit_time='20 to 40 minutes (3 confirmations).',
        withdrawal_time='20 to 60 minutes after 1win broadcasts the transaction',
        fee_note='Bitcoin network fees vary with congestion; typically $1 to $30 USD equivalent.',
        extra_lede='Bitcoin (BTC) is the original cryptocurrency and the most widely held digital asset worldwide.',
        extra_body=limits_body,
        title='Bitcoin deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Bitcoin (BTC) at 1win. No geographic limits, no chargebacks. Use promo code XLBONUS. Curacao 8048/JAZ licensed. Min 0.0001 BTC.',
        h1='Bitcoin deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, faster and lower fees than BTC</li>
    <li><a href="/en/payments/ethereum.html">Ethereum</a> - ETH, smart contract platform</li>
    <li><a href="/en/payments/litecoin.html">Litecoin</a> - faster BTC alternative</li>
    <li><a href="/en/payments/tron.html">Tron</a> - fast, very low fee network</li>
    <li><a href="/en/payments/upi.html">UPI</a> - Indian INR option</li>"""
    )

def make_usdt_trc20():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for USDT TRC20 deposits and withdrawals</h2>
  <p>USDT on the Tron (TRC20) network is one of the fastest and cheapest stablecoin transfer options available. Tron block time is approximately 3 seconds, and 1win requires 20 confirmations, meaning deposits typically credit in under 2 minutes in normal conditions.</p>
  <p>Tron network fees (bandwidth and energy) are very low, typically under $1 USDT for a standard USDT transfer. If your Tron address has sufficient bandwidth from staking TRX, the fee may be zero or near-zero. This makes USDT TRC20 the preferred option for players who want to avoid variable Bitcoin or Ethereum network fees.</p>
  <p>1win has no maximum deposit limit for USDT TRC20. Withdrawals are processed quickly, with most completing within 15 to 30 minutes of request submission during business hours.</p>
</section>"""
    crypto_page(
        slug='usdt-trc20', coin='USDT TRC20', ticker='USDT', network='Tron (TRC20)',
        min_dep='5', min_dep_usd='~$5',
        confirmations='20', deposit_time='1 to 3 minutes (20 Tron confirmations).',
        withdrawal_time='15 to 30 minutes',
        fee_note='Tron (TRC20) network fees are very low, typically under $1 USDT equivalent.',
        extra_lede='USDT (Tether) on the Tron TRC20 network combines USD-pegged stability with Tron\'s near-instant, low-fee blockchain.',
        extra_body=limits_body,
        title='USDT TRC20 deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Tether USDT on Tron TRC20 at 1win. Instant, near-zero fees, USD-stable. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='USDT TRC20 deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-erc20.html">USDT ERC20</a> - Tether on Ethereum, higher fees but wider wallet support</li>
    <li><a href="/en/payments/tron.html">Tron (TRX)</a> - native Tron coin</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - BTC for larger value transfers</li>
    <li><a href="/en/payments/solana.html">Solana</a> - another fast, low-fee network</li>
    <li><a href="/en/payments/upi.html">UPI</a> - Indian INR local option</li>"""
    )

def make_usdt_erc20():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for USDT ERC20 deposits and withdrawals</h2>
  <p>USDT on the Ethereum (ERC20) network has the broadest wallet and exchange support of any USDT variant, but at a higher cost. Ethereum block time is approximately 12 seconds, and 1win requires 12 confirmations, placing typical deposit confirmation time at 3 to 5 minutes under normal conditions.</p>
  <p>Ethereum gas fees vary significantly with network load. In quiet periods, a USDT ERC20 transfer costs $2 to $10 USD in gas. During DeFi activity spikes, fees can reach $50 to $100+ USD per transaction. For deposits under $100 USD, USDT TRC20 is almost always cheaper. USDT ERC20 is worth using if your source wallet or exchange does not support TRC20 withdrawal.</p>
  <p>There is no 1win maximum deposit cap for USDT ERC20. Withdrawals process within 15 to 60 minutes of request submission.</p>
</section>"""
    crypto_page(
        slug='usdt-erc20', coin='USDT ERC20', ticker='USDT', network='Ethereum (ERC20)',
        min_dep='10', min_dep_usd='~$10',
        confirmations='12', deposit_time='3 to 5 minutes (12 Ethereum confirmations).',
        withdrawal_time='15 to 60 minutes',
        fee_note='Ethereum gas fees vary with network congestion; typically $5 to $50 USD per transaction.',
        extra_lede='USDT (Tether) on the Ethereum ERC20 network is the most widely supported USDT variant and is accepted at virtually every crypto exchange.',
        extra_body=limits_body,
        title='USDT ERC20 deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Tether USDT on Ethereum ERC20 at 1win. USD-stable, min $10 USDT. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='USDT ERC20 deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - same Tether but on Tron: much lower fees</li>
    <li><a href="/en/payments/ethereum.html">Ethereum (ETH)</a> - native ETH deposits</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - BTC alternative</li>
    <li><a href="/en/payments/solana.html">Solana</a> - fast, low-fee alternative network</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - e-wallet for USD/EUR</li>"""
    )

def make_ethereum():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for Ethereum deposits and withdrawals</h2>
  <p>Ethereum deposits at 1win require 12 network confirmations. With Ethereum's 12-second block time post-Merge, this means deposits typically confirm in 2 to 4 minutes under normal network conditions. Track your deposit status on Etherscan.io with your transaction hash.</p>
  <p>Ethereum gas fees are paid in ETH (gwei) and fluctuate with network usage. Standard ETH transfers cost less gas than complex smart contract calls. A simple ETH transfer typically costs 21,000 gas units; at 30 gwei gas price, that is 0.00063 ETH (approximately $2 to $3 USD at typical prices). During peak demand periods, gas prices can spike 10x.</p>
  <p>No 1win maximum deposit cap for ETH. Minimum deposit is 0.01 ETH. Withdrawal network fees are deducted from the withdrawal amount and shown before confirmation.</p>
</section>"""
    crypto_page(
        slug='ethereum', coin='Ethereum', ticker='ETH', network='Ethereum',
        min_dep='0.01', min_dep_usd='~$25',
        confirmations='12', deposit_time='2 to 5 minutes (12 Ethereum confirmations).',
        withdrawal_time='15 to 45 minutes',
        fee_note='Ethereum gas fees are paid in ETH and vary with network congestion; typically $2 to $20 USD.',
        extra_lede='Ethereum (ETH) is the second-largest cryptocurrency by market cap and the foundation of the DeFi and NFT ecosystem.',
        extra_body=limits_body,
        title='Ethereum deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Ethereum (ETH) at 1win. Fast blockchain confirmation, global access. Use promo code XLBONUS. Curacao 8048/JAZ licensed. Min 0.01 ETH.',
        h1='Ethereum deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-erc20.html">USDT ERC20</a> - USD-stable Tether on Ethereum</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - lower-fee stablecoin option</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - BTC as the leading cryptocurrency</li>
    <li><a href="/en/payments/solana.html">Solana</a> - faster, cheaper alternative</li>
    <li><a href="/en/payments/ripple.html">Ripple (XRP)</a> - fast settlement coin</li>"""
    )

def make_litecoin():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for Litecoin deposits and withdrawals</h2>
  <p>Litecoin produces a new block every 2.5 minutes (4x faster than Bitcoin). 1win requires 6 Litecoin confirmations, so deposits typically credit in 15 to 20 minutes. This is significantly faster than Bitcoin's average 30-40 minute deposit time at 3 confirmations.</p>
  <p>Litecoin transaction fees are very low compared to Bitcoin and Ethereum. A standard LTC transfer typically costs 0.001 LTC or less in network fees (well under $0.10 USD at current prices). This makes LTC attractive for smaller, frequent deposits where Bitcoin fees would eat into the transferred amount.</p>
  <p>Minimum LTC deposit at 1win is 0.05 LTC. There is no maximum cap from 1win's side. Withdrawal fees are deducted from the sent amount; shown before you confirm.</p>
</section>"""
    crypto_page(
        slug='litecoin', coin='Litecoin', ticker='LTC', network='Litecoin',
        min_dep='0.05', min_dep_usd='~$3',
        confirmations='6', deposit_time='15 to 20 minutes (6 Litecoin confirmations).',
        withdrawal_time='20 to 40 minutes',
        fee_note='Litecoin network fees are very low, typically under $0.10 USD per transaction.',
        extra_lede='Litecoin (LTC) was created in 2011 as a faster, lower-fee alternative to Bitcoin and remains one of the most reliable, battle-tested cryptocurrencies for payments.',
        extra_body=limits_body,
        title='Litecoin deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Litecoin (LTC) at 1win. Faster than Bitcoin, very low fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed. Min 0.05 LTC.',
        h1='Litecoin deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - the original crypto, higher value per coin</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - USD-stable stablecoin, very low fees</li>
    <li><a href="/en/payments/tron.html">Tron (TRX)</a> - fast, cheap alternative</li>
    <li><a href="/en/payments/ripple.html">Ripple (XRP)</a> - fast settlement coin</li>
    <li><a href="/en/payments/solana.html">Solana</a> - high-speed blockchain</li>"""
    )

def make_tron():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for Tron deposits and withdrawals</h2>
  <p>Tron is one of the fastest major blockchains. Block time is approximately 3 seconds, and 1win requires 20 confirmations, meaning deposits confirm in under 2 minutes. This is among the fastest deposit confirmation times of any cryptocurrency accepted at 1win.</p>
  <p>Tron transaction fees are paid using bandwidth and energy resources. Standard TRX transfers cost a small amount of bandwidth, which is replenished over time for addresses with TRX staked. If you have sufficient bandwidth, TRX transfers can be effectively fee-free. For accounts without staked TRX, a small TRX amount is burned as the network fee, typically under 1 TRX ($0.10 USD or less).</p>
  <p>Minimum TRX deposit at 1win is 50 TRX. There is no maximum from 1win's side. Tron's high throughput (2,000 transactions per second capacity) means congestion is rare.</p>
</section>"""
    crypto_page(
        slug='tron', coin='Tron', ticker='TRX', network='Tron',
        min_dep='50', min_dep_usd='~$5',
        confirmations='20', deposit_time='Under 2 minutes (20 Tron confirmations at 3-second blocks).',
        withdrawal_time='10 to 30 minutes',
        fee_note='Tron network fees are near-zero for accounts with staked TRX; typically under 1 TRX for others.',
        extra_lede='Tron (TRX) is a high-throughput blockchain designed for fast, low-cost digital asset transfers and is the native network for USDT TRC20.',
        extra_body=limits_body,
        title='Tron (TRX) deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Tron (TRX) at 1win. Sub-2-minute confirmations, near-zero fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed. Min 50 TRX.',
        h1='Tron (TRX) deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - USD-stable Tether on the Tron network</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - BTC for larger value transfers</li>
    <li><a href="/en/payments/solana.html">Solana</a> - another fast blockchain</li>
    <li><a href="/en/payments/litecoin.html">Litecoin</a> - fast payments alternative</li>
    <li><a href="/en/payments/ripple.html">Ripple (XRP)</a> - settlement-focused crypto</li>"""
    )

def make_solana():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for Solana deposits and withdrawals</h2>
  <p>Solana is one of the fastest layer-1 blockchains, processing up to 65,000 transactions per second with block times of approximately 400 milliseconds. 1win requires 20 confirmations on Solana, which typically complete in under 10 seconds. This makes Solana the fastest option for crypto deposits at 1win.</p>
  <p>Solana network fees are extremely low, typically 0.000005 SOL per transaction (fractions of a cent at current SOL prices). This makes SOL ideal for small and frequent deposits where high ETH or BTC fees would be impractical.</p>
  <p>Minimum SOL deposit at 1win is 0.1 SOL. There is no 1win-imposed maximum. Withdrawals process quickly, with most dispatching within 15 minutes of submission.</p>
</section>"""
    crypto_page(
        slug='solana', coin='Solana', ticker='SOL', network='Solana',
        min_dep='0.1', min_dep_usd='~$15',
        confirmations='20', deposit_time='Under 30 seconds (20 Solana confirmations).',
        withdrawal_time='15 to 30 minutes',
        fee_note='Solana network fees are a fraction of a cent per transaction, among the lowest in crypto.',
        extra_lede='Solana (SOL) is a high-performance layer-1 blockchain capable of 65,000 transactions per second with sub-second finality, making it the fastest major cryptocurrency for payments.',
        extra_body=limits_body,
        title='Solana deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw Solana (SOL) at 1win. Sub-30-second confirmations, near-zero fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed. Min 0.1 SOL.',
        h1='Solana deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - USD-stable option on Tron</li>
    <li><a href="/en/payments/tron.html">Tron (TRX)</a> - fast and low-fee like Solana</li>
    <li><a href="/en/payments/ethereum.html">Ethereum</a> - ETH on the Ethereum network</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - BTC for high-value transfers</li>
    <li><a href="/en/payments/ripple.html">Ripple (XRP)</a> - fast settlement alternative</li>"""
    )

def make_ripple():
    limits_body = """<section class="limits-timing">
  <h2>Limits and timing for Ripple (XRP) deposits and withdrawals</h2>
  <p>XRP transactions settle in 3 to 5 seconds on the XRP Ledger. 1win requires 6 confirmations, meaning deposits typically credit in under 30 seconds. XRP is one of the fastest confirmation chains at 1win, comparable only to Solana and Tron.</p>
  <p>XRP network fees are set by the protocol: a standard XRP transaction costs 0.00001 XRP (10 drops), which is a negligible fraction of a cent at any realistic XRP price. This makes XRP extremely cost-efficient for any deposit size.</p>
  <p>Important note: When depositing XRP at 1win, a destination tag (memo) is required. The cashier displays a unique destination tag when you generate your deposit address. Sending XRP without the correct destination tag may result in your funds being unallocated. Contact live-chat with your TXID and destination tag if you forget to include it.</p>
</section>"""
    crypto_page(
        slug='ripple', coin='Ripple', ticker='XRP', network='XRP Ledger',
        min_dep='5', min_dep_usd='~$3',
        confirmations='6', deposit_time='Under 30 seconds (6 XRP Ledger confirmations).',
        withdrawal_time='10 to 30 minutes',
        fee_note='XRP Ledger fees are a tiny fraction of a cent per transaction (0.00001 XRP).',
        extra_lede='Ripple (XRP) is a digital settlement asset designed for fast, low-cost cross-border payments and is accepted at 1win for instant deposits with near-zero fees.',
        extra_body=limits_body,
        title='Ripple (XRP) deposit and withdrawal at 1win with XLBONUS',
        description='Deposit and withdraw XRP at 1win. Sub-30-second settlement, near-zero fees. Destination tag required. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Ripple (XRP) deposit and withdrawal at 1win',
        alt_methods="""    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - USD-stable stablecoin, also very fast</li>
    <li><a href="/en/payments/tron.html">Tron (TRX)</a> - fast blockchain like XRP</li>
    <li><a href="/en/payments/solana.html">Solana</a> - high-throughput alternative</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - BTC for larger value transfers</li>
    <li><a href="/en/payments/litecoin.html">Litecoin</a> - LTC as crypto alternative</li>"""
    )


if __name__ == '__main__':
    make_bitcoin()
    make_usdt_trc20()
    make_usdt_erc20()
    make_ethereum()
    make_litecoin()
    make_tron()
    make_solana()
    make_ripple()
    print("Crypto pages done: 8 files")
