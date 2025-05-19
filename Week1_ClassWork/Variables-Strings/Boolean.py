"""temp = -10
if temp > 0 and temp < 100:
    print("Liquid")
elif temp <=0:
    print("Ice")
else:
    print("Gas")

attending = True
grade = 59
if (not attending or grade < 60):
    print("drop")
    
if (attending and grade >= 60):
    print("stay")
    
userpass = input("Eter user password: ")
filepass = "12345"
if userpass != filepass:
    print("Invalid Password")
else:
    print("Login successfully")


#write a program to compare two numbers:
#Equals
#num 1 > num2
#num1 < num2
#close by eachother 'by difference'

num1 = float(input("Enter Number1: "))
num2 = float(input("Enter Number2: "))
Diff = num2 - num1
E = 0.05

if(num1 == num2):
    print("Numbers are Equals")
elif(abs(Diff) <= E):
    print(num1,"and",num2,"are close to eachother")
elif(num1 > num2):
    print(num1,"is greater")
elif(num1<num2):
    print(num2,"is greater")
"""
    
frozen = False
if (frozen == True):
    print("frozen is true")
    
if (not frozen == True):
    print("frozen is false")
