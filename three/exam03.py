def fun1(age,*b): #반드시 a는 전달 되어야하고, b부터는(가변인자로) 옵션이다
    print(age)
#    b[0] = b[0]*50 -> tuple이라 값 변경이 불가능하다
    print(b)
    return

fun1(19,50)

print("=======================================")

def fun2(*b,age): #age가 값을 빋지못하고 b가 다 가져감 => positional argument 인 age는 값이 필수로 들어가야하는데 못받으니 오류가남
    print(age)              #같이 쓰일때 positional argument가 반드시 가변매개변수보다 앞에 와야한다.
#    b[0] = b[0]*50 
    print(b)
    return

fun2('나의','살던','고향은',age=50)
print(1,2,3,4,5,sep="   ,   ")
fun2(age=10)

print("=======================================")

def fun3(**args):
    print(type(args))
    print(args.keys())
    print(args.values())
fun3()
fun3(name='yang',age=19)

print("=======================================")

def fun4(*varargs,**vardicargs):
    print(varargs)
    print(vardicargs)
    return
fun4(12, 34, 56, name='yang', age =19, address = "suwon" , jumsu=[100,11,75,97,100])


