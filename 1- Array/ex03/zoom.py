from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_grayscale(image):
    """
    Converts an RGB image to a grayscale image using the weighted sum method.

    Args:
        image (numpy.ndarray): The RGB image to convert.

    Returns:
        numpy.ndarray: The grayscale image.
    """
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])

def zoom():
	original = ft_load("animal.jpeg")
	print(original)


	greyscale = rgb_to_grayscale(original)

	x = 100
	y = 430
	sl_x = slice(x, x+400)
	sl_y = slice(y, y+400)
	zoom = greyscale[sl_x, sl_y]
	print("New shape after slicing:", zoom.shape)
	print(zoom)

	# Display the image with pixel scale on the axes
	plt.imshow(zoom, cmap='gray', aspect='auto')
	plt.show()

def main():
	# your tests and your error handling
	try:
		zoom()
		return (0)
	except:
		print("Error in zoom function")
		return (1)
        

if __name__ == "__main__":
	main()