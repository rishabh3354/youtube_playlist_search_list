# youtube playlist serach by rishabh bhardwaj

from bs4 import BeautifulSoup as bs
import requests
import json

base = "https://www.youtube.com/results?search_query="

qstring = input("enter playlist name\n")
qstring1=qstring.replace(" ", "+")

playlist="&sp=EgIQAw%253D%253D"
finalquery=base+qstring1+playlist

r = requests.get(finalquery)
page = r.text

soup = bs(page, 'html.parser')
vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})
mm=str(vids)

c = mm.count('">')
pos = 0
videolist=[]

while c > 0:
    startpos = mm.find('">', pos, len(mm))
    endpos = mm.find('</a>', startpos, len(mm))
    startpos = startpos + 2
    mydata = mm[startpos:endpos]
    pos = endpos
    c -= 1
    videolist.append(mydata)

videolistlink=[]

for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolistlink.append(tmp)

l1=[]
d1={}

for x in range(0,len(videolist)):

    d1['type']='playlist'
    d1['title']=videolist[x]
    d1['link']=videolistlink[x]

    l1.append(d1)


fvar=open(r"test.json","w")
json.dump(l1,fvar)
fvar.close()

fvar=open(r"test.json","r")
data=json.load(fvar)
fvar.close()
print(data)















