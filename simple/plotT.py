import numpy as np
import pylab as pyl
import matplotlib.pyplot as plt

# load data
Tcontrol, Tref, Troom = pyl.loadtxt('data_T1.txt',unpack=True)

# let's see data: scatter plot
plt.rc('font',size=10)
plt.figure(figsize=(12,6))
plt.title("Temperature control with Arduino")
plt.xlabel("time [s]")
plt.ylabel("T[$^{\circ}$C]")
plt.ylim(0,50)
plt.grid(color='gray',linewidth='0.2')
plt.minorticks_on()

plt.plot(Tcontrol, linestyle = '-', color = 'black', label =  'T control')
plt.plot(Tref, linestyle = ':', color = 'red', label = 'T ref')
plt.plot(Troom,linestyle = '-', color = 'blue', label = 'T room')
plt.legend(loc = 'lower right')

#save the plot
plt.savefig("TcontrolArduino1.png")
plt.show()