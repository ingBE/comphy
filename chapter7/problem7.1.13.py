import numpy as np
from run_kut4 import *

theta = np.pi/6
m  = 0.25    # kg
v0 = 50      # m/s
C  = 0.03    # kg/(m s)^0.5
g  = 9.80665 # m/s^2

## Function for using integrate function of run_kut4 
## x = [x, x', y, y']
def F(t,x):
    F = np.zeros(4)
    v    = (x[1]**2 + x[3]**2)**0.5
    F[0] = x[1]
    F[1] = -C/m*x[1]*(v**0.5)
    F[2] = x[3]
    F[3] = -C/m*x[3]*(v**0.5) - g
    return F

h = 0.001
x0 = [0,v0*np.cos(theta),0,v0*np.sin(theta)]
t, x = integrate(F,0,x0,10,h)

import matplotlib.pyplot as plt

xs = []; ys = []
for i in range(len(t)):
    xs.append(x[i,0]); ys.append(x[i,2])
    if x[i,2] < 0.: break
        


n = len(xs)-1
print(t[n], xs[n], ys[n])
plt.plot(xs,ys,'-')
plt.grid()
plt.show()
