import numpy as np
import matplotlib.pyplot as plt

## y''' = 2y'' + 6xy
## y0(0) = 2, y0(5) = y1(5) = 0
def F(x,y):
    F = np.zeros(3)
    F[0] = y[1]     # y0' = y1
    F[1] = y[2]     # y1' = y2
    F[2] = 2.0*y[2] + 6.0*x*y[0]
    return F

def r(u):
    xs,ys = integrate(F,xStart,initCond(u),xStop,h)
    y = ys[len(ys) - 1]
    r = y[0] - 2.0
    return r

from run_kut5 import *
from ridder import *
from printSoln import *

xStart = 5.0
xStop  = 0.0
h      = -0.1
freq   = 2

## initial condition y0(0) = 0, y1(0) = u
initCond = lambda u:np.array([0.0, 0.0, u])

u1 = 1.0
u2 = 2.0
u = ridder(r,u1,u2)
print(u)

xs,ys = integrate(F,xStart,initCond(u),xStop,h)
printSoln(xs,ys,freq)

plt.plot(xs,ys[:,0],'o-',xs,ys[:,1],'-')
plt.xlabel('x')
plt.legend(['y','dy/dx'],loc = 1)
plt.grid()
plt.show()
