import urllib.request
f = urllib.request.urlopen("http://192.168.43.132:5000/blocks")
print(f.read())
