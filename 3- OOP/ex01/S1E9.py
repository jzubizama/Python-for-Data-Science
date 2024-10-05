from abc import ABC, abstractmethod

class Character(ABC):
	"""Your docstring for Class"""
	@abstractmethod
	def __init__(self, name, is_alive = True):
		'''Your docstring for Constructor'''
		if not isinstance(name, str):
			raise TypeError("name must be a string")
		if not isinstance(is_alive, bool):
			raise TypeError("is_alive must be a boolean")
		self.first_name = name
		self.is_alive = is_alive

	def die(self):
		'''Your docstring for Method'''
		self.is_alive = False

class Stark(Character):
	"""Your docstring for Class"""
    
	def __init__(self, name, is_alive = True):
		'''Your docstring for Constructor'''
		super().__init__(name, is_alive)