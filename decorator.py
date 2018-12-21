def decorator (fun):
  def wrapper():
    print("Код до выполнения функции ")
    fun()
    print("Код, который сработал после функции ")
  return wrapper

@decorator
def show ():
  print ("Я обычная функция")
 
show()