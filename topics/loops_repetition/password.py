
# password.py
# spring 2026
# prof. lehman
# in-class example for sentinel loops and strings

def valid_password( password ):
    
    valid = True
    
    # check length
    if len(password) < 8:
        valid = False
        print("Need 8+ characters")

    # check for number
    found_number = False
    x = 0
    while found_number == False and x < len(password):
        d = password[x]
        if d == "0" or d == "1" or d == "2" or d == "3" or d == "4" or d == "5" or d == "6" or d == "7" or d == "8" or d == "9":
            found_number = True
    
        x = x + 1
        
    if found_number == False:
        valid = False
        print("Need Number")


    return valid


# --- main ---

# priming the loop
password = input("Enter password: ")

while valid_password( password ) == False:
    
    print()
    print("Invalid Password")
    
    password = input("Enter password: ")
    
    # end loop

# note: only way to get to this code is if password is valid
print("Valid Password")


