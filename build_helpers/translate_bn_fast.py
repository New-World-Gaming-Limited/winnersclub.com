#!/usr/bin/env python3
"""
Fast Bengali (bn) translation script for 1win.codes
Uses batched newline-separated translation: ~1-2 API calls per file.
"""
import os
import re
import sys
import time
import json
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag
from deep_translator import GoogleTranslator

REPO = Path("/home/user/workspace/1win-codes-repo")
EN_DIR = REPO / "en"
BN_DIR = REPO / "bn"
INVENTORY = REPO / "build_helpers" / "en_page_inventory.txt"

translator = GoogleTranslator(source="en", target="bn")

# Terms to preserve verbatim (sorted longest-first for safe replacement)
PRESERVE = sorted([
    "XLBONUS", "1win", "Curaçao 8048/JAZ", "8048/JAZ", "Curaçao",
    "Pragmatic Play", "Evolution Gaming", "Spribe", "Hacksaw Gaming",
    "BGaming", "Play'n GO", "NetEnt", "Relax Gaming", "Aviator",
    "Lucky Drive", "JetX", "Spaceman", "Aviatrix", "Plinko", "Mines", "HiLo",
    "Sweet Bonanza", "Gates of Olympus", "Book of Dead", "Starburst",
    "Big Bass Bonanza", "Wolf Gold", "Fruit Party", "Sugar Rush 1000",
    "Dog House Megaways", "Dog House", "Reactoonz", "Fire Joker",
    "Buffalo King Megaways", "Extra Juicy Megaways", "Money Train 4",
    "Razor Shark", "Rise of Olympus 100", "Cash Elevator",
    "Gonzo's Quest", "Wanted Dead or a Wild",
    "bKash", "Nagad", "Rocket",
    "UPI", "PIX", "M-Pesa", "M-PESA",
    "Visa", "Mastercard", "Skrill", "Neteller", "USDT", "Bitcoin",
    "Ethereum", "Litecoin", "Tether", "Tron", "Dogecoin", "Solana",
    "Ripple", "USDT-ERC20", "USDT-TRC20", "IMPS", "NEFT",
    "PhonePe", "Paytm", "RuPay", "Google Pay", "MuchBetter", "ecoPayz",
    "Flutterwave", "Airtel Money", "MTN MoMo", "Orange Money",
    "JazzCash", "EasyPaisa", "Boleto", "Maestro",
    "Premier League", "La Liga", "IPL", "UEFA Champions League",
    "NBA", "NFL", "ICC", "ATP", "WTA",
    "GamCare", "SSL",
    "Android", "iOS",
    "AviaMasters", "Aviamasters", "Gamzix", "Mancala Gaming",
    "1win.codes", "1win.pro", "1win.com",
    "Esports", "esports",
], key=len, reverse=True)

BANNED_BN = [
    "হাজার হাজার", "শত শত", "বিশ্বমানের", "অত্যাধুনিক",
    "পরবর্তী প্রজন্মের", "সর্বশেষ",
]
BN_REPLACEMENTS = {
    "সর্বশেষ": "সাম্প্রতিক",
    "অত্যাধুনিক": "উন্নত",
    "বিশ্বমানের": "উচ্চমানের",
    "পরবর্তী প্রজন্মের": "নতুন",
    "হাজার হাজার": "হাজারো",
    "শত শত": "শতাধিক",
}

NO_TRANSLATE_TAGS = {"script", "style", "code", "pre", "svg", "path"}
TRANSLATE_ATTRS = {"alt", "aria-label"}

# Shared translation cache across all files
_CACHE = {}
_STATS = {'api_calls': 0}

LOCALES = [
    "ar","bg","bn","cs","da","de","el","en","es","et","fa","fi",
    "fr","he","hi","hr","hu","id","it","ja","kk","ko","lo","lt",
    "lv","mn","ms","mt","nb","nl","pl","pt","ro","ru","sk","sl",
    "sq","sr","sv","th","tl","tr","uk","ur","uz","vi","zh",
]


def protect(text: str) -> tuple[str, dict]:
    """Protect URLs and preserve terms. Returns (protected_text, reverse_map)."""
    pmap = {}
    counter = [0]

    def make_ph(val):
        ph = f"BPPH{counter[0]:04d}BP"
        counter[0] += 1
        pmap[ph] = val
        return ph

    t = text.replace("—", " - ").replace("–", " - ")
    # Protect URLs
    t = re.sub(r"https?://\S+|/link/\S+", lambda m: make_ph(m.group()), t)
    # Protect preserved terms
    for term in PRESERVE:
        if term in t:
            t = t.replace(term, make_ph(term))
    # Protect percentages
    t = re.sub(r"\d[\d,]*%", lambda m: make_ph(m.group()), t)
    return t, pmap


