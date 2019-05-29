import numpy as np
import matplotlib.pyplot as plt

m = 20 # kg
c = 3.2e-4 # kg/m
g = 9.80665 # m/s^2

## x'' = -(c/m)*v*x'
## --- Rewrite the equations ---
## y0' = y1
## y1' = -(c/m)*v*y1

## y'' = -(c/m)*v*y - g
## --- Rewrite the equations ---
## y2' = y3
## y3' = -(c/m)*v*y3 - g

## y0(0) = 0.0, y1(0) = v*cos(theta), y2(0) = 0.0, y3(0) = v*sin(theta)
## y0(10) = 8000, y1(10) = ?, y2(10) = ?, y3(10) = ?

def F(t,x):
    F = np.zeros(4)
    v = ( x[1]**2 + x[3]**2 )**0.5
    F[0] = x[1]
    F[1] = -(c/m)*v*x[1]
    F[2] = x[3]
    F[3] = -(c/m)*v*x[3] - g
    return F

def r(u):
    r = np.zeros(len(u))
    xs,ys = integrate(F,xStart,initCond(u),xStop,h)
    y = ys[len(ys) - 1]
    r[0] = y[0] - 8000
    r[1] = y[1] - 0.0
    return r

initCond = lambda u: np.array([0.0,u[0],0.0,u[1]])

from run_kut5 import *
from ridder import *
from printSoln import *

tStart  = 0.0
tStop   = 100
h       = 0.001
freq    = 2

v     = 300
theta = np.pi/6
u     = [v*np.cos(theta), v*np.sin(theta)]

ts,xs = integrate(F,tStart,initCond(u),tStop,h)
printSoln(ts,xs,freq)

plt.plot(xs[:,0],xs[:,2],'o-')
plt.xlim(0,8000)
plt.ylim(0,1000)
plt.grid()
plt.show()
