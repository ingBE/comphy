import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.5,1.9,2.1,2.4,2.6,3.1])
y = np.array([1.06,1.39,1.54,1.73,1.84,2.03])


# We wnt to find the height versus time

time = np.linspace(0,10,100)
y0  = 10        # Ten meters high
a   = -9.8      # Meters/sec^2

var = []
yar = []
for i in range(len(time)) :

    t = time[i]
    var.append( v0 + a*t )
    yar.append( y0 + v*t )

    if y < 0 : v = -v


