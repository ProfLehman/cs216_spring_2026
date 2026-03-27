
# basketball.py
# spring 2026
# in-class example demonstrates dictionaries


# dictionary for points scored
# key is name
# value is score
points = {}

# get player name (priming the loop)
name = input("player: ")

while name != "Done":

    # get points scored
    point = int( input("points scored: ") )
    
    #update points
    if points.get(name) == None:   # check if player is in dictionary
        points[name] = point
    else:
        points[name] = points[name] + point
    
    # get player name
    name = input("player: ")
    
    # end loop
    
# at end display points dictionary
print( points )

