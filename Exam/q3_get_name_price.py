from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.ebay.com/sch/Hard-Drives-HDD-SSD-NAS-/158830/i.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

for text in bsObj.find_all("h3", {"class": "s-item__title"}):
    name = text.getText()
    price = text.findNext("span", {"class": "s-item__price"}).getText()
    print(name + "  :  " + price)

