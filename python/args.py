import sys
import os
import progressbar
import time
import shutil


print("_______________________________________________________")
i = len(sys.argv)
a = 1
if i > 1:
    if sys.argv[1] == "?":
        print("\nВведите аргументы через пробел, например: \nargs.py аргумент1 аргумент2 аргумент3\n")
    else:
        print ("Передано", i - 1, "аргументов")
        print("Вот эти аргументы:")
        while a < i:
            print ("Аргумент No", a, sys.argv[a])
            a+=1
else:
    print("Аргументы не переданы\n")
print("_______________________________________________________")

try:
 print("Удаляем старую папку")
 shutil.rmtree("temp") 
except FileNotFoundError:
 print("Папка Temp не найдена")


print("Создаём папку temp")
bar = progressbar.ProgressBar().start()
bar.update(50)
os.mkdir("temp")
time.sleep(1)
bar.finish()

bar1 = progressbar.ProgressBar().start()
print("Cоздаём", i - 1, "файлов c названиями аргументов")
db=1
b=100 / (i - 1)
while db < i:
    file = open(sys.argv[db], "w")
    file.write(sys.argv[db])
    file.close()
    bar.update(db * b)
    pathsrc = str("/home/rokot/pythonLearning/first/" + sys.argv[db])
    pathdst = str("/home/rokot/pythonLearning/first/temp/" + sys.argv[db])
    shutil.copyfile(pathsrc, pathdst)
    os.remove(pathsrc)
    db += 1
    time.sleep(0.3)

bar.finish()
time.sleep(1)


print("Файлы в текущей папке:")
os.system("cd temp/ ; ls")
#os.system("ls")
#bar1 = progressbar.ProgressBar().start()
y = str(input("Удалить эти файлы? y/n "))
ddb=1
ddb2 = 1
if y == str("y"):
    while ddb < i:
        bar.update(ddb * b)
        pathdst = str("/home/rokot/pythonLearning/first/temp/" + sys.argv[ddb])
        os.remove(pathdst)
        ddb += 1
        time.sleep(0.3)
    print()
    bar.finish()
    
y1 = str(input("Удалить папку? y/n "))

if y1 == str("y"):
        bar.update(50)
        pathdst = str("/home/rokot/pythonLearning/first/temp/")
        shutil.rmtree(pathdst)
        time.sleep(1)
        bar.update(100)
        bar.finish()
print()
print("Готово!")
	

