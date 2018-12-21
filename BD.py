person = {"name" : {"first_name" : "Sergey", "second_name":"Kostrov"}, "address" : {"town" : "Moscow", "street" : "Veresaeva", "home" : "18"}, "phone" :{"mobile": "1234", "home": "22222"}}


print("Имя: ", person["name"]["first_name"], person["name"]["second_name"])
print("Адрес: ", person["address"]["town"], " ", person["address"]["street"], "", person["phone"]["home"])


print(person.values())
print(person.keys())