import numpy as np

python_list = [1,2,3,4,56,7,8]
array = np.array(python_list)
print(array)

print(type(array))
# Creating a 2D array with 3 rows and 5 columns 
a = np.arange(15).reshape(3, 5) 
print(a)

print(a.shape)  # Output: (3, 5)
print(a.ndim)   # Output: 2 (number of dimensions)
# creating arrays with zeros
zeros_array = np.zeros((2, 4)) # it creates 2D array with 2 rows and 4 columns filled with zeros
print("Zeros Array:\n", zeros_array)


# in numpy array all the elements should be of same data type
b = np.array([1, 2, 3.5, 4])
print(b)
print(b.dtype)
c = np.array([1, 2, 3, 4], dtype='float32')
print(c)
print(c.dtype)
# array operations
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)
print("Exponentiation:", arr1 ** 2)
print("Square Root:", np.sqrt(arr2))
print("Dot Product:", np.dot(arr1, arr2))
print("Sum of elements in arr1:", np.sum(arr1))

print("Mean of elements in arr2:", np.mean(arr2))
print("Standard Deviation of elements in arr1:", np.std(arr1))

# Slicing and Indexing
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:\n", array_2d)
print("Element at (1,2):", array_2d[1, 2])  # Accessing element at row 1, column 2
print("First row:", array_2d[0, :])  # Accessing the first row
print("Second column:", array_2d[:, 1])  # Accessing the second column
print("Sub-array (rows 0-1, columns 1-2):\n", array_2d[0:2, 1:3])  # Slicing sub-array
# Reshaping Arrays
original_array = np.arange(12)  # Create a 1D array with values from 0 to 11
reshaped_array = original_array.reshape(3, 4)  # Reshape to 3 rows and 4 columns
print("Original Array:", original_array)
print("Reshaped Array (3x4):\n", reshaped_array)
# Flattening Arrays
flattened_array = reshaped_array.flatten()  # Convert back to 1D array
print("Flattened Array:", flattened_array)

# Transposing Arrays