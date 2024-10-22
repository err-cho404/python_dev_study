#text 파일을 csv 파일로 내용복사해서 넣고 저장함
readf=open("text.txt",'r',encoding='utf=8')
openf=open("text.csv",'w')
readData = readf.read()
openf.write(readData)
readf.close()
openf.close()

#사랑이라는 단어가 얼마나 들어가 있는가?
readf=open("text.txt",'r',encoding='utf=8')
openreadf = readf.read()

print(openreadf.count("사랑"))
readf.close()
    







