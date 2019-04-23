def f(x2):
    return lambda x:x+x2
print(f(2)(1))

g = lambda x2:lambda x:x+x2
print(g(2)(3))
