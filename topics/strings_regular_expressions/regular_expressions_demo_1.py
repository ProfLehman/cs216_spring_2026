
# regular_expressions_demo_1.py
# prof. lehman
# spring 2026
#
# demonstrates regular expressions for pattern matching

# -------------------------------------------------
# Regular Expressions (Regex) Quick Summary
# -------------------------------------------------
# Regular expressions are used to describe patterns in text.
# In Python, we use the built-in "re" module.

# import re


# -------------------------------------------------
# Basic Character Patterns
# -------------------------------------------------

# \d        → Any digit (0–9)
# [0-9]     → Any digit (same as \d)
# [A-Z]     → Any uppercase letter
# [a-z]     → Any lowercase letter
# [A-Za-z]  → Any letter
# .         → Any single character


# -------------------------------------------------
# Repetition (Quantifiers)
# -------------------------------------------------

# {3}   → Exactly 3 times
# {2}   → Exactly 2 times
# *     → 0 or more times
# +     → 1 or more times

# Examples:
# \d{3}        → Exactly 3 digits
# [A-Z]{2}     → Exactly 2 capital letters
# [A-Z]\d{2}   → One capital letter followed by 2 digits


# -------------------------------------------------
# Matching the Entire String
# -------------------------------------------------

# re.fullmatch(pattern, text)
# The ENTIRE string must match the pattern.

# Example:
# pattern = r"\d{3}"
# re.fullmatch(pattern, "123")    → MATCH
# re.fullmatch(pattern, "1234")   → no match

# Always put an "r" in front of regex patterns:
# pattern = r"\d{3}"

# The "r" means raw string.
# It prevents Python from misinterpreting backslashes.



import re

# match exactly x3 digits
pattern = r"\d{3}"
print("regular expression pattern: ", pattern)
print()

test_values = ["123", "000", "12", "1234", "abc", "12a", "0", "987"]

for value in test_values:
    if re.fullmatch(pattern, value):
        print(f"{value} is MATCH")
    else:
        print(f"   {value} is NOT MATCH")

print()
print()

# match upper case letter followed by two digits
pattern = r"[A-Z]\d{2}"
print("regular expression pattern: ", pattern)
print()

test_values = ["A12", "Z99", "AA12", "A123", "a12", "B7"]

for value in test_values:
    if re.fullmatch(pattern, value):
        print(f"{value} is MATCH")
    else:
        print(f"   {value} is NOT MATCH")
        
print()
print()


# more examples

# Pattern for zip code?  XXXXX
# Pattern for zip with extension? XXXXX-XXXX
# Pattern for phone number: (123) 456-7890
pattern = r"\(\d{3}\) \d{3}-\d{4}"








