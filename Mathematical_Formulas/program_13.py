"""Write a program that calculates the work done by a force
acting on an object, using the formula T = F * d, where T is the
work, F is the applied force, and d is the distance traveled by
the object."""


def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_work(force, distance):
	"""Calculate the work done"""
	
	return force * distance

force = get_number("Enter the applied force: ")
distance = get_number("Enter the distance traveled: ") 

work_done = get_work(force, distance)

print(f"The Work done by the force is: {work_done:.2f}")
