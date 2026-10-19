# Mavic 3 Flight Trainer

A browser-based 3D flight trainer for the DJI Mavic 3 and its RC-N1 remote. Learn the sticks, switches and buttons before you fly the real aircraft.

**Live:** https://razee4315.github.io/mavic3-flight-trainer/

Unofficial training project. Not affiliated with or endorsed by DJI.

## What it simulates

- **Stick modes 1, 2 and 3.** Mode 2 is the DJI default.
- **Flight modes with Mavic 3 spec speeds.** Cine is 5 m/s, Normal is 15 m/s and Sport is 21 m/s. Climb is 1, 6 or 8 m/s depending on the mode.
- **GPS position hold and braking.** Release the sticks and the drone stops and hovers. It leans into the wind to hold its spot.
- **ATTI mode.** With no GPS the drone drifts with the wind, and you have to hold it in place yourself.
- **Combination Stick Command.** Start and stop the motors with the sticks, like the real aircraft. Hold the throttle down after landing to stop the motors.
- **Obstacle sensing.** Braking and radar arcs work in Normal and Cine. Sensing is off in Sport mode, and thin power lines can't be detected (just like on the real drone).
- **Return to Home.** RTH climbs to the RTH altitude, flies home and lands. Smart low-battery RTH is included, plus a forced landing at critical battery.
- **Gimbal and camera.** The gimbal tilts from −90° to +35°, the Fn button recentres it, and you get 1x, 3x, 7x and 28x zoom, photos and video.
- **A 3D RC-N1 remote.** Two-part shell, recessed stick wells with grippy caps, a centre-column phone clamp and a DJI Fly-style screen. The sticks tilt, the C/N/S switch slides, the gimbal dial rolls and the buttons press. The phone shows the live camera feed.
- **A detailed Mavic 3.** Gloss-black visor with the forward vision sensors, sensors on every side, a stabilised gimbal with the main and tele lenses, folding-style arms and landing legs.
- **You, on the field.** The pilot stands by the home pad holding the remote, and their head and shoulders follow the drone.
- **Three views.** Chase (pulls back as you speed up and stays out of buildings), Camera (what DJI Fly shows), and Pilot (line of sight from where you stand, zooming in a little when the drone is far). The view keeps the drone above the docked remote.

## Lessons

1. Know your remote
2. Motors, takeoff and hover
3. Altitude and yaw
4. Forward, back and sideways
5. Square pattern, tail-in
6. Nose-forward circuit
7. Nose-in orientation
8. Orbit the water tower
9. Figure eight
10. Precision landing on a roof
11. Wind and ATTI mode
12. Return to Home
13. Cinematic shot

## Controls

| Real remote | Keyboard | Gamepad |
|---|---|---|
| Left stick | W A S D | Left stick |
| Right stick | Arrow keys (or I J K L) | Right stick |
| Start/stop motors (CSC) | S+D with ↓+← | Both sticks down and in |
| Flight mode C / N / S | 1 / 2 / 3 | D-pad ← ↑ → |
| Pause (tap) / RTH (hold) | Space or H | B |
| Auto takeoff / land (hold) | T | Start |
| Gimbal dial | Q / E | LT / RT |
| Fn (recentre gimbal) | F | LB |
| Shutter / record | P | A |
| Photo / video | V | X |
| Change view | C | Y |
| Menu | Esc | Back |

Hold Shift for gentle stick input. You can also drag the sticks on the 3D remote with the mouse, and touch screens get on-screen sticks.

## Run locally

Open `Mavic 3 Flight Trainer.html` in Chrome, Edge or Firefox. You need an internet connection for the first load, because Three.js and the fonts come from a CDN.

## Develop

The source lives in `src/app.html`. After editing it, run:

```bash
python build.py
```

This regenerates `index.html` (for GitHub Pages) and `Mavic 3 Flight Trainer.html`.
