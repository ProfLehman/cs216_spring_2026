# -----------------------------------------------------------------------
#
#        file: Animal.py
#
#      Author: Prof. Lehman
#        Date: March 17, 2025, updated Spring 2026
#
# Description: 'Animal' class with attributes for type, name, and sound,
#               getters and setters for each attribute,
#               a 'speak' method to print the sound,
#               a '__str__' method for formatted output.
#
#               Main demonstrates object creation, 
#               method usage, and attribute modification.
#              
# -----------------------------------------------------------------------
from random import randint

class Animal:

    # constructor
    def __init__(self, species="unknown species", new_name="unknown name", sound="unknown sound"):
        self.species = species
        self.name = new_name
        self.sound = sound
    
    
    # Getters return (ie. get access to) class data
    def get_species(self):
        return self.species
    
    def get_name(self):
        return self.name
    
    def get_sound(self):
        return self.sound
    
    
    # Setters update and change class data
    def set_species(self, species):
        self.species = species
    
    def set_name(self, name):
        self.name = name
    
    def set_sound(self, sound):
        self.sound = sound
    
    
    # other methods
    def speak(self):
        rn = randint(1,3)
        for i in range(0,rn):
            print( f"{self.name} the {self.species} says {self.sound}")
    
    
    # str is a standard method that allows objects to be printed using standard print
    def __str__(self):
        return f"Animal Type: {self.species}, Name: {self.name}, Sound: {self.sound}"


# --- main ---
#
# note: following line ensures this main is only run when Animal.py is run
#       and will not run when Animal class is imported

if __name__ == "__main__":
    
     # instance with initial values specicied
    shep = Animal("Dog", "Shep", "woof ... woof woof")
    print(shep)
    shep.speak()
    print()

    # instance using default values
    maynard = Animal()
    print( maynard )
    maynard.speak()
    print()

    # set values
    maynard.set_species("cat")
    maynard.set_name("Maynard")
    maynard.set_sound("meow, meow ...")
    print(maynard)
    maynard.speak()
    print()

    # create list of animals
    harvey = Animal("rabbit", "Harvey", "nothing")
    bob = Animal("rooster", "Robert", "cockadoodle doo ....")
    finn = Animal("dog", "Finn", "yip, yip ...")
    
    pets = [shep, maynard, harvey, bob, finn]
    
    # process list of animals asking all to "speak"
    for pet in pets:
        print()
        pet.speak()
        #print( pet )







