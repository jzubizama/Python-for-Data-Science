import matplotlib.pyplot as plt
import numpy as np

def ft_invert(array) -> np.ndarray:
	'''
 	Inverts the color of the image received.
	'''
	inverted = array.copy()
	inverted[:,:,0] = 255 - inverted[:,:,0]
	inverted[:,:,1] = 255 - inverted[:,:,1]
	inverted[:,:,2] = 255 - inverted[:,:,2]
	plt.imshow(inverted, aspect='auto')
	plt.axis('off')
	plt.show()
	return inverted
 
def ft_red(array) -> np.ndarray:
	'''
	Args:
		array (numpy.ndarray): The image to convert to red.
	Returns:
		numpy.ndarray: The red image.
 	'''
	red = array.copy()
	red[:, :, 1] = 0
	red[:, :, 2] = 0
	plt.imshow(red, aspect='auto')
	plt.axis('off')
	plt.show()
	return red

def ft_green(array) -> np.ndarray:
	'''
	Args:
		array (numpy.ndarray): The image to convert to green.
	Returns:
		numpy.ndarray: The green image.
 	'''
	green = array.copy()
	green[:, :, 0] = 0
	green[:, :, 2] = 0
	plt.imshow(green, aspect='auto')
	plt.axis('off')
	plt.show()
	return green

def ft_blue(array) -> np.ndarray:
	'''
	Args:
		array (numpy.ndarray): The image to convert to blue.
	Returns:
		numpy.ndarray: The blue image.
 	'''
	blue = array.copy()
	blue[:, :, 1] = 0
	blue[:, :, 0] = 0
	plt.imshow(blue, aspect='auto')
	plt.axis('off')
	plt.show()
	return blue

def ft_grey(array) -> np.ndarray:
	'''
	Args:
		array (numpy.ndarray): The image to convert to grey.
	Returns:
		numpy.ndarray: The grey image.
 	'''
	grey = array.copy()
	for i in range(len(grey)):
		for j in range(len(grey[i])):
			r, g, b = grey[i][j]
			a = (r / (1 / 0.299), g / (1 / 0.587), b / (1 / 0.144))
			grey[i][j] = sum(a)
	print(grey)
	plt.imshow(grey, aspect='auto')
	plt.axis('off')
	plt.show()
	return grey