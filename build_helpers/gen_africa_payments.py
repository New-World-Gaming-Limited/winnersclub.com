"""
Generate Africa payment method pages for 1win.codes
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_helpers.page_template import render_page

os.makedirs('en/payments', exist_ok=True)

# ── M-Pesa ────────────────────────────────────────────────────────────────────
def make_mpesa():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Which countries can use M-Pesa at 1win?","acceptedAnswer":{"@type":"Answer","text":"M-Pesa at 1win primarily covers Kenya and Tanzania. Players in both countries can deposit and withdraw using their Safaricom (Kenya) or Vodacom Tanzania M-Pesa accounts."}},
    {"@type":"Question","name":"What is the minimum M-Pesa deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum M-Pesa deposit is KSh 100 for Kenyan players or TSh 1,000 for Tanzanian players."}},
    {"@type":"Question","name":"How long does an M-Pesa deposit take at 1win?","acceptedAnswer":{"@type":"Answer","text":"M-Pesa deposits are processed in real time. Your 1win balance updates within 2 minutes of completing the STK push or send money flow on your phone."}},
    {"@type":"Question","name":"I entered the wrong phone number for an M-Pesa withdrawal. What do I do?","acceptedAnswer":{"@type":"Answer","text":"Contact 1win live-chat immediately before the transfer is dispatched. Once sent, M-Pesa transfers to incorrect numbers cannot be reversed by 1win. Contact M-Pesa customer service directly for reversals."}},
    {"@type":"Question","name":"Are there daily M-Pesa limits that affect 1win deposits?","acceptedAnswer":{"@type":"Answer","text":"Yes. Safaricom M-Pesa Kenya daily limits are KSh 300,000 for sends per day, with a per-transaction cap of KSh 250,000. Vodacom Tanzania M-Pesa limits differ; check your account tier."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>M-Pesa is accepted at 1win for deposits and withdrawals in KSh (Kenyan Shillings) and TSh (Tanzanian Shillings), giving East African players a fast, familiar mobile money route into the Curaçao 8048/JAZ-licensed platform used by 400,000+ players worldwide. Both Safaricom Kenya and Vodacom Tanzania M-Pesa accounts work. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to get your welcome bonus on the first M-Pesa deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: M-Pesa at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit (Kenya)</td><td>KSh 100</td></tr>
    <tr><td>Minimum deposit (Tanzania)</td><td>TSh 1,000</td></tr>
    <tr><td>Maximum per transaction (Kenya)</td><td>KSh 250,000</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 2 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>5 minutes to 2 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Safaricom/Vodacom standard M-Pesa send fees apply</td></tr>
    <tr><td>Supported currencies</td><td>KSh (Kenya), TSh (Tanzania)</td></tr>
    <tr><td>Geographic availability</td><td>Kenya, Tanzania</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit at 1win with M-Pesa</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> If you are a new user, register and enter promo code <span class="code-highlight">XLBONUS</span> to activate the welcome bonus.</li>
    <li><strong>Select M-Pesa from the payment method list.</strong> Enter the deposit amount in KSh or TSh (minimum KSh 100 / TSh 1,000).</li>
    <li><strong>Note the 1win M-Pesa paybill number or till number shown on screen.</strong> For Kenya, this is typically a Safaricom paybill. For Tanzania, a Vodacom business number.</li>
    <li><strong>Trigger the M-Pesa STK push.</strong> On Safaricom Kenya: go to M-Pesa, select "Lipa na M-Pesa," then "Pay Bill." Enter the paybill number, account number (your 1win user ID), and amount. Enter your M-Pesa PIN. On Vodacom Tanzania: go to M-Pesa, "Pay via M-Pesa," enter the business number and amount.</li>
    <li><strong>Confirm the SMS from M-Pesa.</strong> Safaricom sends a green SMS confirming the transaction. Your 1win balance updates within 2 minutes. If not updated in 5 minutes, contact live-chat with the M-Pesa transaction code.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to M-Pesa</h2>
  <ol>
    <li><strong>Complete identity verification.</strong> Submit your national ID (Kenya: Kenyan National ID or Passport; Tanzania: NIDA or Passport) in your 1win profile.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose M-Pesa.</strong></li>
    <li><strong>Enter your M-Pesa registered phone number.</strong> Format: 07XX-XXXXXX (Kenya) or 07XX-XXXXXX (Tanzania). Verify the number before submitting.</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm the recipient number and name on the summary screen.</li>
    <li><strong>Submit.</strong> 1win dispatches the M-Pesa transfer within 5 minutes to 2 hours. A Safaricom or Vodacom SMS confirms credit to your M-Pesa account.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Safaricom Kenya M-Pesa limits (2024): per-transaction send limit KSh 250,000, daily send limit KSh 300,000, maximum wallet balance KSh 300,000. These limits apply regardless of whether you are paying a paybill or sending to another number.</p>
  <p>Vodacom Tanzania M-Pesa limits vary by SIM registration tier. Basic tier allows TSh 5,000,000 per transaction; enhanced tier (biometric) allows TSh 10,000,000. Check your tier in the M-Pesa menu under "My Account."</p>
  <p>M-Pesa is available 24/7 in Kenya and Tanzania. Deposits process in real time. Withdrawals from 1win dispatch within the hour during business hours; overnight requests may queue until morning processing resumes.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>M-Pesa at 1win covers Kenya (Safaricom M-Pesa, currency KSh) and Tanzania (Vodacom Tanzania M-Pesa, currency TSh). M-Pesa also operates in several other African countries (Ghana, Lesotho, Democratic Republic of Congo, Mozambique, Egypt) but 1win's M-Pesa integration may not cover all countries; check the cashier for your country.</p>
  <p>Kenya's M-Pesa is the world's oldest and most-developed mobile money system, launched by Safaricom in 2007. It processes over 61 billion USD annually and is used by approximately 96% of Kenyan households as of 2024.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/airtel-money.html">Airtel Money</a> - available in Kenya and many other African countries</li>
    <li><a href="/en/payments/flutterwave.html">Flutterwave</a> - multi-method African payments aggregator</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto alternative, no mobile money account needed</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, low-cost cross-border option</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - e-wallet supporting USD/EUR</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: M-Pesa at 1win</h2>
  <details><summary>Which countries can use M-Pesa at 1win?</summary><p>M-Pesa at 1win primarily covers Kenya and Tanzania. Players in both countries can deposit and withdraw using their Safaricom (Kenya) or Vodacom Tanzania M-Pesa accounts.</p></details>
  <details><summary>What is the minimum M-Pesa deposit at 1win?</summary><p>Minimum M-Pesa deposit is KSh 100 for Kenyan players or TSh 1,000 for Tanzanian players.</p></details>
  <details><summary>How long does an M-Pesa deposit take at 1win?</summary><p>M-Pesa deposits are processed in real time. Your 1win balance updates within 2 minutes of completing the STK push or send money flow on your phone.</p></details>
  <details><summary>I entered the wrong phone number for an M-Pesa withdrawal. What do I do?</summary><p>Contact 1win live-chat immediately before the transfer is dispatched. Once sent, M-Pesa transfers to incorrect numbers cannot be reversed by 1win. Contact M-Pesa customer service directly for reversals.</p></details>
  <details><summary>Are there daily M-Pesa limits that affect 1win deposits?</summary><p>Yes. Safaricom M-Pesa Kenya daily limits are KSh 300,000 for sends per day, with a per-transaction cap of KSh 250,000. Vodacom Tanzania M-Pesa limits differ; check your account tier.</p></details>
</section>
"""
    html = render_page(
        slug='payments/mpesa',
        title='M-Pesa deposit at 1win for Kenya and Tanzania players',
        description='Deposit and withdraw KSh or TSh at 1win using M-Pesa. Instant mobile money, min KSh 100, no 1win fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='M-Pesa deposit at 1win for East African players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('M-Pesa', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/mpesa.html','w').write(html)

# ── Airtel Money ──────────────────────────────────────────────────────────────
def make_airtel_money():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Which African countries can use Airtel Money at 1win?","acceptedAnswer":{"@type":"Answer","text":"Airtel Money at 1win covers Kenya, Uganda, Tanzania, Zambia, Rwanda, Malawi, Madagascar, Niger, Chad, Gabon, Congo, and several other countries where Airtel operates. Check the 1win cashier for your specific country."}},
    {"@type":"Question","name":"What currency does 1win use for Airtel Money?","acceptedAnswer":{"@type":"Answer","text":"1win processes Airtel Money transactions in the local currency of the player's country. Kenyan players use KSh, Ugandan players use UGX, Zambian players use ZMW, etc."}},
    {"@type":"Question","name":"How do I send money to 1win via Airtel Money?","acceptedAnswer":{"@type":"Answer","text":"Use the Airtel Money app or USSD (*185#), select Pay Bill or Merchant Payment, enter the 1win merchant code and amount. Confirm with your Airtel Money PIN."}},
    {"@type":"Question","name":"What is the minimum Airtel Money deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum varies by country. For Kenya: KSh 100. For Uganda: UGX 2,000. Check the cashier for your country's minimum."}},
    {"@type":"Question","name":"Airtel Money withdrawal from 1win failed. What should I do?","acceptedAnswer":{"@type":"Answer","text":"Check that your Airtel Money account is active and not suspended. Verify the phone number entered. If the issue persists, contact 1win live-chat with your 1win user ID and the withdrawal amount."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Airtel Money is one of Africa's largest mobile money networks, available across 14 countries on the continent. 1win accepts Airtel Money deposits and withdrawals on its Curaçao 8048/JAZ-licensed platform, giving players in Kenya, Uganda, Tanzania, Zambia, Rwanda, and other Airtel markets a local mobile money route. With 400,000+ players worldwide, 1win is a recognised destination for African sports betting and casino play. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Airtel Money at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit (Kenya)</td><td>KSh 100</td></tr>
    <tr><td>Minimum deposit (Uganda)</td><td>UGX 2,000</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>10 minutes to 2 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Airtel Money standard merchant payment fee</td></tr>
    <tr><td>Supported currencies</td><td>KSh, UGX, TSh, ZMW, RWF (varies by country)</td></tr>
    <tr><td>Geographic availability</td><td>14+ African countries where Airtel operates</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit at 1win with Airtel Money</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> Register first if you are a new user, and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Airtel Money from the payment list.</strong> Enter the deposit amount in your local currency.</li>
    <li><strong>Note the 1win Airtel Money merchant code or number.</strong> This is displayed on screen after you select Airtel Money.</li>
    <li><strong>On your phone, open the Airtel Money app or dial *185#.</strong> Navigate to "Pay Bill," "Merchant Payment," or "Send Money." Enter the 1win merchant number and the exact deposit amount. Include your 1win user ID as the reference.</li>
    <li><strong>Enter your Airtel Money PIN to confirm.</strong> You receive an SMS confirming the transaction. Your 1win balance updates within 5 minutes. Keep the Airtel Money transaction reference in case you need support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to Airtel Money</h2>
  <ol>
    <li><strong>Complete KYC on 1win.</strong> Submit your national ID before requesting a withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose Airtel Money.</strong></li>
    <li><strong>Enter your Airtel registered phone number.</strong> Confirm the number format for your country (e.g., 07XX-XXXXXX in Kenya).</li>
    <li><strong>Enter the withdrawal amount.</strong> The name linked to the Airtel Money account should match your 1win account name.</li>
    <li><strong>Submit.</strong> 1win dispatches the transfer within 10 minutes to 2 hours. An Airtel Money SMS confirms receipt.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Airtel Money limits vary significantly by country. In Kenya, Airtel Money daily limits are lower than Safaricom M-Pesa, typically KSh 150,000 per day for standard accounts. In Uganda, UGX 5,000,000 per day is the standard limit. In Zambia, ZMW 10,000 per transaction is a typical cap. Check your country's Airtel Money limit by dialling *185# and selecting "My Account."</p>
  <p>Airtel Money operates 24/7 across most African markets, though technical maintenance windows may occur between 2 AM and 4 AM local time. During these windows, deposits may take up to 15 minutes to settle instead of the usual 2 to 5 minutes.</p>
  <p>For very large deposits that exceed Airtel Money limits, use Bitcoin or USDT, which have no mobile money account restrictions.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Airtel Money operates in 14 African countries: Kenya, Uganda, Tanzania, Zambia, Rwanda, Malawi, Madagascar, Niger, Chad, Democratic Republic of Congo, Republic of Congo, Gabon, Sierra Leone, and Seychelles. Each country processes in its local currency. 1win's Airtel Money integration covers the major Airtel markets; check the cashier to confirm availability in your country.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/mpesa.html">M-Pesa</a> - Kenya and Tanzania mobile money leader</li>
    <li><a href="/en/payments/mtn-momo.html">MTN MoMo</a> - Ghana, Uganda, and other MTN markets</li>
    <li><a href="/en/payments/flutterwave.html">Flutterwave</a> - multi-method African payments</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no mobile money account needed</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, fast settlement</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Airtel Money at 1win</h2>
  <details><summary>Which African countries can use Airtel Money at 1win?</summary><p>Airtel Money at 1win covers Kenya, Uganda, Tanzania, Zambia, Rwanda, Malawi, Madagascar, Niger, Chad, Gabon, Congo, and several other countries where Airtel operates. Check the 1win cashier for your specific country.</p></details>
  <details><summary>What currency does 1win use for Airtel Money?</summary><p>1win processes Airtel Money transactions in the local currency of the player's country. Kenyan players use KSh, Ugandan players use UGX, Zambian players use ZMW, etc.</p></details>
  <details><summary>How do I send money to 1win via Airtel Money?</summary><p>Use the Airtel Money app or USSD (*185#), select Pay Bill or Merchant Payment, enter the 1win merchant code and amount. Confirm with your Airtel Money PIN.</p></details>
  <details><summary>What is the minimum Airtel Money deposit at 1win?</summary><p>Minimum varies by country. For Kenya: KSh 100. For Uganda: UGX 2,000. Check the cashier for your country's minimum.</p></details>
  <details><summary>Airtel Money withdrawal from 1win failed. What should I do?</summary><p>Check that your Airtel Money account is active and not suspended. Verify the phone number entered. If the issue persists, contact 1win live-chat with your 1win user ID and the withdrawal amount.</p></details>
</section>
"""
    html = render_page(
        slug='payments/airtel-money',
        title='Airtel Money deposit at 1win for African players',
        description='Deposit and withdraw via Airtel Money at 1win across 14 African countries. KSh, UGX, TSh supported. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Airtel Money deposit at 1win for African players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Airtel Money', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/airtel-money.html','w').write(html)

# ── MTN MoMo ──────────────────────────────────────────────────────────────────
def make_mtn_momo():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Which countries can use MTN MoMo at 1win?","acceptedAnswer":{"@type":"Answer","text":"MTN MoMo is available in Ghana (GHS), Uganda (UGX), Cameroon, Ivory Coast, Benin, Burkina Faso, Guinea, Rwanda, South Africa, Zambia, and Eswatini. Check the 1win cashier for your country's availability."}},
    {"@type":"Question","name":"What is the minimum MTN MoMo deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum MTN MoMo deposit is GHS 5 in Ghana or UGX 2,000 in Uganda. Minimums vary by country."}},
    {"@type":"Question","name":"How fast is an MTN MoMo deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"MTN MoMo deposits are processed in real time. Expect your 1win balance to update within 2 to 5 minutes after confirming the payment."}},
    {"@type":"Question","name":"Does 1win support MTN MoMo withdrawals?","acceptedAnswer":{"@type":"Answer","text":"Yes. MTN MoMo withdrawals are supported. Enter your MTN registered phone number in the withdrawal form. Processing takes 15 minutes to 3 hours."}},
    {"@type":"Question","name":"MTN MoMo payment failed but money was deducted. What happens?","acceptedAnswer":{"@type":"Answer","text":"MTN MoMo auto-reverses failed payments within 24 hours. If you do not see a reversal after 24 hours, contact MTN MoMo customer care with the transaction ID. Also contact 1win live-chat to check if the payment was received."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>MTN Mobile Money (MoMo) is one of Africa's most expansive mobile payment networks, available across 17 countries on the continent. 1win accepts MTN MoMo for deposits and withdrawals on its Curaçao 8048/JAZ-licensed platform, which has served 400,000+ players globally. Players in Ghana (GHS), Uganda (UGX), Ivory Coast, Cameroon, and other MTN markets can fund and withdraw from 1win directly through MoMo. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: MTN MoMo at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit (Ghana)</td><td>GHS 5</td></tr>
    <tr><td>Minimum deposit (Uganda)</td><td>UGX 2,000</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>MTN MoMo standard transfer fees apply</td></tr>
    <tr><td>Supported currencies</td><td>GHS, UGX, XOF, XAF (varies by country)</td></tr>
    <tr><td>Geographic availability</td><td>Ghana, Uganda, Ivory Coast, Cameroon, Benin, and 12 other MTN markets</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit at 1win with MTN MoMo</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register with promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select MTN Mobile Money from the payment list.</strong> Enter the deposit amount in your local currency.</li>
    <li><strong>Note the 1win MTN MoMo merchant number displayed on screen.</strong></li>
    <li><strong>Open the MTN MoMo app or dial *170# (Ghana) or *165# (Uganda).</strong> Select "Pay Bill," "Merchant Pay," or "Send Money." Enter the 1win merchant number, the amount, and your 1win user ID as the reference. Confirm with your MTN MoMo PIN.</li>
    <li><strong>Wait for the SMS confirmation from MTN.</strong> Your 1win balance updates within 5 minutes. Keep the MTN transaction ID for reference.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to MTN MoMo</h2>
  <ol>
    <li><strong>Complete identity verification on 1win.</strong> Submit your national ID (Ghana Card, Ugandan National ID, or equivalent) before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose MTN MoMo.</strong></li>
    <li><strong>Enter your MTN registered phone number.</strong> Verify the number format: Ghana uses 024/054/055/059-XXXXXXX; Uganda uses 077/078-XXXXXXX.</li>
    <li><strong>Enter the withdrawal amount.</strong> Verify name match between MTN MoMo account and 1win registration.</li>
    <li><strong>Submit.</strong> Funds arrive within 15 minutes to 3 hours. MTN sends an SMS confirming receipt.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>MTN MoMo limits in Ghana (2024): per transaction up to GHS 10,000, daily up to GHS 10,000, monthly up to GHS 30,000. These limits apply to standard accounts. Enhanced accounts with biometric verification may have higher limits. Check current limits by dialling *170# in Ghana.</p>
  <p>MTN MoMo limits in Uganda (2024): per transaction up to UGX 7,000,000, daily up to UGX 20,000,000 for registered accounts. Limits are set by Bank of Uganda and MTN Uganda together.</p>
  <p>MTN MoMo operates 24/7. Deposits confirm in 2 to 5 minutes. Withdrawals from 1win typically process within an hour during operational hours. An overnight batch may process requests received after 10 PM local time the following morning.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>MTN MoMo is available in 17 African countries with 238 million registered customers as of 2024. For 1win deposits, the primary supported currencies are GHS (Ghana), UGX (Uganda), and XOF/XAF (West/Central African CFA franc for Francophone markets). 1win's MoMo integration may not cover every country MTN operates in; verify your country in the cashier before depositing.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/airtel-money.html">Airtel Money</a> - alternative African mobile money in overlapping markets</li>
    <li><a href="/en/payments/orange-money.html">Orange Money</a> - Francophone Africa mobile money</li>
    <li><a href="/en/payments/flutterwave.html">Flutterwave</a> - multi-method payments aggregator</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no mobile money limits</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin alternative</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: MTN MoMo at 1win</h2>
  <details><summary>Which countries can use MTN MoMo at 1win?</summary><p>MTN MoMo is available in Ghana (GHS), Uganda (UGX), Cameroon, Ivory Coast, Benin, Burkina Faso, Guinea, Rwanda, South Africa, Zambia, and Eswatini. Check the 1win cashier for your country's availability.</p></details>
  <details><summary>What is the minimum MTN MoMo deposit at 1win?</summary><p>Minimum MTN MoMo deposit is GHS 5 in Ghana or UGX 2,000 in Uganda. Minimums vary by country.</p></details>
  <details><summary>How fast is an MTN MoMo deposit at 1win?</summary><p>MTN MoMo deposits are processed in real time. Expect your 1win balance to update within 2 to 5 minutes after confirming the payment.</p></details>
  <details><summary>Does 1win support MTN MoMo withdrawals?</summary><p>Yes. MTN MoMo withdrawals are supported. Enter your MTN registered phone number in the withdrawal form. Processing takes 15 minutes to 3 hours.</p></details>
  <details><summary>MTN MoMo payment failed but money was deducted. What happens?</summary><p>MTN MoMo auto-reverses failed payments within 24 hours. If you do not see a reversal after 24 hours, contact MTN MoMo customer care with the transaction ID. Also contact 1win live-chat to check if the payment was received.</p></details>
</section>
"""
    html = render_page(
        slug='payments/mtn-momo',
        title='MTN MoMo deposit at 1win for Ghana and Uganda players',
        description='Deposit and withdraw via MTN Mobile Money at 1win. GHS, UGX supported. Instant mobile money, min GHS 5. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='MTN MoMo deposit at 1win for African players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('MTN MoMo', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/mtn-momo.html','w').write(html)

# ── Orange Money ──────────────────────────────────────────────────────────────
def make_orange_money():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Which countries can use Orange Money at 1win?","acceptedAnswer":{"@type":"Answer","text":"Orange Money covers Senegal, Mali, Ivory Coast, Burkina Faso, Guinea, Guinea-Bissau, Cameroon, Madagascar, Egypt, Jordan, and Morocco. Check the 1win cashier for your country."}},
    {"@type":"Question","name":"What currency does 1win accept for Orange Money?","acceptedAnswer":{"@type":"Answer","text":"1win accepts XOF (West African CFA franc) for Francophone West Africa, XAF for Central Africa, MAD for Morocco, and EGP for Egypt, depending on the Orange Money market."}},
    {"@type":"Question","name":"How do I deposit at 1win using Orange Money?","acceptedAnswer":{"@type":"Answer","text":"Select Orange Money in the 1win cashier. Note the 1win merchant number. Open Orange Money on your phone or dial the USSD code, choose Merchant Payment, enter the 1win number and amount, confirm with your Orange Money PIN."}},
    {"@type":"Question","name":"What is the minimum Orange Money deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum varies by country. For Senegal: XOF 500. For Ivory Coast: XOF 200. Check the cashier for your country-specific minimum."}},
    {"@type":"Question","name":"Can I withdraw from 1win to Orange Money?","acceptedAnswer":{"@type":"Answer","text":"Yes. Provide your Orange Money registered phone number in the 1win withdrawal form. Processing takes 15 minutes to 2 hours."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Orange Money is the mobile payment service from Orange Group, available across West and Central Africa, North Africa, and the Middle East. 1win accepts Orange Money deposits and withdrawals on its Curaçao 8048/JAZ-licensed platform, which has grown to serve 400,000+ players worldwide. Players in Senegal, Ivory Coast, Mali, Cameroon, and other Orange markets can fund 1win accounts using local mobile money without a bank account. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Orange Money at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit (Senegal)</td><td>XOF 500</td></tr>
    <tr><td>Minimum deposit (Ivory Coast)</td><td>XOF 200</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 2 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Orange Money merchant transfer fees apply</td></tr>
    <tr><td>Supported currencies</td><td>XOF, XAF, MAD, EGP (varies by country)</td></tr>
    <tr><td>Geographic availability</td><td>17 countries across Africa and Middle East</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit at 1win with Orange Money</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register with promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Orange Money from the payment list.</strong> Enter the deposit amount in your local currency.</li>
    <li><strong>Note the 1win Orange Money merchant number.</strong> This is displayed on the cashier screen.</li>
    <li><strong>Open the Orange Money app or dial the USSD code for your country</strong> (e.g., *144# in Senegal, *144# in Ivory Coast). Select "Merchant Payment" or "Payer un marchand." Enter the 1win merchant number, the amount, and your 1win user ID as the reference. Confirm with your Orange Money secret code.</li>
    <li><strong>Wait for SMS confirmation.</strong> Your 1win balance updates within 5 minutes. Keep the Orange Money transaction reference number.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to Orange Money</h2>
  <ol>
    <li><strong>Complete identity verification on 1win.</strong> Submit a valid national ID before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose Orange Money.</strong></li>
    <li><strong>Enter your Orange Money registered phone number.</strong> Format varies by country: Senegal 77/78-XXXXXXX, Ivory Coast 07/08-XXXXXXX.</li>
    <li><strong>Enter the withdrawal amount and confirm.</strong> Verify that the name on your Orange Money account matches your 1win registration.</li>
    <li><strong>Submit.</strong> Funds arrive in 15 minutes to 2 hours. An Orange Money SMS confirms the credit.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Orange Money limits vary by country and account level. In Senegal, standard accounts allow XOF 200,000 per day; in Ivory Coast, XOF 300,000 per day for registered accounts. Advanced accounts (full KYC with biometric verification) have higher limits, up to XOF 2,000,000 per month in many markets.</p>
  <p>Orange Money operates 24/7 but may have scheduled maintenance windows between 2 AM and 4 AM local time. During maintenance, deposits may be delayed by up to 15 minutes. The system automatically retries and settles pending transactions after maintenance ends.</p>
  <p>Orange Money is particularly popular in Francophone West Africa, where it competes directly with MTN MoMo. In countries where both are available, both are typically accepted at 1win.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Orange Money operates in 17 countries: Senegal, Mali, Ivory Coast, Burkina Faso, Guinea, Guinea-Bissau, Cameroon, Central African Republic, Madagascar, Niger, DRC, Morocco (Maroc), Egypt, Jordan, and others. Primary currencies at 1win are XOF (UEMOA zone) and XAF (CEMAC zone) for African markets.</p>
  <p>For Francophone African players, Orange Money is often the most accessible option given Orange's dominant telecoms presence in the region. You can register for Orange Money at any Orange point of sale or through the Orange Money app without a bank account.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/mtn-momo.html">MTN MoMo</a> - available in overlapping Francophone markets</li>
    <li><a href="/en/payments/airtel-money.html">Airtel Money</a> - East African mobile money alternative</li>
    <li><a href="/en/payments/flutterwave.html">Flutterwave</a> - multi-method payment aggregator for Africa</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no mobile money account required</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, low fees across borders</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Orange Money at 1win</h2>
  <details><summary>Which countries can use Orange Money at 1win?</summary><p>Orange Money covers Senegal, Mali, Ivory Coast, Burkina Faso, Guinea, Guinea-Bissau, Cameroon, Madagascar, Egypt, Jordan, and Morocco. Check the 1win cashier for your country.</p></details>
  <details><summary>What currency does 1win accept for Orange Money?</summary><p>1win accepts XOF (West African CFA franc) for Francophone West Africa, XAF for Central Africa, MAD for Morocco, and EGP for Egypt, depending on the Orange Money market.</p></details>
  <details><summary>How do I deposit at 1win using Orange Money?</summary><p>Select Orange Money in the 1win cashier. Note the 1win merchant number. Open Orange Money on your phone or dial the USSD code, choose Merchant Payment, enter the 1win number and amount, confirm with your Orange Money PIN.</p></details>
  <details><summary>What is the minimum Orange Money deposit at 1win?</summary><p>Minimum varies by country. For Senegal: XOF 500. For Ivory Coast: XOF 200. Check the cashier for your country-specific minimum.</p></details>
  <details><summary>Can I withdraw from 1win to Orange Money?</summary><p>Yes. Provide your Orange Money registered phone number in the 1win withdrawal form. Processing takes 15 minutes to 2 hours.</p></details>
</section>
"""
    html = render_page(
        slug='payments/orange-money',
        title='Orange Money deposit at 1win for African players',
        description='Deposit and withdraw via Orange Money at 1win. XOF, XAF, MAD supported. Instant mobile money across 17 countries. Use XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Orange Money deposit at 1win for Francophone African players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Orange Money', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/orange-money.html','w').write(html)

# ── Flutterwave ───────────────────────────────────────────────────────────────
def make_flutterwave():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is Flutterwave and why does 1win use it?","acceptedAnswer":{"@type":"Answer","text":"Flutterwave is a leading African fintech payment infrastructure that aggregates local payment methods including bank transfers, mobile money (M-Pesa, MTN MoMo, Airtel Money), and cards across 34 African countries. 1win uses Flutterwave to offer African players a unified checkout experience."}},
    {"@type":"Question","name":"Which payment methods are available through Flutterwave at 1win?","acceptedAnswer":{"@type":"Answer","text":"Flutterwave at 1win gives access to bank transfers, mobile money networks (M-Pesa, MTN MoMo, Airtel Money, Orange Money), Visa/Mastercard cards, and USSD in a single checkout flow."}},
    {"@type":"Question","name":"Which African countries does Flutterwave cover at 1win?","acceptedAnswer":{"@type":"Answer","text":"Flutterwave covers Nigeria (NGN), Ghana (GHS), Kenya (KSh), Uganda (UGX), Tanzania (TSh), South Africa (ZAR), Rwanda (RWF), and 27 other African countries."}},
    {"@type":"Question","name":"How long do Flutterwave deposits take at 1win?","acceptedAnswer":{"@type":"Answer","text":"Flutterwave deposit speed depends on the payment method selected in the checkout: mobile money and card deposits are instant to 5 minutes; bank transfers may take 15 to 60 minutes."}},
    {"@type":"Question","name":"Is Flutterwave safe for 1win transactions?","acceptedAnswer":{"@type":"Answer","text":"Yes. Flutterwave is PCI DSS Level 1 certified and licensed by 16 African regulatory bodies. It processes over 200 million transactions per year and is used by major global merchants operating in Africa."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Flutterwave is one of Africa's most comprehensive payment infrastructure providers, accepted at 1win to give African players access to mobile money, bank transfers, and card payments through a single checkout. 1win holds a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. Flutterwave covers 34 African countries, making it the broadest single payment option for the African market. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate the welcome bonus on your first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Flutterwave at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes (via bank transfer and mobile money options in the Flutterwave flow)</td></tr>
    <tr><td>Minimum deposit</td><td>Varies by country and method; typically $1 USD equivalent</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 60 minutes (depends on method selected in Flutterwave checkout)</td></tr>
    <tr><td>Withdrawal processing time</td><td>30 minutes to 24 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Flutterwave standard merchant fees; typically 1.4% for card transactions, 0.5% for mobile money</td></tr>
    <tr><td>Supported currencies</td><td>NGN, GHS, KSh, UGX, TSh, ZAR, RWF, XOF, XAF, and 25 more</td></tr>
    <tr><td>Geographic availability</td><td>34 African countries</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit at 1win via Flutterwave</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Flutterwave from the payment list.</strong> A Flutterwave checkout modal opens. Enter the deposit amount in your local currency.</li>
    <li><strong>Choose your preferred payment method inside Flutterwave checkout.</strong> Options typically include: Bank Transfer, Mobile Money (M-Pesa, MTN MoMo, Airtel Money, Orange Money), Card (Visa/Mastercard), and USSD. Select the one that works best for you.</li>
    <li><strong>Complete the payment in the Flutterwave flow.</strong> For mobile money: enter your phone number, confirm on your phone when prompted. For bank transfer: use the account number Flutterwave provides. For card: enter your card details.</li>
    <li><strong>Return to 1win and check your balance.</strong> Mobile money and card deposits update within 5 minutes. Bank transfers may take 15 to 60 minutes.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win via Flutterwave</h2>
  <ol>
    <li><strong>Complete KYC on 1win.</strong> Submit a national ID and proof of address before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose Flutterwave.</strong></li>
    <li><strong>Select your withdrawal method.</strong> Bank account transfer or mobile money. Enter your bank account details or mobile money number.</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm all details on the summary screen.</li>
    <li><strong>Submit.</strong> 1win processes the withdrawal within 30 minutes to 24 hours depending on the method and country. Bank transfers may take longer due to interbank settlement times.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Flutterwave transaction limits vary by country, payment method, and merchant configuration. As a rule, mobile money options within Flutterwave inherit the limits of the underlying provider (M-Pesa, MTN MoMo, etc.). Card transactions processed via Flutterwave are subject to 3D Secure verification and the issuing bank's international transaction limit.</p>
  <p>Flutterwave processes over 200 million transactions per year across Africa and has 99.99% uptime. The system is engineered for the African banking environment, with automatic retries if a mobile money network experiences transient congestion.</p>
  <p>For Nigeria specifically, Flutterwave supports Naira (NGN) bank transfers and card payments. Nigerian players do not see mobile money in the Flutterwave flow as mobile money penetration via USSD is handled differently; instead, bank transfer and card are the primary options.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Flutterwave at 1win covers 34 countries including Nigeria, Ghana, Kenya, Uganda, Tanzania, South Africa, Rwanda, Senegal, Ivory Coast, Cameroon, Zambia, Ethiopia, Egypt, Morocco, and others. Each country is served in its local currency. Flutterwave is licensed by the Central Bank of Nigeria, Bank of Ghana, Bank of Tanzania, Kenya's CBK, and 12 other African financial regulators.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/mpesa.html">M-Pesa</a> - direct M-Pesa integration for Kenya/Tanzania</li>
    <li><a href="/en/payments/mtn-momo.html">MTN MoMo</a> - direct MTN integration for Ghana/Uganda</li>
    <li><a href="/en/payments/airtel-money.html">Airtel Money</a> - Airtel markets across Africa</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no African banking infrastructure needed</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, fast cross-border transfers</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Flutterwave at 1win</h2>
  <details><summary>What is Flutterwave and why does 1win use it?</summary><p>Flutterwave is a leading African fintech payment infrastructure that aggregates local payment methods including bank transfers, mobile money (M-Pesa, MTN MoMo, Airtel Money), and cards across 34 African countries. 1win uses Flutterwave to offer African players a unified checkout experience.</p></details>
  <details><summary>Which payment methods are available through Flutterwave at 1win?</summary><p>Flutterwave at 1win gives access to bank transfers, mobile money networks (M-Pesa, MTN MoMo, Airtel Money, Orange Money), Visa/Mastercard cards, and USSD in a single checkout flow.</p></details>
  <details><summary>Which African countries does Flutterwave cover at 1win?</summary><p>Flutterwave covers Nigeria (NGN), Ghana (GHS), Kenya (KSh), Uganda (UGX), Tanzania (TSh), South Africa (ZAR), Rwanda (RWF), and 27 other African countries.</p></details>
  <details><summary>How long do Flutterwave deposits take at 1win?</summary><p>Flutterwave deposit speed depends on the payment method selected in the checkout: mobile money and card deposits are instant to 5 minutes; bank transfers may take 15 to 60 minutes.</p></details>
  <details><summary>Is Flutterwave safe for 1win transactions?</summary><p>Yes. Flutterwave is PCI DSS Level 1 certified and licensed by 16 African regulatory bodies. It processes over 200 million transactions per year and is used by major global merchants operating in Africa.</p></details>
</section>
"""
    html = render_page(
        slug='payments/flutterwave',
        title='Flutterwave deposit at 1win for African players',
        description='Use Flutterwave at 1win to pay via mobile money, bank transfer or card across 34 African countries. NGN, GHS, KSh supported. Use XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Flutterwave deposit at 1win for African players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Flutterwave', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/flutterwave.html','w').write(html)


if __name__ == '__main__':
    make_mpesa()
    make_airtel_money()
    make_mtn_momo()
    make_orange_money()
    make_flutterwave()
    print("Africa pages done: 5 files")
