# Chapel.py
# spring 2026
# prof. lehman
#
# Chapel class to track required chapel attendance
#

class Chapel:
    
    def __init__(self):
        # total chapels required (can adjust as needed)
        self.required = 30
        self.completed = 0

    def set_chapels(self, number):
        """
        Set the number of chapels completed
        """
        if number < 0:
            self.completed = 0
        else:
            self.completed = number

    def get_remaining(self):
        """
        Return a message showing remaining chapels
        """
        remaining = self.required - self.completed
        
        if remaining <= 0:
            return "All chapel requirements completed!"
        elif remaining <= 2:
            return f"Very close!!! {remaining} to go ..."
        else:
            return f"You need {remaining} more chapels."
     
    def __str__(self):
        return f"Completed = {self.completed}"
     
     
# -----------------------------------------------------
# Local test (runs only if file is executed directly)
# -----------------------------------------------------
if __name__ == "__main__":
    
    #print("Chapel Class Test")
    #print("------------------")
    
    chapel_helper = Chapel()
    
    print( chapel_helper )
    
    chapel_helper.set_chapels( -15 )
    print( chapel_helper )
    
    chapel_helper.set_chapels( 30 )
    print( chapel_helper )
    print( chapel_helper.get_remaining() )
    
    
    
    # test loop
    number = int(input("Enter number of chapels attended (-1 to quit): "))
    
    while number != -1:
        chapel_helper.set_chapels(number)
        
        answer = chapel_helper.get_remaining()
        print(answer)
        print()
        
        number = int(input("Enter number of chapels attended (-1 to quit): "))
    
    print("Done.")
    
    
    