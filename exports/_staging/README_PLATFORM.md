# ICTLabs Retro Console — Full Platform

**Platform Version:** v4.9.2  
**Cartridge Spec:** v2  
**Build Date:** 2026-05-26  
**Vendor:** ICTLabs / Integrated Computer Technology

---

## Supported Devices

| Device | Status |
|---|---|
| iPad / iOS Tablet | ✅ Full support — TRACKPAD controller |
| iPhone / iOS Phone | ✅ Full support — TRACKPAD controller |
| Android Tablet | ✅ Full support — TRACKPAD controller |
| Android Phone | ✅ Full support — TRACKPAD controller |
| Desktop / Laptop | ✅ Full support — Keyboard |
| macOS Safari | ✅ Tested |
| Chrome / Firefox / Edge | ✅ Tested |

---

## Runtime Architecture

The ICTLabs Retro Console is a single-page arcade shell (`arcade/index.html`) that loads
game cartridges into sandboxed `<iframe>` elements. Each cartridge is a self-contained
HTML5/JS file that receives controller input via the `window.ICTLabsInput` transport object.

```
arcade/index.html          ← Shell / Cabinet runtime
  └─ #gameFrame (iframe)  ← Cartridge slot
       └─ games/<game>/<game>.html
```

The shell owns:
- Touch overlay (#touchPanel)
- TRACKPAD analog controller
- D-pad directional pad
- A/B cluster buttons (FIRE, SELECT, PAUSE)
- CONTROLS toggle button
- Manifest loader (arcade/games/manifest.json)
- Cartridge iframe lifecycle

---

## Controller Architecture

### window.ICTLabsInput (Transport Object)

The shell writes controller state to `window.ICTLabsInput` on the iframe's content window
every 250ms and on every interaction event. Cartridges poll this object every frame.

```javascript
window.ICTLabsInput = {
  moveX:     Number,   // -1.0 → +1.0  (trackpad horizontal)
  moveY:     Number,   // -1.0 → +1.0  (trackpad vertical)
  magnitude: Number,   // 0.0 → 1.0    (stick magnitude)
  angle:     Number,   // radians       (stick angle)
  fire:      Boolean,  // FIRE button
  select:    Boolean,  // SELECT button
  cancel:    Boolean,  // PAUSE button
  close:     Boolean,  // CLOSE button
  pause:     Boolean,  // alias for cancel
}
```

### TRACKPAD Analog System

The TRACKPAD is a circular touch zone that generates normalized `moveX`/`moveY` values.
It supports:
- Analog steering (Zaxxon/GZ3, Pong, Galaga)
- Directional edge detection (Frogger, Snake, Pac-Man)
- DAS (Delayed Auto Shift) movement (Tetris)

Thresholds used by cartridges:
- `|moveX/Y| > 0.35` — grid-based games (Frogger, Snake, Pac-Man)
- `|moveX/Y| > 0.18` — analog games (Pong, Galaga)
- `|moveX/Y| > 0.18` — DAS games (Tetris)

### Keyboard Fallback

All cartridges support full keyboard fallback for desktop play:

| Key | Action |
|---|---|
| Arrow Keys | Movement |
| W / A / S / D | Movement (alternate) |
| Space | Fire / Serve / Start |
| Enter | Start / Select |
| P | Pause (where supported) |

---

## Game Library (Stable Cartridges)

| Game | Genre | Year | Adapter | Spec |
|---|---|---|---|---|
| Pac-Man | Maze | 1980 | pacman_input_v1.0 | v2 |
| Frogger | Arcade | 1981 | frogger_input_v1.0 | v2 |
| Galaga | Space Shooter | 1981 | galaga_input_v1.0 | v2 |
| Zaxxon / GZ3 | Space Shooter | 1982 | zaxxon_input_v1.0 | v2 |
| Tetris | Puzzle | 1984 | tetris_input_v1.0 | v2 |
| Snake | Classic | 1976 | snake_input_v1.0 | v2 |
| Pong | Classic | 1972 | pong_input_v1.0 | v2 |

All cartridges listed above are confirmed stable on iPad, phone, and desktop.

---

## Mobile Support

- Touch overlay appears via CONTROLS button
- TRACKPAD handles all analog movement
- SELECT button starts, restarts, and continues games
- PAUSE button pauses and resumes
- FIRE button shoots / acts
- All cartridges implement 30-frame cover-lock to prevent stale launch pulses
- No keyboard emulation — pure ICTLabsInput transport

---

## Desktop Support

- Full keyboard support preserved on all cartridges
- Overlay hidden by default on desktop
- Mouse can trigger the touch overlay if desired

---

## Folder Structure

```
arcade/
  index.html                    ← Main shell (v4.9.2)
  GAME_DEV_SPEC.md              ← Cartridge developer specification
  update_manifest.py            ← Manifest utility
  games/
    manifest.json               ← Game registry
    frogger/
      frogger.html
      game_info.json
    galaga/
      galaga.html
      game_info.json
    pacman/
      pacman.html
      game_info.json
    pong/
      pong.html
      game_info.json
    snake/
      snake.html
      game_info.json
    tetris/
      tetris.html
      game_info.json
    zaxxon/
      zaxxon.html
      game_info.json
```

---

*ICTLabs Retro Console — Integrated Computer Technology*
