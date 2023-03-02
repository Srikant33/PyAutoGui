import pyautogui
import time

# Define the position to click
x, y = 1290, 471

# Move the mouse to the position and click
while True:
    pyautogui.moveTo(x, y)
    pyautogui.click()   
    time.sleep(60)