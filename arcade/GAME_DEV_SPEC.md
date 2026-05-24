# ICTLabs Retro Console — Game Developer Spec
**Version 1.0 · May 2026**

---

## Overview

The ICTLabs Retro Console is a browser-based arcade platform that loads games dynamically from a manifest. Adding a new game is a drop-in operation — no changes to the console shell required.

---

## File Structure

Each game lives in its own folder under `arcade/games/`:

```
arcade/
├── index.html              ← Console shell (do not modify)
├── games/
│   ├── manifest.json       ← Game registry (edit to add games)
│   └── your_game/
│       ├── your_game.html  ← Game file (self-contained)
│       ├── game_info.json  ← Metadata
│       └── main.py         ← Local launcher stub (optional)
```

---

## Step 1 — Register the Game

Edit `arcade/games/manifest.json`:

```json
{
  "games": [
    "galaga",
    "pong",
    "snake",
    "pacman",
    "zaxxon",
    "frogger",
    "your_game"
  ]
}
```

Order determines the list order in the console.

---

## Step 2 — Create `game_info.json`

```json
{
  "name": "YOUR GAME",
  "image_desc": "One sentence description shown in the console preview panel.",
  "video_src": "https://www.youtube.com/embed/VIDEO_ID?autoplay=1&mute=1&controls=0&loop=1&playlist=VIDEO_ID",
  "genre": "Shooter",
  "release_year": 1984,
  "play_url": "games/your_game/your_game.html",
  "multiplayer": false
}
```

### Fields

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `name` | string | ✅ | Displayed in list and preview. Use ALL CAPS. |
| `image_desc` | string | ✅ | 1-2 sentences. Shown above preview. |
| `video_src` | string | ✅ | YouTube embed URL. Must allow embedding. Use `?autoplay=1&mute=1&controls=0&loop=1&playlist=ID` |
| `genre` | string | ✅ | Displayed in subtitle. E.g. `Classic`, `Shooter`, `Maze`, `Arcade` |
| `release_year` | number | ✅ | Original release year of the game being recreated. |
| `play_url` | string | ✅ | Relative path from `arcade/` to the game HTML file. |
| `multiplayer` | boolean | ✅ | If `true`, the **2 PLAYERS** button activates when this game is selected. |

---

## Step 3 — Build the Game HTML

The game must be a **single self-contained HTML file**. No external dependencies except Google Fonts and Web Audio API.

### Required behaviors

**1. Font**
Use Audiowide for all UI text (title screen, score, messages):
```html
<link href="https://fonts.googleapis.com/css2?family=Audiowide&display=swap" rel="stylesheet">
```

**2. Auto-start from console**
The console passes `?mode=1p` or `?mode=2p` via URL parameter. Read it and start the game immediately (skip the title screen):

```javascript
const urlMode = new URLSearchParams(window.location.search).get('mode');
if (urlMode) startGame(urlMode); // '1p' or '2p'
```

If the game does not support 2P, ignore the `2p` value and start normally.

**3. Canvas sizing**
Use responsive scaling so the game fills the right panel iframe cleanly:

```javascript
const W = 640, H = 480; // or your preferred resolution
canvas.width = W; canvas.height = H;

function resize() {
  const s = Math.min(window.innerWidth / W, (window.innerHeight - 52) / H);
  canvas.style.width  = (W * s) + 'px';
  canvas.style.height = (H * s) + 'px';
}
resize();
window.addEventListener('resize', resize);
```

**4. Web Audio — synthesized sound**
Do NOT use audio files or external sound libraries. All sounds must be synthesized via Web Audio API. This ensures the game works without network requests and respects copyright.

```javascript
const AC = new (window.AudioContext || window.webkitAudioContext)();

// Always resume on first keydown (browser autoplay policy)
document.addEventListener('keydown', () => {
  if (AC.state === 'suspended') AC.resume();
}, { once: false });

// Example synthesized sound
function sfxShoot() {
  const o = AC.createOscillator(), g = AC.createGain();
  o.connect(g); g.connect(AC.destination);
  o.type = 'square'; o.frequency.value = 880;
  g.gain.setValueAtTime(0.15, AC.currentTime);
  g.gain.exponentialRampToValueAtTime(0.001, AC.currentTime + 0.08);
  o.start(); o.stop(AC.currentTime + 0.09);
}
```

Synthesize sounds to approximate the original arcade. For noise bursts (explosions), use `createBuffer` with random data filtered through a `BiquadFilter`.

**5. Exit via ESC**
The console handles ESC to exit the game back to the preview panel. The game should not intercept or block ESC.

---

## Instructions Registration

