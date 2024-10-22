import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options=Options()
user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
options.add_argument("user_agent=" + user_agent)
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.naver.com/")
#driver.driver.page_source => 네이버 웹페이지에 대한 페이지 내용을 담고있다.
elem = driver.find_element(By.CSS_SELECTOR,'#query')
#query = driver.find_element(By.ID,'query')  -->여러방법이 있음
#query = driver.find_element(By.XPATH,'//*[@id="query"]')

elem.send_keys("뉴스홈")
time.sleep(1)
elem.clear()
elem.send_keys("화성 화재") #검색창에 검색할 내용 입력
elem.send_keys("기사")
#elem.send_keys(Keys.ENTER) #=>enter키를 누르게함
elebtn = driver.find_element(By.XPATH,'//*[@id="search-btn"]') #검색창에 검색버튼 선택
elebtn.click() #검색버튼 클릭

#셀레니움 3점대 하위 버전에서는 
#elebtn = driver.find_element_by_xpath('//*[@id="search-btn"]')
#elebtn = driver.find_element_by_id('search-btn')
#elebtn = driver.find_element_by_classname('search-btn')

#1회성 검색은 다시 쓰지 않을거면 위처럼 변수에 담을 필요가 없음 => 위 두개를 합칠 수 있다.
#elebtn = driver.find_element(By.XPATH,'//*[@id="search-btn"]').click()

#driver.page_source => 이벤트에 의해서 바뀐 페이지의 내용을 담고있다.
#print(driver.page_source)
newsTitle = driver.find_element(By.CSS_SELECTOR,'#sp_nws_all1 > div > div > div.news_contents > a.news_tit')
newsTitle.click()
#print(newsTitle.text)

#타이틀에 해당하는 답변글(설명글)을 변수(newstitle_desc)에 저장한다.
#저장된 변수의 자료를 cvs파일(newsSearch.csv)로 저장하시오
newstitleDesc = driver.find_element(By.XPATH,'//*[@id="renewal2023"]/div[3]/p[1]')

f=open("newsSearch.csv","w",encoding='utf-8')
f.write(newsTitle.text +','+ newstitleDesc.text)
f.close()

#수집된 자료 파일을 해당응용프로그램파일을 이용해 열어준다.
import os
os.system('start excel "D:/rpawork/workspace/python/newsSearch.csv"') #==> 맥북은 start대신 open사용


driver.close() #활성화 되어있는 탭을 닫음  #driver.quit()==>브라우저를 다 닫음
 




