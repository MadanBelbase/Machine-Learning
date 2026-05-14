# Grouped summary statistics in Pandas
import pandas as pd
 
data = {
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Salary': [50000, 60000, 55000, 70000, 65000, 72000, 68000]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Group by 'Department' and calculate summary statistics for 'Salary'
grouped_stats = df.groupby('Department')['Salary'].agg(['mean', 'median', 'std', 'min', 'max'])
print("\nGrouped Summary Statistics by Department:")
print(grouped_stats)
# Reset index to make 'Department' a column again
grouped_stats_reset = grouped_stats.reset_index()
print("\nGrouped Summary Statistics with Reset Index:")