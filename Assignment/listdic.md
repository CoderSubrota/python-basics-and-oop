A/

In Python, a list is an ordered collection of items that can be of any type. It allows duplicate elements and can be accessed by index. Lists are defined using square brackets [].

A dictionary is an unordered collection of key-value pairs, where each key is unique. It is used for mapping relationships between keys and values. Dictionaries are defined using curly braces {} with key-value pairs separated by colons.

Key differences:
- Lists use indices, dictionaries use keys.
- Lists allow duplicates, dictionaries do not allow duplicate keys.

B/

In Python, *args and **kwargs allow passing a flexible number of arguments to a function, making it more versatile.

*args: This allows passing a variable number of positional arguments to a function. The arguments are captured as a tuple, which you can iterate over or access by index. It helps when you don't know the exact number of arguments that will be passed.

Example:

def add_numbers(*args):
    return sum(args)

# Take user input 
numbers = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

result = add_numbers(*numbers_list)
print(f"The sum of the numbers is: {result}")


**kwargs: This allows passing a variable number of keyword arguments to a function, which are captured as a dictionary where the keys are argument names and the values are argument values.

Example:

def greet(**kwargs):
    print(f"Hello, {kwargs.get('name')}")

# Take user input 
name = input("Enter your name: ")
greet(name=name)



Both *args and **kwargs help in creating functions that can handle dynamic inputs.


