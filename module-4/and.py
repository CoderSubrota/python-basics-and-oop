class AndClass:
    def __init__(self, x):
        self.x = set(x)
        
    def __and__(self,other):
       if isinstance(other,AndClass):
           return AndClass(self.x and other.x)
    NotImplemented
    
    def __repr__(self):
        return f"{self.x}"
    
andCla = AndClass([10,20,30,40,50])
andCla2=AndClass([10,20,30,40,50])

result = andCla and andCla2
print(result)

