"""
Sprint 4: Build all 7 bonus deep-dive pages + hub for 1win.codes EN site.
"""
import os, sys
sys.path.insert(0, '/home/user/workspace/1win-codes-repo')
from build_helpers.page_template import render_page

os.makedirs('en/bonus', exist_ok=True)

# ─────────────────────────────────────────────
# 1. first-deposit-bonus.html
# ─────────────────────────────────────────────

faq_first = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the 1win first deposit bonus percentage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win matches your first deposit at 200%, capped at approximately $200. Deposit $100 and you play with $300 in total credit."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a promo code for the first deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Enter promo code XLBONUS during registration or when making your first deposit to activate the 200% match offer."
      }
    },
    {
      "@type": "Question",
      "name": "What is the wagering requirement on the first deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The bonus carries a 35x wagering requirement. If you receive a $200 bonus, you need to wager $7,000 before the funds convert to withdrawable cash."
      }
    },
    {
      "@type": "Question",
      "name": "How long do I have to clear the first deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You have 30 days from the date the bonus is credited to complete the 35x wagering requirement."
      }
    },
    {
      "@type": "Question",
      "name": "Which games count toward clearing the first deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slots contribute 100% to wagering. Selected crash games including Aviator also count. Live casino and sports bets do not contribute."
      }
    }
  ]
}
</script>'''

first_html = '''
<section class="lede">
  <p>The 1win first deposit bonus doubles your opening stake with a 200% match, capped at roughly $200 equivalent, when you register with promo code <span class="code-highlight">XLBONUS</span>. The platform holds a Curacao 8048/JAZ licence and reports 400,000+ registered players globally. This guide explains exactly what you get, what the wagering math looks like, and which games let you clear the rollover most efficiently.</p>
</section>

<section class="key-facts">
  <h2>Key facts: first deposit bonus</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Match percentage</td><td>200%</td></tr>
      <tr><td>Maximum bonus (approx.)</td><td>$200 equivalent</td></tr>
      <tr><td>Minimum deposit to trigger</td><td>$10 equivalent</td></tr>
      <tr><td>Wagering requirement</td><td>35x on bonus amount</td></tr>
      <tr><td>Time limit</td><td>30 days from credit date</td></tr>
      <tr><td>Eligible games</td><td>Slots (100%), selected crash games</td></tr>
      <tr><td>Promo code required</td><td><span class="code-highlight">XLBONUS</span></td></tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to claim the first deposit bonus</h2>
  <ol>
    <li>Open an account at 1win via <a href="https://1win.codes/en/register?promo=XLBONUS">the registration page</a>. During the sign-up form, enter <span class="code-highlight">XLBONUS</span> in the promo code field.</li>
    <li>Complete your player profile and any required identity steps. 1win operates under Curacao 8048/JAZ rules, so basic KYC may apply.</li>
    <li>Navigate to the Cashier and make your first real-money deposit. The minimum qualifying deposit is approximately $10 equivalent.</li>
    <li>Confirm the deposit. The 200% bonus amount is credited to your bonus balance within a few minutes.</li>
    <li>Start wagering on eligible games. Progress shows in your account bonus tracker.</li>
  </ol>
  <div class="callout">
    <strong>Promo code reminder:</strong> If you do not enter <span class="code-highlight">XLBONUS</span> before or during your first deposit, the bonus will not activate. The code cannot be applied retroactively.
  </div>
</section>

<section class="wagering-rules">
  <h2>Wagering and rules</h2>
  <p>The bonus balance is play money until the rollover is complete. That distinction matters. Here is the honest math:</p>
  <ul>
    <li>Deposit $100, receive a $200 bonus. Total playable credit: $300.</li>
    <li>Wagering requirement: 35x the bonus amount = 35 x $200 = <strong>$7,000 in total bets</strong>.</li>
    <li>At an average slot RTP of 96%, statistical cost to clear: roughly $280 in expected losses.</li>
    <li>If you wager only on sports or live casino, those bets do not count toward rollover.</li>
    <li>Time limit: 30 days. After that, unused bonus funds are forfeited.</li>
  </ul>
  <p>Think of the bonus as a buffer that extends your play time. Whether it covers the rollover cost depends on variance, game selection, and stake size. Lower stakes spread the 35x over more spins and give RTP more time to normalise.</p>
</section>

<section class="best-games">
  <h2>Best games to use the first deposit bonus on</h2>
  <p>Focus on high-RTP slots for the most efficient clearance. 1win carries 12,000+ slots from major studios. Recommended starting points:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza by Pragmatic Play</a> (96.51% RTP) features a tumble mechanic that chains wins, keeping bet count relatively high per session.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus</a> (96.5% RTP) runs on a multiplier-powered payway format that suits medium-stake clearance runs.</li>
    <li><a href="/en/crash/aviator.html">Aviator</a> counts toward rollover in the crash game category. Cash out early and consistently rather than chasing big multipliers while clearing a bonus.</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: first deposit bonus</h2>
  <details>
    <summary>What is the 1win first deposit bonus percentage?</summary>
    <p>1win matches your first deposit at 200%, capped at approximately $200. Deposit $100 and you play with $300 in total credit.</p>
  </details>
  <details>
    <summary>Do I need a promo code for the first deposit bonus?</summary>
    <p>Yes. Enter promo code <span class="code-highlight">XLBONUS</span> during registration or when making your first deposit to activate the 200% match offer.</p>
  </details>
  <details>
    <summary>What is the wagering requirement on the first deposit bonus?</summary>
    <p>The bonus carries a 35x wagering requirement. If you receive a $200 bonus, you need to wager $7,000 before the funds convert to withdrawable cash.</p>
  </details>
  <details>
    <summary>How long do I have to clear the first deposit bonus?</summary>
    <p>You have 30 days from the date the bonus is credited to complete the 35x wagering requirement.</p>
  </details>
  <details>
    <summary>Which games count toward clearing the first deposit bonus?</summary>
    <p>Slots contribute 100% to wagering. Selected crash games including Aviator also count. Live casino and sports bets do not contribute.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/first-deposit-bonus',
    title='1win first deposit bonus: 200% match with XLBONUS',
    description='Get a 200% match on your first deposit at 1win using code XLBONUS. Max bonus approx $200. 35x wagering, 30-day window, slots eligible. Curacao 8048/JAZ licensed.',
    h1='1win first deposit bonus: 200% match',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('First deposit bonus', None)],
    main_html=first_html,
    extra_schema=faq_first,
)
open('en/bonus/first-deposit-bonus.html','w').write(html)
print('Written: first-deposit-bonus.html')

# ─────────────────────────────────────────────
# 2. second-deposit-bonus.html
# ─────────────────────────────────────────────

