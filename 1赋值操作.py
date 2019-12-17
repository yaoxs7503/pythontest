name1 = "wupeiqi"
name2 = name1
print(id(name1))
print(id(name2))
name2="yaoxs"
print(id(name1))
print(id(name2))
L1=[1,2,3,4]
L2=L1
print(id(L1))
print(id(L2))
L1[0]=4
print(id(L1))
print(id(L2))
T1=(1,2,3,4)
T2=T1
print(id(T1))
print(id(T2))