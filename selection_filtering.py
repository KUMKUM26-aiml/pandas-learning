import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")

#show only name
print(df['name'])

#show only name and marks
print(df[['name','marks']])

#use  loc label based indexing
print(df.loc[0])

#use iloc position based indexing
print(df.iloc[1])

#print  only those who have greater than 70 marks
print(df[df['marks']>70])