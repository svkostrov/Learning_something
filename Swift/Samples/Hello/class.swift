class Person {
var name: String = "No name"
var sname: String = "no sname"
var age: Int = 0
var weight: Float = 0.0

init (name: String, sname: String, age: Int, weight: Float) {

	self.name = name
	self.sname = sname
	self.age = age
	self.weight = weight
	}

func info() {

	print("Info about new user\nName: \(self.name) \nSnmame: \(self.sname) \nAge: \(self.age) \nWeight: \(self.weight) ")

	}

func chname_sname (name: String, sname: String) {
	self.name = name
	self.sname = sname

	}
}

func Opros_name() -> String {
	print("Please Enter your name ")
	let uname = readLine()
	return uname!
	}
func Opros_sname() -> String  {
	print("Please Enter your Sname ")
	let usname = readLine()
	return usname!
	}
func Opros_age() -> Int {
	print("Please Enter your age ")
	let uage = readLine()
	let intuage:Int? = Int(uage!)
	return intuage!
	}
func Opros_weight() -> Float {
	print("Please Enter your weight ")
	let uweight = readLine()
	let floatuweight:Float? = Float(uweight!)
	return floatuweight!
	}


var name1: String = Opros_name()
var sname1: String = Opros_sname()
var age1: Int = Opros_age()
var weight1: Float = Opros_weight()

var User = Person (name: name1, sname: sname1, age: age1, weight: weight1)
print()
User.info()

//меняем фамилию
User.chname_sname (name: "Vasia", sname: "Pupkin")

print()
print("New edited user")
User.info()