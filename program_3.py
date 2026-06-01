"""3. Create a program that calculates and displays the arithmetic
mean of three grades entered by the user."""

def get_grade(prompt):
    """Returns the numeric input for grades"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Get the three grades from the user
grade1 = get_grade("Enter the first grade: ")
grade2 = get_grade("Enter the second grade: ")
grade3 = get_grade("Enter the third grade: ")

# Calculate the arithmetic mean
mean = (grade1 + grade2 + grade3) / 3

# Display the result
print(f"The arithmetic mean of the three grades is: {mean:.2f}")