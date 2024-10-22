#파이썬의 dictionary를 이용해 작업이 이루어질 수 있도록
import pyautogui

points={
    'overview' : [80,100],
    'w3s' : [160,100],
    'maven' : [240,100],
}


dictToList=list(points.items())
print(dictToList)

pyautogui.sleep(7)
for j in dictToList :
    i=0
    i=i+1
    print(j[i])
    pyautogui.click(j[i])
