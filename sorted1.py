list1 = [7,3,10,12,5,1,2] ##随机定义了两个列表
list2 = [4,6,11]
list3 = list1 + list2 ##列表的合并
j = 0
while j < len(list3)-1:
    i = 0
    while i < len(list3)-(j+1):
        if list3[i] > list3[i+1]:
            a = list3[i]
            list3[i] = list3[i+1]
            list3[i+1] = a
        i += 1
    j += 1
print(list3)

