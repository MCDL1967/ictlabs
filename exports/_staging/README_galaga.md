# Galaga — ICTLabs Retro Console Cartridge

**Game:** Galaga  
**Genre:** Space Shooter  
**Release Year:** 1981  
**Adapter Version:** galaga_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad LEFT / RIGHT | Move ship left / right (continuous, analog) |
| FIRE (hold) | Shoot continuously |
| SELECT | Start game / Restart |
| PAUSE | Pause / Resume |

Threshold: `|moveX| > 0.18` — responsive analog feel.

### Desktop (Keyboard)

| Key | Action |
|---|---|
| ← / → Arrow | Move ship |
| Space | Shoot |
| Enter | Start game |
| P | Pause |

---

## Gameplay Notes

- Defend against waves of Galaga insect enemies
- Enemies dive-bomb in formation patterns
- Tractor beam can capture your fighter — recapture for dual ship
- Progressive difficulty — wave count increases enemy speed and aggression
- Synthesized arcade audio

## Mobile Adapter Notes

- Continuous analog movement — no edge detection or latching
- FIRE is hold-capable (continuous fire while pressed)
- Ship movement speed is `PLAYER_SPD` per frame, applied every poll tick
- Pause freezes rendering and game update; PAUSED banner drawn over frozen frame
- 30-frame cover-lock prevents stale SELECT from skipping title screen

## Known Limitations

- None

---

*ICTLabs Retro Console — Integrated Computer Technology*
