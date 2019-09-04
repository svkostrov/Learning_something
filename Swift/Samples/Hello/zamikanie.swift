var zam: (Int) -> (Int) = {
	num in
	return num * num
}
print ("5 v kvadrate = \(zam(5))")

var numbers = [9, 4, 5, 8, 2, 7]
let sorted = numbers.sorted(by: {
x, y in x < y
})
 
for i in sorted {
	print (i)
}