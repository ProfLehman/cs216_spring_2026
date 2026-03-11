
# lists_in_class.py
# spring 2026

# Creates a single list containing name, exam1, exam2 repeating

import random

first_names = [
    "Aisha", "Mateo", "Sofia", "Jamal", "Hiroshi",
    "Priya", "Liam", "Fatima", "Diego", "Wei",
    "Amara", "Noah", "Arjun", "Isabella", "Malik",
    "Yuna", "Carlos", "Zara", "Omar", "Elena",
    "Alex", "Jordan", "Taylor", "Morgan", "Casey",
    "Riley", "Avery", "Parker", "Quinn", "Dakota"
]

last_names = [
    "Garcia", "Kim", "Patel", "Nguyen", "Hernandez",
    "Ali", "Singh", "Lopez", "Chen", "Khan",
    "Rivera", "Park", "Hassan", "Diaz", "Okafor",
    "Torres", "Rahman", "Ibrahim", "Santos", "Tanaka",
    "Smith", "Johnson", "Brown", "Davis", "Miller",
    "Wilson", "Moore", "Taylor", "Anderson", "Thomas"

]


data = []

# set seed so results are repeatable
# random.seed(42)

# create 20 records
for i in range(20):
    name = random.choice(first_names) + " " + random.choice(last_names)
    exam1 = random.randint(60, 100)
    exam2 = random.randint(60, 100)

    data.append(name)
    data.append(exam1)
    data.append(exam2)

# display records
for i in range(0, len(data), 3):
    name = data[i]
    exam1 = data[i+1]
    exam2 = data[i+2]

    print(f"{name:20} Exam1: {exam1:3}  Exam2: {exam2:3}")

print()
print()

    
# display all students with their exam 1 score ie. Amy Garcia, 89

# display the class all exam 1 scores in format last name, score ie. Smith, 89

# display the high score for exam 1

# display the class average for exam 1

# display class average combining exam1 and exam2 as the grade for each student




