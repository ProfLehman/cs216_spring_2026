
# password_v2.py
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
        
        #if d == "0" or d == "1" or d == "2" or d == "3" or d == "4" or d == "5" or d == "6" or d == "7" or d == "8" or d == "9":
        if d.isdigit() == True:
            found_number = True
    
        x = x + 1
        
    if found_number == False:
        valid = False
        print("Need Number")
  
  
  
    # check for special character
    found_special = False
    x = 0
    while found_special == False and x < len(password):
        
        d = password[x]
        
        if d.isalnum() == False:
            found_special = True
    
        x = x + 1
        
    if found_special == False:
        valid = False
        print("Need Special Character - not a letter or number")
        
        
    # check for upper and lower case
    found_upper = False
    found_lower = False
    x = 0
    while x < len(password):
        
        # check for upper case
        if password[x].isupper() == True:
            found_upper = True;
            
        # check for upper case
        if password[x].islower() == True:
            found_lower = True;
        
        x = x + 1
        
    if found_upper == False:
        valid = False
        print("Need upper case")

    if found_lower == False:
        valid = False
        print("Need lower case")


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


