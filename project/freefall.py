import numpy as np
import matplotlib.pyplot as plt

## x 	= [ x, x', y, y']
def F(t,x):
	g = -9.8 # m/sec^2
	F = np.zeros(4)
	F[0] = x[1]
	F[1] = 0
	F[2] = x[3]
	F[3] = g
	return F

from run_kut4 import *

h = 0.01

ts, xs = integrate(F,0.0,np.array([0,0,0,9.8]),2.0,h)

plt.plot(ts,xs[:,2],'-')
plt.grid()
plt.show()
