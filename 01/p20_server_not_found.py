from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 如果沒有處理程序處理請求，則可以返回None（儘管默認安裝的全局OpenerDirector使用UnknownHandler來確保永遠不會發生這種情況）
def getURL():
    return None

html = getURL()
if html is None:
    print("server not found")
else:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.div)

