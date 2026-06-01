"""Write a program that calculates the perimeter 
and area of a triangle, using the formulas 
P = a + b + c and A = (b * h) / 2, where a, b and c 
are the sides of the triangle and h is the height
relative to the side B."""

def get_number(prompt):
	"""Returns the valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Try to enter a number")
			

def get_perimeter(a, b, c):
	"""Calculates the perimeter of triangle"""
	
	return a + b + c

	
def get_area(b, h):
	"""Calculates the area of triangle"""
	
	return (b + h) / 2
			

a = get_number("Enter the length of side a: ")
b = get_number("Enter the length of side b: ") 
c = get_number("Enter the length of side c: ")
h = get_number("Enter the height relative to side b: ")

perimeter = get_perimeter(a, b, c)
area = get_area(b, h)

print(f"Perimeter of triangle: {perimeter:.2f}")
print(f"Area of triangle: {area:.2f}")
