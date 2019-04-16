# total function
def total(li):
    total = 0
    arr = li[:]
    while ( arr != [] ):
        total = total + arr.pop()
    return total

# average function
def average(li):
    return total(li)/len(li)

# Create list of input numbers
def numbers():
    arr = []
    while True:
        number_str = input('Enter numbers: ')
        if ( number_str == 'done' ):
            return arr
        try:
            number = int( number_str )
            arr.append( number )
        except:
            print('That is not numbers')

# program start
num_list = numbers()
print( 'total =', total( num_list ) )
print( 'count =', len( num_list ) )
print( 'average =', average( num_list ) )
