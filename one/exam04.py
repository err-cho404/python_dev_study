strData = '                  나의 살던 고향은'
print("strData의 글자 수 : ",len(strData))
print("strData의 공백 지운 글자 수 : ",len(strData.lstrip()))



#a = "Life is too short Life"

#repl=a.replace("Life", "My Life")
#print(a,"\n",repl)

import re
a = "Life is too short life lIFE"

resultOne = re.sub("life", "My Life", a, flags=re.IGNORECASE)
resultTwo = re.sub("[Ll][Ii][Ff][Ee]", "My Life", a)

print(resultOne)
print(resultTwo)

b="나의 살던 고향은 꽃피던 산골"
resultSplit = b.split()
print(resultSplit)

c="나의 살던, 고향은 꽃피던 산골"
resultSplitTwo = c.split(',')

print(resultSplitTwo)

