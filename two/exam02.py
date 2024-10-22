students = [
    {'hakbun':3701,'name':'홍길동','kor':90,'eng':80,'math':70},
    {'hakbun':3702,'name':'나일등','kor':90,'eng':95,'math':90},
    {'hakbun':3703,'name':'김다비','kor':70,'eng':90,'math':70},
    {'hakbun':3704,'name':'나꼴등','kor':60,'eng':70,'math':65},
    {'hakbun':3705,'name':'구민아','kor':70,'eng':80,'math':95}
] #테이블 형태의 자료 구성(리스트로 만들어서 값으로 딕셔너리를 집어넣음)


for student_dict in students :
    if student_dict.get('hakbun') <= 3703: #3703보다 작은 애들은
        continue #다음으로 넘어가라(조기리턴)
    for value in student_dict.values():
        print(value, end = "  ")
    print()
print("======end=======")