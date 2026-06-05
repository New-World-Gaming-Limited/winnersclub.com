"""
Generate India payment method pages for 1win.codes
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_helpers.page_template import render_page

os.makedirs('en/payments', exist_ok=True)

# ── UPI ──────────────────────────────────────────────────────────────────────
def make_upi():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is the minimum UPI deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"The minimum UPI deposit at 1win is 300 INR. There is no 1win fee on the transfer; your bank or UPI app may round up to the nearest rupee."}},
    {"@type":"Question","name":"How long does a UPI deposit take to reach my 1win account?","acceptedAnswer":{"@type":"Answer","text":"UPI deposits are processed instantly. Your balance should update within 30 seconds of completing payment in your UPI app."}},
    {"@type":"Question","name":"Can I withdraw to UPI from 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. UPI withdrawals are supported. Processing typically completes within 15 minutes to 3 hours, depending on banking infrastructure load."}},
    {"@type":"Question","name":"My UPI deposit shows pending. What should I do?","acceptedAnswer":{"@type":"Answer","text":"Wait 10 minutes. If funds left your bank but did not credit your 1win wallet, open the live-chat support and share your UTR (UPI Transaction Reference) number. The team can trace and post the deposit manually."}},
    {"@type":"Question","name":"Are there daily UPI deposit limits?","acceptedAnswer":{"@type":"Answer","text":"RBI mandates a daily UPI transaction cap of 1 lakh INR (100,000 INR) per VPA. 1win's own per-transaction ceiling aligns with this. If you need to deposit more in a single day, split across multiple transactions or use crypto as an alternative."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>1win accepts UPI deposits and withdrawals for Indian players, with Curaçao 8048/JAZ licensing confirming the platform's legitimacy. Over 400,000+ players use 1win globally, and UPI is the fastest INR on-ramp available: money moves in under 30 seconds using any VPA linked to your Indian bank account. Use promo code <span class="code-highlight">XLBONUS</span> when you register to activate the welcome bonus on your first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: UPI at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>300 INR</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>100,000 INR (RBI cap)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 30 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>None (standard UPI is free)</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India (any bank issuing UPI-enabled accounts)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with UPI at 1win</h2>
  <ol>
    <li><strong>Log in to your 1win account.</strong> If you do not have one yet, register and enter promo code <span class="code-highlight">XLBONUS</span> on the registration form.</li>
    <li><strong>Open the Cashier.</strong> Click the green "Deposit" button in the top navigation bar. The cashier panel opens on the right side of the screen.</li>
    <li><strong>Select UPI.</strong> In the payment method list, choose UPI. Enter the INR amount you want to deposit (minimum 300 INR).</li>
    <li><strong>Complete the UPI payment.</strong> 1win's payment gateway redirects you to a UPI deep link or displays a VPA and QR code. Open your UPI app (PhonePe, Google Pay, Paytm, BHIM, or any other), scan the QR or enter the VPA, confirm the amount, and approve with your UPI PIN.</li>
    <li><strong>Wait for confirmation.</strong> Your 1win wallet updates within 30 seconds. If the balance has not changed after 2 minutes, note the UTR shown in your UPI app and contact live-chat support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw with UPI from 1win</h2>
  <ol>
    <li><strong>Ensure KYC is complete.</strong> 1win requires identity verification before the first withdrawal. Upload a government-issued photo ID through the Profile section.</li>
    <li><strong>Open the Cashier and select Withdrawal.</strong> Click the wallet icon, then "Withdraw."</li>
    <li><strong>Choose UPI as the withdrawal method.</strong> Enter your registered UPI VPA (e.g., yourname@okhdfcbank or yourphone@ybl).</li>
    <li><strong>Enter the amount.</strong> Specify the INR amount. Confirm the VPA is correct; withdrawals sent to a wrong VPA cannot be reversed.</li>
    <li><strong>Submit and wait.</strong> Most UPI withdrawals process within 15 minutes to 3 hours. During peak hours or public holidays, bank settlement may extend to 24 hours. You will receive an in-app notification and email when the transfer completes.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing for UPI at 1win</h2>
  <p>The Reserve Bank of India (RBI) caps individual UPI transactions at 1,00,000 INR (1 lakh). This is a hard ceiling applied at the NPCI infrastructure level, not a 1win policy. If you want to deposit more in a session, place multiple transactions with a short gap between them.</p>
  <p>There is no published weekly cap on UPI deposits at 1win, but 1win's risk team may request additional identity checks if deposit patterns spike unusually. On the withdrawal side, 1win processes requests in the order received. The first withdrawal of a calendar month may take slightly longer (up to 4 hours) because the compliance team performs a routine account review on first withdrawals.</p>
  <p>Timing note: UPI payments are 24/7, including bank holidays and weekends, because NPCI operates around the clock. The 15 minute to 3 hour withdrawal window is the standard range; most complete in under an hour during business hours.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>UPI is available exclusively to Indian residents holding a bank account registered with a UPI-enabled institution. 1win processes UPI payments in INR only. No currency conversion occurs: you deposit in INR, your wallet balance shows in INR, and you withdraw in INR.</p>
  <p>All major Indian banks are UPI-enabled: SBI, HDFC, ICICI, Axis, Kotak, Yes Bank, and over 300 others. If your bank is UPI-enabled but the payment fails, the most common cause is a daily limit already reached on your UPI app or a wrong VPA entry. Double-check the VPA on the payment screen before confirming.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods if UPI is unavailable</h2>
  <p>If a UPI payment fails or your daily limit is exhausted, consider these alternatives available at 1win:</p>
  <ul>
    <li><a href="/en/payments/phonepe.html">PhonePe</a> - direct app integration, same INR limits</li>
    <li><a href="/en/payments/google-pay.html">Google Pay</a> - GPay UPI rails, instant</li>
    <li><a href="/en/payments/netbanking.html">Net banking (NEFT/IMPS)</a> - direct bank transfer</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto alternative, no RBI limits, geographic-agnostic</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, low network fees</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: UPI deposits and withdrawals at 1win</h2>
  <details><summary>What is the minimum UPI deposit at 1win?</summary><p>The minimum UPI deposit at 1win is 300 INR. There is no 1win fee on the transfer; your bank or UPI app may round up to the nearest rupee.</p></details>
  <details><summary>How long does a UPI deposit take to reach my 1win account?</summary><p>UPI deposits are processed instantly. Your balance should update within 30 seconds of completing payment in your UPI app.</p></details>
  <details><summary>Can I withdraw to UPI from 1win?</summary><p>Yes. UPI withdrawals are supported. Processing typically completes within 15 minutes to 3 hours, depending on banking infrastructure load.</p></details>
  <details><summary>My UPI deposit shows pending. What should I do?</summary><p>Wait 10 minutes. If funds left your bank but did not credit your 1win wallet, open live-chat support and share your UTR (UPI Transaction Reference) number. The team can trace and post the deposit manually.</p></details>
  <details><summary>Are there daily UPI deposit limits?</summary><p>RBI mandates a daily UPI transaction cap of 1 lakh INR (100,000 INR) per VPA. 1win's own per-transaction ceiling aligns with this. If you need to deposit more in a single day, split across multiple transactions or use crypto as an alternative.</p></details>
</section>
"""
    html = render_page(
        slug='payments/upi',
        title='UPI deposit at 1win for Indian players with XLBONUS',
        description='Deposit and withdraw in INR at 1win using UPI. Instant deposits from 300 INR. Use promo code XLBONUS on registration. Curacao 8048/JAZ licensed.',
        h1='UPI deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('UPI', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/upi.html','w').write(html)

