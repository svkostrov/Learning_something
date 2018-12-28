from urllib import request, parse
import sys
import re
import requests
import shutil
import os


myurl = sys.argv[1]
myheaders = {}
myheaders['User-Agent'] = 'Accept-language: ru", "User-Agent: Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10'



print("Исходная сыылка на картинку: ", myurl)
req = request.Request(myurl, headers=myheaders)
f = open("../imgs/imgsrc.txt", "x")
otvet = request.urlopen(req)
otvet = otvet.readlines()
f.write(str(otvet))

textlookfor = r"https://i.imgur.com/[0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-]\w+.\w\wg"
nameforlook = r"\w\w\w\w\w.\w\wg"
fullurl = re.findall(textlookfor, str(otvet))
nameimg = re.findall(nameforlook, str(otvet))

print("Имя картинки: ", nameimg[3])

myurl = str(fullurl[0])

myfile = "../imgs/" + str(nameimg[3])
try:
        print("\nСкачиваем картинку по адресу", myurl )
        r = requests.get(myurl, stream=True, headers=myheaders)
        if r.status_code == 200:
                with open(myfile, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
        print("\nКартинка загружена\n")
        print("___________________________________________________________________________\n")
        os.remove("../imgs/imgsrc.txt")

except:
        print("\nЧто-то пошло не так")
        print(sys.exc_info()[1])


