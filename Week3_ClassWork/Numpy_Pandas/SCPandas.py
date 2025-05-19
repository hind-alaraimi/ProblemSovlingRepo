import pandas as pd
StuPerfDF= pd.read_csv('study_performance.csv')
StuPerfDF = StuPerfDF[['gender','lunch','test_preparation_course','math_score','reading_score','writing_score']]
print(StuPerfDF)

print(StuPerfDF.info())
print(StuPerfDF.describe())

print(StuPerfDF.columns)

print(StuPerfDF['math_score'].mean())
print(StuPerfDF['writing_score'].mean())
print(StuPerfDF['reading_score'].mean())

print(StuPerfDF['math_score'][StuPerfDF['lunch'] == 'standard'].mean())
print(StuPerfDF['math_score'][StuPerfDF['lunch'] != 'standard'].mean())


StuPerfDF = StuPerfDF[['test_preparation_course']]
