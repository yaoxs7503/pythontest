def func_a(): 
  print('inside func_a')
def func_b(y):
  print('inside func_b')
  return y
def func_c(z):
  print('inside func_c')
  return z()

# 要把结果打印出来一定要用到print
print(func_a())
print(5+func_b(2))
print(func_c(func_a))