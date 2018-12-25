#import sys
import os
import progressbar
#import time
import shutil
import subprocess

print("\nПоиск папок и файлов с проектом........................\n")
dir = os.getcwd()
print("Текущая папка: ", dir)
f = os.listdir()
#f = f[1:]
print ("\nСписок файлов папок\n\n", f)

print("\nКопирование файлов в d:/gitbackup/\n  ")

try:
    bar = progressbar.ProgressBar().start()
    shutil.copytree(dir, "d:/gitbackup/")
    bar.update(50)
    bar.finish()
    print()
    print("Скопировано\n")
except FileExistsError:
    print("Папка уже существует, удаляю её\n")
    bar2 = progressbar.ProgressBar().start()
    shutil.rmtree("d:/gitbackup/")
    bar2.update(50)
    bar2.finish()
    print()
    print("Удалено\n")
    print("Копирование файлов в d:/gitbackup/\n  ")
    bar = progressbar.ProgressBar().start()
    shutil.copytree(dir, "d:/gitbackup/")
    bar.update(50)
    bar.finish()
    print()
    print("Скопировано\n")