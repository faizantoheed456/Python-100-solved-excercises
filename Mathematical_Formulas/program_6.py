"""6. Create a program that calculates and displays the perimeter
of a circle, prompting the user for the radius."""

import math

def get_number(prompt):
	"""Returns the Valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Enter the valid number")
			
def perimeter_circle(radius):
	"""Computes the perimeter of a circle"""
	
	return 2 * math.pi * radius
	
radius = int(get_number("Enter the radius of circle: "))

perimeter_of_circle = perimeter_circle(radius)

print(f"Perimeter of circle: {perimeter_of_circle:.2f}")
