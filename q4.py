from matplotlib import pyplot as plt
import numpy as np
x1=np.array([0,1,2,3])
y1=np.array([3,8,2,10])

x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])

x3=np.array([1,2,3])
x4=np.array([1,2,3])
y3=np.array([4,1,3])
y4=np.array([2,4,0])
plt.subplot(1,3,1)
plt.plot(x1,y1)
plt.title('First Graph')
plt.subplot(1,3,2)
plt.plot(x2,y2)
plt.title('Second Graph')
plt.subplot(1,3,3)
plt.plot(x3,y3,x4,y4)
plt.title('Third Graph')
plt.show()
