#name = input("귀하의 이름을 입력하세요")
#age = input("귀하의 나이를 입력하세요")
#member_info = "{0} 회원님의 나이는 {1} 입니다".format(name,age)
#print(member_info)

sortDataString="{0:^10}".format("hi")
print(len(sortDataString))
print(1234567890)
print(sortDataString,"영구없다",sep="")


print("="*50)
myname="yangdoll" #성:yang 이름:doll
age=19
print(f"{myname}의 나이는 {age}입니다")

"나의 성은 yang이고 이름은 doll이며 전체이름은 yangdoll,나이는 19입니다"


print(f"나의 성은 {myname[:4]}이고 이름은 {myname[4:]}이며 전체이름은 {myname},나이는 {age}입니다")

print("나의 성은 {0}이고 이름은 {1}이며 전체이름은 {2},나이는 {3}입니다".format(myname[:4],myname[4:],myname,age))



print("="*100)
strData="누구나 한 번쯤 사라에 속고 누구나 한 번쯤 사랑에 울고 그것이 사랑 사랑이야"
print("사랑 개수 : " , strData.count("사랑"))

