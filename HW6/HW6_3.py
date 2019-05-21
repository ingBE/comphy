'''
find a suitable interpolating function and calculate numerically
the nonzero root of y(x) = 0. 
'''

import numpy as np
import matplotlib.pyplot as plt

xData = np.array([0,0.25,0.50,0.75,1.0,1.25,1.5])
yData = np.array([0,-1.2233,-2.2685,-2.8420,-2.2130,2.5478,55.507])

## Make map function for replacing for roop to map function
mapli = lambda f,ar:list(map(f,ar))

## Use module newtonRaphson made by me
from newtonRaphson import newtonRaphson

## Use module neville from comphy2019 github
from neville import *

## Make function f for using neville function
## f :: (xData, yData) -> (x -> y)
## f(xData,yData) = neville(xData,yData,x)
f = lambda xData,yData:lambda x:neville(xData,yData,x)
## g :: (x -> y)
g = f(xData,yData)

root = newtonRaphson(g,1.1,dx=0.05)
print(root,g(root))

x = np.linspace(min(xData),max(xData))
plt.plot(xData,yData,'o',root,g(root),'o',x,mapli(lambda x:g(x),x),'-')
plt.legend(['Input data','Root point','Fitting graph'])
plt.grid()
plt.savefig("HW6_3_1")

plt.xlim(root-0.05,root+0.05)
plt.ylim(-5,5)
plt.savefig("HW6_3_2")
