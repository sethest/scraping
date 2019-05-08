import requests
files = { 'uploadFile': open("C:/Users/sethe/Desktop/shortcut.png", 'rb')}
r = requests.post("http://pythonscraping.com/pages/files/processing2.php", files=files)
print(r.text)