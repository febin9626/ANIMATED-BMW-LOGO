"""
=============================================================================
             BMW ANIMATED LOGO - PYTHON TURTLE GRAPHICS
                "KL 13 AY 4411"
=============================================================================
PROJECT DEVELOPED BY FEBIN 
=============================================================================
"""

import turtle
import math
import time

# ---------------------------------------------------------------------------
# Visual Configuration & Dimensions
# ---------------------------------------------------------------------------
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 800

# Color Palette
COLOR_BG = "#0A0B0E"            # Cockpit dark carbon backdrop
COLOR_AMB_RING = "#181A22"      # Gauge ambient ring
COLOR_CHROME_LIGHT = "#F8FAFC"  # Outer chrome highlight
COLOR_CHROME_MID = "#94A3B8"    # Metallic bevel
COLOR_CHROME_DARK = "#334155"   # Shadow rim
COLOR_BLACK_RING = "#0F1115"    # Outer typography ring
COLOR_DIVIDER = "#CBD5E1"       # Dividing crosshair silver

# Official BMW Roundel Colors
COLOR_WHITE = "#FFFFFF"         # Alpine White
COLOR_BLUE = "#0066B1"          # Bavarian Blue

# BMW M-Power Colors
M_LIGHT_BLUE = "#00A3E0"        # BMW M Light Blue
M_DARK_BLUE = "#00205B"         # BMW M Dark Blue / Velvet
M_RED = "#E21A21"               # BMW M Red

# Emblem Dimensions (Radii in pixels)
R_OUTER_BEZEL = 208
R_OUTER_RIM = 202
R_INNER_BEZEL = 194
R_BLACK_RING_INNER = 120
R_ROUNDEL = 114
R_TEXT = 157                    # Centered between R=120 and R=194

# ---------------------------------------------------------------------------
# Application State
# ---------------------------------------------------------------------------
is_running = True
is_intro_done = False
is_paused = False
current_angle = 0.0
base_rpm = 120.0
current_rpm = base_rpm
spin_direction = -1   # -1 = Clockwise, 1 = Counter-Clockwise
m_mode = False
intro_step = 0

# ---------------------------------------------------------------------------
# Setup Screen & Turtles
# ---------------------------------------------------------------------------
screen = turtle.Screen()
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
screen.title("BMW - The Ultimate Driving Machine | Animated Turtle Graphics")
screen.bgcolor(COLOR_BG)
screen.tracer(0)

# Multi-layer Turtles (enables independent redraws with zero flicker)
bg_turtle = turtle.Turtle()
bg_turtle.hideturtle()
bg_turtle.speed(0)

frame_turtle = turtle.Turtle()
frame_turtle.hideturtle()
frame_turtle.speed(0)

roundel_turtle = turtle.Turtle()
roundel_turtle.hideturtle()
roundel_turtle.speed(0)

hud_turtle = turtle.Turtle()
hud_turtle.hideturtle()
hud_turtle.speed(0)

intro_turtle = turtle.Turtle()
intro_turtle.hideturtle()
intro_turtle.speed(0)

# ---------------------------------------------------------------------------
# Drawing Helper Functions
# ---------------------------------------------------------------------------
def draw_circle(t, x, y, radius, fill_color=None, border_color=None, border_width=1):
    """Draws a centered circle at (x, y) with specified fill and border."""
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    if border_color:
        t.pencolor(border_color)
        t.pensize(border_width)
        t.pendown()
    else:
        t.penup()
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()
    t.penup()

def draw_background():
    """Draws cockpit background atmosphere, dial ticks, and header banners."""
    bg_turtle.clear()
    
    # Ambient instrument cluster tick marks
    for deg in range(0, 360, 10):
        rad = math.radians(deg)
        is_major = (deg % 30 == 0)
        r_inner = 230
        r_outer = 244 if is_major else 236
        tick_color = "#333A48" if is_major else "#1A1E27"
        tick_width = 2.5 if is_major else 1.5
        
        x1 = r_inner * math.cos(rad)
        y1 = r_inner * math.sin(rad)
        x2 = r_outer * math.cos(rad)
        y2 = r_outer * math.sin(rad)
        
        bg_turtle.penup()
        bg_turtle.goto(x1, y1)
        bg_turtle.pencolor(tick_color)
        bg_turtle.pensize(tick_width)
        bg_turtle.pendown()
        bg_turtle.goto(x2, y2)
        bg_turtle.penup()
        
    # Ambient perimeter border ring
    draw_circle(bg_turtle, 0, 0, 248, border_color="#141720", border_width=1)
    
    # Header Banner
    bg_turtle.goto(0, 310)
    bg_turtle.pencolor("#94A3B8")
    bg_turtle.write("B A Y E R I S C H E   M O T O R E N   W E R K E", align="center", font=("Segoe UI", 12, "bold"))
    
    bg_turtle.goto(0, 286)
    bg_turtle.pencolor("#475467")
    bg_turtle.write("PROJECT DEVELOPED BY FEBIN ", align="center", font=("Segoe UI", 9, "bold"))

