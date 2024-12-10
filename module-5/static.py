class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Example usage
result1 = MathOperations.add(10, 20)  # Static method called directly using the class
result2 = MathOperations.multiply(5, 4)

print("Addition:", result1)           # Output: Addition: 30
print("Multiplication:", result2)     # Output: Multiplication: 20
