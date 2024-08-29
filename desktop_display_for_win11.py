import pyautogui
import time

pyautogui.FAILSAFE = False

def desktop_display():
    pyautogui.keyDown('winleft')
    pyautogui.press('d')
    pyautogui.keyUp('winleft')
        
w, h = pyautogui.size()

print(f"屏幕宽度：{w}")
print(f"屏幕高度：{h}")

desktop = 0
while True:
    x, y = pyautogui.position()
    if x >= w - 10 and y >= h - 10:
        desktop_display()
        while x >= w - 10 and y >= h - 10:
            x, y = pyautogui.position()
        desktop_display()
        
