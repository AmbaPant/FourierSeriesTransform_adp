# import mantid algorithms, numpy and matplotlib
from mantid.simpleapi import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from math import pi

print("---->>>> start ----->>")
#generate signal
fs = 1000 #sample freq does not change freq position
t = np.arange(0,10,1/fs) #range of time scale does not change freq position 
#BUT interval (1/fs) effects the freq position
print("t interval:",t[2]-t[1])
f1 = 2.0; f2 = 1; f3 = 1.5

x = np.sin(2*pi*f1*t)+ 0.5*np.sin(2*pi*f2*t) + 1.5*np.sin(2*pi*f3*t)

plt.subplot(2,1,1); plt.plot(t,x);plt.title("time spectrum")
plt.xlabel("Time [$\mu$s]");plt.ylabel("Amplitude"); plt.axis([-0.02,10,-4,4])

# generate frequency axes
i4fscale = 2
n = np.size(t); print("n, t points:",n) # points  in time scale
fr = (fs/i4fscale)*np.linspace(0,1,n/i4fscale) #frequency scale of half of time scale
print(fr.size)
print("frq-interval:",fr[2]-fr[1])
#compute FFT
X = fft(x)
X_m = (2/n)*abs(X[0:np.size(fr)])  #2/n is used for normalization

plt.subplot(2,1,2)
#plt.plot(fr,X_m)
#plt.plot(fr,X_m,marker = 'o')
plt.stem(fr,X_m,use_line_collection=True,markerfmt='^r', linefmt='red')
#plt.plot(X) 
plt.title("FFT spectrum"); plt.xlabel("Frequency [MHz]")
plt.ylabel("FFT amplitude"); plt.axis([-0.02,4,0,2])
plt.tight_layout()
plt.grid()

plt.show()
