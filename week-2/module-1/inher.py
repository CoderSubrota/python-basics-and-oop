class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class's __init__
        self.age = age
    
    def greet(self):
        parent_greet = super().greet()  # Call the parent class's greet method
        return f"{parent_greet} You are {self.age} years old."

# Create an instance of Child
child = Child("Alice", 10)
print(child.greet())  # Output: Hello, Alice! You are 10 years old.
