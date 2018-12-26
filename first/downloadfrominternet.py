from urllib import request
import sys

myurl = "https://cdn.pixabay.com/photo/2018/12/16/18/12/open-fire-3879031_960_720.jpg"
myfile = "../kartinka.jpg"


try:
    print("\nСкачиваем картинку \n")
    request.urlretrieve(myurl, myfile)
except:
    print("Что-то пошло не так")
    print(sys.exc_info()[1])
    exit()

print("Картинка загружена")