import time
def display_time(func):
  def wrapper(*args):
    t1=time.time()
    result=func(*args)
    t2=time.time()
    print("共计用了时间:{:.4}秒".format(t2-t1))
    return result
  return wrapper

def is_prime(num):
  if num<2:
    return False
  elif num==2:
    return True
  else:
    for i in range(2,num):
      if num % i ==0:
        return False
    return True 
@display_time
def prime_nums(maxnumber):
    count=0
    for i in range(2,maxnumber):
      if is_prime(i):
        count=count+1
    return count

count=prime_nums(10)
print(count)
        # print(i)
    # t2=time.time()
    # print(t2-t1)

# prime_nums()