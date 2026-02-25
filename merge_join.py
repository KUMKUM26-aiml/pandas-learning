import numpy as np
import pandas as pd

student={
    "Name":["divya","ritika","neha","pihu"],
    "roll":[101,102,103,104]
}

Marks={
    "roll":[101,102,103,104,105],
    "marks":[87,76,97,77,54]
}

df1=pd.DataFrame(student)
df2=pd.DataFrame(Marks)

#Merging two data frames with merge() function with the parameters as the two data frames. 
df=pd.merge(df1,df2)
print(df)

#Merging two data frames with merge() function on some specified column name of the data frames
df=pd.merge(df1,df2,on='roll')
print(df)

#Returns only rows with matching keys in both frames
df = pd.merge(df1, df2, on='roll', how="inner")
print(df)

#Returns all rows from the left frame, and only matching rows from the right.
df = pd.merge(df1, df2, on='roll', how='left')
print(df)

# Returns all rows from the right frame, and only matching rows from the left.
df = pd.merge(df1, df2, on='roll', how='right')
print(df)

# Returns all rows from both frames, filling missing values with NaN
df = pd.merge(df1, df2, on='roll', how="outer")
print(df)

#Merging data frames with the indicator value to see which data frame has that particular record.
df = pd.merge(df1, df2, how = 'left', indicator = True)
print(df)

#Merging data frames with the one-to-many relation in the two data frames
df = pd.merge(df1, df2, validate = 'one_to_one')
print(df)
