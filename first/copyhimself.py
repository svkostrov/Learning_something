import os
import shutil

try:
    os.mkdir("D:/Я ТУТ/")
    shutil.copy("test.exe", "D:/Я ТУТ/test.exe")
    #shutil.copy("test.py", "D:/Я ТУТ/test.py")
except FileExistsError:
    shutil.rmtree("D:/Я ТУТ/")
    shutil.copy("test.exe", "D:/Я ТУТ/test.exe")