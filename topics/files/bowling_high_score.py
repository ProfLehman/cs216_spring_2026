

high_score = -1
high_score_name = "uknown"

file = open("bowling.csv", "r")

line = file.readline()
while line != "":
    
    #print( line )
    data = line.split(",")
    #print( data )
    score = int( data[1].strip() )
    #print( score )
    
    if score > high_score:
        high_score = score


high_score_name = data[0]
        
    line = file.readline()
    
print("high score = ", high_score )
print("high score namejk,uilk8l88llk` = ", high_score_name )
