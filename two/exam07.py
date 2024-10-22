print(range(5))  #인덱스 0부터 5전까지
print(list(range(5)))
print(range(1,5)) #인덱스 1부터 5전까지
print(list(range(1,5)))
print(list(range(1,5,2)))#인덱스 1부터 5전까지 숫자를 2의 간격으로 뛰어 넘어 출력

for i in range(11): #10전까지 출력임. 이게 헷갈린다면 10+1의 형식으로 적어줘도 된다.
    print(i)

sum=0
for i in range(1,11):
    sum+=i  #1~10까지의 숫자를 더함 1+2+3+4+5+6+7+8+9+10
print(sum)

listData =[10,25,30,45,70,85,95] #인덱스 순서 [0,1,2,3,4,5,6]
'''
sum=0
for i in range(len(listData)):
    sum+=listData[i]
print(sum)
'''
print("=====================================")
for i in range(0,len(listData),2): #range(1,7,2) => listData에서 25,45,85
    
    sum+=listData[i]
print(range(1,len(listData),2))
print(sum)


for i in range(2,10):        # 1번 for문
     for j in range(1, 10):   # 2번 for문
         print(i*j, end=" ") 
     print('') 

     
for i in range(2,9+1,3):        # 1번 for문
     for j in range(1, 9+1):   # 2번 for문
         print(f"{i} * {j} = {i*j}") 
     print() 


for i in range(2,10+1,3):        # 1번 for문
     for j in range(1, 9+1):   # 2번 for문
         print(f"{i} * {j} = {i*j}\t{i+1} * {j} = {(i+1)*j}\t{i+2} * {j} = {(i+2)*j} ") 
     print() 

for i in range(2,9+1,3):        # 1번 for문
    for j in range(1, 9+1):   # 2번 for문
        print(f"{i} * {j} = {i*j}\t",end="")
        print(f"{i+1} * {j} = {(i+1)*j}\t",end="")
        if i+2>9:
            print()
            continue
        print(f"{i+2} * {j} = {(i+2)*j}")
    print() 


print("================리스트 컴프리헨션를 이용한 구구단 배열 리스트=================")
result = [x*y for x in range(2,10)
                for y in range(1,10)]
print(result) #==>중첩 for문은 비권장 하는 방법

result=[]
for i in range(2,9+1):
    for j in range (1,9+1):
        result.append(i*j)
print(result)