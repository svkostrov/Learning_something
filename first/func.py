def func (x, a, c):
  res = x + a + c
  return res

print(func("Hello", " ", "MTHFKR"))


def f2 (b):
  def f22 (bb):
    return b + bb
  return f22

test = f2 (100)
print (test(22))


def nf (n):
  def nff (n1):
    def nfff (n3):
      return n3 + n1 + n
    return nfff
  return nff


testnf = nf (2)
testnff = testnf (3)


print (testnff(4))


def passs ():
  x = 5 + 3
  pass

print (passs())

def xz (r, w ,y = 2):
  res = r + w
  res *= y
  return res
 
print(xz (33, 11, 0)) 

def funca (**args): #  * картеж, ** словарь

  return args

#print (funca(3, 5))  #выводится картеж
print(funca(a=23, b = 22))


add1 = lambda x1, y1: x1 * y1
print (add1 (2, 5))
print (add1("You bad ", 2))

