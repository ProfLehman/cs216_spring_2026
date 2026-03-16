
# CS 216 Exam #2 sample review problems

Review text ch7, ch8, and ch9, sample code on GitHub, and program assignments. Review Topics List below.

You may use a 1-page front/back help guide (any notes you want to make on 8.5" x 11" (or A4) paper front and back)

The exam will be paper format with questions similar to the samples shown. 


---

# Chapter 7 – Iteration (Loops)

## Basic Loop Concepts
- Purpose of loops (repeating a set of instructions)
- Difference between **while loops** and **for loops**
- Loop initialization, condition, and update
- Infinite loops and how they occur
- Indentation and loop structure in Python

---

## While Loops
- Basic `while` loop structure
- Creating a **counting loop**
- Updating the loop variable
- Sentinel-controlled loops (example: stop when `-1` is entered)
- Input loops that repeat until a condition is met
- Using `break` to exit a loop early

Example concepts:
- Running totals
- Input validation
- Password loops

---

## For Loops
- Basic `for` loop syntax
- Using `range()` with loops
  - `range(stop)`
  - `range(start, stop)`
  - `range(start, stop, step)`
- Counting by values other than 1 (ex: 10, 20, 30…)

---

## Nested Loops
- Loops inside other loops
- Understanding how many times code executes
- Predicting output of nested loops

---

## Loop Control
- `break` statement
- When and why to use `break`

---

## Iterating Over Data
- Looping through **strings**
- Looping through **lists**
- Using `for item in list`
- Using index-based loops

---

# Chapter 8 – Strings

Note: we will not cover Regular Expressions

## String Slicing
- `s[1]`
- `s[1:2]`
- `s[1:]`
- `s[:1]`
- `s[-1]`

## String Functions
- `len(string)`
- `string.find("A")`
- `string.find("A", 1)`
- `"A" in "ABC"`

## String Methods
- `.lower()`
- `.upper()`
- `.capitalize()`
- `.title()`
- `.strip()`
- `.split()`

## Iterating Over Strings
- Using a **while loop**
- Using a **for loop**

---

# Chapter 9 – Lists 

## Creating Lists
- Create an empty list

```python
my_list = []
````

## Setting Items in a List

* Assign a value to a specific index

```python
my_list[0] = 10
```

## Iterating Over Lists

* Using a **while loop**
* Using a **for loop**
* Using **range()**
* Using the **in operator**

## List Methods

* `.append(newitem)`
* `.insert(0, newitem)`
* `.pop()`
* `.pop(0)`
* `.sort()`
* `.reverse()`
* `.index(item)`
* `.count(item)`

## List Functions

* `min(list)`
* `max(list)`
* `sum(list)`


---


## Sample Questions

## 1. while loop

Fill in the blanks such that the numbers **10, 20, 30, 40, 50** will be printed to the screen.  
Use `x` as your counting variable and the `print` statement provided for your output.  
You may not need to use all of the blanks.

```python
x = 10

while x <= 50:  
    
    ___________________

    print(x, end=", ")

    ___________________
    
    # end loop
````

---

## 2. for loops

Fill in the blanks such that the numbers **10, 20, 30, 40, 50** will be printed to the screen.
Use `x` as your counting variable and the `print` statement provided for your output.
You may not need to use all of the blanks.

```python
for ________________________________________________ :  
    
    ______________________________

    print(x, ", ")

    ______________________________
```

---

## 3. Sentinel Loop - total

Show the code needed to **input numbers, keeping a running total, until `-1` is entered**.
Display the total.

**Sample Run**

```
Enter number (-1 to quit)
6
Enter number (-1 to quit)
7
Enter number (-1 to quit)
-1
total 13
```

---

## 4. Sentinel Loop - valid password

Show the code needed to **input passwords until `"Norman"` is entered**.
Display the message **"Wrong Password"** if `Norman` is not entered.

**Sample Run**

```
Enter password
1234
Wrong Password

Enter password
secret
Wrong Password

Enter password
Norman
```

---

## 5. Nested loops

How many times will `"X"` be printed?

```python
for i in range(0,5):
    for j in range(0,10):
        print("x")
```

---


## 6. Predict output

What will be output by the following?

```python
x = 0

while x < 10:
    print(x, end=" ")
    if x == 5:
        break
    x = x + 1
# end loop

print(x)
```

## 7. Strings

Show the output for the following:

```python
s = "python"

print(s[1])           #________________________

print(s[0:2])         #________________________

print(s[:4])          #________________________
 
print(s[4:])          #________________________

print(s[-1])          #________________________

print(len(s))         #________________________

print(s.find("t"))    #________________________

print(s.find("t",4))  #________________________

print(s.capitalize()) #________________________

print(s.upper())      #________________________

print(s)              #________________________

````

---

## 8. Reverse a String

Complete the function `displayReversed` that will take a string and print the word in reverse order.

*Note: Python does not have a `.reverse()` or `.reversed()` method for strings.*

```python
def displayReversed(word):



displayReversed("Ada Lovelace")      # displays ecalevoL adA
displayReversed("Charles Babbage")   # displays egabbaB selrahC
```

---

## 9. Strings - Get Initials

Complete function `getInitials` to return initials for any name passed as an argument.

*Assume the name will have exactly one space between first and last.*

```python
def getInitials(name):



print(getInitials("Ada Lovelace"))      # AL
print(getInitials("Charles Babbage"))   # CB
```

---

## 10. Strings - Count Letters

Complete the function `countLetters` that will return the number of occurrences of `letter` in `name`.

```python
def countLetters(name, letter):


print(countLetters("Charles Babbage", "b"))   # displays 2
print(countLetters("Apple Computer", "p"))    # displays 3
print(countLetters("Apple Computer", "x"))    # displays 0
```

---

## 11. Lists are mutable

Given the following functions, what will be displayed if the code is executed?

```python
def changeIt(x):
    x = -1

def changeList(list):
    list[0] = -1

x = 7
changeIt(x)
print(x) ______________________

y = 7
changeIt(y)
print(y) ______________________

list = [2, 3, 4]
changeList(list)
print(list) ______________________
```

---

## 12. Lists

What will be displayed if the following code is executed?

```python
list = [1] * 1000

print(len(list)) #______________________

print(list[0])   #______________________
```

---

## 13. Lists - exam scores

Given a list of exam scores:

```python
exam = [77, 90, 54, 46, … , 94, 78]
```

Show code needed to **change the 2nd score to 91** after the list is created.

```python
print(exam)  # displays [77, 91, 54, 46 … , 94, 78]
```

---

## 14. Lists = High Score

Show code needed to **display the highest exam score** in the list.

Using the sample list above, the result would be:

```
94
```

---

## 15. Lists - process list

Show code needed to **display all scores that are less than 60**.

Sample output with current list would display:

```
54
46
```

---

## 16. Add to end of list

Show code needed to **add the score 89 to the end of the exam list**.

```python
print(exam)  # displays [77, 91, 54, 46 … , 94, 78, 89]
```

---

## 17. Remove first item from list 

Show code needed to **remove the first score from the list**.

```python
print(exam)  # displays [91, 54, 46 … , 94, 78, 89]
```

---

## 18. List - processing

Show code needed to **add +2 to all exam scores in the list**.

```python
print(exam)  # displays [93, 56, 48 … , 96, 80, 91]
```

---

## 19. List - sort

Show the code needed to **sort the exam list** in ascending order.

```python
print(exam)  # displays [48, 56, 80, …, 91, 93, 96]
```

-- end --