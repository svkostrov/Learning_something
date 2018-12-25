a = {i ** 2 for i in range (10)}
print(type(a), "\n")
print("Множество а", a, "\n")
print("Добавляем во множество а 666\n")
c = 666
a.add(c)
print("Содержится ли теперь 666 во множистеве?", c in a, '\n')
x={'11', '22', "33"}
print("Множество x", x)
if 1:
  a.isdisjoint(x) #если не имеет общих элементов
  print ("а и x не имеют элемнтов общих")
else:
  print("Имеются общие элементы")

print("Объединяем a и x\n")
a.update(x)
print("Теперь а такое", a, "\n")

b = {i ** 2 for i in range (10)}

print("Объединяем b и x, пересечение\n")
b.intersection_update(x)
print("Теперь а такое", b)