text_world = ""

text_world += "                          =     " + "\n"
text_world += "    =          C     C    #     " + "\n"
text_world += "    #  =      XX          #     " + "\n"
text_world += "    #  #     XXX   XXXX   #     " + "\n"
text_world += "--------------------------------"

# create dictionary
world = {}

lines = text_world.split("\n")

# store non-space characters
for row in range(len(lines)):
    for col in range(len(lines[row])):
        char = lines[row][col]
        if char != " ":
            world[(row, col)] = char

# determine dimensions
max_row = len(lines)
max_col = max(len(line) for line in lines)

# reconstruct and display world from dictionary
print("Reconstructed world:\n")

for row in range(max_row):
    line = ""
    for col in range(max_col):
        if (row, col) in world:
            line += world[(row, col)]
        else:
            line += " "
    print(line)