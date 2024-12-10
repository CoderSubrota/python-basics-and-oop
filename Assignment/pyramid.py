import pyautogui
import time

def draw_pyramid(N):
    time.sleep(5)
    for i in range(1, N+1) :
        space = ' ' * (N-i)
        star = '*' * (2 * i - 1)
        line = space + star
        pyautogui.typewrite(line)
        pyautogui.press("enter")
        
N = int(input())
draw_pyramid(N) 
