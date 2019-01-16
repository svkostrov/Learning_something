import datetime

print('\n______________________Калькулятор расхода______________________\n')

a = input("Введите количество израсходованных литров с момента последней полной заправки: ")
b = float(input("\nВведите сумму в рублях: "))
c = float(input("\nВведите пробег с последней полной заправки в км: "))

rashod = (100 * float(a)) / c
rashod = round(rashod, 2)

print("\nРасход", rashod, "л на 100 км")

filerashod = "rashod.txt"

f = open(filerashod, "a")
now = datetime.datetime.now()
nowtime = now.strftime("%d-%m-%Y %H:%M")
print("Текущая дата: ", nowtime)
list = [nowtime, rashod, a, c, b]
f.write("\n")
f.write(str(list))
f.close()
print("\nЗаписано в файл rashod.txt")

#['29-12-2018 11:38', 17.31, '33.59', 194.0, 1557.0]