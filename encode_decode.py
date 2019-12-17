#coding=gbk
import sys,locale
s="小甲"
#coding=gbk
print(s)
print(type(s))
print(sys.getdefaultencoding())
print(locale.getdefaultlocale())

with open("utf1","w",encoding="utf-8") as f:
  f.write(s)

with open("gbk1","w",encoding="gbk") as f:
  f.write(s)

with open("jis1","w",encoding="shift_jis") as f:
  f.write(s)