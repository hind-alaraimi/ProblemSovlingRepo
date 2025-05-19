"""
#Computes the area of rectangle
def area_rec(a,b):
    return a*b

print(area_rec(2,8))

def main():
    sum = 0
    for i in range(11):
        square = i * i
        sum = sum + square
    print(square,sum)

main()

#-----------------

balance = 10000
def withdraw(amount):
    global balance
    if (balance >= amount):
        balance -= amount
    print(balance)
    
withdraw(1800)

def deposite(amount):
    global balance
    balance += amount
    print(balance)
    
deposite(1800)
"""
#Simple Greeting Function 
def greet(name):
    print(f"Hello, {name}! Welcome to Python")

greet("Hind")
greet("Eman")

#Addition Function 
def add(a,b):
    return a+b
print("Addition =",add(5,3))

#Temperature Converter 
def celsius_to_fahrenheit(Cel):
    return (Cel * (9/5)) + 32
print("Temperature is:",celsius_to_fahrenheit(21))

#Square of a Number
def square(num):
    return num**2
print("Square = ",square(3))

#Check Even or Odd
def is_even(n):
    if(n%2 == 0):
        return True
    else:
        return False
print("Number is even?",is_even(87))









