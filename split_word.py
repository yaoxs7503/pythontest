import os,codecs
import jieba
from collections import Counter

def get_words(txt):
  seg_list=jieba.cut(txt)
  c=Counter()
  for x in seg_list:
    if len(x) > 1 and x!='\r\n':
      # print(c)
      c[x]+=1
  # print(c.items())

  print('常用词频统计结果')
  # for (k,v) in c.most_common(100):
    # print('%s %s %s %d'%(''*(5-len(k)),k,'*'*int(v/3),v))
  name="面对"
  count=0
  if(name in c.keys()):
    count+=1
    print('数量为{}'.format(count))
  else:
    print('没有这个key')
  
if __name__=='__main__':
  with codecs.open('test.txt','r','utf8') as f:
    txt=f.read()
  get_words(txt)
