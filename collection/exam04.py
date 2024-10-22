import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
options.add_argument('user_agent=' + user_agent)
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://naver.com")
# driver.driver.page_source 에는 접속한페이지에서 전달받은 내용이 저장되어 있다.
elem = driver.find_element(By.CSS_SELECTOR, '#query')
# elem = driver.find_element(By.ID, '#query')
# elem = driver.find_element(By.XPATH, '//*[@id="query"]')

elem.send_keys("채상병 특검")
time.sleep(1)
elem.clear()
elem.send_keys("채상병 특검")
elem.send_keys("채상병 특검")
time.sleep(2)
# elem.send_keys(Keys.ENTER)
elebtn = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
# 셀레니움 하위버전에서는 elebtn = driver.find_element_by_xpath( '//*[@id="search-btn"]' )
elebtn.click()  # driver.find_element(By.XPATH, '//*[@id="search-btn"]').click()
# driver.page_source => 이벤트에 의해서 바뀐 페이지의 내용을 담고 있다.
# print( driver.page_source )
newsTitle = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.spw_rerank.type_head._rra_head > section:nth-child(3) > div > ul > li > div > div.detail_box > div.title_area > a')
# 타이들에 해당하는 답변글(설명글)을 변수(newTitleDesc)에 저장한다.
newTitleDesc = driver.find_element(By.XPATH, '//*[@id="main_pack"]/div[3]/section[1]/div/ul/li/div/div[2]/div[2]/a')


# 저장된 변수의 자료를 csv파일(newsSearch.csv)로 저장하시오

f= open("newsSearch.csv", "w")
f.write(newsTitle.text+","+newTitleDesc.text)
f.close()

# 수집된 자료파일을 해당응용프로그램을 이용해서 열고 싶다.
import os
os.system('start excel "D:/rpawork/workspace/python/newsSearch.csv"' )

driver.close() ## driver.quit()