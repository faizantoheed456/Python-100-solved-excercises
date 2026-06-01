"""2. Write a program that calculates the arithmetic mean of two
numbers."""

def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

arithmetic_mean = (num1 + num2) / 2

print('Arithmetic mean of two numbers is: ', arithmetic_mean)