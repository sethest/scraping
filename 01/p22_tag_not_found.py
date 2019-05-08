from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)

if html is None:
    print("server not found")
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    try:
        content = bsObj.find("nonExistingTag").find("anotherTag")
    except AttributeError as e:
        print(e)
    else:
        if content == None:
            print("tag not found")
        else:
            print(content)