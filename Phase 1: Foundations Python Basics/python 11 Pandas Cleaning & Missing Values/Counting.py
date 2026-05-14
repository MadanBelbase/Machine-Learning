# counting 
# Count the number of stores of each store type in store_types
store_counts = store_types["type"].value_counts()
print(store_counts)

# Count the proportion of stores of each store type in store_types
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of stores of each department in store_depts, sorting in descending order
dept_counts_sorted = store_depts["department"].value_counts().sort_values(ascending=False)
print(dept_counts_sorted)

# Count the proportion of stores of each department in store_depts, sorting in descending order
dept_props_sorted = store_depts["department"].value_counts(normalize=True).sort_values(ascending=False)
print(dept_props_sorted)
