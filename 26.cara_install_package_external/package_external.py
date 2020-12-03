import numpy as np
from PIL import Image
a = np.array([1,2,3,4,5,6,])
b = np.array([7,8,9,10,2,3])

print(a + b)

a = Image.open("poto.jpg")

print("format file :" + a.format)

a.show()