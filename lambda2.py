l1 = [8,28,36,0,0,0]
l2 = [9,57,9]

prod = list(map(lambda x:x[0]+x[1],zip(l1,l2)))

print(prod)