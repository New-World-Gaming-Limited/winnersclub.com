# winnersclub.com — Translation Rules (45-locale rollout, May 2026)

## Source of truth
- All translations are made FROM the English files under `/en/`.
- The EN files have just been rewritten to A+ quality (PR #2 + PR #3, branch `en/expansion-2026-05-29`). Treat the EN text as canonical.

## NEVER translate / NEVER substitute (preserve verbatim)
- The promo code: **XLBONUS** — always uppercase, never localised, never spaced.
- Numeric promises: **600%**, **200% + 150% + 100% + 50%**, **30+ sports**, **11,000+ casino games**, **12,000+ slots**, **40,000+ markets**, **400,000+ players**.
- Brand-licence string: **Curaçao 8048/JAZ**.
- Brand names: **1win**, **Pragmatic Play**, **Evolution Gaming**, **Spribe**, **Hacksaw Gaming**, **BGaming**, **Play'n GO**, **NetEnt**, **Relax Gaming**, **Aviator**, **Lucky Drive**.
- All affiliate URLs and `/link/...` paths — never alter.
- All `hreflang`, `canonical`, `lang=` attributes — script will rewrite, translator must not touch.
- All `data-*` attributes, classes, IDs, JSON-LD `@type` and `@id` values.

## NEVER use
- **em dash (—)** or **en dash (–)** — replace with regular hyphen `-` or rephrase the sentence.
- The banned phrase list (case-insensitive, in any language):
  - "HIT THE TABLES", "DOMINATE EVERY MATCH", "OUTPLAY EVERYONE"
  - "no strings attached" / equivalent localisations of the phrase
  - "BET ANYWHERE WIN EVERYWHERE"
  - "thousands of" / "hundreds of" (use specific numbers from the source)
  - "world-class", "cutting-edge", "next-generation", "state-of-the-art"

## Voice rules (preserve across locales)
- Data-led, specific, plain. Match the EN tone.
- First paragraph of every page MUST contain: brand "1win" + "XLBONUS" + a specific number from the source + "Curaçao 8048/JAZ" licence reference.
- CTA verbs allowed: Register / Claim / Open / Start / Play / Access / Get — use the locale's natural imperative equivalent.
- Numbers stay in Arabic numerals (1, 600, 11,000) in every locale **except** Arabic where Eastern Arabic numerals (١, ٦٠٠) are acceptable in body copy but ASCII numerals MUST be kept inside `<code>`/promo blocks. Default: keep ASCII everywhere.

## Per-locale notes

### RTL locales (ar, fa, he, ur)
- Add `dir="rtl"` to `<html>` tag.
- Do NOT mirror layout classes; CSS handles visual flow via logical properties.
- Keep brand names, code blocks, URLs, prices LTR (use Unicode bidi isolation if mixing).

### CJK locales
- **ja**: Polite-neutral (です/ます). No casual だ/である.
- **zh**: Simplified Chinese (zh-CN). Avoid Traditional unless explicitly noted.
- **ko**: HanGul, polite form (-ㅂ니다 / -습니다). Reminder: KO CTAs route to **playstake.io/landing?c=max3000&offer=max3000** — translator MUST preserve this URL verbatim, NOT swap to 1win.

### South Asian
- **hi**: Devanagari. Casino vocabulary uses transliterated brand names + Hindi UX terms (साइन अप करें, बोनस).
- **bn**: Bengali script. Same pattern.
- **ur**: Nastaliq Urdu, RTL.

### MENA / Turkic
- **ar**: Modern Standard Arabic (MSA), no dialect.
- **tr**: Turkish, formal.
- **fa**: Persian (Iran register), RTL.
- **uz**: Latin Uzbek (current official orthography).
- **kk**: Cyrillic Kazakh (current state register).

### Germanic / Nordic
- **de**: Standard German, du-form (not Sie) — matches casino-affiliate norm.
- **nl**: Standard Dutch.
- **da/nb/sv/fi/et**: Informal, plain.

### Romance
- **es**: Neutral Latin American Spanish (not Castilian). "Tú" form.
- **pt**: Neutral, leans Brazilian (1win's primary PT market).
- **fr**: Standard French, "tu" form.
- **it**: Standard Italian, informal.
- **ro**: Standard Romanian.
- **ca**: Standard Catalan (Barcelona/General register), informal "tu".
- **gl**: Galician (RAG normative), informal "ti".

### Slavic / Balkan
- **ru, uk, bg, sr, mk**: Cyrillic per locale (sr accepts both — use Cyrillic).
- **pl, cs, sk, sl, hr**: Latin.
- All informal register.

### Greek / Hungarian / Baltic
- **el**: Modern Greek.
- **hu**: Hungarian, informal "te".
- **lt, lv, et**: Local Latin scripts.

### SEA / Misc
- **vi**: Vietnamese with diacritics. Brand names stay Latin.
- **th**: Thai script, no spaces inside Thai words. Brand names stay Latin.
- **id, ms**: Bahasa Indonesia / Malay, formal-friendly.
- **tl**: Tagalog/Filipino, casual.
- **lo**: Lao script.
- **mn**: Cyrillic Mongolian.

## What stays English in EVERY locale
- The promo code XLBONUS itself.
- All slot/game names (Sweet Bonanza, Gates of Olympus, Aviator, JetX, Spaceman, etc.) — these are recognised brand IPs.
- All provider names (Pragmatic Play, etc.).
- Payment method brand names (Visa, Mastercard, Skrill, Neteller, USDT, Bitcoin, etc.). Local payment rails (UPI, PIX, M-Pesa) stay in their native uppercase too.
- Sport league names by convention (Premier League, La Liga, IPL, etc.) — translator's call if locale has a strong native name (e.g. "프리미어리그" is acceptable in Korean).

## Mechanical post-checks (run by audit script after every locale)
1. 0 em dashes (`—`), 0 en dashes (`–`).
2. XLBONUS appears at least once on every page (case-sensitive uppercase).
3. "Curaçao 8048/JAZ" appears at least once on every page.
4. No banned phrase string match (case-insensitive).
5. `<html lang="XX">` matches the directory locale code.
6. `hreflang` block lists all 46 locales + `x-default`.
7. `canonical` points to the locale's own URL.
8. JSON-LD validates (json.loads).
9. For RTL locales: `<html dir="rtl">` present.
10. For /ko/: every CTA href in `[playstake.io, stake.com, stake.games]` — never `/link/9efea...` or any `winnersclub.com/link/...`.
