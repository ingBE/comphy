def newtonRaphson(f,x,dx = 0.1,ite = 10):
    for i in range(ite):
        ## calulate f'(x)
        diff = (f(x+dx)-f(x))/dx
        x -= f(x)/diff
    return x
