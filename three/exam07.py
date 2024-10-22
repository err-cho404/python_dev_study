f=open("text.txt",'r',encoding='utf=8')
#print(f.readline())
#print(f.readlines())
#print(f.read())
indata = f.read()
words=[]
in_lines = indata.split("\n")
for line in in_lines:
    for word in line.split():
        words.append(word)
f.close()

print(words)