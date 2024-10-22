from bs4 import BeautifulSoup

html = '''
<html>
    <body>
        <h1 class="first">스크랩핑 테스트</h1>
        <p>웹 페이지의 첫번째 문단입니다</p>
        <p id="second">웹 페이지의 두번째 문단입니다</p>
        <a data_anc='myname' href="#">링크정보</a>
    </body>    
</html>    
'''
soup = BeautifulSoup(html, 'html.parser')
print("result==>\n",soup)
print("*****************")
print(soup.html.body.h1,"\n********")
print("*****************")
print(soup.html.body.p,"\n********")
print("*****************")
print(soup.html.body.p.text,"\n********")
print(soup.html.body.p.text,"\n@@@@@@@@@")
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print(p2.text,"\n********")
print(p2.string,"\n********")
print(soup.html.h1.string,"\n********")
print(soup.html.text,"\n********") #스트링보단 test를 사용하는게 더 포괄적임

idfind = soup.find(id='second')
print(idfind,'\n&&&&&&&&&&')

classfind = soup.find(class_='first')
print(classfind,'\n&&&&&&&&&&')

datafind = soup.find(data_anc='myname')
print(datafind,'\n&&&&&&&&&&')


