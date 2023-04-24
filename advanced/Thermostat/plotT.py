import numpy as np
import pylab as pyl
import matplotlib.pyplot as plt
import pandas as pd

# function to calculate the simple moving average
def SMA(data, window_size):
    # convert array to pandas series
    data_series = pd.Series(data)
    # create a series of moving averages of each window and remove null entries
    data_mean = data_series.rolling(window_size).mean()[window_size - 1:]
    # convert pandas series into numpy array
    data_sma = data_mean.to_numpy()
    return data_sma

# function to calculate the exponential moving average
def EMA(data, alpha):
    # Convert array of integers to pandas series
    data_series = pd.Series(data)
    # Get the moving averages of series of observations till the current time
    data_averages = round(data_series.ewm(alpha=alpha, adjust=False).mean(), 2)
    # convert pandas series into numpy array
    data_ema = data_averages.to_numpy()
    return data_ema


#set parameters
Tref = 25
window = 10
alpha = 0.2

#load data
Hstate, Troom = pyl.loadtxt(f'3 watt ca/data_1V1_{Tref}.txt', unpack=True)

Hstate = Hstate * 20
T_sma = SMA(Troom, window)
T_ema = EMA(Troom, alpha)


# let's see data: scatter plot
plt.rc('font',size=10)
plt.figure(figsize=(12,6))
#plt.title("Time rise using T$_{ref}$=%.2d$^{\circ}$C" % Tref)
plt.title("Moving average using Vcc=1.1V")
plt.xlabel("time [s]")
plt.ylabel("T[$^{\circ}$C]")
plt.ylim(22, 26)
plt.grid(visible=True, color='grey', linestyle='-', alpha=0.3)
plt.minorticks_on()


plt.axhline(y=Tref, linestyle=':', color='red', label= 'T$_{ref}$=%.2d$^{\circ}$C' % Tref)
plt.plot(T_sma, linestyle='-', color = 'green', linewidth=1, marker='', label='SMA w = 10')
plt.plot(T_ema, linestyle='-', color = 'blue', linewidth=1, marker='', label=r'EMA $\alpha$ = %.1f'% alpha)
plt.plot(Troom, linestyle='-', color = 'black', linewidth=1, marker='', label='data')
#plt.plot(Hstate, linestyle='-', linewidth=0.9, marker='', color='blue', label='Heater state')
plt.legend(loc='lower right')

#save the plot
plt.savefig(f"3 watt ca/figure/EMA_{alpha}.png")
plt.show()
