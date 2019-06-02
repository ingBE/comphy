from numpy import sign, abs

def bisection(f,a=-100,b=100):
    for i in range(50):
        mp = (a + b)/2  # Midpoint in the bisection formula
        fa = f(a)
        fb = f(b)
        if sign(fa)==sign(fb): return mp,abs(a-b)
        fm = f(mp)
        if sign(fa)!=sign(fm):
            b = mp
        else:
            a = mp
    return mp,abs(a-b)
