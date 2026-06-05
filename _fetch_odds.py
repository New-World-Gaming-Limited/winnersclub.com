#!/usr/bin/env python3
"""Pull top upcoming football fixtures from odds-api.io with Stake odds,
write static JSON consumed by /live-odds/ at build time.

Usage: python3 _fetch_odds.py
Output: /home/user/workspace/winnersclub.com/odds-data.json
"""
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_KEY = os.environ.get("ODDS_API_KEY")
if not API_KEY:
    raise SystemExit("ODDS_API_KEY env var required. Get it from https://odds-api.io/dashboard/settings")
BASE = "https://api.odds-api.io/v3"
BOOKMAKER = "Stake"
AFFILIATE = "https://www.getstake.it/i/maxbet/io/maxbet/u/maxbet/uo/maxbet"

# Top leagues by global pull. World Cup is on so it goes first.
TOP_LEAGUES = [
    "international-world-cup",
    "england-premier-league",
    "spain-laliga",
    "italy-serie-a",
    "germany-bundesliga",
    "france-ligue-1",
    "uefa-champions-league",
    "uefa-europa-league",
    "brazil-brasileiro-serie-a",
    "usa-major-league-soccer",
    "international-int-friendly-games",
    "norway-eliteserien",
    "sweden-allsvenskan",
    "argentina-primera-division",
]


def get(path, **params):
    params["apiKey"] = API_KEY
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=15) as r:
        return json.loads(r.read().decode())


def collect_top_matches(per_league=5, total=12):
    """Pull pending fixtures across top leagues, sorted by kickoff."""
    pool = []
    for slug in TOP_LEAGUES:
        try:
            events = get("events", sport="football", league=slug)
        except Exception:
            continue
        upcoming = sorted(
            (e for e in events if e.get("status") == "pending"),
            key=lambda e: e.get("date", ""),
        )[:per_league]
        for e in upcoming:
            pool.append(e)
    pool.sort(key=lambda e: e.get("date", ""))
    return pool[:total]


def attach_stake_odds(events):
    """For each event, hit /odds with bookmakers=Stake. Skip if Stake doesn't price it."""
    out = []
    for e in events:
        try:
            data = get("odds", eventId=e["id"], bookmakers=BOOKMAKER)
        except Exception:
            continue
        stake_book = (data.get("bookmakers") or {}).get(BOOKMAKER)
        if not stake_book:
            continue
        # Find 1X2 / Moneyline market
        ml = next(
            (m for m in stake_book if m.get("name") in ("ML", "1X2", "Moneyline")),
            None,
        )
        if not ml or not ml.get("odds"):
            continue
        prices = ml["odds"][0]
        out.append({
            "id": e["id"],
            "league": e["league"]["name"],
            "league_slug": e["league"]["slug"],
            "date": e["date"],
            "home": e["home"],
            "away": e["away"],
            "home_odds": prices.get("home"),
            "draw_odds": prices.get("draw"),
            "away_odds": prices.get("away"),
            "updated_at": ml.get("updatedAt"),
            # Use the user's affiliate redirect URL — Stake's direct match URL is the destination
            # but every outbound click goes through the affiliate.
            "stake_url": data.get("urls", {}).get(BOOKMAKER),
            "affiliate_url": AFFILIATE,
        })
    return out


def main():
    print("Pulling top football events…")
    events = collect_top_matches(per_league=4, total=18)
    print(f"  candidates: {len(events)}")
    print("Attaching Stake odds…")
    priced = attach_stake_odds(events)
    print(f"  with Stake prices: {len(priced)}")
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bookmaker": "Stake.com",
        "affiliate_url": AFFILIATE,
        "matches": priced,
    }
    out_path = os.path.join(os.path.dirname(__file__), "odds-data.json")
    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"Wrote {out_path} ({len(priced)} matches)")


if __name__ == "__main__":
    main()
