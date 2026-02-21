import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")

print("1st 5 row: ")
print(df.head())

print("\ncolumn names: ")
print(df.columns)

print("\nshapeof data :")
print(df.shape)

print("\ninfo")
print(df.info())