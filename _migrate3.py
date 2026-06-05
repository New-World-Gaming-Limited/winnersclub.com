#!/usr/bin/env python3
"""Migration pass 3: NEWBONUS -> MAXBET repo-wide."""
import os
from pathlib import Path

ROOT = Path("/home/user/workspace/winnersclub.com")
OLD = "NEWBONUS"
NEW = "MAXBET"
EXT = (".html", ".xml", ".txt", ".json", ".md", ".js", ".css")

swaps = 0
files = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
    for fn in filenames:
        if not fn.endswith(EXT):
            continue
        p = Path(dirpath) / fn
        try:
            t = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if OLD not in t:
            continue
        c = t.count(OLD)
        p.write_text(t.replace(OLD, NEW), encoding="utf-8")
        swaps += c
        files += 1

print(f"NEWBONUS -> MAXBET: {swaps:,} swaps in {files:,} files")
