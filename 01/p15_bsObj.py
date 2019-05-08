from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")

# bsObj = BeautifulSoup(html.read())
bsObj = BeautifulSoup(html.read(), 'html.parser')
# bsObj = BeautifulSoup(html.read(), "lxml")

print(bsObj)
print(bsObj.h1)
print(bsObj.body.h1)

