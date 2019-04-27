## q2.py
## A*x = B
##
## x1 * k' - (x2 - x1) * k' - W = 0
## x2 * (k + k) + (x2 - x1) * k' - (x3 - x2) * k - W' = 0
## (x3 - x2) * k - (x5 - x3) * (k + k) - (x4 - x3) * k' - W' = 0
## (x4 - x3) * k' - (x5 - x4) * k' - W = 0
## (x5 - x3) * (k + k) + (x5 - x4) * k' - W = 0

import numpy as np

## p is prime
W  = 2 #kg
Wp = 1.5 #kg
k  = 0.3 #N/m
kp = 1 #N/m

A = np.array([[2*kp,   -kp,     0,   0,     0],
              [ -kp,3*k+kp,     k,   0,     0],
              [   0,    -k,3*k+kp, -kp,  -2*k],
              [   0,     0,   -kp,2*kp,   -kp],
              [   0,     0,  -2*k, -kp,2*k+kp]])
B = np.array([W,Wp,Wp,W,Wp])

## solve function from module linearSolve made myself
from linearSolve import solve 

x = solve(A,B)
print('[ x1, x2, x3, x4, x5 ] ',x)
