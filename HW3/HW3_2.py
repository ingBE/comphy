import numpy as np

def triangular(A,B):
    # Initializing parameters
    nsize   = len(A)
    a = np.array(A)
    b = np.array(B)

    for ipiv in range(0,nsize-1):
        for rnum in range(ipiv+1,nsize):
            lam     = a[rnum,ipiv]/a[ipiv,ipiv]
            a[rnum] = a[rnum,0:nsize] - lam * a[ipiv,0:nsize]
            b[rnum] = b[rnum] - lam * b[ipiv]

    return [a,b]

def solve(A,B):
    # Initializing parameters
    nsize = len(A)
    a     = np.array(A)
    b     = np.array(B)

    # Triangular
    for ipiv in range(0,nsize-1):
        for rnum in range(ipiv+1,nsize):
            lam     = a[rnum,ipiv]/a[ipiv,ipiv]
            a[rnum] = a[rnum,0:nsize] - lam * a[ipiv,0:nsize]
            b[rnum] = b[rnum] - lam * b[ipiv]

    x = np.zeros(nsize)
    x[nsize-1]=b[nsize-1]/a[nsize-1][nsize-1]
    for n in range(2,nsize+1):
        sum, i = 0, nsize - n
        for j in range(i,nsize):
            sum = sum + a[i][j] * x[j]
        x[i] = (b[i] - sum) / a[i][i]
        
    return x
    
def solve0(A,B): # Use triangular function
    # Initializing parameters
    nsize = len(A)
    C = triangular(A,B)
    a = C[0]
    b = C[1]
    
    x = np.zeros(nsize)
    x[nsize-1]=b[nsize-1]/a[nsize-1][nsize-1]
    for n in range(2,nsize+1):
        sum, i = 0, nsize - n
        for j in range(i,nsize):
            sum = sum + a[i][j] * x[j]
        x[i] = (b[i] - sum) / a[i][i]
    
    return x