# ── PhonePe ───────────────────────────────────────────────────────────────────
def make_phonepe():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Does 1win support direct PhonePe deposits?","acceptedAnswer":{"@type":"Answer","text":"Yes. PhonePe is available in the 1win cashier as a dedicated option. It uses the UPI rail, so the flow is the same as any UPI payment but pre-selects the PhonePe app."}},
    {"@type":"Question","name":"What is the minimum PhonePe deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum is 300 INR, consistent with UPI limits set by NPCI."}},
    {"@type":"Question","name":"Can I withdraw to my PhonePe wallet from 1win?","acceptedAnswer":{"@type":"Answer","text":"Withdrawals go to the bank account linked to your PhonePe VPA. Direct wallet credit is not supported; the amount lands in your savings account."}},
    {"@type":"Question","name":"PhonePe shows payment failed but money was deducted. What now?","acceptedAnswer":{"@type":"Answer","text":"Do not retry immediately. Open 1win live-chat, provide your PhonePe transaction ID (found in PhonePe transaction history). Most auto-reversals complete within 5 minutes; manual credit takes up to 2 hours."}},
    {"@type":"Question","name":"Is PhonePe available 24/7 for 1win deposits?","acceptedAnswer":{"@type":"Answer","text":"Yes. PhonePe operates 24/7 on the UPI network. Even on bank holidays, the NPCI switch routes the transaction to your bank's UPI service."}
    }
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>1win supports PhonePe as a direct INR deposit option for Indian players, operating under Curaçao 8048/JAZ licensing. With 400,000+ registered players worldwide, 1win is one of the most accessible betting platforms for Indian users. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to activate your welcome offer on your first PhonePe deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: PhonePe at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes (to linked bank account via PhonePe VPA)</td></tr>
    <tr><td>Minimum deposit</td><td>300 INR</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>100,000 INR (NPCI UPI cap)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 60 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>None (UPI P2P transfers are free)</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with PhonePe at 1win</h2>
  <ol>
    <li><strong>Log in to 1win.</strong> If you do not have an account, register and enter <span class="code-highlight">XLBONUS</span> to activate the welcome bonus.</li>
    <li><strong>Open the Cashier.</strong> Tap the "Deposit" button in the top navigation. The payment panel slides open.</li>
    <li><strong>Select PhonePe.</strong> From the list of payment options, choose PhonePe. Input the INR amount (minimum 300 INR).</li>
    <li><strong>Complete the PhonePe payment.</strong> You will be shown a QR code or a UPI deep link. If deep link, it will open the PhonePe app directly. Approve the payment using your PhonePe UPI PIN. If using QR, open PhonePe, tap "Scan QR," and scan the displayed code.</li>
    <li><strong>Confirm the balance update.</strong> Return to 1win. Your wallet should reflect the deposit in under 60 seconds. Note the PhonePe transaction ID from your app in case you need to raise a query.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw via PhonePe from 1win</h2>
  <ol>
    <li><strong>Verify your identity.</strong> Complete KYC (government ID upload) in your 1win Profile before your first withdrawal.</li>
    <li><strong>Go to the Cashier and click Withdraw.</strong></li>
    <li><strong>Select PhonePe (UPI).</strong> Enter your PhonePe VPA (example: 9XXXXXXXXX@ybl or yourname@axisbank).</li>
    <li><strong>Enter the withdrawal amount.</strong> Check the minimum withdrawal requirement shown on screen. Confirm the VPA is correct.</li>
    <li><strong>Submit the request.</strong> The amount debits from your 1win wallet immediately. Funds arrive in your bank account linked to PhonePe within 15 minutes to 3 hours. An SMS from PhonePe confirms credit.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>PhonePe transactions run on NPCI's UPI network, which enforces a 1,00,000 INR per-transaction ceiling. There is also a per-day cap across all UPI apps on a single bank account, typically 1,00,000 INR aggregated. If you approach this limit, you will need to wait until midnight for the counter to reset, or use a secondary UPI-linked account.</p>
  <p>PhonePe's own wallet (distinct from UPI) imposes lower limits of 10,000 INR per transaction and 20,000 INR per month for non-KYC wallets. 1win accepts the UPI VPA flow, not the PhonePe wallet balance, so the higher NPCI limits apply.</p>
  <p>Withdrawals at 1win follow a standard queue. First-time withdrawals within a 30-day window may take up to 4 hours due to compliance checks. Subsequent withdrawals in the same month typically process within 30 to 90 minutes.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>PhonePe is available to Indian residents with an Indian mobile number and a UPI-enabled Indian bank account. 1win processes PhonePe transactions in INR exclusively. The app is available on Android and iOS.</p>
  <p>PhonePe had over 500 million registered users as of 2024, making it India's largest UPI app by volume. Any account holder can use it at 1win without additional setup beyond having a VPA already created.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/upi.html">UPI (generic)</a> - use any UPI app, same limits</li>
    <li><a href="/en/payments/google-pay.html">Google Pay</a> - alternative UPI app for INR deposits</li>
    <li><a href="/en/payments/paytm.html">Paytm</a> - wallet plus UPI option</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - crypto alternative if UPI limits are exhausted</li>
    <li><a href="/en/payments/netbanking.html">Net banking</a> - direct NEFT/IMPS bank transfer</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: PhonePe at 1win</h2>
  <details><summary>Does 1win support direct PhonePe deposits?</summary><p>Yes. PhonePe is available in the 1win cashier as a dedicated option. It uses the UPI rail, so the flow is the same as any UPI payment but pre-selects the PhonePe app.</p></details>
  <details><summary>What is the minimum PhonePe deposit at 1win?</summary><p>Minimum is 300 INR, consistent with UPI limits set by NPCI.</p></details>
  <details><summary>Can I withdraw to my PhonePe wallet from 1win?</summary><p>Withdrawals go to the bank account linked to your PhonePe VPA. Direct wallet credit is not supported; the amount lands in your savings account.</p></details>
  <details><summary>PhonePe shows payment failed but money was deducted. What now?</summary><p>Do not retry immediately. Open 1win live-chat, provide your PhonePe transaction ID (found in PhonePe transaction history). Most auto-reversals complete within 5 minutes; manual credit takes up to 2 hours.</p></details>
  <details><summary>Is PhonePe available 24/7 for 1win deposits?</summary><p>Yes. PhonePe operates 24/7 on the UPI network. Even on bank holidays, the NPCI switch routes the transaction to your bank's UPI service.</p></details>
