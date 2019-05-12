from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Node.js")
bsObj = BeautifulSoup(html.read(),"html.parser")


text = bsObj.find(title="List of server-side JavaScript implementations").parent.parent
for link in text('a'):
    print(link.get_text() + "  :  " + link['href'])





