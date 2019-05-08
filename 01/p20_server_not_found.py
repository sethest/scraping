from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getURL():
    return None

html = getURL()
if html is None:
    print("server not found")
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.div)

