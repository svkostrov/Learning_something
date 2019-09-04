//может быть значение, а может и не быть
// объявление var friend : String?
// чтобы вытащить friend!



print("Please Enter your Name")
let name:String? = readLine()

if name! == "" {
print("Emty name")
}else {
print("Your name is \(name!)")
}


var friend : String?
friend = "Alex"


if friend != nil {
print("FriendList not empty")
}
if friend == nil {
print("FriendList empty")
}