print("Please Enter your age", terminator: ".")
let age2 = readLine()
print("Your age is \(age2!).")
let intage:Int? = Int(age2!)
print("New age \(intage!)")


//var age = 8

if intage! >= 18 {
print ("You good!!")
}else if intage! < 4 {
print ("You soo little!")
}else if (intage! >= 5) &&  (intage! == 5) {
print("You are 5 years old?")
} else {
print("Age bad")
}

var result = (intage! >  6) || (!true) ? "Right" : "Wrong"
print ("\(result)")