a = 20
b = a #옅은 복사
print(a,b,sep='\t\t')
a = 30
print(a,b,sep='\t\t')

print("============================")

groupa=[1,2]
groupb=groupa
print(groupa,groupb,sep='\t\t')
groupa[0] = groupa[0]*12
print(groupa,groupb,sep='\t\t')




print("=============구분자=============")
#숫자, 문자열을 담겨있는 변수를 다른 변수에 할당하면 원본과 복사본의 값을 변경해도 서로에게 영향을 주지 않는다->일반적 인식
#묶음데이터의 경우 값을 변경하게 되면 복사본이 영향을 받음 (파이썬은 다 참조 타입의 선언을 한다-동적이기 때문에)
a = 20
b = a #옅은 복사
print(a,b,sep='\t\t')
b = 30
print(a,b,sep='\t\t')

print("============================")

groupa=[1,2]
groupb=groupa 
print(groupa,groupb,sep='\t\t')
groupb[0] = groupb[0]*12 #옅은 복사이기 때문에 원본값에도 영향을 줌
print(groupa,groupb,sep='\t\t')

print("============================")
#원본은 유지하면서 복사본만 변경(깊은 복사)
import copy
a = [1,2,3]
b = copy.deepcopy(a)
print(a,b,sep="\t")
b[0] = 12345
print(a,b,sep="\t")


print("=============구분자=============")
tuData = (1,2,3)
print(tuData[0])
#tuData[0] = 2 튜플안의 데이터 변경 불가
tuData2 = ([1,2,3])
print(type(tuData2))
tuData2 = ([1,2,3],)
print(type(tuData2))

tuData2[0].append(4)
print(tuData2)

print(5 in [1,2,3,4,5]) #5가 [1,2,3,4,5]안에 있는가 => True False반환
