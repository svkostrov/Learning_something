import os

bashCommand = "echo Привет >> 1.txt"
os.system(bashCommand)
os.system("cat 1.txt")
os.remove("1.txt")

