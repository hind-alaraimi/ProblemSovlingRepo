import numpy as np

# Lst = [1,2,3,4]
# #print(Lst)
# arr = np.array(Lst[:len(Lst)-1])
# #print(arr)

# #print(arr.dtype)

# LS2 = [11,22,33,44]
# #print(LS2)

# lST3 = [Lst,LS2,[5,10,15,20]]
# arr2 = np.array(lST3[::-1])
# #print(arr2)

# #print(arr2.shape)

# zerosArr = np.ones([2,4],'bool')
# v = 1
# print(zerosArr)
# print(bool(v))

# print(np.empty(5))
# print(np.eye(5))

# print(np.arange(arr))
# ProdArr1 = arr2*arr2
# print(ProdArr1)
# arr **= 3
# print(arr)

# arr6 = arr2.transpose()
# print(arr2)

# print(arr6)


# # Dot function:
# A = [[1,2],[3,4]]
# B = [[3,5],[6,7]]
# print (np.dot(A,B))

# a1 = np.array([1,3,5])
# a2 = np.array([2,4,6])
# print("Addition:",a1+a2)
# print("Subtraction:",a1-a2)
# print("Multiplication:",a1*a2)
# print("Division:",a1/a2)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.reshape(2,3,2))


# Lst = [[1, 2, 3], [4, 5, 6]]
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# for i in Lst:
#     print(i)


# arr2 = np.array([[1, 2, 3], [4, 5, 6]])

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2[:])
for i in arr2:
    print(i)

arr2[:][:1] = 50
print(arr2)
"""

"""
ARR = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(ARR)
print(ARR[0][2])

print(ARR[0,2])

arr3 = np.array([1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12])
arr2 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9], [10, 11, 12]])
print(arr2)
print(arr2[2::,2::])

print(arr3.reshape(2,6))

grid = np.arange(16).reshape(4,4)
print(grid)

print(np.vsplit(grid,[3])) # starting index 2 'Vertically'
print(np.hsplit(grid,[4])) # starting index 2 'Horizontally'


TotalGrades = 0
avg = 0
tAvg = 0
Grades = np.array([[89,77,85],[94,91,78],[88,65,77]])
for i in range(3):
    print(f"student({i+1}):")
    for j in range(3):
        TotalGrades += Grades[i][j]
        avg = sum(Grades[i])/len(Grades[i])
        if (Grades[i][j] == max(Grades[i])):
            print(f"Average marks for student{i}:",avg)
            print("Highest mark: ",max(Grades[i]))
        print()
print("Average grades across all students: ",np.mean(Grades))
