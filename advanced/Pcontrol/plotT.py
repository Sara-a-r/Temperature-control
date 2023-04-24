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

def data_reduction(Troom,alpha):
    #evaluate moving average
    T_ema = EMA(Troom, alpha)
    t_ema = np.linspace(0, len(T_ema), len(T_ema))
    t_ema = t_ema[0: len(t_ema):4]
    T_ema = T_ema[0:len(T_ema):4]

    # create time array
    t = np.linspace(0, len(Troom), len(Troom))
    t = t[0: len(t):4]

    # take data every four seconds
    Troom = Troom[0:len(Troom):4]
    return Troom, T_ema, t, t_ema


#set parameters
Tref = 24
window = 10     #window size for sma
alpha = 0.1     #alpha value for ema
kp = [20, 80, 180, 200, 500]        #proportional gain

#load data
Troom1, _, _ = pyl.loadtxt(f'data/Pcontrol{Tref}_kp{kp[0]}.txt', unpack=True)
Troom2, _, _ = pyl.loadtxt(f'data/Pcontrol{Tref}_kp{kp[1]}.txt', unpack=True)
Troom3, _, _ = pyl.loadtxt(f'data/Pcontrol{Tref}_kp{kp[2]}.txt', unpack=True)
Troom4, _, _ = pyl.loadtxt(f'data/Pcontrol{Tref}_kp{kp[3]}.txt', unpack=True)
Troom5, _, _ = pyl.loadtxt(f'data/Pcontrol{Tref}_kp{kp[4]}.txt', unpack=True)


Troom1, T_ema1, t1, t_ema1 = data_reduction(Troom1, alpha)
Troom2, T_ema2, t2, t_ema2 = data_reduction(Troom2, alpha)
Troom3, T_ema3, t3, t_ema3 = data_reduction(Troom3, alpha)
Troom4, T_ema4, t4, t_ema4 = data_reduction(Troom4, alpha)
Troom5, T_ema5, t5, t_ema5 = data_reduction(Troom5, alpha)


# let's see data: scatter plot
plt.rc('font',size=10)
plt.figure(figsize=(12,6))
plt.title("Proportional control varing $k_p$")
plt.xlabel("time [s]")
plt.ylabel("T[$^{\circ}$C]")
plt.ylim(22, 26)
plt.grid(visible=True, color='grey', linestyle='-', alpha=0.3)
plt.minorticks_on()

t_ema = [t_ema1, t_ema2, t_ema3, t_ema4, t_ema5]
T_ema = [T_ema1, T_ema2, T_ema3, T_ema4, T_ema5]

plt.axhline(y=Tref, linestyle=':', color='red', label= 'T$_{ref}$=%.2d$^{\circ}$C' % Tref)
i = 0
for i in range(len(t_ema)):
    plt.plot(t_ema[i], T_ema[i], linestyle='-', linewidth=1.5, marker='', label=r'EMA $\alpha$ = %.1f, $k_p$ = %d' % (alpha, kp[i]))
    plt.legend(loc='lower right', fancybox=True)
    i = i + 1


#save the plot
plt.savefig(f"figure/Pcontrol_kp.png")
plt.show()
