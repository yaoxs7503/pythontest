class fraction(object):
  def __init__(self,number,denom):
    self.number=number
    self.denom=denom
  def __str__(self):
    return str(self.number)+' / '+str(self.denom)
  def getNumber(self):
    return self.number
  def getDenom(self):
    return self.denom
  def __add__(self,other):
    numerNew=other.getDenom()*self.getNumber()+other.getNumber()*self.getDenom()
    denomNew=other.getDenom()*self.getDenom()
    return fraction(numberNew,denomNew)
  def __sub__(self,other):
    numerNew=other.getDenom()*self.getNumber() - other.getNumber()*self.getDenom()
    return fraction(numerNew,denomNew)
  def convert(self):
    return self.getNumber() / self.getDenom()
