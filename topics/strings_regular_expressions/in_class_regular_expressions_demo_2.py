import re

"""
test = [ "46750", "46750, IN", "IN", "12364, "]



pattern = r"[0-9]{5}, [A-Z]{2}"

i = 0
while i < len(test):
    
    print( test[i], end="    ")
    print( bool( re.fullmatch(pattern, test[i] )  ))
    
    i = i + 1

"""

print( re.search(r"[0-9]", "test" )  )
print( re.search(r"[0-9]", "test3" )  )





