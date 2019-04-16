# Problem.
# Iterate from 0 to 10.
# Open a file 'nexp.txt' to write the results of i, exp(i).
# Set an appropriate format.
# Close the file

#from numpy import exp

aa = []

def a(n):
	return n**2

f = open('nexp.txt','w')

for i in range(1,11):
	aa.append('{:2d} {:5.5f}'.format( i, a(i) ) )
	f.write('{:2d} {:5.5f}'.format( i, a(i) ) )
	f.write('\n')

f.close()
print(aa)
