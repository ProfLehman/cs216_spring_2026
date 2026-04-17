
# in_class_review.py
# partial answers to Exam 3 review questions
# prof. lehman
# spring 2026

# *** dictionaries ***

# empty dictionary
student_scores = {}

# dictionary with starting values
student_scores = {"Norman":100, "Norma":99 }

#   dictionary    key       value
student_scores[ "Alice" ] = 95
student_scores[ "Bob" ] = 88
student_scores[ "Carlos" ] = 91

print( student_scores )
print()

print( student_scores["Alice"] )

print( student_scores.get("Bob") )

#print( student_scores["Dan"] ) #error
print( student_scores.get("Dan") ) #None
print( student_scores.get("Dan", -1) ) # -1

if "Dan" in student_scores:
    print("Dan is in dictionary")
else:
    print("Dan is NOT in dictionary")
    

key = "Carlos"

if key not in student_scores:
    print("Adding {key} ...")
    student_scores[ key ] = 0 # create entry
else:   
    student_scores[ key ] += 1
    
print( student_scores )
print()

student_scores[ "Bob" ] = 99
student_scores[ "Alice" ] += 80
student_scores.pop("Norman")

if "Frank" in student_scores:
    student_scores.pop("Frank")

print( student_scores )
print()

# display keys
for k in student_scores:
    print( k )
    
# display values
for v in student_scores.values():
    print( v )
    
# display keys and values
for k,v in student_scores.items():
    print( f"key is {k}, value is {v} )" )

for k in student_scores:
    print( k, student_scores[k] )
    

print()


# *** files ***


# read text file one line at a time

file = open("numbers.txt", "r")

count = 0
total = 0

line = file.readline().strip()
#line = file.readline()
#line = line.strip()

while line != "":
    print( line )
    count = count + 1
    
    # note line contains number as string, must convert to int
    total = total + int(line)
    
    line = file.readline().strip()

print("count = ", count)
print("total = ", total)


# read csv file and write to csv file

# file to write
file_out = open("selected_data.csv", "w")
file_out.write( "name, score\n" )

# file to read
file = open("data.csv", "r")

count = 0
total = 0

line = file.readline().strip()

while line != "":
    
    # line is a string
    print( line )
    
    # split into list
    items = line.split(",")
    print( items )
    
    # extract name
    name = items[0].strip()
    
    # extract number and convert to int
    value = int( items[1].strip() )

    print( name, value )
    print()
    
    total = total + value

    # write out names and values that meet criteria
    if value >= 50 and value <= 75:
        count = count + 1
        file_out.write( f"{name}, {value}\n" )
    
    line = file.readline().strip()

print("count = ", count)
print("total = ", total)

# close files to ensure data is written to file
file.close()
file_out.close()





