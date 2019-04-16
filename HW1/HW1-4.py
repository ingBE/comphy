# function to converted A into B
def convert( T, A, B ):
    if ( A == B ):
        return T
    if ( A == 'TC' ):
        if ( B == 'TF' ):
            return T * 9/5+32
        if ( B == 'TK' ):
            return T + 273.15
    if ( A == 'TF' ):
        if ( B == 'TC' ):
            return (T-32)*5/9
        if ( B == 'TK' ):
            return convert( convert( T, 'TF', 'TC' ), 'TC', 'TK' )
    if ( A == 'TK' ):
        return convert( T - 273.15, 'TC', B )

# program start
print('Temperature type: [ TC, TF, TK ]')
A = input('Enter Temperature type before convert: ')

while ( (A != 'TC') & (A != 'TF') & (A != 'TK') ):
    A = input('Enter right Temperature type before convert: ')
T = input('Enter Temperature: ')

while True:
    try:
        Temp = float(T)
        break
    except:
        T = input('Enter right Temperature: ')

B = input('Enter Temperature type after convert: ')
while ( (B != 'TC') & (B != 'TF') & (B != 'TK') ):
    B = input('Enter right Temperature type after convert: ')

print( convert( float(T), A, B ) )
