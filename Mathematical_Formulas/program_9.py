"""Write a program that calculates the perimeter and area of a
rectangle, using the formulas P = 2(w + l) and A = wl, where w
is the width and l is the length"""

def get_number(prompt):
	"""Returns the valid data for processing"""
	
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Try to enter a number")
			
			
def get_perimeter(w, l):
	"""Calculates the perimeter of rectangle"""
	
	return 2 * (w + l)
	
def get_area(w, l):
	"""Calculates the area of rectangle"""
	
	return w * l
	
	
w = get_number("Enter width of rectangle: ")
l = get_number("Enter length of rectangle: ")

perimeter = get_perimeter(w, l)
area = get_area(w, l)

print(f"Perimeter of rectangle: {perimeter:.2f}")
print(f"Area of rectangle: {area:.2f}")
