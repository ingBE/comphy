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

f = lambda x:x**3 - 20.0*x**2 + 5*x +3

root,error = bisection(f)
print('Root:',root,' error:',error)
