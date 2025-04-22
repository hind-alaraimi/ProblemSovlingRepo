#Problem 4:
matrixSize = int(input("Enter Matrix size: "))
lst =[]
for i in range(matrixSize):
    Inlst =[]
    for j in range(matrixSize):
        num = int(input("Enter values: "))
        Inlst.append(num)
    lst.append(Inlst)

for i in lst:
    print(i)

sumDig1 = 0
sumDig2 = 0
Diff = 0
for i in range(len(lst)):
    sumDig1 += lst[i][i]
    sumDig2 += lst[i][2-i]
Diff = abs(sumDig1 - sumDig2)
#print(sumDig1)
#print(sumDig2)
print(Diff)
