# winnersclub.com — Compliance Baseline
## Sports-Betting / Online-Casino Affiliate Marketing

**Document version:** 1.0  
**Prepared:** 2026  
**Operator licence:** Curaçao 8048/JAZ (Antillephone N.V. master-licence sub-licensee / transitioning to CGA direct LOK licence)  
**Site type:** Affiliate review site promoting the 1win brand  

> **Legal caveat.** This is a practical compliance ruleset, not legal advice. Laws change rapidly. Verify jurisdiction-specific rules before publishing new content or expanding to a new market. For legally sensitive markets (UK, Germany, Italy, Netherlands), review with qualified local counsel before launch.

---

## 1. Executive Summary — Universal Compliance Baseline

Every page on winnersclub.com, regardless of language or target audience, must meet the following minimum standards. These rules are non-negotiable and apply globally before any jurisdiction-specific layering.

### 1.1 The Non-Negotiable Global Floor

| Requirement | Standard |
|---|---|
| Age gate / disclaimer | **18+ only** on all pages; "21+" addendum for markets that require it |
| Responsible-gambling statement | Must appear on every page (footer at minimum) |
| License disclosure | Curaçao 8048/JAZ licence number visible in footer |
| "Play Responsibly" call | Must be present with helpline link |
| Affiliate disclosure | "This site contains affiliate links" / "We may receive a commission" — clearly disclosed |
| No guarantee language | Absolutely no "guaranteed win", "sure bet", "risk-free" (unless genuinely risk-free with no wagering requirement) |
| No financial-solution framing | Never suggest gambling can solve debt, replace income, or provide financial security |
| No targeting of minors | No youth-culture references, no cartoon characters with minor appeal, no under-25s in gambling contexts |
| No addiction exploitation | No language suggesting gambling relieves depression, loneliness, or personal problems |

### 1.2 Why This Baseline Matters for an Unlicensed-Operator Affiliate

winnersclub.com promotes an operator (1win, Curaçao-licensed) that is not licensed in most EU, UK, or heavily-regulated markets it receives traffic from. This creates layered risk:

- **Criminal risk in some jurisdictions** (UK, Germany, Italy, Poland, France): advertising unlicensed gambling to local consumers can be a criminal offence for the advertiser, not just the operator.
- **Reputational and platform risk**: Google, Meta, and other ad platforms now enforce gambling ad policies in the EMEA that can de-index or demonetise sites promoting unlicensed operators.
- **Operator risk transfer**: Most Curaçao operator agreements hold affiliates responsible for geo-compliance of traffic they send.

The universal baseline below is designed to: (a) protect the site from the clearest legal exposure; (b) demonstrate good-faith responsible-gambling commitments; (c) be practically implementable in a single CMS template.

---

## 2. Per-Jurisdiction Compliance Matrix

### 2A. Strictly Regulated EU / European Markets

