# Slicing and subsetting with .loc and .iloc 

#slicing lists

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Using .loc to slice by labels
loc_slice = df.loc[1:3, ['Name', 'City']]
print("\nSlicing with .loc (rows 1 to 3, columns 'Name' and 'City'):")
print(loc_slice)