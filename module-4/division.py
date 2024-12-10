class DivClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __truediv__(self,other):
         if isinstance(other, DivClass):
             return DivClass(self.x/other.x, self.y/other.y)
    NotImplemented
    
    def __repr__(self):
        return f"{self.x} {self.y}"
    
divCla = DivClass(41,45)
divCla2=DivClass(12,15)

result = divCla/divCla2
print(result)