faq_second = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does the 1win second deposit bonus work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "After your first deposit, your second deposit at 1win receives a 150% match bonus, capped at approximately $300 equivalent, when promo code XLBONUS was used at registration."
      }
    },
    {
      "@type": "Question",
      "name": "Is the second deposit bonus automatic?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The bonus is tied to your XLBONUS registration. Your second qualifying deposit triggers it automatically, provided your account is in good standing."
      }
    },
    {
      "@type": "Question",
      "name": "What wagering applies to the second deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The same 35x wagering requirement applies. A $300 bonus means $10,500 in qualifying bets before withdrawing bonus-derived winnings."
      }
    },
    {
      "@type": "Question",
      "name": "Can I skip the first deposit bonus and go straight to the second?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The welcome package is sequential. The 150% second deposit offer activates only after the first deposit bonus has been claimed or has expired."
      }
    },
    {
      "@type": "Question",
      "name": "How long does the second deposit bonus last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "30 days from the credit date, consistent with all stages of the 1win welcome package."
      }
    }
  ]
}
</script>'''

second_html = '''
<section class="lede">
  <p>On your second deposit, 1win tops you up with a 150% match worth up to approximately $300 equivalent. This is the second stage of the welcome package activated by promo code <span class="code-highlight">XLBONUS</span>. With the platform holding a Curacao 8048/JAZ licence and serving 400,000+ registered players, the multi-stage structure is designed to extend your bankroll over several sessions rather than a single sitting.</p>
</section>

<section class="key-facts">
  <h2>Key facts: second deposit bonus</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Match percentage</td><td>150%</td></tr>
      <tr><td>Maximum bonus (approx.)</td><td>$300 equivalent</td></tr>
      <tr><td>Minimum deposit to trigger</td><td>$10 equivalent</td></tr>
      <tr><td>Wagering requirement</td><td>35x on bonus amount</td></tr>
      <tr><td>Time limit</td><td>30 days from credit date</td></tr>
      <tr><td>Eligible games</td><td>Slots (100%), selected crash games</td></tr>
      <tr><td>Stage in welcome package</td><td>2 of 4</td></tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to claim the second deposit bonus</h2>
  <ol>
    <li>Ensure you registered with <span class="code-highlight">XLBONUS</span> and have already made your first deposit. The second deposit offer activates after the first stage is triggered.</li>
    <li>Log in to your 1win account and visit the Cashier section.</li>
    <li>Make your second deposit. A minimum of roughly $10 equivalent qualifies.</li>
    <li>The 150% bonus is credited to your bonus balance automatically within a few minutes.</li>
    <li>Wager on eligible slots or qualifying crash games to clear the 35x rollover.</li>
  </ol>
  <div class="callout">
    <strong>Sequence matters:</strong> The 1win welcome package runs in order. You cannot access the second deposit match without first triggering deposit 1. If your first bonus period has lapsed without a second deposit, contact support to confirm eligibility status.
  </div>
</section>

<section class="wagering-rules">
  <h2>Wagering and rules</h2>
  <p>The second deposit bonus is bonus credit, not cash. Here is what 35x looks like at this stage:</p>
  <ul>
    <li>Maximum bonus at the $300 cap: $300 x 35 = <strong>$10,500 in required wagers</strong>.</li>
    <li>At $0.50 per slot spin (a common mid-range stake), that is 21,000 spins to clear.</li>
    <li>At $1.00 per spin, 10,500 spins over 30 days is about 350 spins per day.</li>
    <li>High-RTP slots reduce expected losses during the clearance run.</li>
    <li>Bonus funds expire after 30 days if rollover is incomplete.</li>
  </ul>
  <p>The honest read: a $300 bonus at 35x is a significant rollover. Treat it as extended play time rather than guaranteed profit. The math works in your favour only if variance runs your way or you pick games with RTP above 96%.</p>
</section>

<section class="best-games">
  <h2>Best games to use the second deposit bonus on</h2>
  <p>With a larger bonus pool to clear, game selection matters more at deposit 2. 1win hosts 12,000+ slots:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza</a> (96.51% RTP): Tumble mechanic generates high bet counts per session, useful for chipping away at a large rollover.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus</a> (96.5% RTP): Consistent mid-variance play with strong hit frequency in base game.</li>
    <li><a href="/en/crash/aviator.html">Aviator</a>: If you prefer crash games, low-multiplier auto-cashout strategies accumulate wager count efficiently.</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: second deposit bonus</h2>
  <details>
    <summary>How does the 1win second deposit bonus work?</summary>
    <p>After your first deposit, your second deposit at 1win receives a 150% match bonus, capped at approximately $300 equivalent, when promo code <span class="code-highlight">XLBONUS</span> was used at registration.</p>
  </details>
  <details>
    <summary>Is the second deposit bonus automatic?</summary>
    <p>The bonus is tied to your <span class="code-highlight">XLBONUS</span> registration. Your second qualifying deposit triggers it automatically, provided your account is in good standing.</p>
  </details>
  <details>
    <summary>What wagering applies to the second deposit bonus?</summary>
    <p>The same 35x wagering requirement applies. A $300 bonus means $10,500 in qualifying bets before withdrawing bonus-derived winnings.</p>
  </details>
  <details>
    <summary>Can I skip the first deposit bonus and go straight to the second?</summary>
    <p>No. The welcome package is sequential. The 150% second deposit offer activates only after the first deposit bonus has been claimed or has expired.</p>
  </details>
  <details>
    <summary>How long does the second deposit bonus last?</summary>
    <p>30 days from the credit date, consistent with all stages of the 1win welcome package.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/second-deposit-bonus',
    title='Second deposit at 1win: 150% top up with XLBONUS',
    description='Stage 2 of the 1win welcome package gives a 150% match on your second deposit, up to approx $300. Use code XLBONUS. 35x wagering, 30 days. Curacao 8048/JAZ licensed.',
    h1='Second deposit at 1win: 150% top up',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('Second deposit bonus', None)],
    main_html=second_html,
    extra_schema=faq_second,
)
open('en/bonus/second-deposit-bonus.html','w').write(html)
print('Written: second-deposit-bonus.html')

# ─────────────────────────────────────────────
# 3. third-deposit-bonus.html
# ─────────────────────────────────────────────

faq_third = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does the 1win third deposit bonus give me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The third deposit in the 1win welcome package earns a 150% match, capped at approximately $400 equivalent. It is activated by having registered with promo code XLBONUS."
      }
    },
    {
      "@type": "Question",
      "name": "Why is the third deposit cap higher than the second?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win structures the welcome package so the caps increase at deposits 2 and 3 to reward players who continue engaging. The third deposit cap of roughly $400 is the highest in the package."
      }
    },
    {
      "@type": "Question",
      "name": "What is the wagering on the third deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "35x the bonus amount. At the $400 cap, that is $14,000 in total qualifying wagers."
      }
    },
    {
      "@type": "Question",
      "name": "Does a payment method affect the third deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generally no, but crypto deposits may unlock additional perks on top. Check the promotions tab in your account after depositing."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if I do not complete the wagering within 30 days?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uncompleted bonus funds are forfeited at the end of the 30-day window. Your real-money balance is unaffected."
      }
    }
  ]
}
</script>'''

third_html = '''
<section class="lede">
  <p>Stage three of the 1win welcome package delivers a 150% match on your third deposit, with a cap of approximately $400 equivalent, the largest bonus ceiling in the four-stage sequence. Activate it by registering with <span class="code-highlight">XLBONUS</span> at 1win, a Curacao 8048/JAZ licensed operator with 400,000+ players worldwide. This page breaks down the math, the eligible games, and the realistic path to clearing the rollover.</p>
