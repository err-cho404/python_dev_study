import urllib.request as req
url = "http://uta.pw/shodou/img/28/214.png"
savename = "testimg01.png"
imsi_img = req.urlopen(url).read()
#print(imsi_img)

with open(savename,'wb') as fs : #with로 연것은 닫을 필요없음 자동으로 닫힘
    fs.write(imsi_img)