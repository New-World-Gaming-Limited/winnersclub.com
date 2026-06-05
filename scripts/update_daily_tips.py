#!/usr/bin/env python3
"""
update_daily_tips.py
====================
Daily tips updater for 1win.codes/en/tips/ pages.

This script:
  1. Fetches upcoming matches from a match/odds data feed (odds-api.io or similar).
  2. Selects the top 3-5 most liquid fixtures per sport.
  3. Generates a short tip string per fixture via generate_tip().
  4. Writes updated HTML tip-card blocks into the <div id="todays-tips"> containers
     in en/tips/todays-*.html.
  5. Updates the data-updated="<ISO timestamp>" attribute on each container div.
  6. Logs all actions to scripts/logs/daily_tips.log.
  7. Supports --dry-run to preview changes without writing files.

Usage:
  python scripts/update_daily_tips.py [--dry-run]

Dependencies:
  pip install beautifulsoup4 requests python-dateutil

Cron example (runs at 07:00 UTC daily):
  0 7 * * * cd /path/to/1win-codes-repo && python scripts/update_daily_tips.py >> scripts/logs/cron.log 2>&1
"""

import argparse
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = REPO_ROOT / "scripts" / "logs"
LOG_FILE = LOG_DIR / "daily_tips.log"
TIPS_DIR = REPO_ROOT / "en" / "tips"

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config: sport -> output file + div id + data-sport value
# ---------------------------------------------------------------------------

SPORTS_CONFIG = {
    "football": {
        "file": "todays-football.html",
        "div_id": "todays-tips",
        "data_sport": "football",
        "leagues": ["Premier League", "La Liga", "Bundesliga", "Serie A", "Champions League"],
    },
    "cricket": {
        "file": "todays-cricket.html",
        "div_id": "todays-tips",
        "data_sport": "cricket",
        "leagues": ["IPL", "T20I", "ODI", "Test"],
    },
    "tennis": {
        "file": "todays-tennis.html",
        "div_id": "todays-tips",
        "data_sport": "tennis",
        "leagues": ["ATP Tour", "WTA Tour", "Challenger"],
    },
    "basketball": {
        "file": "todays-basketball.html",
        "div_id": "todays-tips",
        "data_sport": "basketball",
        "leagues": ["NBA", "EuroLeague", "NBL"],
    },
    "esports": {
        "file": "todays-esports.html",
        "div_id": "todays-tips",
        "data_sport": "esports",
        "leagues": ["CS2", "Dota 2", "League of Legends", "Valorant"],
    },
}

# ---------------------------------------------------------------------------
# Step 1: Fetch matches from odds feed
# ---------------------------------------------------------------------------

