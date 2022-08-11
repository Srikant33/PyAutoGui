from logging import BufferingFormatter
import time 
import keyboard
from multiprocessing import Process
from termcolor import colored
  

# a module which has functions related to time.  
# It can be installed using cmd command:  
# pip install time, in the same way as pyautogui. 
import pyautogui
import xlrd
pyautogui.PAUSE = 0.01
BufferingFormatter
# pyautogui.moveTo(2780, 607)
# pyautogui.moveTo(2750, 607)
# Give the location of the file
pause_keyboard = False  # I use a bolean as a state is clearer for me

loc = (r"C:\Users\k.iyer-es\aa.xls")
# pyautogui.moveTo(2780, 607)
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
time.sleep(5) 
# For row 0 and column 0

for i in range (1,100):
    print(i)
    
    if keyboard.is_pressed('p'):
        while True:
            time.sleep(1)
            if keyboard.is_pressed('s'):
                break

    pyautogui.moveTo(257, 227)
    pyautogui.click()
    BufferingFormatter
    time.sleep(2) 
    
    pyautogui.moveTo(610, 207)
    pyautogui.click()
    
    a=str(int(sheet.cell_value(i, 0)))+"-"+sheet.cell_value(i, 1)
    pyautogui.write(a) 
    
    pyautogui.moveTo(610, 507)
    pyautogui.click()
    
    pyautogui.write(sheet.cell_value(i, 2))
    pyautogui.press('enter')
    
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.write('Resolution Text')
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 'b')
    pyautogui.write(sheet.cell_value(i, 3))
    pyautogui.press('enter')
    
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.write('Bug Type')    
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.press('enter')
    
    pyautogui.hotkey('ctrl', 'b')
    pyautogui.write(sheet.cell_value(i, 4))
    pyautogui.press('enter')

    if (sheet.cell_value(i, 5)!=""):
        pyautogui.hotkey('ctrl', 'b')
        pyautogui.write('Min. Tool')
        pyautogui.hotkey('ctrl', 'b')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'b')
        pyautogui.write(sheet.cell_value(i, 5))

    pyautogui.moveTo(920, 607)
    time.sleep(5)
    pyautogui.click()
    time.sleep(4) 
