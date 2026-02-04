
# Exam #1 sample review problems

Sample questions (or slightly modified) from previous exams.

---
Below are the **questions only**, formatted cleanly in **Markdown**, with all code shown in **Python code blocks** and **no answers included**—ready to post as an exam review.

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


