def split(n):
    return n//10,n%10
all_but_last,last=split(2013)

def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
        return sum_digits(all_but_last)+last
        
sum_digits(2013)