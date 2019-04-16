def fac(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac

def exponential(x,n):
    exp = 0
    for i in range(0,n+1):
        exp = exp + x**i/fac(i)
    return exp

def exp(x):
    return exponential(x,100)

aa = []

f = open('nexp.txt','w')

for i in range(1,11):
    f.write('{:2d} {:7.10f}\n'.format(i,exp(i)))
    aa.append('{:2d} {:7.10f}\n'.format(i,exp(i)))

f.close()
print(aa)
