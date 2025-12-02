# sorting 
#  
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print(data["Name"])

# Sorting by Age
sorted_by_age = df.sort_values(by='Age')
print("\nDataFrame sorted by Age:")
print(sorted_by_age)
# Subsetting rows where Age > 25
subset_age_gt_25 = df[df['Age'] > 25]
print("\nSubset of DataFrame where Age > 25:")
print(subset_age_gt_25)
# Subsetting rows where City is 'Chicago'
subset_city_chicago = df[df['City'] == 'Chicago']
print("\nSubset of DataFrame where City is 'Chicago':")
print(subset_city_chicago)
# Subsetting specific columns (Name and City)
subset_name_city = df[['Name', 'City']]
print("\nSubset of DataFrame with only Name and City columns:")
print(subset_name_city)
# Combining subsetting conditions (Age > 25 and City is 'Phoenix')

subset_combined = df[(df['Age'] > 25) & (df['City'] == 'Phoenix')]
print("\nSubset of DataFrame where Age > 25 and City is 'Phoenix':")
print(subset_combined)

# concept  to remember
# .sort_values() is used to sort the dataframe by a specific column
# Subsetting can be done using boolean indexing
# Multiple conditions can be combined using & (and) and | (or) operators
# Specific columns can be selected by passing a list of column names
# Always use parentheses when combining multiple conditions to ensure correct evaluation order

# we use single [] when we are selecting a single column
# we use double [[]] when we are selecting multiple columns
# Example:
single_column = df['Name']  # Single column
multiple_columns = df[['Name', 'City']]  # Multiple columns
print("\nSingle Column (Name):")
print(single_column)
print("\nMultiple Columns (Name and City):")
print(multiple_columns)
# Remember to install pandas library if you haven't already
# You can install it using pip:
