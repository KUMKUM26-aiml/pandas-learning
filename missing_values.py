import numpy as np
import pandas as pd

data={
    "name":["kumkum","kunal",np.nan,"sumit"],
    "roll":[67,54,np.nan,43],
    "marks":[89,np.nan,54,75]
}

df=pd.DataFrame(data)
#detect misssing values
print(df.isnull())

#missing marks 
missing=pd.isna(df["marks"])
print(missing)

#filling missing values with 0
print(df.fillna(0))

#filling missing marks with average
average=df["marks"].mean()
print(df['marks'].fillna(average,inplace=True))
