class Multiplication:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __mul__(self, other):
         if isinstance(other, Multiplication):
             return Multiplication(self.x*other.x , self.y*other.y)
         NotImplemented
         
    def __repr__(self):
        return f"{self.x} {self.y}"
    
mul = Multiplication(5,8)
mul2=Multiplication(4,5)

result = mul * mul2
print(result)
