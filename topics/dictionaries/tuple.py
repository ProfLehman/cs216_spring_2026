
t = 'l', 'u', 'p', 'i', 'n'
print( type(t) )

t2 = ('p')
print( type(t2) ) #str

t2fix = ('p',)
print( type(t2fix) ) #tuple
print( t2fix )

t = tuple()
print( t )

t = tuple('huntington')
print( t )
print( t[0] ) #h
print( t[0:4] ) #h, u, n, t

# t[0] = "X" # error, not mutable
print()
t = tuple('spam') * 2
print( t )
print()
t = tuple("huntington")
print()
print( t )
t_sorted = tuple( sorted(t) )
print( t_sorted )

t_reversed = tuple(reversed(t))
print( t_reversed )
print( t )
print()
print()

spot = (4,3)

print( spot )
print( type(spot) )


def addto( a, b, c ):
    
    return (a+1, b+1, c+1)


print( addto(3, 4, 5) )


x, y = spot
print( x )
print( y )


j, k, l = addto( 1, 2, 3 )
print( j, k, l )







