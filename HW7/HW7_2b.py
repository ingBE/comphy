import numpy as np

time = np.linspace(0,10,100)
x = [-1.0]  # x0 = -1.0 meter
v = [ 0.0]  # v0 = 0 meter/sec
m = 0.5 # kg
k = 5   # N/m

# calculate to use leapfrog method
for i in range(len(time)-1):

    dt = time[i+1] - time[i]
    a  = - k/m * x[i]    # calculate the accelerate
    v_ = v[i] + a*dt/2   # calculate v[i+1/2]
    v.append( v_ + a*dt/2 ) # calculate the velocity
    x.append( x[i] + v[i+1]*dt )  # calculate the new position

import matplotlib.pyplot as plt
plt.plot(time,x,'-',time,v,'-')
plt.legend(['position','velocity'])
plt.grid()
#plt.savefig('HW7_2b')
plt.show()

