cube=36
epsilon=0.01
guess=0.0
increment=0.0001
num_guesses=0
while abs(guess**3-cube)>=epsilon and guess <= cube:
  guess+=increment
  num_guesses+=1
print('猜测的次数',num_guesses)
if abs(guess**3-cube)>=epsilon:
  print('猜错了数字',cube)
else:
  print(guess,'猜的数字是',cube)