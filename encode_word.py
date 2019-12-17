#coding=shift-jis
import sys, locale

s = "小甲"
print(s)
print(type(s))
print(sys.getdefaultencoding())
print(locale.getdefaultlocale(), "\n\n")

a = s.encode("shift-jis")
print(a)
print(type(a))
b = a.decode("utf-8")
print(b)
print(type(b))
c= a.decode("gbk")
print(c)
c=c.encode("gbk")
print(c.decode("utf-8"))

with open("utf3","w",encoding = "utf-8") as f:
    f.write(s)
with open("gbk3","w",encoding = "gbk") as f:
    f.write(s)
with open("jis3","w",encoding = "shift-jis") as f:
    f.write(s)