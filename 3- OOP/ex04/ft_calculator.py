class calculator:
	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		res = 0
		for i in range(len(V1)):
			res += V1[i] * V2[i]
		print("Dot product is:", res)

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		res = []
		for i in range(len(V1)):
			res.append(float(V1[i] + V2[i]))
		print("Add vector is:", res)
	
	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		res = []
		for i in range(len(V1)):
			res.append(float(V1[i] - V2[i]))
		print("Add vector is:", res)