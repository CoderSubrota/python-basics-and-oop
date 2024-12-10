from math import pi

class Shape:
    def area(self):
        pass
    
class Triangle(Shape):
    def __init__(self, height,width):
     self.height=height
     self.width=width
     
    def area(self):
     return 1/2*(self.height * self.width)
 
class Rectangle(Shape):
    def __init__(self, height,width):
       self.height = height
       self.width = width
       
    def area(self):
      return self.height * self.width 
  
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
       return pi*self.radius*self.radius
   
triang = Triangle(45,23) 
print(triang.area())
rectan = Rectangle(79,45)
print(rectan.area())
circl = Circle(4)
print(circl.area())


         
         