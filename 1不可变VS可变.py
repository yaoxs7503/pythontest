# int 类型
i=5
print(id(i))
i+=1
print(i)
print(id(i))
# 浮点数
i=2.5
print(id(i))
i+=1
print(i)
print(id(i))
c=2.5
print(id(c))
# 可变类型
a=[1,2,3]
print(id(a))
b=a
b.append(4)
print(id(b))

a={1:"yaoxs",2:"philip"}
print(id(a))
b=a
b["name"]="ying"
print(id(b))
print(a)
print(id(a))