a=(10+3*5) #계산식으로 ()는 우선 순위 개념

a=(10+3*5, )#,를 사용시 ()는 튜플이 된다

a,b,c = 3,4,5
print(a)
print(b)
print(c)

(d,e,f)=(6,7,8)
print(d)
print(e)
print(f)
print("="*50)
q=20
w=30
print(q,"======",w)
q,w = w,q
print(q,"======",w)

print("="*50)
#다른 언어들에서의 값 교환 방법
q=20
w=30
print(q,"======",w)
imsi=q
q=w
w=imsi
print(q,"======",w)

print("="*50)
miss = (1,2,3)
#miss.append(4)=>튜블에서는 한번 생성되면 값 변경이 불가
misslist=list(miss)#=>튜플이 배열로 변경된다.
print(misslist)
misslist.append(4)
print(misslist)
miss=tuple(misslist)
print(miss)

