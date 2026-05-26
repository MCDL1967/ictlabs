# Zaxxon / GZ3 — ICTLabs Retro Console Cartridge

**Game:** Zaxxon — GZ3 Edition  
**Genre:** Space Shooter (3D Isometric)  
**Release Year:** 1982  
**Adapter Version:** zaxxon_input_v1.0  
**Console Target:** v4.9.2+  
**Cartridge Spec:** v2  
**Visual Polish:** gz3_visual_v1.0

---

## Controls

### Mobile / Tablet (ICTLabsInput)

| Input | Action |
|---|---|
| Trackpad LEFT / RIGHT | Strafe ship horizontally (analog, continuous) |
| Trackpad UP / DOWN | Climb / Descend altitude (analog, damped 0.7×) |
| FIRE (hold) | Shoot — rate-limited by fireCooldown |
| SELECT | Start game / Restart / Respawn |
| PAUSE | Pause / Resume |

Altitude is damped at 0.7× horizontal speed for arcade-accurate feel.  
Threshold: `moveX/Y` applied proportionally — no dead zone cutoff (pure analog).

### Desktop (Keyboard)

| Key | Action |
|---|---|
| ← / → Arrow or A / D | Strafe left / right |
| ↑ / ↓ Arrow or W / S | Climb / Descend |
| Space | Shoot |
| Enter | Start / Respawn |

---

## Gameplay Notes

- Forward-scrolling 3D isometric fortress assault (Three.js)
- Fly through enemy waves — fighters, turrets, the Zaxxon boss
- Collect fuel tanks to replenish fuel (game ends at zero fuel)
- Altitude meter: HUD bar + 3D indicator on right edge of playfield
- Boss requires multiple hits; progressively harder waves
- Synthesized explosion and weapon audio

## GZ3 Visual Pass (gz3_visual_v1.0)

- Premium title screen: ICTLabs · GZ3 badge, animated neon ZAXXON title
- Controller hint strip on cover screen
- Reinhard tone mapping, deep-space blue atmosphere
- Upgraded lighting: strong blue-white key + hot orange rim + cool fill
- Enhanced materials: crisper player ship, vivid enemies, brighter boss
- Larger multi-color explosions with quadratic flash falloff
- Forward headlight on player ship illuminates obstacles ahead
- Dual-layer starfield with blue-tinted distant stars
- Gradient HUD bars, dark-panel PAUSED overlay

## Mobile Adapter Notes

- Strict 30-frame cover-lock with consecutive-false counter
- urlMode auto-start disabled (shell passes ?mode=1p — ignored)
- Smooth analog movement — no edge detection, no latching
- FIRE continuous while held; fireCooldown provides rate limiting
- Pause preserves exact game frame (Three.js render stops)

## Known Limitations

- None

---

*ICTLabs Retro Console — Integrated Computer Technology*
