def remove_dups(L1,L2):
  # 非常重要的思想
  L1_copy=L1[:]
  for e in L1_copy:
    if e in L2:
      L1.remove(e)

L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups(L1,L2)
print(L1)

def remove_dups1(L1,L2):
  # 非常重要的思想

  for e in L1:
    if e in L2:
      L1.remove(e)

L1=[1,2,3,4]
L2=[1,2,5,6]
remove_dups1(L1,L2)
print(L1)