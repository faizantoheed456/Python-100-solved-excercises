"""Write a program that calculates the delta of a quadratic
equation (Δ = b² - 4ac)."""


def get_number(prompt):
	"""Returns the valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Try to enter a number")
			
def delta_quadratic_equation(a, b, c):
	"""Calculates the delta of a quadratic equation"""
	
	return (b**2) - (4*a*c)
	
	
	
a = get_number("Enter the coefficient a: ")
b = get_number("Enter the coefficient b: ")
c = get_number("Enter the coefficient c: ")

delta = delta_quadratic_equation(a, b, c)

print(f"Δ = {delta:.2f}") 
