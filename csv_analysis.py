import numpy as np
import pandas as pd
#read csv
df=pd.read_csv('data.csv')
print("original dat")
print(df)

#print 1st 5 row
print(df.head())

print("\n data information")
print(df.info())


# Total students
total_students = len(df)
print("\nTotal students:", total_students)

# Highest marks city-wise
highest=df.groupby('city')['marks'].max()
print(highest)

# lowest marks city-wise
lowest=df.groupby('city')['marks'].min()
print(lowest)

# average marks city-wise
average=df.groupby('city')['marks'].mean()
print(average)

# Check missing values
print("\nMissing values:")
print(df.isnull())

## Fill missing marks with average
average=df["marks"].mean()
missing_values=df['marks'].fillna(average,inplace=True)
print(missing_values)


#Show students city-wise
print(df.groupby('city')['name'].apply(list))


# Save cleaned file
df.to_csv("cleaned_students.csv", index=False)
print("\nCleaned file saved as cleaned_students.csv")


