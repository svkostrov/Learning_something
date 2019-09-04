for i in 1...13 {
print ("i is \(i)")
}
print()

print("Iz massiva")
var arr = [1, 2, 3, 4, 6, 8]  
for i in arr where (i / 2) == 2 && (i % 2) == 0 {
print("\(i)")
}
print()

print("Iz spiska")
for i in 1...10 where (i / 2) == 2 && (i % 2) == 0 {
print("\(i)")
}
print()


print("Perebor while and if, stop na 10 i propuskaem 9")
var i = 0
while i < 50 {
	if i > 10 {
	break
	}
	if i == 9 {
	i += 1
	continue
	}
print ("\(i)")
i += 1
}
print()

print("Cikl srabotaet hotiabi 1 raz")
i = 100
repeat {
	print("\(i)")
}while (i < 10)

