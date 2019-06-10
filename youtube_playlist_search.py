# youtube playlist serach by rishabh bhardwaj

from bs4 import BeautifulSoup as bs
import requests
import json
import re

base = "https://www.youtube.com/results?search_query="

qstring = input("enter playlist name\n")
qstring1=qstring.replace(" ", "+")

playlist="&sp=EgIQAw%253D%253D"
finalquery=base+qstring1+playlist

r = requests.get(finalquery)
page = r.text
soup = bs(page, 'html.parser')

souptext=soup.text
number=re.findall('[0-9]{,3} videosPlay all', souptext)
numberlist=[]
for numb in number:
    number2=numb.strip('videosPlay all')
    numberlist.append(number2)

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


finaldata=[]
dictdata={}

for counter in range(0, len(numberlist)):

    dictdata['type']='playlist'
    dictdata['title']=str(videolist[counter])
    dictdata['link']=str(videolistlink[counter])
    dictdata['video_count'] = str(numberlist[counter])
    # print(dictdata)

    finaldata.append(dictdata.copy())


# print(finaldata)


fvar=open(r"test.json","w")
json.dump(finaldata,fvar)
fvar.close()

fvar=open(r"test.json","r")
data=json.load(fvar)
fvar.close()
print(data)
