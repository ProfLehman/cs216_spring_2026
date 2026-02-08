"""
exam1_review_sample_answers.py
Spring 2026
Prof. Lehman (sample answers)

Sample answers shown.

Try running (and modifying) the sample code to test your understanding

"""

import random


# ---------------------------------------------------------------------
# 1) Output tracing - output shown below
# ---------------------------------------------------------------------
"""

AB
C
bl
D

note:
print for A includes end="" which keeps next print on the same line
print for C includes an extra line return with the slash n, thus there is a blank line between

"""


# ---------------------------------------------------------------------
# 2) Output tracing with variables and strings
# ---------------------------------------------------------------------
"""
# 2) output shown after comment hash tag

A = 4
B = 2

print("A + B")         # A + B

print(A * B)           # 8

print(A, B)            # 4 2

print('"A", "B"')      # "A", "B"

"""


# ---------------------------------------------------------------------
# 3) f-string formatting as currency with comma + 2 decimals
# ---------------------------------------------------------------------
city = "London"
price = 1235.658

# 3) Fill-in-the-blank answer:
print(f"Ticket for {city} is ${price:,.2f}")
print()

# ---------------------------------------------------------------------
# 4) Operators and assignment - assume code is executed in order
# ---------------------------------------------------------------------
x = 7
print(x % 5)            # 2

x -= 1
print(x)                # 6

x = 4**2
print(x)                # 16

x = x / 2
print(x + 2)            # 10.0
print()

# ---------------------------------------------------------------------
# 5) type()
# ---------------------------------------------------------------------
letter = "A"
gpa = 3.67
age = 18

print( type(letter) )     # <class 'str'>
print( type(gpa) )        # <class 'float'>
print( type(age) )        # <class 'int'>
print()

# ---------------------------------------------------------------------
# 6) Order of operations
# ---------------------------------------------------------------------
print(40 + 50 / 5 * 5 + 10)    # 100.0
print()

# ---------------------------------------------------------------------
# 7) Function returns a formatted string + example calls
# ---------------------------------------------------------------------
def output_line(product, price):
    result = ""

    # sample answer code:
    result = f"Price of {product} is ${price:.2f}"

    return result

# main
item = "iPhone"
cost = 750.2500

# b) call using item and cost variables
line1 = output_line(item, cost)
print( line1 )
print()

# c) call using string and float literal
line2 = output_line("HU t-shirt", 27.50)
print( line2 )
print()

# ---------------------------------------------------------------------
# 8) Stub function getPayment
# ---------------------------------------------------------------------
def getPayment(amount, rate, years):
    
    # Stub: returns default value until implemented
    payment = -1.0
    
    # code for payment would go here
    
    return payment


# main
print( getPayment(10000, 3.2, 5) )  # displays -1.0
print()

# ---------------------------------------------------------------------
# 9) If statements: individual-if approach and nested/elif approach
# ---------------------------------------------------------------------

"""
a) Individual If Approach (no else/elif).
Assumes hour is valid (8,9,10,11,12,1,2,3).
"""

hour = int( input("Enter hour (8 to 12, 1 to 3): ") )
day = "unknown"

if hour == 8 or hour == 9 or hour == 10:
    day = "Monday"

if hour == 11 or hour == 12:
    day = "Wednesday"

if hour == 1 or hour == 2 or hour == 3:
    day = "Friday"

print("Individual If - Day =", day)
print()

"""
b) Nested If / elif Approach (most efficient).
"""
day = "unknown"

if hour == 8 or hour == 9 or hour == 10:
    day = "Monday"
elif hour == 11 or hour == 12:
    day = "Wednesday"
else:
    day = "Friday"

print("Nested If - Day =", day) 
print()


# ---------------------------------------------------------------------
# 10) If logic trace
# ---------------------------------------------------------------------
day = "Friday" 
delay = False 
time = "unknown" 

if delay == True: 
    time = "10:00 am" 