def fetch_matches(sport: str, config: dict) -> list[dict]:
    """
    Fetch upcoming matches for the given sport from the data feed.

    Returns a list of match dicts with keys:
        match_name, league, kickoff_utc, home_team, away_team,
        liquidity_score (float), market_odds (dict)

    TODO: Replace the placeholder implementation below with a live API call.
    Example integration with odds-api.io:

        import requests
        API_KEY = os.environ.get("ODDS_API_KEY", "")  # set in environment
        url = f"https://api.odds-api.io/v4/sports/{sport}/odds"
        params = {
            "apiKey": API_KEY,
            "regions": "eu",
            "markets": "h2h,totals,spreads",
            "oddsFormat": "decimal",
            "dateFormat": "iso",
        }
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        raw = resp.json()
        return _normalise_odds_api_response(raw)

    For now, returns deterministic test data so the update flow can be
    demonstrated end-to-end without a live API key.
    """
    log.info("[%s] Fetching matches (stub - replace with live feed)", sport)

    # TODO: Remove stub data and connect to live odds-api.io (or equivalent) feed.
    # The stub below mirrors the shape a real feed normaliser would return.
    stub_matches = {
        "football": [
            {
                "match_name": "Manchester United vs Arsenal",
                "league": "Premier League",
                "kickoff_utc": "15:00 UTC",
                "home_team": "Manchester United",
                "away_team": "Arsenal",
                "liquidity_score": 9.5,
                "market_odds": {"btts_yes": 1.82, "over_2_5": 1.79, "ah_home_minus_half": 2.10},
            },
            {
                "match_name": "Bayern Munich vs Dortmund",
                "league": "Bundesliga",
                "kickoff_utc": "17:30 UTC",
                "home_team": "Bayern Munich",
                "away_team": "Dortmund",
                "liquidity_score": 9.1,
                "market_odds": {"btts_yes": 1.74, "over_2_5": 1.68, "ah_home_minus_half": 1.85},
            },
            {
                "match_name": "Barcelona vs Atletico Madrid",
                "league": "La Liga",
                "kickoff_utc": "19:45 UTC",
                "home_team": "Barcelona",
                "away_team": "Atletico Madrid",
                "liquidity_score": 8.8,
                "market_odds": {"btts_yes": 1.91, "over_2_5": 1.85, "ah_home_minus_half": 1.90},
            },
        ],
        "cricket": [
            {
                "match_name": "India vs Australia",
                "league": "T20I",
                "kickoff_utc": "14:00 UTC",
                "home_team": "India",
                "away_team": "Australia",
                "liquidity_score": 9.3,
                "market_odds": {"total_runs_over_315": 1.85, "home_top_batter_over_38": 1.90},
            },
            {
                "match_name": "Mumbai Indians vs RCB",
                "league": "IPL",
                "kickoff_utc": "14:30 UTC",
                "home_team": "Mumbai Indians",
                "away_team": "Royal Challengers Bengaluru",
                "liquidity_score": 8.7,
                "market_odds": {"total_runs_over_325": 1.87, "home_top_batter_over_40": 1.92},
            },
            {
                "match_name": "England vs New Zealand",
                "league": "ODI",
                "kickoff_utc": "09:30 UTC",
                "home_team": "England",
                "away_team": "New Zealand",
                "liquidity_score": 8.2,
                "market_odds": {"home_win_dnb": 1.78},
            },
        ],
        "tennis": [
            {
                "match_name": "Carlos Alcaraz vs Jannik Sinner",
                "league": "ATP Masters",
                "kickoff_utc": "TBC",
                "home_team": "Carlos Alcaraz",
                "away_team": "Jannik Sinner",
                "liquidity_score": 9.0,
                "market_odds": {"total_games_over_35_5": 1.88, "match_winner_home": 1.65},
            },
            {
                "match_name": "Iga Swiatek vs Elena Rybakina",
                "league": "WTA 1000",
                "kickoff_utc": "TBC",
                "home_team": "Iga Swiatek",
                "away_team": "Elena Rybakina",
                "liquidity_score": 8.9,
                "market_odds": {"match_winner_home": 1.72, "first_set_winner_home": 1.60},
            },
            {
                "match_name": "ATP Challenger Featured Match",
                "league": "Challenger",
                "kickoff_utc": "TBC",
                "home_team": "Local qualifier",
                "away_team": "Seeded opponent",
                "liquidity_score": 5.1,
                "market_odds": {"first_set_winner_home": 1.80},
            },
        ],
        "basketball": [
            {
                "match_name": "Los Angeles Lakers vs Boston Celtics",
                "league": "NBA",
                "kickoff_utc": "00:30 UTC",
                "home_team": "Los Angeles Lakers",
                "away_team": "Boston Celtics",
                "liquidity_score": 9.7,
                "market_odds": {"total_under_216_5": 1.92, "spread_away_minus_5": 1.87},
            },
            {
                "match_name": "Real Madrid vs Olympiacos",
                "league": "EuroLeague",
                "kickoff_utc": "19:00 UTC",
                "home_team": "Real Madrid",
                "away_team": "Olympiacos",
                "liquidity_score": 7.8,
                "market_odds": {"spread_home_minus_5_5": 1.87},
            },
            {
                "match_name": "Golden State Warriors vs Phoenix Suns",
                "league": "NBA",
                "kickoff_utc": "02:00 UTC",
                "home_team": "Golden State Warriors",
                "away_team": "Phoenix Suns",
                "liquidity_score": 8.5,
                "market_odds": {"player_props_primary_over_24_5": 1.95},
            },
        ],
        "esports": [
            {
                "match_name": "Natus Vincere vs FaZe Clan",
                "league": "CS2 - ESL Pro League",
                "kickoff_utc": "15:00 UTC",
                "home_team": "Natus Vincere",
                "away_team": "FaZe Clan",
                "liquidity_score": 8.6,
                "market_odds": {"total_maps_over_2_5": 1.95, "match_winner_home": 2.05},
            },
            {
                "match_name": "Team Spirit vs Gaimin Gladiators",
                "league": "Dota 2 - DPC",
                "kickoff_utc": "12:00 UTC",
                "home_team": "Team Spirit",
                "away_team": "Gaimin Gladiators",
                "liquidity_score": 7.4,
                "market_odds": {"map_handicap_home_minus_1_5": 2.05},
            },
            {
                "match_name": "T1 vs Gen.G",
                "league": "League of Legends - LCK",
                "kickoff_utc": "10:00 UTC",
                "home_team": "T1",
                "away_team": "Gen.G",
                "liquidity_score": 8.2,
                "market_odds": {"match_winner_home": 1.78},
            },
        ],
    }
    return stub_matches.get(sport, [])


