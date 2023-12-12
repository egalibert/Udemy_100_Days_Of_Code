import numpy as np

import matplotlib.pyplot as plt
from scipy import misc 
from PIL import Image 
import random

# 1-Dimensional Arrays (Vectors)
my_array = np.array([1.1, 9.2, 8.1, 4.7])
my_array.shape
my_array[2]
my_array.ndim

# 2-Dimensional Arrays (Matrices)
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

# N-Dimensional Arrays (Tensors)
# Challenge:

# How many dimensions does the array below have?
# What is its shape (i.e., how many elements are along each axis)?
# Try to access the value 18 in the last line of code.
# Try to retrieve a 1 dimensional vector with the values [97, 0, 27, 18]
# Try to retrieve a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]

mystery_array = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[7, 86, 6, 98],
							[5, 1, 0, 4]],[[5, 36, 32, 48],[97, 0, 27, 18]]])

mystery_array.ndim # answer is 3
mystery_array.shape # answer is 3, 2, 4
mystery_array[2,1,3]
mystery_array[2,1,:]
mystery_array[:, :, 0]

# Challenge 1
# Use .arange()to createa a vector a with values ranging from 10 to 29.
# You should get this:

# print(a)

# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

a = np.arange(10, 30)
print(a)

# Challenge 2: Use Python slicing techniques on a to:
# Create an array containing only the last 3 values of a
# Create a subset with only the 4th, 5th, and 6th values
# Create a subset of a containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])
# Create a subset that only contains the even numbers (i.e, every second number)

new_array = a[-3:]
new_array = a[3:6]
new_array = a[12:]
new_array = a[::2]
print(new_array)

# Challenge 3:
# Reverse the order of the values in a, so that the first element comes last:
# [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

new_array = a[::-1]
print(new_array)

# Challenge 4:
# Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
print(nz_indices)

# Challenge 5: Use NumPy to generate a 3x3x3 array with random numbers

from numpy.random import random
z = random((3,3,3))
z

# Challenge 6:
# Use .linspace() to create a vector x of size 9
# with values spaced out evenly between 0 to 100 (both included).

x = np.linspace(0, 100, num=9)
print(x)
x.shape

# Challenge 7:
# Use .linspace() to create another vector y of size 9 with values between -3 to 3 (both included).
# Then plot x and y on a line chart using Matplotlib.

y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

# Challenge 8:
# Use NumPy to generate an array called noise with shape 128x128x3 that has random values.
# Then use Matplotlib's.imshow() to display the array as an image.

noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)

# Manipulating Images as ndarrays
img = misc.face()
plt.imshow(img)

# Challenge:
# What is the data type of img?
# Also, what is the shape of img and how many dimensions does it have?
# What is the resolution of the image?

type(img)
img.shape
img.ndim