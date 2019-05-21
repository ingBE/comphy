import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

mapli = lambda f,x:list(map(f,x))

def readData( dataName ):
    x = open( dataName, 'r')
    temp = []
    for ii in x.readlines():
        temp.append(ii)
    return mapli( float, temp )

xdata = readData('Kgrid_x.dat')
ydata = readData('Kgrid_y.dat')
zdata = readData('Curv_z.dat')

print(xdata)
plt.plot(xdata,ydata,'-')
colors = (0,0,1)
plt.axes().set_aspect(aspect='equal')
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter3D(xdata,ydata,zdata,cmat='viridis')
ax.view_init(30,30)
plt.show()
