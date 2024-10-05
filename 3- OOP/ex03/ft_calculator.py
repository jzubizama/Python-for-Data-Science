class calculator:
	def __init__(self, result: list) -> None:
		self.result = result
	#your code here
	def __add__(self, object) -> None:
		for i in range(len(self.result)):
			self.result[i] += object
		print(self.result)
	#your code here
	def __mul__(self, object) -> None:
		for i in range(len(self.result)):
			self.result[i] *= object
		print(self.result)
	#your code here
	def __sub__(self, object) -> None:
		for i in range(len(self.result)):
			self.result[i] -= object
		print(self.result)
	#your code here
	def __truediv__(self, object) -> None:
		if object == 0:
			#raise TypeError("Cannot divide by 0")
			print("Cannot divide by 0")
		else:
			for i in range(len(self.result)):
				self.result[i] /= object
			print(self.result)
	#your code here