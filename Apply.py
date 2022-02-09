import time 
  
# a module which has functions related to time.  
# It can be installed using cmd command:  
# pip install time, in the same way as pyautogui. 
import pyautogui 
time.sleep(5)  
pyautogui.PAUSE = 0.5
skills= ["Java" ,"C++" ,"F#" ,"PHP" ,"HTML" ,"CSS" ,"Python" ,"JavaScript" ,"SQL" ,"Scilab" ,"Go","Git" ,"Microsoft-Office" ,"Worksoft" ,"Control-M" ,"VS" ,"Code" ,"SAP" ,"Agile" ,"NumPy" ,"Pyautogui" ,"Selenium" ,"Matplotlib" ,"REACT" ,"Node.js" ,"TCP" ,"UDP" ,"pywhatkit" ,"Jupyter" ,"Git"]

for s in skills:
    print(s)
    pyautogui.write(s)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    # time.sleep(3)
    pyautogui.click()
# while (1):
#      pyautogui.keyDown('shift')
#      pyautogui.keyUp('shift')
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

