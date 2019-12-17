class intSet(object):
  def __init__(self):
    self.vals=[]
  def insert(self,e):
    if not e in self.vals:
      self.vals.append(e)
  def member(self,e):
    return e in self.vals
  def remove(self,e):
    try:
      self.vals.remove(e)
    except:
      raise ValueError(str(e)+' not found') 
  def __str__(self):
    self.vals.sort()
    result=''
    for e in self.vals:
      result=result+str(e)+' '
    return '{'+result[:-1]+'}'

s=intSet()
print(s)
s.insert("hello")
s.insert("姚晓昇")
s.insert("小明")
print(s)
s.remove("小明")
print(s)
print(s.member("小明"))
s.insert("5")
print(s)
s.insert("阿英")
print(s)
s.remove("5")
print(s)