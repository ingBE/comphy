## Definite the function will be used
mapli = lambda f,x:list(map(f,x))

def readData( dataName ):
    x = open( dataName, 'r')
    temp = []
    for ii in x.readlines():
        temp.append(ii)
    return mapli( float, temp )

## data[0] = xdata, data[1] = ydata1, data[2] = ydata2
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
from sineFit import sineFit, sineCoef, f

xsol = [0.63,10,10]
xsol = [0.627,2,3]
coef = sineCoef(data[0],data[1])(xsol)
x = np.linspace(min(data[0]),max(data[0]),1000)
y = mapli(sineFit(coef),x)

d = f(data[0],data[1])

print('partial diff ',d(coef))
print('coefficients ',coef)
print('stdDev ',stdDev(sineFit(coef),data[0],data[1]))

## Plot the data points
import matplotlib.pyplot as plt

plt.plot(data[0],data[1],'o',data[0],data[2],'o',x,y,'-')
plt.legend(['ydata1','ydata2','Fit'])
plt.grid()
plt.savefig('q1_plot')
