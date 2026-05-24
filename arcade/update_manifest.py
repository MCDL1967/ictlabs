#!/usr/bin/env python3
"""
update_manifest.py
──────────────────
Run this script from the project root whenever you add or remove
a game folder. It scans the games/ directory and rebuilds
games/manifest.json automatically.

Usage:
    python update_manifest.py
"""

import os
import json

GAMES_DIR = os.path.join(os.path.dirname(__file__), 'games')
MANIFEST_PATH = os.path.join(GAMES_DIR, 'manifest.json')


def update_manifest():
    if not os.path.isdir(GAMES_DIR):
        print(f"ERROR: '{GAMES_DIR}' folder not found. Make sure you're running from the project root.")
        return

    folders = []
    for entry in sorted(os.listdir(GAMES_DIR)):
        full_path = os.path.join(GAMES_DIR, entry)
        info_path = os.path.join(full_path, 'game_info.json')
        if os.path.isdir(full_path) and os.path.isfile(info_path):
            folders.append(entry)
            print(f"  ✔  Found: {entry}")
        elif os.path.isdir(full_path) and entry != '__pycache__':
            print(f"  ⚠  Skipped (no game_info.json): {entry}")

    manifest = {"games": folders}
    with open(MANIFEST_PATH, 'w') as f:
        json.dump(manifest, f, indent=2)

    print(f"\n✅  manifest.json updated — {len(folders)} game(s) registered.")
    print(f"   → {MANIFEST_PATH}")


if __name__ == '__main__':
    update_manifest()
