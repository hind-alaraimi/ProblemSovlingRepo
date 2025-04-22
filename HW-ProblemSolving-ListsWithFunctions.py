"""
analyze whether a die is fair by counting how often each value
(1, 2, 3, 4, 5, 6) appears
Our input will be a series of die toss values
For example, if the scores are: 1, 2, 1, 3, 4, 6, 5, 6
The result is 1: 2; 2: 1; 3: 1; 4: 1; 5: 1; 6: 2
"""
lst=[]
num = int(input("Enter number of die toss tries: "))
for i in range(num):
    val = int(input("Enter score (1-6): "))
    lst.append(val)
    

lst.sort()
dict1 = {1:0,2:0,3:0,4:0,5:0,6:0}
for i in lst:
    if (i<7 and i>0):
       dict1[i] += 1
    else:
        exit("Inputs out of bounds")
        break

for i in dict1.values():
    print(i,end=" ")
    
    
    
    
    
    