import threading
import time
from pynput import keyboard, mouse

# Mouse controller
mouse_controller = mouse.Controller()

# Movement settings
SPEED = 3        # Pixels per step (adjust for speed)
DELAY = 0.005      # Time between steps in seconds (adjust for smoothness)
HOLD_DURATION = 0.9 # Duration for hold and release in seconds

# Track which directions are active
directions = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

def move_mouse():
    while True:
        dx = dy = 0
        if directions["up"]:
            dy -= SPEED
        if directions["down"]:
            dy += SPEED
        if directions["left"]:
            dx -= SPEED
        if directions["right"]:
            dx += SPEED
        if dx != 0 or dy != 0:
            x, y = mouse_controller.position
            mouse_controller.position = (x + dx, y + dy)
        time.sleep(DELAY)

def perform_click(button):
    mouse_controller.click(button)

def perform_hold_release(button, duration):
    mouse_controller.press(button)
    time.sleep(duration)
    mouse_controller.release(button)

def on_press(key):
    if key == keyboard.Key.up:
        directions["up"] = True
    elif key == keyboard.Key.down:
        directions["down"] = True
    elif key == keyboard.Key.left:
        directions["left"] = True
    elif key == keyboard.Key.right:
        directions["right"] = True
    elif key == keyboard.KeyCode.from_char('\\'):  # Left click once
        threading.Thread(target=perform_click, args=(mouse.Button.left,), daemon=True).start()
    elif key == keyboard.KeyCode.from_char('/'):   # Right click once
        threading.Thread(target=perform_click, args=(mouse.Button.right,), daemon=True).start()
    elif key == keyboard.KeyCode.from_char(']'):   # Right click hold and release
        threading.Thread(target=perform_hold_release, args=(mouse.Button.right, HOLD_DURATION), daemon=True).start()
    elif key == keyboard.Key.esc:
        print("Exiting...")
        return False

def on_release(key):
    if key == keyboard.Key.up:
        directions["up"] = False
    elif key == keyboard.Key.down:
        directions["down"] = False
    elif key == keyboard.Key.left:
        directions["left"] = False
    elif key == keyboard.Key.right:
        directions["right"] = False

# Start the mouse movement in a background thread
threading.Thread(target=move_mouse, daemon=True).start()

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()