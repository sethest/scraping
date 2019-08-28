from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# "http://pythonscraping.com/pages/page1.html"
# 定義方法
def getTitle(url):
    # p17_page_not_found
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        bsObj = BeautifulSoup(html.read(), "html.parser")

    # p18_tag_not_found
    try:
        title = bsObj.find("title")
    except AttributeError as e:
        print(e)
    else:
        return title


# 程式進入點 (呼叫方法)
title = getTitle("http://pythonscraping.com/pages/page1.html")

# p20_server_not_found
if title is None:
    print("title was not found")
else:
    print(title)
