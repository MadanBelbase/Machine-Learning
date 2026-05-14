# manupulations with new columns in pandas DataFrame
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Adding a new column 'Salary' with default values
df['Salary'] = [50000, 60000, 55000, 70000, 65000]
print("\nDataFrame after adding 'Salary' column:")
print(df)