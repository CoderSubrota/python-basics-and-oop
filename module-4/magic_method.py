class Vector:
    def __init__(self, x,y):
        self.x = x 
        self.y = y
        
    def __add__(self,other):
        if isinstance(other , Vector): #`isinstance` ensures `other` is the expected type, preventing errors when unsupported types are passed, improving robustness and clarity.
            return Vector(self.x + other.x, other.y + self.y)
        return NotImplemented #Returning `NotImplemented` signals Python to try alternative methods, like `other.__radd__`, ensuring proper handling of unsupported operations gracefully.
    def __repr__(self):
        return f"{self.x } {self.y}"
    
vec1 = Vector(2,5)
vec2 = Vector(32,8)
result = vec1 + vec2
print(result)



