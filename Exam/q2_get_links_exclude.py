from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Node.js")
bsObj = BeautifulSoup(html.read(), "html.parser")

result = ''
for i in range(0, 4):
    result += str(bsObj.find("table", {"class": "infobox vevent"}).find_next_siblings("p")[i])


bsObj = BeautifulSoup(result,"html.parser")
links = bsObj.find_all('a')
for i in links:
    text = i.get_text()
    href = i["href"]
    if(text[:1] == '['):
        print(text + "  :  " )
    else:
        print( text + "  :  " + href )
