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

## x0(0) = 0.0, x1(0) = v*cos(theta), x2(0) = 0.0, x3(0) = v*sin(theta)
## x0(10) = 8000, x1(10) = ?, x2(10) = 0, x3(10) = ?

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
    ts,xs = integrate(F,tStart,initCond(u),tStop,h)
    y = xs[len(ts) - 1]
    r[0] = y[0] - 8000  ## x(10) = 8000
    r[1] = y[2] - 0.0   ## y(10) = 0
    return r

initCond = lambda u: np.array([0.0,u[0],0.0,u[1]])

from run_kut4 import *
## Use newtonRaphson2 module for finding v0, theta
from newtonRaphson2 import *

tStart  = 0.0
tStop   = 10.0
h       = 0.001

## Initial value for newtonRaphson2
v0 = 50
theta = np.pi/6
u     = [v0*np.cos(theta), v0*np.sin(theta)]

## Consider initial value
u     = newtonRaphson2(r,u)

ts,xs = integrate(F,tStart,initCond(u),tStop,h)

#from printSoln import *
#printSoln(ts,xs,freq)

## Write new txt file for save solution
f = open('problem8.1.19.txt','w')
f.write('u             '+str(u))
f.write('\nv0            '+str((u[0]**2 + u[1]**2)**0.5))
f.write('\ntheta         '+str(np.arctan(u[1]/u[0])))
f.write('\nx(10)         '+str(xs[len(ts)-1,0]))
f.write('\nr(u)          '+str(r(u)))
f.close()

plt.plot(xs[:,0],xs[:,2],'-')
plt.grid()
plt.savefig('problem8.1.19.png')
