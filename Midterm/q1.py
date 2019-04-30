## Definite the function will be used
mapli = lambda f,x:list(map(f,x))

def readData( dataName ):
    x = open( dataName, 'r')
    temp = []
    for ii in x.readlines():
        temp.append(ii)
    return mapli( float, temp )

## data[0] = xdata, data[1] = ydata1, data[2] = ydata2
## ydata1 is the same as ydata2
dataName = ['xdata.dat','ydata1.dat','ydata2.dat']
data = mapli( readData, dataName )

## Calculate standard deciation of ydata1, ydata2
def stdDev(f,xData,yData):
    n = len(xData)
    S = 0
    for i in range(n):
        S += (yData[i] - f(xData[i]))**2
    sigma = (S/(n-3))**0.5
    return sigma

import numpy as np
## Fitting Straight Line using Least-Squares method
from polyFit import polyFit

def f(coef):
    def g(x):
        p = 0
        for i in range(len(coef)):
            p += coef[i]*(x**i)
        return p
    return g

coef = polyFit(data[0],data[1],3)
x    = np.linspace(min(data[0]),max(data[0]),1000)
poly = mapli(f(coef),x)

print('--- Polynomial Fitting ---')
print('coefficients ',coef)
print('stdDev ',stdDev(f(coef),data[0],data[1]))
print('')

## Fitting Sine graph using Least-Squares method
from sineFit import sineFit, sineCoef, f

xsol = [0.627,2,3]
sinCoef = sineCoef(data[0],data[1])(xsol)
x = np.linspace(min(data[0]),max(data[0]),1000)
sin = mapli(sineFit(sinCoef),x)

print('--- Sine Fitting ---')
print('a, b, omega ',sinCoef)
print('stdDev ',stdDev(sineFit(sinCoef),data[0],data[1]))

## Plot the data points
import matplotlib.pyplot as plt

plt.plot(data[0],data[1],'-',x,poly,'-',x,sin,'-')
plt.legend(['ydata','Poly Fit','Sine Fit'])
plt.grid()
plt.savefig('q1_plot')
