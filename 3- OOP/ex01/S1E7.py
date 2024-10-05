from S1E9 import Character

class Baratheon(Character):
	'''Representing the Baratheon family.'''
	def __init__(self, name, is_alive = True):
		'''Initializes the Baratheon family.'''
		super().__init__(name, is_alive)
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "black"

	def __str__(self):
		'''Returns the string representation of the object.'''
		return "Vector: ({}, {}, {})".format(self.family_name, self.eyes, self.hairs)

	def __repr__(self):
		'''Returns the string repr representation of the object.'''
		return "Vector: ({}, {}, {})".format(self.family_name, self.eyes, self.hairs)

class Lannister(Character):
	'''Representing the Lannister family.'''
	def __init__(self, name, is_alive = True):
		'''Initializes the Lannister family.'''
		super().__init__(name, is_alive)
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"

	def __str__(self):
		'''Returns the string representation of the object.'''
		return "Vector: ({}, {}, {})".format(self.family_name, self.eyes, self.hairs)

	def __repr__(self):
		'''Returns the string repr representation of the object.'''
		return "Vector: ({}, {}, {})".format(self.family_name, self.eyes, self.hairs)
	# decorator
	@staticmethod
	def create_lannister(name, is_alive = True):
		'''Creates a new Lannister instance.'''
		return Lannister(name, is_alive)