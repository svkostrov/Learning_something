#import sys
import os
#import progressbar
#import time
#import shutil
import subprocess

print("\nПоиск папок и файлов с проектом........................\n")

g = str((os.popen("cd")).read())
g1 = str((os.popen("dir")).read())
print("Текущая папка: ", g)
print('В ней содержатся: ', g1)
f = os.listdir()
print ("\nСписок файлов\n", f)