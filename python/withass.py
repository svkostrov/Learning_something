with open ("test.txt", 'wt', encoding='utf-8') as inFile:
  num = int(input("Введите число: "))
  line = str('1 / ' + str(num) + ' = ' + str(1 / num))
  print (line)
  inFile.write(line)



f = open("test.txt")
print(f.read())
f.close