"""
for i in range(1,6):
    for j in range(1,5):
        print(i**j,end=" ")
    print()

print()

for i in range(1,6):
    for j in range(1,5):
        if(i%2==0):
            print(" *",end="")
        else:
            print("*",end=" ")
    print()

print()


r=5
for i in range(5):
    print(" "*(r-i),end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

print()


for i in range(3):
    for j in range(5):
        if(j%2 == 1):
            print("*",end="")
        else:
            print("-",end="")
    print()

print()

    
for i in range(3):
    for j in range(5):
        if (i%2 == j%2):
            print("*" ,end="")
        else:
            print(" ",end="")
    print()

print()


for i in range(3):
    for j in range(4):
        print("[]", end="")
    print()

"""

noOfExams = 3
noOfStudents = int(input("Enter Number of student: "))
for i in range(noOfStudents):
    totalMarks=0
    name = input("Enter Student Name: ")
    for j in range(noOfExams):
        markOfExam= float(input("Enter Mark of exam: "))
        totalMarks += markOfExam
    Average = totalMarks/noOfExams
    print(f"{name} got average marks of:{Average}")
    print()


