def bisect_search1(L,e):
  if L==[]:
    return False
  elif len(L)==1:
    return L[0]==e
  else:
    half=len(L)//2
    if L[half] > e:
      return bisect_search1(L[:half],e)
    else:
      return bisect_search1(L[half:],e)

L=[1,3,5,7,8,9]
bisect_search1(L,15)
