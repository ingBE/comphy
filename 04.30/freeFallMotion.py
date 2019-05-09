import numpy as np
import matplotlib.pyplot as plt

# We wnt to find the height versus time

time = np.linspace(0,10,100)
y0  = 10        # Ten meters high
a   = -9.8      # Meters/sec^2
v0  = 0


var = [0.0]
yar = [10.0]
for i in range(len(time)-1) :

    dt = time[i+1] - time[i]
    var.append( var[i] + a*dt )
    yar.append( yar[i] + var[i]*dt )

    if yar[i+1] < 0 : var[i+1] = -var[i]

plt.plot(time,yar,'-',time,var,'-')
plt.legend(['position','velocity'])
plt.grid()
plt.savefig('freeFallMotion')
plt.show()
