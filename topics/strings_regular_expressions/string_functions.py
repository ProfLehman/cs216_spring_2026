
# strings_inclass_february_23.py
# demos from class Feburary 23, 2026
# prof. lehman
#
#    0123456789012
s = "python coding"

print( s[1] )

print( s[0:2] ) 

print( s[:4] ) 

print( s[4:] ) 

print( s[-1] ) 

print( len(s) ) 

print( s.find("t") )

print( s.find("t", 4) )

print( s.capitalize() )

print( s.title() )

print( s.upper() )

print( s )

print( s[-2] )

print( s[1:len(s)-1] )
print( s[1:-1] )


print()
print("01234567890123456789")
print( s )
print( s.find("o") )
print( s.find("o", 5) )

# print all the o's?

s = "oops oh no ... oh"
x = 0
while x < len(s):
    if s[x] == "o":
        print( "o at", x )
    x = x + 1


print()

pos = s.find("o")
while pos != -1:
    print( "o at ", pos )
    pos = s.find("o", pos+1)
    
    





print()

s = "abc"
print( s.upper() )
print( s.capitalize() )
print( s )
s = s.upper()
print( s )

s = "   Monday   "
print( f"*{s}*" )
s = s.strip()
print( f"*{s}*" )










