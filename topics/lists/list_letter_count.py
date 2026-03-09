

s = "monday after spring break, yeah!!!"

#count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#letters = ["a", "b", "c" ...]

count = []
letters = []

temp = "abcdefghijklmnopqrstuvwxyz"
for letter in temp:
    letters.append( letter )
    count.append( 0 )
    
print( count )
print( letters )
print()

i = 0
while i < len(s):

    j = 0
    while j < len(letters):
        
        if s[i] == letters[j]:
            count[j] = count[j] + 1
     
        j = j + 1
        # end loop j
         
    i = i + 1
    # end loop i
   
print()
print( count )
print( letters )
print()


i = 0
while i < len(letters):
    print( letters[i], count[i] )
    i = i + 1







