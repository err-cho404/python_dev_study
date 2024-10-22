#가변매개변수를 사용하지 n개의 자료를 전달하고 전달 받는 방법
def fun1(a):
    print(type(a))
    sum = 0
    for i in a:
        sum=sum+i
    return sum

data1 = [1,2,3,4,5,6,7,8,9,10]

print(fun1(data1)) #함수를 호출하는 쪽에서 여러개의 자료를 하나로 묶어서 전달->반드시 자료하나를 남겨줘야 오류안남
#print(fun1()) -> 오류발생
print(fun1([]))

print("===================================================")

def fun2(*a):
    print(type(a))
    sum = 0
    for i in a:
        sum=sum+i
    return sum

print(fun2(1,2,3,4,5,6,7,8,9,10)) #반드시 자료 넣을 필요없음=>자료없으면 0 반환
print(fun2())