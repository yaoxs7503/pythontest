string='hello world'
c=set(string.replace(' ',''))
# print(c)
# print(type(c))
for a in c:
  count=string.count(a)
  print("单词:{} 字数{}".format(a,count))
