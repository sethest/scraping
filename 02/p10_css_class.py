from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
http.client._MAXHEADERS = 1000

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

redList = bsObj.findAll("span", {"class": "red"})
print(redList.__len__())
greenList = bsObj.findAll("span", {"class": "green"})
print(greenList.__len__())

html = urlopen("http://www.ruten.com.tw/")
bsObj = BeautifulSoup(html.read(), "html.parser")

linkList = bsObj.findAll("a", {"class":"link"})
print(linkList.__len__())