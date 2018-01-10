import pandas as pd

s = pd.Series([1,2,3,4], index=['a','b','c','d'])

print(s['b'])

data = {'Country': ['Belgium', 'India', 'Brazil'],
	 'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
	 'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])

print(df)