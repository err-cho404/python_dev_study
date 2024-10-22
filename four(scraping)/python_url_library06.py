import requests #->외부 라이브러리
from bs4 import BeautifulSoup 
from lxml import etree
import openpyxl as op

wb = op.Workbook()
ws = wb.sheetnames,"한빛도서목록"
url = "https://www.hanbit.co.kr/media/books/full_book_list.html?page="
for i in range(0,10+1):
    pagenum = str(i+1)
    pageurl = url+pagenum
#    print(pageurl)
    response = requests.get(pageurl)
    soup = BeautifulSoup(response.content, 'html.parser')

    book_list_tr_all = soup.select("table.tbl_type_list tbody>tr")
    for i in range(len(book_list_tr_all)): #위에 있는 head의 tr은 제외
        book_list = book_list_tr_all[i]
        book_info = book_list.select("td")
        for k in range(len(book_info)):
            book_td_info = book_info[k].text
            print(book_td_info)
            append_data=[]
            append_data.append(k)
            if k%4==1 :
                append_data.append()
            
           



        

