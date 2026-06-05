#!/usr/bin/env python3
"""
Bengali (bn) translation script for 1win.codes
Translates all 184 pages from /en/ to /bn/
"""
import os
import re
import time
import json
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag
from deep_translator import GoogleTranslator

# ── Config ──────────────────────────────────────────────────────────────────
REPO = Path("/home/user/workspace/1win-codes-repo")
EN_DIR = REPO / "en"
BN_DIR = REPO / "bn"
INVENTORY = REPO / "build_helpers" / "en_page_inventory.txt"
LOG_FILE = REPO / "build_helpers" / "translation_log_bn.md"

translator = GoogleTranslator(source="en", target="bn")

# ── Strings to NEVER translate (preserve verbatim) ──────────────────────────
PRESERVE_EXACT = sorted([
    "XLBONUS", "1win", "Curaçao 8048/JAZ", "8048/JAZ", "Curaçao",
    "Pragmatic Play", "Evolution Gaming", "Spribe", "Hacksaw Gaming",
    "BGaming", "Play'n GO", "NetEnt", "Relax Gaming", "Aviator", "Lucky Drive",
    "JetX", "Spaceman", "Aviatrix", "Plinko", "Mines", "HiLo",
    "Sweet Bonanza", "Gates of Olympus", "Book of Dead", "Starburst",
    "Big Bass Bonanza", "Wolf Gold", "Fruit Party", "Sugar Rush 1000",
    "Dog House Megaways", "Dog House", "Reactoonz", "Fire Joker",
    "Buffalo King Megaways", "Extra Juicy Megaways", "Money Train 4",
    "Razor Shark", "Rise of Olympus 100", "Cash Elevator",
    "Gonzo's Quest", "Wanted Dead or a Wild",
    "bKash", "Nagad", "Rocket", "UPI", "PIX", "M-Pesa", "M-PESA",
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
    "G-S2MXR8D3HS",
    "AviaMasters", "Aviamasters", "Gamzix", "Mancala Gaming",
    "1win.codes", "1win.pro", "1win.com",
], key=len, reverse=True)

# ── Banned phrases that must NOT appear in output ───────────────────────────
BANNED_EN = [
    "world-class", "cutting-edge", "next-generation", "state-of-the-art",
    "thousands of", "hundreds of", "HIT THE TABLES", "DOMINATE EVERY MATCH",
    "OUTPLAY EVERYONE", "no strings attached", "BET ANYWHERE WIN EVERYWHERE",
]
BANNED_BN = [
    "হাজার হাজার", "শত শত", "বিশ্বমানের", "অত্যাধুনিক",
    "পরবর্তী প্রজন্মের", "সর্বশেষ",
]

# BN replacements for banned words that appear in translation
BN_REPLACEMENTS = {
    "সর্বশেষ": "সাম্প্রতিক",
    "অত্যাধুনিক": "উন্নত",
    "বিশ্বমানের": "উচ্চমানের",
    "পরবর্তী প্রজন্মের": "নতুন",
    "হাজার হাজার": "হাজারো",
    "শত শত": "শতাধিক",
}

# ── Tags whose text content should NOT be translated ────────────────────────
NO_TRANSLATE_TAGS = {"script", "style", "code", "pre", "svg", "path"}

# ── Attributes that hold translatable text ──────────────────────────────────
TRANSLATE_ATTRS = {"alt", "title", "aria-label", "placeholder"}
# For meta content, we handle separately based on name/property

# ── Translation cache ────────────────────────────────────────────────────────
_cache = {}
_cache_hits = 0
_api_calls = 0


