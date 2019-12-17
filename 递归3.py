from ucb import trace

@trace
def square(x):
  return x*x

def sum_squares_up_to(n):
  k=1
  total=0
  while k<=n:
    total,k=total+square(k),k+1
  return total


