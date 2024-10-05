from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	def __init__(self, name, is_alive = True):
		'''Initializes the King.'''
		super().__init__(name, is_alive)

	def set_eyes(self, eyes):
		'''Sets the eyes color of the King.'''
		self.eyes = eyes

	def set_hairs(self, hairs):
		'''Sets the hairs color of the King.'''
		self.hairs = hairs
	
	def get_eyes(self):
		'''Returns the eyes color of the King.'''
		return self.eyes

	def get_hairs(self):
		'''Returns the hairs color of the King.'''
		return self.hairs