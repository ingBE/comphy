## Find one of the roots of y(x) = -x^2 / 4 +1 with a precision of 1e-4
##
##	1. By choosing sufficiently small dx
##	2. By dividing the interval by 5 and repeating the process starting from [1,3] bracket.
##
##	Compare how many iterations are required for each method.

from numpy import sign

def rootsearch(f,a=-100,b=100,dx=0.1):
	x1 = a; f1 = f(x1)
	x2 = b; f2 = f(x2)

	ite = 0
	while sign(f1) != sign(f2):
		if x1 >= b:
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
