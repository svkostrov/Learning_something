print("Please Enter your age", terminator: ".")
let age2 = readLine()
print("Your age is \(age2!).")
let intage:Int? = Int(age2!)


switch intage {
case 18:
	print("Come in")
case 5:
	print("Come out")
default:
	print("AgeCode denyed")
}