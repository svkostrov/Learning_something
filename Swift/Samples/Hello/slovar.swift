var dict = [String:String]()
dict["Name"] = "Sergey"
//dict.append("Fename":"Kostrov")
print("\(dict)")
print("\(dict["Name"])")
print()

var dict2:[String:String] = ["first": "Lex", "second": "Max"]
print("\(dict2["second"])")
print()

print("Perebor")
for (key, value) in dict2 {
print("\(key) : \(value)")
}
