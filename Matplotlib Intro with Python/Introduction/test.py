import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('data.xlsx')
 
X = list(df['X'])
Y = list(df['Y'])
print(df)
print(X)
print(Y)