import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
print(df)

#group names by city
print(df.groupby('city')['name'].apply(list))

#Average marks per city (bar chart)
average_marks=df.groupby('city')['marks'].mean()
print(average_marks)

average_marks.plot(kind='bar')
plt.xlabel('city')
plt.ylabel("average marks")
plt.title("average marks per city")
plt.tight_layout()
plt.show()


# number of students per city(bar chart)
city_count=df.groupby('city')['name'].count()
city_count.plot(kind='bar')
plt.xlabel('city')
plt.ylabel("total student ")
plt.title("numer of students per city")
plt.tight_layout()
plt.show()


#plot histogram for marks
df['marks'].plot(kind='hist', bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.tight_layout()
plt.show()


# Plot line chart
plt.plot(df.index, df['marks'], marker='o')

plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Line Chart of Marks")
plt.tight_layout()
plt.show()