def draw_frame(show_letters=True):
    """Draws outer chrome bezel, black ring, and authentic BMW typography."""
    frame_turtle.clear()
    
    # M-Power Heritage Side Arcs (active in ///M Mode)
    if m_mode:
        stripes = [
            (M_LIGHT_BLUE, 218, -60, 60),
            (M_DARK_BLUE, 224, -55, 55),
            (M_RED, 230, -50, 50),
        ]
        for color, r, a_start, a_end in stripes:
            frame_turtle.pencolor(color)
            frame_turtle.pensize(4)
            frame_turtle.penup()
            for angle in range(a_start, a_end + 1, 3):
                rad = math.radians(angle)
                x = r * math.cos(rad)
                y = r * math.sin(rad)
                if angle == a_start:
                    frame_turtle.goto(x, y)
                    frame_turtle.pendown()
                else:
                    frame_turtle.goto(x, y)
            frame_turtle.penup()

    # Outer 3D Chrome Bezel Rings
    draw_circle(frame_turtle, 0, 0, R_OUTER_BEZEL, fill_color=COLOR_CHROME_DARK, border_color="#475467", border_width=2)
    draw_circle(frame_turtle, 0, 0, R_OUTER_RIM, fill_color=COLOR_CHROME_LIGHT)
    draw_circle(frame_turtle, 0, 0, R_INNER_BEZEL, fill_color=COLOR_BLACK_RING, border_color=COLOR_CHROME_DARK, border_width=2)
    
    # Inner Chrome Bezel separating black ring from roundel
    draw_circle(frame_turtle, 0, 0, R_BLACK_RING_INNER + 3, fill_color=COLOR_CHROME_MID)
    draw_circle(frame_turtle, 0, 0, R_ROUNDEL + 2, fill_color=COLOR_CHROME_LIGHT)
    
    # Render BMW Typography
    if show_letters:
        draw_letters()

def draw_letters():
    """
    Renders 'B', 'M', 'W' curved radially on the black band with 3D drop-shadows.
    In Turtle graphics, canvas coordinate (0, 0) is already centered at window center.
    Turtle (x, y) maps to Canvas (x, -y).
    """
    canvas = screen.getcanvas()
    canvas.delete("bmw_text")
    
    # Letter configurations: (Character, Angle on circle, Counter-clockwise rotation tilt)
    letters = [
        ("B", 135, 45),   # Top-Left arch
        ("M", 90, 0),     # Top-Center arch
        ("W", 45, -45),   # Top-Right arch
    ]
    
    for char, deg, tilt in letters:
        rad = math.radians(deg)
        x = R_TEXT * math.cos(rad)
        y = R_TEXT * math.sin(rad)
        
        # Canvas coordinates: +y in turtle is -y in Tkinter canvas
        canvas_x = x
        canvas_y = -y
        
        # 3D Drop Shadow for realistic engraved/embossed look
        canvas.create_text(
            canvas_x + 2,
            canvas_y + 2,
            text=char,
            fill="#000000",
            font=("Arial", 38, "bold"),
            angle=tilt,
            tags="bmw_text"
        )
        # Main Bold White Face
        canvas.create_text(
            canvas_x,
            canvas_y,
            text=char,
            fill="#FFFFFF",
            font=("Arial", 38, "bold"),
            angle=tilt,
            tags="bmw_text"
        )
        
    # Ensure letters are always rendered on top of the black bezel
    canvas.tag_raise("bmw_text")

