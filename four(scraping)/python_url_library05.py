import requests #->외부 라이브러리
from bs4 import BeautifulSoup 
from lxml import etree
import openpyxl as op

wb = op.Workbook()
ws = wb.sheetnames,"한빛도서목록"
ws = wb.active
titles ="일련번호 도서명 저자 발행일 가격 ".split()
ws.append(titles)
url = "https://www.hanbit.co.kr/media/books/full_book_list.html?page="
i=0
pageurl = url+str(i+1)
response = requests.get(pageurl)
soup = BeautifulSoup(response.content, 'html.parser')
page = len(soup.select("#container > div.full_book_list_wrap > div.paginate.bdr_no > a"))+1

for i in range(page+1):
    pageurl = url+str(i+1)
    response = requests.get(pageurl)
    soup = BeautifulSoup(response.content, 'html.parser')

    book_list_tr_all = soup.select("table.tbl_type_list tbody>tr")
    for k in range(len(book_list_tr_all)): #위에 있는 head의 tr은 제외
        append_data = []
        append_data.append(k+1)
        book_list = book_list_tr_all[k]
        append_data.append(book_list.select_one("td:nth-child(1)").text)
        append_data.append(book_list.select_one("td:nth-child(2)").text)
        append_data.append(book_list.select_one("td:nth-child(3)").text)
        append_data.append(book_list.select_one("td:nth-child(4)").text)
        
        ws.append(append_data)

wb.save("hanbook_list.xlsx")
                
            
           



        

