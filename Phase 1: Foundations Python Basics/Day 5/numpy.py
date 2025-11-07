import numpy as np   # Importing the NumPy library for numerical operations

# Create a 2D list (list of lists) where:
# Each inner list represents a player’s [height (in inches), weight (in pounds), age (in years)]
np_baseball = [
    [74, 180, 25],
    [72, 210, 28],
    [75, 205, 30]
]

# Convert the list to a NumPy array
# This allows us to use NumPy operations like slicing and math functions
np_baseball = np.array(np_baseball)

# Extract the first column (heights) from np_baseball
# : → means all rows
# 0 → means the first column
np_height_in = np_baseball[:, 0]

# np_height_in now contains only the height values:
# Example: array([74, 72, 75])

# Calculate and print the mean (average) of the height values
print("Mean height (in inches):", np.mean(np_height_in))

# Calculate and print the median (middle value) of the height values
print("Median height (in inches):", np.median(np_height_in))