</section>

<section class="key-facts">
  <h2>Key facts: third deposit bonus</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Match percentage</td><td>150%</td></tr>
      <tr><td>Maximum bonus (approx.)</td><td>$400 equivalent</td></tr>
      <tr><td>Minimum deposit to trigger</td><td>$10 equivalent</td></tr>
      <tr><td>Wagering requirement</td><td>35x on bonus amount</td></tr>
      <tr><td>Time limit</td><td>30 days from credit date</td></tr>
      <tr><td>Eligible games</td><td>Slots (100%), selected crash games</td></tr>
      <tr><td>Stage in welcome package</td><td>3 of 4</td></tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to claim the third deposit bonus</h2>
  <ol>
    <li>Complete deposits 1 and 2 with their respective bonuses triggered. The package advances sequentially.</li>
    <li>Log in to 1win and head to the Cashier.</li>
    <li>Make your third qualifying deposit (minimum approximately $10 equivalent).</li>
    <li>The 150% bonus up to $400 is credited to your bonus balance automatically.</li>
    <li>Play slots or qualifying crash games to work through the 35x rollover before the 30-day timer runs out.</li>
  </ol>
  <div class="callout">
    <strong>Tip:</strong> If the third deposit cap is $400, there is no advantage to depositing more than the amount that produces a $400 bonus. At 150%, a deposit of approximately $267 is enough to hit the cap.
  </div>
</section>

<section class="wagering-rules">
  <h2>Wagering and rules</h2>
  <p>The third deposit bonus follows the same 35x structure as the earlier stages. Here is how it scales:</p>
  <ul>
    <li>Maximum bonus at cap: $400. Required wager: 35 x $400 = <strong>$14,000</strong>.</li>
    <li>At $1.00 per spin over 30 days: approximately 467 spins per day.</li>
    <li>At $2.00 per spin: roughly 233 spins per day.</li>
    <li>Statistical expected loss at 96% RTP: about $560 over the clearance run (not guaranteed).</li>
  </ul>
  <p>The $400 cap is generous in absolute terms. But the 35x rollover is also proportionally larger. Budget your session lengths accordingly and avoid jumping to high-variance slots that could bust the bonus balance before rollover completes.</p>
</section>

<section class="best-games">
  <h2>Best games to use the third deposit bonus on</h2>
  <p>At a $400 bonus, efficiency matters. Choose games with both high RTP and a manageable variance level. 1win carries 12,000+ slot titles:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza</a> (96.51% RTP): High frequency of small tumble wins keeps the balance relatively stable during the clearance run.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus</a> (96.5% RTP): The multiplier bonus can accelerate clearance if it hits during base play.</li>
    <li><a href="/en/crash/aviator.html">Aviator</a>: Crash game with 97% RTP. Auto-cashout at 1.5x to 2x builds wager count without excessive variance.</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: third deposit bonus</h2>
  <details>
    <summary>What does the 1win third deposit bonus give me?</summary>
    <p>The third deposit in the 1win welcome package earns a 150% match, capped at approximately $400 equivalent. It is activated by having registered with promo code <span class="code-highlight">XLBONUS</span>.</p>
  </details>
  <details>
    <summary>Why is the third deposit cap higher than the second?</summary>
    <p>1win structures the welcome package so the caps increase at deposits 2 and 3 to reward players who continue engaging. The third deposit cap of roughly $400 is the highest in the package.</p>
  </details>
  <details>
    <summary>What is the wagering on the third deposit bonus?</summary>
    <p>35x the bonus amount. At the $400 cap, that is $14,000 in total qualifying wagers.</p>
  </details>
  <details>
    <summary>Does a payment method affect the third deposit bonus?</summary>
    <p>Generally no, but crypto deposits may unlock additional perks on top. Check the promotions tab in your account after depositing.</p>
  </details>
  <details>
    <summary>What happens if I do not complete the wagering within 30 days?</summary>
    <p>Uncompleted bonus funds are forfeited at the end of the 30-day window. Your real-money balance is unaffected.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/third-deposit-bonus',
    title='Third deposit boost at 1win: 150% match up to $400',
    description='The 1win third deposit bonus gives 150% up to approx $400 equivalent via XLBONUS. Stage 3 of 4 in the welcome package. 35x wagering, 30 days. Curacao 8048/JAZ.',
    h1='Third deposit boost at 1win: 150% match',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('Third deposit bonus', None)],
    main_html=third_html,
    extra_schema=faq_third,
)
open('en/bonus/third-deposit-bonus.html','w').write(html)
print('Written: third-deposit-bonus.html')

# ─────────────────────────────────────────────
# 4. fourth-deposit-bonus.html
# ─────────────────────────────────────────────

faq_fourth = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the 1win fourth deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The fourth and final deposit in the 1win welcome package gives a 100% match, capped at approximately $200 equivalent, completing the total 600% welcome offer across four deposits."
      }
    },
    {
      "@type": "Question",
      "name": "What is the combined value of all four welcome deposits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The four deposits combine to a 600% welcome total: 200% + 150% + 150% + 100%, with a maximum headline value of approximately $1,100 in bonus credit."
      }
    },
    {
      "@type": "Question",
      "name": "Do all four deposits use the same XLBONUS code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. You only need to enter XLBONUS once at registration. All four deposit stages activate automatically from that single code."
      }
    },
    {
      "@type": "Question",
      "name": "What wagering applies to the fourth deposit bonus?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "35x on the bonus amount. A $200 bonus requires $7,000 in qualifying wagers to convert to withdrawable funds."
      }
    },
    {
      "@type": "Question",
      "name": "Are there any bonuses after the fourth deposit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The four-stage welcome package ends at deposit 4. After that, 1win runs ongoing reload bonuses, cashback offers, and free spin promotions for existing players."
      }
    }
  ]
}
</script>'''

fourth_html = '''
<section class="lede">
  <p>The fourth and final deposit in the 1win welcome package completes a 100% match of up to approximately $200 equivalent, closing out a 600% combined offer across four deposits. Register with <span class="code-highlight">XLBONUS</span> to activate all four stages at this Curacao 8048/JAZ licensed operator, which counts 400,000+ players in its community. This page covers the final-stage details and what to expect once the welcome period ends.</p>
</section>

