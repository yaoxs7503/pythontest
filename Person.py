import datetime

class Person(object):
  def __init__(self,name):
    self.name=name
    self.birthday=None
    self.lastName=name.split(' ')[-1]
  
  def setBirthday(self,month,days,year):
    self.birthday=datetime.date(year,month,days)
  def getLastName(self):
    return self.lastName
  def __str__(self):
    return self.name
  def getAge(self):
    if self.birthday==None:
      raise ValueError
    return (datetime.date.today-self.birthday.days)
  def __lt__(self,other):
    if self.lastName==other.lastName:
      return self.name<other.name
    return self.lastName<other.lastName

# p1=Person('Mark Zuckerberg')
# p1.setBirthday(5,14,84)
# print(p1)
# p2=Person('Drew Houston')
# p2.setBirthday(3,4,83)
# print(p2)
# p3=Person('Bill Gates')
# print(p3)
# p4=Person('Andrew Gates')
# p5=Person('Steve Wozniak')

# personList=[p1,p2,p3,p4,p5]
# for e in personList:
#   print(e)
# personList.sort()
# for e in personList:
#   print(e)