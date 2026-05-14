# group by to pivot table 
 
# pivot table is used to summarize and aggregate data in a tabular format.

import pandas as pd 

data = {
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Salary': [50000, 60000, 55000, 70000, 65000, 72000, 68000],
    'Bonus': [5000, 6000, 5500, 7000, 6500, 7200, 6800]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Create a pivot table to summarize average Salary and Bonus by Department

pivot_table = pd.pivot_table(df, values=['Salary', 'Bonus'], index='Department', aggfunc='mean')
print("\nPivot Table - Average Salary and Bonus by Department:")
print(pivot_table)

# Create a pivot table to summarize total Salary by Department and Employee 