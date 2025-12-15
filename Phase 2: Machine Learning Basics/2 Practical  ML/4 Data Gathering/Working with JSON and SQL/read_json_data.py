# working with the json and sql 

import pandas as  pd

df = pd.read_json('data.json')
print(df.head())

# reading from  url 
# url = 'https://api.example.com/data.json'
# df_url = pd.read_json(url)



