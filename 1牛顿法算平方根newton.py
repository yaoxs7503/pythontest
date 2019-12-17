epsilon=0.01
y=24.0
guess=y/2.0
numGuesses=0

while abs(guess*guess-y)>=epsilon:
  numGuesses+=1
  guess=guess-(((guess**2)-y)/(2*guess))
print('一共猜了'+str(numGuesses)+'次')
print('数值是'+str(y)+'多少'+str(guess))