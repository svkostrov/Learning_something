from urllib import request

myurl = "https://ya.ru"

otvet = request.urlopen(myurl)
mytext1 = otvet.readlines()
mytext2 = otvet.read()


print("____________")
print ("\nOtvet: ", otvet)
print("____________")

print("\nMy text2: ", mytext2)
print("____________")


for line in mytext1:
    print(line)