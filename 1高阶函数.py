L2=[1,2,3,4,5]

for i in range(len(L2)):
  if(L2[i]!=4):
    print(L2[i])
  
print(L2)
print(list(filter(lambda x:x>9,map(lambda x:x*4,filter(lambda x:x!=4,L2)))))