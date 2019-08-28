# https://docs.python.org/3/library/urllib.html
from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

# https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
with  urlopen("http://pythonscraping.com/pages/page1.html") as html:
    print(html.read())