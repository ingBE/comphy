#!/usr/bin/python
## y'' - 3yy' = 0

import numpy as np
import matplotlib.pyplot as plt

from run_kut4 import *
from ridder import *
from printSoln import *

def initCond(u):  # Init. values of [y,y']; use 'u' if unknown
    return np.array([0.0, u])

def r(u):         # Boundary condition residual
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    y = Y[len(Y) - 1]
    r = y[0] - 1.0
    return r

def F(x,y):       # First-order differential equations
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -3.0*y[0]*y[1]
    return F

xStart = 0.0
xStop = 2.0
u1 = 1.0
u2 = 2.0
# Start of integration
# End of integration
# 1st trial value of unknown init. cond.
# 2nd trial value of unknown init. cond.
# Step size
# Printout frequency
h = 0.1
freq = 2
u = ridder(r,u1,u2) # Compute the correct initial condition
X,Y = integrate(F,xStart,initCond(u),xStop,h)
printSoln(X,Y,freq)

plt.plot(X,Y[:,0],'o-',X,Y[:,1],'-')
plt.xlabel('x')
plt.legend(('y','dy/dx'),loc = 1)
plt.grid(True)
plt.show()
