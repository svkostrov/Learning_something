class Person:
  name = "Ivan"
  age = 10
  _address = "Moscow" #доступ только для класса Person
  
  def set(self, name, age):
    self.name = name
    self.age = age

class Student (Person):
  course =1

igor = Student ()
igor.set ("Igor", 19)

print("Курс Игоря: ",igor.course)


from datetime import datetime


newman = Student()
name = input ("Введите имя: ")
age = int (input ("Введите дату рождения: "))
newman.course = int (input ("Введите курс: "))

newman.set(name, age)
print("Студент ",  newman.name, " добавлен")


now = datetime.now()
year = int( datetime.strftime(datetime.now(), "%Y"))
age = year - age


f = open("text.txt", "w")
f.write("\nСтуденты в наличии:\n")
f.write("\nИмя: " + str(newman.name) + "\n")
f.write("Возраст: " + str(newman.age)+ "\n")
f.write("Курс: " + str(newman.course)+ "\n")
f.write("добавлен: " + str(now)+ "\n")
f.close()

yes = 1

while yes == 1 :
  yes = str (input("\nДобавить нового студента? y/n: "))
  if yes == "y":
   yes = 1
   print ("Хрен там, не дописал я еще этого...")
  else:
    yes = 0 
    print ("Ну как хочешь")
  


f = open("text.txt")
print(f.read()) 
f.close

vlad = Person ()
vlad.set("Vlad", 30)
print ("\nИмя: ",vlad.name)
print ("Возраст: ",vlad.age)

username = str(input ("\nВведи своё имя: "))
print ("\n", username, "просмативает базу")
now = datetime.now()
print("\nСейчас: ", now)