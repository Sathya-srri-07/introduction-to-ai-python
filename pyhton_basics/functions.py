# Functions in Python

# Simple function
def greet():
    print("Hello! Welcome to Python.")


greet()


# Function with parameters
def add(a, b):
    return a + b


result = add(10, 20)
print("Sum:", result)


# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("10 is:", check_even_odd(10))
print("7 is:", check_even_odd(7))
