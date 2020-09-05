class partyAnimal:
	x = 0

	def party(self):
		print(type(self))
		self.x = self.x + 1
		print("So far", self.x)


an = partyAnimal()
an.party()
an.party()
an.party()
print(partyAnimal.x)
print(dir(an))