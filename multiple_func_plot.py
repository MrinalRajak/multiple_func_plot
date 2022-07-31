

#multiple function plot using matplotlib


import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,100)
y1=np.exp(-x)-np.exp(-2*x)
y2=2*np.exp(-x)-np.exp(-2*x)-np.exp(-3*x)
y3=np.exp(-x)-np.exp(-x**2)
y4=(x**2-x)*np.exp(-x**2)
fig,axar=plt.subplots(2,2)
axar[0,0].plot(x,y1,c='r')
axar[0,0].set_title(r'$e^{-x}-e^{-2x}$',fontsize=15)
axar[0,1].plot(x,y2,c='g')
axar[0,1].set_title(r'$e^{-x}-e^{-2x}-e^{-3x}$',fontsize=15)
axar[1,0].plot(x,y3,c='m')
axar[1,0].set_title(r'$e^{-x}-e^{-x^2}$',fontsize=15)
axar[1,1].plot(x,y4,c='chocolate')
axar[1,1].set_title(r'${(x^2-x)}e^{-x^2}$',fontsize=15)
fig.subplots_adjust(hspace=0.4,wspace=0.4)
plt.show()
