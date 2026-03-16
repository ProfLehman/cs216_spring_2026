
# review.py
# exam 2 in-class review questions
# spring 2026
# lehman

# 1. While Loop 10, 20, 30, 40, 50
x = 10

while x <= 50:  
    print(x, end=", ")

    x = x + 10  
    # end loop

print()

# 2. for loops 10, 20, 30, 40, 50
for x in range(10,51,10):
    print( x, end=", " )
   
print()


# 3. Sentinel Loop - total
total = 0
n = int( input("enter n (-1 to quit)"))
while n != -1:
    total = total + n
    n = int( input("enter n (-1 to quit)"))
    # end loop  
    
print( "total ", total )
print()


# 4. Sentinel Loop - valid password
password = input("enter password: ")
while password != "Norman":
    print( "Error, wrong password")
    
    password = input("enter password: ")
    # end loop  

print("Password Valid")


# 5. Nested loops
#  note: 0,5 gives 0, 1, 2, 3, 4  thus x5 numbers
count = 0
for i in range(0,5):
    for j in range(0,10):
        print("x")
        count = count + 1

print( "count", count )
print()

# 6. Predict output
x = 0
while x < 10:
    print(x, end=" ")
    if x == 5:
        break
    x = x + 1
# end loop
print()


# 7. strings
s = "python"

print(s[1])           # y

print(s[0:2])         # py

print(s[:4])          # pyth
 
print(s[4:])          # on

print(s[-1])          # n

print(len(s))         # 6

print(s.find("t"))    # 2

print(s.find("t",4))  # -1

print(s.capitalize()) # Python

print(s.upper())      # PYTHON

print(s)              # python


# 8. Reverse a String
def displayReversed(word):
    
    i = len(word)-1
    while i >= 0:
        print( word[i], end="")
        i = i - 1
        # end loop
    print() 

displayReversed("Ada Lovelace")      # displays ecalevoL adA
displayReversed("Charles Babbage")   # displays egabbaB selrahC
displayReversed("Monday")   # 
print()

# 9. Strings - Get Initials
def getInitials(name):
    
    space = name.find(" ")
    #print( space )
    
    first = name[0]
    #print( first )
    last = name[space+1:space+2]
    #print( last )
    return first + last

print(getInitials("Ada Lovelace"))      # AL
print(getInitials("Charles Babbage"))   # CB
print()
 
# 10. Strings - Count Letters
def countLetters(name, letter):

    count = 0  
    
    # while loop approach
    #i = 0
    #while i < len(name):
    #    if name[i] == letter:
    #        count = count + 1
    #    i = i + 1
    
    # for loop approach
    #for i in range(0,len(name)):
    #    if name[i] == letter:
    #        count = count + 1
    
    # in approach
    for temp in name:
        if temp == letter:
            count = count + 1
            
    return count

print(countLetters("Charles Babbage", "b"))   # displays 2
print(countLetters("Apple Computer", "p"))    # displays 3
print(countLetters("Apple Computer", "x"))    # displays 0
print()

# 11. Lists are mutable
def changeIt(x):
    x = -1

def changeList(list):
    list[0] = -1

x = 7
changeIt(x)
print(x) # 7

y = 7
changeIt(y)
print(y) # 7

list = [2, 3, 4]
changeList(list)
print(list) # -1 3 , 4
print()

# 12. Lists
list = [0] * 1000
print(len(list)) # 1000
print(list[0])   # 1
# print( list )
print()

# 13. Lists - exam scores
exam = [77, 90, 54, 46, 94, 78]

print(exam)  # displays [77, 91, 54, 46 … , 94, 78]
exam[1] = 91
print(exam)

# 14. Lists = High Score
print( max(exam) )
print()

# 15. display all scores that are less than 60.
i = 0
while i < len(exam):
    if exam[i] < 60:
        print( exam[i] )      
    i = i + 1

print()

# alternate with range
for i in range(0, len(exam)):
    if exam[i] < 60:
        print( exam[i] ) 

print()

# alternate with in
for score in exam:
    if score < 60:
        print( score )

print()

# 16. Add to end of list
exam.append(89)
print(exam)  # displays [77, 91, 54, 46 … , 94, 78, 89]
print()

# alterate append
exam = exam + [67]
print( exam )
print()

# 17. Remove first item from list
exam.pop(0) #first item
print( exam )

exam.pop() #last item
print( exam )

# 18. Add +2 to all list items
for i in range(0, len(exam)):
    exam[i] = exam[i] + 2
    
print( exam )

# 19. sort list
exam.sort()
print(exam)  # displays [48, 56, 80, …, 91, 93, 96]

# reverse a list
exam.reverse()
print( exam )

# -- end --








    