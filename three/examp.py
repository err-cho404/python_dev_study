#사칙연산을 수행하는 함수를 작성하시오

#덧셈=>multiCalcu(10,20,'+') =>30
#뺄셈=>multiCalcu(10,20,'-') =>-10
#나눗셈=>multiCalcu(10,20,'/') => 0.5
#곱셈=>multiCalcu(10,20,'*') =>200
#나머지=>multiCalcu(10,20,'%') =>10
#몫=>multiCalcu(10,20,'//') =>0

'''def multiCalcu2(a,b):
    add = lambda a,b : a+b
    print(add(a,b))
    sub = lambda a,b : a-b
    print(sub(a,b))
    mul = lambda a,b : a*b
    print(mul(a,b))
    div = lambda a,b : a/b
    print(div(a,b))
    quote = lambda a,b : a//b
    print(quote(a,b))
    rest = lambda a,b : a%b
    print(rest(a,b))
multiCalcu2(10,20)
'''
var_def = 'yangdoll'
def multi_calcu(data1,data2,operator):
    oper_dict={
        '+' : data1 + data2,
        '-' : data1 - data2,
        '*' : data1 * data2,
        '/' : data1 / data2,
        '%' : data1 % data2,
        '//' : data1 // data2,
        '**' : data1 ** data2
    }
    return oper_dict[operator]

print(multi_calcu(10,20,'*'))




#eval함수 사용법
'''
data1 = str(data1) ; data2 = str(data2)
result = eval(data1+operator+data2)
return result
'''
