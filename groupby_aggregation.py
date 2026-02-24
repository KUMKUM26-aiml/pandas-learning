import numpy as np
import pandas as pd

data={
    "Name":["Aman","Riya","Neha","Rahul","sourya","mahi"],
    "Class":["10A","10C","10B","10A","10C","10B"],
    "Marks":[76,87,97,45,71,82]
}
df=pd.DataFrame(data)


#Collect all students of same class together
grouping=df.groupby('Class')['Name'].apply(list)
print(grouping)

#Apply aggregation
summary=df.groupby('Class')['Marks'].agg(['max','mean','count'])
print(summary)

#Show output clearly
print("Original Data")
print(df)

#Grouped Data
print("\nAverage Marks per class")
Average_marks=df.groupby('Class')['Marks'].mean()
print(Average_marks)

#Highest marks per class
print("Highest marks per class")
highest_marks=df.groupby('Class')['Marks'].max()
print(highest_marks)

#Student count per class
print("Student count per class")
Student_count=df.groupby('Class')['Marks'].count()
print(Student_count)
