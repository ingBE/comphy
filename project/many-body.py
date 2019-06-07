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
    n = len(x0)
    t = tStart
    x = x0
    #x1 = x0[0]
    #x2 = x0[1]
    ts = []
    ts.append(t)
    xs = []
    for i in range(n):
        xs.append([])
    #x1s = []
    #x2s = []
    for i in range(n):
        xs[i].append(x[i])
    #x1s.append(x1)
    #x2s.append(x2)
    while t < tStop:
        for i in range(n-1):
            if distance(x[i],x[i+1]) < d: # collision
                #print('a',t)
                temp = x[i][1]; x[i][1] = x[i+1][1]; x[i+1][1] = temp
        if n > 2:
            if distance(x[0],x[n-1]) < d:
                #print('b',t)
                temp = x[0][1]; x[0][1] = x[n-1][1]; x[n-1][1] = temp
        for i in range(n):
            x[i] = x[i] + dx(F,t,x[i],h)
        #x1 = x1 + dx(F,t,x1,h)
        #x2 = x2 + dx(F,t,x2,h)
        t = t + h
        ts.append(t)
        for i in range(n):
            xs[i].append(x[i])
        #x1s.append(x1)
        #x2s.append(x2)
    for i in range(n):
        xs[i] = np.array(xs[i])
    #x1s = np.array(x1s)
    #x2s = np.array(x2s)
    return np.array(ts),xs

d = 1.0e-02
h = 0.01

x0 = np.array([0,0,0,9.8])
x1 = np.array([0.0,1,0,9.8])
x2 = np.array([-1,2,9.8,0.0])
x3 = np.array([0.5,-1,9.8,0.0])
x0 = [x0,x1,x2,x3]
ts, xs = integrate(F,0.0,x0,2.0,h)

legend = []
for i in range(len(xs)):
    plt.plot(xs[i][:,0],xs[i][:,2],'-')
    legend.append('particle '+str(i))

plt.legend(legend)
plt.grid()
plt.show()
