# galaga.py
# ─────────────────────────────────────────────────────────────────
# Launches the Galaga HTML5 game in the system default browser.
# The full game runs in galaga.html (Canvas/JS — no server needed
# if opened directly; use http.server for the full console launch).
# ─────────────────────────────────────────────────────────────────

import os
import webbrowser

def run_game():
    """Open the Galaga HTML game in the default browser."""
    game_path = os.path.join(os.path.dirname(__file__), 'galaga.html')
    abs_path  = os.path.abspath(game_path)
    url       = f'file://{abs_path}'
    print(f"[GALAGA] Launching → {url}")
    webbrowser.open(url)


if __name__ == '__main__':
    run_game()
