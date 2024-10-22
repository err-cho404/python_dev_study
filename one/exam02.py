a = "Life is too short, You need Python"
a1 = a[0:7]
a2 = a[:7]
a3 = a[7:]
a4 = a[7:-1]
a5 = a[7:0]
a6 = a[7::2] #7번부터 두칸씩 건너뛰며 출력
a7 = a[:] 
print(a,"원본 문자열")
print(a1,"a[0:7]로 슬라이싱한 문자열")
print(a2,"a[:7]로 슬라이싱한 문자열")
print(a3,"a[7:]로 슬라이싱한 문자열")
print(a4,"a[7:-1]로 슬라이싱한 문자열")
print(a5,"a[7:0]로 슬라이싱한 문자열")
print(a6,"a[7::0]로 슬라이싱한 문자열")
print(a7,"a[:] 로 슬라이싱한 문자열")

print("=" * 50)

list_a = [1,2,3,4,5,6,7,8,9]
print(list_a[:3:2])

list_a[0]=15

print(list_a)

print( "I eat %s apples." % "five" )
print( "I eat %d apples." % 3)

a = "Pithon"
#a[1]
#a[1] = 'y' =>불가
print(a[:1] + 'y' + a[2:])
print(a[0] + 'y' + a[2:])

number = 10
day = "three"
print( "I ate %d apples. so I was sick for %s days." % (number, day) )

