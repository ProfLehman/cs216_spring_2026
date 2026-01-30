from grade_eval import *

# grade_eval_test.py
#
# your name
# spring 2026
#
# test functions that return values in grade_eval.py


# helper function
def header(functionName):
    print()
    print()
    print("+---------------------------+")
    print("+  testing:", functionName)
    print("+---------------------------+")
    print()

"""
# --------------------------------------------
# --- grade_percentage(attendance, exams, assignments)
# --------------------------------------------

header("grade_percentage(attendance, exams, assignments)")

# Test 1: (95, 89, 92) -> 95(.10) + 89(.50) + 92(.40) = 9.5 + 44.5 + 36.8 = 90.8
expected = 90.8
actual = grade_percentage(95, 89, 92)

if abs(actual - expected) < 0.0001:
    print("Passed: grade_percentage(95, 89, 92) == 90.8")
else:
    print("Failed: grade_percentage(95, 89, 92) should be 90.8")
    print("  expected:", expected)
    print("  actual:  ", actual)
"""

# --------------------------------------------
# --- letter_grade(percent)
# --------------------------------------------

header("letter_grade(percent)")

# Test numbers around A's
expected = "A"
actual = letter_grade(100.0)

if actual == expected:
    print("Passed: letter_grade(100) == 'A'")
else:
    print("Failed: letter_grade(100) should be 'A'")
    print("  expected:", expected)
    print("  actual:  ", actual)
    
expected = "A"
actual = letter_grade(90)

if actual == expected:
    print("Passed: letter_grade(90) == 'A'")
else:
    print("Failed: letter_grade(90) should be 'A'")
    print("  expected:", expected)
    print("  actual:  ", actual)

expected = "A"
actual = letter_grade(90.1)

if actual == expected:
    print("Passed: letter_grade(90.1) == 'A'")
else:
    print("Failed: letter_grade(90.1) should be 'A'")
    print("  expected:", expected)
    print("  actual:  ", actual)
    
expected = "B"
actual = letter_grade(89.9)

if actual == expected:
    print("Passed: letter_grade(89.9) == 'B'")
else:
    print("Failed: letter_grade(89.9) should be 'B'")
    print("  expected:", expected)
    print("  actual:  ", actual)  


expected = "C"
actual = letter_grade(75.0)

if actual == expected:
    print("Passed: letter_grade(75.0 == 'C'")
else:
    print("Failed: letter_grade(75.0) should be 'C'")
    print("  expected:", expected)
    print("  actual:  ", actual)
    
    
expected = "C"
actual = letter_grade(79.95)

if actual == expected:
    print("Passed: letter_grade(79.9 == 'C'")
else:
    print("Failed: letter_grade(79.9) should be 'C'")
    print("  expected:", expected)
    print("  actual:  ", actual)
    

"""
# --------------------------------------------
# --- minimum_grade(grade, category, major)
# --------------------------------------------

header("minimum_grade(grade, category, major)")

# Test 3: CS major course requires C or higher; C should pass
if minimum_grade("C", "major", "CS") == True:
    print("Passed: minimum_grade('C', 'major', 'CS') returned True")
else:
    print("Failed: minimum_grade('C', 'major', 'CS') should return True")
"""