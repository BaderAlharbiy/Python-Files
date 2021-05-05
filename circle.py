# Given a radius vlaue, print the circumference of a circle
# Formula for a circumference is c = pi * 2 * raduis

class Circle:

	def __init__(self,raduis):
		self.raduis=raduis

	def circumference(self):
		pi = 3.14
		circumferenceVlaue = pi * self.raduis * 2
		return circumferenceVlaue
	
	def printCircumference(self):
		myCircumference = self.circumference()
		print("Circumference of a cericle wuth raduis of "+str(self.raduis)
		+ " is "+str(myCircumference))
		
#First instantaion of the Circle class
#circle = Circle(2)
c1 = Circle(2)
print(c1.circumference())
c1.printCircumference()