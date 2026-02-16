


a = 2
while a <= 20:
    print( a, end=" " )
    a = a + 2
    # end of while a
    
print()

for b in range(2, 21, 2):
    print( b, end = " ")

print()
for i in range(3):
    print(i, end=' ')
    
print()
for i in range(3,7):
    print(i, end=' ')  
print()
print()

for letter in "Huntington":
    print( letter, end="-" )
print()

s = "Huntington  U."

for letter in s:
    print( letter, end="-" )
print()

print( len(s) )
print()

x = 0
while x < len(s):
    print( x, s[x] )
    x = x + 1
    
print()

for i in range(0, len(s)):
    print( i, s[i] )
print()

#    012345
s = "work"
x = len(s) - 1

while x >= 0:
    
    print( x, s[x] )
    
    x = x - 1
print()

s = "Monday"
for i in range(len(s)-1, -1, -1):
    print( i, s[i] )
print()


  
  
  
  
    