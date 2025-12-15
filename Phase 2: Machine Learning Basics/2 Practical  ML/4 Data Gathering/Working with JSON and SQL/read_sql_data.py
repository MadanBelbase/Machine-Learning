import sqlite3
import pandas as pd

conn = sqlite3.connect("student.db")
df = pd.read_sql_query("SELECT * FROM student_performance", conn)

print(df.head())
print(df.info())
