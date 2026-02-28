import pandas as pd
import matplotlib.pyplot as plt
#Read data
df=pd.read_csv('data.csv')
print(df)

#show first  5 row
print("show first row")
print(df.head())

#handle missing marks
print("\n filling missing marks with average")
df['marks'] = df['marks'].fillna(df['marks'].mean())
print(df)

#function - average marks per city
def average(data):
    return data.groupby('city')['marks'].mean()

# Function- topper per city
def topper(data):
    return data.loc[data.groupby('city')['marks'].idxmax()]

#Function: sort students by marks
def sort_by_marks(data):
    return data.sort_values(by='marks', ascending=False)


print("\n avearge marks per city")
print(average(df))

print("\nTopper Per City ")
print(topper(df))

print("\nStudents Sorted By Marks")
print(sort_by_marks(df))

# Save cleaned file
df.to_csv("cleaned_students.csv", index=False)
print("\nCleaned file saved as cleaned_students.csv")
