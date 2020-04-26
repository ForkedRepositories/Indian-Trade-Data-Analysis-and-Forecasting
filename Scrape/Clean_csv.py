import pandas as pd

df = pd.read_csv('Year-HSCode-Value_Import.csv')
df = df.dropna(axis=0, subset=['Value'])
df.to_csv('Year-HSCode-Value_Import.csv', header = True, index = False)

df = pd.read_csv('Year-HSCode-Value_Export.csv')
df = df.dropna(axis=0, subset=['Value'])
df.to_csv('Year-HSCode-Value_Export.csv', header = True, index = False)

df = pd.read_csv('Year-Country-Value_Import.csv')
df = df.dropna(axis=0, subset=['Value'])
df.to_csv('Year-Country-Value_Import.csv', header = True, index = False)

df = pd.read_csv('Year-Country-Value_Export.csv')
df = df.dropna(axis=0, subset=['Value'])
df.to_csv('Year-Country-Value_Export.csv', header = True, index = False)