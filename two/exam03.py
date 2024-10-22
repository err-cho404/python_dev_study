# set은 순서가 없다. 중복된 데이터를 갖지 않는다.
# 1.리터럴을 이용한 set 자료 생성
setData1 = {1,2,3,1,2,3,4,5,6}
print(setData1)
# print(setData1[0]) =>순서가 없으므로 불가(인덱스를 이용한 자료읽기가 불가능 하다)
# 반복문을 사용해 읽어오거나 list로 형식 바꾸어 가져오는 방법이 있다.
setData1ConList = list(setData1) #set구조를 list로 바꿈
print(setData1ConList[0])

print("============================")
for setData in setData1:
    print(setData) #순서가 없어 자료의 구성 순서대로 출력이 보장되지는 않는다


print("============================")
# 2.set메서드(set생성자)를 이용한 자료 생성
setData2 = set([1,2,3,4,5,1,7,5,1,6,5])
print(setData2)

print("============================")
setData3 = set('qwertyuiqwertyui')
print(setData3)

print("============================")
setData4 = set('나의 살던 고향은 꽃피는 산골'.split()) #set(['나의','살던' ......])
print(setData4)

print("==============논리 자료==============")
bool1 = True
bool2 = 10==20 #False
print(bool2)

dataEx1 = (None)

if dataEx1:
    print(f'숫자 {dataEx1}은 참으로 해석됩니다')
else:  
    print(f'숫자 {dataEx1}은 거짓으로 해석됩니다')