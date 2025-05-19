import numpy as np

student_grades = np.array([
    [90,80,77],
    [70,50,40],
    [100,100,100]
])
"""
studentavg = np.mean(student_grades,axis=1)
print(studentavg)
highestSub = np.max(student_grades,axis=0)
print(highestSub)

TotalAverage = np.mean(studentavg)
print(TotalAverage)

A = np.array([1,2,3,4])
B = np.array([100,200,300,400])

condition = np.array([True,False,True,False])

answer2 = np.where(condition,A,B)

print(answer2)
"""
import random
from numpy.random import randn
arr = randn(5,5)
np.where(arr< 0,0,arr)
"""
print(arr.sum(1))
print(arr.sum(0))

print(arr.any())
"""
sales =np.array([20,31,2,0,55])
print(np.sort(sales))

countries = np.array([
    'USA', 'Canada', 'Brazil', 'Germany', 'Japan',
    'USA', 'Egypt', 'France', 'India', 'South Africa',
    'Germany', 'Brazil', 'India'
])
print(np.unique(countries))

arr1 = np.array(['USA', 'Germany', 'Egypt'])
arr2 = np.array(['Germany', 'India', 'Egypt', 'France'])

arr = np.array([1,10,0,-3,0.5],'bool')
print(arr)