"""Write a program that calculates the area of a circle from the
radius, using the formula A = πr²"""

import math

def get_number(prompt):
	"""Returns the Valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Enter the valid number")
			
def area_circle(radius):
	"""Computes the area of a circle"""
	
	return math.pi * (radius ** 2)
	
radius = int(get_number("Enter the radius of circle: "))

area_of_circle = area_circle(radius)

print(f"Area of circle: {area_of_circle:.2f}")
