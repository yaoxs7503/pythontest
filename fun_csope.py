def g(x):
  def h():
    x='abc'
    return x
  x=x+1
  print('in g(x): x=',x)
  h()
  return x

x=3
z=g(x)
print(g(x))