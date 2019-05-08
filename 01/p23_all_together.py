from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# "http://pythonscraping.com/pages/page1.html"

def getTitle(url):
    # avoid not found url
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        bsObj = BeautifulSoup(html.read(), "html.parser")

    # avoid not found tag
    try:
        title = bsObj.find("title")
    except AttributeError as e:
        print(e)
    else:
        return title


title = getTitle("http://pythonscraping.com/pages/page1.html")

# title tag no value
if title is None:
    print("title was not found")
else:
    print(title)
