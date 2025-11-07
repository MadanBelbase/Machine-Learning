import numpy as np   # Import the NumPy library

# Create a 2D list where each inner list = [height (in inches), weight (in pounds), age (in years)]
np_baseball = [
    [74, 180, 25],   # Player 1
    [72, 210, 28],   # Player 2
    [75, 205, 30],   # Player 3
    [78, 220, 24],   # Player 4
    [69, 185, 26]    # Player 5
]

# Convert the list into a NumPy array to use advanced operations
np_baseball = np.array(np_baseball)

# -------------------------
#  BASIC ARRAY OPERATIONS
# -------------------------

print("Full 2D Array (All Data):")
print(np_baseball)

# Shape of the array → (5 rows, 3 columns)
print("\nShape of array:", np_baseball.shape)

# -------------------------
#  COLUMN SELECTION
# -------------------------

# Select only the HEIGHT column (column index 0)
np_height_in = np_baseball[:, 0]
print("\nAll heights (in inches):", np_height_in)

# Select only the WEIGHT column (column index 1)
np_weight_lb = np_baseball[:, 1]
print("All weights (in pounds):", np_weight_lb)

# Select only the AGE column (column index 2)
np_age = np_baseball[:, 2]
print("All ages:", np_age)

# -------------------------
#  ROW SELECTION
# -------------------------

# Select the first row (index 0 → Player 1)
print("\nFirst row (Player 1 data):", np_baseball[0])

# Select the last row (Player 5)
print("Last row (Player 5 data):", np_baseball[-1])

# Select rows 1 to 3 (Players 2 to 4)
print("Rows 1 to 3 (Players 2–4):")
print(np_baseball[1:4])

# -------------------------
#  SPECIFIC ELEMENT SELECTION
# -------------------------

# Height of Player 3 → row 2, column 0
print("\nHeight of Player 3:", np_baseball[2, 0], "inches")

# Weight of Player 4 → row 3, column 1
print("Weight of Player 4:", np_baseball[3, 1], "pounds")

# -------------------------
#  STATISTICAL OPERATIONS
# -------------------------

print("\nMean height (in inches):", np.mean(np_height_in))
print("Median height (in inches):", np.median(np_height_in))
print("Average weight (in pounds):", np.mean(np_weight_lb))
print("Oldest player's age:", np.max(np_age))
print("Youngest player's age:", np.min(np_age))

# -------------------------
#  UNIT CONVERSIONS
# -------------------------

# Conversion factors
conversion = np.array([0.0254, 0.453592, 1])  # inches→meters, pounds→kg, age stays same

# Apply conversion to np_baseball
np_baseball_metric = np_baseball * conversion

print("\nConverted Data (meters, kilograms, years):")
print(np_baseball_metric)

# -------------------------
#  SELECT MULTIPLE COLUMNS TOGETHER
# -------------------------

# Select only height and weight columns
height_weight = np_baseball[:, [0, 1]]
print("\nHeight and Weight columns only:")
print(height_weight)

# -------------------------
#  CONDITIONAL SELECTION
# -------------------------

# Find players taller than 74 inches
tall_players = np_baseball[np_baseball[:, 0] > 74]
print("\nPlayers taller than 74 inches:")
print(tall_players)

# -------------------------
#  SUMMARY
# -------------------------

print("\nSummary:")
print("Heights (inches):", np_height_in)
print("Heights (meters):", np_baseball_metric[:, 0])
print("Weights (pounds):", np_weight_lb)
print("Weights (kg):", np_baseball_metric[:, 1])