# ---------------------------------------------------------------------------
# Step 2: Select top matches by liquidity
# ---------------------------------------------------------------------------

def select_top_matches(matches: list[dict], top_n: int = 3) -> list[dict]:
    """
    Sort matches by liquidity_score descending and return the top N.

    TODO: When using a live feed, liquidity_score should be derived from
    the total matched volume on the event across major exchanges (e.g.,
    Betfair matched volume) or estimated from open market depth.
    """
    sorted_matches = sorted(matches, key=lambda m: m.get("liquidity_score", 0), reverse=True)
    selected = sorted_matches[:top_n]
    log.info("Selected %d matches (top by liquidity): %s", len(selected), [m["match_name"] for m in selected])
    return selected


# ---------------------------------------------------------------------------
# Step 3: Generate tips
# ---------------------------------------------------------------------------

def generate_tip(match: dict) -> dict:
    """
    Generate a tip for a single match.

    Returns a dict with keys:
        pick (str): market name and direction
        odds_label (str): suggested odds range
        reasoning (str): 1-2 sentence rationale

    TODO: Replace the deterministic heuristic below with a model-driven
    approach. Options include:
      - Rule-based: best odds/probability delta from your edge model
      - LLM-assisted: send match context to an LLM to generate reasoning text
        (keep model calls cached for identical inputs to avoid re-generation)
      - External signal: use closing-line value from a sharp market benchmark

    Current implementation picks the market with the highest decimal odds
    (as a proxy for market uncertainty) and returns a fixed reasoning template.
    This is sufficient to demonstrate the update flow for a future developer.
    """
    market_odds = match.get("market_odds", {})
    if not market_odds:
        return {
            "pick": "No market available",
            "odds_label": "N/A",
            "reasoning": "Insufficient market data for this fixture.",
        }

    # Select market with highest odds as the primary pick (placeholder heuristic)
    # TODO: Replace with a positive-EV selection model
    best_market = max(market_odds, key=lambda k: market_odds[k])
    best_odds = market_odds[best_market]

    # Convert internal key to readable label
    readable_market = best_market.replace("_", " ").replace("  ", " ").strip()

    reasoning = (
        f"Placeholder reasoning for {match['match_name']}: "
        f"the {readable_market} market at {best_odds:.2f} shows a positive expected "
        f"value delta based on form and head-to-head data. "
        f"Full analysis will be populated by the live model integration."
        # TODO: Replace this string with model-generated or analyst-written reasoning.
    )

    return {
        "pick": readable_market,
        "odds_label": f"around {best_odds:.2f}",
        "reasoning": reasoning,
    }


# ---------------------------------------------------------------------------
# Step 4: Build HTML tip card
# ---------------------------------------------------------------------------

CTA_URL = "https://1win.codes/en/register?promo=XLBONUS"

def build_tip_card_html(match: dict, tip: dict) -> str:
    """Build a single tip card HTML block."""
    return f'''    <div class="tip-card">
      <div class="tip-card-header">
        <span class="tip-sport-tag">{match["league"]}</span>
        <span class="tip-time">Start: {match.get("kickoff_utc", "TBC")}</span>
      </div>
      <p class="tip-match"><strong>{match["match_name"]}</strong></p>
      <p class="tip-pick">Pick: {tip["pick"]} | Suggested odds: {tip["odds_label"]}</p>
      <p class="tip-reasoning">{tip["reasoning"]}</p>
      <a class="btn btn-primary" href="{CTA_URL}">Claim XLBONUS and bet at 1win</a>
    </div>'''


def build_tips_html(matches: list[dict]) -> str:
    """Build the full inner HTML for the tips-grid div."""
    cards = [build_tip_card_html(m, generate_tip(m)) for m in matches]
    return "\n".join(cards)


# ---------------------------------------------------------------------------
# Step 5: Update HTML file
# ---------------------------------------------------------------------------

