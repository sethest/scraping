from urllib.parse import urlparse
a = urlparse("http://search.ruten.com.tw/search/s000.php?enc=u&searchfrom=indexbar&k=iphone&t=0&p=2")
print(a)
print(a.netloc)
print(a.path)
print(a.query)

# print(type(a.query))
commands = a.query.split("&")
for c in commands:
    print(c)
