from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    # html = urlopen("http://pythonscraping.com/pages/xxx.html")
except HTTPError as e:
    print(e)

if html is None:
    print("server not found")
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    try:
        badContent = bsObj.find("nonExistingTag").find("anotherTag")
        # badContent = bsObj.nonExistingTag.anotherTag  # 棄用
    except AttributeError as e:
        print(e)
        print("Tag was not found")
    else:
        if badContent == None:
            print("tag not found")
        else:
            print(badContent)
