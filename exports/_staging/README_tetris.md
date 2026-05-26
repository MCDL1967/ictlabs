# Tetris — ICTLabs Retro Console Cartridge

**Game:** Tetris  
**Genre:** Puzzle  
**Release Year:** 1984  
**Adapter Version:** tetris_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad LEFT / RIGHT | Move piece left / right (DAS) |
| Trackpad DOWN | Soft drop (DAS) |
| Trackpad UP | Rotate piece |
| SELECT | Rotate piece / Start game |
| FIRE | Hard drop |
| PAUSE | Pause / Resume |

**DAS Timings:** Initial delay 160ms, repeat rate 50ms — standard Tetris feel.

### Desktop (Keyboard)

| Key | Action |
|---|---|
| ← / → Arrow | Move left / right |
| ↓ Arrow | Soft drop |
| ↑ Arrow | Rotate |
| Space | Hard drop |
| Enter | Start / Rotate |
| P | Pause / Resume |

---

## Gameplay Notes

- Hold piece mechanic included (C key on desktop)
- Ghost piece shows landing position
- Line clear scoring: 100 / 300 / 500 / 800 (1 / 2 / 3 / 4 lines)
- Speed increases every 5 levels
- Synthesized chiptune audio

## Mobile Adapter Notes

- Trackpad UP uses edge detection (one rotate per push, release to repeat)
- DAS (Delayed Auto Shift) provides standard Tetris lateral movement feel
- SELECT acts as rotate (same as UP) for ergonomic one-thumb play
- FIRE as hard drop is intentionally fire-button-only (not trackpad push)
- 30-frame cover-lock prevents auto-start on load

## Known Limitations

- None

---

*ICTLabs Retro Console — Integrated Computer Technology*
