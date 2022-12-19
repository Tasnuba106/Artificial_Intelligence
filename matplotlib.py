import matplotlib.pyplot as plt#for 
import numpy as np#array handle
#single graph
# x=np.array([1,2,6,2])
# y=np.array([3,5,7,8])
# plt.plot(x,y,marker='o',linestyle='dashdot',mec='r',mfc='r',ms=10,color='r',linewidth=4)#single graph
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.show()

#multiple graph
# x1=np.array([1,2,6,2])
# y1=np.array([3,5,7,8])
# x2=np.array([1,3,7,5])
# y2=np.array([3,9,7,8])
# font={'family':'serif','color':'darkred','size':22}
# plt.plot(x1,y1,label="first line")
# plt.plot(x2,y2,label="second line")
# plt.legend()
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.title('Sadmans CGPA',fontdict=font,loc='right')
# plt.grid(True,color='k',linestyle='--',linewidth=1)
# plt.show()




# # show 6 graph in one window
# x1=np.array([1,2,6,2])
# y1=np.array([3,5,7,8])
# x2=np.array([1,3,7,5])
# y2=np.array([3,9,7,8])
# x3=np.array([1,2,6,2])
# y3=np.array([3,5,7,8])
# x4=np.array([1,3,7,5])
# y4=np.array([3,9,7,8])
# x5=np.array([1,2,6,2])
# y5=np.array([3,5,7,8])
# x6=np.array([1,3,7,5])
# y6=np.array([3,9,7,8])
# plt.subplot(2,3,1)
# plt.plot(x1,y1)
# plt.title('X Graph')
# plt.subplot(2,3,2)
# plt.plot(x2,y2)
# plt.title('Y Graph')
# plt.subplot(2,3,3)
# plt.plot(x3,y3)
# plt.title('Z Graph')
# plt.subplot(2,3,4)
# plt.plot(x4,y4)
# plt.title('A Graph')
# plt.subplot(2,3,5)
# plt.plot(x5,y5)
# plt.title('B Graph')
# plt.subplot(2,3,6)
# plt.plot(x6,y6)
# plt.title('C Graph')
# plt.suptitle('Ajaira Graph')
# plt.show()



# x=[1,2,3,4,5]
# y=[10,20,30,40,50]
# labelx=['one','two','three','four','five']
# plt.bar(x,y,width=0.5,tick_label=labelx,color=['red','blue','green','gold','cyan'])
# plt.show()