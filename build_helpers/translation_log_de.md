# Translation Log: EN → DE
**Completed:** Saturday, 30 May 2026  
**Scope:** 184 HTML pages from `/en/` → `/de/`  
**Final audit:** `pages: 184, with issues: 0, clean: 184`

---

## Summary

| Metric | Value |
|--------|-------|
| Pages translated | 184 / 184 |
| Pages with audit issues | 0 |
| Clean pages | 184 |
| Total DE output (chars) | ~5,913,057 |
| Translation engine | pplx LLM extract (parallel, 10 workers) |
| Avg chunks per page | 1.8 |

---

## Workflow

### Phase 1 — Static structural fixes (`translate_de_bs4.py`, previously run)
Applied to all 184 files before LLM pass:
- `<html lang="en">` → `<html lang="de">`
- Canonical URL `/en/` → `/de/`
- hreflang block updated to `/de/`
- Nav, footer, meta tags translated via phrase dictionary
- JSON-LD human-readable fields translated
- GA4 snippet `G-S2MXR8D3HS` preserved exactly

### Phase 2 — LLM body translation (`translate_de_parallel.py`)
- Extracted body HTML from `</header>` to `<footer` per page (EN source)
- Split large bodies (>7,500 chars) at `</section>` boundaries
- Sent each chunk as JSONL to `pplx llm extract` with German translation instruction
- 10 concurrent workers; completed all 184 pages in ~3 batches of ~60 pages
- Reassembled: DE header/footer + LLM-translated body
- Applied post-fix regex pass after every page

### Phase 3 — Post-fix pass (`apply_post_fixes`)
Ran on every translated file:
- Em dash (—) and en dash (–) → hyphen (-)
- Banned number phrases replaced with specific figures (e.g., "Tausende von Spielen" → "11.000+ Casino-Spiele")
- Banned superlatives replaced (Weltklasse → erstklassig, hochmodern → modern)
- CTA standardization

### Phase 4 — Audit
Script: `/home/user/workspace/audit_locale.py`  
Checks: em/en dashes, XLBONUS present, Curaçao 8048/JAZ within 80 chars, banned phrases, `<html lang="de">`, GA4 tag, valid JSON-LD.  
Result: **pages: 184, with issues: 0, clean: 184**

---

## Translation Decisions

### 1. CTA standardization
EN had several CTA variants: "Register at 1win", "Sign up now", "Claim your bonus", "Get promo code".  
All mapped to the allowed DE verbs:
- "Register at 1win" → "Bei 1win registrieren"
- "Claim promo code" / "Get promo code" → "Promo-Code holen"
- "Sign up" → "Registrieren"
- "Get your bonus" → "Bonus sichern"

### 2. du-form throughout
All second-person address is informal (du/dein/dir), consistent with the EN "you/your" voice. No Sie-form appears.  
Example: "Use your promo code" → "Nutze deinen Promo-Code" (not "Verwenden Sie Ihren Promo-Code")

### 3. Compound nouns handled correctly
German requires compound nouns be written closed or hyphenated. LLM consistently produced:
- "sports betting" → "Sportwetten" (not "Sport Wetten")
- "welcome bonus" → "Willkommensbonus"
- "deposit bonus" → "Einzahlungsbonus"
- "wagering requirements" → "Umsatzbedingungen"
- "free spins" → "Freispiele"
- "promo code" → "Promo-Code" (hyphenated hybrid compound)

### 4. Specific numbers preserved, vague quantities replaced
Per the rules, "thousands of games" was replaced with the specific figure "11.000+ Casino-Spiele" rather than a direct translation of "thousands". Similarly "hundreds of providers" → "70+ Anbieter". The LLM was instructed to use specific numbers from source; post-fix regex caught any remaining "tausende"/"hunderte" patterns.

### 5. Payment/game/brand names untouched
Extensive preserve list enforced: XLBONUS, 1win, Curaçao 8048/JAZ, Aviator, JetX, Mines, Plinko, Spaceman, Hilo, Aviatrix, Lucky Drive, Visa, Mastercard, UPI, PIX, USDT, Bitcoin, Ethereum, Flutterwave, Easypaisa, Airtel Money, EcoPayz, Boleto, Neteller, Skrill, Solana, Ripple, Tron, Litecoin. Verified in sample pages — none were translated.

### 6. "Freispiele heute" page partially re-translated
`bonus/free-spins-today.html` had mixed EN/DE content after the first pass (static script had only partially covered it). Second LLM pass from clean EN source produced full German body. Same fix applied to `bonus/fourth-deposit-bonus.html`.

---

## Files Created / Modified

| File | Role |
|------|------|
| `/home/user/workspace/translate_de_bs4.py` | Static structural translator (Phase 1, prior run) |
| `/home/user/workspace/translate_de_parallel.py` | **Primary LLM translator** — parallel, 10 workers |
| `/home/user/workspace/translate_de_llm_v2.py` | Sequential LLM translator (superseded by parallel) |
| `/home/user/workspace/1win-codes-repo/de/**` | 184 translated HTML files |

---

## Preserved Elements (never translated)

- All `<script>` blocks including GA4 `G-S2MXR8D3HS` and `/exit-tracker.js`
- All `<style>` blocks
- JSON-LD `@type`, `@id`, `url`, `sameAs` fields
- HTML attributes: `class`, `id`, `data-*`, `href`, `src`, `alt` (left as-is per instruction)
- hreflang and canonical hrefs (updated `/en/` → `/de/` but not content-translated)
- All brand names, game names, payment method names listed above
