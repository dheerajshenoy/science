import matplotlib.pyplot as plt 
import numpy as np 

T = 5
a0 = 0
f = [] 
terms = 10

def an(n):
    global T
    if(n%2!=0):
        return -4/(np.pi*n)
    else:
        return 0

def wn(n):
    global T
    wn = 2*np.pi*n/T
    return wn

def wave(x,terms):
    global a0
    b = a0
    for i in range(1,terms):
        b = b + an(i)*np.sin(wn(i)*(2*x+1))
    return b

t = np.linspace(-5,10*np.pi,10000)

for l in t:
    f.append(wave(l,terms))
plt.plot(t,f,'b')
plt.show()