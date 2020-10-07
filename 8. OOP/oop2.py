#Constructor
class partyAnimal:
	x = 0

	name = ""
	def __init__(self, z):
		self.name = z
		print(self.name, "Created")

	def party(self):
		self.x = self.x +1
		print(self.name,"party count", self.x)


s = partyAnimal("Galib")
# s.party()

# j = partyAnimal("Nobody")
# j.party()

#Remember: self is the defined class 'partyAnimal' itself   