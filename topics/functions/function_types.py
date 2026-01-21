# function_types.py
# prof. lehman
# spring 2026
# quick overview of function types and how they are called

# ----------------------
# define functions
# ----------------------

# no arguments, no return
def test_a():
    print("same message, every time ...")
    
# arguments, no return
def test_b(msg):
    print( "msg argument was", msg )
  
# no arguments, has return
def test_c():
    return 2026

# has arguments, has return
def test_d(x, y):
    result = x + y
    return result

# ----------------------
# main - function calls
# ----------------------

# no arguments, no return
# call by using function name and ()
test_a()
test_a()
print()

# arguments, no return
# call by using function name and give argument in ()
test_b("red")
test_b("blue")
print()

# no arguments, has return
# call using function name and (),
# but must print result, store result, or use in some way

# print result
print( test_c() )

# store result and then print
temp = test_c()
print( "value returned was", temp )

# use result in if statement
if test_c() >= 2000:
    print( "result was >= 2000")
else:
    print( "result was < 2000" )

print()

# has arguments, has return
# call using function name and give argument in (),
# but must print result, store result, or use in some way

# print result
print( test_d(100, 300) )

# store result and then print
temp = test_d(400, 500)
print( "value returned was", temp )

# use result in if statement
if test_d(20, 30) >= 35:
    print( "result was >= 35")
else:
    print( "result was < 35")

# -- end --



