from curses.ascii import FF
from selectors import EpollSelector
import pyautogui 
from time import sleep as t

ass = './img/'
png = '.png'
sim = 0.83 #이미지 유사성
#pyautogui.locateCenterOnScreen(confidence=0.9,  grayscale=True, region=(0,0, 300, 400))#유사성/흑백/x,y,가로, 세로
    # pyautogui.position()

img = ''
def ck():
    while True:
        capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
        if capture == None:
            t(1)
        else:
            break
    center = pyautogui.center(capture)
    pyautogui.click(center)
def find ():
    while True:
        capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
        if capture == None:
            t(1)
        else:
            break

def active():
    def ck():
        while True:
            capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
            if capture == None:
                t(1)
            else:
                break
        center = pyautogui.center(capture)
        pyautogui.click(center)
    def find ():
        while True:
            capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
            if capture == None:
                t(1)
            else:
                break

    img = 'active_work'
    ck()
    img = 'm2'
    ck()
    img = 'echo'
    while True:
        capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
        if capture == None:
            pyautogui.write('e')
            t(1)
        else:
            break
    center = pyautogui.center(capture)
    pyautogui.click(center)
    

i = 1       
while True:
    ck()






    i += 1