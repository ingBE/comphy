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

root = [0.9825055,  -0.08180717, -0.40328052]
x = np.linspace(min(data[0]),max(data[0]),1000)
y = root[1]*np.sin(root[0]*x)+root[2]*np.cos(root[0]*x)

## Plot the data points
import matplotlib.pyplot as plt

plt.plot(data[0],data[1],'--',data[0],data[2],'--',x,y,'-')
plt.legend(['ydata1','ydata2','Fit'])
plt.grid()
plt.show()
