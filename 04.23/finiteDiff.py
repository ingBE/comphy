'''
Find the first and second derivatives at x = 0, 0.2, and 0.4 of the following dataset
x    = 0        0.1     0.2     0.3      0.4
f(x) = 0.0000   0.0819  0.1341  0.1646   0.1797
'''

x = [0,0.1,0.2,0.3,0.4]
f = [0.0,0.0819,0.1341,0.1646,0.1797]

# Finite difference in the abscissa h
h = x[1]-x[0]

nc = 2
# Forward difference calculation
f1f = (f[nc+1] - f[nc]) / h
f2f = (f[nc] - 2*f[nc+1] + f[nc+2]) / h**2

# Central difference calculation
f1c = (f[nc+1] - f[nc-1]) / (2*h)
f2c = (f[nc+1] - 2*f[nc] + f[nc-1]) / h**2

# Backward difference calculation
f1b = (-f[nc-1] + f[nc]) / h
f2b = (f[nc-2] - 2*f[nc-1] + f[nc]) / h**2

r = lambda x:round(x,8)

print("Forward vs Central vs Backward f1 at x = 0.2  ",r(f1f),r(f1c),r(f1b))
print("Forward vs Central vs Backward f2 at x = 0.2  ",r(f2f),r(f2c),r(f2b))

# Forward difference at x = 0
nc = 0
f1f = (f[nc+1] - f[nc]) / h
f2f = (f[nc] - 2*f[nc+1] + f[nc+2]) / h**2

print('')
print('Forward f1 and f2 at x = 0  ',r(f1f),r(f2f))
