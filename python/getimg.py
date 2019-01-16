from urllib import request
import sys

b = list(range(1, 50))

for num in b:
    imgname = "tSTG" + str(num)
    img = imgname + ".png"
    myurl = "https://i.imgur.com/" + img
    print (myurl)
    myfile = "../imgs/" + img
    try:
        print("\nСкачиваем картинку \n")
        request.urlretrieve(myurl, myfile)
    except:
        print("Что-то пошло не так")
        print(sys.exc_info()[1])
        #exit()

print("Картинки загружены")