def restore(text: str, pmap: dict) -> str:
    for ph, val in pmap.items():
        text = text.replace(ph, val)
    return text


def batch_translate(texts):
    """Translate a batch of strings using newline-separated API call."""
    

    if not texts:
        return []

    # Split into sub-batches of 5000 chars max
    results = []
    batch = []
    batch_pmaps = []
    batch_len = 0

    def flush_batch():
        nonlocal batch, batch_pmaps, batch_len
        if not batch:
            return
        joined = "\n".join(batch)
        try:
            _STATS['api_calls'] += 1
            translated = translator.translate(joined)
            if not translated:
                translated = joined
            time.sleep(0.05)
        except Exception as e:
            print(f"  [WARN] Translate error: {e}")
            translated = joined

        parts = translated.split("\n")
        # Pad if fewer parts returned
        while len(parts) < len(batch):
            parts.append("")

        for i, part in enumerate(parts[:len(batch)]):
            restored = restore(part.strip(), batch_pmaps[i])
            # Apply BN replacements
            for bad, good in BN_REPLACEMENTS.items():
                restored = restored.replace(bad, good)
            results.append(restored)

        batch.clear()
        batch_pmaps.clear()
        batch_len = 0

    for text in texts:
        p_text, pmap = protect(text.strip())
        if batch_len + len(p_text) + 1 > 4500 or len(batch) >= 30:
            flush_batch()
        batch.append(p_text)
        batch_pmaps.append(pmap)
        batch_len += len(p_text) + 1

    flush_batch()
    return results


def collect_text_nodes(soup_node):
    """Collect all translatable text nodes (NavigableString objects)."""
    nodes = []

    def _collect(node):
        if isinstance(node, NavigableString):
            for p in node.parents:
                if hasattr(p, "name") and p.name in NO_TRANSLATE_TAGS:
                    return
            text = str(node)
            if text.strip() and re.search(r"[a-zA-Z]", text):
                nodes.append(node)
        elif isinstance(node, Tag):
            if node.name in NO_TRANSLATE_TAGS:
                return
            for child in list(node.children):
                _collect(child)

    _collect(soup_node)
    return nodes


def translate_soup(soup: BeautifulSoup) -> BeautifulSoup:
    """Translate all text content in a BeautifulSoup object."""
    # Collect all text nodes from body + head (title, meta)
    all_nodes = []
    if soup.body:
        all_nodes += collect_text_nodes(soup.body)

    # Collect raw texts
    raw_texts = [str(n) for n in all_nodes]

    # Batch translate (using cache)
    new_texts = []
    uncached_indices = []
    uncached_texts = []

    for i, text in enumerate(raw_texts):
        stripped = text.strip()
        if stripped in _CACHE:
            new_texts.append(None)  # placeholder
        else:
            new_texts.append(None)
            uncached_indices.append(i)
            uncached_texts.append(stripped)

    # Translate uncached
    if uncached_texts:
        translated_batch = batch_translate(uncached_texts)
        for i, (orig_idx, trans) in enumerate(zip(uncached_indices, translated_batch)):
            orig_text = uncached_texts[i]
            _CACHE[orig_text] = trans

    # Apply translations
    for i, node in enumerate(all_nodes):
        stripped = raw_texts[i].strip()
        if stripped in _CACHE:
            translated = _CACHE[stripped]
            # Preserve leading/trailing whitespace
            prefix = raw_texts[i][: len(raw_texts[i]) - len(raw_texts[i].lstrip())]
            suffix = raw_texts[i][len(raw_texts[i].rstrip()):]
            node.replace_with(prefix + translated + suffix)

    # Translate head: title
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        t = str(title_tag.string).strip()
        if t not in _CACHE:
            translated = batch_translate([t])[0]
            _CACHE[t] = translated
        title_tag.string = _CACHE.get(t, t)

    # Translate meta description and og tags
    for meta in soup.find_all("meta"):
        name = meta.get("name", "")
        prop = meta.get("property", "")
        if name in ("description",) or prop in ("og:title", "og:description"):
            c = meta.get("content", "")
            if c and re.search(r"[a-zA-Z]", c):
                cs = c.strip()
                if cs not in _CACHE:
                    _CACHE[cs] = batch_translate([cs])[0]
                meta["content"] = _CACHE.get(cs, c)

    # Translate alt and aria-label attrs
    for tag in soup.find_all(True):
        for attr in TRANSLATE_ATTRS:
            if attr in tag.attrs:
                val = tag.attrs[attr]
                if isinstance(val, str) and val.strip() and re.search(r"[a-zA-Z]", val):
                    vs = val.strip()
                    if vs not in _CACHE:
                        _CACHE[vs] = batch_translate([vs])[0]
                    tag.attrs[attr] = _CACHE.get(vs, val)

    return soup


