from collections import Counter
shakes=open('test.txt','r',encoding='utf8')
text=shakes.read().split()
changeTxt=''.join(text)
# print(changeTxt)

# def checkText(text):
  # name="爱"
  # {name:text.count(a) for a in set(text.replace(' ',''))}
  # print(i)
count=Counter(changeTxt)
name='吗'
  # number=0
for (key,value) in count.items():
  if name in key:
    print(value)

# checkText(changeTxt)
# print("查找的这个数字为{}".format(c))
# print(text[:25])
# changeTxt=Counter(''.join(text))
# print(changeTxt)
# if(name in changeTxt):
#   count+=1
