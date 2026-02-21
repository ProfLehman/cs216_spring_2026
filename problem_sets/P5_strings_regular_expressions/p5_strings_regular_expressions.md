# CS216 – Software Development

**Programming Assignment CS 216 P5 – Strings and Regular Expressions**  
**30 points**  
**Due: 5:00 pm, Wednesday, February 27, 2026** 

---
# Part 1. Clean Phone Numbers

Clean and normalize a list of messy 10 digit phone numbers utilizing
* String indexing
* Loops
* Conditionals
* String slicing
* String methods `isdigit()` 

For each phone number:
1. Remove leading spaces.
2. Remove trailing spaces.
3. Remove all non digit characters
4. format using XXX-XXX-XXXX
5. Print "Invalid" for any phone number that does not have exactly 10 digits
6. Print each cleaned name on its own line

**Sample Output**
```
260-555-1234
Invalid
```

**Starter Code**
```python
# --------------------------------
# Exercise 1 – Clean Phone Numbers
# --------------------------------

phones = [
    "(260) 555-1234",
    "260.555.9876",
    "260-555-0000",
    "260  555 4321",
    "  260)555  2468 ",
    "  (260) 555-9999",
    "2605551111",
    "260-55-1234",
    "CALL: 260-555-1212 ext 9",
    "N/A"
]

for phone in phones:
    
    # Step 1: keep only digits

    
    # Step 2: validate length (must be 10 digits, else pring Invalid)
    
    
    # Step 3: if valid format as 260-555-1234 and print
    print(phone)

```

---

# Part 2. Utilizing String Methods to Clean Data 

Clean and normalize a list of messy names utilizing
* String indexing
* Loops
* Conditionals
* String methods `lower()`, `upper()`, `strip()`, and `title()` 

You **may not** use the `split()` method.

For each name:
1. Remove leading spaces.
2. Remove trailing spaces.
3. Reduce multiple internal spaces to a single space.
4. Convert to proper capitalization.
5. Print the cleaned name.

**Sample Output**
```
Moses
David Shepherd
Mary Magdalene
```

**Starting Code**

```python

# ------------------------------------------
# 1. Utiizing String Methods to Clean Data
# ------------------------------------------
names = [
    "  moSes   ",
    "DAVID shepherd",
    "  maRy   magDalene  ",
    "pEter  fIsherman",
    "paUL apostle   ",
    "  estHER queen",
    "joSePh  ",
    "   saMUel prophet",
    "rUTH  gleaner ",
    "  soLoMon   king"
]

for name in names:

    # *** to do - clean data here ***
    print( name )
    
    
    
    # end loop

# ------------------------------------------
```

---

# Part 3: Validate Course Codes Using Regular Expressions

Use a regular expresson pattern to determine if a course code is valid.

Each course code must follow this format:
- 2–4 uppercase letters
- Followed by exactly 3 digits

**Valid Examples**
```
CS111
MATH101
BIO202
HIST300
```

**Invalid Examples**
```
cs111        (lowercase letters)
CS-111       (contains hyphen)
CS11         (only 2 digits)
COMPSCI101   (too many letters)
ENGR10A      (letter at the end)
```

**Pattern Rules**

A valid course code must:
- Start with 2–4 uppercase letters
- End with exactly 3 digits
- Contain nothing else

**Sample Ouput**
```
CS111 - Valid
MATHEMATICS101 - Not Valid
A200 - Not Valid
ma151 - Not Valid
MA151 - Valid
```

**Starter Code**
```python
# ------------------------------------------
# 3. Validate Course Codes (Regex)
# ------------------------------------------

import re

courses = [
    "CS111",
    "MATH101",
    "BIO202",
    "cs111",
    "CS-111",
    "CS11",
    "COMPSCI101",
    "ENGR10A",
    "HIST300"
]

pattern = r""   # *** write your regex pattern here ***

for course in courses:

    # *** use re.fullmatch() to validate ***
    
    print(course)
```

# Submitting your assignment

Host each of the three exercises on GitHub and upload links.

-- end --