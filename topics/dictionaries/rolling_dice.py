
# rolling_dice.py
# spring 2026
# in-class example demonstrates dictionaries
#
# roll two dice N times
# keep track of the number of times each total is rolled

import random

# number of rolls
N = 1000

# dictionary to store counts
counts = {}

# simulate rolling the dice N times
for i in range(N):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    total = die1 + die2
    
    # update dictionary counts
        
    
# display results of rolling 2 to 12
# in format
#   2: 1
#   3: 4
# ...
#  12: 2
print( counts )


# update N to be 10 rather than 1000 and run code
# update N to be 0 rather than 1000 and run code




