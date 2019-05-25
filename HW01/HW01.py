# HW01: 請寫一爬蟲抓取google新聞中的”健康”的”最新”新聞標題與新聞來源與日期，存入一個sqlite檔案中。請上傳你的程式與sqlite檔案。

from urllib.request import urlopen
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

html = urlopen(
    "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
bsObj = BeautifulSoup(html.read(), "html.parser")

itemList = bsObj.findAll("div", {"class": "xrnccd"})

id = 0
dArr = []
for item in itemList:
    id += 1
    titleText = item.find("a", {"class": "DY5T1d"}).getText()
    sourceText = item.find("a", {"class": "wEwyrc AVN2gc uQIVzc Sksgp"}).getText()
    date = item.find("time", {"class": "WW6dff uQIVzc Sksgp"})
    dateText = ''
    d = {}
    if date != None:
        dateText = date.getText()
        d = {"id": id, "titleText": titleText, "sourceText": sourceText, "dateText": dateText}
    else:
        d = {"id": id, "titleText": titleText, "sourceText": sourceText, "dateText": ""}
    dArr.append(d)

print(dArr)

### SQLite setting
engine = create_engine('sqlite:///HW01.db', echo=False)
meta = MetaData()
HW01 = Table('HW01', meta,
             Column('id', Integer, primary_key=True),
             Column('titleText', String),
             Column('sourceText', String),
             Column('dateText', String))

meta.create_all(engine)
HW01.drop(engine, checkfirst=True)
HW01.create(engine, checkfirst=True)
conn = engine.connect()
conn.execute(HW01.insert(), dArr)
