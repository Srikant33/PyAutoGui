import time 
  
# a module which has functions related to time.  
# It can be installed using cmd command:  
# pip install time, in the same way as pyautogui. 
import pyautogui
import random
time.sleep(5)  
pyautogui.PAUSE = 0.1
while (1):
     pyautogui.keyDown('shift')
     pyautogui.press('down')
     pyautogui.keyUp('shift')
     r=random.randint(50, 250)
     time.sleep(5)
     pyautogui.hotkey('ctrl', 'enter')
     time.sleep(5)
     pyautogui.press('down')
     pyautogui.press('up')
     time.sleep (r)
     