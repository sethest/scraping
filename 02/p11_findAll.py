from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client

http.client._MAXHEADERS = 1000

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

headTwo = bsObj.findAll({"h1","h2"})
print(headTwo)

