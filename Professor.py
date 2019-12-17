from MITPerson import MITPerson
class Professor(MITPerson):
  def __init__(self,name,department):
    MITPerson.__init__(self,name)
    self.department=department
  
  def speak(self,utterance):
    new='In course'+self.department+' we say'
    return MITPerson.speak(self," Yo Bro,"+utterance)
  
  def lecture(self,topic):
    return self.speak('it is obvious that'+topic)
