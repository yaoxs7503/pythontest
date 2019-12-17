label_path='test.txt'
file=open(label_path,'r',encoding='utf-8')
print(type(file))
label=[x.strip() for x in file]
print(type(label))
print(label)
file.close()