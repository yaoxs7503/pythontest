import time
def fib(n):
  global numFibCalls
  numFibCalls+=1
  if n==1:
    return 1
  elif n==2:
    return 2
  else:  
    return fib(n-1)+fib(n-2)

def fib_efficient(n,d):
  global numFibCalls
  numFibCalls+=1
  if n in d:
    return d[n]
  else:
    ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
    d[n]=ans
    return ans

d={1:1,2:2}
# print(fib_efficient(n,d))

argToUse=12
print("")
print('using fib')
# t1=time.time()
numFibCalls=0
print(fib(argToUse))
print('function calls',numFibCalls)
# t2=time.time()
# print('共计用了时间：{:.4}秒'.format(t2-t1))
print("")
numFibCalls=0
print('using fib_efficient')
# t3=time.time()
# print(t3)
print(fib_efficient(argToUse,d))
print('function calls',numFibCalls)
# t4=time.time()
# print(t4)
# print('字典数列共计用了时间：{:.4}秒'.format(t4-t3))