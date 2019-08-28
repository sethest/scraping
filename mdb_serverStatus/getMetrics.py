from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getURL(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        return bsObj


try:
    bsObj = getURL("https://docs.mongodb.com/manual/reference/command/serverStatus/")
    # print(bsObj.find("head.title"))           # fail
    # print(bsObj.find("title"))                # pass
    # print(bsObj.find("head").find("title"))   # pass
    # print(bsObj.findAll("h3"))                # pass
    # print(bsObj.find("div",{"id":"instance-information"}).find("h3") )    # pass
    # print(bsObj.find("div",{"class":"section"}).find("h3") )              # pass
    # print(bsObj.find("div", {"class": "section"}))                        # pass
    print(bsObj.findAll("dl", {"class": "serverstatus"}))                   # pass
except AttributeError as e:
    print(e)