def draw_roundel(t, theta):
    """
    Renders rotating center roundel rotated by angle `theta`.
    Official BMW quadrant configuration:
      - Top-Left: Alpine White
      - Top-Right: Bavarian Blue
      - Bottom-Right: Alpine White
      - Bottom-Left: Bavarian Blue
    """
    t.clear()
    
    # 1. Base Alpine White Circle
    draw_circle(t, 0, 0, R_ROUNDEL, fill_color=COLOR_WHITE)
    
    # 2. Bavarian Blue Sector 1 (Top-Right relative to theta)
    t.penup()
    t.goto(0, 0)
    t.setheading(theta)
    t.forward(R_ROUNDEL)
    t.left(90)
    t.fillcolor(COLOR_BLUE)
    t.pencolor(COLOR_BLUE)
    t.pensize(1)
    t.pendown()
    t.begin_fill()
    t.circle(R_ROUNDEL, 90)
    t.goto(0, 0)
    t.end_fill()
    t.penup()
    
    # 3. Bavarian Blue Sector 2 (Bottom-Left relative to theta)
    t.goto(0, 0)
    t.setheading(theta + 180)
    t.forward(R_ROUNDEL)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(R_ROUNDEL, 90)
    t.goto(0, 0)
    t.end_fill()
    t.penup()
    
    # 4. Chrome Crosshairs / Spoke Lines
    t.pencolor(COLOR_DIVIDER)
    t.pensize(2.5)
    for spoke in [theta, theta + 90, theta + 180, theta + 270]:
        rad = math.radians(spoke)
        x = R_ROUNDEL * math.cos(rad)
        y = R_ROUNDEL * math.sin(rad)
        t.goto(0, 0)
        t.pendown()
        t.goto(x, y)
        t.penup()
        
    # 5. Crisp Outer Roundel Border
    t.goto(0, -R_ROUNDEL)
    t.setheading(0)
    t.pencolor(COLOR_CHROME_LIGHT)
    t.pensize(2)
    t.pendown()
    t.circle(R_ROUNDEL)
    t.penup()
    
    # 6. 3D Specular Glass Arc (Domed enamel reflection)
    t.pencolor("#FFFFFF")
    t.pensize(2.5)
    r_sheen = R_ROUNDEL - 5
    for a in range(70, 155, 3):
        rad = math.radians(a)
        x = r_sheen * math.cos(rad)
        y = r_sheen * math.sin(rad)
        if a == 70:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    t.penup()
    
    # 7. Center Chrome Axis Button
    draw_circle(t, 0, 0, 5, fill_color=COLOR_CHROME_MID, border_color=COLOR_CHROME_DARK, border_width=1)
    draw_circle(t, 0, 0, 2.5, fill_color="#FFFFFF")

def update_hud():
    """Renders digital tachometer rev meter bar and telemetry display."""
    hud_turtle.clear()
    
    bar_y = -275
    bar_w = 340
    bar_h = 10
    
    # Tachometer Background Track
    hud_turtle.penup()
    hud_turtle.goto(-bar_w / 2, bar_y)
    hud_turtle.fillcolor("#151820")
    hud_turtle.pencolor("#252A36")
    hud_turtle.pensize(1)
    hud_turtle.pendown()
    hud_turtle.begin_fill()
    for _ in range(2):
        hud_turtle.forward(bar_w)
        hud_turtle.left(90)
        hud_turtle.forward(bar_h)
        hud_turtle.left(90)
    hud_turtle.end_fill()
    hud_turtle.penup()
    
    # Dynamic Meter Fill (proportional to RPM)
    fill_ratio = min(max(current_rpm / 7000.0, 0.02), 1.0)
    active_w = bar_w * fill_ratio
    
    # Color Shift: Cyan -> Amber -> Redline
    if current_rpm >= 6000:
        meter_color = "#EF4444"      # Redline
    elif current_rpm >= 4000:
        meter_color = "#F59E0B"      # Powerband Amber
    elif m_mode:
        meter_color = M_LIGHT_BLUE   # M-Sport Cyan
    else:
        meter_color = "#38BDF8"      # Cruise Blue
        
    hud_turtle.goto(-bar_w / 2, bar_y)
    hud_turtle.fillcolor(meter_color)
    hud_turtle.pendown()
    hud_turtle.begin_fill()
    for _ in range(2):
        hud_turtle.forward(active_w)
        hud_turtle.left(90)
        hud_turtle.forward(bar_h)
        hud_turtle.left(90)
    hud_turtle.end_fill()
    hud_turtle.penup()
    
    # Telemetry Status Readout
    mode_text = "///M SPORT" if m_mode else "CLASSIC"
    status_text = "PAUSED" if is_paused else "RUNNING"
    dir_text = "CW" if spin_direction < 0 else "CCW"
    
    hud_turtle.goto(0, bar_y - 25)
    hud_turtle.pencolor("#E2E8F0")
    hud_turtle.write(
        f"ENGINE: {int(current_rpm):,} RPM  |  CRUISE: {int(base_rpm)} RPM  |  MODE: {mode_text}  |  STATUS: {status_text}  |  DIR: {dir_text}",
        align="center",
        font=("Segoe UI", 10, "bold")
    )
    
    # Interactive Controls Guide
    hud_turtle.goto(0, bar_y - 50)
    hud_turtle.pencolor("#64748B")
    hud_turtle.write(
        "[CLICK] Rev Engine   [SPACE] Pause/Play   [UP/DOWN] Speed   [M] M-Sport   [R] Reverse   [ESC] Exit",
        align="center",
        font=("Segoe UI", 9, "normal")
    )

