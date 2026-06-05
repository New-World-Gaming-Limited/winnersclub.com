"""
Generate payments hub page (en/payments/index.html) for 1win.codes
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_helpers.page_template import render_page

os.makedirs('en/payments', exist_ok=True)

def make_hub():
    extra_head = """<style>
.payment-search-bar {
  margin: 1.5rem 0;
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
}
.payment-search-bar input {
  flex: 1 1 220px;
  padding: 0.55rem 1rem;
  border: 1px solid var(--color-border, #ddd);
  border-radius: 6px;
  font-size: 1rem;
}
.filter-btns {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.filter-btn {
  padding: 0.4rem 0.9rem;
  border: 1px solid var(--color-border, #ccc);
  border-radius: 20px;
  cursor: pointer;
  font-size: 0.875rem;
  background: var(--color-bg, #fff);
  transition: background 0.15s, color 0.15s;
}
.filter-btn.active, .filter-btn:hover {
  background: #1a3fa3;
  color: #fff;
  border-color: #1a3fa3;
}
.pm-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}
.pm-card {
  border: 1px solid var(--color-border, #e0e0e0);
  border-radius: 10px;
  padding: 1.1rem;
  text-decoration: none;
  color: inherit;
  display: block;
  transition: box-shadow 0.15s, transform 0.1s;
}
.pm-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  transform: translateY(-2px);
  text-decoration: none;
}
.pm-card .pm-name { font-weight: 600; font-size: 1rem; margin-bottom: 0.25rem; }
.pm-card .pm-meta { font-size: 0.8rem; color: #666; }
.pm-card .pm-badge {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  border-radius: 10px;
  font-size: 0.7rem;
  font-weight: 600;
  margin-bottom: 0.4rem;
}
.pm-card .pm-badge.badge-india { background: #FF9933; color: #fff; }
.pm-card .pm-badge.badge-brazil { background: #009c3b; color: #fff; }
.pm-card .pm-badge.badge-africa { background: #c8102e; color: #fff; }
.pm-card .pm-badge.badge-pakistan { background: #01411C; color: #fff; }
.pm-card .pm-badge.badge-crypto { background: #F7931A; color: #fff; }
.pm-card .pm-badge.badge-ewallet { background: #6941C6; color: #fff; }
.pm-card .pm-badge.badge-card { background: #1a3fa3; color: #fff; }
.pm-group-title { font-size: 1.25rem; font-weight: 700; margin: 2rem 0 0.75rem; padding-bottom: 0.4rem; border-bottom: 2px solid var(--color-border, #eee); }
.hidden { display: none !important; }
.no-results { padding: 2rem 0; color: #888; font-size: 1rem; display: none; }
</style>"""

    extra_scripts = """<script>
(function() {
  var searchInput = document.getElementById('pm-search');
  var filterBtns = document.querySelectorAll('.filter-btn');
  var allCards = document.querySelectorAll('.pm-card');
  var noResults = document.getElementById('no-results');
  var activeFilter = 'all';

  function applyFilters() {
    var q = searchInput.value.toLowerCase().trim();
    var count = 0;
    allCards.forEach(function(card) {
      var cat = card.getAttribute('data-cat');
      var text = card.textContent.toLowerCase();
      var matchCat = (activeFilter === 'all' || cat === activeFilter);
      var matchQ = (!q || text.indexOf(q) > -1);
      if (matchCat && matchQ) { card.classList.remove('hidden'); count++; }
      else { card.classList.add('hidden'); }
    });
    // Show/hide section headers based on visible cards
    document.querySelectorAll('.pm-section').forEach(function(section) {
      var visible = section.querySelectorAll('.pm-card:not(.hidden)').length;
      section.style.display = visible ? '' : 'none';
    });
    noResults.style.display = count === 0 ? 'block' : 'none';
  }

  searchInput.addEventListener('input', applyFilters);

  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      filterBtns.forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeFilter = btn.getAttribute('data-filter');
      applyFilters();
    });
  });
})();
</script>"""

    main = """
<section class="lede">
  <p>1win supports 32 payment methods across India, Brazil, Africa, Pakistan, crypto networks, e-wallets, and cards, all on a Curaçao 8048/JAZ-licensed platform trusted by 400,000+ players worldwide. Find your method below, or search by name. Use promo code <span class="code-highlight">XLBONUS</span> on your first deposit to activate the welcome bonus.</p>
</section>

<div class="payment-search-bar">
  <input type="search" id="pm-search" placeholder="Search payment methods..." aria-label="Search payment methods">
  <div class="filter-btns" role="group" aria-label="Filter by region">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="india">India</button>
    <button class="filter-btn" data-filter="brazil">Brazil</button>
    <button class="filter-btn" data-filter="africa">Africa</button>
    <button class="filter-btn" data-filter="pakistan">Pakistan</button>
    <button class="filter-btn" data-filter="crypto">Crypto</button>
    <button class="filter-btn" data-filter="ewallet">E-wallets</button>
    <button class="filter-btn" data-filter="card">Cards</button>
  </div>
</div>

<p class="no-results" id="no-results">No payment methods found. Try a different search term or filter.</p>

<!-- India -->
<div class="pm-section">
<p class="pm-group-title">India (INR)</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/upi.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">UPI</p>
    <p class="pm-meta">Instant. Min INR 300. Any UPI app.</p>
  </a>
  <a class="pm-card" href="/en/payments/phonepe.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">PhonePe</p>
    <p class="pm-meta">Instant UPI. Min INR 300. India's largest UPI app.</p>
  </a>
  <a class="pm-card" href="/en/payments/google-pay.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">Google Pay</p>
    <p class="pm-meta">Instant UPI via GPay. Min INR 300.</p>
  </a>
  <a class="pm-card" href="/en/payments/paytm.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">Paytm</p>
    <p class="pm-meta">UPI via Paytm VPA. Min INR 300.</p>
  </a>
  <a class="pm-card" href="/en/payments/imps.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">IMPS</p>
    <p class="pm-meta">Up to 5 lakh INR per transaction. 5-30 min.</p>
  </a>
  <a class="pm-card" href="/en/payments/neft.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">NEFT</p>
    <p class="pm-meta">No RBI cap. 30-120 min batch settlement.</p>
  </a>
  <a class="pm-card" href="/en/payments/rupay.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">RuPay</p>
    <p class="pm-meta">Domestic Indian card. Min INR 500.</p>
  </a>
  <a class="pm-card" href="/en/payments/netbanking.html" data-cat="india">
    <span class="pm-badge badge-india">India</span>
    <p class="pm-name">Net banking</p>
    <p class="pm-meta">SBI, HDFC, ICICI and 50+ banks. Min INR 500.</p>
  </a>
</div>
</div>

<!-- Brazil -->
<div class="pm-section">
<p class="pm-group-title">Brazil (BRL)</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/pix.html" data-cat="brazil">
    <span class="pm-badge badge-brazil">Brazil</span>
    <p class="pm-name">PIX</p>
    <p class="pm-meta">Instant 24/7. Min R$20. CPF required.</p>
  </a>
  <a class="pm-card" href="/en/payments/boleto.html" data-cat="brazil">
    <span class="pm-badge badge-brazil">Brazil</span>
    <p class="pm-name">Boleto</p>
    <p class="pm-meta">Bank slip. Min R$30. 1-3 business days.</p>
  </a>
</div>
</div>

<!-- Africa -->
<div class="pm-section">
<p class="pm-group-title">Africa (mobile money and more)</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/mpesa.html" data-cat="africa">
    <span class="pm-badge badge-africa">Africa</span>
    <p class="pm-name">M-Pesa</p>
    <p class="pm-meta">Kenya (KSh), Tanzania (TSh). Instant mobile money.</p>
  </a>
  <a class="pm-card" href="/en/payments/airtel-money.html" data-cat="africa">
    <span class="pm-badge badge-africa">Africa</span>
    <p class="pm-name">Airtel Money</p>
    <p class="pm-meta">14 African countries. KSh, UGX and more.</p>
  </a>
  <a class="pm-card" href="/en/payments/mtn-momo.html" data-cat="africa">
    <span class="pm-badge badge-africa">Africa</span>
    <p class="pm-name">MTN MoMo</p>
    <p class="pm-meta">Ghana (GHS), Uganda (UGX) and 15 more markets.</p>
  </a>
  <a class="pm-card" href="/en/payments/orange-money.html" data-cat="africa">
    <span class="pm-badge badge-africa">Africa</span>
    <p class="pm-name">Orange Money</p>
    <p class="pm-meta">Francophone Africa. XOF, XAF, MAD supported.</p>
  </a>
  <a class="pm-card" href="/en/payments/flutterwave.html" data-cat="africa">
    <span class="pm-badge badge-africa">Africa</span>
    <p class="pm-name">Flutterwave</p>
    <p class="pm-meta">34 African countries. NGN, GHS, KSh and more.</p>
  </a>
</div>
</div>

<!-- Pakistan -->
<div class="pm-section">
<p class="pm-group-title">Pakistan (PKR)</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/easypaisa.html" data-cat="pakistan">
    <span class="pm-badge badge-pakistan">Pakistan</span>
    <p class="pm-name">Easypaisa</p>
    <p class="pm-meta">Instant mobile money. Min PKR 500.</p>
  </a>
  <a class="pm-card" href="/en/payments/jazzcash.html" data-cat="pakistan">
    <span class="pm-badge badge-pakistan">Pakistan</span>
    <p class="pm-name">JazzCash</p>
    <p class="pm-meta">Instant mobile money. Min PKR 500. Jazz network.</p>
  </a>
</div>
</div>

<!-- Crypto -->
<div class="pm-section">
<p class="pm-group-title">Cryptocurrency</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/bitcoin.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">Bitcoin (BTC)</p>
    <p class="pm-meta">Global. Min 0.0001 BTC. 20-40 min (3 confirmations).</p>
  </a>
  <a class="pm-card" href="/en/payments/usdt-trc20.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">USDT TRC20</p>
    <p class="pm-meta">Tether on Tron. USD-stable. Under 2 min. Near-zero fees.</p>
  </a>
  <a class="pm-card" href="/en/payments/usdt-erc20.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">USDT ERC20</p>
    <p class="pm-meta">Tether on Ethereum. USD-stable. 3-5 min.</p>
  </a>
  <a class="pm-card" href="/en/payments/ethereum.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">Ethereum (ETH)</p>
    <p class="pm-meta">Min 0.01 ETH. 2-5 min (12 confirmations).</p>
  </a>
  <a class="pm-card" href="/en/payments/litecoin.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">Litecoin (LTC)</p>
    <p class="pm-meta">Min 0.05 LTC. 15-20 min. Very low fees.</p>
  </a>
  <a class="pm-card" href="/en/payments/tron.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">Tron (TRX)</p>
    <p class="pm-meta">Min 50 TRX. Under 2 min. Near-zero fees.</p>
  </a>
  <a class="pm-card" href="/en/payments/solana.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">Solana (SOL)</p>
    <p class="pm-meta">Min 0.1 SOL. Under 30 seconds. Fraction-of-cent fees.</p>
  </a>
  <a class="pm-card" href="/en/payments/ripple.html" data-cat="crypto">
    <span class="pm-badge badge-crypto">Crypto</span>
    <p class="pm-name">Ripple (XRP)</p>
    <p class="pm-meta">Min 5 XRP. Under 30 sec. Destination tag required.</p>
  </a>
</div>
</div>

<!-- E-wallets -->
<div class="pm-section">
<p class="pm-group-title">E-wallets</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/skrill.html" data-cat="ewallet">
    <span class="pm-badge badge-ewallet">E-wallet</span>
    <p class="pm-name">Skrill</p>
    <p class="pm-meta">120+ countries. USD, EUR, GBP. Instant deposits.</p>
  </a>
  <a class="pm-card" href="/en/payments/neteller.html" data-cat="ewallet">
    <span class="pm-badge badge-ewallet">E-wallet</span>
    <p class="pm-name">Neteller</p>
    <p class="pm-meta">200+ countries. Net+ Mastercard for winnings.</p>
  </a>
  <a class="pm-card" href="/en/payments/ecopayz.html" data-cat="ewallet">
    <span class="pm-badge badge-ewallet">E-wallet</span>
    <p class="pm-name">EcoPayz</p>
    <p class="pm-meta">160+ countries. FCA regulated. EcoCard available.</p>
  </a>
  <a class="pm-card" href="/en/payments/muchbetter.html" data-cat="ewallet">
    <span class="pm-badge badge-ewallet">E-wallet</span>
    <p class="pm-name">MuchBetter</p>
    <p class="pm-meta">Mobile-first. Push-notification approval. Instant.</p>
  </a>
</div>
</div>

<!-- Cards -->
<div class="pm-section">
<p class="pm-group-title">Cards</p>
<div class="pm-grid">
  <a class="pm-card" href="/en/payments/visa.html" data-cat="card">
    <span class="pm-badge badge-card">Card</span>
    <p class="pm-name">Visa</p>
    <p class="pm-meta">200+ countries. Debit and credit. Instant.</p>
  </a>
  <a class="pm-card" href="/en/payments/mastercard.html" data-cat="card">
    <span class="pm-badge badge-card">Card</span>
    <p class="pm-name">Mastercard</p>
    <p class="pm-meta">200+ countries. Debit and credit. Instant.</p>
  </a>
  <a class="pm-card" href="/en/payments/maestro.html" data-cat="card">
    <span class="pm-badge badge-card">Card</span>
    <p class="pm-name">Maestro</p>
    <p class="pm-meta">European debit card. Phasing out in some markets.</p>
  </a>
</div>
</div>

<section class="cta" style="margin-top:2.5rem;">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="key-facts" style="margin-top:2.5rem;">
  <h2>About 1win payments</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>1win fee on deposits</td><td>None (all 32 methods)</td></tr>
    <tr><td>1win fee on withdrawals</td><td>None for fiat; crypto withdrawals deduct network fee</td></tr>
    <tr><td>Fastest deposit method</td><td>Solana (SOL), Tron (TRX), USDT TRC20 (under 2 min); UPI, PIX, MuchBetter (under 1 min)</td></tr>
    <tr><td>Fastest withdrawal</td><td>Crypto: 10-60 min. E-wallets: 15 min to 3 hr. Bank transfers: 1-5 business days</td></tr>
    <tr><td>License</td><td>Curacao 8048/JAZ</td></tr>
    <tr><td>KYC requirement</td><td>Required before first withdrawal. ID upload via Profile section.</td></tr>
    <tr><td>Currency conversion</td><td>1win wallet displays USD equivalent for most methods; local currency for regional methods</td></tr>
  </table>
</section>

<section class="faq">
  <h2>FAQ: 1win payment methods</h2>
  <details><summary>Which payment method is fastest for deposits at 1win?</summary><p>For crypto: Solana (SOL) and Tron (TRX) confirm in under 30 seconds. USDT TRC20 confirms in under 2 minutes. For fiat: UPI (India), PIX (Brazil), M-Pesa (Africa), and MuchBetter (global) all credit in under 60 seconds. Standard bank transfers like NEFT and Boleto take longer due to batch settlement.</p></details>
  <details><summary>Does 1win charge any fees on deposits or withdrawals?</summary><p>1win charges zero fees on deposits and withdrawals for all 32 payment methods. Crypto withdrawals include a network fee that is deducted from the sent amount; this is a blockchain fee, not a 1win charge. Provider fees (bank charges, mobile money fees, card foreign transaction fees) are set by the payment provider and are outside 1win's control.</p></details>
  <details><summary>Which payment method is best for Indian players at 1win?</summary><p>UPI is the fastest and most convenient for Indian players. IMPS is best for large single transfers (up to 5 lakh INR). NEFT has no transaction cap. If UPI/bank methods are declining, USDT TRC20 or Bitcoin are geographic-agnostic alternatives with no RBI restrictions.</p></details>
  <details><summary>How do I withdraw winnings from 1win?</summary><p>Open the Cashier, click Withdrawal, and choose your preferred method. Complete KYC (identity verification) in your Profile before the first withdrawal. Most e-wallet and mobile money withdrawals complete in 15 minutes to 3 hours. Bank transfers take 1 to 5 business days. Crypto withdrawals take 10 to 60 minutes depending on the network.</p></details>
  <details><summary>Is my payment information safe at 1win?</summary><p>Yes. 1win uses PCI DSS-compliant payment gateways. Card details are processed by the payment provider, not stored on 1win's servers. Crypto deposits use a unique wallet address per user session. E-wallet deposits do not expose bank details to 1win.</p></details>
</section>
"""

    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Which payment method is fastest for deposits at 1win?","acceptedAnswer":{"@type":"Answer","text":"For crypto: Solana (SOL) and Tron (TRX) confirm in under 30 seconds. For fiat: UPI, PIX, M-Pesa, and MuchBetter all credit in under 60 seconds."}},
    {"@type":"Question","name":"Does 1win charge any fees on deposits or withdrawals?","acceptedAnswer":{"@type":"Answer","text":"1win charges zero fees on deposits and withdrawals for all 32 payment methods. Crypto withdrawals include a network fee deducted from the sent amount; provider fees are set by the payment provider."}},
    {"@type":"Question","name":"Which payment method is best for Indian players at 1win?","acceptedAnswer":{"@type":"Answer","text":"UPI is fastest. IMPS handles up to 5 lakh INR. NEFT has no cap. USDT TRC20 or Bitcoin work without RBI restrictions."}},
    {"@type":"Question","name":"How do I withdraw winnings from 1win?","acceptedAnswer":{"@type":"Answer","text":"Open the Cashier, click Withdrawal, choose your method. Complete KYC first. E-wallet/mobile money takes 15 min to 3 hr; bank transfers 1-5 business days; crypto 10-60 min."}},
    {"@type":"Question","name":"Is my payment information safe at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win uses PCI DSS-compliant gateways. Card details are processed by the provider, not stored on 1win. Crypto uses a unique address per session. E-wallet deposits do not expose bank details."}}
  ]
}
</script>"""

    html = render_page(
        slug='payments/index',
        title='1win payment methods: 32 options for deposit and withdrawal',
        description='All 32 payment methods at 1win: UPI, PIX, M-Pesa, Bitcoin, USDT, Skrill, Visa and more. Search by region or type. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='1win payment methods hub',
        breadcrumbs=[('Home','/en/'), ('Payments', None)],
        main_html=main,
        extra_head=extra_head,
        extra_scripts=extra_scripts,
        extra_schema=faq_schema,
    )
    open('en/payments/index.html','w').write(html)
    print("Hub page done: en/payments/index.html")


if __name__ == '__main__':
    make_hub()
