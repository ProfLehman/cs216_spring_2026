
# rolling_dice.py
# spring 2026
# in-class example demonstrates dictionaries
#
# roll two dice N times
# keep track of the number of times each total is rolled

import random

# number of rolls
N = 100

# dictionary to store counts
counts = {}

# alternate approach add entry for each
#for key in range(2,13):
#	counts[key] = 0

# simulate rolling the dice N times
for i in range(N):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    total = die1 + die2
    
     # update dictionary counts
    if total in counts:
        counts[ total ] = counts[ total ] + 1
    else:
        counts[ total ] = 1
     
    # end loop
    
    
# display results of rolling 2 to 12
# in format
#   2: 1
#   3: 4
# ...
#  12: 2
print()
print( counts )
print()

key = 2

while key <= 12:

    if key in counts:
        print( f"{key} : {counts[key]}" )
    else:
        print( f"{key} : 0" )
    
    key = key + 1

# update N to be 10 rather than 1000 and run code
# update N to be 0 rather than 1000 and run code




