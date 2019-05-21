## f(x) = exp(-x), find f''(x = 1)
## solution = 0.36787944117144233
## Consider h from 1 to 0.001 

import numpy as np

mapli = lambda f,x:list(map(f,x))
h = [1,10,50,100,500,1000]

h = mapli(lambda x:1/x,h)

for i in h:
    x = -1
    npr = 12
    f1 = (round(np.exp(x + i),npr) - round(np.exp(x - i),npr)) / (2*i)
    print('Derivatives, h ',f1, i)
