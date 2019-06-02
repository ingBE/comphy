from numpy import abs, sign

def rootsearch(f,a=-100,b=100,dx=0.1):
    dx = abs(dx)
    x1 = a; f1 = f(x1)
    x2 = b; f2 = f(x2)

    ite = 0
    while sign(f1) != sign(f2):
        if (x1 >= b):
            return False
        x1 += dx; f1 = f(x1)
        ite += 1

    x1 -= dx; f1 = f(x1)
    while sign(f1) != sign(f2):
        if x2 <= x1:
            x2 += dx
            return False
        x2 -= dx; f2 = f(x2)
        ite += 1

    x2 += dx
    return ite,x1,x2
