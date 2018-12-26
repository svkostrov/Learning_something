from urllib import request, parse
import sys


myurl = "https://google.com/search?"
value = {'q': "Nightwish"}
myheaders = {}
myheaders['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'


try:
    mydata = parse.urlencode(value)
    print(mydata)
    myurl = myurl + mydata
    req = request.Request(myurl, headers=myheaders)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except:
    print("Error web request")
    print(sys.exc_info()[1])

