# in_class_example_eh.py
# prof. lehman
# spring 2026
#
# demonstrates use of regular expressions
# to determine the number of "eh's" in a sentence

sentence = "Nice weather for February, eh? Thought it was supposed to snow, eh? Guess we got lucky, eh?"
print( sentence )
print()

# option #1 - old school loop
count = 0
i = 0
while i < len(sentence)-1:
    if sentence[i:i+2] == "eh":
        count = count + 1
    
    i = i + 1

print("count: ", count )
print()


# option #2 - find method within sentinel loop
count = 0
position = sentence.find("eh")
while position != -1:
    count = count + 1
    
    # note in subsequent find's we start at the last position + 1
    position = sentence.find("eh", position + 1)
    
print("count: ", count )
print()


# option #3 - regular expressions
import re

pattern = r"eh"
matches = re.findall(pattern, sentence)

print( matches ) #displayes list
count = len(matches) #counts matches in list

print("count: ", count )
print()

# -- end --
