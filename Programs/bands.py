# importing Image class from PIL package
from PIL import Image

# opening a multiband image (RGB specifically)
im = Image.open(r"D:\IIIT G\SEM 6\DL-Project\Programs\test1.png")
im1 = Image.Image.split(im)

# showing each band
im1[0].save('band1.png')
im1[1].save('band2.png')
im1[2].save('band3.png')