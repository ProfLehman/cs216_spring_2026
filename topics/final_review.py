
# sample answer from final exam review
# spring 2026

# ------------------------
# *** reading csv file ***
# ------------------------

"""
Accounts.csv
A0001, Vince, 200.25
A0345, Sara, 401.50
...
A4567, Olivia, 100.00
A4444, Jacob, 100.00
"""

high_amount = -1.0
best_person = "unknown"

file = open("Accounts.csv", "r")

line = file.readline()
while line != "":
    
    print( "debug 1", line )
    data = line.split(",")
    print( "debug 2", data )
    
    amount = float( data[2].strip() )
    print( "debug 3: ", amount )

    if amount > high_amount:
        high_amount = amount
        best_person = data[1].strip()
    
    line = file.readline()
    

print( "high amount", high_amount )
print( "person", best_person )
print()
print()

# ------------------------
# *** lists ***
# ------------------------

#          0   1   2 
scores = [50, 70, 89, 77, 92, 99, 100, 98, 44, 86]

passing = 0
failing = 0

i = 0
while i < len(scores):
    
    print( scores[ i ] )
    
    if scores[ i ] >= 60:
        passing += 1
    else:
        failing += 1
    
    i = i + 1

print( f"Passing: {passing}" )
print( f"Failing: {failing}" )


passing = 0
failing = 0
print()

# alternate approach with in
for score in scores:
    
    print( score )
    
    if score >= 60:
        passing += 1
    else:
        failing += 1
    
    i = i + 1

print( f"Passing: {passing}" )
print( f"Failing: {failing}" )
print()

# ------------------------
# *** dictionaries ***
# ------------------------

# starting dictionary
parts = {"a127":32.99, "b16":55.89}

print( parts )

# add new key and value to dictionary
parts["c333"] = 99.9

print( parts )

#print( parts["HU"] ) #will give error if key not in dictionary

name = "HU"

#parts["HU"] = 1897.0

# approach 1
if name in parts:
    print( name, " => ", parts[name] )
else:
    print( name, "Not Found")

# approach 2
print( parts.get( name, "Not Found" ) )
print()

# display all keys and values
for k, v in parts.items():
    print( k, v )
print()

# display all keys
for k in parts.keys():
    print( k )
print()

# display all values
for v in parts.values():
    print( v )
print()

# ------------------------------
# *** OOP classe and objects ***
# ------------------------------

class Account:
    
    # constructor
    def __init__(self, name="unknown", balance=0.0):
        print("in constructor")
        self.name = name
        self.balance = balance
    
    # getters
    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name
    
    # setters
    def addBalance(self, amount):
        if amount > 0:
            self.balance += amount
            
    def setName(self, name):
        self.name = name
    
    # string method allows normal print to work for object
    def __str__(self):
        return f"Name = {self.name}, Balance = ${self.balance}"
            

# main

# create "instances"
norm = Account("Norman Forester", 598.63)
norma = Account()

# call getters
print( norm.getBalance() )
print( norma.getBalance() )
print()

# call addBalance
norm.addBalance( 40.0 )
print( norm.getBalance() )

norm.addBalance( -140.0 )
print( norm.getBalance() )

# call __str__ ... done when you print object
print( norm )
print( norma )
print()

# instance variables can be referenced directly
# but this can lead to problems,
# so generally best to use methods
print( norm.name )
print( norm.balance )

# setting balance directly allows for negative balance
norm.balance = -90
print( norm.getName() )

# call setter for name
norma.setName("Norma Forester")
print( norma )



