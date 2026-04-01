# writeNumbers.py
# spring 2026
# prof. lehman
# write numbers to text file
# one data item per line

from random import *
import os

# open file for writing
file_name = "numbers2.txt"
file = open(file_name, "w") # w is for write mode

# write 50 numbers
for i in range(0,50):
    
    n = randint(0,2000) # get random number
    
    file.write( f"{n}\n" )
    print(f"{n}") #echo data written to file
    
file.close() #ensures file is written

# output number of bytes written
bytes = os.path.getsize(file_name)
print()
print(f"{bytes} bytes written to {file_name}")



