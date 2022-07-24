# from curses.ascii import FF
# from selectors import EpollSelector
import pyautogui 
from time import sleep as t

ass = 'C:/Users/gram/Desktop/mirM/mirm/img/'
png = '.PNG'
sim = 0.83 #이미지 유사성
#pyautogui.locateCenterOnScreen(confidence=0.9,  grayscale=True, region=(0,0, 300, 400))#유사성/흑백/x,y,가로, 세로
    # pyautogui.position()

img = ''
def ck():
    while True:
        capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
        if capture == None:
            print(str(capture)+': '+img)
            t(1)
        else:
            break
    pyautogui.click(capture)
    print(img+': done')
def find ():
    while True:
        
        capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
        if capture == None:
            print(str(capture)+': '+img)
            t(1)
        else:
            break
        print(img+': done')
def active_2():
    img = 'active_work'
    def ck():
        while True:
            capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
            if capture == None:
                print(str(capture)+': '+img)
                t(1)
            else:
                break    
            pyautogui.click(capture)
            print(img+': done')
    def find ():
        while True:
            capture = pyautogui.locateCenterOnScreen(ass+img+png, confidence = sim)    
            if capture == None:
                print(str(capture)+': '+img)     
                t(1)
            else:
                break
            print(img+': done')
        
    img = 'active_work'
    ck()
    img = 'm2'
    ck()
    img = 'echo'
    while True:
        capture = pyautogui.locateOnScreen(ass+img+png, confidence = sim)    
        if capture == None:
            pyautogui.write('e',1)
            print(str(capture)+': '+img)
            t(1)
        else:
            break
    pyautogui.write('e')

# 모니터 해상도 가져오기
width, height = pyautogui.size()
print('width={0}, height={1}'.format(width, height))

# i = 1       
# while True:
#     img = 'active_work'
#     ck()
#     img = 'm2'
#     ck()
#     img = 'echo'
#     while True:
#         capture = pyautogui.locateOnScreen(ass+img+png, confidence = sim)    
#         if capture == None:
#             pyautogui.write('e',1)
#             print(str(capture)+': '+img)
#             t(1)
#         else:
#             break
#     pyautogui.write('e')

#     i += 1



img = 'active_work'
ck()
img = 'm2'
ck()
img = 'echo'
while True:
    capture = pyautogui.locateOnScreen(ass+img+png, confidence = sim)    
    if capture == None:
        pyautogui.write('e',1)
        print(str(capture)+': '+img)
        t(1)
    else:
        break
pyautogui.write('e')
