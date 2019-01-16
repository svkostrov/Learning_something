import re
import os

print("_______________________________")
print("\nПоиск емэилов\n")

filename = "../dump.xml"
resultfile = "../results.txt"

inputfile = open(filename)
outputfile = open(resultfile, "w")

mytext = inputfile.read()


lookfor = r"[\w.-]+@\w+\.\w+"

results = re.findall(lookfor, mytext)


for item in results:
    print(item)
    outputfile.write(item + "\n")



inputfile.close()
outputfile.close()

print("\nTotal ", len(results))

y = str(input("\nУдалить файл results? y/n "))

if y == "y":
  os.remove(str(resultfile))
  print("\nУдалено\n")
