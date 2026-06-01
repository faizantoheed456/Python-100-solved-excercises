"""Write a program that calculates the average 
velocity of an object, using the formula v = Δs/Δt, 
where v is the average velocity, Δs is the 
space variation, and Δt is the time variation"""

def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
			
			
def get_velocity(space_variation, time_variation):
	"""Calculates the average velocity of object"""
	try: 
		return space_variation/time_variation
	except ZeroDivisionError:
		print("Can't divide by zero")
		return None
		
		
space_variation = get_number("Enter the space variation (Δs): ")
time_variation = get_number("Enter the time variation (Δt): ")

avg_velocity = get_velocity(space_variation, time_variation)

if avg_velocity is not None:
    print(f"Average Velocity: {avg_velocity:.2f}")
else:
    print("Could not calculate average velocity due to invalid time input.")
