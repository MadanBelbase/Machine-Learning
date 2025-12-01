# two ways to fitter arrays in numpy

import numpy as np

array_1d = np.array([10, 25, 30, 45, 50, 65, 70, 85, 90, 100])

# Method 1: Boolean Indexing
bool_index = array_1d > 50
print("Boolean Index Array (greater than 50):", bool_index)

filtered_elements_bool = array_1d[bool_index]
print("Filtered elements using Boolean Indexing (greater than 50):", filtered_elements_bool)


# Method 2: Using np.where
indices = np.where(array_1d > 50)
filtered_elements_where = array_1d[indices]
print("Filtered elements using np.where (greater than 50):", filtered_elements_where)
# Both methods yield the same result
# Verify both methods give the same result
assert np.array_equal(filtered_elements_bool, filtered_elements_where)
print("Both methods yield the same result.")
