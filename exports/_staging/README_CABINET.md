# ICTLabs Arcade Cabinet — Shell Runtime

**Shell Version:** v4.9.2  
**Cartridge Spec Supported:** v2  
**Build Date:** 2026-05-26  
**Vendor:** ICTLabs / Integrated Computer Technology

---

## Overview

The ICTLabs Arcade Cabinet is a reusable HTML5 arcade shell and controller runtime.
It provides:
- A complete touch controller ecosystem for mobile/tablet
- Full keyboard support for desktop
- An iframe-based cartridge loading framework
- A manifest-driven game registry
- A standardized input transport layer (`window.ICTLabsInput`)

Cartridge developers only need to write a game HTML file and wire the
`window.ICTLabsInput` transport to receive controller input.

---

## Shell Architecture

### Entry Point: `arcade/index.html`

The shell is a single self-contained HTML file. It handles:
- Manifest fetch and game menu rendering
- Cartridge loading into `#gameFrame` (sandboxed `<iframe>`)
- Touch overlay lifecycle (open/close, panel states)
- Controller signal generation and transport to the active cartridge

### Iframe Cartridge Model

Each game is loaded into a sandboxed iframe:

```javascript
gameFrame.src = game.play_url;   // e.g. "games/tetris/tetris.html"
```

The shell pushes controller state to the iframe every 250ms and on every user interaction:

```javascript
frame.contentWindow.ICTLabsInput = input;
```

The cartridge polls this object every frame using:

```javascript
function getICTInput() {
  return (
    window.ICTLabsInput ||
    (window.parent && window.parent.ICTLabsInput) ||
    null
  );
}
```

---

## window.ICTLabsInput Transport

The controller abstraction layer. Written by the shell, read by cartridges.

```javascript
{
  moveX:     Number,   // -1.0 → +1.0   trackpad horizontal axis
  moveY:     Number,   // -1.0 → +1.0   trackpad vertical axis
  magnitude: Number,   // 0.0  → 1.0    trackpad stick magnitude
  angle:     Number,   // radians        trackpad stick angle
  fire:      Boolean,  // FIRE button    (hold-capable)
  select:    Boolean,  // SELECT button  (pulse, 120ms)
  cancel:    Boolean,  // PAUSE button   (pulse, 120ms)
  close:     Boolean,  // CLOSE button   (exits cartridge)
  pause:     Boolean,  // alias → cancel
}
```

Boolean signals are pulsed via `pulse(prop, 120ms)` which sets them true,
calls `pushInput()`, then resets after 120ms. `pushInput()` writes the
full state object to `frame.contentWindow.ICTLabsInput`.

---

## TRACKPAD System

A circular analog touch zone. Outputs normalized `moveX` / `moveY`.

- Dead zone: inner ~10% of the circle
- Output range: -1.0 to +1.0 on each axis
- Supports: steering, edge detection, DAS movement

---

## Touch Panel Layout

| Element | Purpose |
|---|---|
| `#touchPanel` | Full overlay panel, shown via CONTROLS button |
| `#dpad` | Digital D-pad (fires ArrowKey events via postMessage) |
| `#aFire` | FIRE button |
| `#aSelect` | SELECT button |
| `#aCancel` | PAUSE button |
| `#touchToggle` | CONTROLS toggle button (opens/closes panel) |

---

## Manifest Architecture

`arcade/games/manifest.json` is an array of game objects:

```json
[
  {
    "name": "TETRIS",
    "genre": "Puzzle",
    "release_year": 1984,
    "play_url": "games/tetris/tetris.html",
    "image_desc": "...",
    "video_src": "..."
  }
]
```

The shell fetches this at startup and renders the game selection menu.
Adding a new cartridge only requires:
1. Adding a game folder under `arcade/games/`
2. Adding an entry to `manifest.json`
3. Wiring `window.ICTLabsInput` in the cartridge

---

## Cartridge Spec v2 Requirements

Cartridges must implement:

1. `getICTInput()` polling function (poll every frame)
2. `pollICTInput()` called from the game loop
3. 30-frame cover-lock arming guard on SELECT at load
4. Edge detection for one-shot signals (SELECT, CANCEL)
5. Runtime header comment:

```javascript
/*
Game: <Name>
Adapter Version: <name>_input_v1.0
Console Target: v4.9.2+
Spec Version: v2
*/
```

---

## Mobile Support Notes

- Overlay hidden by default; shown via CONTROLS toggle
- All input routed through `window.ICTLabsInput` — no keyboard simulation
- Cover-lock prevents stale SELECT pulses from auto-starting cartridges
- AudioContext resumed automatically when ICT input arrives

---

## Desktop Support Notes

- Keyboard controls remain fully functional (not intercepted by shell)
- Arrow keys, WASD, Space, Enter all pass through to active cartridge
- Touch overlay available but optional on desktop

---

## Package Contents

```
arcade/
  index.html              ← Main shell (v4.9.2)
  GAME_DEV_SPEC.md        ← Cartridge developer specification
  update_manifest.py      ← Manifest generation utility
  games/
    manifest.json         ← Game registry
```

*(Game cartridges not included — see individual cartridge packages)*

---

*ICTLabs Retro Console — Integrated Computer Technology*
