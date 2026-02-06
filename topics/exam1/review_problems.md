
# CS 216 Exam #1 sample review problems

Sample questions (or slightly modified questions) from previous exams and class examples.

---

## 1. What will be output by the following statements?

*(Clearly show blank lines as **bl** if applicable.)*

```python
print("A", end="")
print("B")
print("C\n")
print("D")
```

---

## 2. What will be output by the following statements?

*(Clearly show blank lines as **bl** if applicable.)*

```python
A = 4
B = 2

print("A + B")         ______________
print(A * B)           ______________
print(A, B)            ______________
print('"A", "B"')      ______________
```

---

## 3. Fill in the blank

Fill in the blank such that the message
**“Ticket for London is $1,235.66”**
will be printed using the variables `city` and `price`.
The price must be formatted as currency with a comma and **2 decimal places**.

```python
city = "London"
price = 1235.658

print(f"_______________________________________________________")
```

---

## 4. What will be output by the following statements?

```python
x = 7
print(x % 5)            ______________

x -= 1
print(x)                ______________

x = 4**2
print(x)                ______________

x = x / 2
print(x + 2)            ______________
```

---

## 5. What will be output by the following statements?

```python
letter = "A"
gpa = 3.67
age = 18

print(type(letter))     ______________
print(type(gpa))        ______________
print(type(age))        ______________
```

---

## 6. What will be output by the following statement?

```python
print(40 + 50 / 5 * 5 + 10)    ____________________
```

---

## 7. function that returns a formatted string

a. Complete the following function **output_line** that takes a **product and price** and returns the message as shown. 
The formatted message must be in the form "Price of iPhone is $750.25" with price formatted to two decimal places.
Assume product is a string and price is a float.

```python
# output_line function 
# output_line( string, float ) -> string

def output_line( product, price ):
  result = ""

  *** show code here ***

  return result
```

```python
# main
item = "iPhone"
cost = 750.2500
```

b. Show a function call to output_line function using item and cost variables
```python
```
c. show a function call to output_line function using string "HU t-shirt" and float value 27.50
```python
```

---

## 8. stub function

Create a "stub" function called getPayment that takes an amount, rate, and years and returns the 
loan payment. Use -1.0 as the default payment returned.

```python
# getPayment function
# getPayment( float, float, int ) -> float

*** show code here ***




# main
print( getPayment(10000, 3.2, 5) ) #displays -1.0
```

---

## 9. If statements

Final Exams at ACME University are determined by the starting hour for the course as shown in the table below.  
Write individual and nested if logic to determine the day based on the hour. 

| hour        | day        |
|-------------|------------|
| 8, 9, 10    | Monday     |
| 11, 12      | Wednesday  |
| 1, 2, 3     | Friday     |

You can assume the hour is valid integer shown in the table above.  
Your code does not need to handle invalid values for the hour.  
Your code must set the value for the day (ie. a string), 
you do not add code to print anything to the screen as a print statement for day is provided below. 

a. **Individual If Approach** (may not use else or elif) 

```python
hour = int( input() ) 

day = "unknown" 

# *** add if code here *** 
 

print("Day =", day) 
```

b. **Nested If Approach** (use elif or else, most efficient)
 
```python
hour = int( input() ) 

day = "unknown" 

# *** add if code here *** 
 

print("Day =", day) 
```

---

## 10. If logic

What will be displayed by the following? 

```python

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

print( time )                 ___________________ 
```
---


## 11. Input and If logic (hint: helpful to know mod ie. % operator in Python)

Show the Python statements needed to input an age as an integer value using the console and determine if the number ends with a zero. 

Display the output shown in the sample runs.

You may assume the number entered is a **positive integer greater than zero**

### Sample Run #1

```
Enter number: 20
Ends with a zero
```
### Sample Run #2

```
Enter number: 17
Does not end with a zero
```

```python

*** show code here

```

---

## 12. Input, Branching Question

A local tech company evaluates job candidates based on **soft skills** and **technical skills**.

* `soft_skills` — an integer from **1 to 10**
  * A score of **6 or higher** is required to meet the soft-skills requirement
* `tech_skills` — an integer from **1 to 10**
  * A score of **7 or higher** is required to meet the technical-skills requirement

a. Write a Python program that:

1. Inputs the values for `soft_skills` and `tech_skills`. You may assume the user will enter valid integers within the given ranges.
2. Uses **if statements** to determine the correct outcome
3. Uses the **least number of comparisons possible**
4. Outputs **exactly one** of the following messages (with priority shown):

```
Do Not Hire - Soft skills low
Do Not Hire - Tech skills low
Do Not Hire - Tech and Soft skills low
Hire
```

---

b. How would your logic change if the program only needed to output one of the following? (explain in detail or show code)

```
Hire
Do Not Hire
```

---

# 13 Calling Functions

Given the following functions: `display_menu()`, `get_random_number`, `print_square`, and `multiply`, 

Complete the following Python code in Main to use (ie. call) each of the functions as specified. **Do Not Modify the Functions**.

```python
# *** do not modify the functions ***

def display_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Quit")

def get_random_number():
    import random
    return random.randint(1, 10)

def print_square(number):
    print(number * number)

def multiply(a, b):
    return a * b

# *** do not modify the functions ***

# main

# a. Use the display_menu function to display a menu ie. 1. Add, 2 Subtract ...

# b. Use the get_random_number to assign a random number to variable spin

# c. Display the square of 50 using the print_square function

# d. Display 16 x 256 using the multiply function

```

---

# 13. modules and main

Consider the following two files.

### File: `program1.py`

```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()
````

### File: `program2.py`

```python
import program1
print("Done")
```

---

### Questions

a. What is printed when `program2.py` is executed?

b. What is printed when `program1.py` is executed?


-- end --




