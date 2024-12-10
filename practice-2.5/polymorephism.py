
class Shape:
    
    def area(self):
        pass
    def addition(self):
        pass
    
class Rectangle(Shape):
    def area(self,height,width):
        return height*width
    def addition(self, height,width):
        return height+width
    
rec = Rectangle()

print(rec.area(12,23))
print(rec.addition(120,203))

