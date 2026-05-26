# Frogger — ICTLabs Retro Console Cartridge

**Game:** Frogger  
**Genre:** Arcade  
**Release Year:** 1981  
**Adapter Version:** frogger_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad UP | Hop forward (toward homes) |
| Trackpad DOWN | Hop backward |
| Trackpad LEFT | Hop left |
| Trackpad RIGHT | Hop right |
| SELECT | Start game / Respawn / Restart |
| PAUSE | Pause / Resume |

Threshold: `|moveX/Y| > 0.35` — one hop per push, require release to re-fire.  
Movement locks for 120ms after each hop (moveLock) for grid correctness.

### Desktop (Keyboard)

| Key | Action |
|---|---|
| ↑ Arrow | Hop up |
| ↓ Arrow | Hop down |
| ← / → Arrow | Hop left / right |
| Space | Start |

---

## Gameplay Notes

- Grid-based hop movement — each input advances frog one full cell
- Cross the road (avoid cars) and river (ride logs/turtles) to reach home slots
- Reaching a home slot scores points and starts a new frog
- All 5 homes filled → level complete, difficulty increases
- Countdown timer per life — runs out = lose a life
- Timer pauses correctly while PAUSED
- Level number displayed in HUD
- Synthesized hop, death, and level-complete sounds

## Mobile Adapter Notes

- Per-direction latch system: `ictLUp/Down/Left/Right` — one hop per direction per push
- Release-required: holding a direction does NOT cause repeated hopping
- Deliberate, arcade-like movement feel as specified
- moveLock reused from keyboard path for consistent grid behavior
- Pause patches `timerInterval` to prevent countdown during pause
- 30-frame cover-lock prevents stale SELECT on load
- urlMode auto-start removed (shell always passes ?mode=1p)

## Known Limitations

- None

---

*ICTLabs Retro Console — Integrated Computer Technology*
