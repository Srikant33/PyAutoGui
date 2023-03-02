import time 
  
# a module which has functions related to time.  
# It can be installed using cmd command:  
# pip install time, in the same way as pyautogui. 
import pyautogui 
import keyboard
time.sleep(2)  
pyautogui.PAUSE = 0.01


while(1):
    for i in range(60):
        if keyboard.is_pressed("q"):
            # Key was pressed
            break
        pyautogui.press('down')

    if keyboard.is_pressed("q"):
        # Key was pressed
        break
    # for i in range (20):
    #     for j in range(20):
    #         if keyboard.is_pressed("q"):
    #             # Key was pressedq
    #             break
    #         pyautogui.click(300+(50*i), 200+(25*j))
    
