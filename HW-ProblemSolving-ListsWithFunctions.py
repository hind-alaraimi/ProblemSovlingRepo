"""
analyze whether a die is fair by counting how often each value
(1, 2, 3, 4, 5, 6) appears
Our input will be a series of die toss values
For example, if the scores are: 1, 2, 1, 3, 4, 6, 5, 6
The result is 1: 2; 2: 1; 3: 1; 4: 1; 5: 1; 6: 2
"""
lst = [1, 2, 1, 3, 4, 6, 5, 6]
c=1
lst.sort()
dict1 = {}
for i in lst:
    if(i in dict1.keys()):
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)