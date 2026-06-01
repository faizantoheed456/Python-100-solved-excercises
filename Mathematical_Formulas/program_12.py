"""Write a program that calculates the kinetic 
energy of a moving object, using the formula 
E = (mv²) / 2, where E is the kinetic energy, 
m is the mass of the object, and v is the velocity."""

def get_number(prompt):
    """Returns the numeric input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
            
def get_kinetic_energy(mass, velocity):
	"""Calculates the kinetic energy of the object"""
	
	return (mass * velocity ** 2) / 2
	

mass = get_number("Enter the mass of the object: ")
velocity = get_number("Enter the velocity of the object: ")

kinetic_energy = get_kinetic_energy(mass, velocity)

print(f"Kinetic energy of moving object: {kinetic_energy:.2f}")
