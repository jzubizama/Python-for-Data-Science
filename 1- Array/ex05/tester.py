from pimp_image import ft_grey, ft_red, ft_green, ft_blue, ft_invert
from load_image import ft_load

array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)

