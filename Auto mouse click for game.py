import time 
  
# a module which has functions related to time.  
# It can be installed using cmd command:  
# pip install time, in the same way as pyautogui. 
import pyautogui 
time.sleep(0)  
pyautogui.PAUSE = 0.01

while (1):
   for i in range (5):
       for j in range(5):
           pyautogui.click(575+(50*i), 340+(50*j))