def update_html_file(filepath: Path, div_id: str, new_inner_html: str, iso_ts: str, dry_run: bool) -> bool:
    """
    Replace the inner content of <div id="{div_id}" ...> and update
    the data-updated attribute with the ISO timestamp.

    Uses regex for robustness without requiring a full HTML parser at runtime.
    BeautifulSoup4 is the preferred approach for complex mutations:

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")
        div = soup.find("div", {"id": div_id})
        if div:
            div.clear()
            div.append(BeautifulSoup(new_inner_html, "html.parser"))
            div["data-updated"] = iso_ts

    The regex approach below is used to avoid an external dependency at
    verification time. If BeautifulSoup4 is installed, prefer that.
    """
    if not filepath.exists():
        log.error("File not found: %s", filepath)
        return False

    content = filepath.read_text(encoding="utf-8")

    # Pattern: match the opening div tag with id=div_id (allow any attributes, any order)
    # and capture everything up to the closing </div>
    open_tag_pattern = re.compile(
        rf'(<div\b[^>]*\bid="{re.escape(div_id)}"[^>]*>)',
        re.DOTALL,
    )
    match = open_tag_pattern.search(content)
    if not match:
        log.error("Could not find <div id=\"%s\"> in %s", div_id, filepath)
        return False

    tag_start = match.start()
    tag_end = match.end()
    original_tag = match.group(1)

    # Update data-updated attribute in the opening tag
    if 'data-updated=' in original_tag:
        updated_tag = re.sub(r'data-updated="[^"]*"', f'data-updated="{iso_ts}"', original_tag)
    else:
        # Insert data-updated before the closing >
        updated_tag = original_tag[:-1] + f' data-updated="{iso_ts}">'

    # Find the matching closing </div> (naively: first one after tag_end)
    # For robustness, count nesting depth
    depth = 1
    pos = tag_end
    while depth > 0 and pos < len(content):
        open_match = re.search(r'<div\b', content[pos:])
        close_match = re.search(r'</div>', content[pos:])
        if close_match is None:
            log.error("Unmatched div in %s", filepath)
            return False
        open_offset = open_match.start() if open_match else len(content)
        close_offset = close_match.start()
        if open_offset < close_offset:
            depth += 1
            pos += open_offset + len("<div")
        else:
            depth -= 1
            if depth == 0:
                close_end = pos + close_match.end()
                break
            pos += close_offset + len("</div>")

    new_content = (
        content[:tag_start]
        + updated_tag
        + "\n"
        + new_inner_html
        + "\n  "
        + content[close_end - len("</div>"):close_end]
        + content[close_end:]
    )

    if dry_run:
        log.info("[DRY RUN] Would write %d chars to %s", len(new_content), filepath)
        log.info("[DRY RUN] data-updated would be set to: %s", iso_ts)
        log.info("[DRY RUN] First tip card preview:\n%s", build_tip_card_html(
            {"league": "Preview", "kickoff_utc": "TBC", "match_name": "Team A vs Team B", "market_odds": {}},
            {"pick": "N/A", "odds_label": "N/A", "reasoning": "Dry run preview."}
        ))
        return True

    filepath.write_text(new_content, encoding="utf-8")
    log.info("Updated %s (data-updated=%s)", filepath.name, iso_ts)
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Update daily tips pages for 1win.codes")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without modifying any files",
    )
    parser.add_argument(
        "--sport",
        choices=list(SPORTS_CONFIG.keys()),
        default=None,
        help="Update only a specific sport (default: all sports)",
    )
    args = parser.parse_args()

    iso_ts = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    log.info("=== update_daily_tips.py start | ts=%s | dry_run=%s ===", iso_ts, args.dry_run)

    sports_to_run = [args.sport] if args.sport else list(SPORTS_CONFIG.keys())
    success_count = 0
    error_count = 0

    for sport in sports_to_run:
        config = SPORTS_CONFIG[sport]
        filepath = TIPS_DIR / config["file"]
        log.info("--- Processing sport: %s -> %s ---", sport, filepath.name)

        # 1. Fetch
        try:
            matches = fetch_matches(sport, config)
        except Exception as exc:
            log.error("[%s] fetch_matches failed: %s", sport, exc)
            error_count += 1
            continue

        if not matches:
            log.warning("[%s] No matches returned; skipping update.", sport)
            continue

        # 2. Select top N by liquidity
        selected = select_top_matches(matches, top_n=3)

        # 3. Build HTML
        tips_html = build_tips_html(selected)

        # 4. Write to file
        ok = update_html_file(
            filepath=filepath,
            div_id=config["div_id"],
            new_inner_html=tips_html,
            iso_ts=iso_ts,
            dry_run=args.dry_run,
        )
        if ok:
            success_count += 1
        else:
            error_count += 1

    log.info("=== Done: %d updated, %d errors ===", success_count, error_count)
    sys.exit(0 if error_count == 0 else 1)


if __name__ == "__main__":
    main()
