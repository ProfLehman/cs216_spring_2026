
# change.py
# spring 2026
# prof. lehman

# in-class example
# nested for loops to determine
# number of ways to make change for a dollar
# uses "brute-force" approach by testing
# every single combination


count = 0

for p in range(0,101):
    for n in range(0,21):
        for d in range(0, 11):
            for q in range(0,5):
                for h in range(0,3):
                    
                    if (p + n*5 + d*10 + q*25 + h*50) == 100:
                    
                        #print( p, n, d, q,)
                        print( f"{p} pennies, ", end="")
                        print( f"{d} dimes, ", end="")
                        print( f"{n} nickels, ", end="")
                        print( f"{q} quarters, ", end="")
                        print( f"{h} halves = $1.00")
                        
                        count = count + 1
                        
                # end for h
            # end for q
        # end for d
    # end for n
# end for p

print()
print( f"Total change combinations = {count}" )