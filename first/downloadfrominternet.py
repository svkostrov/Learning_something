from urllib import request
import sys

imgname = "tSTG6"
img = imgname + ".png"

myurl = "https://i.imgur.com/" + img
myfile = "../" + img


try:
    print("\nСкачиваем картинку \n")
    request.urlretrieve(myurl, myfile)
except:
    print("Что-то пошло не так")
    print(sys.exc_info()[1])
    exit()

print("Картинка загружена")