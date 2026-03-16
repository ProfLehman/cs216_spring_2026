# class examples
# prof. lehman
# spring 2026
# demonstrates use of string functions to 
# convert first last to last, first initial period
#
# Ada Lovelace -> lovelace, a.
# Charles Babbage -> baggage, c.

s = "Ada Lovelace"
#s = "Charles Babbage"


# option #1 to find space - old school loop
space = -1 # not found
i = 0
while i < len(s) and space == -1:
    if s[i] == " ":
        space = i
    i = i + 1
    
print( "space at", space )


# option #2 to find space - string method
# -1 is returned if not found
space = s.find(" ")
print( "space at", space )


# extract first and last names using position of space
first = s[0:space]
last = s[space+1:]

initial = first[0:1]
#initial = s[0,1]  # this also works in this example

#initial = s[space+1:space+2] # fyi: not needed, but this gets first letter of last name

print()
print( "first = ", first )
print( "last = ", last )
print( "initial = ", initial )
print()

print(
    s )
print()
answer = last + ", " + initial + "."
print( answer )

# convert to lower case
answer = answer.lower()
print( answer )


