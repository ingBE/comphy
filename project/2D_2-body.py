import numpy as np
import matplotlib.pyplot as plt

## x = [ x, x', y, y']
distance = lambda x1,x2:((x1[0]-x2[0])**2 + (x1[2]-x2[2])**2)**0.5

## x 	= [ x, x', y, y']
def F(t,x):
	g = -9.8 # m/sec^2
	F = np.zeros(4)
	F[0] = x[1]
	F[1] = 0
	F[2] = x[3]
	F[3] = g
	return F

#from run_kut4 import *

# 2-body problem
def integrate(F,tStart,x0,tStop,h):
    def dx(F,t,x,h):
        k0 = h*F(t,x)
        k1 = h*F(t+h/2.0,x+k0/2.0)
        k2 = h*F(t+h/2.0,x+k1/2.0)
        k3 = h*F(t+h,x+k2)
        return (k0 + 2.0*k1 + 2.0*k2 + k3)/6.0
    t = tStart
    x1 = x0[0]
    x2 = x0[1]
    ts = []
    x1s = []
    x2s = []
    ts.append(t)
    x1s.append(x1)
    x2s.append(x2)
    while t < tStop:
        if distance(x1,x2) < d: # collision
            temp = x1[1]; x1[1] = x2[1]; x2[1] = temp
        x1 = x1 + dx(F,t,x1,h)
        x2 = x2 + dx(F,t,x2,h)
        t = t + h
        ts.append(t)
        x1s.append(x1)
        x2s.append(x2)
    x1s = np.array(x1s)
    x2s = np.array(x2s)
    xs = [x1s,x2s]
    return np.array(ts),xs

d = 1.0e-02
h = 0.01

x0 = np.array([[0.5,1,0,9.8],[1,-1,0,9.8]])
ts, xs = integrate(F,0.0,x0,2.0,h)


plt.plot(xs[0][:,0],xs[0][:,2],'-',xs[1][:,0],xs[1][:,2],'-')
plt.legend(['particle 1','particle 2'])
plt.grid()
plt.show()
