'''
HW6_2.py

(x-a)^2 + (y-b)^2 = R^2

xData = [8.21, 0.34, 5.96]
yData = [0.00, 6.62, -1.12]

Determine R, a and b numerically.
'''

import numpy as np
import matplotlib.pyplot as plt

## f = (x-a)^2 + (y-b)^2 - R^2 = 0

xData = [8.21, 0.34, 5.96]
yData = [0.00, 6.62, -1.12]

plt.plot(xData,yData,'o')
plt.show()
