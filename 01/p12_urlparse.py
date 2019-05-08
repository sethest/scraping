# https://docs.python.org/3/library/urllib.parse.html
# <scheme>://<netloc>/<path>;<parameters>?<query>#<fragment>

from urllib.parse import urlparse
a = urlparse("http://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=3008")
print(a)
print(a.netloc)
print(a.path)
print(a.query)

