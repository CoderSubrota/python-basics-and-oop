class OrClass:
    def __init__(self, x):
        self.x = set(x)
        
    def __or__(self,other):
       if isinstance(other,OrClass):
           return OrClass(self.x | other.x)
    NotImplemented
    
    def __repr__(self):
        return f"{self.x}"
    
orCla = OrClass([12,45,65,12])
orCla2=OrClass([10,20,30,40])

result = orCla | orCla2
print(result)

