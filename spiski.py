
print("Это L")
l = [34, "sd", 56, 34.34]
print(l)

print("Это b")
b = [24, 67]
print (b)

print("Добавление в конец l")
l.append("new") 
print(l)

print("Добавляем b к l")
l.extend(b)
print(l)

print("Insert to 0 index")
l.insert(0, "1st element")
print(l)

print("Удаляет конкретный элемент 1 раз(34)")
l.remove(34)
print(l)

print("удаляет iй или последний элемент")
l.pop()
print(l)

print("возврат индекса конкретного элемента")
print(l.index(34.34))

print("Возврат количество конкретных элементов в списке")
print(l.count(34))

print("Сортировка-закомичено")
#l.sort()
#print(l)

print("Реверс")
l.reverse
print(l)

print("Длина списка")
print(len(l))

print("Последний элемент")
print(l[-1])

print("Предпоследний")
print(l[-2])

print("Срез l[start:stop:step] ")
print(l[::2])

print("Очистка")
l.clear()
print(l)





#https://repl.it/repls/ShamefulAdorableAggregators