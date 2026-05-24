════════════════════════════════════════════════════════════════
  ICTLab Retro Console — README & Setup Guide
════════════════════════════════════════════════════════════════

WHAT YOU HAVE
─────────────
  retro_console/
  ├── index.html              ← The console UI (open this in a browser)
  ├── update_manifest.py      ← Run this every time you add a game
  └── games/
      ├── manifest.json       ← Auto-generated list of games (don't edit by hand)
      └── example_game/
          ├── game_info.json  ← Game metadata (name, description, video, etc.)
          └── main.py         ← Your Python game file


────────────────────────────────────────────────────────────────
HOW TO RUN THE CONSOLE
────────────────────────────────────────────────────────────────

The browser needs to fetch the manifest.json and game_info.json
files via HTTP, so you can't just double-click index.html —
you need a simple local web server.

OPTION A — Python (easiest, no install needed)
  1. Open a terminal / command prompt
  2. cd into the retro_console/ folder
  3. Run:
       python -m http.server 8000
  4. Open your browser and go to:
       http://localhost:8000

OPTION B — VS Code Live Server extension
  1. Install "Live Server" extension in VS Code
  2. Right-click index.html → "Open with Live Server"

OPTION C — Node.js (if you have it)
  npx serve .


────────────────────────────────────────────────────────────────
HOW TO ADD A NEW GAME
────────────────────────────────────────────────────────────────

Step 1 — Create a folder for your game inside games/
  Example:  games/pacman/

Step 2 — Create game_info.json inside that folder
  Copy the template below and fill in your details:

  {
    "name":         "Pac-Man",
    "image_desc":   "Classic maze arcade game. Eat dots, avoid ghosts.",
    "video_src":    "https://www.youtube.com/embed/YOUR_VIDEO_ID?autoplay=1&mute=1&controls=0&loop=1&playlist=YOUR_VIDEO_ID",
    "genre":        "Maze",
    "release_year": 1980
  }

  ── Field notes ──────────────────────────────────────────────
  name          Display name shown in the game list
  image_desc    Short description shown in the preview panel
  video_src     YouTube embed URL for the preview (or "" for none)
  genre         Any genre label you like
  release_year  Year as a number (no quotes needed)
  ─────────────────────────────────────────────────────────────

Step 3 — Add your Python game file (e.g. pacman.py or main.py)
  The file must contain a run_game() function:

    def run_game():
        # your game logic here
        pass

    if __name__ == '__main__':
        run_game()

Step 4 — Run the manifest updater
  From the retro_console/ folder, run:
    python update_manifest.py

  This scans games/ and rebuilds manifest.json automatically.
  You'll see a ✔ for each game it finds.

Step 5 — Reload the browser
  Hit F5 or Ctrl+R — your game will appear in the list.


────────────────────────────────────────────────────────────────
HOW TO GET A YOUTUBE EMBED URL
────────────────────────────────────────────────────────────────

1. Find the game video on YouTube
2. Click Share → Embed
3. Copy just the VIDEO_ID from the URL (the part after /embed/)
4. Use this template:
   https://www.youtube.com/embed/VIDEO_ID?autoplay=1&mute=1&controls=0&loop=1&playlist=VIDEO_ID

If you don't have a video, just set "video_src" to "" and the
console will show "NO PREVIEW AVAILABLE" instead.


────────────────────────────────────────────────────────────────
CONSOLE CONTROLS
────────────────────────────────────────────────────────────────

  Keyboard:   ↑ / ↓ arrows to navigate, Enter to select
  Buttons:    ▲ UP / ▼ DOWN / ⏎ SELECT buttons at the bottom
  Mouse:      Click any game in the left panel
  Skin:       🎨 Skin button cycles through 4 color themes
              (Green → Yellow → Purple → Red)


────────────────────────────────────────────────────────────────
CONNECTING PYTHON GAME LAUNCH (ADVANCED / FUTURE STEP)
────────────────────────────────────────────────────────────────

Currently the SELECT button shows an alert as a placeholder.
To actually launch your Python game from the browser, you need
a small backend server. Example using Python + Flask:

  pip install flask

  # server.py
  from flask import Flask, request
  import importlib, sys, os

  app = Flask(__name__, static_folder='.', static_url_path='')

  @app.route('/')
  def index():
      return app.send_static_file('index.html')

  @app.route('/launch/<folder>')
  def launch(folder):
      path = os.path.join('games', folder)
      sys.path.insert(0, path)
      mod = importlib.import_module('main')
      mod.run_game()
      return 'ok'

  if __name__ == '__main__':
      app.run(port=8000)

Then in index.html, replace the alert() in launchGame() with:
  fetch(`/launch/${game._folder}`)

This is an optional advanced step — the console UI works fully
without it for browsing and previewing games.


────────────────────────────────────────────────────────────────
QUICK CHECKLIST
────────────────────────────────────────────────────────────────

  □ Each game has its own folder inside games/
  □ Each folder has a game_info.json with all 5 fields
  □ Each folder has a .py file with a run_game() function
  □ You ran update_manifest.py after adding/removing games
  □ You're serving via http.server (not opening the file directly)

════════════════════════════════════════════════════════════════
  Built for ICTLabs · Class Project Bootstrap
════════════════════════════════════════════════════════════════
