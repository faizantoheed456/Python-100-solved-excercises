"""Write a program that reads the x and y position of two
points in the Cartesian plane, and calculates the distance
between them."""

import math

def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_distance(x1, y1, x2, y2):
	"""Calculates the distance between two points"""
	
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	
	            
x1 = get_number("Enter the x-coordinate of point 1: ")
y1 = get_number("Enter the y-coordinate of point 1: ")

x2 = get_number("Enter the x-coordinate of point 2: ")
y2 = get_number("Enter the y-coordinate of point 2: ")

distance = get_distance(x1, y1, x2, y2)

print(f"Distance between two points: {distance:.2f}")