def protect_and_translate(text: str) -> str:
    """Translate text with preservation of special terms."""
    global _cache_hits, _api_calls

    if not text or not text.strip():
        return text

    stripped = text.strip()

    # Skip if no Latin letters
    if not re.search(r'[a-zA-Z]', stripped):
        return text

    # Cache check
    if stripped in _cache:
        _cache_hits += 1
        result = text.replace(stripped, _cache[stripped])
        return result

    # Replace em/en dashes before translation
    working = stripped.replace("—", " - ").replace("–", " - ")

    # Protect: URLs and /link/ paths
    protected = {}
    counter = [0]

    def protect(val):
        ph = f"__PH{counter[0]}__"
        counter[0] += 1
        protected[ph] = val
        return ph

    # Protect URLs
    url_re = re.compile(r'https?://[^\s<>"]+|/link/[^\s<>"]+')
    working = url_re.sub(lambda m: protect(m.group()), working)

    # Protect exact terms (longest first)
    for term in PRESERVE_EXACT:
        if term in working:
            ph = protect(term)
            working = working.replace(term, ph)

    # Protect codes like XLBONUS (already protected above if in PRESERVE_EXACT)
    # Protect percent numbers: 600%, 200%, etc
    pct_re = re.compile(r'\d[\d,]*%')
    working = pct_re.sub(lambda m: protect(m.group()), working)

    # Check if anything translatable remains
    if not re.search(r'[a-zA-Z]', working):
        # Restore and return
        for ph, val in protected.items():
            working = working.replace(ph, val)
        _cache[stripped] = working
        return text.replace(stripped, working)

    # Translate
    try:
        _api_calls += 1
        translated = translator.translate(working)
        if translated is None:
            translated = working
        time.sleep(0.04)
    except Exception as e:
        print(f"  [WARN] Translation error: {e}")
        translated = working

    # Restore protected values
    for ph, val in protected.items():
        translated = translated.replace(ph, val)

    # Remove em/en dashes that may have crept back
    translated = translated.replace("—", " - ").replace("–", " - ")

    # Apply BN replacements for banned words
    for bad, good in BN_REPLACEMENTS.items():
        translated = translated.replace(bad, good)

    _cache[stripped] = translated

    # Preserve leading/trailing whitespace from original
    prefix = text[: len(text) - len(text.lstrip())]
    suffix = text[len(text.rstrip()):]
    return prefix + translated + suffix


def is_in_no_translate(node) -> bool:
    """Return True if node is inside a no-translate tag."""
    for parent in node.parents:
        if hasattr(parent, "name") and parent.name in NO_TRANSLATE_TAGS:
            return True
    return False


def translate_tree(node):
    """Recursively translate text nodes in a BS4 tree."""
    if isinstance(node, NavigableString):
        if is_in_no_translate(node):
            return
        text = str(node)
        if text.strip() and re.search(r"[a-zA-Z]", text):
            translated = protect_and_translate(text)
            node.replace_with(translated)
        return

    if isinstance(node, Tag):
        if node.name in NO_TRANSLATE_TAGS:
            return

        # Translate certain attributes
        for attr in TRANSLATE_ATTRS:
            if attr in node.attrs:
                val = node.attrs[attr]
                if isinstance(val, str) and val.strip() and re.search(r"[a-zA-Z]", val):
                    node.attrs[attr] = protect_and_translate(val)

        # Recurse
        for child in list(node.children):
            translate_tree(child)


def fix_html_structure(content: str, page_path: str) -> str:
    """Fix lang attribute, canonical URL, and internal /en/ links."""
    # Fix html lang
    content = re.sub(r'<html\s+lang="en"', '<html lang="bn"', content)

    # Fix canonical - handle both attribute orders BS4 may produce
    # Pattern: href="...1win.codes/en/..."
    content = re.sub(
        r'(href="https://1win\.codes)/en(/[^"]*")',
        lambda m: m.group(1) + "/bn" + m.group(2),
        content,
    )
    # Also handle rel="canonical" ... href pattern
    content = re.sub(
        r'(<link[^>]+rel="canonical"[^>]+href=")https://1win\.codes/en(/[^"]*")',
        lambda m: m.group(1) + "https://1win.codes/bn" + m.group(2),
        content,
    )

    # Fix internal navigation links /en/ -> /bn/
    # Only for href attributes pointing to internal pages (not affiliate links)
    def replace_en_link(m):
        # Don't replace /link/ URLs or external
        full = m.group(0)
        if "/link/" in full or "1win.codes/link" in full:
            return full
        return full.replace('href="/en/', 'href="/bn/')

    content = re.sub(r'href="/en/[^"]*"', replace_en_link, content)

    return content


