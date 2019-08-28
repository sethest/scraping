from urllib.request import urlopen
from bs4 import BeautifulSoup

with urlopen("http://www.pythonscraping.com/pages/page1.html") as f:
    bsObj = BeautifulSoup(f.read(), "html.parser")
    print(bsObj.div)            # 方式1 (棄用)
    print(bsObj.find("div"))    # 方式2 (建議) 可以設定 AttributeError handling (p.20)