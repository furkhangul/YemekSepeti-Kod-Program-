import pyautogui
import time

def click(x , y ):
    pyautogui.moveTo(x,y)
    pyautogui.click()



click(1200 , 1080)
time.sleep(1)
click(750,300)
time.sleep(2)
click(1000,955)
time.sleep(1)
click(850,310)
pyautogui.write("5418640498")
time.sleep(0.5)
click(950,980)
time.sleep(1)
