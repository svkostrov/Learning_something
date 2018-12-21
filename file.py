f = open ("text.txt")
#print(f.read ())

for line in f:
 print("Было: \n", line )
f.close()

f = open ("text.txt", "w")
f.write("\nHi, its me")
f.close()

f = open ("text.txt")
print("Стало: ", f.read ())
f.close()

f = open ("text.txt", "w")
f.write("Привет! ")
f.close()