# ---------------------------------------------------------------------------
# Animation & Game Loop
# ---------------------------------------------------------------------------
def game_loop():
    """Main 60 FPS animation loop with momentum physics."""
    global current_angle, current_rpm, is_running
    
    if not is_running:
        return
    
    # Flywheel Deceleration: smoothly decays rev burst back to base cruise RPM
    if current_rpm > base_rpm:
        current_rpm = base_rpm + (current_rpm - base_rpm) * 0.94
        if current_rpm - base_rpm < 2.0:
            current_rpm = base_rpm
    elif current_rpm < base_rpm:
        current_rpm = base_rpm
        
    if not is_paused:
        deg_per_frame = (current_rpm * 0.1) * spin_direction
        current_angle = (current_angle + deg_per_frame) % 360
        draw_roundel(roundel_turtle, current_angle)
        
    update_hud()
    screen.update()
    screen.ontimer(game_loop, 16)

def run_intro():
    """Intro sequence that progressively draws and assembles the emblem."""
    global intro_step, is_intro_done
    
    if not is_running or is_intro_done:
        return
    
    intro_step += 1
    
    # Draw outer chrome arc progressively
    if intro_step <= 18:
        angle = intro_step * 20
        intro_turtle.pencolor(COLOR_CHROME_LIGHT)
        intro_turtle.pensize(3)
        intro_turtle.penup()
        intro_turtle.goto(0, -R_OUTER_RIM)
        intro_turtle.setheading(0)
        intro_turtle.pendown()
        intro_turtle.circle(R_OUTER_RIM, angle)
    
    # Lock in full background & frame with BMW text boldly visible
    elif intro_step == 20:
        intro_turtle.clear()
        draw_background()
        draw_frame(show_letters=True)
        draw_roundel(roundel_turtle, 0)
        update_hud()
        
    # Launch continuous animation
    elif intro_step >= 26:
        is_intro_done = True
        intro_turtle.clear()
        draw_frame(show_letters=True)
        screen.ontimer(game_loop, 16)
        return

    screen.update()
    screen.ontimer(run_intro, 30)

def skip_intro():
    """Instantly skips intro sequence if user clicks or presses a key."""
    global is_intro_done
    if not is_intro_done:
        is_intro_done = True
        intro_turtle.clear()
        draw_background()
        draw_frame(show_letters=True)
        draw_roundel(roundel_turtle, 0)
        update_hud()
        screen.ontimer(game_loop, 16)

# ---------------------------------------------------------------------------
# User Input Handlers
# ---------------------------------------------------------------------------
def on_click(x, y):
    """Rev throttle upon clicking or skip intro."""
    global current_rpm
    if not is_intro_done:
        skip_intro()
        return
    current_rpm = 6800.0  # REV THROTTLE!
    update_hud()

def toggle_pause():
    """Toggles animation pause state."""
    global is_paused
    if not is_intro_done:
        skip_intro()
        return
    is_paused = not is_paused
    update_hud()

def speed_up():
    """Increases cruising RPM."""
    global base_rpm, current_rpm
    if not is_intro_done:
        skip_intro()
        return
    base_rpm = min(base_rpm + 30, 800)
    current_rpm = max(current_rpm, base_rpm)
    update_hud()

def speed_down():
    """Decreases cruising RPM."""
    global base_rpm, current_rpm
    if not is_intro_done:
        skip_intro()
        return
    base_rpm = max(base_rpm - 30, 0)
    current_rpm = max(current_rpm, base_rpm)
    update_hud()

def reverse_spin():
    """Inverts rotation direction."""
    global spin_direction
    if not is_intro_done:
        skip_intro()
        return
    spin_direction *= -1
    update_hud()

def toggle_m_mode():
    """Toggles between Classic BMW and BMW M-Sport performance mode."""
    global m_mode, base_rpm, current_rpm
    if not is_intro_done:
        skip_intro()
        return
    m_mode = not m_mode
    if m_mode:
        base_rpm = max(base_rpm, 240)
        current_rpm = 5800.0  # Launch kick!
    else:
        base_rpm = 120.0
    draw_frame(show_letters=True)
    update_hud()

def exit_app():
    """Graceful exit handler."""
    global is_running
    is_running = False
    try:
        screen.bye()
    except Exception:
        pass

# ---------------------------------------------------------------------------
# Event Bindings & Startup
# ---------------------------------------------------------------------------
screen.listen()
screen.onscreenclick(on_click)
screen.onkey(toggle_pause, "space")
screen.onkey(speed_up, "Up")
screen.onkey(speed_down, "Down")
screen.onkey(reverse_spin, "r")
screen.onkey(reverse_spin, "R")
screen.onkey(toggle_m_mode, "m")
screen.onkey(toggle_m_mode, "M")
screen.onkey(lambda: on_click(0, 0), "Return")
screen.onkey(exit_app, "Escape")
screen.onkey(exit_app, "q")
screen.onkey(exit_app, "Q")

# Start with progressive intro animation
run_intro()

# Enter Tkinter event loop
try:
    turtle.mainloop()
except (turtle.Terminator, KeyboardInterrupt):
    pass