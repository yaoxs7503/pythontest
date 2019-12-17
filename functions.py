def applyToEach(L,f):
  for i in range(len(L)):
    L[i]=f(L[i])
  
L=[1,-2,3.4]

applyToEach(L,abs)

applyToEach(L,int)

applyToEach(L,fact)

applyToEach(L,fib)

