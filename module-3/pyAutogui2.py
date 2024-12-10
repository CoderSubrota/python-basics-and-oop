import pyautogui as py
import time 


screenshot = py.screenshot()
screenshot.save(f"screenshot2.jpeg")

time.sleep(5) 
for i in range(10):
    py.write("I Love My Country!", interval=0.1)
    py.press("enter")


