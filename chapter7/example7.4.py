#!/usr/bin/python
## example7_4
import numpy as np
from printSoln import *
from run_kut4 import *
import matplotlib.pyplot as plt
def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1*y[1] - x
    return F

x = 0.0
xStop = 2.0
y = np.array([0.0, 1.0])
h = 0.2
# Start of integration
# End of integration
# Initial values of {y}
# Step size

X,Y = integrate(F,x,y,xStop,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()
