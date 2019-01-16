print  ("               Калькулятор: деление\n")

try:
  x = int (input("Введи первое число: "))
except ValueError:
  print ("  Введено не число, будет 0 ")
  x = 0
else:
  print("  Проверка правильности ввода: Выполнено")
finally:
  print("  Число сохранено")
try:  
  y = int (input("Введи второе число: ")) 
except ValueError:
  print ("  Введено не чсисло, будет 0")
  y = 0
else:
  print("  Проверка правильности ввода: Выполнено")
finally:
  print("  Число сохранено")
try:
  res = x / y
except ZeroDivisionError:
  print("На ноль делить не стоит")
  res = 0

if y == 0:
  print ("Результат: бесконечность")

else:
  print ("Результат: ", res)

# except:
  # print(sys.exc_info()[1])   вывод типа ошибки