# in_class_example_currency.py
# prof. lehman
# spring 2026
# clean and convert currency 

temp = "$$$$ 5,,,567.89"

print( "original:", temp  )
print()


# option #1 - old school loop
# only keeps digits and period
#comma_count = 0
amount = ""
i = 0
while i < len(temp):
    #print( temp[i] )
    if temp[i].isdigit() or temp[i] == ".":
        amount = amount + temp[i]
    
    # fyi: if you needed to keep one comma
    #if temp[i] == "," and comma_count == 0:
    #    amount = amount + temp[i]
    #    comma_count = comma_count + 1
        
    i = i + 1

print( "cleaned:", amount )


# option #2 for loop with index
amount = ""
for i in range(0,len(temp)):
    if temp[i].isdigit() or temp[i] == ".":
        amount = amount + temp[i]

print( "cleaned:", amount )


# option #3 for loop with in operator
amount = ""
for thing in temp:
    if thing.isdigit() or thing == ".":
        amount = amount + thing       

print( "cleaned:", amount )
print()

# convert amount to float
amount = float(amount)
print( type(amount) )
print( amount )

# add one to amount to demontrate amount is valid float
print( amount + 1 )

# -- end --
