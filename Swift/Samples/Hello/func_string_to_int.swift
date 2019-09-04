print("Please Enter your Name")
let name:String? = readLine()

print("Please Enter your SecondName")
let sname:String? = readLine()


func say (first: String, second: String) {
print("\(first + second)")
}

say(first: name!, second: sname!)

func say2 (str: String, str2: String) {
print("\(str + str2)")
}
say2 (str: "Anna", str2: "Gretta")

print("Please Enter first number")
let n1:String? = readLine()
var number1:Int? = Int(n1!)

print("Please Enter second number")
let n2:String? = readLine()
var number2:Int? = Int(n2!)


func sum (num1: Int, num2: Int) -> Int {
return num1 + num2
}
print("\(number1!) + \(number2!) = \(sum(num1: number1!, num2: number2!))")
print()

func calc (nums: Int...) -> (sum: Int, proizv:Int) {
var sum = 0
	for k in nums {
	sum += k 
	}
var proizv = 1
	for i in nums {
	proizv *= i
}
return (sum, proizv)
}
print("\(calc(nums: 1, 2, 3, 4, 5))")
//просто занчения
var mass = calc(nums: 1, 2, 3, 4, 5)
print("Summa: \(mass.sum) Umnojenie: \(mass.proizv)")