L1=[8,28,36,2.2]
L2=[9,57,9,23,45.5]
L2_copy=[]
sum=0
L3=[]
for i in range(len(L1)):
  for t in range(len(L2)):
    if i==t:
      sum=L1[i]+L2[t]
      L2_copy.append(sum)
if len(L2)>len(L1):
  for i in (range(len(L2)-len(L1))):
    L3=L2[len(L1):len(L2)]
    sum=L3[i]
    L2_copy.append(sum)
else:
  for t in (range(len(L1)-len(L2))):
    L3=L1[len(L2):len(L1)]
    sum=L3[t]
    L2_copy.append(sum)
print(L2_copy)