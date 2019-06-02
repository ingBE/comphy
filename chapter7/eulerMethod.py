import numpy as np

##  y'' = -0.1*y' - x,   y(0) = 0,   y'(0) = 1

##  Define the first orde equations. For ordef 2 we have two variables.
##  yvec = [y0 , y1 ],  where y0 = y,  y1 = y'
##  yvec'= [y0', y1'] = F(x, yvec)

##  Let's solve in a pedestrian manner starting from x = 0
##  Let's set h = 0.2

##  Solve for y0(0)
x = []; y0 = []; y1 = []
x.append(0);      y0.append(0);      y1.append(1)

y1p = lambda x,y0,y1:-0.1*y1 - x

h = 0.2

##  Let's evaluate at 0 + h
x.append(h)
y0.append( y0[0] + y1[0]*h )
y1.append( y1[0] + y1p(x[0],y0[0],y1[0])*h )

##  Let's caculate at 0 + 2h
x.append(2*h)
y0.append( y0[1] + y1[1]*h )
y1.append( y1[1] + y1p(x[1],y0[1],y1[1])*h )

print('  x      y0     y1')
print(np.transpose([x,y0,y1]))
print('\n-----------------------\n')
##
from euler import *
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

# Call the integration routine    
X,Y = integrate(F,x,y,xStop,h)
yExact = 100.0*X - 5.0*X**2 + 990.0*(np.exp(-0.1*X) - 1.0)

from printSoln import *
freq = 2
printSoln(X,Y,freq)

# Plotting tool
plt.plot(X,Y[:,0],'o',X,yExact,'-')
plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()
