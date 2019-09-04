var arr = [Int]()
print("Empty? \(arr.isEmpty)")
arr.append(5)
arr.append(3)
arr += [33 ,44]
var count = arr.count
var first = arr[0]
var last = arr[arr.count - 1]
print("Empty after append? \(arr.isEmpty)")
print("Array: \(arr)")
print("first number in arr: \(first) ")
print("Couts of elements \(count)")
print("last number in arr: \(last) ")
//вставляем  33 на 1 место
arr.insert (99, at:0)
print("Now first number in \(arr) : \(arr[0]) ")
//remove
arr.remove(at: count)
print ("After remove last \(arr)")
print()

var arr2 = Array (repeating: 0, count: 7)
print("arr2: \(arr2)")
var arr3 = arr + arr2
print("arr + arr2: \(arr3)")