<section class="key-facts">
  <h2>Key facts: fourth deposit bonus</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Match percentage</td><td>100%</td></tr>
      <tr><td>Maximum bonus (approx.)</td><td>$200 equivalent</td></tr>
      <tr><td>Minimum deposit to trigger</td><td>$10 equivalent</td></tr>
      <tr><td>Wagering requirement</td><td>35x on bonus amount</td></tr>
      <tr><td>Time limit</td><td>30 days from credit date</td></tr>
      <tr><td>Eligible games</td><td>Slots (100%), selected crash games</td></tr>
      <tr><td>Stage in welcome package</td><td>4 of 4 (final)</td></tr>
      <tr><td>Total welcome value</td><td>600% across 4 deposits, up to approx $1,100</td></tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to claim the fourth deposit bonus</h2>
  <ol>
    <li>Complete deposits 1, 2, and 3 with their respective bonuses triggered in order.</li>
    <li>Log in to 1win and go to the Cashier.</li>
    <li>Make your fourth qualifying deposit (minimum approximately $10 equivalent). To hit the $200 cap at 100% match, deposit at least $200.</li>
    <li>The 100% bonus is credited to your bonus balance automatically.</li>
    <li>Wager on eligible slots or selected crash games within the 30-day window to clear the 35x rollover.</li>
  </ol>
  <div class="callout">
    <strong>After the welcome package:</strong> Once deposit 4 is complete, ongoing promotions replace the welcome bonus. Check the 1win promotions page regularly for reload offers, free spins, and cashback deals.
  </div>
</section>

<section class="wagering-rules">
  <h2>Wagering and rules</h2>
  <p>The fourth deposit bonus mirrors the same 35x structure as the earlier stages:</p>
  <ul>
    <li>Maximum bonus: $200. Required wager: 35 x $200 = <strong>$7,000</strong>.</li>
    <li>At $0.50 per spin: 14,000 spins over 30 days, about 467 spins per day.</li>
    <li>At $1.00 per spin: 7,000 spins over 30 days, about 233 spins per day.</li>
    <li>Statistical expected loss at 96% RTP: approximately $280 in expected costs (variance dependent).</li>
  </ul>
  <p>By stage 4, you will have a clearer sense of your preferred games and average spin pace. Apply those same habits here. The $200 rollover is the smallest in the package in absolute terms, making it the most achievable final stage.</p>
</section>

<section class="best-games">
  <h2>Best games to use the fourth deposit bonus on</h2>
  <p>Stage 4 is the most approachable in terms of rollover size. Strong options across 1win's 12,000+ slot library:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza</a> (96.51% RTP): A reliable workhorse for rollover clearance with consistent base-game hits.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus</a> (96.5% RTP): Familiar if you used it for earlier stages. Bonus frequency suits consistent wagering.</li>
    <li><a href="/en/crash/aviator.html">Aviator</a>: At 97% RTP, this is one of the most efficient crash games for rollover. Set conservative auto-cashout targets.</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: fourth deposit bonus</h2>
  <details>
    <summary>What is the 1win fourth deposit bonus?</summary>
    <p>The fourth and final deposit gives a 100% match, capped at approximately $200 equivalent, completing the total 600% welcome offer across four deposits.</p>
  </details>
  <details>
    <summary>What is the combined value of all four welcome deposits?</summary>
    <p>200% + 150% + 150% + 100% = 600% total, with a maximum headline value of approximately $1,100 in bonus credit.</p>
  </details>
  <details>
    <summary>Do all four deposits use the same XLBONUS code?</summary>
    <p>Yes. Enter <span class="code-highlight">XLBONUS</span> once at registration. All four deposit stages activate automatically from that single code.</p>
  </details>
  <details>
    <summary>What wagering applies to the fourth deposit bonus?</summary>
    <p>35x on the bonus amount. A $200 bonus requires $7,000 in qualifying wagers to convert to withdrawable funds.</p>
  </details>
  <details>
    <summary>Are there any bonuses after the fourth deposit?</summary>
    <p>The four-stage welcome package ends at deposit 4. After that, 1win runs ongoing reload bonuses, cashback offers, and free spin promotions for existing players.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/fourth-deposit-bonus',
    title='Fourth deposit bonus at 1win: 100% complete the 600%',
    description='Finish the 1win welcome package with a 100% match on deposit 4, up to approx $200. Total 600% welcome value with XLBONUS. 35x wagering. Curacao 8048/JAZ licensed.',
    h1='Fourth deposit bonus at 1win: 100% complete',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('Fourth deposit bonus', None)],
    main_html=fourth_html,
    extra_schema=faq_fourth,
)
open('en/bonus/fourth-deposit-bonus.html','w').write(html)
print('Written: fourth-deposit-bonus.html')

# ─────────────────────────────────────────────
# 5. wagering-requirements.html
# ─────────────────────────────────────────────

faq_wagering = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the 1win wagering requirement multiplier?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win applies a 35x wagering requirement to all welcome bonus credit. That means for every dollar of bonus received, you must wager 35 dollars on eligible games before withdrawing."
      }
    },
    {
      "@type": "Question",
      "name": "Which games contribute 100% to wagering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slots contribute 100% toward the wagering requirement. Selected crash games including Aviator also contribute. Sports bets and live casino games do not count."
      }
    },
    {
      "@type": "Question",
      "name": "How long do I have to complete wagering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You have 30 days from the date bonus funds are credited. After 30 days, any uncleared bonus balance is forfeited."
      }
    },
    {
      "@type": "Question",
      "name": "What happens to my real-money balance during wagering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your real-money balance remains separate and fully withdrawable at any time. Wagering requirements apply only to bonus-derived funds."
      }
    },
    {
      "@type": "Question",
      "name": "Can I withdraw winnings before completing the wagering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Winnings generated from bonus funds cannot be withdrawn until the full 35x rollover is completed. Initiating a withdrawal before completion may cancel the active bonus."
      }
    }
  ]
}
</script>'''

wagering_html = '''
<section class="lede">
  <p>1win applies a 35x wagering requirement to all bonus credit, including every stage of the welcome package activated by <span class="code-highlight">XLBONUS</span>. The platform holds a Curacao 8048/JAZ licence and operates for 400,000+ registered players. This page explains exactly what 35x means in practice, which games count, and how to plan your sessions realistically.</p>
</section>

<section class="key-facts">
  <h2>Key facts: wagering requirements</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Wagering multiplier</td><td>35x on bonus amount</td></tr>
      <tr><td>Applies to</td><td>All welcome package bonus credit</td></tr>
      <tr><td>Time limit</td><td>30 days from bonus credit date</td></tr>
      <tr><td>Slots contribution</td><td>100%</td></tr>
      <tr><td>Selected crash games</td><td>100% (e.g. Aviator)</td></tr>
      <tr><td>Sports bets</td><td>0% (do not count)</td></tr>
      <tr><td>Live casino</td><td>0% (do not count)</td></tr>
    </tbody>
  </table>
</section>

