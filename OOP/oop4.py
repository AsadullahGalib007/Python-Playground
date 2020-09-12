# Inheritance

class partyAnimal:
	x = 0

	name = ""
	def __init__(self, z):
		self.name = z
		print(self.name, "Created")

	def party(self):
		self.x = self.x +1
		print(self.name,"party count", self.x)


class footBallFan(partyAnimal):
	points = 0
	def touchDown(self):
		self.points = self.points+3
		self.party()
		print(self.name, "points", self.points)


# s = partyAnimal("Galib")
# s.party()

j = footBallFan("Nobody")
j.party()
j.touchDown()