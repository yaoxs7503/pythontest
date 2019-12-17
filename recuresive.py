def mult(a,b):
  if b==1:
    return a
  else:
    print(a+mult(a,b-1))

print(mult(5,4))