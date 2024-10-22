import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import openpyxl as op

wb = op.Workbook()
wb.sheetnames,"네이버증권"
ws = wb.active
ws.title = "네이버증권 국내증시리스트"
titles ="N 종목명 현재가 전일비 등락률 거래량 거래대금 매수호가 매도호가 시가총액".split()
ws.append(titles)

options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
options.add_argument('user_agent=' + user_agent)
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://naver.com")

elem = driver.find_element(By.CSS_SELECTOR, '#shortcutArea > ul > li:nth-child(6) > a > span.service_icon.type_stock')
elem.click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

elebtn = driver.find_element(By.CSS_SELECTOR, '#content > div.article > div.section > div.section_sise_top > div.group_type.is_active > a')
elebtn.click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

checkboxPER = driver.find_element(By.ID,'option6')
checkboxPER.click()
checkboxROE = driver.find_element(By.ID, 'option12')
checkboxROE.click()

collect = driver.find_element(By.XPATH,'//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img')
collect.click()

pageurl = driver.current_url

response = requests.get(pageurl)
soup = BeautifulSoup(response.content,"html.parser")

innerlistAll = len(soup.select("#contentarea > div.box_type_l > table >tr"))
for i in range(2,innerlistAll):
    prelist = i+1
    listInfolist = innerlistAll[i]
    print(listInfolist)
    for k in range(len(listInfolist)):
        append_data =[]
        list_td_info = listInfolist[k]
        list_td_info
        
        ws.append(list_td_info)
    
    #contentarea > div.box_type_l > table > tbody > tr:nth-child(3)
wb.save("naverlist.xlsx")
    




