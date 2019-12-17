import pylab as plt
mySamples=[]
myLinear=[]
myQuadratic=[]
myCubic=[]
myExponential=[]

for i in range(0,30):
  mySamples.append(i)
  myLinear.append(i)
  myQuadratic.append(i**2)
  myCubic.append(i**3)
  myExponential.append(1.5**i)

plt.figure('一阶函数')
plt.clf()
plt.ylim(0,1000)
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples,myLinear,label='linear')
plt.plot(mySamples,myQuadratic,label='quadratic')
plt.legend(loc='upper left')
# plt.figure('立方根')
# plt.plot(mySamples,myCubic)
# plt.figure('指数函数')
# plt.plot(mySamples,myExponential)
plt.show()
