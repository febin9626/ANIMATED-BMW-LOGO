# ANIMATED-BMW-LOGO
🏎️ Animated BMW Logo in Python Turtle Graphics
*“The Ultimate Driving Machine”*

[![Python 3.x](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Graphics](https://img.shields.io/badge/graphics-Python%20Turtle-green.svg)](https://docs.python.org/3/library/turtle.html)
[![Dependencies](https://img.shields.io/badge/dependencies-zero%20(stdlib)-brightgreen.svg)](#prerequisites)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](#license)

A high-performance, interactive, and visually faithful recreation of the iconic **BMW Roundel Emblem** engineered using Python's built-in `turtle` graphics library.

---

## 📸 Overview

This project renders an authentic BMW badge within a sleek, dark-cockpit instrument cluster environment, featuring:
- An introductory progressive assembly animation.
- A butter-smooth **60 FPS** continuous rotating center roundel (paying homage to BMW’s historic aviation propeller heritage).
- A dynamic engine throttle simulator with flywheel drag physics.
- Real-time digital telemetry HUD with a live tachometer rev-meter.
- An interactive **BMW ///M-Sport Heritage Mode**.

---

## ✨ Features

### 1. 🎯 Authentic BMW Geometry & Design
- **Official Bavarian Colors**: Uses authentic Alpine White (`#FFFFFF`) and Bavarian Blue (`#0066B1`).
- **Exact Quadrant Orientation**: Arranged clockwise from top-left:
  1. **Top-Left**: Alpine White
  2. **Top-Right**: Bavarian Blue
  3. **Bottom-Right**: Alpine White
  4. **Bottom-Left**: Bavarian Blue
- **Radially Arched Typography**: The letters **`B`**, **`M`**, and **`W`** are curved along the upper black band with 3D drop-shadows:
  - **`B`**: Positioned at $135^\circ$ (tilted $+45^\circ$)
  - **`M`**: Positioned at $90^\circ$ (top-dead-center, upright)
  - **`W`**: Positioned at $45^\circ$ (tilted $-45^\circ$)
- **3D Metallic Bevels & Dome Reflection**: Outer chrome rings with highlights and shadows, plus a specular gloss arc simulating an enamel dome reflection.

### 2. ⚡ High-Performance 60 FPS Multi-Turtle Engine
- Uses `screen.tracer(0)` and a decoupled multi-turtle architecture:
  - `bg_turtle`: Static instrument-cluster backdrop and ambient ticks (drawn once).
  - `frame_turtle`: Outer chrome bezels and black band (drawn once).
  - `roundel_turtle`: Spinning central quadrants and crosshairs (redrawn each frame).
  - `hud_turtle`: Live digital telemetry HUD and tachometer bar (updated dynamically).
- Delivers fluid, tear-free, flicker-free rendering with low CPU overhead.

### 3. 🏁 Interactive Engine Revving & Flywheel Physics
- **Click or press Enter** to floor the accelerator pedal! The engine spikes instantly to **6,800 RPM** redline.
- Realistic rotational drag and momentum decay formula:
  $$\text{RPM}_{t} = \text{RPM}_{\text{base}} + (\text{RPM}_{t-1} - \text{RPM}_{\text{base}}) \times 0.94$$
- Live color-shifting tachometer bar:
  - **Blue / Cyan**: Idle and cruising range ($< 4,000\text{ RPM}$)
  - **Warm Amber**: High powerband ($4,000 - 6,000\text{ RPM}$)
  - **Redline**: Maximum throttle ($> 6,000\text{ RPM}$)

### 4. 🔴🔵 ///M-Sport Performance Mode
- Press **`M`** to toggle the BMW M-Power Heritage Edition:
  - Displays the iconic BMW M tri-color arcs (**Light Blue**, **Dark Blue**, **Red**) along the outer bezel.
  - Switches the cockpit HUD into sport mode.
  - Automatically boosts cruise RPM to $240\text{ RPM}$.

---

## 🎮 Interactive Controls

| Key / Input | Action | Description |
| :--- | :--- | :--- |
| **Mouse Click** | **Rev Throttle** | Spikes RPM to 6,800 with realistic deceleration |
| **Enter** | **Rev Throttle** | Keyboard alternative to throttle rev |
| **Spacebar** | **Pause / Play** | Freezes or resumes the rotation animation |
| **Up Arrow ($\uparrow$)** | **Speed Up** | Increases cruise RPM by $+30\text{ RPM}$ |
| **Down Arrow ($\downarrow$)** | **Slow Down** | Decreases cruise RPM by $-30\text{ RPM}$ |
| **M** | **///M-Sport Mode** | Toggles M-Sport tri-color racing stripes & HUD |
| **R** | **Reverse Spin** | Inverts rotation direction (Clockwise $\leftrightarrow$ CCW) |
| **Esc / Q** | **Exit** | Gracefully closes the window |

---

## 🛠️ Prerequisites

- **Python 3.8+** (Tested on Python 3.8 through 3.14)
- **Standard Library Only**:
  - `turtle` (built-in)
  - `tkinter` (built-in with standard Python installations)
  - `math` (built-in)
  - `time` (built-in)
- **Zero third-party installations** (`pip install` is NOT required).

---

## 🚀 Quick Start

### 1. Open Terminal or PowerShell
Navigate to the project folder:
```powershell
cd "C:\Users\febin\.gemini\antigravity\scratch\bmw_logo"
```

### 2. Launch the Application
```powershell
python bmw_logo.py
```

> 💡 **Tip**: If you want to skip the opening assembly intro and immediately start continuous high-speed spinning, click anywhere or press the **Spacebar**.

---

## 📂 Project Structure

```text
bmw_logo/
├── bmw_logo.py      # Main Python turtle application
└── README.md        # Comprehensive documentation and controls guide
```

---

## ⚙️ Customization Guide

You can easily tweak constants near the top of `bmw_logo.py` to customize the experience:

```python
# Change base cruising speed (default: 120 RPM)
base_rpm = 150.0

# Change logo scale by adjusting radii
R_OUTER_BEZEL = 208
R_ROUNDEL = 114
R_TEXT = 157

# Modify official colors
COLOR_BLUE = "#0066B1"   # Bavarian Blue
COLOR_WHITE = "#FFFFFF"  # Alpine White
```

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
