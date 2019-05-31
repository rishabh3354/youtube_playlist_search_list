# youtube playlist serach by rishabh bhardwaj

from bs4 import BeautifulSoup as bs
import requests


base = "https://www.youtube.com/results?search_query="

qstring = input("enter playlist name\n")
qstring1=qstring.replace(" ","+")
# print(qstring)

playlist="&sp=EgIQAw%253D%253D"
finalquery=base+qstring1+playlist

r = requests.get(finalquery)
page = r.text

soup = bs(page, 'html.parser')


vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

# print(vids)
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
    # print(mydata)
    videolist.append(mydata)

videolistlink=[]

for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolistlink.append(tmp)

print(videolistlink)
# print(len(videolistlink))
print()
print(videolist)
# print(len(videolist))
