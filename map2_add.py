L1=[8,28,36]
L2=[9,57,9]
L2_copy=[]
sum=0
# for elt in L1:
#   for elt2 in L2:
#   sum=elt+elt2
#   L2_copy.append(sum)
# print(L2_copy)

for i in range(len(L1)):
  for t in range(len(L2)):
    if i==t:
      sum=L1[i]+L2[t]
      L2_copy.append(sum)

print(L2_copy)