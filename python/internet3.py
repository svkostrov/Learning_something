from urllib import request
import re
import os


nepodoshli = []
b = list(range(1, 99))
for num in b:
    print("Определяем хостинг....\n")

    url = "http://prntscr.com/m0ks" + str(num)
    myheaders = {}
    myheaders['User-Agent'] = 'Accept-language: ru", "User-Agent: Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10'

    print("Исходная сcылка на картинку: ", url)
    req = request.Request(url, headers=myheaders)
    f = open("../imgs/imghost.txt", "x")
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    f.write(str(otvet))

    textprntsc = r"https://image.prntscr.com/image/[0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-]+.\w\wg"
    textimgur = r"imgur"
    nameforlook = r"[0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-][0-9a-zA-Z_-]+.\w\wg"
    textimageshack = r"imageshack.us"

    etoprnsc = re.findall(textprntsc, str(otvet))
    etoimgur = re.findall(textimgur, str(otvet))
    etoimageshack = re.findall(textimageshack, str(otvet))

    try:
        try:
            print("imageshak? ", etoimageshack[0])
        except:
            print("Имгур? ", etoimgur[0])
            os.system('python3 imgur.py ' + str(url))

    except:
        try:
            print("printsc? ", etoprnsc[0])
            os.system('python3 prtsc.py ' + str(url))
        except:
            print("\nНе подшло под регулярное выражение: ", url, "\n")
            nepodoshli.append(url)


    finally:
        os.remove("../imgs/imghost.txt")



print("Не подошли эти:", nepodoshli)