| Jurisdiction | Legal Status for Curaçao Affiliate | Required Disclaimers (MINIMUM) | Banned Words / Claims | RG Helpline to Link | Bonus Advertising Restrictions |
|---|---|---|---|---|---|
| **United Kingdom** (UKGC / ASA CAP Code) | **ILLEGAL** — advertising unlicensed operators to UK consumers is a criminal offence under the Gambling Act 2005. Unlicensed affiliates referencing UK-accessible content face ASA referral and Gambling Commission action. | N/A — should not be served to UK users. If UK traffic reaches site, must carry: "18+", "BeGambleAware.org", "Play Responsibly", operator licence disclosure | "risk-free" (if wagering req exists), "free" (if conditions apply), "guaranteed", "sure bet", anything suggesting financial security; persons appearing under 25 in gambling contexts; any content with strong appeal to under-18s | [BeGambleAware](https://www.begambleaware.org) (0808 8020 133) / [GamCare](https://www.gamcare.org.uk) (0808 8020 133) | "Free bet" only if genuinely free; full T&Cs required; wagering requirements must be prominently stated |
| **Germany** (GlüStV 2021 / GGL) | **ILLEGAL** for unlicensed operators; advertising unlicensed gambling is explicitly prohibited under GlüStV 2021. GGL actively blocks domains and blocks payment flows. | N/A — must geo-block DE traffic. If unavoidable: 18+, OASIS link, responsible gambling message occupying ≥20% visual space | Celebrity endorsement, daytime ads 06:00–21:00 (for slots/poker), "jackpot", "win big", any claim about financial gain | [Bundeszentrale für gesundheitliche Aufklärung (BZgA)](https://www.bzga.de/infomaterialien/gluecksspielsucht/) — **0800 1 37 27 00** (free) | Bonus advertising for unlicensed operators: fully prohibited |
| **Netherlands** (KSA / Kansspelautoriteit) | **ILLEGAL** — KSA actively fines affiliates promoting unlicensed operators. Untargeted gambling ads banned since July 2023. | N/A — geo-block NL. If NL traffic reaches site: 18+, Loket Kansspel, licence disclosure | Celebrity endorsements (explicitly banned by KSA for "high-risk" games including online casinos), untargeted advertising, ads reaching under-24 audiences | [Loket Kansspel](https://www.loketkansspel.nl) | All advertising must be demonstrably targeted at 24+ audiences; blanket welcome-bonus advertising effectively impossible |
| **Sweden** (Spelinspektionen / Gambling Act 2018) | **ILLEGAL** for unlicensed operators — Sweden requires a Swedish licence. Enforcement active; ISP blocking used. | N/A — geo-block SE. If SE traffic: 18+, Spelpaus.se link, "Måttfullt spel" (moderate gambling message) | Celebrity/influencer use (banned); exaggerating winning chances; gambling as lifestyle; welcome-bonus promotion beyond first-registration bonus | [Stödlinjen (Sweden)](https://www.stodlinjen.se) — **020-81 91 00** | Only one welcome bonus permitted per new player registration; further bonuses heavily restricted |
| **Italy** (ADM / Dignity Decree 2018) | **ILLEGAL** — Italy has a near-total gambling advertising ban (Dignity Decree, Law 96/2018). Affiliates are included; AGCOM has fined platforms hosting affiliate content. Italy under review for partial lift in 2025/2026 but ban remains in force as of writing. | N/A — geo-block IT. If IT traffic: informational content only ("purely informational" narrow exception may apply); NO call to action | ALL gambling advertising language; celebrity endorsement; bonus claims; anything construed as a "commercial communication" for gambling | [Giocatori Anonimi (Italy)](https://www.giocatorianonomi.it) / ADM's "Gioco Responsabile" | **ALL** bonus advertising banned |
| **Spain** (DGOJ / RD 958/2020 as modified by Supreme Court 2024) | **ILLEGAL** for unlicensed operators — DGOJ actively fines offshore operators and affiliates (€5M fines applied in H2 2024). | N/A — geo-block ES. If ES traffic: 18+, licence number, "Juega con Responsabilidad" | Sports sponsorship (still banned); ads targeting new players without verified accounts (ban reinstated via Amendment 176); celebrities currently allowed after 2024 Supreme Court ruling but Amendment 176 seeks to re-ban | [Jugarbien.es](https://www.jugarbien.es) | Welcome bonuses may only be shown to existing customers (registered 30+ days) in operator's dedicated section; new-player bonus advertising effectively banned |
| **France** (ANJ / Gambling Law 2010 + ANJ guidelines) | **ILLEGAL** for non-ANJ-licensed operators — only licensed operators (sports betting, horse racing, poker) may advertise. Online casino not licensed in France. Influencer gambling ads criminalised (€300K fine / 2 yrs imprisonment). | N/A — geo-block FR. If FR traffic: licensed operators only; ANJ-approved messaging; 18+, "Jouez responsable", ANJ hotline | Trivialising gambling; "unfounded statements on chances of winning"; equating gambling with improved social status, financial success, relationship success, glory; individuals appealing to under-18s | [Joueurs Info Service](https://www.joueurs-info-service.fr) — **09 74 75 13 13** | Strict budget caps imposed on operators; marketing spend capped annually by ANJ; no unlimited promotional arms races |
| **Poland** (Ministry of Finance / Gambling Act 2009 + 2017 amendments) | **ILLEGAL** — Poland blocks unlicensed domains (26,200+ blocked as of 2022). Only state monopoly (Totalizator Sportowy) operates online casino. Private operators limited to online sports betting with Polish licence. | N/A — geo-block PL. If PL traffic: 18+, responsible gambling warning, no call to action for casino content | Advertising of games reserved for state monopoly (online casino, slots) by private/offshore entities; cannot evoke sexual attractiveness, relaxation, professional success | [Centrum Wsparcia](https://centrumsupportu.pl) | Casino/slot advertising prohibited for non-state entities entirely |

---

### 2B. Permissive / Grey Markets

| Jurisdiction | Legal Status for Curaçao Affiliate | Required Disclaimers | Banned Words / Claims | RG Helpline | Bonus Restrictions | Risk Level |
|---|---|---|---|---|---|---|
| **India** | **NOW ILLEGAL** — India passed the Promotion and Regulation of Online Gaming Act, 2025 (August 22, 2025). Advertising online money games (including betting) is prohibited with criminal penalties (up to 2 yrs imprisonment + ₹50L fine for advertisers). Extraterritorial application. Offshore platforms blocked by MeitY (1,410+ blocks by 2025). | **Geo-block IN immediately.** Content must not be accessible to Indian users. | All gambling/betting advertising language. Celebrity endorsements criminalised. | N/A | N/A | **CRITICAL — Geo-block required** |
| **South Africa** | **RESTRICTED** — Online casino is illegal (National Gambling Act §11 bans interactive games). Online sports betting is legal only with SA provincial licence. Curaçao operators not licensed for SA. | If SA traffic served (grey area for sports betting review content only): 18+, responsible gambling message, operator licence disclosure | "Win guaranteed", financial promises, content targeting youth | [Responsible Gambling Foundation (SA)](https://www.responsiblegambling.co.za) — **0800 006 008** (free) | No welcome-bonus promotion without licensed SA operator | HIGH |
| **Nigeria** | **GREY / RESTRICTED** — NLRC requires foreign operators to hold NLRC approval or Nigerian state licence to advertise online games to Nigerian users. Curaçao licence alone insufficient for fully compliant advertising. However, enforcement is limited in practice. | 18+, NLRC-style responsible gambling message, operator licence disclosure | Fraudulent/deceptive advertising; misleading promotions | [NLRC Helpline (Nigeria)](https://www.nlrc.gov.ng) | All promotions must avoid misleading odds claims | MEDIUM-HIGH |
| **Ghana** | **GREY** — Gaming Commission of Ghana regulates; foreign operators serve via grey market. Limited advertising enforcement but regulations exist. | 18+, "Bet Responsibly", licence disclosure | False winning claims, targeting youth | [Gaming Commission Ghana](https://www.gcgghana.com) | No specific ban but misleading bonus claims prohibited | MEDIUM |
| **Kenya** | **REGULATED but GREY for Curaçao** — BCLB requires Kenyan licence. Gambling ads now require dual BCLB + KFCB approval before publication (2025 rules). Ad ban was imposed April–June 2025. | 18+, BCLB licence number (if licensed), "Not for persons under 18 years", responsible gambling message, operator contact details | Celebrity endorsements (banned), influencer testimonials, claims about money/achievement/popularity from betting | [Responsible Gambling Foundation Kenya](https://responsiblegambling.co.ke) | Each billboard max 2 gambling ads/hour; all ads require prior BCLB approval | HIGH |
| **Tanzania** | **REGULATED** — Gaming Board of Tanzania; foreign operators need Tanzania licence. Government restricted all gaming advertising in January 2019 pending Gaming Board directives. Effective advertising ban remains. | Serve only informational content if at all; 18+, responsible gambling | General gambling promotion language | [Gaming Board of Tanzania](https://www.gamingboard.go.tz) | Advertising restricted/banned pending gaming board directives | HIGH |
| **Malawi** | **GREY** — National Lotteries Board regulates; limited enforcement of online gambling. Curaçao operators operate in grey market. | 18+, responsible gambling message | False winning claims | N/A (no established national helpline) | No specific rules; apply conservative global standard | LOW-MEDIUM |
| **Brazil** | **NEWLY REGULATED** — Lei das Apostas (Law 14,790/2023) + Ordinance SPA/MF 1,231/2024 now in force. Only licensed operators (≤3 brands) may advertise. Unlicensed operators effectively banned. TV/streaming ads 7:30pm–midnight only; social media for age-verified 18+ only. | If BR traffic: 18+, responsible gambling message, licensed operator's registration number, CONAR-compliant content | Content targeting minors (including sporting events involving minors), false financial promises, advertising outside permitted hours | [SENAD Brasil / CVV](https://www.cvv.org.br) — **188** | Affiliate advertising treated as operator advertising; full operator liability | HIGH — only licensed operators |
| **Indonesia** | **ILLEGAL** — All online gambling prohibited under Indonesian law (including Sharia-based prohibitions). Government actively blocks gambling sites. | **Geo-block ID** — no content should be served | All gambling language | N/A | N/A | **CRITICAL — Geo-block** |
| **Vietnam** | **ILLEGAL** — Online gambling (casino, slots) explicitly prohibited. Online sports betting limited to licensed domestic operators only. | **Geo-block VN** for casino content | All casino/betting advertising | N/A | N/A | **CRITICAL — Geo-block casino** |
| **Philippines** | **COMPLEX** — PAGCOR-licensed operations for offshore market were phased out (POGO ban 2024). Domestic online gambling via licensed operators permitted. Curaçao operators in grey zone. | 18+, responsible gambling, operator licence | False winning claims | [PAGCOR Responsible Gambling](https://www.pagcor.ph) | Standard responsible gambling | MEDIUM-HIGH |
| **Russia** | **ILLEGAL** — Online gambling banned for unlicensed operators. Russia blocks gambling sites aggressively. CIS traffic is significant for 1win's existing user base but advertising to Russia carries risk. | If RU traffic served (current reality for 1win): 18+, responsible gambling, licence | All financial promise language | [Gambling Addiction Russia (narcologiya)](https://www.nncn.ru) | No specific rules; apply global standard | HIGH (legal) |
| **Kazakhstan** | **GREY** — Online casino prohibited but poorly enforced; online betting technically regulated. No blacklist of offshore operators. | 18+, responsible gambling | Financial promises | [Ministry of Culture and Sport KZ](https://mcs.gov.kz) | Apply global standard | MEDIUM |
| **Uzbekistan** | **ILLEGAL** — All gambling banned since 2007; sports betting legalization still not completed. | **Geo-block UZ** | All gambling language | N/A | N/A | **HIGH — consider geo-block** |
| **Tajikistan** | **ILLEGAL** — Gambling prohibited | **Geo-block TJ** | All gambling language | N/A | N/A | **HIGH — geo-block** |
| **South Korea** | **ILLEGAL** for offshore — all online gambling illegal except domestic horse/boat/cycle racing. Japan requested Curaçao block Korean users (2025). | **Geo-block KR** | All gambling language | [Korea Centre on Gambling Problems (KCGP)](https://www.kcgp.or.kr) — **1336** | N/A | **CRITICAL — Geo-block** |
| **Japan** | **ILLEGAL** — Offshore online gambling illegal under Japanese Penal Code; new 2025 law explicitly prohibits presenting websites with links to offshore casinos. Japan formally requested Curaçao block Japanese users (June 2025). | **Geo-block JP** | All gambling language | [Japan Association for the Prevention of Problem Gambling (JAPP)](https://www.japp.jp) | N/A | **CRITICAL — Geo-block required** |
| **Argentina** | **GREY/REGULATED** — Province-level regulation; 17 of 23 provinces have some online gambling framework. Buenos Aires City has regulations. Curaçao operators serve via grey market in unlicensed provinces. | 18+, responsible gambling, operator licence, "Juega con responsabilidad" | Financial promises, targeting youth | [Jugarbien Argentina](https://www.jugarbien.com.ar) | Varies by province | MEDIUM |
| **Mexico** | **GREY** — Online gambling operates without digital licences (tied to land-based licence holders). Growing market; enforcement limited. | 18+, responsible gambling, operator licence | False winning claims | [Consejo Nacional contra las Adicciones (CONADIC)](https://www.gob.mx/salud/conadic) | Apply global standard | LOW-MEDIUM |
| **Chile** | **ILLEGAL** — Online gambling illegal for offshore operators. | **Geo-block CL** | All gambling language | N/A | N/A | **HIGH** |
| **Peru** | **UNREGULATED** — No federal online gambling licensing framework in place (as of writing); Curaçao operators in grey zone. | 18+, responsible gambling, operator licence | False winning claims | [Ministerio de Salud Peru](https://www.gob.pe/minsa) | Apply global standard | LOW-MEDIUM |

---

## 3. The "Global Safe" Footer Block

This block must appear on **every page** of winnersclub.com, regardless of locale. It is the minimum compliance floor.

### 3.1 Recommended HTML/Text

```html
<!-- COMPLIANCE FOOTER — DO NOT REMOVE OR MODIFY WITHOUT LEGAL REVIEW -->
<footer class="compliance-footer">
  <div class="compliance-age-bar">
    <span class="age-icon" aria-label="18+ only">18+</span>
    <span class="play-responsibly">Play Responsibly</span>
  </div>

  <div class="compliance-body">
    <p>
      <strong>Gambling involves financial risk and may be addictive.</strong>
      Only persons aged 18 or over (21+ where applicable) are permitted to gamble.
      If you or someone you know has a gambling problem, help is available.
    </p>

    <p class="rg-links">
      <strong>Responsible Gambling Resources:</strong>
      <a href="https://www.begambleaware.org" rel="nofollow noopener" target="_blank">BeGambleAware (UK)</a> ·
      <a href="https://www.gamcare.org.uk" rel="nofollow noopener" target="_blank">GamCare (UK)</a> ·
      <a href="https://www.ncpgambling.org" rel="nofollow noopener" target="_blank">NCPG (USA)</a> ·
      <a href="https://www.gamblingtherapy.org" rel="nofollow noopener" target="_blank">Gambling Therapy (International)</a>
    </p>

    <p class="affiliate-disclosure">
      <strong>Affiliate Disclosure:</strong> winnersclub.com is an independent affiliate review website.
      We may receive a commission when you click links to operators featured on this site.
      This does not affect our editorial independence. We do not provide gambling services.
    </p>

    <p class="license-disclosure">
      <strong>Operator Licence:</strong> Games and betting services featured on this site are operated
      by 1win, licensed under Curaçao Gaming Authority Licence No. 8048/JAZ.
      This licence is issued under the laws of Curaçao (Kingdom of the Netherlands).
      Players are responsible for ensuring online gambling is legal in their jurisdiction before participating.
    </p>

    <p class="geo-warning">
      <strong>Territory Notice:</strong> Services featured on this site are not available to residents of
      the United Kingdom, Germany, Netherlands, Sweden, France, Italy, Spain, Poland, United States,
      India, Indonesia, South Korea, Japan, Vietnam, Chile, Uzbekistan, Tajikistan, or other jurisdictions
      where online gambling is prohibited or restricted.
    </p>
  </div>
</footer>
<!-- END COMPLIANCE FOOTER -->
```

### 3.2 Styling Requirements

- Footer text: minimum **12px** font size; must not be grey-on-grey or otherwise obscured
- Age badge (18+): minimum **16px**, bold, visible contrast
- Footer must appear **above** the page's final HTML closing tag on every page
- On mobile, the compliance block must not be hidden behind a "show more" accordion on first load

---

## 4. The "Global Safe" Hero-Area Disclosure

This block belongs **above the fold** on every landing page — visible without scrolling on desktop 1200px viewport and mobile 375px viewport.

### 4.1 Recommended Text

```html
<!-- HERO COMPLIANCE BAR — ABOVE THE FOLD ON ALL LANDING PAGES -->
<div class="hero-compliance-bar" role="complementary" aria-label="Responsible gambling notice">
  <span class="hero-age-badge">18+</span>
  <span class="hero-rg-text">
    Gambling can be addictive. Play responsibly.
    <a href="https://www.gamblingtherapy.org" rel="nofollow noopener" target="_blank">Get Help</a>
  </span>
  <span class="hero-license">
    Licensed: Curaçao 8048/JAZ
  </span>
</div>
<!-- END HERO COMPLIANCE BAR -->
```

### 4.2 Design Rules

- Sticky or pinned to top of viewport until user scrolls past hero section
- Background: high-contrast (dark banner or coloured strip is acceptable)
- Age badge: visually distinct — icon or bold badge format
- On bonus/promotional landing pages: add "T&Cs Apply | Wagering requirements apply | 18+ only" immediately below the bonus headline

---

## 5. Per-Country Page Recommendations

For country-specific pages (e.g., `/en/`, `/ru/`, `/br/`, `/ng/`), the following additional compliance layers apply:

### 5.1 United Kingdom (`/en-gb/` or any UK-targeted pages)

> **Recommendation: Do not create UK-targeted pages.** 1win is not UKGC-licensed. Targeting UK users via an affiliate site promoting an unlicensed operator is a criminal offence under the Gambling Act 2005.

If any UK traffic is unavoidable (organic search):
- Add a geo-redirect: UK IP → landing page stating "1win is not licensed in the UK. Please visit BeGambleAware for support: [link]."
- Do NOT include promotional content, bonus claims, or affiliate links visible to UK IPs.

### 5.2 Germany (`/de/`)

> **Recommendation: Do not create /de/ pages.** GGL actively enforces against unlicensed advertising. Google removed unlicensed gambling ads from German search in 2024.

If German SEO traffic is unavoidable:
- Add geo-redirect to responsible gambling information page
- Remove all promotional CTAs from any German-language content
- Add OASIS (self-exclusion) link and BZgA helpline prominently

### 5.3 Russia / CIS (`/ru/`)

This is likely 1win's primary existing market. Apply the following:
- **18+** badge on every page, above the fold
- "Azartные игры могут вызывать зависимость. Играйте ответственно." ("Gambling can be addictive. Play responsibly.")
- Link to Russian narcology helpline: **8-800-200-0200** (free) or international: [Gambling Therapy](https://www.gamblingtherapy.org)
- Curaçao 8048/JAZ licence disclosure in Russian
- Do NOT promise guaranteed wins, specific bonus amounts without T&Cs, or financial freedom framing
- For Kazakhstan (`/kz/`) — same requirements as RU pages

### 5.4 Nigeria / Ghana (`/ng/`, `/gh/`)

- 18+ badge prominently displayed
- "Gambling involves risk. Play responsibly. Not for persons under 18."
- Include operator's NLRC licence information if applicable
- Link to local RG resource or Gambling Therapy internationally
- Avoid celebrity/influencer-style framing (NLRC standards)

### 5.5 Kenya (`/ke/`)

- 18+ prominently displayed; "Not for persons under 18 years" (exact BCLB language)
- BCLB licence number of promoted operator (if licensed in KE)
- No celebrity endorsements
- No claims about money, achievement, or popularity from betting
- Responsible gambling message: [Responsible Gambling Foundation Kenya](https://responsiblegambling.co.ke)

### 5.6 Brazil (`/br/`)

- 18+ badge above fold
- Responsible gambling message (Portuguese): "O jogo pode causar dependência. Jogue com responsabilidade."
- Licensed operator registration number (SPA/MF No) — if 1win obtains Brazilian licence
- CVV helpline link: **188** or [cvv.org.br](https://www.cvv.org.br)
- Do NOT advertise to users under 18 or at sporting events involving minors
- Bonus claims must include full T&Cs; wagering requirements must be stated

### 5.7 India (`/in/` or `/hi/`)

> **STOP. India's Promotion and Regulation of Online Gaming Act, 2025 explicitly prohibits advertising online money games extraterritorially. Criminal penalties apply to advertisers.**

- **Geo-block all Indian IPs immediately.**
- Remove any Hindi-language promotional content.
- Do not use Indian payment methods, Indian celebrity endorsements, or Indian cricket/IPL-themed content.
- If existing Hindi content exists, either remove or convert to a non-promotional informational page with a clear notice that 1win is not available in India.

### 5.8 Korea (`/ko/`) and Japan (`/ja/`)

> **Geo-block both.** Japan formally requested Curaçao block Japanese users (June 2025) and passed new legislation targeting affiliate link sharing. Korea has total online gambling prohibition.

- Remove or restrict Korean and Japanese language pages from promotional content
- If maintaining language pages for SEO/informational purposes only: no affiliate links, no CTAs, no bonus promotion — informational content only with clear disclaimer that services are not available

### 5.9 Indonesia (`/id/`) and Vietnam (`/vi/`)

> **Geo-block. Full prohibition applies.**

### 5.10 Argentina / Mexico / Peru (`/ar/`, `/mx/`, `/pe/`)

- 18+ badge; "Juega con responsabilidad" / "Jogue com responsabilidade"
- Curaçao licence disclosure in Spanish/Portuguese
- Operator affiliate disclosure
- CONADIC link for Mexico: [gob.mx/salud/conadic](https://www.gob.mx/salud/conadic)
- No financial-freedom framing; no guaranteed win language

### 5.11 Philippines (`/ph/`)

- 18+ badge
- PAGCOR responsible gambling link
- Operator licence disclosure
- Standard responsible gambling footer

---

## 6. Banned-Words List

### 6.1 Universal (Never Use in Any Market)

These terms are prohibited on ALL pages regardless of jurisdiction:

| Category | Banned Terms / Phrases |
|---|---|
| Financial guarantees | "guaranteed win", "guaranteed profit", "sure bet", "no-lose", "risk-free bet" (unless genuinely risk-free), "certain winner", "can't miss", "100% sure", "zero risk" |
| Financial solutions | "solve your debt", "get rich quick", "financial freedom", "replace your salary", "extra income guaranteed", "pay your bills with winnings", "investing in sports" |
| Escape / therapy framing | "forget your problems", "escape from reality", "feel better", "cure boredom by gambling", "gambling therapy", "stress relief", "helps with depression" |
| Exaggerated lifestyle | "become rich overnight", "millionaire through betting", "luxury lifestyle from gambling" |
| Peer pressure | "everyone bets", "don't be left out", "join millions of winners", "only losers don't bet" |
| Youth appeal | cartoon characters appealing to under-18s; references to school, homework, teenage milestones; youth sports without appropriate context |
| Work/productivity | gambling depicted in workplace settings; "bet between meetings"; "earn while working" |
| Sexual / attractiveness | gambling linked to dating success, sexual attractiveness, becoming more popular |
| Toughness framing | "real men bet", "winners bet", "only weak people quit", recklessness glorification |

### 6.2 UK-Specific Additional Bans (ASA CAP Code)

- "Free bet" if wagering requirements apply — must say "bonus bet" or "matched bet" with T&Cs
- Any image of a person appearing under 25 in a gambling context (outside of transactional placement)
- Adolescent or loutish behaviour depicted
- Cultural beliefs about luck exploited (e.g., "lucky charm", "destiny win")
- Any personality with strong under-18 appeal (UK definition: 100,000+ under-18 followers on social platforms)

### 6.3 Germany-Specific Additional Bans

- Jackpot promotion for slots (jackpots banned for advertising)
- Any ads during 06:00–21:00 for slot/poker content
- Celebrity endorsement (prohibited under GlüStV 2021)
- Anything not linked to a GGL whitelist-licensed operator

### 6.4 Italy-Specific (Dignity Decree 2018)

- **ALL** commercial communications for gambling — the ban is near-total
- Celebrity/influencer use
- Bonus claims of any type
- Logos or references to gambling brands in non-editorial contexts

### 6.5 Netherlands-Specific

- Any content reachable by under-24 audiences for casino/high-risk games
- Celebrity endorsement for online casino products
- Untargeted advertising (TV, radio, outdoor, written media)

### 6.6 Spain-Specific

- Sports sponsorship references (still banned)
- Welcome bonus / sign-up offer promotion to new players without verified accounts (Amendment 176)
- Anonymous payment methods

### 6.7 France-Specific

- Gambling equated with improved social status, financial success, relationship success, glory, power, respect
- "Accessing services usually reserved for very wealthy people"
- Individuals under 18 or personalities where under-18s form >16% of audience
- Anyone who could be mistaken for a minor
- Influencer endorsement (criminal offence in France)

### 6.8 Sweden-Specific

- Any celebrity/influencer with under-18 appeal
- Exaggerating chances of winning
- Multiple welcome bonus promotions (only one first-registration bonus permitted)
- Gambling as alternative income or lifestyle upgrade

### 6.9 Brazil-Specific

- Advertising during prohibited hours (before 7:30pm or after midnight)
- Content at sporting events involving minors
- Promotion suggesting guaranteed financial return
- Content not meeting CONAR Annex X standards

### 6.10 India-Specific (COMPLETE BAN)

- **All gambling and betting advertising language** — criminal offence to advertise
- Celebrity endorsements of any gambling/betting platform
- Any reference to 1win or affiliated brands as gambling services available in India

---

## 7. Risk-Tier Classification

### Tier 1 — MUST Geo-Block (Illegal; Active Enforcement Risk)

Operators and affiliates face criminal penalties or immediate enforcement action in these markets. These should be geo-blocked at the IP/CDN level.

| Market | Primary Risk |
|---|---|
| 🇬🇧 United Kingdom | Criminal offence under Gambling Act 2005; UKGC enforcement; ASA referral |
| 🇩🇪 Germany | GGL enforcement, payment blocking, domain blocking, criminal liability |
| 🇮🇳 India | Online Gaming Act 2025: criminal imprisonment up to 3 years; extraterritorial application |
| 🇯🇵 Japan | New 2025 law prohibiting affiliate links to offshore casinos; formal Curaçao cooperation request |
| 🇰🇷 South Korea | Total online gambling ban; criminal penalties |
| 🇮🇩 Indonesia | Total prohibition; active site blocking |
| 🇻🇳 Vietnam | Casino/betting effectively prohibited; state-only licensed |
| 🇨🇱 Chile | Offshore online gambling illegal |
| 🇺🇿 Uzbekistan | Gambling banned since 2007 |
| 🇹🇯 Tajikistan | Gambling prohibited |

### Tier 2 — High Risk / Soft Restrict (Present Regulatory Risk; Operate Cautiously)

These markets have active regulators, meaningful enforcement, or are in the process of becoming Tier 1. Serve with maximum disclaimers; avoid promotional landing pages; consider soft geo-redirect to disclaimer.

| Market | Primary Risk |
|---|---|
| 🇳🇱 Netherlands | KSA active fines on affiliates; untargeted ad ban |
| 🇸🇪 Sweden | Spelinspektionen enforcement; ISP blocking |
| 🇮🇹 Italy | Dignity Decree; AGCOM fines; near-total advertising ban |
| 🇪🇸 Spain | DGOJ active fines (€5M+ on offshore operators H2 2024) |
| 🇫🇷 France | ANJ enforcement; influencer criminalization |
| 🇵🇱 Poland | 26,200+ blocked domains; state monopoly casino |
| 🇧🇷 Brazil | New licensing regime; unlicensed operators must comply or exit |
| 🇰🇪 Kenya | BCLB dual-approval requirement; ad ban imposed April 2025 |
| 🇹🇿 Tanzania | Government advertising restriction order (2019, still in effect) |
| 🇵🇭 Philippines | POGO ban 2024; evolving regulatory landscape |
| 🇿🇦 South Africa | Online casino illegal (NGA §11); only licensed sports betting permitted |

### Tier 3 — Operational with Enhanced Disclaimers (Grey Markets; Moderate Risk)

Curaçao operators serve these markets but without formal local licensing. Apply global floor + market-specific best practices.

| Market | Approach |
|---|---|
| 🇷🇺 Russia | 18+, RG message, licence disclosure; high-volume existing market |
| 🇰🇿 Kazakhstan | Same as Russia; grey zone for online casino |
| 🇳🇬 Nigeria | NLRC awareness; RG compliance; avoid deceptive advertising |
| 🇬🇭 Ghana | Standard 18+, RG message |
| 🇲🇼 Malawi | Standard 18+, RG message |
| 🇦🇷 Argentina | Province-level variation; 18+, RG, Curaçao licence |
| 🇲🇽 Mexico | Grey-market operation; 18+, RG |
| 🇵🇪 Peru | Unregulated; 18+, RG |

### Tier 4 — Permissive / Low Current Risk (Full Operation with Standard Disclaimers)

| Market | Notes |
|---|---|
| 🇦🇲 Armenia / 🇬🇪 Georgia | Licensed or permissive online gambling environments |
| Various LatAm (non-blocked) | Colombia (licensed), Panama, Nicaragua, Dominican Republic, Venezuela |
| Most of sub-Saharan Africa (non-blocked) | Low regulatory enforcement; apply standard compliance floor |

---

## 8. Sample Compliant vs. Non-Compliant Copy

### 8.1 Bonus Promotion

**NON-COMPLIANT ❌**
```
Get a FREE $1,000 and start winning today! Zero risk, 100% guaranteed winnings.
Join 1win and change your life. Top players earn $5,000/month!
```

**COMPLIANT ✅**
```
New players can claim up to $500 across their first four deposits.
Wagering requirements apply (35x). Full terms and conditions at 1win.com.
18+ only. Gambling involves risk. Play responsibly.
```

---

### 8.2 Aviator / Crash Game Description

**NON-COMPLIANT ❌**
```
Aviator is the EASIEST way to make money online. Players are winning thousands daily.
Never lose again with our secret strategy guide!
```

**COMPLIANT ✅**
```
Aviator is a multiplier-style game available at 1win where players set their own cash-out point.
Outcomes are random and determined by a provably fair algorithm.
There is no guaranteed winning strategy. Gambling involves risk of financial loss.
18+. Play responsibly: [Gambling Therapy](https://www.gamblingtherapy.org)
```

---

### 8.3 Sports Betting Preview

**NON-COMPLIANT ❌**
```
This is a 100% guaranteed win! Place your mortgage on this match.
Expert tipsters = free money. Use betting to pay off your loans.
```

**COMPLIANT ✅**
```
Our analysis of [Match] suggests [Team A] has strong historical form at home.
This is not guaranteed, and past performance does not predict future results.
Bet only what you can afford to lose. 18+. T&Cs apply.
```

---

### 8.4 Casino Review

**NON-COMPLIANT ❌**
```
1win Casino will make you rich! Thousands of players win every day.
Forget your job — our players earn a living from slots!
Playing online casino is totally risk-free and just for fun.
```

**COMPLIANT ✅**
```
1win Casino offers [X] slot titles, table games, and live dealer options.
Players should be aware that all casino games carry a house edge and that gambling is
not a reliable source of income. Outcomes are determined by RNG software.
18+. Licensed under Curaçao 8048/JAZ. Gambling involves financial risk.
[BeGambleAware](https://www.begambleaware.org) | [GamCare](https://www.gamcare.org.uk) | [Gambling Therapy](https://www.gamblingtherapy.org)
```

---

### 8.5 Page-Level Bonus Call-to-Action

**NON-COMPLIANT ❌**
```
CLICK HERE FOR FREE MONEY → No Risk! Everyone wins!
```

**COMPLIANT ✅**
```
Claim Welcome Bonus →
18+ | T&Cs apply | Wagering requirements: 35x | Play Responsibly
```

---

## 9. Curaçao Licence Disclosure — Exact Recommended Wording

### 9.1 Standard Footer Disclosure

```
1win is operated by [Operator Legal Name], licensed and regulated by the
Curaçao Gaming Authority (CGA) under Licence No. 8048/JAZ
(issued under the National Ordinance on Offshore Games of Chance (NOOGH),
transitioning to the National Ordinance on Games of Chance (LOK), Curaçao,
Kingdom of the Netherlands).
```

> **Note on the operator entity:** 1win's Curaçao entity should be confirmed from their licence documentation. The platform is registered in Willemstad, Curaçao. Affiliates should check 1win's current T&Cs for the current legal entity name to insert.

### 9.2 Short-Form Licence Badge (for hero bar / compact placement)

```
Curaçao Gaming Authority | Licence 8048/JAZ
```

### 9.3 18+ Symbol Placement Rules

- **Every page header or sticky navigation**: small "18+" badge (minimum 14px)
- **Every bonus CTA button or banner**: "18+" immediately adjacent to the CTA
- **Every landing page hero**: "18+" badge above the fold, minimum 16px, high contrast
- **Footer**: "18+" badge alongside the responsible gambling statement

### 9.4 "Play Responsibly" Pattern

Place in the following locations:
1. Sticky header or top navigation bar
2. Immediately below any bonus headline or CTA
3. Footer (full statement + helpline links)
4. At the end of every review article
5. On any page with bonus/promotional copy

Minimum wording: **"Play Responsibly | 18+ | Gambling can be addictive"**

Full wording for footer: **"Gambling involves financial risk and may lead to addiction. Play responsibly. Only gamble what you can afford to lose. If gambling is affecting your life, seek help: [Gambling Therapy](https://www.gamblingtherapy.org) | [GamCare](https://www.gamcare.org.uk)"**

---

## 10. Cross-Market Implementation Checklist

Use this as a deployment checklist when publishing or updating content:

### 10.1 Every Page

- [ ] 18+ badge visible above fold
- [ ] Compliance footer present with full RG block
- [ ] Curaçao 8048/JAZ licence disclosure in footer
- [ ] Affiliate relationship disclosed
- [ ] Territory exclusion notice present
- [ ] No guaranteed-win language present
- [ ] No financial-solution framing present

### 10.2 Every Bonus / Promotional Page

- [ ] Wagering requirements stated clearly and prominently
- [ ] Expiry date / time limits stated
- [ ] "T&Cs Apply" immediately adjacent to offer headline
- [ ] "18+" immediately adjacent to offer headline
- [ ] "Play Responsibly" immediately adjacent to CTA
- [ ] No "free" if conditions attach — use "bonus" or "matched"

### 10.3 Every Country-Specific Page

- [ ] Country-appropriate RG helpline linked
- [ ] Language-appropriate responsible gambling message
- [ ] Geo-check: is this market Tier 1 or Tier 2? If so, redirect/restrict
- [ ] No content targeted at known-illegal markets (India, Japan, Korea, Indonesia, etc.)

### 10.4 Technical / Site-Level

- [ ] Geo-blocking or geo-redirect in place for Tier 1 markets
- [ ] Curaçao NOO-LOK 23-country restricted list implemented at CDN/server level
- [ ] Age gate implemented (pop-up or interstitial for new visitors): "By entering this site you confirm you are 18+ and that gambling is legal in your jurisdiction"
- [ ] Google Search Console: no indexing of country-specific pages for Tier 1 markets (hreflang or robots.txt)
- [ ] Privacy policy includes data handling for player referral tracking

---

## 11. Key Sources

| Source | URL |
|---|---|
| ASA CAP Code Section 16 (Gambling) | https://www.asa.org.uk/type/non_broadcast/code_section/16.html |
| UKGC LCCP Condition 3.3.1 (RG Information) | https://www.gamblingcommission.gov.uk/licensees-and-businesses/lccp/condition/3-3-1-responsible-gambling-information |
| Germany GlüStV 2021 Overview | https://altenar.com/blog/understanding-gambling-laws-and-regulations-in-germany/ |
| Netherlands KSA Advertising Ban | https://igamingbusiness.com/legal-compliance/regulation/ksa-netherlands-annual-report-2023/ |
| Sweden Gambling Act Overview | https://altenar.com/en-us/blog/gambling-laws-and-regulations-in-sweden/ |
| Italy Dignity Decree / DLA Piper | https://www.dlapiper.com/insights/publications/2025/03/italy-to-lift-gambling-advertising-ban-a-key-moment-for-market-entry |
| Spain DGOJ / Supreme Court 2024 | https://www.imgl.org/publications/imgl-magazine-volume-3-no-1/recent-regulatory-developments-in-spain |
| France ANJ Guidelines | https://www.igamingtoday.com/france-tightens-the-screws-on-gambling-ads-ahead-of-the-2026-world-cup/ |
| Poland Gambling Act Overview | https://altenar.com/blog/gambling-laws-and-regulations-in-poland/ |
| India Online Gaming Act 2025 | https://chambers.com/articles/india-s-new-online-gaming-law-implications-for-the-gaming-ecosystem |
| India Online Gaming Act 2025 (PIB) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2115414 |
| Brazil Lei das Apostas / Chambers 2025 | https://practiceguides.chambers.com/practice-guides/gaming-law-2025/brazil |
| Brazil IBJR Advertising Guidelines | https://ibjr.org.br/en/advertising-guidelines/ |
| Nigeria NLRC Overview | https://www.mondaq.com/pdf/1416096.pdf |
| Kenya BCLB New Advertising Rules 2025 | https://sigma.world/news/kenya-introduces-stricter-rules-for-gambling-ads-after-30-day-halt/ |
| Tanzania Gaming Board Ad Restriction | https://www.gamingboard.go.tz/news/restriction-on-advertisement-of-gaming-activities-in-tanzania |
| South Africa NGB FAQ | https://www.ngb.org.za/faqs/ |
| Japan 2025 Online Gambling Law | https://asgam.com/2025/06/18/japan-asks-eight-countries-to-block-its-citizens-from-gambling-on-online-sites/ |
| Korea / Asia iGaming Legal Status | https://evenbetgaming.com/blog/from-black-markets-to-licensing-how-asia-is-redefining-online-gambling-regulation/ |
| Curaçao LOK Regulation | https://www.advennt.com/jurisdictions/online-gaming/curacao/ |
| Curaçao NOO-LOK 23-Country Restricted List | https://track360.io/blog/curacao-gaming-license-restricted-countries-operator-2026 |
| Kazakhstan / Uzbekistan Analysis | https://sbcnews.co.uk/features/2022/11/09/4h-agency-kaz-uzb-analysis/ |
| Europe Regulators Enforcement 2026 | https://www.dlapiper.com/en/insights/blogs/mse-today/2026/european-regulators-join-forces-to-combat-illegal-online-gambling |
| Global Gambling Legality Overview | https://richads.com/blog/where-is-online-gambling-legal/ |
| Celebrity Endorsement Global Analysis | https://www.imgl.org/publications/imgl-magazine-volume-3-no-1/a-global-analysis-of-celebrity-gambling-endorsement-laws/ |
| Gambling Therapy (International Helpline) | https://www.gamblingtherapy.org |
| GamCare International Contacts | https://www.gamcare.org.uk/self-help/links-to-other-support-agencies/international-support-contacts/ |
| BeGambleAware | https://www.begambleaware.org |
| NCPG (USA) | https://www.ncpgambling.org |