<section class="worked-example">
  <h2>Worked example: clearing a $100 bonus</h2>
  <p>Suppose you receive a $100 bonus credit. Here is the full wagering picture:</p>
  <table class="facts-table">
    <thead>
      <tr><th>Stake per bet</th><th>Bets needed (35x on $100)</th><th>Days at 20 sessions/day</th></tr>
    </thead>
    <tbody>
      <tr><td>$0.20 per spin</td><td>17,500 spins</td><td>~44 days (over limit)</td></tr>
      <tr><td>$0.50 per spin</td><td>7,000 spins</td><td>~18 days</td></tr>
      <tr><td>$1.00 per spin</td><td>3,500 spins</td><td>~9 days</td></tr>
      <tr><td>$2.00 per spin</td><td>1,750 spins</td><td>~5 days</td></tr>
      <tr><td>$5.00 per spin</td><td>700 spins</td><td>~2 days</td></tr>
    </tbody>
  </table>
  <p>Total wagering required at 35x: <strong>$3,500</strong>.</p>
  <p>At an average slot RTP of 96%, the statistical expected cost to generate $3,500 in wagers is approximately $140 in house edge (4% of $3,500). That is the theoretical break-even cost of clearing the bonus, assuming perfect RTP adherence and ignoring variance.</p>
  <p>In reality, variance runs in both directions. A bonus run player can finish well above that cost or well below it. The key insight: <strong>bonus money is play money until cleared.</strong> It becomes real only when the rollover is complete.</p>
</section>

<section class="how-to">
  <h2>How the wagering clock works</h2>
  <ol>
    <li>Deposit and claim a bonus with <span class="code-highlight">XLBONUS</span>. The 35x requirement starts from the moment the bonus is credited to your account.</li>
    <li>Open the promotions or bonus tracker section in your account. 1win displays your current wagering progress in real time.</li>
    <li>Place bets on eligible games (slots or qualifying crash games). Each qualifying bet reduces the remaining rollover amount.</li>
    <li>When the tracker reaches zero, your bonus balance converts to withdrawable cash.</li>
    <li>If 30 days pass before completion, the remaining bonus balance is forfeited. Your real-money deposit balance is never at risk.</li>
  </ol>
</section>

<section class="wagering-rules">
  <h2>Common wagering pitfalls</h2>
  <ul>
    <li><strong>Betting on sports:</strong> Zero contribution. Every sports wager during a bonus period is still a sports wager, but it does not move the rollover counter.</li>
    <li><strong>High-stake volatility:</strong> Betting large amounts on high-variance slots can wipe out the bonus balance before rollover is complete. Consider mid-range stakes.</li>
    <li><strong>Withdrawing early:</strong> Requesting a withdrawal before clearing the rollover cancels the active bonus in most cases. Confirm the specific rule in your account terms.</li>
    <li><strong>Ignoring the timer:</strong> Thirty days sounds like a long time. At $0.50 per spin and 30 sessions per day, clearing a $400 bonus (35x = $14,000) still requires roughly 933 spins per session. Plan ahead.</li>
  </ul>
</section>

<section class="best-games">
  <h2>Best games for clearing wagering requirements</h2>
  <p>The goal during a rollover run is to maximise bet count while keeping the expected loss rate reasonable. 1win offers 12,000+ slots:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza</a> (96.51% RTP): Tumble wins generate extra hits per spin, increasing bet count efficiency.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus</a> (96.5% RTP): Consistent base-game hits with payway format keep the balance stable through long sessions.</li>
    <li><a href="/en/crash/aviator.html">Aviator</a> (97% RTP): The highest RTP among qualifying games. A conservative auto-cashout strategy at 1.5x to 2x accumulates wager count with the lowest expected loss rate.</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: wagering requirements</h2>
  <details>
    <summary>What is the 1win wagering requirement multiplier?</summary>
    <p>1win applies a 35x wagering requirement to all welcome bonus credit. For every dollar of bonus received, you must wager 35 dollars on eligible games before withdrawing.</p>
  </details>
  <details>
    <summary>Which games contribute 100% to wagering?</summary>
    <p>Slots contribute 100% toward the wagering requirement. Selected crash games including Aviator also contribute. Sports bets and live casino games do not count.</p>
  </details>
  <details>
    <summary>How long do I have to complete wagering?</summary>
    <p>You have 30 days from the date bonus funds are credited. After 30 days, any uncleared bonus balance is forfeited.</p>
  </details>
  <details>
    <summary>What happens to my real-money balance during wagering?</summary>
    <p>Your real-money balance remains separate and fully withdrawable at any time. Wagering requirements apply only to bonus-derived funds.</p>
  </details>
  <details>
    <summary>Can I withdraw winnings before completing the wagering?</summary>
    <p>Winnings generated from bonus funds cannot be withdrawn until the full 35x rollover is completed. Initiating a withdrawal before completion may cancel the active bonus.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/wagering-requirements',
    title='1win wagering requirements explained: 35x rollover guide',
    description='Learn how the 1win 35x wagering requirement works. Worked example: $100 bonus = $3,500 in bets. Eligible games, time limits, tips. Curacao 8048/JAZ. Use code XLBONUS.',
    h1='1win wagering requirements explained',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('Wagering requirements', None)],
    main_html=wagering_html,
    extra_schema=faq_wagering,
)
open('en/bonus/wagering-requirements.html','w').write(html)
print('Written: wagering-requirements.html')

# ─────────────────────────────────────────────
# 6. free-spins-today.html
# ─────────────────────────────────────────────

faq_freespins = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I get free spins at 1win today?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Free spins at 1win are distributed via the promo box in your account dashboard and as deposit bonuses. Crypto deposits often trigger additional free spin packages. Register with XLBONUS to access the daily promo rotation."
      }
    },
    {
      "@type": "Question",
      "name": "Do 1win free spins expire?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Free spins typically have a 24-hour to 7-day validity window depending on the source. Check the terms attached to each spin offer in your account."
      }
    },
    {
      "@type": "Question",
      "name": "Do winnings from free spins have wagering requirements?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generally yes. Winnings from free spins are credited as bonus funds subject to a wagering requirement, typically 35x the win amount. Check the specific offer terms in your account."
      }
    },
    {
      "@type": "Question",
      "name": "Which games are free spins usually valid on?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Free spins from 1win are generally tied to specific slot titles listed in the offer. They cannot be used on crash games, live casino, or sports."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get free spins without making a deposit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win occasionally offers no-deposit free spin promotions for new registrations. Check the current promotions page in your account after registering with XLBONUS."
      }
    }
  ]
}
</script>'''

freespins_html = '''
<section class="lede">
  <p>1win distributes free spins daily through its in-account promo box and as a reward for crypto deposits, giving 400,000+ registered players regular access to spin credit without an additional cash stake. Register with <span class="code-highlight">XLBONUS</span> at this Curacao 8048/JAZ licensed operator to appear in the daily promo rotation. This page explains how the system works, where to find active offers, and what the terms typically look like.</p>
</section>

<div id="daily-spins-update">Updated daily</div>

