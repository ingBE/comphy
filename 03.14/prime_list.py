def prime_list(x):
	def prime0(x,a=[]):
		def prime(x0,x1):
			if ( x1 == 1 ):
				return True
			if ( x0 % x1 == 0 ):
				return False
			return prime(x0,x1-1)
		if ( x == 1 ):
			return a
		if prime(x,x-1):
			return prime0(x-1,[x]+a)
		return prime0(x-1,a)
	return prime0(x)

print(prime_list(500))
