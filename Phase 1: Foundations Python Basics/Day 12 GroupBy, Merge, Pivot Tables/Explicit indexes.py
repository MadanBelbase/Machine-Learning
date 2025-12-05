# isin use 

import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Values': [10, 20, 15, 25, 30, 10, 20]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Set 'Category' as the index
df_indexed = df.set_index('Category')

print("\nDataFrame with 'Category' as Index:")
print(df_indexed)
# Access data using the explicit index
# loc in Pandas is used to access a group of rows and columns by labels or a boolean array.
# 
value_a = df_indexed.loc['A']

print("\nValues for Category 'A':")
print(value_a)
# Check if specific categories exist in the index
d = df[df['Category'].isin(['A', 'C'])]
print("\nRows where Category is 'A' or 'C':")
print(d)