def build_hreflang_block(page_path: str, en_canonical: str = None) -> str:
    """Build complete 48-entry hreflang block using EN canonical URL as template."""
    # Derive URL path from EN canonical or page_path
    if en_canonical:
        # en_canonical is like "https://1win.codes/en/bonus/cashback-bonus"
        # Extract path after /en/
        m = re.search(r"https://1win\.codes/en(.*)", en_canonical)
        if m:
            path_part = m.group(1)  # e.g. "/bonus/cashback-bonus" or "/" or "/bonus/"
        else:
            path_part = "/"
    else:
        # Derive from page_path
        if page_path == "index.html":
            path_part = "/"
        elif page_path.endswith("/index.html"):
            dir_part = page_path[:-len("index.html")]
            path_part = "/" + dir_part
        else:
            # Strip .html
            path_part = "/" + page_path.replace(".html", "")

    lines = []
    for loc in LOCALES:
        href = f"https://1win.codes/{loc}{path_part}"
        if not href.endswith("/") and "." not in path_part.split("/")[-1]:
            pass  # keep as-is
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{href}" />')

    # x-default -> en
    xd = f"https://1win.codes/en{path_part}"
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{xd}" />')

    return "\n".join(lines)


def fix_structure(content: str, page_path: str) -> str:
    """Fix lang, canonical, hreflang, internal links."""
    # lang="en" -> lang="bn"
    content = re.sub(r'<html(\s[^>]*)?lang="en"', lambda m: m.group().replace('lang="en"', 'lang="bn"'), content)

    # Fix canonical URL: /en/ -> /bn/
    # Handle both attribute orders (BS4 may reorder)
    content = re.sub(
        r'(href="https://1win\.codes)/en(/[^"]*")',
        lambda m: m.group(1) + "/bn" + m.group(2),
        content,
    )

    # Remove existing hreflang alternate links
    content = re.sub(r'\s*<link[^>]+hreflang[^>]+/?>\s*', "\n", content)

    # Extract EN canonical URL for accurate hreflang building
    en_canonical_m = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', content)
    if not en_canonical_m:
        en_canonical_m = re.search(r'<link[^>]+href="([^"]+)"[^>]+rel="canonical"', content)
    # At this point, content already has /bn/ in canonical
    # We need to derive the URL pattern from what we have
    en_canonical = None
    if en_canonical_m:
        bn_canonical = en_canonical_m.group(1)
        # Convert back to derive the path
        en_canonical = bn_canonical.replace("/bn/", "/en/").replace("/bn", "/en")
    block = build_hreflang_block(page_path, en_canonical)
    canonical_re = re.compile(r'(<link[^>]+rel="canonical"[^>]*/?>)', re.IGNORECASE)
    m = canonical_re.search(content)
    if m:
        pos = m.end()
        content = content[:pos] + "\n" + block + content[pos:]
    else:
        head_m = re.search(r"(<head[^>]*>)", content)
        if head_m:
            pos = head_m.end()
            content = content[:pos] + "\n" + block + content[pos:]

    # Fix internal nav links /en/ -> /bn/ (not affiliate /link/ URLs)
    def fix_link(m):
        href = m.group(0)
        if "/link/" in href:
            return href
        return href.replace('href="/en/', 'href="/bn/')
    content = re.sub(r'href="/en/[^"]*"', fix_link, content)

    # Final: remove any remaining em/en dashes
    content = content.replace("—", " - ").replace("–", " - ")

    # Apply BN replacements
    for bad, good in BN_REPLACEMENTS.items():
        content = content.replace(bad, good)

    return content


