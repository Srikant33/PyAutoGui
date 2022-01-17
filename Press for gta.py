import time 
  
# a module which has functions related to time.  
# It can be installed using cmd command:  
# pip install time, in the same way as pyautogui. 
import pyautogui 
time.sleep(0)  
pyautogui.PAUSE = 0.01
while (1):
     pyautogui.keyDown('shift')
     pyautogui.keyUp('shift')
     #pyautogui.click()
    #pyautogui.moveRel(1, 0)
    #pyautogui.moveRel(-1, 0)

# makes program execution pause for 10 sec 

#pyautogui.moveTo(575, 340, duration = 0)
#pyautogui.moveTo(575, 400, duration = 0.5)
#pyautogui.moveTo(575, 450, duration = 0.5)
#pyautogui.moveTo(575, 500, duration = 0.5)
#pyautogui.moveTo(575, 550, duration = 0)

#pyautogui.moveTo(575, 340, duration = 0)
#pyautogui.moveTo(625, 340, duration = 0.5)
#pyautogui.moveTo(675, 340, duration = 0.5)
#pyautogui.moveTo(725, 340, duration = 0.5)
#pyautogui.moveTo(775, 340, duration = 0.5)
  
#pyautogui.click(10, 10) 
#pyautogui.click(575, 250) 

#while (1):
#    for i in range (5):
#        for j in range(5):
#            pyautogui.click(575+(50*i), 340+(50*j))

