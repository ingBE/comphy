## q3.py
##
## M1, y:  T1*sin(theta1) - T2*sin(theta2) - M1*g = 0
## M1, x: -T1*cos(theta1) + T2*cos(theta2)        = 0
## M2, y:  T2*sin(theta2) + T3*sin(theta3) - M2*g = 0
## M2, x: -T2*cos(theta2) + T3*cos(theta3)        = 0
##      :  L1*cos(theta1) + L2*cos(theta2) + L3*cos(theta3) - L = 0
##      :  L1*sin(theta1) + L2*sin(theta2) - L3*sin(theta3)     = 0
##
## Let sin(theta) = sin, cos(theta) = cos
##      :  sin1^2 + cos1^2 - 1= 0
##      :  sin2^2 + cos2^2 - 1= 0
##      :  sin3^2 + cos3^2 - 1= 0

import numpy as np
## Use module newtonRaphson2 from comphy2019 github
from newtonRaphson2 import newtonRaphson2

## Definite usual function
mapli = lambda f,x:list(map(f,x))
r = lambda x:mapli(lambda x:round(x,6),x)

## xsol = [ T1, T2, T3, sin1, sin2, sin3, cos1, cos2, cos3 ]
## unpack :: xsol -> (T, sin, cos)
unpack = lambda xsol:(xsol[0:3],xsol[3:6],xsol[6:9])
## f is function for using function newtonRaphson2
## f :: (M, L) -> (xsol -> system of equations)
## M = [ M1, M2 ], L = [ L1, L2, L3, L ]
def f(M,L):
    def aa(xsol):
        g = 9.8 # m/s^2
        T, sin, cos = unpack(xsol)

        aa = np.zeros(9)
        aa[0] =  T[0]*sin[0] - T[1]*sin[1] - M[0]*g
        aa[1] = -T[0]*cos[0] + T[1]*cos[1]
        aa[2] =  T[1]*sin[1] + T[2]*sin[2] - M[1]*g
        aa[3] = -T[1]*cos[1] + T[2]*cos[2]
        aa[4] =  L[0]*cos[0] + L[1]*cos[1] + L[2]*cos[2] - L[3]
        aa[5] =  L[0]*sin[0] + L[1]*sin[1] - L[2]*sin[2]
        aa[6] =  sin[0]*sin[0] + cos[0]*cos[0] - 1
        aa[7] =  sin[1]*sin[1] + cos[1]*cos[1] - 1
        aa[8] =  sin[2]*sin[2] + cos[2]*cos[2] - 1

        return aa
    return aa

L = [0.5, 1.5, 2.5, 3.0]
## (a) M1 = 1 kg, M2 = 5 kg
x = np.ones(9)
solve = newtonRaphson2(f([1, 5],L),x)
T, sin, cos = unpack(solve)

thetaSin = mapli(lambda x:np.arcsin(x),sin)
thetaCos = mapli(lambda x:np.arccos(x),cos)

print('(a) M1 = 1 kg, M2 = 5 kg')
print('[ T1, T2, T3 ] ',r(T))
print('\ntheta caculated from sin values')
print('[ theta1, theta2, theta3 ] ',r(thetaSin))
print('\ntheta caculated from cos values')
print('[ theta1, theta2, theta3 ] ',r(thetaCos))

## (b) M1 = 1 kg, M2 = 0 kg
x = np.ones(9)
solve = newtonRaphson2(f([1, 0],L),x)
T, sin, cos = unpack(solve)

thetaSin = mapli(lambda x:np.arcsin(x),r(sin))
thetaCos = mapli(lambda x:np.arccos(x),r(cos))

print('')
print('(b) M1 = 1 kg, M2 = 0 kg')
print('[ T1, T2, T3 ] ',r(T))
print('\ntheta caculated from sin values')
print('[ theta1, theta2, theta3 ] ',r(thetaSin))
print('\ntheta caculated from cos values')
print('[ theta1, theta2, theta3 ] ',r(thetaCos))
