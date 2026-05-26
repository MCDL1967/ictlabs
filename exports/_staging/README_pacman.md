# Pac-Man — ICTLabs Retro Console Cartridge

**Game:** Pac-Man  
**Genre:** Maze  
**Release Year:** 1980  
**Adapter Version:** pacman_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad UP | Queue turn UP |
| Trackpad DOWN | Queue turn DOWN |
| Trackpad LEFT | Queue turn LEFT |
| Trackpad RIGHT | Queue turn RIGHT |
| SELECT | Start game (idle) · Continue (dead_wait) · Restart (gameover) |
| PAUSE | Pause / Resume |

Threshold: `|moveX/Y| > 0.35` — one directional intent per push, release to repeat.  
Turns are queued and executed when Pac-Man reaches a tile-aligned intersection.

### Desktop (Keyboard)

| Key | Action |
|---|---|
| Arrow Keys | Queue direction |
| W / A / S / D | Queue direction |
| Space | Start / Continue |

---

## Gameplay Notes

- 19×21 tile grid; cell-to-cell movement with smooth pixel interpolation
- Queued direction system: input buffered until legal turn is available
- Power pellets frighten ghosts (blue) — eat them for 200–1600 points
- 4 ghosts: each has unique exit delay and behavior weight
- Level clear resets map; speed and ghost aggression increase per wave
- Synthesized waka-waka audio, power pulse, ghost-eat, death jingle

## Mobile Adapter Notes

- Queued direction feeds `pac.wantDx`/`pac.wantDy` directly (game's native queue)
- Game's tile-alignment turn execution is fully preserved
- Per-direction latches ensure one intent per push — no rapid-fire spam
- Fixed 60fps-equivalent game tick (accumulator pattern) — device-rate-independent
- Idle-state draw guard (`!map || !pac`) prevents crash before game starts
- 30-frame cover-lock prevents stale SELECT on load
- Difficulty buttons on title screen: BEGINNER / INTERMEDIATE / ADVANCED
- SELECT defaults to last-selected difficulty

## Known Limitations

- None

---

*ICTLabs Retro Console — Integrated Computer Technology*
