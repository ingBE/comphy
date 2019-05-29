import numpy as np
import matplotlib.pyplot as plt

## y'' = 4(x - y)

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]     # y0' = y1
    F[1] = 4.0*(x-y[0]) # y1' = 4(x - y0)
    return F

def r(u):
    xs,ys = integrate(F,xStart,initCond(u),xStop,h)
    y = ys[len(ys) - 1]
    r = y[1] - 1.0
    return r

from run_kut4 import *
from ridder import *
from printSoln import *

xStart = 0
xStop = 2.0
h = 0.1
freq = 2

initCond = lambda u:np.array([0.0, u])

u1 = 1
u2 = 10
u = ridder(r,u1,u2)

xs,ys = integrate(F,xStart,initCond(u),xStop,h)
printSoln(xs,ys,freq)

plt.plot(xs,ys[:,0],'o-',xs,ys[:,1],'-')
plt.xlabel('x')
plt.legend(['y','dy/dx'],loc = 1)
plt.grid()
plt.show()
