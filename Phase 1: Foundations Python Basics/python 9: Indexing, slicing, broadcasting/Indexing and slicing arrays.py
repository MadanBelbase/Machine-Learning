# indexing and slicing arrays in numpy
import numpy as np

array_2d = np.array([[10, 20, 30, 40],
                        [50, 60, 70, 80],
                        [90, 100, 110, 120],
                        [130, 140, 150, 160]])      

# Accessing specific element (row 2, column 3)
element = array_2d[2, 3]
print("Element at (2,3):", element)
# Accessing entire row (row 1)
row_1 = array_2d[1, :]
print("Row 1:", row_1)
# Accessing entire column (column 2)
column_2 = array_2d[:, 2]
print("Column 2:", column_2)
# Slicing sub-array (rows 1 to 3, columns 1 to 3)
sub_array = array_2d[1:4, 1:4]
print("Sub-array (rows 1-3, columns 1-3):\n", sub_array)

# Modifying specific element (row 0, column 0)
array_2d[0, 0] = 999
print("Modified Array:\n", array_2d)
# Modifying entire row (row 2)
array_2d[2, :] = [1, 2, 3, 4]
print("Modified Array after changing row 2:\n", array_2d)
# Modifying entire column (column 3)
array_2d[:, 3] = [7, 8, 9, 10]
print("Modified Array after changing column 3:\n", array_2d)
# Modifying sub-array (rows 0 to 1, columns 0 to 1)
array_2d[0:2, 0:2] = [[111, 222], [333, 444]]
print("Modified Array after changing sub-array:\n", array_2d)
# Boolean Indexing
bool_index = array_2d > 100
filtered_elements = array_2d[bool_index]
print("Elements greater than 100:", filtered_elements)

# Fancy Indexing
fancy_indexed_elements = array_2d[[0, 2], [1, 3]]
print("Fancy Indexed Elements:", fancy_indexed_elements)