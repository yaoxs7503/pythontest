def genFib():
  fibn_1=1
  fibn_2=0
  while True:
    next=fibn_1+fibn_2
    yield next
    fibn_2=fibn_1
    fibn_1=next
    yield fibn_2
    fibn_2=fibn_1

fib=genFib()
print(fib)
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())