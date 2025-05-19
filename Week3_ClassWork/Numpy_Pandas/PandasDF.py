import pandas as pd

empDF = pd.read_csv('employees.csv')
# print(empDF)
#print(type(empDF))

#print(empDF.columns)
# print("Info:")
# print(empDF.info())

# print("Description:")
# print(empDF.describe())

print(empDF[['Age']])
print()
print(empDF[['Name','Age']])
print()
print(empDF[empDF['Salary']>50000])