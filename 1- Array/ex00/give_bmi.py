def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	'''Function that returns the calculated BMI list given the height and weight lists
	Args:
		height (list[int | float]): list of heights
		weight (list[int | float]): list of weights
	Returns:
		list[int | float]: list of calculated BMI values
	Error:
		returns an empty list if the length of the height and weight lists are not equal
	'''
	if len(height) != len(weight):
		return []
	bmi = []
	for i in range(len(height)):
		bmi.append(weight[i] / (height[i] ** 2))
	return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	'''
	Function that returns a list of boolean values based on the BMI values and the limit
	Args:
		bmi (list[int | float]): list of BMI values
		limit (int): limit value
	Returns:
		list[bool]: list of boolean values
	'''
	return [b >= limit for b in bmi]
