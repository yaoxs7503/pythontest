y=24
epsilon=0.01
numGuesses=0
low=1.0
high=y
ans=(high+low)/2.0

while abs(ans**2-y)>=epsilon:
  # print('low=' +str(low)+'high='+str(high)+"ans="+str(ans))
  numGuesses+=1
  if ans**2<y:
    low=ans
  else:
    high=ans
  ans=(high+low)/2.0
print('一共猜了'+str(numGuesses)+'次')
print(str(ans)+'接近于'+str(y))