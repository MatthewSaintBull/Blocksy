import urllib.request

a = input('che fare : ')
f = urllib.request.urlopen("http://0.0.0.0:5000/{0}".format(a))
print(f.read())