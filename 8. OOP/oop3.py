#COnstructor and Destructor

class partyAnimal:
	x = 0

	#Whenever an object is created the constructor is called automatically
	def __init__(self):
		print("I am Constructed")

	def party(self):
		self.x = self.x +1
		print("SO far", self.x)

	#Whenever an object is destroyed the destructor is called automatically
	def __del__(self):
		print("I am destructed", self.x)

# Calling Constructor
an = partyAnimal()			#I am Constructed
an.party()					#So far 1
an.party()					#So far 2

#Calling Distructor
an = 42						#I am destructed 2
print("an contains", an)	#an contains 42

#Remember: self is the defined class 'partyAnimal' itself