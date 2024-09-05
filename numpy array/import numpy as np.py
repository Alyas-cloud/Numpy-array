import numpy as np

# Create a NumPy array from a Python list
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)

# Generate arrays of zeros, ones, and random numbers
zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 4))
random_array = np.random.rand(3, 3)

print("Zeros array:\n", zeros_array)
print("Ones array:\n", ones_array)
print("Random array:\n", random_array)

# Array mathematical operations
array2 = np.array([10, 20, 30, 40, 50])
sum_array = array + array2
product_array = array * array2
square_array = np.square(array)

print("Sum of arrays:", sum_array)
print("Product of arrays:", product_array)
print("Square of array:", square_array)

# Basic statistics on arrays
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# Matrix operations
transpose = np.transpose(matrix)
dot_product = np.dot(matrix, np.array([[7], [8], [9]]))

print("Transpose of matrix:\n", transpose)
print("Dot product of matrix:\n", dot_product)

# Reshaping arrays
reshaped = np.reshape(array, (5, 1))
print("Reshaped array:\n", reshaped)

# Indexing and slicing
element = matrix[1, 2]  # Access element at second row, third column
slice_array = array[1:4]  # Get a slice from index 1 to 3

print("Element at [1, 2]:", element)
print("Slice of array:", slice_array)
