def search(f):
  x=0
  while True:
    if f(x):
      return x
    x+=1

def is_three(x):
  return x==3

def square(x):
  return x*x

def positive(x):
  return max(0,square(x)-100)

