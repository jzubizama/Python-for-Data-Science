def check_list(family: list) -> bool:
	'''Function that checks the 2D list
	Args:
		family (list): 2D list
	'''
	if (type(family) != list or len(family) == 0 or type(family[0]) != list):
		return False
	y = len(family[0])
	for i in family:
		if (type(i) != list):
			return False
		if (len(i) != y):
			return False
	return True
		


def slice_me(family: list, start: int, end: int) -> list:
	'''Function that slices a 2D list
	Args:
		family (list): 2D list
		start (int): starting index
		end (int): ending index
	Returns:
		list: sliced 2D list
	Error:
		returns an empty list if the family list is not a 2D list
	'''
	if (not check_list(family)):
		return []
	print("My shape is: (%d, %d)" % (len(family), len(family[0])))
	x = slice(start, end)
	new_family = family[x]
	print(f"My new shape is: (%d, %d)" % (len(new_family), len(new_family[0])))
	return new_family
