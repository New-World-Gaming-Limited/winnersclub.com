"""
Generate Brazil and Pakistan payment method pages for 1win.codes
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_helpers.page_template import render_page

os.makedirs('en/payments', exist_ok=True)

# ── PIX ───────────────────────────────────────────────────────────────────────
def make_pix():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Preciso de um CPF para depositar via PIX na 1win?","acceptedAnswer":{"@type":"Answer","text":"Yes. PIX transactions in Brazil are linked to a CPF (Cadastro de Pessoas Fisicas) or CNPJ. Your PIX key at your bank is typically your CPF, mobile number, or email. You provide your PIX key to receive withdrawals."}},
    {"@type":"Question","name":"What is the minimum PIX deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum PIX deposit at 1win is R$20 (20 Brazilian Reais)."}},
    {"@type":"Question","name":"How fast is a PIX deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"PIX operates 24/7 and payments are instant. Deposits credit to your 1win wallet in under 60 seconds."}},
    {"@type":"Question","name":"Can I withdraw from 1win to my PIX key?","acceptedAnswer":{"@type":"Answer","text":"Yes. Enter your PIX key (CPF, phone, or email) in the withdrawal form. Funds arrive in your Brazilian bank account within minutes."}},
    {"@type":"Question","name":"Is there a fee for PIX transactions at 1win?","acceptedAnswer":{"@type":"Answer","text":"1win does not charge a fee for PIX deposits or withdrawals. Banco Central do Brasil mandates that PIX is free for individuals."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>PIX is Brazil's instant payment system, and 1win accepts PIX deposits and withdrawals in BRL (Brazilian Reais) on its Curaçao 8048/JAZ-licensed platform. With 400,000+ players worldwide, 1win is a trusted sports betting and casino destination. PIX operates 24/7, including weekends and public holidays, with settlement in under 60 seconds. Use promo code <span class="code-highlight">XLBONUS</span> when you register to get your welcome bonus applied to your first PIX deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: PIX at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>R$20 BRL</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>R$20,000 BRL (Banco Central limit for natural persons overnight)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant (under 60 seconds)</td></tr>
    <tr><td>Withdrawal processing time</td><td>Under 60 minutes</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>None (Banco Central mandates free PIX for individuals)</td></tr>
    <tr><td>Supported currencies</td><td>BRL</td></tr>
    <tr><td>Geographic availability</td><td>Brazil</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>Deposito via PIX na 1win: como fazer (How to deposit with PIX at 1win)</h2>
  <ol>
    <li><strong>Crie sua conta / Register your 1win account.</strong> New users: complete the registration form and enter promo code <span class="code-highlight">XLBONUS</span> to activate the welcome bonus.</li>
    <li><strong>Acesse o Caixa (Open the Cashier).</strong> Click the green "Deposit" button. The cashier panel opens.</li>
    <li><strong>Selecione PIX (Select PIX).</strong> Choose PIX from the payment method list. Enter the BRL amount you want to deposit (minimum R$20).</li>
    <li><strong>Escaneie o QR code (Scan the QR code).</strong> A PIX QR code and a copy-paste PIX key string appear on screen. Open your bank's app (Itau, Bradesco, Nubank, Caixa, BTG, or any PIX-enabled bank), navigate to "PIX," tap "Pagar via QR code," and scan the code. Alternatively, paste the PIX copy-paste key directly.</li>
    <li><strong>Confirme o pagamento (Confirm).</strong> Your 1win balance updates in under 60 seconds. A confirmation email arrives shortly after. Keep the PIX end-to-end transaction ID (E2EID) from your bank app in case you need to contact support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win via PIX</h2>
  <ol>
    <li><strong>Complete account verification.</strong> Submit CPF and a valid Brazilian ID (RG or CNH) in your 1win profile before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose PIX.</strong></li>
    <li><strong>Enter your PIX chave (key).</strong> This is typically your CPF number, registered mobile number, or email address linked to your bank account. PIX keys are case-sensitive when using email format.</li>
    <li><strong>Enter the withdrawal amount.</strong> Check that the name on the PIX key matches your 1win-registered name; mismatches can delay or reject the transfer.</li>
    <li><strong>Submit.</strong> 1win processes withdrawals within 30 to 60 minutes during business hours. PIX transfers complete in seconds on the banking side, so the total time is mostly queue-dependent on 1win's end.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Banco Central do Brasil (BCB) sets PIX limits at the individual bank level. For natural persons, the default daytime limit is R$20,000 BRL per transaction and the overnight limit (8 PM to 6 AM) is lower, typically R$1,000 BRL. You can request a limit increase through your bank's app, usually effective within 24 hours.</p>
  <p>PIX is available 24 hours a day, 7 days a week, 365 days a year. Unlike TED (which requires bank business hours) or boleto (which requires manual processing), PIX has no blackout windows. This makes it ideal for late-night deposits after a match or event you want to bet on.</p>
  <p>CPF validation: PIX keys linked to a CPF are validated by the DICT (Diretorio de Identificadores de Contas Transacionais) system. If the CPF on the PIX key does not match the name registered on your 1win account, the withdrawal may be returned. Ensure your 1win registration name exactly matches your bank account name.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>PIX is available in Brazil only, for individuals and businesses registered with Brazilian financial institutions. All transactions are in BRL. 1win's PIX integration processes payments in real time through a Brazilian payment aggregator regulated by BCB.</p>
  <p>Brazilian residents can create a PIX key using any of four key types: CPF/CNPJ, mobile phone number, email address, or an EVP (Evolutionary Virtual Key) generated by their bank. Any of these key types are accepted at 1win for withdrawals.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/boleto.html">Boleto</a> - bank slip payment, slightly slower but no real-time requirement</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto option available globally, no BRL conversion required</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin for users preferring crypto</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - e-wallet supporting BRL</li>
    <li><a href="/en/payments/visa.html">Visa card</a> - international card deposits in BRL</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: PIX at 1win</h2>
  <details><summary>Preciso de um CPF para depositar via PIX na 1win?</summary><p>Yes. PIX transactions in Brazil are linked to a CPF (Cadastro de Pessoas Fisicas) or CNPJ. Your PIX key at your bank is typically your CPF, mobile number, or email. You provide your PIX key to receive withdrawals.</p></details>
  <details><summary>What is the minimum PIX deposit at 1win?</summary><p>Minimum PIX deposit at 1win is R$20 (20 Brazilian Reais).</p></details>
  <details><summary>How fast is a PIX deposit at 1win?</summary><p>PIX operates 24/7 and payments are instant. Deposits credit to your 1win wallet in under 60 seconds.</p></details>
  <details><summary>Can I withdraw from 1win to my PIX key?</summary><p>Yes. Enter your PIX key (CPF, phone, or email) in the withdrawal form. Funds arrive in your Brazilian bank account within minutes.</p></details>
  <details><summary>Is there a fee for PIX transactions at 1win?</summary><p>1win does not charge a fee for PIX deposits or withdrawals. Banco Central do Brasil mandates that PIX is free for individuals.</p></details>
</section>
"""
    html = render_page(
        slug='payments/pix',
        title='Deposito via PIX no 1win, valido com XLBONUS',
        description='Deposite e saque em BRL na 1win com PIX. Instantaneo, sem taxas, minimo R$20. Use o codigo XLBONUS ao registrar. Licenca Curacao 8048/JAZ.',
        h1='PIX deposit at 1win for Brazilian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('PIX', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/pix.html','w').write(html)

