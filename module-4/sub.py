class Substitute:
    def __init__(self, x,y):
        self.x = x
        self.y= y
        
    def __sub__(self,other):
       if isinstance(other,Substitute):
           return Substitute(self.x-other.x, self.y-other.y)
    NotImplemented
    
    def __repr__(self):
        return f"{self.x} {self.y}"
    
sub = Substitute(152,245)
sub2=Substitute(45,56)
result = sub - sub2
print(result)

