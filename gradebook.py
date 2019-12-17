class Grades(object):
  def __init__(self):
    self.students=[]
    self.grades={}
    self.isSorted=True

  def addStudent(self,student):
    if student in self.students:
      raise ValueError('重复的学习')
    self.students.append(student)
    self.grades[student.getIdNum()]=[]
    self.isSorted=False

  def addGrade(self,student,grade):
    try:
      self.grades[student.getIdNum()].append(grade)
    except KeyError:
      raise ValueError('没有学生在这个班')
  
  def getGrades(self,student):
    try:
      return self.grades[student.getIdNum()][:]
    except KeyError:
      raise ValueError