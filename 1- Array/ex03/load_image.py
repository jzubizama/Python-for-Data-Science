import matplotlib.pyplot as plt
import numpy as np

def chech_image(path: str) -> bool:
	'''
	Check if the file is an image.
	:param path: The path to the image file.
	:return: True if the file is an image, False otherwise.
	'''
	try:
		img = plt.imread(path)
		return True
	except:
		return False

def ft_load(path: str) -> np.ndarray:
	'''
	Load an image from a file into a numpy array.
	:param path: The path to the image file.
	:return: The numpy array of the image.
	'''
	try:
		img = plt.imread(path)
		print("The shape of image is:", img.shape)
		return img
	except:
		print("Error loading the image.")
		return None