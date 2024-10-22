import urllib.request as req
import urllib.parse

url ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = { # 내가 넘겨 받고자 하는 속성 파라미터를 딕셔너리로 만듦
    'stnId' : '184' #내가 보고자 하는 지역의 날씨 일보 184 -> 제주 / 109 -> 서울 경기 / 105 -> 강원도
}
params = urllib.parse.urlencode(values)  #딕셔너리를 데이터를 파라미터 형식으로 변환해줌
url = url + "?" + params
res = req.urlopen(url)
get_data = res.read().decode("utf-8") #16진수로 데이터가 나오면 한글 포함일 수 있음. 그럴때는 decode "utf-8"로 읽어오기

print(get_data)