#이미지파일을('textselimg.png') 이용하여 선택하기
import pyautogui

# pyautogui.sleep(7)
# result = pyautogui.locateOnScreen('textselimg.png')
# print(result)
# pyautogui.click(result) #이미지좌표를 변수에 담아 클릭 할 수 있게 만듦


pyautogui.sleep(5)
result = pyautogui.locateAllOnScreen('checkbox.png',confidence=0.95,region=(0,0,1920,1200))#confidence ==>이미지의 정확도지정가능 / region ==>찾을 범위를 지정해줌

print(result)
#pyautogui.sleep(5)
#pyautogui.click(result) #이미지좌표를 변수에 담아 클릭 할 수 있게 만듦

for i  in result : 
    print(i)
    pyautogui.click(i)


'''
파일 선택 방법
- 이미지를 이용해 선택 : locate(All)OnScreen('이미지명') ==> 좌표정보를 반환 
==> 일치하는 이미지가 있다면 창을 전체화면으로 하지 않아도 찾아준다. 화면확대(해상도%조절)시에는 이미지크기가 달라져 찾기 불가, 속도 느릴 수 있음,오차가 있어 100%작동한다고 보기 어려움
======================================================================================
- 위치값을 이용해서 선택 : move(To)(x,y) ==>좌표값을 알고 있을 때
- 이벤트를 이용한 위치값 선택 및 동작 : click(x,y) ==> 위치값을 클릭해라
==> 화면의 좌표를 찾아가므로 일정한 창의 크기를 유지시켜줘야한다. 좌표가 지정되어있어 속도가 빠름
'''