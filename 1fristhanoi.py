def printMove(fr,to):
  print(' 从 '+str(fr)+' 到 '+str(to))


def Towers(n,fr,to ,spare):
  if n==1:
    printMove(fr,to)
  else:
    Towers(n-1,fr,spare,to)
    Towers(1,fr,to,spare)
    Towers(n-1,spare,to,fr)

Towers(4,"起点柱子","终点柱子","中间的柱子")