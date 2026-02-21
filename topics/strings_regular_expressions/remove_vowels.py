
# remove_vowels.py
# spring 2026
# prof. lehman
# in-class example for strings

s = "Class does not meet in Friday"
s2 = ""

i = 0
while i < len(s):
    
    c = s[i].lower()
    c = s[i]
    #if c != "a" and c != "e" and c != "i" and c != "o" and c != "u" and c != "y":
    #if c not in "aeiouyAEIOUY":
    if "aeiouyAEIOUY".find(c) == -1:  
        s2 = s2 + c    
    
    i = i + 1

print()
print( s )
print( s2 )


