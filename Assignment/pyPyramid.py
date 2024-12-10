import pyautogui
import time

# Give yourself a few seconds to switch to the drawing area
time.sleep(5)

def draw_pyramid(base_length):
    height = base_length // 2
    half_base = base_length // 2

    # Move to the starting point (bottom center of the pyramid)
    start_x, start_y = pyautogui.position()
    pyautogui.moveTo(start_x - half_base, start_y)

    # Draw the pyramid
    pyautogui.dragRel(base_length, 0, duration=0.5)  # Base
    pyautogui.dragRel(-half_base, -height, duration=0.5)  # Left side
    pyautogui.dragRel(-half_base, height, duration=0.5)  # Right side to top
    pyautogui.dragRel(half_base, height, duration=0.5)  # Back to top

# Set the base length of the pyramid
draw_pyramid(200)