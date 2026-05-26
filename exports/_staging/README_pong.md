# Pong — ICTLabs Retro Console Cartridge

**Game:** Pong  
**Genre:** Classic  
**Release Year:** 1972  
**Adapter Version:** pong_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad UP | Move your paddle up (continuous) |
| Trackpad DOWN | Move your paddle down (continuous) |
| SELECT | Start 1P game (idle) · Advance set (set break) · Replay (match over) |
| PAUSE | Pause / Resume |

Threshold: `|moveY| > 0.18` — low threshold for smooth, responsive feel.  
Movement is continuous and analog-feeling, capped at `PAD_SPD` per tick.

The ICT controller always controls the **right paddle** (Player 2 / YOU side).  
In 2-player mode, Player 1 (left paddle) still uses W / S keyboard keys.

### Desktop (Keyboard)

| Key | Action |
|---|---|
| ↑ / ↓ Arrow | Move right paddle |
| W / S | Move left paddle (2P only) |
| Enter | Start / Menu |

---

## Gameplay Notes

- 1 Player vs CPU or 2 Players local
- First to 7 points wins a set; best of 3 sets wins the match
- CPU difficulty scales with set number
- Ball accelerates slightly on each paddle hit
- Hit angle depends on contact point on the paddle
- Synthesized classic Pong bleeps (paddle hit, wall, score)
- Match result overlay with PLAY AGAIN / MAIN MENU

## Mobile Adapter Notes

- `ictMoveY` stored as float state, read inside `update()` alongside `keys[]`
- Keyboard path completely unmodified — both inputs coexist
- Fixed 60fps-equivalent game tick (accumulator pattern) — ball/paddle speed
  is device-rate-independent (120fps iPad same speed as 60fps desktop)
- Pause freezes game update only; canvas renders the frozen frame
- 30-frame cover-lock prevents stale SELECT on load
- SELECT defaults to 1P mode when starting from the title screen
- urlMode auto-start removed

## Known Limitations

- ICT controller controls right (YOU) paddle only; 2P left paddle always requires keyboard

---

*ICTLabs Retro Console — Integrated Computer Technology*
