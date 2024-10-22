#f=open("three\sample.csv",'w')
#f.write("나의 살던 고향은 꽃피는 산골".split())
#f.close()



#키보드로부터 입력을 받아서 파일을 저장하시오
#키보드로부터 false로 판단되는 값을 입력하면 더이상 입력을 종료
#1행에 5개의 자료를 입력한다.
#단 마지막 자료는 5개가 아닐 수 있다.(맨 마지막행은 결축치이다)



questionList = ["이름","나이","주소"]
f=open("example.csv","w")
a=1
while a:
    for question in questionList:
        data=input(f"{question}을 입력해 주세요")
        if data == "":
            f.close()
            a = 0>1
            break
        else:
            if question == "주소":
                f.write(data+"\n")
                break
            f.write(data+",")
f.close()






