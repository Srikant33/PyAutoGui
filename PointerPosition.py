import pyautogui

# Continuously print the current position of the mouse pointer
while True:
    x, y = pyautogui.position()
    print('Mouse position: x = {}, y = {}'.format(x, y))