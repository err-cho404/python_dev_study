import pyautogui
# 마우스 이동시키기(move(현재위치에서 특정거리만큼 이동-상대거리),moveTo(화면 전체에서 특정거리를 이동해라-절대거리))

#백그라운드애서 동작하는 대상 프로그램을 포그라운드로 바꾼다. 
pyautogui.sleep(2) #2초 기다림
#같은 조건을 활용하기 위해서 엑셀을 최대화
excelWindow = pyautogui.getWindowsWithTitle("통합 문서1")[0] #작업관리자에서 작동중인 프로그램들 중 타이틀이 "통합 문서1" 파일을 선택

excelWindow.activate() #선택된 엑셀을 포그라운드로 만들어라
excelWindow.maximize()
print(excelWindow)
pyautogui.moveTo(85,210,duration=2) #3초동안 x=85 y=210위치로 이동
pyautogui.click()
pyautogui.move(100,200,2)
pyautogui.click()
pyautogui.move(100,200,2)
pyautogui.rightClick()
pyautogui.move(20,-100,2)
pyautogui.click()
pyautogui.sleep(2)

excelWindow.restore() #모든 작업이 끝나면 엑셀을 원상태로 되돌려야한다.

print(pyautogui.position())#마우스 좌표확인