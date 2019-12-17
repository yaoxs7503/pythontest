def genSubsets(L):
  res=[]
  if len(L)==0:
    return [[]]
  smaller=genSubsets(L[:-1])
  extra=L[-1:]
  new=[]
  for small in smaller:
    new.append(small+extra)
  return smaller+new

L=[1,3,5,6,79]
print(genSubsets(L))


