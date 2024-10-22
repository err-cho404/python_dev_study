import pyautogui

mspaint = pyautogui.getWindowsWithTitle("제목 없음")[0]
mspaint.activate()
mspaint.maximize()
pyautogui.moveTo(360,70,duration=2)
pyautogui.click()
pyautogui.moveTo(690,70,duration=2)
pyautogui.click()
pyautogui.moveTo(690,275,duration=2)
pyautogui.click()

# pyautogui.moveTo(100,250,duration=2)
# pyautogui.click()

# for i in range(1,3) :
#     pyautogui.move(100,100,duration=2)
#     pyautogui.click()


pyautogui.moveTo(450,70,duration=1)
pyautogui.click()

pyautogui.moveTo(400,400,duration=1)
pyautogui.click()
pyautogui.drag(100,100,1)

pyautogui.moveTo(470,70,duration=1)
pyautogui.click()
pyautogui.drag(150,150,3)


#pyautogui.click(1000,800,2)
#mspaint.minimize() 창아래로 내리기
mspaint.restore() 
pyautogui.scroll(-300)
pyautogui.sleep(2)