def build_hreflang_block(page_path: str) -> str:
    """Build the full 48-entry hreflang block for a page."""
    locales = [
        "ar", "bg", "bn", "cs", "da", "de", "el", "en", "es", "et",
        "fa", "fi", "fr", "he", "hi", "hr", "hu", "id", "it", "ja",
        "kk", "ko", "lo", "lt", "lv", "mn", "ms", "mt", "nb", "nl",
        "pl", "pt", "ro", "ru", "sk", "sl", "sq", "sr", "sv", "th",
        "tl", "tr", "uk", "ur", "uz", "vi", "zh",
    ]

    # Determine URL path suffix
    if page_path == "index.html":
        suffix = ""  # just the locale dir with trailing slash
    elif page_path.endswith("/index.html"):
        # e.g. bonus/index.html -> /bonus/
        dir_part = page_path[: -len("index.html")]
        suffix = dir_part  # e.g. "bonus/"
    else:
        # e.g. bonus/cashback-bonus.html -> /bonus/cashback-bonus.html
        suffix = page_path  # keep as-is

    lines = []
    for loc in locales:
        if suffix == "":
            href = f"https://1win.codes/{loc}/"
        elif suffix.endswith("/"):
            href = f"https://1win.codes/{loc}/{suffix}"
        else:
            href = f"https://1win.codes/{loc}/{suffix}"
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{href}" />')

    # x-default -> en
    if suffix == "":
        xdef_href = "https://1win.codes/en/"
    elif suffix.endswith("/"):
        xdef_href = f"https://1win.codes/en/{suffix}"
    else:
        xdef_href = f"https://1win.codes/en/{suffix}"
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{xdef_href}" />')

    return "\n".join(lines)


def inject_hreflang(content: str, page_path: str) -> str:
    """Replace any existing hreflang block with the full canonical one."""
    # Remove existing hreflang alternate links (keep canonical)
    content = re.sub(
        r'\s*<link[^>]+rel="alternate"[^>]+hreflang[^>]+/?>\s*',
        "\n",
        content,
    )
    # Also handle BS4 reordered: hreflang before rel
    content = re.sub(
        r'\s*<link[^>]+hreflang=[^>]+/?>\s*',
        "\n",
        content,
    )

    # Build full block
    block = build_hreflang_block(page_path)

    # Insert after canonical link
    canonical_re = re.compile(r'(<link\s[^>]*rel="canonical"[^>]*/?>)', re.IGNORECASE)
    m = canonical_re.search(content)
    if m:
        pos = m.end()
        content = content[:pos] + "\n" + block + content[pos:]
    else:
        # Insert after <head> if no canonical found
        head_m = re.search(r"<head[^>]*>", content)
        if head_m:
            pos = head_m.end()
            content = content[:pos] + "\n" + block + content[pos:]

    return content


def post_process(content: str) -> str:
    """Apply post-processing fixes to translated content."""
    # Remove em/en dashes everywhere
    content = content.replace("—", " - ").replace("–", " - ")

    # Apply BN replacements for banned words
    for bad, good in BN_REPLACEMENTS.items():
        content = content.replace(bad, good)

    # Clean up multiple consecutive spaces/newlines that BS4 may introduce
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def audit_content(content: str, page_path: str) -> list:
    """Run mechanical post-checks on translated content."""
    issues = []

    # 1. No em or en dashes
    if "—" in content:
        issues.append("em dash found")
    if "–" in content:
        issues.append("en dash found")

    # 2. XLBONUS present
    if "XLBONUS" not in content:
        issues.append("XLBONUS missing")

    # 3. Curaçao 8048/JAZ present
    if "8048/JAZ" not in content:
        issues.append("Curaçao 8048/JAZ missing")

    # 4. No banned EN phrases
    content_lower = content.lower()
    for phrase in BANNED_EN:
        if phrase.lower() in content_lower:
            issues.append(f"Banned EN phrase: '{phrase}'")

    # 5. No banned BN phrases
    for phrase in BANNED_BN:
        if phrase in content:
            issues.append(f"Banned BN phrase: '{phrase}'")

    # 6. html lang="bn"
    if 'lang="bn"' not in content:
        issues.append("html lang != bn")

    # 7. hreflang count >= 47
    hreflang_count = content.count("hreflang=")
    if hreflang_count < 47:
        issues.append(f"Incomplete hreflang: {hreflang_count}/48")

    # 8. canonical points to /bn/
    canonical_match = re.search(r'rel="canonical"[^>]+href="([^"]+)"', content)
    if not canonical_match:
        canonical_match = re.search(r'href="([^"]+)"[^>]+rel="canonical"', content)
    if canonical_match:
        canonical_url = canonical_match.group(1)
        if "/en/" in canonical_url:
            issues.append(f"Canonical points to /en/: {canonical_url}")
    else:
        issues.append("No canonical link found")

    # 9. JSON-LD validates
    json_ld_blocks = re.findall(
        r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>',
        content,
        re.DOTALL,
    )
    for i, block in enumerate(json_ld_blocks):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as e:
            issues.append(f"JSON-LD block {i + 1} invalid: {str(e)[:80]}")

    return issues


