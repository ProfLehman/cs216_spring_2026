# p2_test.py
# CS216 - P2 Test Cases
# Tests functions in p2.py
#
# Put p2.py and p2_test.py in the same folder
# Run with:
#   python p2_test.py

import p2

print("=== Running P2 Tests ===")
print()

# -------------------------------------------------
# Test 1: calculate_miles
# -------------------------------------------------
print("Test 1: calculate_miles(3000, 28)")
expected = 1.33
actual = p2.calculate_miles(3000, 28)

if abs(actual - expected) < 0.01:
    print("PASS: Test 1")
else:
    print("FAIL: Test 1")
    print("  expected:", expected)
    print("  actual:  ", actual)

print()

# -------------------------------------------------
# Test 2: step_difference
# -------------------------------------------------
print("Test 2: step_difference(3000)")
expected = 7000
actual = p2.additional_steps_needed(3000)

if actual == expected:
    print("PASS: Test 2")
else:
    print("FAIL: Test 2")
    print("  expected:", expected)
    print("  actual:  ", actual)

print()

# -------------------------------------------------
# Test 3: miles_output_line
# -------------------------------------------------
print("Test 3: miles_output_line(3000, miles)")
expected = "You walked 3,000 steps which is 1.33 miles"
actual = p2.miles_output_line(3000, 1.33)

if actual == expected:
    print("PASS: Test 3")
else:
    print("FAIL: Test 3")
    print("  expected:", expected)
    print("  actual:  ", actual)

print()

# -------------------------------------------------
# Test 4: steps_output_line (under)
# -------------------------------------------------
print("Test 4: steps_output_line(7000)")
expected = "You need 7,000 more steps to reach 10,000"
actual = p2.steps_output_line(7000)

if actual == expected:
    print("PASS: Test 4")
else:
    print("FAIL: Test 4")
    print("  expected:", expected)
    print("  actual:  ", actual)

print()

# -------------------------------------------------
# Test 5: steps_output_line (over)
# -------------------------------------------------
print("Test 5: steps_output_line(2500)")
expected = "You were 2,500 steps over 10,000"
actual = p2.steps_output_line(-2500)

if actual == expected:
    print("PASS: Test 5")
else:
    print("FAIL: Test 5")
    print("  expected:", expected)
    print("  actual:  ", actual)

print()

# -------------------------------------------------
# Test 6: steps_output_line (exact)
# -------------------------------------------------
print("Test 6: steps_output_line(0)")
expected = "You walked exactly 10,000 steps"
actual = p2.steps_output_line(0)

if actual == expected:
    print("PASS: Test 6")
else:
    print("FAIL: Test 6")
    print("  expected:", expected)
    print("  actual:  ", actual)

print()
print("=== End of Instructor Tests ===")
print()

# ---- add your tests here ----



