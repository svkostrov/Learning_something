enum Cars {
	case Audi
	case BMW
	case Volvo
	case Ford
}

var car = Cars.BMW

struct Square {

	var lenght : Int
		func sum (num: Int) {
		print("\(num + num)")
	}
}

var block = Square (lenght: 10)
block.sum (num: 2)