"""
Generate E-wallet and Card payment method pages for 1win.codes
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_helpers.page_template import render_page

os.makedirs('en/payments', exist_ok=True)

# ── Skrill ────────────────────────────────────────────────────────────────────
def make_skrill():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is the minimum Skrill deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Skrill deposit at 1win is $10 USD (or equivalent in EUR or GBP). The exact minimum depends on your Skrill account currency."}},
    {"@type":"Question","name":"How fast are Skrill deposits at 1win?","acceptedAnswer":{"@type":"Answer","text":"Skrill deposits are instant. Your 1win wallet updates within 60 seconds of completing payment in the Skrill flow."}},
    {"@type":"Question","name":"Can I withdraw from 1win to Skrill?","acceptedAnswer":{"@type":"Answer","text":"Yes. Withdrawals to Skrill are supported. Processing takes 15 minutes to 3 hours from 1win's side; once credited to Skrill, funds are available instantly in your Skrill wallet."}},
    {"@type":"Question","name":"Does Skrill charge fees for 1win transactions?","acceptedAnswer":{"@type":"Answer","text":"Skrill charges a currency conversion fee if your Skrill wallet currency differs from the transaction currency. 1win charges no additional fee. Skrill-to-bank withdrawal fees may apply when cashing out of Skrill."}},
    {"@type":"Question","name":"My country is not supported by Skrill. What should I do?","acceptedAnswer":{"@type":"Answer","text":"Skrill has a restricted country list (some African and Asian countries). If Skrill is not available in your country, use a local mobile money method, Neteller, or crypto at 1win instead."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Skrill is a globally accepted digital wallet supporting USD, EUR, and GBP, fully integrated at 1win for instant deposits and withdrawals. 1win holds a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. Skrill's VIP programme and loyalty points make it particularly attractive for high-volume players. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus on your first Skrill deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Skrill at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or EUR/GBP equivalent)</td></tr>
    <tr><td>Maximum deposit</td><td>No 1win cap; Skrill account limits apply</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 60 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Skrill currency conversion fee may apply; no P2P merchant fee</td></tr>
    <tr><td>Supported currencies</td><td>USD, EUR, GBP (and 40 other currencies in Skrill)</td></tr>
    <tr><td>Geographic availability</td><td>120+ countries (Skrill's supported country list)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Skrill at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Skrill from the payment method list.</strong> Enter the deposit amount in USD, EUR, or GBP.</li>
    <li><strong>You are redirected to a Skrill login page.</strong> Log in to your Skrill account (or create one at skrill.com if you do not have one).</li>
    <li><strong>Authorise the payment in Skrill.</strong> Confirm the amount and recipient (1win). Skrill may send a one-time password (OTP) to your registered email or phone for 2FA confirmation.</li>
    <li><strong>Return to 1win.</strong> The redirect brings you back to 1win automatically. Your wallet balance updates within 60 seconds. If it does not, check the Skrill transaction history and contact 1win live-chat with the Skrill transaction ID.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to Skrill</h2>
  <ol>
    <li><strong>Complete KYC on 1win.</strong> Upload a photo ID before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose Skrill.</strong></li>
    <li><strong>Enter your Skrill account email address.</strong> This is the email you use to log in to Skrill. Verify it carefully.</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm the Skrill email on the summary screen.</li>
    <li><strong>Submit.</strong> 1win processes the withdrawal within 15 minutes to 3 hours. Once credited, funds appear instantly in your Skrill balance. You then withdraw from Skrill to your bank or card as needed.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Skrill account limits depend on your verification level. Unverified Skrill accounts have a cumulative lifetime upload limit of 2,500 EUR and cannot withdraw to a bank. Verified accounts (passport/ID submitted) have higher limits: up to 900,000 EUR per year in uploads and withdrawals. For 1win deposits, the practical limit is whichever is lower: your Skrill account limit or 1win's own maximum.</p>
  <p>Skrill deposits at 1win are instant, making it one of the best e-wallet options for time-sensitive deposits before a match starts. Withdrawals from 1win back to Skrill process within the hour for most requests during business hours.</p>
  <p>Skrill charges a 4.99% fee for deposits funded by credit or debit card. If you fund your Skrill wallet via bank transfer first, you avoid this card surcharge. Funding via cryptocurrency to Skrill is also free of this fee.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Skrill is available in 120+ countries and supports 40+ currencies. In Europe, USD, EUR, and GBP are the primary currencies. Skrill is not available in some countries including the United States (for gambling transactions), North Korea, and a few others on the restricted list. If you are in a region where Skrill is restricted, use Neteller, crypto, or local mobile money at 1win instead.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/neteller.html">Neteller</a> - sister e-wallet to Skrill, similar features</li>
    <li><a href="/en/payments/ecopayz.html">EcoPayz</a> - European-regulated e-wallet</li>
    <li><a href="/en/payments/muchbetter.html">MuchBetter</a> - mobile-first e-wallet</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - crypto stablecoin, no e-wallet account needed</li>
    <li><a href="/en/payments/visa.html">Visa</a> - card deposit directly without a wallet</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Skrill at 1win</h2>
  <details><summary>What is the minimum Skrill deposit at 1win?</summary><p>Minimum Skrill deposit at 1win is $10 USD (or equivalent in EUR or GBP). The exact minimum depends on your Skrill account currency.</p></details>
  <details><summary>How fast are Skrill deposits at 1win?</summary><p>Skrill deposits are instant. Your 1win wallet updates within 60 seconds of completing payment in the Skrill flow.</p></details>
  <details><summary>Can I withdraw from 1win to Skrill?</summary><p>Yes. Withdrawals to Skrill are supported. Processing takes 15 minutes to 3 hours from 1win's side; once credited to Skrill, funds are available instantly in your Skrill wallet.</p></details>
  <details><summary>Does Skrill charge fees for 1win transactions?</summary><p>Skrill charges a currency conversion fee if your Skrill wallet currency differs from the transaction currency. 1win charges no additional fee. Skrill-to-bank withdrawal fees may apply when cashing out of Skrill.</p></details>
  <details><summary>My country is not supported by Skrill. What should I do?</summary><p>Skrill has a restricted country list (some African and Asian countries). If Skrill is not available in your country, use a local mobile money method, Neteller, or crypto at 1win instead.</p></details>
</section>
"""
    html = render_page(
        slug='payments/skrill',
        title='Skrill at 1win: deposit, withdraw, claim XLBONUS',
        description='Use Skrill e-wallet at 1win for instant deposits and withdrawals. USD, EUR, GBP supported. Register with promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Skrill at 1win: deposit and withdrawal guide',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Skrill', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/skrill.html','w').write(html)

