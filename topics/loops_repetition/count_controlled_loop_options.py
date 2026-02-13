
# count_controlled_loop_options.py
# spring 2026
# prof. lehman
# count controlled loop options


# while loop
a = 0
while a < 4:
    print( a )
    a = a + 1


# for loop with range (start to stop+1)
for b in range(0, 4):
    print(b)

# for loop with range 0 to stop+1
for c in range(4):
    print(c)


# for loop with list
for d in [0,1,2,3]:
    print( d )
    
    

# recursive approach
def count(value, stop):
    if value < stop:
        print( value )
        count( value + 1, stop) # recursive call

# call count function
count(0, 4)




    