#!/usr/bin/env python3
"""
Post-deploy live SEO verification for winnersclub.com.

Runs AFTER `git push` to confirm Cloudflare Pages picked up the new build and
the SEO traps are still closed. Use as the final cron step.

Usage:
    python3 seo_verify_live.py [--wait-seconds 90]
    # exit 0 -> live site behaviour is correct
    # exit 1 -> regression detected, escalate
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Site-specific config
# ---------------------------------------------------------------------------
BASE = "https://winnersclub.com"
TRAP_HEADER = "x-winnersclub-trap"

TRAP_URLS = [
    # Compound-URL traps the worker MUST 410
    "/promo-code/index.html/casino/stake/foo",
    "/mirror/index.html/anywhere",
    "/casino/stake/foo/bar/baz",
    "/sports/league/team/player/something",
    "/ko/promo-code/foo/bar/baz",
    "/ar/casino/x/y/z",
    "/__media__/anything/here",
]

# Traps where 410 OR a 301/302 to a real page is acceptable (anything that
# is not a soft-404 200 with garbage path).
SOFT_TRAP_URLS = [
    "/link/abc/123/extra-segment",  # Cloudflare /link/ rewrite to home
]

RANDOM_404_URLS = [
    "/some-totally-nonexistent-path-12345",
    "/another-fake-path-that-does-not-exist",
    "/zz/this-locale-does-not-exist/",
]

REAL_200_URLS = [
    "/",
    "/casino/",
    "/sports/",
    "/promo-code/",
    "/mirror/",
    "/stake-us-bonus/",
    "/ko/",
    "/ko/promo-code/",
    "/sitemap.xml",
    "/robots.txt",
    "/404.html",
]

MIN_SITEMAP_URLS = 300  # current sitemap has 342

SITEMAP_LEAK_RE = None  # winnersclub.com has no dated stale pages

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
FAILS: list[str] = []


def fetch(path: str, follow_redirects: bool = False):
    url = path if path.startswith("http") else BASE + path
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        if follow_redirects:
            opener = urllib.request.build_opener()
        else:
            class NoRedirect(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, *a, **kw):
                    return None
            opener = urllib.request.build_opener(NoRedirect)
        try:
            r = opener.open(req, timeout=20)
            body = r.read().decode("utf-8", errors="ignore")
            return r.status, dict(r.headers), body
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore") if e.fp else ""
            return e.code, dict(e.headers or {}), body
    except Exception as e:
        FAILS.append(f"network error fetching {url}: {e}")
        return 0, {}, ""


def fail(msg: str) -> None:
    FAILS.append(msg)
    print(f"{RED}FAIL{RESET}  {msg}")


def ok(msg: str) -> None:
    print(f"{GREEN}OK{RESET}    {msg}")


def check_traps() -> None:
    for u in TRAP_URLS:
        status, hdr, _ = fetch(u, follow_redirects=False)
        # Header keys are case-insensitive on the wire; check both
        trap = (
            hdr.get(TRAP_HEADER)
            or hdr.get(TRAP_HEADER.title())
            or hdr.get(TRAP_HEADER.upper())
        )
        if status != 410:
            fail(f"trap {u}: expected 410, got {status}")
        elif trap != "1":
            fail(f"trap {u}: got 410 but no {TRAP_HEADER} header (worker did not fire)")
        else:
            ok(f"trap {u} -> 410 with trap header")

    # Soft traps: anything except a 200 with the home/garbage body is fine
    for u in SOFT_TRAP_URLS:
        status, hdr, _ = fetch(u, follow_redirects=False)
        if status == 200:
            fail(f"soft trap {u}: returned 200 (soft-404 risk); expected 3xx or 4xx")
        else:
            ok(f"soft trap {u} -> {status} (acceptable)")


def check_random_404() -> None:
    for u in RANDOM_404_URLS:
        status, _, _ = fetch(u, follow_redirects=False)
        if status not in (404, 410):
            fail(f"{u}: expected 404 or 410, got {status}")
        else:
            ok(f"{u} -> {status}")


def check_real_pages() -> None:
    for u in REAL_200_URLS:
        status, _, _ = fetch(u, follow_redirects=True)
        if status != 200:
            fail(f"real page {u}: expected 200, got {status}")
        else:
            ok(f"real page {u} -> 200")


def check_sitemap() -> None:
    status, _, body = fetch("/sitemap.xml", follow_redirects=True)
    if status != 200:
        fail(f"sitemap.xml: expected 200, got {status}")
        return
    if SITEMAP_LEAK_RE:
        leaks = re.findall(r"<loc>https?://[^<]*?" + SITEMAP_LEAK_RE + r"</loc>", body)
        if leaks:
            fail(f"sitemap has {len(leaks)} stale leak entries; first: {leaks[0]}")
        else:
            ok("sitemap has no stale leak entries")
    n = len(re.findall(r"<loc>", body))
    if n < MIN_SITEMAP_URLS:
        fail(f"sitemap suspiciously small: {n} URLs (expected >= {MIN_SITEMAP_URLS})")
    else:
        ok(f"sitemap has {n} URLs")


def check_404_robots() -> None:
    status, _, body = fetch("/404.html", follow_redirects=True)
    if status != 200:
        fail(f"/404.html: expected 200 on direct fetch, got {status}")
        return
    tags = re.findall(r'<meta\s+name="robots"[^>]*>', body, re.IGNORECASE)
    if len(tags) != 1:
        fail(f"/404.html has {len(tags)} robots meta tags (expected 1): {tags!r}")
    elif "noindex" not in tags[0].lower():
        fail(f"/404.html robots tag missing noindex: {tags[0]!r}")
    else:
        ok("/404.html has 1 robots tag with noindex")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wait-seconds", type=int, default=0,
        help="seconds to wait before starting (give Cloudflare time to redeploy)")
    args = parser.parse_args()

    if args.wait_seconds:
        print(f"Waiting {args.wait_seconds}s for Cloudflare Pages redeploy...")
        time.sleep(args.wait_seconds)

    print(f"\n{GREEN}=== live SEO verification ==={RESET}")
    print(f"Base: {BASE}\n")

    check_traps()
    check_random_404()
    check_real_pages()
    check_sitemap()
    check_404_robots()

    print()
    if FAILS:
        print(f"{RED}=== {len(FAILS)} live verification FAILURES ==={RESET}")
        for f in FAILS:
            print(f"  - {f}")
        return 1
    print(f"{GREEN}All live SEO checks passed.{RESET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
