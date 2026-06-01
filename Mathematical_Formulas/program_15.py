"""Create a program that prompts the user for the radius of a
sphere and calculates and displays its volume."""

import math

def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_volume(radius):
	"""Calculates the volume of the sphere"""
	
	return (4/3) * math.pi * (radius ** 3)


radius = get_number("Enter the radius of the sphere: ")

volume_of_sphere = get_volume(radius)

print(f"Volume of sphere: {volume_of_sphere:.2f}")
