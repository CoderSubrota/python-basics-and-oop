# Type "Hello World!" with a delay between each keystroke
import pyautogui
 
 # Press the "Enter" key
# pyautogui.press("enter")

# Hold and release a key combination (e.g., Ctrl+C)
# pyautogui.hotkey("ctrl", "c")


# for inx in range(100) :
    #   pyautogui.write("I love you!\n", interval=0.2)
      


# Take a screenshot and save it
screenshot = pyautogui.screenshot()
screenshot.save("images/screenshot.png")


print(pyautogui.size())

pyautogui.click()

# Click at a specific position (x=200, y=200)
pyautogui.click(x=200, y=200)