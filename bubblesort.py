def bubble_sort(L):
  swap=False
  while not swap:
    swap=True
    for j in range(1,len(L)):
      if L[j-1]>L[j]:
        swap=False
        temp=L[j]
        L[j]=L[j-1]
        L[j-1]=temp
  return L
test=[1,5,3,8,4,9,6,2]
print(bubble_sort(test))