# ── Boleto ────────────────────────────────────────────────────────────────────
def make_boleto():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"How long does a Boleto deposit take to process at 1win?","acceptedAnswer":{"@type":"Answer","text":"Boleto deposits typically take 1 to 3 business days to confirm. Unlike PIX, boleto requires bank batch processing. If you need an instant deposit, use PIX instead."}},
    {"@type":"Question","name":"What is the minimum Boleto deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Boleto deposit is R$30 BRL."}},
    {"@type":"Question","name":"Can I withdraw from 1win using Boleto?","acceptedAnswer":{"@type":"Answer","text":"No. Boleto is a deposit-only method. Withdrawals at 1win for Brazilian players are done via PIX, which sends directly to your bank account."}},
    {"@type":"Question","name":"What happens if I let my Boleto expire before paying?","acceptedAnswer":{"@type":"Answer","text":"An expired boleto cannot be paid. You will need to request a new one from the 1win cashier. Boleto expiry is typically 1 to 3 days from issuance."}},
    {"@type":"Question","name":"Does 1win charge any fee for Boleto deposits?","acceptedAnswer":{"@type":"Answer","text":"1win does not charge a fee. Some banks charge up to R$3 for processing a boleto payment; this is a bank fee, not a 1win charge."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Boleto bancario is a widely used Brazilian payment slip accepted at 1win for BRL deposits. 1win holds a Curaçao 8048/JAZ licence and has attracted 400,000+ players worldwide, including a growing Brazilian player base. Boleto works even if you do not have a credit or debit card, making it accessible to players who prefer traditional banking. Use promo code <span class="code-highlight">XLBONUS</span> at registration to get your welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Boleto at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>No (use PIX for withdrawals)</td></tr>
    <tr><td>Minimum deposit</td><td>R$30 BRL</td></tr>
    <tr><td>Maximum deposit</td><td>Varies by issuing bank, typically up to R$10,000 BRL</td></tr>
    <tr><td>Deposit processing time</td><td>1 to 3 business days</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Up to R$3 (bank-dependent)</td></tr>
    <tr><td>Supported currencies</td><td>BRL</td></tr>
    <tr><td>Geographic availability</td><td>Brazil</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Boleto at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> Click "Deposit" and select Boleto from the payment method list.</li>
    <li><strong>Enter the deposit amount.</strong> Input the BRL amount (minimum R$30). A boleto PDF or barcode is generated on screen.</li>
    <li><strong>Save or print the boleto.</strong> The boleto has a barcode and a numeric string (linha digitavel). Note the due date; boletos typically expire within 1 to 3 days.</li>
    <li><strong>Pay the boleto.</strong> You can pay via your bank's app (scan the barcode), Loteria (lottery kiosk), ATM, or any bank branch. Payment via banking app is fastest. Enter the barcode number or scan the QR code if your bank supports boleto QR.</li>
    <li><strong>Wait for processing.</strong> After payment, boleto takes 1 to 3 business days to clear. Your 1win balance updates once the bank confirms settlement. If you need funds credited faster for an upcoming event, use PIX instead.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win as a Brazilian player (not via Boleto)</h2>
  <ol>
    <li><strong>Boleto is deposit-only.</strong> For withdrawals, use PIX via the cashier withdrawal section.</li>
    <li><strong>Open the Cashier and select Withdrawal.</strong></li>
    <li><strong>Choose PIX.</strong> Enter your CPF-linked PIX key or phone number.</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm the PIX key details match your registered name.</li>
    <li><strong>Submit.</strong> PIX withdrawals process within 30 to 60 minutes from 1win's side; the actual bank transfer completes in seconds.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Boleto processing is not instant. After you pay, the clearing house (CIP or Febraban) processes the payment, which takes 1 to 2 business days at minimum. Weekend payments (Saturday or Sunday) typically do not settle until Monday or Tuesday. Public holidays add one business day each.</p>
  <p>For time-sensitive deposits, PIX is the clear superior option. Boleto is best used when you plan ahead and want to fund your 1win account days before an event or tournament.</p>
  <p>The boleto face value must exactly match the amount entered in the 1win cashier. If you pay a different amount (e.g., rounding up), the entire payment may be rejected and returned to you after 3 to 5 business days.</p>
  <p>Maximum boleto values vary by the issuing bank. Most 1win boletos cap at R$10,000 BRL per slip. For larger deposits, generate multiple boletos or use PIX or crypto.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Boleto is available in Brazil only. It is a Brazilian-specific payment instrument regulated by Febraban and Banco Central do Brasil. All boleto transactions at 1win are in BRL. Players outside Brazil cannot use boleto.</p>
  <p>Boleto is accepted at all Brazilian banks and thousands of payment kiosks (including Casas Loterica, Correios post offices, and supermarkets). It remains one of the most used payment instruments in Brazil, particularly for players who prefer not to use a bank app or do not have PIX set up.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/pix.html">PIX</a> - instant, 24/7, same day settlement for deposits and withdrawals</li>
    <li><a href="/en/payments/visa.html">Visa</a> - instant card deposit in BRL</li>
    <li><a href="/en/payments/mastercard.html">Mastercard</a> - card deposit alternative</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no boleto processing delays</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, instant settlement</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Boleto at 1win</h2>
  <details><summary>How long does a Boleto deposit take to process at 1win?</summary><p>Boleto deposits typically take 1 to 3 business days to confirm. Unlike PIX, boleto requires bank batch processing. If you need an instant deposit, use PIX instead.</p></details>
  <details><summary>What is the minimum Boleto deposit at 1win?</summary><p>Minimum Boleto deposit is R$30 BRL.</p></details>
  <details><summary>Can I withdraw from 1win using Boleto?</summary><p>No. Boleto is a deposit-only method. Withdrawals at 1win for Brazilian players are done via PIX, which sends directly to your bank account.</p></details>
  <details><summary>What happens if I let my Boleto expire before paying?</summary><p>An expired boleto cannot be paid. You will need to request a new one from the 1win cashier. Boleto expiry is typically 1 to 3 days from issuance.</p></details>
  <details><summary>Does 1win charge any fee for Boleto deposits?</summary><p>1win does not charge a fee. Some banks charge up to R$3 for processing a boleto payment; this is a bank fee, not a 1win charge.</p></details>
</section>
"""
    html = render_page(
        slug='payments/boleto',
        title='Deposito via Boleto no 1win, valido com XLBONUS',
        description='Deposite BRL na 1win via Boleto bancario. Minimo R$30, sem taxas 1win. Use o codigo XLBONUS ao registrar. Licenca Curacao 8048/JAZ.',
        h1='Boleto deposit at 1win for Brazilian players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Boleto', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/boleto.html','w').write(html)

# ── Easypaisa ─────────────────────────────────────────────────────────────────
def make_easypaisa():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is the minimum Easypaisa deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum Easypaisa deposit at 1win is PKR 500."}},
    {"@type":"Question","name":"How long does an Easypaisa deposit take?","acceptedAnswer":{"@type":"Answer","text":"Easypaisa deposits are processed instantly or within 5 minutes. Your 1win wallet reflects the balance as soon as the transaction is confirmed on Easypaisa's network."}},
    {"@type":"Question","name":"Can I withdraw from 1win to my Easypaisa account?","acceptedAnswer":{"@type":"Answer","text":"Yes. Withdrawals to Easypaisa mobile accounts are supported. Processing takes 15 minutes to 3 hours."}},
    {"@type":"Question","name":"I do not have a mobile account. Can I use Easypaisa OTC?","acceptedAnswer":{"@type":"Answer","text":"Easypaisa OTC (over-the-counter at a franchise) requires a registered mobile account to receive the funds at 1win. A full Easypaisa mobile account is needed for 1win deposits and withdrawals."}},
    {"@type":"Question","name":"Does 1win charge a fee for Easypaisa transactions?","acceptedAnswer":{"@type":"Answer","text":"1win charges no fee. Easypaisa may charge a standard wallet-to-wallet transfer fee; check the Easypaisa fee schedule in their app."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>Easypaisa is Pakistan's leading mobile money service and is accepted at 1win for PKR deposits and withdrawals. 1win operates under a Curaçao 8048/JAZ licence and serves 400,000+ players worldwide. Easypaisa and JazzCash are the two dominant payment rails for Pakistani players at 1win, covering most of the country's unbanked and mobile-first population. Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate your welcome bonus.</p>
</section>

<section class="key-facts">
  <h2>Key facts: Easypaisa at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>PKR 500</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>PKR 50,000 (Level 1 account) or PKR 200,000 (Level 2+ account)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>Easypaisa transfer fees apply; check Easypaisa fee schedule</td></tr>
    <tr><td>Supported currencies</td><td>PKR</td></tr>
    <tr><td>Geographic availability</td><td>Pakistan</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with Easypaisa at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and open the Cashier.</strong> New users: register and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select Easypaisa from the payment options.</strong> Enter the PKR amount (minimum PKR 500).</li>
    <li><strong>Note the 1win Easypaisa account number displayed.</strong> This is the recipient account number you send money to.</li>
    <li><strong>Open the Easypaisa app.</strong> Tap "Send Money," enter the 1win account number, confirm the amount. Enter your Easypaisa MPIN to authorise. Include your 1win user ID in the remarks/reference field.</li>
    <li><strong>Wait for credit.</strong> Your 1win wallet updates within 5 minutes. Keep the Easypaisa transaction ID in case you need to contact support.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to Easypaisa</h2>
  <ol>
    <li><strong>Complete identity verification.</strong> Submit your CNIC (Computerised National Identity Card) details in your 1win profile before the first withdrawal.</li>
    <li><strong>Open the Cashier and select Withdrawal. Choose Easypaisa.</strong></li>
    <li><strong>Enter your Easypaisa mobile account number.</strong> This is your registered Pakistani phone number (03XX-XXXXXXX format).</li>
    <li><strong>Enter the withdrawal amount.</strong> Confirm all details. Check that the name on your Easypaisa account matches your 1win registration.</li>
    <li><strong>Submit.</strong> 1win queues the withdrawal. Funds arrive in your Easypaisa mobile account within 15 minutes to 3 hours. An SMS from Easypaisa confirms receipt.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>Easypaisa account limits depend on your account level. Level 1 accounts (basic, with CNIC only) can hold a maximum balance of PKR 25,000 and transact up to PKR 50,000 per month. Level 2 and Level 3 accounts (full biometric verification) allow up to PKR 200,000 per transaction and PKR 500,000 per month. Upgrade your Easypaisa account level at any Telenor franchise for higher limits.</p>
    <p>Easypaisa operates 24/7. Deposits are confirmed in real time on working days; late-night transactions may take up to 10 minutes if the system is running batch reconciliation. Withdrawals from 1win to Easypaisa process within 15 minutes to 3 hours depending on 1win's payment queue.</p>
  <p>JazzCash is the other dominant Pakistani mobile money rail; if Easypaisa is temporarily unavailable, switch to JazzCash in the 1win cashier for an identical experience.</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>Easypaisa is available in Pakistan only, operated by Telenor Microfinance Bank. Transactions are in PKR exclusively. To use Easypaisa, you need a registered Easypaisa mobile account linked to a Pakistani phone number and verified with a CNIC.</p>
  <p>Easypaisa is one of the largest fintech platforms in Pakistan, with over 30 million registered accounts as of 2024. Its nationwide agent network of 450,000+ franchise points means Pakistani players can also load cash into their Easypaisa wallet at any local franchise before depositing at 1win.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/jazzcash.html">JazzCash</a> - Pakistan's other major mobile money platform</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no PKR conversion needed, geographic-agnostic</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin, low network fees</li>
    <li><a href="/en/payments/visa.html">Visa</a> - international card deposits</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - e-wallet supporting multiple currencies</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: Easypaisa at 1win</h2>
  <details><summary>What is the minimum Easypaisa deposit at 1win?</summary><p>Minimum Easypaisa deposit at 1win is PKR 500.</p></details>
  <details><summary>How long does an Easypaisa deposit take?</summary><p>Easypaisa deposits are processed instantly or within 5 minutes. Your 1win wallet reflects the balance as soon as the transaction is confirmed on Easypaisa's network.</p></details>
  <details><summary>Can I withdraw from 1win to my Easypaisa account?</summary><p>Yes. Withdrawals to Easypaisa mobile accounts are supported. Processing takes 15 minutes to 3 hours.</p></details>
  <details><summary>I do not have a mobile account. Can I use Easypaisa OTC?</summary><p>Easypaisa OTC (over-the-counter at a franchise) requires a registered mobile account to receive the funds at 1win. A full Easypaisa mobile account is needed for 1win deposits and withdrawals.</p></details>
  <details><summary>Does 1win charge a fee for Easypaisa transactions?</summary><p>1win charges no fee. Easypaisa may charge a standard wallet-to-wallet transfer fee; check the Easypaisa fee schedule in their app.</p></details>
</section>
"""
    html = render_page(
        slug='payments/easypaisa',
        title='Easypaisa deposit at 1win for Pakistani players with XLBONUS',
        description='Deposit and withdraw PKR at 1win via Easypaisa. Min PKR 500, instant deposits, no 1win fees. Use promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='Easypaisa deposit at 1win for Pakistani players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('Easypaisa', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/easypaisa.html','w').write(html)

# ── JazzCash ──────────────────────────────────────────────────────────────────
def make_jazzcash():
    faq_schema = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"What is the minimum JazzCash deposit at 1win?","acceptedAnswer":{"@type":"Answer","text":"Minimum JazzCash deposit at 1win is PKR 500."}},
    {"@type":"Question","name":"How do I deposit at 1win using JazzCash?","acceptedAnswer":{"@type":"Answer","text":"Select JazzCash in the 1win cashier, note the 1win JazzCash account number, then open the JazzCash app, select Send Money, enter the account number, amount and your MPIN. Funds credit within 5 minutes."}},
    {"@type":"Question","name":"Can I withdraw from 1win to JazzCash?","acceptedAnswer":{"@type":"Answer","text":"Yes. Provide your JazzCash registered phone number in the withdrawal form. Processing takes 15 minutes to 3 hours."}},
    {"@type":"Question","name":"What is the daily JazzCash transaction limit?","acceptedAnswer":{"@type":"Answer","text":"JazzCash Level 0 accounts have a daily limit of PKR 25,000. Level 1 accounts (CNIC verified) allow up to PKR 200,000 per day. Upgrade via biometric verification at any Jazz franchise."}},
    {"@type":"Question","name":"JazzCash vs Easypaisa at 1win. Which is better?","acceptedAnswer":{"@type":"Answer","text":"Both are functionally equivalent at 1win: same limits, same speed, same fees. Use whichever you already have. If one has a temporary outage, switch to the other in the cashier."}}
  ]
}
</script>"""

    main = """
<section class="lede">
  <p>JazzCash, operated by Jazz (formerly Mobilink), is one of the two dominant mobile payment networks in Pakistan and is fully supported at 1win for PKR deposits and withdrawals. 1win holds a Curaçao 8048/JAZ licence and has 400,000+ registered players globally. JazzCash and Easypaisa together cover the vast majority of mobile money users in Pakistan, giving Pakistani players reliable local payment options. Enter promo code <span class="code-highlight">XLBONUS</span> at registration to activate your welcome bonus on the first deposit.</p>
</section>

<section class="key-facts">
  <h2>Key facts: JazzCash at 1win</h2>
  <table class="facts-table">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td>Available for deposit</td><td>Yes</td></tr>
    <tr><td>Available for withdrawal</td><td>Yes</td></tr>
    <tr><td>Minimum deposit</td><td>PKR 500</td></tr>
    <tr><td>Maximum deposit (per transaction)</td><td>PKR 25,000 (Level 0) / PKR 200,000 (Level 1+)</td></tr>
    <tr><td>Deposit processing time</td><td>Instant to 5 minutes</td></tr>
    <tr><td>Withdrawal processing time</td><td>15 minutes to 3 hours</td></tr>
    <tr><td>1win fee</td><td>None</td></tr>
    <tr><td>Provider fee</td><td>JazzCash standard transfer fees apply</td></tr>
    <tr><td>Supported currencies</td><td>PKR</td></tr>
    <tr><td>Geographic availability</td><td>Pakistan</td></tr>
  </table>
</section>

<section class="how-to">
  <h2>How to deposit with JazzCash at 1win</h2>
  <ol>
    <li><strong>Log in to 1win and click Deposit.</strong> New users: register first and enter promo code <span class="code-highlight">XLBONUS</span>.</li>
    <li><strong>Select JazzCash from the cashier.</strong> Enter the PKR deposit amount (minimum PKR 500). The screen shows a 1win JazzCash mobile account number.</li>
    <li><strong>Open the JazzCash app on your phone.</strong> Tap "Send Money" or "Mobile Account." Enter the 1win account number as the recipient.</li>
    <li><strong>Confirm the amount and add your 1win user ID in the remarks field.</strong> Enter your JazzCash MPIN to authorise the transaction.</li>
    <li><strong>Check your 1win balance.</strong> Funds appear within 5 minutes. Note the JazzCash transaction ID from the app confirmation screen.</li>
  </ol>
</section>

<section class="how-to">
  <h2>How to withdraw from 1win to JazzCash</h2>
  <ol>
    <li><strong>Verify your identity on 1win.</strong> Submit CNIC details and a selfie in the Profile verification section before the first withdrawal.</li>
    <li><strong>Open Cashier and select Withdrawal. Choose JazzCash.</strong></li>
    <li><strong>Enter your JazzCash registered number.</strong> Format: 03XX-XXXXXXX. This must be a number with an active JazzCash mobile account.</li>
    <li><strong>Enter withdrawal amount and confirm details.</strong> The recipient name shown should match your 1win registration name.</li>
    <li><strong>Submit.</strong> 1win debits your wallet and dispatches the transfer. JazzCash credits your mobile account within 15 minutes to 3 hours. An SMS confirms receipt.</li>
  </ol>
</section>

<section class="limits-timing">
  <h2>Limits and timing</h2>
  <p>JazzCash mobile account limits depend on your KYC level. Level 0 (unverified, registered with mobile number only): maximum wallet balance PKR 25,000, daily transactions PKR 25,000. Level 1 (CNIC verified): maximum wallet balance PKR 200,000, daily transactions PKR 200,000. Level 2 (biometric verification at Jazz franchise): PKR 500,000 per month limit.</p>
  <p>To maximise your deposit and withdrawal limits at 1win via JazzCash, complete Level 1 verification by visiting any Jazz franchise with your CNIC. The process takes about 10 minutes and limits increase immediately after biometric registration.</p>
  <p>JazzCash has 99%+ uptime and operates 24/7. Deposits are real-time confirmed. Withdrawals from 1win depend on the payment queue; most process within the first hour during business hours (9 AM to 10 PM PKT).</p>
</section>

<section class="country-currency">
  <h2>Country availability and currency</h2>
  <p>JazzCash is available to Pakistani residents with a Jazz or Warid SIM. As of 2024, JazzCash has over 25 million registered accounts and 130,000+ franchise points across Pakistan. All transactions are in PKR. JazzCash is regulated by the State Bank of Pakistan (SBP) as a Branchless Banking licence holder.</p>
  <p>Non-Jazz SIM holders can also register for JazzCash using any Pakistani mobile number, though the wallet is primarily linked to Jazz/Warid numbers. Check JazzCash's website for non-Jazz registration options.</p>
</section>

<section class="alternatives">
  <h2>Alternative payment methods</h2>
  <ul>
    <li><a href="/en/payments/easypaisa.html">Easypaisa</a> - Pakistan's other major mobile wallet</li>
    <li><a href="/en/payments/bitcoin.html">Bitcoin</a> - crypto, no SBP restrictions, global access</li>
    <li><a href="/en/payments/usdt-trc20.html">USDT TRC20</a> - stablecoin with very low network fees</li>
    <li><a href="/en/payments/skrill.html">Skrill</a> - international e-wallet</li>
    <li><a href="/en/payments/visa.html">Visa</a> - card deposit if you hold an international card</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: JazzCash at 1win</h2>
  <details><summary>What is the minimum JazzCash deposit at 1win?</summary><p>Minimum JazzCash deposit at 1win is PKR 500.</p></details>
  <details><summary>How do I deposit at 1win using JazzCash?</summary><p>Select JazzCash in the 1win cashier, note the 1win JazzCash account number, then open the JazzCash app, select Send Money, enter the account number, amount and your MPIN. Funds credit within 5 minutes.</p></details>
  <details><summary>Can I withdraw from 1win to JazzCash?</summary><p>Yes. Provide your JazzCash registered phone number in the withdrawal form. Processing takes 15 minutes to 3 hours.</p></details>
  <details><summary>What is the daily JazzCash transaction limit?</summary><p>JazzCash Level 0 accounts have a daily limit of PKR 25,000. Level 1 accounts (CNIC verified) allow up to PKR 200,000 per day. Upgrade via biometric verification at any Jazz franchise.</p></details>
  <details><summary>JazzCash vs Easypaisa at 1win. Which is better?</summary><p>Both are functionally equivalent at 1win: same limits, same speed, same fees. Use whichever you already have. If one has a temporary outage, switch to the other in the cashier.</p></details>
</section>
"""
    html = render_page(
        slug='payments/jazzcash',
        title='JazzCash deposit at 1win for Pakistani players with XLBONUS',
        description='Deposit and withdraw PKR at 1win via JazzCash. Instant, min PKR 500, no 1win fees. Register with promo code XLBONUS. Curacao 8048/JAZ licensed.',
        h1='JazzCash deposit at 1win for Pakistani players',
        breadcrumbs=[('Home','/en/'), ('Payments','/en/payments/'), ('JazzCash', None)],
        main_html=main,
        extra_schema=faq_schema,
    )
    open('en/payments/jazzcash.html','w').write(html)


if __name__ == '__main__':
    make_pix()
    make_boleto()
    make_easypaisa()
    make_jazzcash()
    print("Brazil + Pakistan pages done: 4 files")
