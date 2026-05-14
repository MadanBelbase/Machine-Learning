#  datafranes in python using pandas library

# .head() this is used to display the first 5 rows of the dataframe
# .tail() this is used to display the last 5 rows of the dataframe
#  .info () this is used to display the information about the dataframe
# .shape() this is used to display the shape of the dataframe


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nFirst 5 rows using .head():")
print(df.head())
print("\nLast 5 rows using .tail():")
print(df.tail())
print("\nDataFrame Info using .info():")
print(df.info())
print("\nDataFrame Shape using .shape:")
print(df.shape)
print(df.shape)
