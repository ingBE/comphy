def comgrade( Score ):
    if (( Score > 10 ) or ( Score < 0 )):
        return 'Bad score'
    if ( Score >= 8 ):
        return 'A'
    if ( Score >= 6 ):
        return 'B'
    if ( Score >= 4 ):
        return 'C'
    if ( Score >= 2 ):
        return 'D'
    if ( Score < 2 ):
        return 'F'

# program start

triger = True

while triger:
    try:
        score = input('Enter score: ')
        print( comgrade( float( score ) ) )
    except:
        print('Bad score')
        triger = False