def translate_file(page_path: str, force: bool = False) -> dict:
    """Translate a single page from en/ to bn/."""
    en_file = EN_DIR / page_path
    bn_file = BN_DIR / page_path
    result = {"path": page_path, "status": "ok", "issues": []}

    if not en_file.exists():
        result["status"] = "error_no_source"
        result["issues"] = [f"Source missing: {en_file}"]
        return result

    # Skip if already done (and not forced)
    if bn_file.exists() and not force:
        content = bn_file.read_text(encoding="utf-8")
        issues = audit_content(content, page_path)
        result["issues"] = issues
        result["status"] = "skipped_existing" if not issues else "skipped_with_issues"
        return result

    en_content = en_file.read_text(encoding="utf-8")

    # Parse HTML
    soup = BeautifulSoup(en_content, "html.parser")

    # Translate body text
    body = soup.body
    if body:
        translate_tree(body)

    # Translate head: title and meta description/og
    head = soup.head
    if head:
        title_tag = head.find("title")
        if title_tag and title_tag.string:
            title_tag.string = protect_and_translate(str(title_tag.string))

        for meta in head.find_all("meta"):
            name_attr = meta.get("name", "")
            prop_attr = meta.get("property", "")
            if name_attr in ("description",) or prop_attr in ("og:title", "og:description"):
                c = meta.get("content", "")
                if c and re.search(r"[a-zA-Z]", c):
                    meta["content"] = protect_and_translate(c)

    # Serialize
    content = str(soup)

    # Fix HTML structure (lang, canonical, internal links)
    content = fix_html_structure(content, page_path)

    # Inject full hreflang block
    content = inject_hreflang(content, page_path)

    # Post-process (banned phrases, dash cleanup)
    content = post_process(content)

    # Write output
    bn_file.parent.mkdir(parents=True, exist_ok=True)
    bn_file.write_text(content, encoding="utf-8")

    # Audit
    issues = audit_content(content, page_path)
    result["issues"] = issues
    if issues:
        result["status"] = "ok_with_issues"

    return result


def main(force_all: bool = False):
    pages = [p.strip() for p in INVENTORY.read_text().splitlines() if p.strip()]
    print(f"Processing {len(pages)} pages (force={force_all})...")

    results = []
    ok = 0
    issues_total = 0
    error_count = 0

    for i, page_path in enumerate(pages):
        print(f"[{i+1:3d}/{len(pages)}] {page_path}", end=" ... ", flush=True)
        result = translate_file(page_path, force=force_all)
        results.append(result)

        if not result["issues"] and result["status"] in ("ok", "skipped_existing"):
            ok += 1
            print("✓")
        elif result["status"].startswith("error"):
            error_count += 1
            print(f"✗ ERROR: {result['issues']}")
        else:
            issues_total += 1
            print(f"⚠ ISSUES: {result['issues']}")

        # Checkpoint every 25
        if (i + 1) % 25 == 0:
            print(
                f"\n  ─── Checkpoint {i+1}: "
                f"clean={ok}, issues={issues_total}, errors={error_count} ───\n"
            )

    print(
        f"\n{'='*60}\n"
        f"FINAL: pages={len(pages)}, clean={ok}, "
        f"issues={issues_total}, errors={error_count}\n"
        f"API calls: {_api_calls}, cache hits: {_cache_hits}\n"
        f"{'='*60}"
    )

    return results, ok, issues_total, error_count


if __name__ == "__main__":
    import sys
    force = "--force" in sys.argv
    results, ok, issues_total, error_count = main(force_all=force)