# ── Neteller ──────────────────────────────────────────────────────────────────
def make_neteller():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is the minimum Neteller deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Neteller deposit at 1win is $10 USD or EUR equivalent."}},
    {"@type":"Question","name":"How quickly are Neteller deposits credited at 1win?","acceptedAnswer":{"@type":"Answer","text":"Neteller deposits are instant. Your 1win wallet updates within 60 seconds of authorising the payment in Neteller."}},
    {"@type":"Question","name":"Can I get a Net+ card to use my 1win Neteller winnings in person?","acceptedAnswer":{"@type":"Answer","text":"Yes. Neteller issues the Net+ prepaid Mastercard linked to your Neteller wallet. Once winnings are withdrawn from 1win to Neteller, you can use the Net+ card at any Mastercard terminal."}},
    {"@type":"Question","name":"Does 1win support Neteller withdrawals?","acceptedAnswer":{"@type":"Answer","text":"Yes. Neteller withdrawals are supported. Processing takes 15 minutes to 3 hours from 1win. Once credited to Neteller, funds are available immediately."}},
    {"@type":"Question","name":"Neteller vs Skrill for 1win. Which is better?","acceptedAnswer":{"@type":"Answer","text":"Both are equivalent in speed and 1win integration. Neteller tends to have slightly higher limits and is popular in eastern Europe and Asia. Skrill has a larger global footprint. Choose based on which is easier to fund in your country."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Neteller is a long-established digital payment wallet used at iGaming platforms globally, including 1win, the Curaçao 8048/JAZ-licensed platform serving 400,000+ players worldwide. Neteller supports USD, EUR, and GBP with instant deposits and fast withdrawals. The Net+ prepaid Mastercard lets you spend Neteller balances (including 1win winnings) at physical and online stores. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Neteller at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or EUR equivalent)</td></tr>
    <tr><td>Maximum deposit</td><td>Subject to Neteller account limits</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 60 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Neteller currency conversion fee may apply</td></tr>
    <tr><td>Supported currencies</td><td>USD, EUR, GBP (and 28 other currencies in Neteller)</td></tr>
    <tr><td>Geographic availability</td><td>200+ countries (Neteller's supported country list)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Neteller at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> Register first if new; enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Neteller from the payment options.</strong> Enter the deposit amount in USD or EUR.</li>
    <li><strong>Log in to Neteller.</strong> You are redirected to a Neteller-hosted page. Enter your Neteller account email and secure ID.</li>
    <li><strong>Approve the payment.</strong> Confirm the merchant name (1win) and amount. Complete any 2FA required by Neteller (email code or authenticator app).</li>
    <li><strong>Return to 1win.</strong> The browser returns to 1win automatically. Your wallet balance updates within 60 seconds. Check Neteller transaction history for the Neteller Transaction ID if you need to follow up.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to Neteller</h2>
  <ol>
    <li><strong>Complete 1win identity verification.</strong> Submit a government-issued photo ID before your first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose Neteller.</strong></li>
    <li><strong>Enter your Neteller account email and the withdrawal amount.</strong> The email must match the Neteller account you want to receive funds in.</li>
    <li><strong>Confirm on the summary screen.</strong> Double-check the email address.</li>
    <li><strong>Submit.</strong> 1win processes the withdrawal in 15 minutes to 3 hours. Funds appear in your Neteller wallet balance immediately upon receipt. From there, transfer to your bank or use the Net+ card.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Neteller's monthly upload limit for unverified accounts is 2,500 EUR. Verified accounts (with submitted ID and proof of address) have higher limits, potentially up to 1,000,000 EUR annually. For 1win withdrawals to Neteller, the effective limit is whichever is smaller: 1win's configured withdrawal maximum or your Neteller account's available balance capacity.</p>
  <p>Neteller processes transfers using the Paysafe Group infrastructure, which operates 24/7. Deposits are instant. Withdrawal timing from 1win to Neteller is determined by 1win's payment queue, not Neteller's processing speed. Once 1win dispatches the transfer, Neteller credits it immediately.</p>
  <p>Neteller's Net+ prepaid Mastercard allows spending of Neteller balance at any Mastercard-accepting merchant worldwide. This gives you a direct path from 1win winnings to spendable funds: 1win withdrawal to Neteller (instant once dispatched), then spend via Net+ card.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Neteller is available in 200+ countries and supports 28 currencies. Primary currencies for 1win transactions are USD, EUR, and GBP. Neteller is owned by Paysafe Group, a publicly listed UK company regulated by the FCA. Neteller is widely used in the iGaming sector and specifically designed for online betting and casino payments.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/skrill.html">Skrill</a> - Paysafe's other major e-wallet</li>
    <li><a href="/en/payments/ecopayz.html">EcoPayz</a> - European-regulated alternative</li>
    <li><a href="/en/payments/muchbetter.html">MuchBetter</a> - mobile-first e-wallet option</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no e-wallet account needed</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin alternative</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Neteller at 1win</h2>
  <details><summary>What is the minimum Neteller deposit at 1win?</summary><p>Minimum Neteller deposit at 1win is $10 USD or EUR equivalent.</p></details>
  <details><summary>How quickly are Neteller deposits credited at 1win?</summary><p>Neteller deposits are instant. Your 1win wallet updates within 60 seconds of authorising the payment in Neteller.</p></details>
  <details><summary>Can I get a Net+ card to use my 1win Neteller winnings in person?</summary><p>Yes. Neteller issues the Net+ prepaid Mastercard linked to your Neteller wallet. Once winnings are withdrawn from 1win to Neteller, you can use the Net+ card at any Mastercard terminal.</p></details>
  <details><summary>Does 1win support Neteller withdrawals?</summary><p>Yes. Neteller withdrawals are supported. Processing takes 15 minutes to 3 hours from 1win. Once credited to Neteller, funds are available immediately.</p></details>
  <details><summary>Neteller vs Skrill for 1win. Which is better?</summary><p>Both are equivalent in speed and 1win integration. Neteller tends to have slightly higher limits and is popular in eastern Europe and Asia. Skrill has a larger global footprint. Choose based on which is easier to fund in your country.</p></details>
</section>
"""
    html = render_page(
        slug='payments/neteller',
        title='Neteller at 1win: deposit, withdraw, claim XLBONUS',
        description='Use Neteller e-wallet at 1win for instant deposits and fast withdrawals. USD, EUR, GBP. Net+ card available. Register with XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Neteller at 1win: deposit and withdrawal guide',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Neteller', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/neteller.html','w').write(html)

# ── EcoPayz ───────────────────────────────────────────────────────────────────
def make_ecopayz():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is EcoPayz and how does it work at 1win?","acceptedAnswer":{"@type":"Answer","text":"EcoPayz (now branded as EcoPayz by MIR) is a UK-regulated e-wallet accepted at 1win. Fund your EcoPayz account from a bank or card, then transfer to 1win instantly. Withdrawals from 1win go back to your EcoPayz balance."}},
    {"@type":"Question","name":"What is the minimum EcoPayz deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum EcoPayz deposit at 1win is $10 USD or EUR equivalent."}},
    {"@type":"Question","name":"How do I fund my EcoPayz account to use at 1win?","acceptedAnswer":{"@type":"Answer","text":"Fund EcoPayz via bank transfer, Visa, Mastercard, or local payment options depending on your country. Once funded, depositing to 1win from EcoPayz is instant."}},
    {"@type":"Question","name":"Does EcoPayz have a prepaid card I can use with my 1win winnings?","acceptedAnswer":{"@type":"Answer","text":"Yes. EcoPayz issues an EcoCard Mastercard prepaid card linked to your EcoPayz balance. Withdraw winnings from 1win to EcoPayz, then spend via the EcoCard."}},
    {"@type":"Question","name":"Is EcoPayz available worldwide for 1win deposits?","acceptedAnswer":{"@type":"Answer","text":"EcoPayz is available in 160+ countries. Some high-risk jurisdictions may be restricted. Check ecopayz.com for the full supported country list."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>EcoPayz is a UK-regulated e-wallet accepted at 1win for instant deposits and withdrawals in USD, EUR, and GBP. 1win holds a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. EcoPayz is a privacy-preserving payment option: once you fund your EcoPayz account, you only need your EcoPayz credentials (not bank details) to transact at 1win. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: EcoPayz at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or EUR equivalent)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>EcoPayz currency conversion fee may apply</td></tr>
    <tr><td>Supported currencies</td><td>USD, EUR, GBP (EcoPayz supports 45 currencies)</td></tr>
    <tr><td>Geographic availability</td><td>160+ countries</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with EcoPayz at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select EcoPayz from the payment options.</strong> Enter the deposit amount in USD or EUR.</li>
    <li><strong>Log in to EcoPayz when redirected.</strong> Enter your EcoPayz email and password on the EcoPayz-hosted page.</li>
    <li><strong>Authorise the payment.</strong> Confirm the merchant (1win) and amount. Complete any 2FA required. EcoPayz deducts the amount from your EcoPayz balance.</li>
    <li><strong>Return to 1win.</strong> Your wallet balance updates within 60 seconds. If it does not, check your EcoPayz transaction history and share the EcoPayz transaction ID with 1win live-chat.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to EcoPayz</h2>
  <ol>
    <li><strong>Complete KYC on 1win.</strong> Upload a photo ID before requesting withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose EcoPayz.</strong></li>
    <li><strong>Enter your EcoPayz account email and withdrawal amount.</strong> Verify the email address carefully.</li>
    <li><strong>Submit.</strong> 1win processes the withdrawal in 15 minutes to 3 hours. Once credited to EcoPayz, the balance is available immediately.</li>
    <li><strong>Access funds.</strong> From EcoPayz, transfer to your bank, or use the EcoCard Mastercard prepaid card for immediate spending.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>EcoPayz has tiered account levels (EcoAccount, Silver, Gold, Platinum, VIP) with increasing limits. A standard EcoAccount allows monthly incoming transfers up to EUR 10,000. Gold and above accounts have significantly higher limits. Upgrade by submitting additional identity verification documents through the EcoPayz portal.</p>
  <p>EcoPayz is FCA-regulated in the UK and PCI DSS Level 1 certified. All transactions are encrypted and protected. The EcoCard (optional, order through your EcoPayz account) is a Mastercard prepaid card that lets you spend EcoPayz funds in stores or online without additional transfers.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>EcoPayz is available in 160+ countries and 45 currencies. It is particularly popular in Europe, Asia, and Latin America. Players in the UK, Germany, France, Spain, and eastern European countries will find EcoPayz easy to fund via local bank transfer. Check ecopayz.com for specific country and currency support.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/skrill.html">Skrill</a> - large global e-wallet alternative</li>
    <li><a href="/en/payments/neteller.html">Neteller</a> - Paysafe e-wallet, Net+ card available</li>
    <li><a href="/en/payments/muchbetter.html">MuchBetter</a> - mobile-first e-wallet</li>
    <li><a href="/en/payments/visa.html">Visa</a> - direct card deposit</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no e-wallet needed</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: EcoPayz at 1win</h2>
  <details><summary>What is EcoPayz and how does it work at 1win?</summary><p>EcoPayz (now branded as EcoPayz by MIR) is a UK-regulated e-wallet accepted at 1win. Fund your EcoPayz account from a bank or card, then transfer to 1win instantly. Withdrawals from 1win go back to your EcoPayz balance.</p></details>
  <details><summary>What is the minimum EcoPayz deposit at 1win?</summary><p>Minimum EcoPayz deposit at 1win is $10 USD or EUR equivalent.</p></details>
  <details><summary>How do I fund my EcoPayz account to use at 1win?</summary><p>Fund EcoPayz via bank transfer, Visa, Mastercard, or local payment options depending on your country. Once funded, depositing to 1win from EcoPayz is instant.</p></details>
  <details><summary>Does EcoPayz have a prepaid card I can use with my 1win winnings?</summary><p>Yes. EcoPayz issues an EcoCard Mastercard prepaid card linked to your EcoPayz balance. Withdraw winnings from 1win to EcoPayz, then spend via the EcoCard.</p></details>
  <details><summary>Is EcoPayz available worldwide for 1win deposits?</summary><p>EcoPayz is available in 160+ countries. Some high-risk jurisdictions may be restricted. Check ecopayz.com for the full supported country list.</p></details>
</section>
"""
    html = render_page(
        slug='payments/ecopayz',
        title='EcoPayz at 1win: deposit, withdraw, claim XLBONUS',
        description='Use EcoPayz e-wallet at 1win for instant deposits. USD, EUR, GBP supported. EcoCard for spending winnings. Register with XLBONUS. Curacao 8048/JAZ licensed.',
        h1='EcoPayz at 1win: deposit and withdrawal guide',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('EcoPayz', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/ecopayz.html','w').write(html)

# ── MuchBetter ────────────────────────────────────────────────────────────────
def make_muchbetter():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is MuchBetter and is it available at 1win?","acceptedAnswer":{"@type":"Answer","text":"MuchBetter is a mobile-first e-wallet designed specifically for the iGaming sector. It is accepted at 1win for instant deposits and withdrawals and is known for its streamlined app-based flow and contactless wristband/keyfob payment accessories."}},
    {"@type":"Question","name":"What is the minimum MuchBetter deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum MuchBetter deposit at 1win is $10 USD or EUR equivalent."}},
    {"@type":"Question","name":"Does MuchBetter offer withdrawals from 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. MuchBetter withdrawals from 1win take 15 minutes to 3 hours. Once credited to MuchBetter, you can transfer to a bank, card, or use the MuchBetter wristband/keyfob."}},
    {"@type":"Question","name":"How does the MuchBetter app deposit flow work at 1win?","acceptedAnswer":{"@type":"Answer","text":"In the 1win cashier, select MuchBetter and enter your registered mobile number. MuchBetter sends a push notification to your app. Approve it in the app with biometrics or PIN. Deposit credited instantly."}},
    {"@type":"Question","name":"Is MuchBetter available in my country for 1win deposits?","acceptedAnswer":{"@type":"Answer","text":"MuchBetter is available in 80+ countries. It is particularly strong in Europe. Check muchbetter.com for the supported country list."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>MuchBetter is a mobile-first e-wallet built specifically for iGaming, and it is accepted at 1win for fast deposits and withdrawals. 1win holds a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. MuchBetter's push-notification-based approval flow (no password entry on every transaction) and optional wristband payment accessory make it one of the most seamless e-wallet experiences available. Use promo code <span class="code-highlight">XLBONUS</span> at registration to get the welcome bonus on your first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: MuchBetter at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or EUR equivalent)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 30 seconds with push notification approval)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>MuchBetter free P2P; withdrawal to bank may have a fee</td></tr>
    <tr><td>Supported currencies</td><td>USD, EUR, GBP (MuchBetter supports 15 currencies)</td></tr>
    <tr><td>Geographic availability</td><td>80+ countries</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with MuchBetter at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select MuchBetter from the payment options.</strong> Enter the deposit amount in USD or EUR.</li>
    <li><strong>Enter your MuchBetter registered phone number.</strong> This is the number linked to your MuchBetter account.</li>
    <li><strong>Approve the push notification.</strong> Your MuchBetter app receives a push notification with the transaction details. Open the app and approve using your biometrics (fingerprint, face ID) or PIN. No browser redirect needed.</li>
    <li><strong>Check your 1win wallet.</strong> Funds credit within 30 seconds of approval. This is one of the fastest deposit flows available at 1win.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to MuchBetter</h2>
  <ol>
    <li><strong>Complete KYC on 1win.</strong> Submit a photo ID before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose MuchBetter.</strong></li>
    <li><strong>Enter your MuchBetter registered phone number and withdrawal amount.</strong></li>
    <li><strong>Confirm and submit.</strong> 1win processes the withdrawal in 15 minutes to 3 hours. MuchBetter credits the amount to your wallet balance. An in-app notification confirms receipt.</li>
    <li><strong>Access your funds from MuchBetter.</strong> Transfer to a bank account, linked card, or use the MuchBetter wristband or keyfob for contactless payment at participating merchants.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>MuchBetter account limits depend on your KYC verification level. Standard accounts allow monthly transactions up to EUR 2,500. Verified accounts (with submitted ID and proof of address) have higher limits, typically up to EUR 20,000 per month. Submit verification documents through the MuchBetter app to unlock higher limits.</p>
  <p>MuchBetter's push notification approval system means no typing passwords or going through bank security steps for each deposit. The average time from clicking "Pay" on 1win to funds appearing in your wallet is under 30 seconds, which is faster than most other e-wallet flows.</p>
  <p>MuchBetter also rewards loyal users through its in-app rewards programme, giving cashback on transaction volume. This compounds positively for active 1win depositors using MuchBetter regularly.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>MuchBetter is available in 80+ countries, primarily in Europe (UK, Germany, Nordics, eastern Europe) and selected markets in Asia and Latin America. It supports 15 currencies. The app is available on iOS and Android. MuchBetter holds an FCA e-money institution licence in the UK.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/skrill.html">Skrill</a> - large global e-wallet</li>
    <li><a href="/en/payments/neteller.html">Neteller</a> - Net+ card access for winnings</li>
    <li><a href="/en/payments/ecopayz.html">EcoPayz</a> - European-regulated e-wallet with EcoCard</li>
    <li><a href="/en/payments/visa.html">Visa</a> - direct card without a wallet account</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - crypto stablecoin alternative</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: MuchBetter at 1win</h2>
  <details><summary>What is MuchBetter and is it available at 1win?</summary><p>MuchBetter is a mobile-first e-wallet designed specifically for the iGaming sector. It is accepted at 1win for instant deposits and withdrawals and is known for its streamlined app-based flow and contactless wristband/keyfob payment accessories.</p></details>
  <details><summary>What is the minimum MuchBetter deposit at 1win?</summary><p>Minimum MuchBetter deposit at 1win is $10 USD or EUR equivalent.</p></details>
  <details><summary>Does MuchBetter offer withdrawals from 1win?</summary><p>Yes. MuchBetter withdrawals from 1win take 15 minutes to 3 hours. Once credited to MuchBetter, you can transfer to a bank, card, or use the MuchBetter wristband/keyfob.</p></details>
  <details><summary>How does the MuchBetter app deposit flow work at 1win?</summary><p>In the 1win cashier, select MuchBetter and enter your registered mobile number. MuchBetter sends a push notification to your app. Approve it in the app with biometrics or PIN. Deposit credited instantly.</p></details>
  <details><summary>Is MuchBetter available in my country for 1win deposits?</summary><p>MuchBetter is available in 80+ countries. It is particularly strong in Europe. Check muchbetter.com for the supported country list.</p></details>
</section>
"""
    html = render_page(
        slug='payments/muchbetter',
        title='MuchBetter at 1win: deposit, withdraw, claim XLBONUS',
        description='Use MuchBetter e-wallet at 1win for instant push-notification deposits. USD, EUR, GBP. Min $10. Register with promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='MuchBetter at 1win: deposit and withdrawal guide',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('MuchBetter', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/muchbetter.html','w').write(html)

# ── Visa ──────────────────────────────────────────────────────────────────────
def make_visa():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What types of Visa cards are accepted at 1win?","acceptedAnswer":{"@type":"Answer","text":"1win accepts Visa debit, Visa credit, and Visa prepaid cards. The card must have online transactions enabled and sufficient available credit or balance."}},
    {"@type":"Question","name":"Why was my Visa card declined at 1win?","acceptedAnswer":{"@type":"Answer","text":"Common reasons: your bank blocks gaming merchant category code (MCC 7995), your card's online transaction limit is exceeded, 3D Secure OTP failed, or the card issuer requires manual approval for international transactions. Try a different card, use UPI (India) or crypto as alternatives."}},
    {"@type":"Question","name":"Can I withdraw to my Visa card from 1win?","acceptedAnswer":{"@type":"Answer","text":"Visa card withdrawals are available at some 1win accounts but not universally. Check the cashier withdrawal section for card withdrawal availability. If not available, withdraw via bank transfer or e-wallet instead."}},
    {"@type":"Question","name":"What is the minimum Visa card deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Visa card deposit at 1win is $10 USD (or local currency equivalent)."}},
    {"@type":"Question","name":"Indian Visa cards are being declined at 1win. What should I do?","acceptedAnswer":{"@type":"Answer","text":"Some Indian banks block transactions to international gaming merchants. Use UPI, IMPS, or crypto (Bitcoin, USDT TRC20) as reliable alternatives that bypass this MCC restriction."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Visa cards are one of the most universally available payment methods at 1win, the Curaçao 8048/JAZ-licensed platform used by 400,000+ players globally. Both Visa debit and Visa credit cards are accepted for deposits in USD, EUR, and dozens of other currencies. Players from India, Brazil, Africa, and Europe can all use their Visa card, though some regional banks may block gaming transactions. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Visa card at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Varies by account; check cashier</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or local currency equivalent)</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>Your card's daily online transaction limit</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>3 to 5 business days (card refund timeline)</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Foreign transaction fee may apply from your bank for non-USD cards</td></tr>
    <tr><td>Supported currencies</td><td>USD, EUR, GBP, INR, BRL and 150+ Visa currencies</td></tr>
    <tr><td>Geographic availability</td><td>200+ countries (Visa's global network)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with a Visa card at 1win</h2>
  <ol>
    <li><strong>Enable online transactions on your card.</strong> Before attempting a card deposit, confirm in your bank's app that online/international transactions are enabled. Set your daily online limit to cover the intended deposit amount.</li>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Visa (or Card) from the payment options.</strong> Enter the deposit amount and click Proceed.</li>
    <li><strong>Enter your Visa card details.</strong> Card number (16 digits), expiry month/year, CVV (3-digit code on the back). Name on card as printed.</li>
    <li><strong>Complete 3D Secure verification.</strong> Your bank sends an OTP to your registered mobile number. Enter the OTP within the time limit (typically 3 minutes). The transaction is approved, and your 1win wallet updates within 5 minutes.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw to a Visa card from 1win</h2>
  <ol>
    <li><strong>Complete KYC verification.</strong> Submit a photo ID and proof that the card belongs to you (a photo of the card with the middle 8 digits obscured).</li>
    <li><strong>Open the Cashier and select Withdrawal. Check if card withdrawal is available.</strong></li>
    <li><strong>If available, select Visa.</strong> Enter the card number and the withdrawal amount.</li>
    <li><strong>Submit.</strong> Card refunds typically take 3 to 5 business days to appear in your bank statement. This is a Visa network timeline, not a 1win delay.</li>
    <li><strong>If card withdrawal is not available,</strong> use an e-wallet or bank transfer as the withdrawal method instead.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Visa card limits at 1win are controlled by your issuing bank, not 1win. Check your bank's online transaction daily limit in your banking app. Standard Visa debit cards typically allow $1,000 to $5,000 USD per day online; Visa credit cards may have higher limits depending on your credit limit.</p>
  <p>Note for Indian players: Some Indian banks block gaming merchant category code (MCC 7995) transactions on Visa cards. If your Visa card is declined, use UPI, IMPS, or crypto (Bitcoin, USDT TRC20) as alternatives that bypass MCC restrictions entirely. These options are unaffected by bank MCC filtering.</p>
  <p>3D Secure is mandatory for all Visa card transactions at 1win. Ensure your bank has your current mobile number registered to receive OTP. If your OTP does not arrive within 60 seconds, request a resend or contact your bank.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Visa cards are accepted in 200+ countries at 1win. The transaction currency may be USD or the local currency depending on 1win's gateway configuration for your country. If your card currency differs from the transaction currency, your bank applies a foreign exchange conversion rate plus any applicable foreign transaction fee (typically 1.5% to 3%).</p>
  <p>Visa cards from all major issuers are accepted: Barclays, HSBC, Citibank, HDFC, SBI, Itau, Standard Chartered, and thousands of others worldwide.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/mastercard.html">Mastercard</a> - alternative card network</li>
    <li><a href="/en/payments/upi.html">UPI</a> - bypass Indian bank MCC blocks for INR deposits</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - e-wallet: fund with card, then deposit without card data at 1win</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no MCC restrictions</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin alternative</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Visa cards at 1win</h2>
  <details><summary>What types of Visa cards are accepted at 1win?</summary><p>1win accepts Visa debit, Visa credit, and Visa prepaid cards. The card must have online transactions enabled and sufficient available credit or balance.</p></details>
  <details><summary>Why was my Visa card declined at 1win?</summary><p>Common reasons: your bank blocks gaming merchant category code (MCC 7995), your card's online transaction limit is exceeded, 3D Secure OTP failed, or the card issuer requires manual approval for international transactions. Try a different card, use UPI (India) or crypto as alternatives.</p></details>
  <details><summary>Can I withdraw to my Visa card from 1win?</summary><p>Visa card withdrawals are available at some 1win accounts but not universally. Check the cashier withdrawal section for card withdrawal availability. If not available, withdraw via bank transfer or e-wallet instead.</p></details>
  <details><summary>What is the minimum Visa card deposit at 1win?</summary><p>Minimum Visa card deposit at 1win is $10 USD (or local currency equivalent).</p></details>
  <details><summary>Indian Visa cards are being declined at 1win. What should I do?</summary><p>Some Indian banks block transactions to international gaming merchants. Use UPI, IMPS, or crypto (Bitcoin, USDT TRC20) as reliable alternatives that bypass this MCC restriction.</p></details>
</section>
"""
    html = render_page(
        slug='payments/visa',
        title='Visa card deposits at 1win and the XLBONUS bonus',
        description='Deposit at 1win with your Visa debit or credit card. Instant, USD/EUR/INR/BRL supported. Use promo code XLBONUS. Curacao 8048/JAZ licensed. Min $10.',
        h1='Visa card deposits at 1win',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Visa', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/visa.html','w').write(html)

# ── Mastercard ────────────────────────────────────────────────────────────────
def make_mastercard():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Does 1win accept Mastercard debit and credit cards?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win accepts Mastercard debit, credit, and prepaid cards. Online transactions must be enabled on your card before depositing."}},
    {"@type":"Question","name":"What is the minimum Mastercard deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Mastercard deposit at 1win is $10 USD or local currency equivalent."}},
    {"@type":"Question","name":"My Mastercard was declined at 1win. Why?","acceptedAnswer":{"@type":"Answer","text":"Common reasons: gaming MCC block by your bank, exceeded daily limit, failed 3D Secure OTP, or international transaction restriction. Enable international transactions in your banking app and retry. If declined again, use crypto or an e-wallet."}},
    {"@type":"Question","name":"Can I withdraw from 1win to my Mastercard?","acceptedAnswer":{"@type":"Answer","text":"Card withdrawals to Mastercard may be available; check the cashier. If not, use bank transfer or an e-wallet for withdrawals."}},
    {"@type":"Question","name":"Does 1win charge extra for Mastercard deposits?","acceptedAnswer":{"@type":"Answer","text":"1win does not charge any fee for Mastercard deposits. Your bank may charge a foreign transaction fee if the deposit currency differs from your card currency."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Mastercard is a globally accepted card network at 1win, with Mastercard debit, credit, and prepaid cards all supported for deposits. 1win holds a Curaçao 8048/JAZ licence and has grown to serve 400,000+ players worldwide. Deposits are instant upon 3D Secure approval, and the card is accepted from players in India, Europe, Brazil, Africa, and beyond. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to claim the welcome bonus on your first Mastercard deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Mastercard at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Varies by account; check cashier</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or local currency equivalent)</td></tr>
    <tr><td>Maximum deposit</td><td>Your card's daily online transaction limit</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>3 to 5 business days (card refund)</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Foreign transaction fee from your bank may apply</td></tr>
    <tr><td>Supported currencies</td><td>USD, EUR, GBP, INR, BRL and 150+ Mastercard currencies</td></tr>
    <tr><td>Geographic availability</td><td>200+ countries</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Mastercard at 1win</h2>
  <ol>
    <li><strong>Enable online/international transactions.</strong> Open your bank app and confirm your Mastercard has online e-commerce and international transactions enabled. Set an appropriate daily limit.</li>
    <li><strong>Log in to 1win and open the Cashier.</strong> Register if new; enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Mastercard (or Card) from payment options.</strong> Enter the deposit amount.</li>
    <li><strong>Enter card details.</strong> 16-digit card number, expiry date, CVV (3 digits on back), and cardholder name as printed.</li>
    <li><strong>Complete 3D Secure (Mastercard Identity Check).</strong> An OTP or push notification from your bank arrives. Approve within the time limit. Your 1win wallet updates within 5 minutes.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw to Mastercard from 1win</h2>
  <ol>
    <li><strong>Complete KYC.</strong> Submit photo ID and card ownership proof before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal.</strong> Check whether card withdrawal is listed.</li>
    <li><strong>If available, select Mastercard.</strong> Enter card number and withdrawal amount. Submit.</li>
    <li><strong>Await the refund.</strong> Card withdrawals take 3 to 5 business days to appear due to Mastercard's refund processing timeline. This is not a 1win delay.</li>
    <li><strong>If card withdrawal is not listed,</strong> use a bank transfer or e-wallet option in the cashier instead.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Mastercard deposit limits at 1win are determined by your issuing bank. Most banks set daily online purchase limits between $1,000 and $5,000 USD for standard cards; premium and infinite cards may have higher limits. Check your bank app under "Card Limits" or call your bank to confirm.</p>
  <p>For Indian players: Indian banks often apply gaming MCC (7995) blocks to both Visa and Mastercard. If your Mastercard is declined, UPI is the most reliable alternative for INR deposits. Crypto (Bitcoin, USDT TRC20) works without any MCC classification and is available regardless of which bank issued your card.</p>
  <p>3D Secure (Mastercard Identity Check) is required for all Mastercard transactions at 1win. This is a security layer that protects your card from unauthorized use. Ensure your bank has your current phone number for OTP delivery.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Mastercard is accepted in 200+ countries at 1win. The transaction may be processed in USD or local currency depending on 1win's gateway configuration. Foreign transaction fees from your bank (typically 1.5% to 3%) apply if your card currency and the transaction currency differ. Mastercard cards from Citibank, HSBC, Chase, HDFC, Itau, Standard Chartered, and thousands of other issuers are accepted.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/visa.html">Visa</a> - alternative card network</li>
    <li><a href="/en/payments/maestro.html">Maestro</a> - Mastercard's debit card variant</li>
    <li><a href="/en/payments/upi.html">UPI</a> - bypass Indian MCC blocks for INR</li>
    <li><a href="/en/payments/neteller.html">Neteller</a> - e-wallet, fund with card without sharing card at 1win</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no MCC restrictions</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Mastercard at 1win</h2>
  <details><summary>Does 1win accept Mastercard debit and credit cards?</summary><p>Yes. 1win accepts Mastercard debit, credit, and prepaid cards. Online transactions must be enabled on your card before depositing.</p></details>
  <details><summary>What is the minimum Mastercard deposit at 1win?</summary><p>Minimum Mastercard deposit at 1win is $10 USD or local currency equivalent.</p></details>
  <details><summary>My Mastercard was declined at 1win. Why?</summary><p>Common reasons: gaming MCC block by your bank, exceeded daily limit, failed 3D Secure OTP, or international transaction restriction. Enable international transactions in your banking app and retry. If declined again, use crypto or an e-wallet.</p></details>
  <details><summary>Can I withdraw from 1win to my Mastercard?</summary><p>Card withdrawals to Mastercard may be available; check the cashier. If not, use bank transfer or an e-wallet for withdrawals.</p></details>
  <details><summary>Does 1win charge extra for Mastercard deposits?</summary><p>1win does not charge any fee for Mastercard deposits. Your bank may charge a foreign transaction fee if the deposit currency differs from your card currency.</p></details>
</section>
"""
    html = render_page(
        slug='payments/mastercard',
        title='Mastercard deposits at 1win and the XLBONUS bonus',
        description='Deposit at 1win with your Mastercard debit or credit card. Instant, global, min $10. Use promo code XLBONUS at registration. Curacao 8048/JAZ licensed.',
        h1='Mastercard deposits at 1win',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Mastercard', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/mastercard.html','w').write(html)

# ── Maestro ───────────────────────────────────────────────────────────────────
def make_maestro():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Is Maestro still accepted at 1win in 2024?","acceptedAnswer":{"@type":"Answer","text":"Maestro card acceptance depends on the payment processor. As Mastercard has phased out new Maestro issuance in some markets, check the 1win cashier for current Maestro availability. If not listed separately, your Maestro card may work under the general Mastercard option."}},
    {"@type":"Question","name":"What is the minimum Maestro deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Maestro deposit at 1win is $10 USD or local currency equivalent."}},
    {"@type":"Question","name":"Can I withdraw from 1win to a Maestro card?","acceptedAnswer":{"@type":"Answer","text":"Maestro is typically debit-only and may not support card-back refunds depending on your bank. If card withdrawal fails, use bank transfer or e-wallet as the withdrawal method."}},
    {"@type":"Question","name":"My Maestro card has no CVV. Can I still deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Some Maestro cards do not have a CVV. In this case, the deposit form may accept '000' or leave CVV blank, depending on the gateway. Contact 1win live-chat for guidance if the form requires a CVV your card does not have."}},
    {"@type":"Question","name":"Maestro was declined. What alternatives do I have?","acceptedAnswer":{"@type":"Answer","text":"Use a Visa or Mastercard credit/debit card, an e-wallet (Skrill, Neteller, EcoPayz), or crypto (Bitcoin, USDT TRC20) as alternatives at 1win."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Maestro, Mastercard's debit card brand, is accepted at 1win as an INR and EUR deposit option for eligible cardholders. 1win operates under a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. Note that Mastercard began phasing out new Maestro issuance in many European markets from 2023; if you hold an existing Maestro card, it may still be accepted at 1win through the Mastercard gateway. Enter promo code <span class="code-highlight">XLBONUS</span> at registration for the welcome bonus on your first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Maestro at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes (where Maestro is accepted by the gateway)</td></tr>
    <tr><td>Available for withdrawal</td><td>Limited (debit card; bank transfer preferred for withdrawals)</td></tr>
    <tr><td>Minimum deposit</td><td>$10 USD (or local currency equivalent)</td></tr>
    <tr><td>Maximum deposit</td><td>Your card's daily debit transaction limit</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>Via bank transfer: 1 to 5 business days</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Bank may charge foreign transaction fee</td></tr>
    <tr><td>Supported currencies</td><td>EUR, GBP, INR and other Maestro-enabled currencies</td></tr>
    <tr><td>Geographic availability</td><td>Europe and select markets where Maestro is still issued</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Maestro at 1win</h2>
  <ol>
    <li><strong>Check your card.</strong> Confirm your card shows the Maestro logo on the front or back. Note whether your Maestro card has a CVV (some older Maestro cards do not).</li>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Maestro or Mastercard/Debit Card.</strong> Some gateways list Maestro separately; others route it through Mastercard.</li>
    <li><strong>Enter your card details.</strong> Card number (typically 13 to 19 digits on Maestro), expiry date, CVV if your card has one, and cardholder name.</li>
    <li><strong>Complete 3D Secure.</strong> Maestro cards use Mastercard Identity Check (3DS2). Approve the OTP or push notification from your bank. Your 1win wallet updates within 5 minutes upon approval.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw if you deposited via Maestro at 1win</h2>
  <ol>
    <li><strong>Complete KYC verification on 1win.</strong> Submit a photo ID before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal.</strong> If Maestro/card withdrawal is not available, use bank transfer (NEFT, IMPS for India; SEPA for Europe) or an e-wallet.</li>
    <li><strong>For bank transfer:</strong> Enter your account number, IFSC/IBAN, and account holder name matching your bank records.</li>
    <li><strong>Enter withdrawal amount and submit.</strong></li>
    <li><strong>Await settlement.</strong> Bank transfers take 1 to 5 business days depending on the destination country and bank processing speed.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Maestro is a debit card, which means transactions debit directly from your bank account. Daily debit limits are set by your bank, typically in the range of EUR 1,000 to EUR 5,000 per day for online transactions. Some banks have lower online Maestro limits than general debit limits; check with your bank.</p>
  <p>Maestro card issuance was discontinued for new cards in many European markets from 2023 as Mastercard transitioned to Debit Mastercard. However, existing Maestro cards remain valid until their expiry date. If your Maestro card is nearing expiry, contact your bank for a replacement Debit Mastercard.</p>
  <p>For Indian players holding Maestro-branded cards: Indian bank MCC blocks apply to Maestro cards the same way as Visa and Mastercard. If declined for gaming reasons, use UPI, IMPS, or crypto instead.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Maestro cards are primarily issued in Europe (Germany, Italy, Netherlands, Belgium, Austria, and eastern European countries) and a few other markets. UK banks have largely replaced Maestro with Debit Mastercard. Indian banks issue Maestro-branded RuPay cards but these operate on RuPay's domestic network. 1win accepts Maestro where supported by its payment gateway; if not listed in the cashier, use Mastercard or Visa.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/mastercard.html">Mastercard</a> - Debit Mastercard as Maestro replacement</li>
    <li><a href="/en/payments/visa.html">Visa</a> - alternative card network</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - e-wallet, fund with any card</li>
    <li><a href="/en/payments/neteller.html">Neteller</a> - e-wallet alternative with Net+ card</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no card infrastructure needed</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Maestro card at 1win</h2>
  <details><summary>Is Maestro still accepted at 1win in 2024?</summary><p>Maestro card acceptance depends on the payment processor. As Mastercard has phased out new Maestro issuance in some markets, check the 1win cashier for current Maestro availability. If not listed separately, your Maestro card may work under the general Mastercard option.</p></details>
  <details><summary>What is the minimum Maestro deposit at 1win?</summary><p>Minimum Maestro deposit at 1win is $10 USD or local currency equivalent.</p></details>
  <details><summary>Can I withdraw from 1win to a Maestro card?</summary><p>Maestro is typically debit-only and may not support card-back refunds depending on your bank. If card withdrawal fails, use bank transfer or e-wallet as the withdrawal method.</p></details>
  <details><summary>My Maestro card has no CVV. Can I still deposit at 1win?</summary><p>Some Maestro cards do not have a CVV. In this case, the deposit form may accept '000' or leave CVV blank, depending on the gateway. Contact 1win live-chat for guidance if the form requires a CVV your card does not have.</p></details>
  <details><summary>Maestro was declined. What alternatives do I have?</summary><p>Use a Visa or Mastercard credit/debit card, an e-wallet (Skrill, Neteller, EcoPayz), or crypto (Bitcoin, USDT TRC20) as alternatives at 1win.</p></details>
</section>
"""
    html = render_page(
        slug='payments/maestro',
        title='Maestro card deposits at 1win and the XLBONUS bonus',
        description='Deposit at 1win with your Maestro debit card. Min $10, no 1win fees. Use promo code XLBONUS. Note: Mastercard phasing out Maestro in some markets. Curacao 8048/JAZ.',
        h1='Maestro card deposits at 1win',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Maestro', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/maestro.html','w').write(html)


if __name__ == '__main__':
    make_skrill()
    make_neteller()
    make_ecopayz()
    make_muchbetter()
    make_visa()
    make_mastercard()
    make_maestro()
    print("E-wallet + Card pages done: 7 files")
