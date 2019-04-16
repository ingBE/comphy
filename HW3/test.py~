import numpy as np
from HW3_2 import *

a, b = [], []

A = np.array([[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,0.,0.]])

# Make 10 random array b
for i in range(0,10):
    b.append(np.random.random(4))

for i in range(0,10):
    a_sample = np.random.random(16)

    for j in range(0,4):
        A[j,0:4] = a_sample[j*4:(j+1)*4]
    
    a.append(A)

num = 0
results = np.zeros(4)
for i in range(0,10):
    x = np.linalg.solve(a[i],b[i])
    solve = solve0(a[i],b[i])
    results += x - solve
    num =+ 1

print(results/num)
