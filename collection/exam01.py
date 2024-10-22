import time  #기계적 접근 차단, 자바 스크립트의 동작을 피하기 위해 사용함 time.sleep

#셀레니움 필수 import
from selenium import webdriver #셀레니움은 브라우저의 모든 것을 핸들링 할 수 있음
from selenium.webdriver.common.by import By 

#셀레니움 옵션 import
#from selenium.webdriver.common.keys import Keys # 선택객체.send_keys(Keys.ENTER) 로 사용 => key에대한 기능설정
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service


options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" #내용이 바뀌므로 어떻게 찾는지 알아두기
options.add_argument("user_agent=" + user_agent) #기계(로봇)의 접근에의한 크롤링을 막기위한 설정을 속이기 위해 실제유저가 움직이는 것처럼 속이는 기능
# 브라우저 창 자동 닫힘 제어 옵션
options.add_experimental_option("detach",True)

browser = webdriver.Chrome(options=options) #사용할 브라우저 선택
url = "https://www.naver.com/"
browser.get(url)
print("현재 url은", browser.current_url)
time.sleep(2)


url2 = "https://www.daum.net/"
browser.get( url2 )
print("현재 url은", browser.current_url)
time.sleep(3)

browser.back() #뒤로가기(네이버로 갓다가 다음으로 간 후 뒤로 가기가 되어 네이버로 돌아감)
print("현재 url은", browser.current_url)
time.sleep(1)
browser.refresh() #새로고침
print("현재 url은", browser.current_url)
time.sleep(3)
browser.forward() #앞으로가기
print("현재 url은", browser.current_url)
time.sleep(5)




#query = browser.find_element(By.CLASS_NAME, "ContentHeaderSubView-module__link_home___hdZDg")
#query = browser.find_element(By.CSS_SELECTOR, "#account > div > p")

#print(query.text)