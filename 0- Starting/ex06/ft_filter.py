def ft_filter(func, iterable):
	"""
    Returns a list of elements from the iterable for which the function returns True.
	Simulates the built-in filter() function.
	
    Args:
        func: A function that returns a boolean value.
		iterable: An iterable object.

    Returns:
		A list of elements from the iterable for which the function returns True
    """
	return [x for x in iterable if func(x)]