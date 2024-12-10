# Basic Unpacking
person = ('John', 25, 'Engineer')
name, age, profession = person
print(name, age, profession)  # Output: John 25 Engineer


# Unpacking in loops
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x: {x}, y: {y}")
    
    
from collections import namedtuple

# Define a named tuple class
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p = Point(1, 2)

# Access fields by name
print(p.x, p.y)  # Output: 1 2
