from Person import Person

class MITPerson(Person):
  nextIdNum=0 
  def __init__(self,name):
    Person.__init__(self,name)
    self.idNum=MITPerson.nextIdNum
    MITPerson.nextIdNum+=1

  def getIdNum(self):
    return self.idNum<other.idNum
  
  def __lt__(self,other):
    return self.idNum<other.idNum
  def speak(self,utterance):
    return (self.getLastName()+" say:" +utterance)

# m3=MITPerson('Mark Zuckerberg')
# Person.setBirthday(m3,5,14,84)
# m2=MITPerson('Drew Houston')
# Person.setBirthday(m2,3,4,83)
# m1=MITPerson('Bill Gates')
# Person.setBirthday(m1,10,28,55)
# MITPersonList=[m1,m2,m3]
# print(m1.speak('hi there'))
# print(m2)
# print(m3)
# for e in MITPersonList:
#   print(e)
# MITPersonList.sort()
# Person.setBirthday(m3,5,14,84)
# m2=MITPerson('Drew Houston')
# Person.setBirthday(m2,3,4,83)
# m1=MITPerson('Bill Gates')
# Person.setBirthday(m1,10,28,55)
# print(m1)
# print(m3)
# print(m1.speak('hi there'))

# p1=MITPerson('Eric')
# p2=MITPerson('John')
# p3=MITPerson('John')
# p4=Person('John')
# print(p1<p2)
# print(p1<p4)
# print(p4<p1)