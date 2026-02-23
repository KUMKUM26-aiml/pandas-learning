import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")

print(df)

#Sort students from lowest marks to highest marks
print(df.sort_values(by="marks",ascending=True))

#Sort students from highest marks to lowest marks
print(df.sort_values(by="marks",ascending=False))


#Sort students in alphabetical order of name
print(df.sort_values(by="name",ascending=True))

#Sort by index
print(df.sort_index())






