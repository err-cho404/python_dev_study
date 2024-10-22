dict_data={'김연아':'피겨스케이팅선수'} #딕셔너리 데이터 생성

print(dict_data)

dict_data['김연경']='배구선수' #딕셔너리 데이터 추가

print(dict_data)

dict_data['김연경']='배구여제' #딕셔너리 값 수정

print(dict_data)

del dict_data['김연경'] #딕셔너리 데이터 삭제

print(dict_data)

dict_data['김연경']='배구여제' #딕셔너리 데이터 추가

print(dict_data)

dict_data['손흥민']='축구선수' #딕셔너리 데이터 추가

print(dict_data)


for keyName in dict_data.keys():
    print(keyName,end=" => ")
    print(dict_data[keyName]+" 입니다.")

#딕셔너리의 장점 : k값(사용자가 정의한 k값으로)으로 자료를 검색할 수 있다. => 키값이 메모리를 차지하는 양이 많을 수 있다.
#리스트는 저장된 인덱스 위치를 알아야만 찾을 수 있다.