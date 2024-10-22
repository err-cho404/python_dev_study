import openpyxl.worksheet
import openpyxl 
from datetime import datetime
import os

createEx = openpyxl.Workbook()
creatWorksheet = createEx.sheetnames,"증권리스트"
creatWorksheet = createEx.active
titles = ("N 종목명 현재가 전일비 등락률 거래량 거래대금 매수호가 매도호가 시가총액 PER ROE").split()
creatWorksheet.append(titles)
today=datetime.today().strftime("%Y%m%d")
createEx.save(filename="D:/stockData/stock"+today+".xlsx")

os.chdir('\\')
os.system("D:/rpawork/workspace/python/pyautoapp/exam08.py")

