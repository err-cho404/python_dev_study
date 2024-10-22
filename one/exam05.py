listdata = [] #리터럴을 이용한 리스트(배열)
listdataTwo = list() #생성자 함수를 통해서 비어있는 리스트 만듦

print(type(listdataTwo),len(listdata),len(listdataTwo))


listdataThree = [1,2,'영구없다','땡칠이없다', (3,4),{},[]] #리스트 안에는 모든 요소타입이 들어갈 수 있다

print(type(listdataThree),len(listdataThree),listdataThree[3][:3])

a=[1,2,3,['a','b','c']]
print(a[-1][1])

b=[1,2,3,4,5]
print(b[0],"     ",type(b[0:1]),type(b[0]))

del a[0]
print(a)


del a[2][:2]
print(a)

a.append([5,6,7])
print(a)
a+=[8,9,10]
print(a)
a+=[[8,9,10]]
print(a)


print("="*50)

c=[1,2,3,4]

print(c+[5,6,7]) #새로운 리스트가 생성된 개념
print(c) #원본은 변하지 않음 
print("="*50)
print(c.extend([5,6,7])) #c리스트에 츄가된 개념
print(c)