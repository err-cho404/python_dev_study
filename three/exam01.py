def consumer(a,b): #데이터를 소비하는 함수
    print(f"{a}와 {b}의 합은 {a+b}입니다.")
    return None
#print("=======" , consumer(30,50),"========")

def mapping(c,d):
    result1 = c+d
    result2 = c*d
    return result1,result2
returnData = mapping(10,20)
print(returnData)
print(type(returnData))
#돌려받은 값은 튜플=>변경불가, 리스트로 형변환해서 변경가능

def mapping(c,d):
    result1 = c+5
    result2 = c*5
    return result1
returnData = mapping(10,20)
print(returnData)
print(type(returnData))

def mapping(c,d):
    result1 = c+5
    result2 = c*5
    return result1,
returnData = mapping(10,20)
print(returnData)
print(type(returnData))
returnData=700
print(type(returnData))
#변수의 타입이 느슨하기 때문에 발생