def audit(content: str, page_path: str) -> list:
    """Return list of quality issues."""
    issues = []

    if "—" in content or "–" in content:
        issues.append("dash chars present")

    if "XLBONUS" not in content:
        issues.append("XLBONUS missing")

    if "8048/JAZ" not in content:
        issues.append("Curaçao 8048/JAZ missing")

    content_lower = content.lower()
    for phrase in ["world-class", "cutting-edge", "next-generation",
                   "state-of-the-art", "thousands of", "hundreds of"]:
        if phrase in content_lower:
            issues.append(f"Banned EN: '{phrase}'")

    for phrase in BANNED_BN:
        if phrase in content:
            issues.append(f"Banned BN: '{phrase}'")

    if 'lang="bn"' not in content:
        issues.append("html lang != bn")

    hreflang_count = content.count("hreflang=")
    if hreflang_count < 47:
        issues.append(f"hreflang: {hreflang_count}/48")

    # Canonical check
    for pattern in [
        r'rel="canonical"[^>]+href="([^"]+)"',
        r'href="([^"]+)"[^>]+rel="canonical"',
    ]:
        m = re.search(pattern, content)
        if m:
            url = m.group(1)
            if "/en/" in url:
                issues.append(f"Canonical -> /en/: {url}")
            break
    else:
        issues.append("No canonical")

    # JSON-LD validation
    for i, block in enumerate(
        re.findall(r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>', content, re.DOTALL)
    ):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as e:
            issues.append(f"JSON-LD {i+1}: {str(e)[:60]}")

    return issues


def translate_file(page_path: str, force: bool = False) -> dict:
    en_file = EN_DIR / page_path
    bn_file = BN_DIR / page_path
    result = {"path": page_path, "status": "ok", "issues": []}

    if not en_file.exists():
        result["status"] = "error_no_source"
        result["issues"] = [f"No source: {en_file}"]
        return result

    if bn_file.exists() and not force:
        content = bn_file.read_text(encoding="utf-8")
        issues = audit(content, page_path)
        result["issues"] = issues
        result["status"] = "skipped" if not issues else "skipped_issues"
        return result

    en_content = en_file.read_text(encoding="utf-8")
    soup = BeautifulSoup(en_content, "html.parser")

    # Translate
    translate_soup(soup)

    content = str(soup)
    content = fix_structure(content, page_path)

    bn_file.parent.mkdir(parents=True, exist_ok=True)
    bn_file.write_text(content, encoding="utf-8")

    issues = audit(content, page_path)
    result["issues"] = issues
    result["status"] = "ok_with_issues" if issues else "ok"
    return result


def main():
    pages = [p.strip() for p in INVENTORY.read_text().splitlines() if p.strip()]
    force = "--force" in sys.argv

    print(f"Translating {len(pages)} pages to Bengali (force={force})")
    print(f"Cache pre-loaded with {len(_CACHE)} entries\n")

    results = []
    ok = issues_count = error_count = 0

    for i, page in enumerate(pages):
        print(f"[{i+1:3d}/{len(pages)}] {page}", end=" ", flush=True)
        t0 = time.time()
        r = translate_file(page, force=force)
        elapsed = time.time() - t0
        results.append(r)

        if r["status"] in ("ok", "skipped"):
            ok += 1
            print(f"✓ ({elapsed:.1f}s)")
        elif r["status"].startswith("error"):
            error_count += 1
            print(f"✗ {r['issues']}")
        else:
            issues_count += 1
            print(f"⚠ {r['issues']} ({elapsed:.1f}s)")

        if (i + 1) % 25 == 0:
            print(f"\n  CHECKPOINT {i+1}: clean={ok} issues={issues_count} errors={error_count} api_calls={_STATS['api_calls']}\n")

    print(f"\n{'='*60}")
    print(f"FINAL: pages={len(pages)}, clean={ok}, issues={issues_count}, errors={error_count}")
    print(f"API calls: {_STATS['api_calls']}, cache entries: {len(_CACHE)}")
    print(f"{'='*60}")

    # Write log
    log_lines = [
        "# Bengali (BN) Translation Log\n",
        f"Pages: {len(pages)} | Clean: {ok} | Issues: {issues_count} | Errors: {error_count}\n",
        f"API calls: {_STATS['api_calls']} | Cache entries: {len(_CACHE)}\n\n",
        "## Page Results\n\n",
    ]
    for r in results:
        status_sym = "✓" if r["status"] in ("ok","skipped") else ("⚠" if "issue" in r["status"] else "✗")
        issues_str = "; ".join(r["issues"]) if r["issues"] else "none"
        log_lines.append(f"- {status_sym} `{r['path']}` — {issues_str}\n")

    log_path = REPO / "build_helpers" / "translation_log_bn.md"
    log_path.write_text("".join(log_lines))
    print(f"\nLog written to {log_path}")

    return results, ok, issues_count, error_count


if __name__ == "__main__":
    main()
