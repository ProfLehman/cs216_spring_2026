class Travel:
    
    def __init__(self, city="undefined", miles=-1):
        self.city = city
        self.miles = miles

    def get_kilometers(self):
        return 1.6 * self.miles
        
    def __str__(self):
        return f"city {self.city} {self.miles} miles"
    
    
# main

paris = Travel("Paris", 2456)
print( paris )
print( paris.get_kilometers() )

berlin = Travel("Berlin", 2700)
print( berlin )
print( berlin.get_kilometers() )

fw = Travel("Fort Wayne", 27)
print( fw )
print( fw.get_kilometers() )


