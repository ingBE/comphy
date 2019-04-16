import numpy as np

x = []

triger = -100
while (triger <= 100):
    x.append(triger/10.0)
    triger = triger + 1

result1, result2 = [], []
for i in x:
    result1.append(np.exp(-1*i**2))
    if (i == 0):
        result2.append('div 0')
    else:
        result2.append(np.sin(i)/i)

f = open('results.txt','w')

j = 0
for i in x:
    if (i == 0):
        f.write('{:5.1f}    {:10.4g}    '.format(i,result1[j]))
        f.write('  undifined\n')
    else:
        f.write('{:5.1f}    {:10.4g}    {:10.6f}\n'.format(i,result1[j],result2[j]))
    j = j+1

f.close()
