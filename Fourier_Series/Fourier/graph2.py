import matplotlib.pyplot as plt 
import numpy as np 

plt.ylim(-10,10)

def bn(n):
    if(n%2!=0):
        return 10/(np.pi*n)
    else:
        return 0 
T = 40

def wn(n):
    global T
    wn = 2*np.pi*n/T
    return wn

a0 = 5/2

def wave(x,n_max):
    global a0
    b = a0
    for i in range(1,terms):
        b = b + bn(i)*np.sin(wn(i)*(2*x+1))
    return b

t = np.linspace(-20*np.pi,20*np.pi,10000)
f = [] 

terms = 100

plt.title("Fourier Series \n Armonic Count : %s ; a0 = %s; Time Period = %s"%(terms,a0,T))
plt.grid()
plt.ylim(-6,12)


for i in t:
    f.append(wave(i,terms))
plt.plot(t,f,'b')
plt.show()
