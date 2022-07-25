from turtle import hideturtle
import mouse
import pyautogui
import time

 

click  = 0    # 몇 번째 클릭인지저장할 변수  

 
# 모니터 해상도 가져오기
width, height = pyautogui.size()
print(width, height)
while True:
    if mouse.is_pressed("right"):             # 마우스 오른쪽 클릭이면
        click += 1                             # 클릭 숫자 증가
        print('Right-Clicked: ' + str(click))   # 메시지 출력
        x, y = mouse.get_position()       # 현재 마우스 포인터 좌표
        print('{0}, {1}'.format(x, y))# 마우스 포인터 좌표를 출력  print('{0}, {1}'.format(x, y))
        time.sleep(0.1)                          # 0.05초 대기 (중복 체크 예방)
        fx =  x/width#좌표/해상도 = 비율
        fy = y/height#좌표/해상도 = 비율
        fx_ = fx*width#비율*해상도 = 클릭 좌표
        fy_ = fy*height#비율*해상도 = 클릭 좌표

        print(fx*width)#비율*해상도 = 클릭 좌표
        print(fy*height)#비율*해상도 = 클릭 좌표
        print(fx_)#비율*해상도 = 클릭 좌표
        print(fy_)#비율*해상도 = 클릭 좌표
        print('{0}, {1}'.format(fx_,fy_))#비율*해상도 = 클릭 좌표
        print('')
        print('width, height = pyautogui.size()')#1. 해당 컴퓨터 해상도 가져오기 width, height
        print('fx = {0}'.format(fx))#2. 미리 셋팅한 비율 정의하기 fx, fy
        print('fy =  {0}'.format(fy))#2. 미리 셋팅한 비율 정의하기 fx, fy
        print('fx_ = fx*width')#3. 클릭좌표 정의하기 fx_, fy_
        print('fy_ = fy*height')#3. 클릭좌표 정의하기 fx_, fy_
        pyautogui.click(fx_, fy_)


# while True: #원래 코드
#     if mouse.is_pressed("left"):             # 마우스 왼쪽 클릭이면
#         click += 1                             # 클릭 숫자 증가
#         print('Left-Clicked: ' + str(click))   # 메시지 출력
#         pos = mouse.get_position()       # 현재 마우스 포인터 좌표
#         print(pos)                                  
#         mouse.move(pos[0], pos[1]+20)  # 마우스 포인터 좌표를 아래로 이동
#     time.sleep(0.05)                          # 0.05초 대기 (중복 체크 예방)
