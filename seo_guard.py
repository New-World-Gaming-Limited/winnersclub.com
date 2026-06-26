#!/usr/bin/env python3
"""
SEO guardrails for winnersclub.com — runs after build, BEFORE deploy.

This script exists because static affiliate sites on Cloudflare Pages have a
soft-404 / compound-URL trap that gets sites deindexed. See
references/the-may-2026-deindex-postmortem.md in the seo-deploy-guardrails
skill for the full story.

The fix requires three control files at the project root:
  - _redirects                  (Cloudflare Pages routing, no SPA fallback)
  - 404.html                    (branded noindex 404 page)
  - functions/_middleware.js    (true HTTP 410 for known compound URL traps)

This guard verifies all three are present and well-formed in the build output.
If any check fails, the script exits non-zero and the cron pipeline aborts
before deploy, leaving the live site untouched.

Usage:
    python3 seo_guard.py
    # exit 0  -> all clear, safe to deploy
    # exit 1  -> guard failed, do NOT deploy
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Site-specific config
# ---------------------------------------------------------------------------
SITE_HOST = "winnersclub.com"
TRAP_HEADER = "x-winnersclub-trap"
CANONICAL_HOSTS = [
    "https://winnersclub.com",
    "https://www.winnersclub.com",
]

# Labels + Python regex the middleware MUST contain (substring/regex match)
MIDDLEWARE_MUST_HAVE = [
    ("compound .html trap",  r"\.html\\/"),
    ("category compound trap", r"about-stake\|aviator"),
    ("locale compound trap", r"ar\|es\|fr"),
    ("returns 410",          r"status:\s*410"),
    ("trap header",          r"x-winnersclub-trap"),
    ("__media__ trap",       r"__media__"),
]

# No dated-tip pages on winnersclub.com — skip the stale rule
STALE_DIR = None
KEEP_DAYS = 0
SLUG_DATE_RE = r""
SITEMAP_LEAK_RE = None

# Files to spot-check for relative internal hrefs (one per major section + a locale)
RELATIVE_HREF_SAMPLES = [
    "index.html",
    "casino/index.html",
    "sports/index.html",
    "promo-code/index.html",
    "mirror/index.html",
    "stake-us-bonus/index.html",
    "ko/index.html",
    "ko/promo-code/index.html",
    "pl/index.html",
    "ar/index.html",
]

# ---------------------------------------------------------------------------
# Implementation
# ---------------------------------------------------------------------------
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

FAILURES: list[str] = []
WARNINGS: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)
    print(f"{RED}FAIL{RESET}  {msg}")


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"{YELLOW}WARN{RESET}  {msg}")


def ok(msg: str) -> None:
    print(f"{GREEN}OK{RESET}    {msg}")


def check_control_files() -> None:
    required = {
        "_redirects": "Cloudflare Pages routing. No SPA fallback rule.",
        "404.html": "Branded 404 page with noindex.",
        "functions/_middleware.js": "Cloudflare Function for explicit 410 on trap URLs.",
        "sitemap.xml": "Sitemap is mandatory.",
        "robots.txt": "robots.txt must declare the sitemap.",
    }
    for rel, why in required.items():
        path = ROOT / rel
        if not path.exists():
            fail(f"missing {rel} — {why}")
        elif path.stat().st_size == 0:
            fail(f"empty {rel} — {why}")
        else:
            ok(f"control file present: {rel} ({path.stat().st_size} bytes)")


def check_no_spa_fallback() -> None:
    path = ROOT / "_redirects"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    spa = re.compile(r"^\s*/\*\s+/index\.html\s+200\s*$", re.MULTILINE | re.IGNORECASE)
    if spa.search(text):
        fail(
            "_redirects contains SPA fallback rule '/* /index.html 200'. "
            "This is the bug-class that deindexes static sites on Cloudflare Pages. "
            "Delete it."
        )
    else:
        ok("_redirects has no SPA fallback rule")


def check_404_robots() -> None:
    path = ROOT / "404.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    tags = re.findall(r'<meta\s+name="robots"[^>]*>', text, re.IGNORECASE)
    if not tags:
        fail("404.html has no robots meta tag. Should be noindex,follow.")
    elif len(tags) > 1:
        fail(
            f"404.html has {len(tags)} robots meta tags (must be exactly 1). "
            f"Found: {tags!r}."
        )
    elif "noindex" not in tags[0].lower():
        fail(f"404.html robots tag missing 'noindex'. Found: {tags[0]!r}")
    else:
        ok(f"404.html has 1 robots tag with noindex: {tags[0]}")


def check_middleware_traps() -> None:
    # winnersclub.com runs Advanced Mode (_worker.js). When _worker.js is
    # present, Cloudflare Pages disables functions/_middleware.js entirely.
    # So we check the trap logic lives in _worker.js (primary), and verify
    # functions/_middleware.js stays in sync as a fallback / documentation.
    worker_path = ROOT / "_worker.js"
    func_path = ROOT / "functions" / "_middleware.js"

    if not worker_path.exists() and not func_path.exists():
        fail("neither _worker.js nor functions/_middleware.js exists — no trap layer at all")
        return

    # Primary: _worker.js (Advanced Mode wins on this site)
    if worker_path.exists():
        text = worker_path.read_text(encoding="utf-8")
        for label, pat in MIDDLEWARE_MUST_HAVE:
            if not re.search(pat, text, re.IGNORECASE):
                fail(f"_worker.js missing trap logic: {label} (no match for /{pat}/)")
            else:
                ok(f"_worker.js has {label}")
    # Secondary: functions/_middleware.js (only runs if _worker.js is removed)
    if func_path.exists():
        text = func_path.read_text(encoding="utf-8")
        missing = [label for label, pat in MIDDLEWARE_MUST_HAVE if not re.search(pat, text, re.IGNORECASE)]
        if missing:
            warn(f"functions/_middleware.js out of sync with _worker.js (missing: {missing}). "
                 "It's a fallback only — fix when convenient.")
        else:
            ok("functions/_middleware.js fallback in sync")


def check_sitemap_leaks() -> None:
    if not SITEMAP_LEAK_RE:
        return
    path = ROOT / "sitemap.xml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    leaks = re.findall(r"<loc>https?://[^<]*?" + SITEMAP_LEAK_RE + r"</loc>", text)
    if leaks:
        fail(
            f"sitemap contains {len(leaks)} stale URLs matching {SITEMAP_LEAK_RE!r}. "
            f"First 3: {leaks[:3]}"
        )
    else:
        ok("sitemap has no stale leak URLs")


def check_no_relative_hrefs() -> None:
    bad_href_re = re.compile(
        r'<a\s+[^>]*href="(?!(?:/|#|https?:|mailto:|tel:|javascript:|data:))([^"]+)"',
        re.IGNORECASE,
    )
    total_bad = 0
    for rel in RELATIVE_HREF_SAMPLES:
        path = ROOT / rel
        if not path.exists():
            warn(f"sample file missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        bad = [b for b in bad_href_re.findall(text) if b.strip() and not b.startswith("#")]
        if bad:
            total_bad += len(bad)
            fail(
                f"{rel} has {len(bad)} relative internal hrefs. This is the template "
                f"bug-class that triggers compound-URL deindex. fix_links.py is "
                f"supposed to root-relativize them. First 3: {bad[:3]}"
            )
    if total_bad == 0:
        ok("sampled pages have no relative internal hrefs")


def check_robots_sitemap() -> None:
    path = ROOT / "robots.txt"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if "sitemap.xml" not in text.lower():
        fail("robots.txt does not declare sitemap.xml")
    else:
        ok("robots.txt declares sitemap")


def check_homepage_canonical() -> None:
    path = ROOT / "index.html"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', text, re.IGNORECASE)
    if not m:
        fail("index.html has no canonical link")
        return
    canon = m.group(1).rstrip("/")
    if canon not in CANONICAL_HOSTS:
        fail(f"index.html canonical is {canon!r}, expected one of {CANONICAL_HOSTS}")
    else:
        ok(f"index.html canonical is {canon}")


def main() -> int:
    print(f"\n{GREEN}=== {SITE_HOST} SEO guardrails ==={RESET}")
    print(f"Site root: {ROOT}\n")

    check_control_files()
    check_no_spa_fallback()
    check_404_robots()
    check_middleware_traps()
    check_sitemap_leaks()
    check_no_relative_hrefs()
    check_robots_sitemap()
    check_homepage_canonical()

    print()
    if FAILURES:
        print(f"{RED}=== {len(FAILURES)} SEO guardrail FAILURES ==={RESET}")
        for f in FAILURES:
            print(f"  - {f}")
        print(f"\n{RED}DO NOT DEPLOY.{RESET} Fix the above and re-run.")
        return 1
    if WARNINGS:
        print(f"{YELLOW}{len(WARNINGS)} warnings (deploy allowed):{RESET}")
        for w in WARNINGS:
            print(f"  - {w}")
    print(f"{GREEN}All SEO guardrails passed. Safe to deploy.{RESET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
