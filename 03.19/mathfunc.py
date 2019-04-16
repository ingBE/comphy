def fac(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac

def expfunc(x,n):
    exp = 0
    for i in range(0,n+1):
        exp = exp + x**i/fac(i)
    return exp

def exp(x):
    return expfunc(x,20)

def sinfunc(x,n):
    if x==0:
        return 0
    sin = 0
    for i in range(1,n+1):
        sin = sin - ( ((-1)**i) * (x)**(2*i-1) )/fac(2*i-1)
    return sin

def sin(x):
    return sinfunc(x,20)

def cosfunc(x,n):
    if x==0:
        return 1
    cos = 0
    for i in range(1,n+1):
        cos = cos + x**(2*i)/fac(2*i)
    return cos

def cos(x):
    return cosfunc(x,20)

print(sin(0.01))
