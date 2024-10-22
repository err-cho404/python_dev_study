#import examp
#result = examp.multi_calcu(50,3,"")
#print(result)
#from examp import multi_calcu as mc
#from examp import var_def
#print (mc(10,30,'+'))
#print(var_def)
from openpyxl import Workbook

        # 엑셀파일 쓰기
write_wb = Workbook()

        # 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('생성시트')

        # Sheet1에다 입력
write_ws = write_wb.active
write_ws.append(['학번','이름','국어','영어','수학','합계','평균'])
write_ws.append(['3701','홍길동',100,100,100,'=SUM(C2:E2)','=AVERAGE(C2:E2)'])
write_ws.append(['3702','나일등',70,100,90,'=SUM(C3:E3)','=AVERAGE(C3:E3)'])

write_wb.save("imsi.xlsx")
