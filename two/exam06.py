a=[(1,2,3),(3,4,5),(5,6,6)]
for first,last,end in a:
    print(first+last+end)

#for (first,last) in a:
#   print(first+last)  자료와 매칭이 안되어 오류발생


b=[(1,2),(3,4,5),(5,6,6,8)]
for elements in b:
    print(elements)
    sum = 0
    for i in elements:
        sum+=i
    print(sum)


print("==================응용 문제===================")
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)


print("==================다른 방법===================")
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
        continue
    print("%d번 학생은 불합격입니다." % number)



print("==================정보처리 기사 문제===================")
#합격 불합격을 판단하는 프로그램 작성
marks = [90, 25, 67, 45, 80]
marks.sort() #미리 정렬해서 작은 수를 앞에 오게 함(무의미한 반복을 줄여줌)=>안써도 결과에는 문제 없음
for mark in marks: 
    if mark<40: #과락먼저 결과내고 모든과목 더 40점이상이면
        print("과락") 
        break #현재 if문에서 나감
    sum=sum+mark #총합점수 계산
#    print(sum)
if sum/len(marks) <60: #총합점수가 60점 미만이면 불합격
    print("불합격") 
else : #그외(과락없고 60점 이상의 경우만 남음)는 합격
    print("합격")
    

print("==================정보처리 기사 문제(선생님 풀이 법)===================")
marks = [100, 65, 100,100, 5] #정보처리 기사 시험의 각 과목별 점수
# 합격 불합격을 판단하는 프로그램을 작성하시오...
sum = 0
marks.sort() #오름차순으로 리스트이 내용을 정렬
panjumg = '불합격'
for jum in marks:
    if jum < 40 : # 과락 검증
        print('과락')
#        sum = 299 
        break
    sum += jum
if sum / len(marks) >=60 :
    panjumg = "합격"
print(panjumg)