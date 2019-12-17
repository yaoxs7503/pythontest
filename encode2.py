import sys,locale

s="小甲"
print(s)
print(type(s))
print(sys.getdefaultencoding())
print(locale.getdefaultlocale())

with open("utf1","w",encoding="utf-8") as f:
  print(f.write(s))


with open("gbk1","w",encoding="gbk") as f:
  print(f.write(s))


with open("jis1","w",encoding="shift-jis") as f:
  print(f.write(s))