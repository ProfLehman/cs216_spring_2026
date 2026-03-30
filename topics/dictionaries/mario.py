
# mario.py
# spring 2026
# prof. lehman
# dictionary and tuple to store 2-D world


text_world = ""

text_world += "                          =     " + "\n"
text_world += "    =          C     C    #     " + "\n"
text_world += "    #  =      XX          #     " + "\n"
text_world += "    #  #     XXX   XXXX   #     " + "\n"
text_world += "--------------------------------"

# display original world
print(text_world)

# create dictionary
world = {}

# split into rows
lines = text_world.split("\n")

# populate dictionary with non-space characters
for row in range(len(lines)):
    for col in range(len(lines[row])):
        char = lines[row][col]
        if char != " ":
            world[(row, col)] = char

# display dictionary
print("\nDictionary contents:")
for key in sorted(world):
    print(f"{key}: '{world[key]}'")
    
    
# display world from dictionary
for row in range(0,6):
    for col in range(0,30):
        if (row, col) in world:
            print( world[row,col], end="")
        else:
            print( " ", end="")
    print()


