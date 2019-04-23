'''
HW6_2.py

(x-a)^2 + (y-b)^2 = R^2

xData = [8.21, 0.34, 5.96]
yData = [0.00, 6.62, -1.12]

Determine R, a and b numerically.
'''

import numpy as np

## f = (x-a)^2 + (y-b)^2 - R^2 = 0

xData = [8.21, 0.34, 5.96]
yData = [0.00, 6.62, -1.12]

## Use newtonRaphson2 module from comphy2019 github
from newtonRaphson2 import newtonRaphson2
## Make function f for using newtonRaphson2 function
## f return function g
## f :: (xData,yData,xsol) -> (xsol -> list)
def f(xData,yData):
    def g(xsol):
        R = xsol[0]; a = xsol[1]; b = xsol[2]
        g = np.zeros(3)
        
        for i in range(3):
            g[i] = (xData[i]-a)**2 + (yData[i]-b)**2 - R**2

        return g
    return g

x = [5,4,3]
root = newtonRaphson2(f(xData,yData),x)

print(root)

## Test R, a, b
print('')
for i in range(3):
    print(((xData[i]-root[1])**2 + (yData[i]-root[2])**2)**0.5)
