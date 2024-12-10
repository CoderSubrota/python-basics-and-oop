def add_numbers(*args):
    return sum(args)

# Take user input 
numbers = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

result = add_numbers(*numbers_list)
print(f"The sum of the numbers is: {result}")


def greet(**kwargs):
    print(f"Hello, {kwargs.get('name')}")

# Take user input 
name = input("Enter your name: ")
greet(name=name)
