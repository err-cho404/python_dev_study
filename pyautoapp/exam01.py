import pyautogui
import sys

size = (1920,1200) #프로그램을 짤때 디폴트 해상도
resolution = pyautogui.size()
print("size() =>",pyautogui.size()) #실제 프로그램 짤때 화면 해상도
print("size() =>",pyautogui.size()[0])

#동일조건에서 실행되는지를 체크=>rpa에서 동일조건을 만드는 것이 중요하다.
#자동화 개발시 해당도와 현재 해상도가 다르면 프로그램 종료
if size[0] != pyautogui.size()[0] or size[1] != pyautogui.size()[1] :
    print("값이 다르다")
    sys.exit()