To add "How To Play" instructions for your game, edit `arcade/index.html` and add an entry to the `INSTRUCTIONS` object in the script:

```javascript
const INSTRUCTIONS = {
  // ... existing games ...
  your_game: {
    title: 'YOUR GAME — Controls',
    body: 'Arrow keys or WASD to move\nSpace to fire\n\nObjective description here.\nScoring: item = X pts'
  }
};
```

Use `\n` for line breaks. The key must match the folder name exactly.

---

## 1P / 2P Support

If your game supports 2 players, set `"multiplayer": true` in `game_info.json`. The console will activate the **2 PLAYERS** button when your game is selected.

Your game should check the URL param and branch accordingly:

```javascript
function startGame(mode) {
  const is2P = mode === '2p';
  // set up player 2 controls if is2P
}

const urlMode = new URLSearchParams(window.location.search).get('mode');
if (urlMode) startGame(urlMode);
```

**Suggested key mappings:**
- Player 1: `W/S/A/D` or `Arrow Keys`
- Player 2: `I/K/J/L` or `Numpad`

---

## UI Standards

| Element | Spec |
|---------|------|
| Font | Audiowide |
| Score display | Top bar, 11px, letter-spacing: 2px |
| Player message (flash) | Centered, 14-22px, #ff0, blink animation |
| Overlay (title/game over) | `rgba(0,0,0,0.88)` background, centered |
| Start button | Transparent, border 2px solid accent color |
| Accent color | Game-specific (Galaga=yellow, Pong=white, Snake=green, Pac-Man=yellow, Frogger=green, Zaxxon=yellow) |

---

## Checklist Before Submitting

```
□ manifest.json updated with folder name
□ game_info.json complete with all required fields
□ YouTube video ID tested for embed support
□ Game starts immediately when ?mode= param is present
□ Canvas scales correctly in iframe (640×480 base recommended)
□ All sounds synthesized via Web Audio API — no audio files
□ Font is Audiowide
□ ESC key not intercepted
□ Game over screen has PLAY AGAIN option
□ Instructions added to INSTRUCTIONS object in arcade/index.html
□ multiplayer flag set correctly in game_info.json
```

---

## Example: Minimal Game Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<title>MY GAME</title>
<link href="https://fonts.googleapis.com/css2?family=Audiowide&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#000;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;overflow:hidden;font-family:'Audiowide',sans-serif;}
canvas{display:block;image-rendering:pixelated;}
#ui{color:#fff;font-size:11px;letter-spacing:2px;margin-bottom:6px;}
#overlay{position:fixed;inset:0;background:rgba(0,0,0,0.88);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;z-index:10;}
#overlay h1{font-size:clamp(32px,6vw,60px);color:#ff0;margin-bottom:20px;letter-spacing:6px;}
.btn{background:transparent;border:2px solid #ff0;color:#ff0;font-family:'Audiowide',sans-serif;font-size:13px;letter-spacing:2px;padding:13px 48px;cursor:pointer;}
.btn:hover{background:#ff0;color:#000;}
</style>
</head>
<body>
<div id="ui">SCORE: <b id="sc">0</b></div>
<canvas id="c"></canvas>
<div id="overlay">
  <h1>MY GAME</h1>
  <button class="btn" id="startBtn">START GAME</button>
</div>
<script>
const canvas=document.getElementById('c'),ctx=canvas.getContext('2d');
const W=640,H=480;
canvas.width=W;canvas.height=H;
function resize(){const s=Math.min(window.innerWidth/W,(window.innerHeight-52)/H);canvas.style.width=(W*s)+'px';canvas.style.height=(H*s)+'px';}
resize();window.addEventListener('resize',resize);

const AC=new(window.AudioContext||window.webkitAudioContext)();
document.addEventListener('keydown',()=>{if(AC.state==='suspended')AC.resume();});

let score=0,gstate='idle';

function startGame(mode){
  document.getElementById('overlay').style.display='none';
  gstate='playing';
  // Initialize your game here
}

document.getElementById('startBtn').onclick=()=>startGame('1p');
document.addEventListener('keydown',e=>{
  if(gstate==='idle'&&e.code==='Space') startGame('1p');
});

function loop(){
  requestAnimationFrame(loop);
  if(gstate==='playing'){
    // Update game logic here
  }
  // Draw here
  ctx.fillStyle='#000';ctx.fillRect(0,0,W,H);
}

loop();
// Auto-start from console
const urlMode=new URLSearchParams(window.location.search).get('mode');
if(urlMode)startGame(urlMode);
</script>
</body>
</html>
```

---

*ICTLabs Retro Console · ict-labs.com*
