# rgb_colors.py
#
# prof. lehman
# spring 2026
#
# demonstrates nested loops to display
# rgb color options with starting value for red
# and varying green and blue

# Input starting Red value
red = int(input("Enter starting Red value (0-255): "))

# Keep red in valid range
if red < 0:
    red = 0
if red > 255:
    red = 255

filename = "rgb_nested_loops.html"

with open(filename, "w") as f:
    
    # write html starting tags to create page
    f.write("<html><head>")
    f.write("<style>")
    f.write(".grid { display: grid; grid-template-columns: repeat(5, 100px); }")
    f.write(".box { width: 100px; height: 100px; border: 1px solid black; ")
    f.write("display: flex; align-items: center; justify-content: center; font-size: 12px; }")
    f.write("</style></head><body>")

    f.write(f"<h2>Red = {red}</h2>")
    f.write("<div class='grid'>")

    g_percent = 0
    while g_percent <= 100:

        g = int(255 * g_percent / 100)

        b_percent = 0
        while b_percent <= 100:

            b = int(255 * b_percent / 100)

            f.write(f"<div class='box' "
                    f"style='background-color: rgb({red},{g},{b});'>"
                    f"{red},{g},{b}</div>")

            b_percent += 25

        g_percent += 25
        # end while b_percent
        
    #end while g_percent
        
        
    # write html ending tags
    f.write("</div></body></html>")

print("HTML page created: rgb_nested_loops.html")
