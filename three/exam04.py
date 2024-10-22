def say_myself(name, age,man=True):  # default 초기값'man=True'을 가짐
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
    return

say_myself("yang",19)
say_myself("yang",19,0)

print("=======================================")

def fun1(man=True, *a):
    pass

def fun2(man=True,**arg1):
    pass

def fun3(*args1, man=True,age):
    print(args1,man,age,sep="  ,  ")
    fun3(1,2,3,man=False,age=25)
    fun3(1,2,3,age=25)

print("===================함수 global 키워드====================")
#함수 밖의 변수 선언
name = "yang"
def fun4():
    global name
    print("name에 저장된 값 변경전===>",name) 
    name="hong"
    print("name에 저장된 값 변경후===>",name)
fun4()
print(name,'<===함수 호출 후 name에 저장된 값 출력') 

