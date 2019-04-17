## Projectile motion:
##
## Constraints: x = 300m, y = 61m, vx = - vy at (xsol,ysol)
## Find the initial velocity v, time elapsed t, initial angle theta
##
## x = v*cos(theta)*t
## y = v*sin(theta)*t - 1/2*g*t*t
## v_y/v_x = -1

import numpy as np
import math
from newtonRaphson2 import *

g = 9.8 # m/sec^2

def f(xsol):
    t = xsol[0]; theta = xsol[1]; v = xsol[2]
    f = np.zeros(3)

    f[0] = v*np.cos(theta)*t - 300    # x axis eq
    f[1] = v*np.sin(theta)*t - 1/2*g*t*t - 61 #y axis eq
    vx = v*np.cos(theta)
    vy = v*np.sin(theta) - g*t
    f[2] = vy/vx + 1

    return f


#def newtonRaphson():


x = np.array([9,np.pi/4,40])
print(x)
