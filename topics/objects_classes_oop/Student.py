class Student:
    
    def __init__(self, e1, e2, e3, e4):
        
        self.exam1 = e1
        self.exam2 = e2
        self.exam3 = e3
        self.exam4 = e4
    
    def getAvg(self):
        
        data = []
        data.append( self.exam1 )
        data.append( self.exam2 )
        data.append( self.exam3 )
        data.append( self.exam4 )
        
        lowest = min( data )
        total = sum( data )
        avg = (total - lowest) / 3.0
        
        return avg
    
        
# main
if __name__ == "__main__":
    
    alice = Student(80, 80, 80, 80)
    print( alice.getAvg() )
    