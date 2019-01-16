class Person:
  name = "Ivan"
  age = 10
  _address = "Moscow" #доступ только для класса Person
  
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def set(self, name, age):
    self.name = name
    self.age = age

class Student (Person):
  #course = 2
  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

igor = Student ("Igor", 19, 6)


print("Курс Игоря: ", igor.course)


