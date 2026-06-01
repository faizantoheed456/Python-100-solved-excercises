"""1. Write a program that prompts the user for two numbers and
displays the addition, subtraction, multiplication, and division
between them."""

def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def divison_Case():
    """Handling the Division error"""
    try:
        print(f"Divison of {num1} and {num2} is: {num1 / num2}")
    except ZeroDivisionError:
        print('Can\'t be divided by zero')

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"Addition of {num1} and {num2} is: {addition}")
print(f"Subtraction of {num1} and {num2} is: {subtraction}")
print(f"Multiplication of {num1} and {num2} is: {multiplication}")
divison_Case()