<section class="key-facts">
  <h2>Key facts: 1win free spins</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Primary distribution channel</td><td>In-account promo box</td></tr>
      <tr><td>Crypto deposit bonus</td><td>Additional free spins on qualifying crypto deposits</td></tr>
      <tr><td>Wagering on winnings</td><td>Typically 35x on spin winnings</td></tr>
      <tr><td>Spin validity</td><td>24 hours to 7 days (varies by offer)</td></tr>
      <tr><td>Eligible games</td><td>Specified slots per offer (see offer terms)</td></tr>
      <tr><td>Activation</td><td>Register with <span class="code-highlight">XLBONUS</span>, then check promo box</td></tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to access 1win free spins today</h2>
  <ol>
    <li>Register at 1win with promo code <span class="code-highlight">XLBONUS</span> or log in if you already have an account.</li>
    <li>Navigate to the Promotions or Bonuses section in your account dashboard. 1win refreshes available offers regularly, and the promo box shows your personalised active offers.</li>
    <li>Click on any active free spin offer to see which slot it applies to and the validity period.</li>
    <li>Open the eligible slot directly from the offer card. Free spins are consumed automatically when you start the session.</li>
    <li>Winnings from free spins are credited as bonus funds. The attached wagering requirement (typically 35x the win amount) applies before withdrawal.</li>
  </ol>
  <div class="callout">
    <strong>Crypto deposits and free spins:</strong> 1win runs periodic campaigns where depositing via USDT, Bitcoin, or other cryptocurrencies unlocks a free spin package on top of the standard deposit bonus. Check the promotions page immediately after a crypto deposit to claim any triggered offer.
  </div>
</section>

<section class="fallback-slots">
  <h2>Top slots to use when free spins are active</h2>
  <p>If your current free spin offer does not specify a game, or while you wait for the next daily refresh, these three slots from 1win's library of 12,000+ titles are strong default picks:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza by Pragmatic Play</a> (96.51% RTP): Frequently featured in free spin promotions. The tumble mechanic means each spin can generate multiple win evaluations, making free spins feel more valuable per credit used.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus by Pragmatic Play</a> (96.5% RTP): Another common promo slot. Multipliers accumulate during the bonus round, which is accessible even from free spin sessions.</li>
    <li><a href="/en/crash/aviator.html">Aviator by Spribe</a>: Not typically available for free spins, but a strong backup for bonus credit wagering once spin winnings need to be cleared through rollover.</li>
  </ul>
</section>

<section class="wagering-rules">
  <h2>Wagering and rules for free spin winnings</h2>
  <p>Free spin winnings are not instant cash. Here is the typical flow:</p>
  <ul>
    <li>You complete a free spin session and win, for example, $20.</li>
    <li>That $20 is credited as bonus funds, not real cash.</li>
    <li>A 35x wagering requirement applies: 35 x $20 = <strong>$700 in qualifying bets</strong> before the $20 converts.</li>
    <li>The validity clock on the winnings starts from the point they are credited, usually 30 days.</li>
    <li>Eligible games for clearing free spin winnings are the same as for deposit bonuses: slots at 100%, selected crash games.</li>
  </ul>
  <p>Low free spin win amounts produce a rollover that is easy to clear in a normal session. If you land a large win from free spins, the 35x on that larger amount can take more planning to complete before the timer expires.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: 1win free spins</h2>
  <details>
    <summary>How do I get free spins at 1win today?</summary>
    <p>Free spins at 1win are distributed via the promo box in your account dashboard and as deposit bonuses. Crypto deposits often trigger additional free spin packages. Register with <span class="code-highlight">XLBONUS</span> to access the daily promo rotation.</p>
  </details>
  <details>
    <summary>Do 1win free spins expire?</summary>
    <p>Yes. Free spins typically have a 24-hour to 7-day validity window depending on the source. Check the terms attached to each spin offer in your account.</p>
  </details>
  <details>
    <summary>Do winnings from free spins have wagering requirements?</summary>
    <p>Generally yes. Winnings from free spins are credited as bonus funds subject to a wagering requirement, typically 35x the win amount. Check the specific offer terms in your account.</p>
  </details>
  <details>
    <summary>Which games are free spins usually valid on?</summary>
    <p>Free spins from 1win are generally tied to specific slot titles listed in the offer. They cannot be used on crash games, live casino, or sports.</p>
  </details>
  <details>
    <summary>Can I get free spins without making a deposit?</summary>
    <p>1win occasionally offers no-deposit free spin promotions for new registrations. Check the current promotions page in your account after registering with <span class="code-highlight">XLBONUS</span>.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/free-spins-today',
    title='1win free spins today with XLBONUS: daily offers guide',
    description='Claim 1win free spins today via the promo box or crypto deposits. Register with XLBONUS to access the daily refresh. 35x on winnings, slots eligible. Curacao 8048/JAZ.',
    h1='1win free spins today with XLBONUS',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('Free spins today', None)],
    main_html=freespins_html,
    extra_schema=faq_freespins,
)
open('en/bonus/free-spins-today.html','w').write(html)
print('Written: free-spins-today.html')

# ─────────────────────────────────────────────
# 7. cashback-bonus.html
# ─────────────────────────────────────────────

faq_cashback = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does the 1win cashback bonus work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1win calculates net losses over a weekly or monthly cycle, then returns a percentage of those losses as cashback credit to your account. The exact rate varies by VIP tier and active promotion."
      }
    },
    {
      "@type": "Question",
      "name": "What games are eligible for 1win cashback?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slots and selected casino games are typically eligible. Sports betting losses may be covered by separate reload promotions rather than the main cashback scheme. Check your account for the current eligible games list."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a wagering requirement on cashback?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cashback credit at 1win generally carries a wagering requirement before it can be withdrawn. The standard is 35x on the cashback amount received."
      }
    },
    {
      "@type": "Question",
      "name": "When is cashback credited at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Weekly cashback is typically credited on Mondays for the prior week's activity. Monthly cashback is credited at the start of the following calendar month."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need XLBONUS to access cashback?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Registering with XLBONUS ensures you enter the promotional ecosystem and may unlock better cashback rates. Check your promotions tab after registering to see your eligible cashback tier."
      }
    }
  ]
}
</script>'''

cashback_html = '''
<section class="lede">
  <p>1win's cashback programme returns a portion of net losses to your account on weekly or monthly cycles, giving 400,000+ registered players a partial buffer against downswings. Register with <span class="code-highlight">XLBONUS</span> at this Curacao 8048/JAZ licensed operator to enter the cashback rotation. This page explains how losses are calculated, when cashback arrives, which games count, and what the wagering terms look like.</p>
</section>

<section class="key-facts">
  <h2>Key facts: cashback bonus</h2>
  <table class="facts-table">
    <thead>
      <tr><th>Detail</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>Cashback basis</td><td>Net losses over the cycle period</td></tr>
      <tr><td>Cycle options</td><td>Weekly (credited Mondays) and monthly</td></tr>
      <tr><td>Eligible games</td><td>Slots, selected casino games</td></tr>
      <tr><td>Wagering on cashback</td><td>Typically 35x on cashback amount</td></tr>
      <tr><td>Validity of cashback credit</td><td>30 days from credit date</td></tr>
      <tr><td>Rate</td><td>Varies by VIP tier and active promotion</td></tr>
      <tr><td>Activation</td><td>Register with <span class="code-highlight">XLBONUS</span></td></tr>
    </tbody>
  </table>
