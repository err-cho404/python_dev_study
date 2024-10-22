import pyautogui as pg
import sys
import pyperclip
#pg.mouseInfo() #마우스 좌표나 정보를 얻을 수 있음
# 332,72

#그림판 실행
#텍스트입력 아이콘으로 마우스 이동
#텍스트입력아이콘 클릭
#텍스트를 입력할 위치로 마우스 이동 37,175 
#클릭해서 hongildong입력하게 한다.

size = (1920,1200) #프로그램을 짤때 디폴트 해상도
resolution = pg.size()
print("size() =>",pg.size()) #실제 프로그램 짤때 화면 해상도
print("size() =>",pg.size()[0])
if size[0] != pg.size()[0] or size[1] != pg.size()[1] :
    print("값이 다르다")
    sys.exit()

pg.hotkey("win","r")
pg.sleep(1.5)
pg.write("mspaint")
pg.sleep(1.5)
pg.press("enter")

# for win in pg.getAllWindows():
#     print(win)

# for win in pg.getWindowsWithTitle('제목 없음') :
#     print(win)

pg.sleep(2)

win = pg.getWindowsWithTitle('제목 없음 - 그림판')[0]

try:
    if win.isActive == False:
        win.activate()
        win.restore()
    if win.isMaximized == False:
            win.maximize()
except Exception as e:
    win.minimize()
    win.maximize()


pg.moveTo(332,72,2)
pg.click()
pg.sleep(1.5)
pg.moveTo(37,175,2)
pg.sleep(1.5)
pg.click()
# pg.write("honggildong",interval=0.1)
pyperclip.copy('한글도 쓸 수 있는 기능')
pg.hotkey("ctrl","v") #pyperclip.paste()가 작동 하지 않아 pg.hotkey("ctrl","v")를 사용
pg.sleep(1.5)
pg.moveTo(150,250,2)
pg.click()

#pyautogui.pause = 1   -->모든 동작을 수행할때 일괄적으로 sleep(1)을 설정한다.(시간설정 환경변수)