</section>
"""
    html = render_page(
        slug='payments/phonepe',
        title='PhonePe deposit at 1win for Indian players with XLBONUS',
        description='Use PhonePe to deposit INR at 1win instantly. Min 300 INR, no fees. Register with promo code XLBONUS. Curacao 8048/JAZ licensed platform.',
        h1='PhonePe deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('PhonePe', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/phonepe.html','w').write(html)

# ── Google Pay ────────────────────────────────────────────────────────────────
def make_googlepay():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can I use Google Pay for 1win deposits in India?","acceptedAnswer":{"@type":"Answer","text":"Yes. Google Pay (GPay) uses the UPI rail and is fully supported at 1win for INR deposits."}},
    {"@type":"Question","name":"What Google Pay VPA format does 1win accept?","acceptedAnswer":{"@type":"Answer","text":"1win accepts any valid UPI VPA including the standard Google Pay formats: mobilenumber@okaxis, mobilenumber@okhdfcbank, mobilenumber@okicici, mobilenumber@oksbi."}},
    {"@type":"Question","name":"Is there a Google Pay withdrawal option at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. Enter your GPay VPA in the withdrawal form. Funds land in the bank account linked to that VPA within 15 minutes to 3 hours."}},
    {"@type":"Question","name":"My GPay payment was declined. Why?","acceptedAnswer":{"@type":"Answer","text":"Common reasons: daily UPI limit reached on your bank account, incorrect VPA, or your bank temporarily flagging the transaction. Try a smaller amount or switch to a different UPI app on the same account."}},
    {"@type":"Question","name":"Does 1win charge any fee for Google Pay transactions?","acceptedAnswer":{"@type":"Answer","text":"No. 1win does not charge any fee. Google Pay itself does not charge for UPI P2P transfers in India."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Indian players can fund 1win accounts instantly using Google Pay (GPay) on the UPI rail. 1win holds a Curaçao 8048/JAZ licence and has served 400,000+ players globally. GPay deposits credit in under 60 seconds with no fees from either Google or 1win. Register with promo code <span class="code-highlight">XLBONUS</span> to get your welcome bonus activated on the first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Google Pay at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>300 INR</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>100,000 INR (NPCI/RBI UPI cap)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 60 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>None</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit using Google Pay at 1win</h2>
  <ol>
    <li><strong>Log in to your 1win account.</strong> New users: register first and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Click Deposit in the cashier.</strong> The payment method panel opens. Select Google Pay or the generic UPI option.</li>
    <li><strong>Enter the deposit amount.</strong> Minimum is 300 INR. The screen will display a QR code or UPI payment link.</li>
    <li><strong>Open Google Pay on your phone.</strong> Tap "Scan QR code," point at the screen, or tap the UPI deep-link on mobile to jump directly into GPay. Confirm the amount and approve with your UPI PIN.</li>
    <li><strong>Check your 1win wallet.</strong> Funds appear within 60 seconds. If not, note the GPay transaction ID (visible in GPay under transaction history) and contact 1win live-chat support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw to Google Pay from 1win</h2>
  <ol>
    <li><strong>Complete KYC.</strong> Submit a valid government-issued photo ID in your 1win profile settings before the first withdrawal.</li>
    <li><strong>Open the Withdrawal section of the cashier.</strong></li>
    <li><strong>Select Google Pay (UPI).</strong> Enter your GPay VPA. Standard formats: mobilenumber@okaxis, mobilenumber@okhdfcbank, mobilenumber@okicici, mobilenumber@oksbi.</li>
    <li><strong>Enter the withdrawal amount.</strong> Double-check the VPA. An error in the VPA will cause the funds to reach the wrong account with no recourse.</li>
    <li><strong>Submit.</strong> The wallet deducts immediately. Funds arrive in 15 minutes to 3 hours; you will get a GPay notification on credit.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Google Pay on UPI inherits the NPCI per-transaction limit of 1,00,000 INR. Google also sets its own daily aggregate limit, which for fully KYC-verified accounts is 1,00,000 INR per day. Some banks that participate in GPay set lower limits; check your bank's UPI limit in your net banking portal if you experience declines at high amounts.</p>
  <p>For deposits, timing is effectively instant: the NPCI switch confirms transactions in real time. For withdrawals, 1win's payment processor queues and dispatches the request, which typically completes within the first hour during the working day. Night-time withdrawals (midnight to 6 AM IST) may take slightly longer as the banking batch settlement runs.</p>
  <p>No cap on the number of daily GPay deposits from 1win's side, but if your bank declines after three failed attempts in a row, UPI may temporarily block further attempts to that VPA for up to 24 hours. In that case, use a different UPI app or crypto.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Google Pay UPI is available in India only. 1win processes GPay transactions exclusively in INR. If you have an overseas Google Pay account, it operates on different payment rails and is not the same product; 1win's UPI integration applies only to Indian accounts.</p>
  <p>Google Pay is available on Android and iOS. The app requires an Indian mobile number and an Indian bank account to create a UPI VPA. As of 2024, Google Pay is the second-largest UPI app in India by transaction volume, ensuring high reliability and uptime.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/phonepe.html">PhonePe</a> - leading UPI app in India</li>
    <li><a href="/en/payments/upi.html">UPI (generic)</a> - any UPI-capable app</li>
    <li><a href="/en/payments/imps.html">IMPS</a> - direct interbank transfer, higher single-transaction limits</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto option with no RBI limits</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, fast and low fee</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Google Pay at 1win</h2>
  <details><summary>Can I use Google Pay for 1win deposits in India?</summary><p>Yes. Google Pay (GPay) uses the UPI rail and is fully supported at 1win for INR deposits.</p></details>
  <details><summary>What Google Pay VPA format does 1win accept?</summary><p>1win accepts any valid UPI VPA including the standard Google Pay formats: mobilenumber@okaxis, mobilenumber@okhdfcbank, mobilenumber@okicici, mobilenumber@oksbi.</p></details>
  <details><summary>Is there a Google Pay withdrawal option at 1win?</summary><p>Yes. Enter your GPay VPA in the withdrawal form. Funds land in the bank account linked to that VPA within 15 minutes to 3 hours.</p></details>
  <details><summary>My GPay payment was declined. Why?</summary><p>Common reasons: daily UPI limit reached on your bank account, incorrect VPA, or your bank temporarily flagging the transaction. Try a smaller amount or switch to a different UPI app on the same account.</p></details>
  <details><summary>Does 1win charge any fee for Google Pay transactions?</summary><p>No. 1win does not charge any fee. Google Pay itself does not charge for UPI P2P transfers in India.</p></details>
</section>
"""
    html = render_page(
        slug='payments/google-pay',
        title='Google Pay deposit at 1win for Indian players with XLBONUS',
        description='Fund your 1win account with Google Pay in INR. Instant deposits from 300 INR, no fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Google Pay deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Google Pay', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/google-pay.html','w').write(html)

# ── Paytm ─────────────────────────────────────────────────────────────────────
def make_paytm():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can I use Paytm Wallet for 1win deposits?","acceptedAnswer":{"@type":"Answer","text":"1win accepts Paytm via the UPI VPA route. Deposits from the Paytm Wallet balance may not be available; use the Paytm UPI handle (yourname@paytm) linked to your bank account instead."}},
    {"@type":"Question","name":"What is the Paytm VPA format for 1win?","acceptedAnswer":{"@type":"Answer","text":"The standard Paytm UPI handle is mobilenumber@paytm. This VPA draws from the bank account linked in the Paytm app."}},
    {"@type":"Question","name":"How long do Paytm deposits take at 1win?","acceptedAnswer":{"@type":"Answer","text":"Paytm UPI deposits are instant. Your 1win balance updates within 60 seconds of payment approval in the Paytm app."}},
    {"@type":"Question","name":"Can I withdraw from 1win to Paytm?","acceptedAnswer":{"@type":"Answer","text":"Yes, withdrawals to the Paytm UPI VPA (linked bank account) are supported. Processing takes 15 minutes to 3 hours."}},
    {"@type":"Question","name":"Paytm deposit failed. What should I check?","acceptedAnswer":{"@type":"Answer","text":"First, confirm the Paytm UPI PIN was entered correctly. Second, check your linked bank account balance. Third, check if your bank has blocked gaming MCC transactions. If all clear, provide the Paytm order ID to 1win live-chat."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Paytm is accepted at 1win for INR deposits and withdrawals, giving Indian players a familiar, locally trusted payment option on a Curaçao 8048/JAZ-licensed platform used by 400,000+ players around the world. Use promo code <span class="code-highlight">XLBONUS</span> during registration to unlock the welcome bonus on your first Paytm deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Paytm at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes (via Paytm UPI VPA)</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes (to Paytm-linked bank account)</td></tr>
    <tr><td>Minimum deposit</td><td>300 INR</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>100,000 INR (NPCI UPI cap)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 60 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>None (UPI transfers)</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Paytm at 1win</h2>
  <ol>
    <li><strong>Log in to 1win.</strong> New users: register with promo code <span class="code-highlight">XLBONUS</span> to activate the welcome bonus.</li>
    <li><strong>Open the Cashier and select Deposit.</strong> The payment method panel loads.</li>
    <li><strong>Choose Paytm or UPI.</strong> Some versions of the 1win cashier show Paytm as a dedicated tile; others show a generic UPI input. Either will work with a Paytm VPA.</li>
    <li><strong>Enter amount and complete payment.</strong> Enter 300 INR or more. A QR code or deep-link appears. In the Paytm app, tap "Scan and Pay" or follow the deep-link, verify the amount, and approve with your Paytm UPI PIN.</li>
    <li><strong>Confirm the credit.</strong> The 1win wallet updates within 60 seconds. Save the Paytm Order ID from the app in case you need to follow up.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw to Paytm from 1win</h2>
  <ol>
    <li><strong>Complete identity verification.</strong> Upload an Aadhaar or PAN card scan in your 1win profile before requesting a withdrawal.</li>
    <li><strong>Go to Cashier and select Withdrawal.</strong></li>
    <li><strong>Choose Paytm (UPI).</strong> Enter your Paytm VPA, typically mobilenumber@paytm.</li>
    <li><strong>Specify the withdrawal amount.</strong> Verify the VPA on screen. Even a single digit error routes funds to the wrong account.</li>
    <li><strong>Submit.</strong> Funds deduct from your wallet instantly and arrive in your Paytm-linked bank account within 15 minutes to 3 hours. A Paytm notification confirms receipt.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Paytm UPI transactions are subject to the same NPCI ceiling of 1,00,000 INR per transaction. Paytm's own daily transaction limit for fully verified accounts is also 1,00,000 INR. For the Paytm wallet (as opposed to UPI), limits are lower: 10,000 INR per transaction and 1,00,000 INR per month. Because 1win routes through UPI VPA, not the wallet balance, the higher limit applies.</p>
  <p>During peak times like IPL season or major cricket matches, Paytm payment server load increases. If the payment takes more than 90 seconds to confirm, it is still being processed; do not restart the flow or you risk a duplicate transaction. Wait at least 3 minutes before concluding a payment has failed.</p>
  <p>If your Paytm account is under Minimum KYC status, UPI limits may be lower than full KYC accounts. Upgrade to full KYC in the Paytm app for maximum limits.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Paytm is available to Indian residents only. 1win processes all Paytm transactions in INR. Paytm is regulated by the Reserve Bank of India (RBI) as a Payment Aggregator and must comply with RBI guidelines, which include transaction monitoring requirements.</p>
  <p>Paytm has over 300 million registered users in India as of 2024. The UPI VPA linked to the Paytm app can be associated with any Indian bank, including SBI, HDFC, ICICI, Axis, and others.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/upi.html">UPI (generic)</a> - use any UPI app</li>
    <li><a href="/en/payments/phonepe.html">PhonePe</a> - alternative UPI app</li>
    <li><a href="/en/payments/netbanking.html">Net banking</a> - direct bank transfer</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - no RBI limits, global availability</li>
    <li><a href="/en/payments/ethereum.html">Ethereum</a> - fast crypto alternative</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Paytm at 1win</h2>
  <details><summary>Can I use Paytm Wallet for 1win deposits?</summary><p>1win accepts Paytm via the UPI VPA route. Deposits from the Paytm Wallet balance may not be available; use the Paytm UPI handle (mobilenumber@paytm) linked to your bank account instead.</p></details>
  <details><summary>What is the Paytm VPA format for 1win?</summary><p>The standard Paytm UPI handle is mobilenumber@paytm. This VPA draws from the bank account linked in the Paytm app.</p></details>
  <details><summary>How long do Paytm deposits take at 1win?</summary><p>Paytm UPI deposits are instant. Your 1win balance updates within 60 seconds of payment approval in the Paytm app.</p></details>
  <details><summary>Can I withdraw from 1win to Paytm?</summary><p>Yes, withdrawals to the Paytm UPI VPA (linked bank account) are supported. Processing takes 15 minutes to 3 hours.</p></details>
  <details><summary>Paytm deposit failed. What should I check?</summary><p>First, confirm the Paytm UPI PIN was entered correctly. Second, check your linked bank account balance. Third, check if your bank has blocked gaming MCC transactions. If all clear, provide the Paytm Order ID to 1win live-chat.</p></details>
</section>
"""
    html = render_page(
        slug='payments/paytm',
        title='Paytm deposit at 1win for Indian players with XLBONUS',
        description='Deposit INR at 1win via Paytm UPI. Instant, no fees, min 300 INR. Enter promo code XLBONUS at registration. Curacao 8048/JAZ licensed.',
        h1='Paytm deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Paytm', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/paytm.html','w').write(html)

# ── IMPS ──────────────────────────────────────────────────────────────────────
def make_imps():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is IMPS and how is it different from UPI at 1win?","acceptedAnswer":{"@type":"Answer","text":"IMPS (Immediate Payment Service) is a direct interbank transfer using IFSC code and account number, while UPI uses a virtual payment address. IMPS allows transfers up to 5 lakh INR per transaction compared to UPI's 1 lakh cap."}},
    {"@type":"Question","name":"How long does an IMPS deposit take to reach 1win?","acceptedAnswer":{"@type":"Answer","text":"IMPS is instant, 24/7. Funds typically appear in your 1win wallet within 5 to 30 minutes after your bank confirms the transfer."}},
    {"@type":"Question","name":"What details do I need to make an IMPS deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"You need the 1win beneficiary account number and IFSC code, which are displayed in the cashier when you select IMPS."}},
    {"@type":"Question","name":"Is there a minimum amount for IMPS deposits at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes, minimum is 500 INR for IMPS deposits at 1win."}},
    {"@type":"Question","name":"My IMPS transfer was successful but 1win balance did not update. What do I do?","acceptedAnswer":{"@type":"Answer","text":"IMPS reconciliation can take up to 30 minutes. If balance is still not updated after 30 minutes, provide your bank UTR number and the RRN (Reference Number) to 1win live-chat for manual credit."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>IMPS (Immediate Payment Service) lets Indian players send INR directly from their bank account to 1win without any app or wallet intermediary. 1win is licensed under Curaçao 8048/JAZ and serves 400,000+ players. IMPS supports up to 5 lakh INR per transaction, making it the preferred choice for large deposits where UPI's 1 lakh cap is restrictive. Use promo code <span class="code-highlight">XLBONUS</span> on your first deposit to activate the welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: IMPS at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>500 INR</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>500,000 INR (5 lakh, NPCI IMPS cap)</td></tr>
    <tr><td>Deposit processing time</td><td>5 to 30 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>1 to 6 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Bank-dependent; most banks charge 5 to 25 INR per IMPS transaction</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India (all NPCI member banks)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit using IMPS at 1win</h2>
  <ol>
    <li><strong>Log in and open the Cashier.</strong> Click "Deposit" and select IMPS from the payment list.</li>
    <li><strong>Note the 1win bank details.</strong> The cashier displays a beneficiary account number, IFSC code, and account name. Write these down or screenshot them.</li>
    <li><strong>Open your bank's net banking or mobile app.</strong> Navigate to "Fund Transfer" or "IMPS Transfer."</li>
    <li><strong>Enter the beneficiary details.</strong> Input the account number and IFSC code from the 1win cashier. Enter the deposit amount (minimum 500 INR). Add your 1win user ID in the payment remarks/reference field so the payment team can match your transfer.</li>
    <li><strong>Submit the transfer and wait.</strong> Your bank will send an SMS with a UTR number. Keep this. Your 1win wallet updates within 5 to 30 minutes. If not updated in 30 minutes, share the UTR with live-chat support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw via IMPS from 1win</h2>
  <ol>
    <li><strong>Complete KYC.</strong> Provide a government-issued ID and proof of bank account (cancelled cheque or bank statement) in your 1win profile.</li>
    <li><strong>Open Cashier and select Withdrawal.</strong> Choose IMPS.</li>
    <li><strong>Enter your bank account details.</strong> Provide your full account number, IFSC code, and account holder name exactly as registered with your bank.</li>
    <li><strong>Enter the withdrawal amount.</strong> Minimum varies; check the cashier screen.</li>
    <li><strong>Submit.</strong> 1win initiates the IMPS transfer within 1 to 2 hours. End-to-end completion is 1 to 6 hours. Your bank will credit the amount and send an SMS confirmation.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>IMPS has a per-transaction cap of 5,00,000 INR (5 lakh) set by NPCI, which is significantly higher than UPI's 1 lakh limit. This makes IMPS the best option for high-value deposits. Individual banks may impose lower per-transaction limits; check your net banking settings or contact your bank to confirm your IMPS limit.</p>
  <p>IMPS operates 24 hours a day, 7 days a week, including public holidays and weekend banking non-business days. However, very large transfers (above 2 lakh) may trigger an additional review delay on the bank's fraud prevention system, adding 15 to 30 minutes to the posting time.</p>
  <p>Banks typically charge 5 to 25 INR per IMPS transaction. This fee is deducted by your bank; 1win does not charge any additional processing fee.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>IMPS is available across all NPCI member banks in India, covering virtually every bank in the country. Transactions are in INR only. IMPS is governed by the Reserve Bank of India (RBI) under the Payment and Settlement Systems Act, 2007.</p>
  <p>Players who prefer not to use a third-party app (like PhonePe or GPay) can use IMPS directly from their bank's net banking portal or mobile app, giving more control over the transfer details.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/upi.html">UPI</a> - app-based instant transfer, 1 lakh cap</li>
    <li><a href="/en/payments/neft.html">NEFT</a> - lower fee, slightly slower, no transaction cap</li>
    <li><a href="/en/payments/netbanking.html">Net banking</a> - covers both NEFT and IMPS in one flow</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto alternative for large deposits without bank limits</li>
    <li><a href="/en/payments/usdt-erc20.html">USDT ERC20</a> - stablecoin for large value transfers</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: IMPS at 1win</h2>
  <details><summary>What is IMPS and how is it different from UPI at 1win?</summary><p>IMPS (Immediate Payment Service) is a direct interbank transfer using IFSC code and account number, while UPI uses a virtual payment address. IMPS allows transfers up to 5 lakh INR per transaction compared to UPI's 1 lakh cap.</p></details>
  <details><summary>How long does an IMPS deposit take to reach 1win?</summary><p>IMPS is instant, 24/7. Funds typically appear in your 1win wallet within 5 to 30 minutes after your bank confirms the transfer.</p></details>
  <details><summary>What details do I need to make an IMPS deposit at 1win?</summary><p>You need the 1win beneficiary account number and IFSC code, which are displayed in the cashier when you select IMPS.</p></details>
  <details><summary>Is there a minimum amount for IMPS deposits at 1win?</summary><p>Yes, minimum is 500 INR for IMPS deposits at 1win.</p></details>
  <details><summary>My IMPS transfer was successful but 1win balance did not update. What do I do?</summary><p>IMPS reconciliation can take up to 30 minutes. If balance is still not updated after 30 minutes, provide your bank UTR number and the RRN (Reference Number) to 1win live-chat for manual credit.</p></details>
</section>
"""
    html = render_page(
        slug='payments/imps',
        title='IMPS deposit at 1win for Indian players with XLBONUS',
        description='Deposit up to 5 lakh INR at 1win via IMPS direct bank transfer. Fast, no 1win fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='IMPS deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('IMPS', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/imps.html','w').write(html)

# ── NEFT ──────────────────────────────────────────────────────────────────────
def make_neft():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"How long does a NEFT deposit take at 1win?","acceptedAnswer":{"@type":"Answer","text":"NEFT processes in half-hourly batches 24/7. Deposits typically credit to your 1win wallet within 30 to 120 minutes after the bank initiates the transfer."}},
    {"@type":"Question","name":"Is there a maximum limit on NEFT deposits at 1win?","acceptedAnswer":{"@type":"Answer","text":"RBI has removed the NEFT transaction cap. Theoretically you can transfer any amount. In practice, your bank may impose daily or per-transaction limits; check your net banking settings."}},
    {"@type":"Question","name":"What is the minimum NEFT deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum NEFT deposit is 500 INR."}},
    {"@type":"Question","name":"Does 1win charge a fee for NEFT deposits?","acceptedAnswer":{"@type":"Answer","text":"1win charges no fee. Your bank may charge up to 25 INR for outward NEFT transfers depending on your account type."}},
    {"@type":"Question","name":"My NEFT deposit has not arrived after 2 hours. What should I do?","acceptedAnswer":{"@type":"Answer","text":"Collect your bank's NEFT UTR number and the transfer acknowledgement. Contact 1win live-chat and provide both the UTR and your 1win user ID. The payments team can locate and manually post the credit."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>NEFT (National Electronic Funds Transfer) is a batch-based bank transfer method accepted at 1win for INR deposits. The platform holds a Curaçao 8048/JAZ licence and is trusted by 400,000+ players worldwide. NEFT has no per-transaction cap set by RBI, making it suitable for large deposits that exceed UPI or IMPS limits. Register with promo code <span class="code-highlight">XLBONUS</span> to activate the welcome bonus on your first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: NEFT at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>500 INR</td></tr>
    <tr><td>Maximum deposit</td><td>No RBI cap; bank limits apply</td></tr>
    <tr><td>Deposit processing time</td><td>30 to 120 minutes (batch settlement)</td></tr>
    <tr><td>Withdrawal processing time</td><td>2 to 12 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Up to 25 INR (bank-dependent)</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India (all RBI-member banks)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit using NEFT at 1win</h2>
  <ol>
    <li><strong>Log in and open the Cashier.</strong> Select "Deposit," then choose NEFT from the payment method list.</li>
    <li><strong>Copy the 1win beneficiary details.</strong> The cashier displays the account number, IFSC code, and account name. Screenshot this screen.</li>
    <li><strong>Log in to your bank's net banking or mobile app.</strong> Add 1win as a NEFT beneficiary using the details from step 2. Beneficiary addition may require a 30-minute bank cool-down on first-time additions.</li>
    <li><strong>Initiate the NEFT transfer.</strong> Select NEFT, choose the 1win beneficiary, enter the amount (minimum 500 INR), and include your 1win user ID in the payment remarks field. Confirm with your net banking password or OTP.</li>
    <li><strong>Wait for the batch to settle.</strong> NEFT batches run every 30 minutes. You will get a UTR confirmation SMS from your bank. Your 1win wallet updates after the batch settles, typically within 30 to 120 minutes. Keep the UTR in case you need to follow up with support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw via NEFT from 1win</h2>
  <ol>
    <li><strong>Verify your identity on 1win.</strong> Upload PAN card or Aadhaar and a bank proof document before your first withdrawal.</li>
    <li><strong>Open Cashier and click Withdraw. Select NEFT.</strong></li>
    <li><strong>Enter your bank account number, IFSC code, and account holder name.</strong> These must match your bank records exactly.</li>
    <li><strong>Enter the withdrawal amount.</strong> NEFT withdrawals have no system-level cap, but 1win's risk team may request additional verification for very large withdrawals.</li>
    <li><strong>Submit.</strong> 1win queues your withdrawal request. NEFT credits arrive in 2 to 12 hours depending on when the next batch settles at your bank. Your bank sends an SMS on credit.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>RBI removed the NEFT per-transaction ceiling in December 2019, meaning there is no cap on individual NEFT transfers at the network level. However, your bank may still impose daily transfer limits through net banking (common caps are 5 lakh to 25 lakh per day depending on the bank and account type). Check your bank's net banking settings under "Transaction Limits" to see your specific cap.</p>
  <p>NEFT operates 24/7 on all days of the year including Sundays and public holidays since December 2019. Batches settle every 30 minutes, starting at midnight. If you initiate a transfer at 2:15 PM, the batch settles at 2:30 PM and 1win should receive the funds by 3:00 PM at the latest.</p>
  <p>NEFT is slower than IMPS or UPI for small amounts, but for transfers above 5 lakh, it remains a reliable option without IMPS's occasional high-value bank flags.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>NEFT is available at all banks that are RBI members in India, covering virtually all public and private sector banks, regional rural banks, and cooperative banks. NEFT transfers are in INR only. 1win's receiving bank account is an Indian bank account denominated in INR.</p>
  <p>Non-resident Indians (NRI) with NRE or NRO accounts can also use NEFT if their bank allows outward domestic transfers from these accounts.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/imps.html">IMPS</a> - faster settlement, up to 5 lakh per transaction</li>
    <li><a href="/en/payments/upi.html">UPI</a> - instant, app-based, 1 lakh cap</li>
    <li><a href="/en/payments/netbanking.html">Net banking</a> - integrated bank login flow</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto for large transfers without bank-level limits</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin with fast settlement</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: NEFT at 1win</h2>
  <details><summary>How long does a NEFT deposit take at 1win?</summary><p>NEFT processes in half-hourly batches 24/7. Deposits typically credit to your 1win wallet within 30 to 120 minutes after the bank initiates the transfer.</p></details>
  <details><summary>Is there a maximum limit on NEFT deposits at 1win?</summary><p>RBI has removed the NEFT transaction cap. Theoretically you can transfer any amount. In practice, your bank may impose daily or per-transaction limits; check your net banking settings.</p></details>
  <details><summary>What is the minimum NEFT deposit at 1win?</summary><p>Minimum NEFT deposit is 500 INR.</p></details>
  <details><summary>Does 1win charge a fee for NEFT deposits?</summary><p>1win charges no fee. Your bank may charge up to 25 INR for outward NEFT transfers depending on your account type.</p></details>
  <details><summary>My NEFT deposit has not arrived after 2 hours. What should I do?</summary><p>Collect your bank's NEFT UTR number and the transfer acknowledgement. Contact 1win live-chat and provide both the UTR and your 1win user ID. The payments team can locate and manually post the credit.</p></details>
</section>
"""
    html = render_page(
        slug='payments/neft',
        title='NEFT bank transfer deposit at 1win with XLBONUS',
        description='Deposit INR at 1win via NEFT bank transfer. No RBI cap, no 1win fee, min 500 INR. Use promo code XLBONUS at registration. Curacao 8048/JAZ licensed.',
        h1='NEFT deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('NEFT', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/neft.html','w').write(html)

# ── RuPay ─────────────────────────────────────────────────────────────────────
def make_rupay():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Can I use a RuPay debit card at 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. RuPay debit cards are accepted at 1win for INR deposits. Ensure your card has online transactions enabled through your bank's app or net banking."}},
    {"@type":"Question","name":"Does 1win accept RuPay credit cards?","acceptedAnswer":{"@type":"Answer","text":"RuPay credit card acceptance depends on the 1win payment gateway at the time of deposit. Debit cards are more reliably accepted. If a credit card is declined, use UPI or IMPS as an alternative."}},
    {"@type":"Question","name":"What is the minimum RuPay card deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum card deposit is 500 INR."}},
    {"@type":"Question","name":"My RuPay card was declined. Why?","acceptedAnswer":{"@type":"Answer","text":"Common reasons: online transactions not enabled, daily debit card limit reached, bank blocking gaming merchant category code (MCC 7995), or 3D Secure OTP failure. Enable online transactions in your bank app and try again."}},
    {"@type":"Question","name":"Can I withdraw to a RuPay card from 1win?","acceptedAnswer":{"@type":"Answer","text":"Direct card refunds to RuPay are not standard; withdrawals typically go via UPI or bank transfer. Check the cashier for current withdrawal methods available on your account."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>RuPay is India's domestic card network, and 1win accepts RuPay debit card deposits in INR on its Curaçao 8048/JAZ-licensed platform. With 400,000+ players globally and direct INR processing, 1win gives Indian players a straightforward card-based option alongside UPI. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to unlock your welcome bonus on your first RuPay deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: RuPay at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Limited (UPI or bank transfer preferred for withdrawals)</td></tr>
    <tr><td>Minimum deposit</td><td>500 INR</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>Up to your bank's daily debit card limit</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>Via UPI: 15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>None for standard debit; some banks charge domestic card transaction fee</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with a RuPay card at 1win</h2>
  <ol>
    <li><strong>Enable online card transactions.</strong> Before attempting a card deposit, open your bank's mobile app and confirm online/e-commerce transactions are enabled for your RuPay card. Set the daily online limit to cover your intended deposit.</li>
    <li><strong>Log in to 1win and open the Cashier.</strong> Click "Deposit" and select Card or RuPay from the payment options.</li>
    <li><strong>Enter your card details.</strong> Input the 16-digit card number, expiry date, and CVV. Confirm the amount (minimum 500 INR).</li>
    <li><strong>Complete 3D Secure verification.</strong> Your bank will send an OTP to your registered mobile number. Enter the OTP on the payment page within the time limit (usually 3 minutes).</li>
    <li><strong>Wait for confirmation.</strong> The payment processes in under 5 minutes. Your 1win wallet updates and you receive an email confirmation.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw when using RuPay at 1win</h2>
  <ol>
    <li><strong>Complete KYC first.</strong> Upload your Aadhaar or PAN card in your 1win profile.</li>
    <li><strong>Open the Cashier and select Withdrawal.</strong> Since direct card withdrawals to RuPay are limited, use UPI as the withdrawal method.</li>
    <li><strong>Link a UPI VPA.</strong> Enter your UPI VPA (from any UPI app, including one linked to the same bank as your RuPay card).</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm the VPA, then submit.</li>
    <li><strong>Track the transfer.</strong> UPI withdrawal completes in 15 minutes to 3 hours. You will get an in-app notification from 1win and an SMS from your bank.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>RuPay card deposit limits at 1win are controlled by your bank, not 1win. Standard daily online limits for Indian debit cards range from 25,000 INR to 1,00,000 INR depending on the bank and account type. RuPay Classic cards typically have lower limits than RuPay Platinum cards.</p>
  <p>If your bank blocks gaming merchant category codes (MCC 7995), the RuPay card deposit will be declined. In this case, UPI is a seamless alternative because UPI transfers use P2P rails that bypass MCC restrictions. Crypto deposits (Bitcoin, USDT) are also fully available as a fallback and have no MCC classification.</p>
  <p>Deposit processing via RuPay card is instant to 5 minutes. There is no batch settlement like NEFT; the card payment network confirms in real time.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>RuPay is India's domestic card scheme, launched by NPCI in 2012. It is accepted at all Indian point-of-sale terminals and most e-commerce merchants. 1win processes RuPay deposits in INR only. RuPay has expanded internationally to a few countries (UAE, Singapore, Bhutan), but 1win's RuPay acceptance applies to Indian-issued cards only.</p>
  <p>RuPay cards are issued by most Indian banks including SBI, Bank of Baroda, Punjab National Bank, Canara Bank, and many cooperative banks. Jan Dhan Yojana accounts come with a free RuPay card, making this payment method accessible to a very large segment of the Indian population.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/upi.html">UPI</a> - bypasses MCC blocks, instant, no card details needed</li>
    <li><a href="/en/payments/netbanking.html">Net banking</a> - direct bank login, no card required</li>
    <li><a href="/en/payments/visa.html">Visa</a> - international card option</li>
    <li><a href="/en/payments/mastercard.html">Mastercard</a> - international card alternative</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - no MCC restrictions, crypto alternative</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: RuPay at 1win</h2>
  <details><summary>Can I use a RuPay debit card at 1win?</summary><p>Yes. RuPay debit cards are accepted at 1win for INR deposits. Ensure your card has online transactions enabled through your bank's app or net banking.</p></details>
  <details><summary>Does 1win accept RuPay credit cards?</summary><p>RuPay credit card acceptance depends on the 1win payment gateway at the time of deposit. Debit cards are more reliably accepted. If a credit card is declined, use UPI or IMPS as an alternative.</p></details>
  <details><summary>What is the minimum RuPay card deposit at 1win?</summary><p>Minimum card deposit is 500 INR.</p></details>
  <details><summary>My RuPay card was declined. Why?</summary><p>Common reasons: online transactions not enabled, daily debit card limit reached, bank blocking gaming merchant category code (MCC 7995), or 3D Secure OTP failure. Enable online transactions in your bank app and try again.</p></details>
  <details><summary>Can I withdraw to a RuPay card from 1win?</summary><p>Direct card refunds to RuPay are not standard; withdrawals typically go via UPI or bank transfer. Check the cashier for current withdrawal methods available on your account.</p></details>
</section>
"""
    html = render_page(
        slug='payments/rupay',
        title='RuPay card deposit at 1win for Indian players with XLBONUS',
        description='Deposit INR at 1win using your RuPay debit card. Instant, min 500 INR, no 1win fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='RuPay card deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('RuPay', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/rupay.html','w').write(html)

# ── Net Banking ───────────────────────────────────────────────────────────────
def make_netbanking():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Which banks does 1win accept for net banking deposits?","acceptedAnswer":{"@type":"Answer","text":"1win supports all major Indian banks for net banking including SBI, HDFC, ICICI, Axis, Kotak, Punjab National Bank, Bank of Baroda, and dozens of others through its payment aggregator."}},
    {"@type":"Question","name":"How long do net banking deposits take at 1win?","acceptedAnswer":{"@type":"Answer","text":"Net banking deposits route via IMPS or NEFT depending on the bank. IMPS-routed deposits arrive in 5 to 30 minutes; NEFT-routed deposits arrive in 30 to 120 minutes."}},
    {"@type":"Question","name":"Is net banking safe for 1win deposits?","acceptedAnswer":{"@type":"Answer","text":"Yes. 1win uses a PCI-compliant payment aggregator. Your bank credentials are entered on your bank's own secure login page, not on 1win's site."}},
    {"@type":"Question","name":"What is the minimum net banking deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum is 500 INR for net banking deposits."}},
    {"@type":"Question","name":"Can I withdraw to my bank account directly via net banking from 1win?","acceptedAnswer":{"@type":"Answer","text":"Withdrawals go via NEFT or IMPS directly to your registered bank account number. You do not need to log into net banking for withdrawals; you only provide your account number and IFSC code in the 1win cashier."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Net banking (online banking) is one of the most reliable INR deposit methods at 1win, the Curaçao 8048/JAZ-licensed platform used by 400,000+ players worldwide. The payment routes directly from your Indian bank account to 1win through a secure payment aggregator, without any wallet or app in between. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate your welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Net banking at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes (direct to bank account via NEFT/IMPS)</td></tr>
    <tr><td>Minimum deposit</td><td>500 INR</td></tr>
    <tr><td>Maximum deposit</td><td>Your bank's daily online transfer limit</td></tr>
    <tr><td>Deposit processing time</td><td>5 to 120 minutes (IMPS or NEFT-routed)</td></tr>
    <tr><td>Withdrawal processing time</td><td>1 to 12 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Bank-dependent; typically 0 to 25 INR</td></tr>
    <tr><td>Supported currencies</td><td>INR</td></tr>
    <tr><td>Geographic availability</td><td>India (all major banks)</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit via net banking at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> Click "Deposit" and select Net Banking from the payment options.</li>
    <li><strong>Select your bank.</strong> A list of supported banks appears. Choose your bank from the dropdown. If your bank is not listed, use UPI or IMPS as alternatives.</li>
    <li><strong>Enter the deposit amount.</strong> Input the INR amount (minimum 500 INR). Confirm and click "Proceed to Bank."</li>
    <li><strong>Log in on your bank's secure page.</strong> You are redirected to your bank's own net banking login. Enter your user ID and password. Complete any additional verification (OTP, grid card, etc.) required by your bank.</li>
    <li><strong>Authorise the payment.</strong> Confirm the transfer on your bank's portal. You are redirected back to 1win. The wallet updates within 5 to 120 minutes depending on whether the transfer routes via IMPS or NEFT.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw to your bank account from 1win</h2>
  <ol>
    <li><strong>Complete KYC verification.</strong> Submit identity documents in your 1win profile before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal.</strong> Choose Bank Transfer (NEFT/IMPS).</li>
    <li><strong>Enter your bank account details.</strong> Provide the account number, IFSC code, account holder name, and bank name.</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm all details on the summary screen.</li>
    <li><strong>Submit.</strong> 1win debits your wallet immediately and initiates the bank transfer. Funds arrive in 1 to 12 hours via NEFT or 30 minutes to 3 hours via IMPS. Your bank sends an SMS on credit.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Net banking deposit limits at 1win are constrained by your bank's daily online transfer limit, which varies. SBI allows up to 10 lakh INR per day via net banking; HDFC and ICICI allow up to 25 lakh per day for retail customers. Check your bank's limit in your net banking profile under "Transaction Limits."</p>
  <p>1win's payment aggregator routes the transaction via IMPS for faster settlement or NEFT for larger amounts, depending on the aggregator's routing logic. In practice, most standard deposits settle within 30 minutes during business hours.</p>
  <p>Net banking requires an active internet connection and access to your bank's portal. If your bank enforces session time limits, complete the 1win payment page quickly. Sessions that expire mid-flow may result in a pending transaction that settles automatically within 30 minutes or returns to your bank account.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Net banking at 1win is available for Indian residents with accounts at any major Indian bank. All transactions are in INR. The list of supported banks through 1win's payment aggregator includes SBI, HDFC Bank, ICICI Bank, Axis Bank, Kotak Mahindra Bank, Punjab National Bank, Bank of Baroda, Canara Bank, Union Bank of India, and many others.</p>
  <p>If your bank is not in the supported list, use UPI or IMPS instead, as these payment rails cover all NPCI member banks regardless of net banking integration status.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/upi.html">UPI</a> - instant, app-based, no need for net banking login</li>
    <li><a href="/en/payments/imps.html">IMPS</a> - faster than NEFT for large transfers</li>
    <li><a href="/en/payments/neft.html">NEFT</a> - no transaction cap, batch settlement</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto alternative without bank dependency</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin with fast, low-cost settlement</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Net banking at 1win</h2>
  <details><summary>Which banks does 1win accept for net banking deposits?</summary><p>1win supports all major Indian banks for net banking including SBI, HDFC, ICICI, Axis, Kotak, Punjab National Bank, Bank of Baroda, and dozens of others through its payment aggregator.</p></details>
  <details><summary>How long do net banking deposits take at 1win?</summary><p>Net banking deposits route via IMPS or NEFT depending on the bank. IMPS-routed deposits arrive in 5 to 30 minutes; NEFT-routed deposits arrive in 30 to 120 minutes.</p></details>
  <details><summary>Is net banking safe for 1win deposits?</summary><p>Yes. 1win uses a PCI-compliant payment aggregator. Your bank credentials are entered on your bank's own secure login page, not on 1win's site.</p></details>
  <details><summary>What is the minimum net banking deposit at 1win?</summary><p>Minimum is 500 INR for net banking deposits.</p></details>
  <details><summary>Can I withdraw to my bank account directly via net banking from 1win?</summary><p>Withdrawals go via NEFT or IMPS directly to your registered bank account number. You do not need to log into net banking for withdrawals; you only provide your account number and IFSC code in the 1win cashier.</p></details>
</section>
"""
    html = render_page(
        slug='payments/netbanking',
        title='Net banking deposit at 1win for Indian players with XLBONUS',
        description='Deposit INR at 1win via net banking from SBI, HDFC, ICICI and 50+ Indian banks. Min 500 INR, no 1win fees. Promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Net banking deposit at 1win for Indian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Net banking', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/netbanking.html','w').write(html)


if __name__ == '__main__':
    make_upi()
    make_phonepe()
    make_googlepay()
    make_paytm()
    make_imps()
    make_neft()
    make_rupay()
    make_netbanking()
    print("India pages done: 8 files")