</section>

<section class="how-to">
  <h2>How to access cashback at 1win</h2>
  <ol>
    <li>Register at 1win using promo code <span class="code-highlight">XLBONUS</span> to enter the promotional ecosystem and see your eligible cashback rate in the promotions tab.</li>
    <li>Play eligible casino games (primarily slots) during the cashback cycle period. The platform tracks your net wins and losses in real time.</li>
    <li>At the end of the weekly or monthly cycle, 1win calculates your net loss. If you are net negative for the period, cashback applies.</li>
    <li>Cashback credit is deposited to your bonus balance automatically. Weekly cashback typically arrives on Monday mornings. Monthly cashback arrives on the first of the following month.</li>
    <li>Use the cashback credit on eligible games and clear the 35x wagering requirement within 30 days to convert it to withdrawable funds.</li>
  </ol>
  <div class="callout">
    <strong>VIP tiers and cashback rate:</strong> 1win's VIP programme increases the cashback percentage as you move up tiers. Regular high-volume players receive a better return rate than entry-level accounts. Check the VIP section in your account for your current tier and rate.
  </div>
</section>

<section class="wagering-rules">
  <h2>Wagering and rules</h2>
  <p>Cashback is not free cash in the literal sense. Here is how it works in practice:</p>
  <ul>
    <li>Suppose you lose $200 net over a week. At a 10% cashback rate, you receive $20 back as bonus credit.</li>
    <li>That $20 carries 35x wagering: 35 x $20 = <strong>$700 in qualifying bets</strong> before the $20 becomes withdrawable.</li>
    <li>The cashback does not change the underlying loss. It provides a partial stake to continue playing, not a refund.</li>
    <li>If you lose again during the cashback clearance run, those losses may count toward the next week's cashback calculation.</li>
    <li>Attempting to withdraw before clearing the wagering on cashback credit will forfeit the cashback amount.</li>
  </ul>
  <p>Cashback is most useful as a session-extender after a poor run, not as a profit mechanism. The value is that it gives you more bets for the same real-money outlay, which is genuinely useful if you stay in eligible games with high RTP.</p>
</section>

<section class="best-games">
  <h2>Best games to use cashback credit on</h2>
  <p>The same high-RTP logic applies to clearing cashback wagering as it does to deposit bonuses. From 1win's library of 12,000+ slots:</p>
  <ul>
    <li><a href="/en/slots/sweet-bonanza.html">Sweet Bonanza</a> (96.51% RTP): A steady base-game hit rate makes it efficient for working through a 35x rollover on a smaller cashback amount.</li>
    <li><a href="/en/slots/gates-of-olympus.html">Gates of Olympus</a> (96.5% RTP): Multiplier-heavy bonus rounds can convert a modest cashback balance into a meaningful sum if the feature triggers.</li>
    <li><a href="/en/crash/aviator.html">Aviator</a> (97% RTP): The lowest house edge among qualifying game types. Conservative low-multiplier cashout strategies minimise the expected cost of the rollover.</li>
  </ul>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: cashback bonus</h2>
  <details>
    <summary>How does the 1win cashback bonus work?</summary>
    <p>1win calculates net losses over a weekly or monthly cycle, then returns a percentage of those losses as cashback credit to your account. The exact rate varies by VIP tier and active promotion.</p>
  </details>
  <details>
    <summary>What games are eligible for 1win cashback?</summary>
    <p>Slots and selected casino games are typically eligible. Sports betting losses may be covered by separate reload promotions rather than the main cashback scheme. Check your account for the current eligible games list.</p>
  </details>
  <details>
    <summary>Is there a wagering requirement on cashback?</summary>
    <p>Cashback credit at 1win generally carries a wagering requirement before it can be withdrawn. The standard is 35x on the cashback amount received.</p>
  </details>
  <details>
    <summary>When is cashback credited at 1win?</summary>
    <p>Weekly cashback is typically credited on Mondays for the prior week's activity. Monthly cashback is credited at the start of the following calendar month.</p>
  </details>
  <details>
    <summary>Do I need XLBONUS to access cashback?</summary>
    <p>Registering with <span class="code-highlight">XLBONUS</span> ensures you enter the promotional ecosystem and may unlock better cashback rates. Check your promotions tab after registering to see your eligible cashback tier.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/cashback-bonus',
    title='1win cashback: weekly losses returned with XLBONUS',
    description='1win cashback returns a percentage of net losses weekly or monthly. 35x wagering on credit. Slots eligible. Register with XLBONUS. Curacao 8048/JAZ licensed operator.',
    h1='1win cashback: weekly losses returned',
    breadcrumbs=[('Home','/en/'), ('Bonuses','/en/bonus/'), ('Cashback bonus', None)],
    main_html=cashback_html,
    extra_schema=faq_cashback,
)
open('en/bonus/cashback-bonus.html','w').write(html)
print('Written: cashback-bonus.html')

# ─────────────────────────────────────────────
# 8. en/bonus/index.html (hub page)
# ─────────────────────────────────────────────

faq_hub = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the total 1win welcome bonus value?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The 1win welcome package totals 600% across four deposits, with a maximum combined value of approximately $1,100 in bonus credit when using promo code XLBONUS."
      }
    },
    {
      "@type": "Question",
      "name": "How do I activate all four deposit bonuses at 1win?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Register with promo code XLBONUS. All four deposit stages activate automatically from that single code. Make deposits in sequence to trigger each stage."
      }
    },
    {
      "@type": "Question",
      "name": "What wagering applies to 1win welcome bonuses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All stages of the welcome package carry a 35x wagering requirement on the bonus amount. You have 30 days per stage to complete the rollover on eligible slots and crash games."
      }
    },
    {
      "@type": "Question",
      "name": "Does 1win offer ongoing bonuses after the welcome package?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. After the four-deposit welcome package, 1win offers weekly cashback, free spin promotions via the promo box, and reload bonuses. XLBONUS players may also access improved VIP cashback rates."
      }
    },
    {
      "@type": "Question",
      "name": "Is 1win a licensed operator?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. 1win operates under a Curacao 8048/JAZ licence, which covers its casino and sports betting products globally."
      }
    }
  ]
}
</script>'''

hub_html = '''
<section class="lede">
  <p>1win's bonus programme starts with a 600% welcome package across four deposits, activated by promo code <span class="code-highlight">XLBONUS</span>, then continues with weekly cashback, daily free spin rotations, and ongoing reload offers. The platform holds a Curacao 8048/JAZ licence and serves 400,000+ registered players. This hub covers every bonus type available, with detailed pages for each.</p>
</section>

