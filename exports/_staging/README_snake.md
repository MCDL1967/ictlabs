# Snake — ICTLabs Retro Console Cartridge

**Game:** Snake  
**Genre:** Classic  
**Release Year:** 1976  
**Adapter Version:** snake_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad UP | Turn snake UP |
| Trackpad DOWN | Turn snake DOWN |
| Trackpad LEFT | Turn snake LEFT |
| Trackpad RIGHT | Turn snake RIGHT |
| SELECT | Start game / Retry |
| PAUSE | Pause / Resume |

Threshold: `|moveX/Y| > 0.35` — one direction change per push, release to repeat.  
Reverse-into-self is blocked (cannot turn 180° instantly).

### Desktop (Keyboard)

| Key | Action |
|---|---|
| Arrow Keys | Steer |
| W / A / S / D | Steer |
| Space | Start / Retry |

---

## Gameplay Notes

- 28×22 grid, cell-to-cell movement via setInterval tick
- Speed increases each level (level up every 5 food eaten per level tier)
- Eat 🍎 food to grow and score 10 × level points
- ⭐ Bonus star (5× points) appears randomly — grab it before it expires
- Countdown ring shows remaining bonus time
- Level-up fanfare with brief message
- Animated snake head with tongue flick
- Synthesized eat, bonus, level, and death sounds

## Mobile Adapter Notes

- Input polled via dedicated `requestAnimationFrame` loop — 60fps responsiveness
  independent of the `setInterval` game tick rate
- Per-direction latches: one turn per push, release required for repeat
- Reverse prevention: `d.x === dir.x*-1 && d.y === dir.y*-1` check mirrors keyboard guard
- Pause stops `setInterval` tick entirely (`gameLoop = null`) and restarts it on resume
- 30-frame cover-lock prevents stale SELECT on load
- urlMode auto-start removed

## Known Limitations

- None

---

*ICTLabs Retro Console — Integrated Computer Technology*
