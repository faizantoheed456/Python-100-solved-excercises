"""4. Write a program that calculates the geometric mean of three
numbers entered by the user"""

import math 

def get_number(prompt):
	"""Returns the Valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Enter the valid number")
			

def find_geometric_mean(num1, num2, num3):
	"""Computes the geometric mean of three numbers"""
	
	product = num1 * num2 * num3 
	return math.pow(product, 1/3)
	
num1 = get_number("Enter a number: ")
num2 = get_number("Enter a number: ")
num3 = get_number("Enter a number: ")

gm = find_geometric_mean(num1, num2, num3)

rounded = round(gm, 2)

print(f"Geometric mean of three number is {rounded:.2f}")
