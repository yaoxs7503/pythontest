# def genTest():
#   yield 1
#   yield 2

# foo=genTest()
# print(genTest().__next__())
# print(genTest().__next__())
# print(foo.__next__())
# print(foo.__next__())
# print(foo.__next__())

def genFib():
  fibn_1=1
  fibn_2=0
  while True:
    next=fibn_1+fibn_2
    yield next
    fibn_2=fibn_1
    fibn_1=next

fib=genFib()
print(fib)
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())