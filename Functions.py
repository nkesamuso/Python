# function definition
# basic mathematical operations
a = 15
b = 5

def birthday():
    print ("Happy birthday Muso")

birthday()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print("Sum:", sum_result)

# Function with default parameter
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")


    


# Mathematical Operations Functions

def add(a, b):
    """
    Add two numbers
    """
    return a + b

def subtract(a, b):
    """
    Subtract b from a
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers
    """
    return a * b

def divide(a, b):
    """
    Divide a by b
    Returns None if division by zero is attempted
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None

def power(base, exponent):
    """
    Calculate base raised to the power of exponent
    """
    return base ** exponent

def modulus(a, b):
    """
    Calculate remainder when a is divided by b
    Returns None if division by zero is attempted
    """
    try:
        return a % b
    except ZeroDivisionError:
        return None

def floor_division(a, b):
    """
    Perform floor division of a by b
    Returns None if division by zero is attempted
    """
    try:
        return a // b
    except ZeroDivisionError:
        return None

def absolute_value(number):
    """
    Return the absolute value of a number
    """
    return abs(number)

# Test the mathematical functions
if __name__ == "__main__":
    # Test cases
    print("\nTesting Mathematical Operations:")
    print(f"Addition: {add(10, 5)}")
    print(f"Subtraction: {subtract(10, 5)}")
    print(f"Multiplication: {multiply(10, 5)}")
    print(f"Division: {divide(10, 5)}")
    print(f"Power: {power(2, 3)}")
    print(f"Modulus: {modulus(17, 5)}")
    print(f"Floor Division: {floor_division(17, 5)}")
    print(f"Absolute Value: {absolute_value(-42)}")