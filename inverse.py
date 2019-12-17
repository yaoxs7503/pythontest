def inverse_cascade(n):
  grow(n)
  print(n)
  shrink(n)

def f_then_g(f,g,n):
  if n:
    f(n)
    g(n)