<section class="welcome-breakdown">
  <h2>600% welcome package breakdown</h2>
  <p>The four-deposit welcome structure is the core of 1win's new player offer. Here is how the stages stack:</p>
  <table class="facts-table">
    <thead>
      <tr>
        <th>Deposit</th>
        <th>Match %</th>
        <th>Max bonus (approx.)</th>
        <th>Wagering</th>
        <th>Time limit</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="/en/bonus/first-deposit-bonus.html">Deposit 1</a></td>
        <td>200%</td>
        <td>~$200</td>
        <td>35x</td>
        <td>30 days</td>
      </tr>
      <tr>
        <td><a href="/en/bonus/second-deposit-bonus.html">Deposit 2</a></td>
        <td>150%</td>
        <td>~$300</td>
        <td>35x</td>
        <td>30 days</td>
      </tr>
      <tr>
        <td><a href="/en/bonus/third-deposit-bonus.html">Deposit 3</a></td>
        <td>150%</td>
        <td>~$400</td>
        <td>35x</td>
        <td>30 days</td>
      </tr>
      <tr>
        <td><a href="/en/bonus/fourth-deposit-bonus.html">Deposit 4</a></td>
        <td>100%</td>
        <td>~$200</td>
        <td>35x</td>
        <td>30 days</td>
      </tr>
      <tr class="total-row">
        <td><strong>Total</strong></td>
        <td><strong>600%</strong></td>
        <td><strong>~$1,100</strong></td>
        <td>35x per stage</td>
        <td>30 days per stage</td>
      </tr>
    </tbody>
  </table>
  <p>Use promo code <span class="code-highlight">XLBONUS</span> at registration to activate all four stages. The code needs to be entered only once.</p>
</section>

<section class="bonus-cards">
  <h2>All 1win bonus pages</h2>
  <div class="card-grid">
    <div class="card">
      <h3><a href="/en/bonus/first-deposit-bonus.html">First deposit bonus</a></h3>
      <p>200% match up to approx $200. The biggest percentage in the welcome package, ideal for building an initial bankroll.</p>
    </div>
    <div class="card">
      <h3><a href="/en/bonus/second-deposit-bonus.html">Second deposit bonus</a></h3>
      <p>150% match up to approx $300. Stage 2 of 4, with the highest absolute cap after deposit 3.</p>
    </div>
    <div class="card">
      <h3><a href="/en/bonus/third-deposit-bonus.html">Third deposit bonus</a></h3>
      <p>150% match up to approx $400. The highest absolute cap in the package. Stage 3 of 4.</p>
    </div>
    <div class="card">
      <h3><a href="/en/bonus/fourth-deposit-bonus.html">Fourth deposit bonus</a></h3>
      <p>100% match up to approx $200. Completes the 600% welcome total. After this, ongoing promotions take over.</p>
    </div>
    <div class="card">
      <h3><a href="/en/bonus/wagering-requirements.html">Wagering requirements explained</a></h3>
      <p>Full guide to the 35x rollover: worked examples, eligible games, time limits, and clearance strategies.</p>
    </div>
    <div class="card">
      <h3><a href="/en/bonus/free-spins-today.html">Free spins today</a></h3>
      <p>How 1win surfaces daily free spins via the promo box and crypto deposit rewards. Updated regularly.</p>
    </div>
    <div class="card">
      <h3><a href="/en/bonus/cashback-bonus.html">Cashback bonus</a></h3>
      <p>Weekly and monthly cashback on net losses. Rates vary by VIP tier. Slots and selected casino games count.</p>
    </div>
  </div>
</section>

<section class="how-to">
  <h2>How the welcome package works in sequence</h2>
  <ol>
    <li>Register at 1win and enter <span class="code-highlight">XLBONUS</span> in the promo code field during sign-up.</li>
    <li>Make your first deposit. The 200% bonus (up to $200) is credited automatically.</li>
    <li>Clear the 35x wagering on slots within 30 days, or let it expire and proceed to stage 2.</li>
    <li>Deposit again. The 150% second deposit bonus (up to $300) activates.</li>
    <li>Continue through deposits 3 and 4 to collect the full 600% welcome value.</li>
    <li>After deposit 4, access the cashback programme and daily free spin rotation via your promotions tab.</li>
  </ol>
</section>

<section class="wagering-rules">
  <h2>Honest assessment of the wagering</h2>
  <p>Every bonus at 1win is play money until the 35x rollover is cleared. That is not unusual in online casino terms, but it is worth stating plainly. Here is what the math looks like across the full welcome package:</p>
  <ul>
    <li>Maximum total bonus credit: approximately $1,100.</li>
    <li>Total wagering required to clear all four stages: 35 x $1,100 = <strong>$38,500 in qualifying bets</strong>.</li>
    <li>At an average 96% RTP, the statistical expected cost: roughly $1,540 in house edge over the full clearance run.</li>
    <li>That cost is not guaranteed. Variance means some players clear well ahead of expectation; others do not reach it.</li>
  </ul>
  <p>The bonus is real value if you were planning to play regardless. It extends your session time and gives you more bets for the same outlay. Approach it with a stake size that lets you sustain the rollover over the 30-day window per stage.</p>
</section>

<section class="cta">
  <a class="btn btn-primary btn-lg" href="https://1win.codes/en/register?promo=XLBONUS">Register at 1win and claim XLBONUS</a>
</section>

<section class="faq">
  <h2>FAQ: 1win bonuses</h2>
  <details>
    <summary>What is the total 1win welcome bonus value?</summary>
    <p>The 1win welcome package totals 600% across four deposits, with a maximum combined value of approximately $1,100 in bonus credit when using promo code <span class="code-highlight">XLBONUS</span>.</p>
  </details>
  <details>
    <summary>How do I activate all four deposit bonuses at 1win?</summary>
    <p>Register with promo code <span class="code-highlight">XLBONUS</span>. All four deposit stages activate automatically from that single code. Make deposits in sequence to trigger each stage.</p>
  </details>
  <details>
    <summary>What wagering applies to 1win welcome bonuses?</summary>
    <p>All stages of the welcome package carry a 35x wagering requirement on the bonus amount. You have 30 days per stage to complete the rollover on eligible slots and crash games.</p>
  </details>
  <details>
    <summary>Does 1win offer ongoing bonuses after the welcome package?</summary>
    <p>Yes. After the four-deposit welcome package, 1win offers weekly cashback, free spin promotions via the promo box, and reload bonuses. <span class="code-highlight">XLBONUS</span> players may also access improved VIP cashback rates.</p>
  </details>
  <details>
    <summary>Is 1win a licensed operator?</summary>
    <p>Yes. 1win operates under a Curacao 8048/JAZ licence, which covers its casino and sports betting products globally.</p>
  </details>
</section>
'''

html = render_page(
    slug='bonus/',
    title='1win bonus guide: 600% welcome offer with XLBONUS explained',
    description='Full guide to 1win bonuses: 600% welcome across 4 deposits, free spins, cashback. Use XLBONUS at registration. 35x wagering, 30 days per stage. Curacao 8048/JAZ.',
    h1='1win bonus guide: 600% welcome package and beyond',
    breadcrumbs=[('Home','/en/'), ('Bonuses', None)],
    main_html=hub_html,
    extra_schema=faq_hub,
)
open('en/bonus/index.html','w').write(html)
print('Written: index.html')

print('\nAll 8 bonus pages written successfully.')
