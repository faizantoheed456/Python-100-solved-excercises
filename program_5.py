"""5. Write a program that calculates the BMI of an individual,
using the formula BMI = weight / height²"""

def get_number(prompt):
	"""Returns the Valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Enter the valid number")
			
def calculate_bmi(weight, height):
	"""Computes the BMI of an individual"""
	
	return weight / (height ** 2)
	
weight = float(get_number("Enter your weight in kilograms: "))
height = float(get_number("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")
