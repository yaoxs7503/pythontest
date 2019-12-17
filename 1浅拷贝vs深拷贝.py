values=[0,1,2]
print(id(values))
print(values)
values[1]=values[:]
print(id(values))

# 深复制
import copy
a=[0,[1,2],3]
b=copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(a[1]))
print(id(b[1]))

import copy
L=[1,2,3]
D={'a':1,'b':2}
A=L[:]
B=D.copy()
print(L,D)
print(A,B)

# 浅复制
L=[1,2]
M=L
print(id(M))
print(id(L))
L=L+[3,4]
print(id(M))
print(id(L))
print(L,M)

#浅复制和深复制
import copy
n1={"k1":"wu","k2":123,"k3":["alex",456]}
n3=copy.deepcopy(n1)
print(id(n1))
print(id(n3))
print(id(n1["k3"]))
print(id(n3["k3"]))