else: 
    if day == "Wednesday": 
        time = "8:30 am" 
    else: 
        time = "8:00 am" 

print( time )                 # 8:00 am
print()

# ---------------------------------------------------------------------
# 11) Input + if + mod operator: ends with zero
# ---------------------------------------------------------------------

# alternate approach for input
# print("Enter number: ", end="")
# number = int( input() )

number = int(input("Enter number: "))

if number % 10 == 0:
    print("Ends with a zero")
else:
    print("Does not end with a zero")

print()

# ---------------------------------------------------------------------
# 12) Input + branching with least comparisons
# ---------------------------------------------------------------------

soft_skills = int(input("Soft skills (1-10): "))
tech_skills = int(input("Tech skills (1-10): "))

# if logic
if soft_skills < 6 and tech_skills < 7:
    print("Do Not Hire - Tech and Soft skills low")
elif soft_skills < 6:
    print("Do Not Hire - Soft skills low")
elif tech_skills < 7:
    print("Do Not Hire - Tech skills low")
else:
    print("Hire")

print()



# ---------------------------------------------------------------------
# 13) Calling functions (do not modify given functions)
# ---------------------------------------------------------------------
def display_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Quit")


def get_random_number():
    return random.randint(1, 10)


def print_square(number):
    print(number * number)


def multiply(a, b):
    answer = a * b
    return answer


# main
# a) display menu
display_menu()

# b) assign random number to spin
spin = get_random_number()
print("spin =", spin)

# c) display square of 50
print_square(50)

# d) display 16 x 256 using multiply
print( multiply(16, 256) )
print()

# ---------------------------------------------------------------------
# 14) Function creation: circle_area + call and store
# ---------------------------------------------------------------------
def circle_area(radius):
    pi = 3.14
    
    answer = pi * (radius ** 2)
    
    return answer


area = circle_area(5)
print("area =", area)
print()


# ---------------------------------------------------------------------
# 15) Modules and __main__
# ---------------------------------------------------------------------
"""
15a) When program2.py is executed:

Done

Reason: program1 is imported, but greet() is inside
if __name__ == "__main__", so it does NOT run on import.

15b) When program1.py is executed:

Hello!

Reason: when run directly, __name__ == "__main__", so greet() runs.
"""


# ---------------------------------------------------------------------
# 16 IPO
# ---------------------------------------------------------------------
"""
An IPO (Input-Process-Output) chart is a planning tool that helps you design a program before you write code.
In the Input section you list the data the program needs (what values will be entered or read, and their types/meaning).
It can be helpful to define your variable names

In the Process section you describe the steps and calculations that transform the inputs
into results (formulas, decisions, loops, and key rules).

In the Output section you list what the program should produce
(what to display, save, or return, including formatting).

IPO charts are useful because they clarify requirements, reduce confusion about what the program must do,
and provide a simple roadmap that makes coding faster and less error-prone.

IPO chart is best used in tandem with sample hand calculations to verify accuracy of your IPO chart planning
"""


# ---------------------------------------------------------------------
# 17) Sample Hand Calculations
# ---------------------------------------------------------------------
"""
Hand calculations demonstrate that your IPO planning is correct.
They are especially helpful to verify the math/logic before writing code.

Hand calculations can also help you understand the problem. They can be used
to identify the inputs needed, outputs needed, and define the processing needed.

Sample hand calculations are best used in tandem with an IPO chart.

Saple hand calculations can be used to verify that a program is working correctly by
providing sample data to use when testing your code.
"""

# ---------------------------------------------------------------------
# 17) Automated Test Cases 
# ---------------------------------------------------------------------
"""
Writing automated test cases before coding helps to clearly define
the problem and requirements.

Edge cases can be defined that ensure your code will work for all inputs.

During coding (and after you finish), automated tests help you catch mistakes
quickly and ensure your changes don’t break previously working parts of the program.

The make debugging more efficient because a failing test shows where errors
are located and help to identify scenarios are not not handled correctly.
"""

# -- end ---

