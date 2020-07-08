# SAW TOOTH GRAPH

import matplotlib.pyplot as plt 
import numpy as np 
from numpy import pi, sin, cos

T = 20
terms = 20
f = []


def an(n):
    global T
    if(n%2!=0):
        return -T**2/((2*n**2)*pi**4)
    else:
        return 0

def bn(n):
    global T
    if(n%2!=0):
        return (-4*T + T**2)/(4*n*pi**3)
    else:
        return 0

def wn(n):
    global T
    return 2*pi*n/T

def wave(x,terms):
    global T
    b = T**2/(8*pi**2)
    for i in range(1,terms):
        b = b + an(i)*sin(wn(i)*(2*x+1)) + bn(i)*cos(wn(i)*(2*x+1))
    return(b) 

t = np.linspace(-20,20,10000)
plt.title("Fourier Series of the function x/pi \n Time period = %s ; Armonic = %s"%(T,terms))
for i in t:
    f.append(wave(i,terms))
plt.plot(t,f,'b')
plt.show()