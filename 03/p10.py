def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

addr = splitAddress(("http://oreilly.com/abc/def/hig.thm"))
print(addr[0])

addr = splitAddress("http://oreily.com")
print(addr[0])