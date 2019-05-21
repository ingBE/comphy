from functools import partial

def f(x2):
    return lambda x:x+x2*2
print(f(2)(1))

g = lambda x2:lambda x:x+x2*2
print(g(2)(3))

f = lambda x1,x2:x1+x2*2
g = partial(f,1)
print(g(2))
