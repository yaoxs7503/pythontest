data=[]

file_name=input("Provide a name of a file of data")

try:
  fh=open(file_name,'r',encoding="utf-8")
except IOError:
  print('cannot open',file_name)
else:
  for new in fh:
    if new !='\n':
      addIt=new[:-1].split(',')
      data.append(addIt)
finally:
    fh.close()

print(data)