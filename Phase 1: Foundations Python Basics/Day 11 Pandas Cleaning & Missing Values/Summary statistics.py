 # summary 
# .mean() - calculates the mean (average) of a numerical column.
# .median() - finds the median (middle value) of a numerical column.
# .mode() - returns the mode (most frequent value) of a column.
# .std() - computes the standard deviation, measuring the spread of data points.
#.min() - identifies the minimum value in a numerical column.
#.max() - identifies the maximum value in a numerical column.

import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [50000, 60000, 55000, 70000, 65000]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Calculate summary statistics
mean_age = df['Age'].mean()
median_salary = df['Salary'].median()
mode_age = df['Age'].mode()[0]
std_salary = df['Salary'].std()
min_age = df['Age'].min()
max_salary = df['Salary'].max()
print("\nSummary Statistics:")
print(f"Mean Age: {mean_age}")
print(f"Median Salary: {median_salary}")
print(f"Mode Age: {mode_age}")
print(f"Standard Deviation of Salary: {std_salary}")
print(f"Minimum Age: {min_age}")
print(f"Maximum Salary: {max_salary}")


# cumulative sum 
df['Cumulative_Salary'] = df['Salary'].cumsum()
print("\nDataFrame with Cumulative Salary:")
print(df)
