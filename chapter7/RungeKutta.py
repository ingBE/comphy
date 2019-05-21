import numpy
from run_kut4 import *
from printSoln import *
import matplotlib.pyplot as plt

##  y' = -4y + x^2,  y(0) = 1
def F(x,y):
    F = np.zeros(1)
    F[0] = -4.0*y[0] + x**2
    return F

x = 0.0
xStop = 2.0
y = np.array([1.0])
h = 0.05

# Call the integration routine
X,Y = integrate(F,x,y,xStop,h)

# Plotting tool
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
plt.subplot(2,1,1)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)

# Print solutions with given frequency freq
freq = 5
printSoln(X,Y,freq)



##  y' = 3*y - 4*exp(-x), y(0) = 1
def F(x,y):
    F = np.zeros(1)
    F[0] = -3.0*y[0] - 4.0*np.exp(-x)
    return F

x = 0.0
xStop = 2.0
y = np.array([1.0])
h = 0.05

#
X,Y = integrate(F,x,y,xStop,h)

#
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)
plt.subplot(2,1,2)
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)

freq = 5
printSoln(X,Y,freq)

plt.show()
