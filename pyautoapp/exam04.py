import pyautogui

#openfile = pyautogui.getWindowsWithTitle("제목 없음")
#openfile.activate()
pyautogui.hotkey("win","r")
#pyautogui.write("notepad")
pyautogui.write("excel")
pyautogui.press("enter") # pyautogui.hotkey("enter")
pyautogui.sleep(2)
pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.write("Hello~It's me",interval=0.2)
pyautogui.press("enter")

nameData = ["김씨","박씨","이씨","최씨","홍씨","조씨","허씨","금씨","신씨","임씨"]

for i in nameData:
    pyautogui.write(i)
    pyautogui.press("enter")

#pyautogui.hotkey("Alt","F4") #열린파일 닫기