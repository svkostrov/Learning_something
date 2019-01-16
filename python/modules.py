#import time
#import os
#import random as r
try:
 import nomodule
except ImportError:
  print("Нет такого модуля nomodule, да и насрать, идём дальше") 
#import module
from module import add as ad
#module.load()
a=int(input("Введи первое число: "))
b=int(input("Введи второе число: "))
ad(a, b)

#print (r.randrange (10))
#print (r.random())
#print(os.getcwd())
#print(os.uname())