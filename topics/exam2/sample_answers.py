

email = "rpepper@hu.edu"

pos = 0
i = 0
while i < len(email):
    if email[i] == "@":
        pos = i
    i = i + 1
    
#pos = email.find("@")

id = email[:pos]

print( id )

print()


sentence = "Today is Wednesday really"

count = 0

i = 0
while i < len(sentence):
    if sentence[i] == " ":
        count = count + 1
    i = i + 1

count = 0
for thing in sentence:
    if thing == " ":
        count = count + 1



words = count + 1
print( "number of words = ", words ) 
    
print( sentence.count(" ") + 1 )
    
    
word = "H  un   ting to   n"

i = len(word)-1
while i >= 0:
    
    if word[i] != " ":
        print( word[i], end="")
        
    i = i - 1
    
print()
for i in range(len(word)-1, -1, -1):
    
    if word[i] != " ":
        print( word[i], end="")
  
print()
word = "Hu ntin g ton"

word = word.replace(" ", "")
                    
print( word )

for i in range(len(word)-1, -1, -1):
    print( word[i], end="")
               
print()

exam = [ 40, 50, 90, 23 ]

print( exam )

i = 0
while i < len(exam):
    #print( exam[i] )
    
    if exam[ i ] < 70:
        exam[ i ] = exam[ i ] + 5
    
    i = i + 1

print( exam )

for i in range( 0, len(exam) ):
    #print( exam[i] )
    
    if exam[ i ] < 70:
        exam[ i ] = exam[ i ] + 5


print()

print("before")
print( exam )
for score in exam:
    
    if score < 70:
        #print( score )
        score = score + 5

print( exam )




    
    
    
    