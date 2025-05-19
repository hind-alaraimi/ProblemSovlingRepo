#Problem 1:
name = "Hind"
age = 24
height = 1.6
print(f"Hello, my name is {name}. I am {age} years old and my height is {height} meters")

#Problem 2:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Addition: ",num1+num2)
print("Subtraction: ",num1-num2)
print("Multiplication: ",num1*num2)
print("Division: ",num1/num2)

#Problem 3:
a = 3
b = 5.5
c = "Oman"

print("The type of variable a is ",type(a))
print("The type of variable b is ",type(b))
print("The type of variable c is ",type(c))

#Problem 4:
length = int(input("Length: "))
width = int(input("Width: "))
area = length * width
print(f"The area of the rectangle is {area}")

#Problem 5:
principal = int(input("Enter Principal amount: "))
rate = int(input("Enter Rate of Interest: "))
timeYears = int(input("Enter Time (in years): "))
simpleInterest = (principal*rate*timeYears)/100
print("The Simple Interest is",simpleInterest)