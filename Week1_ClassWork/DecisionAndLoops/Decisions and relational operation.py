"""
floorNum = int(input("Enter Number of floor: "))

if(floorNum>13):
    print("Actual Floor: ",floorNum-1)
elif(floorNum == 13):
    print("There's No 13 Floor")
else:
    print("Actual Floor: ",floorNum)

#---------

purchasedPrice = float(input("Enter Purchased Price: "))

if(purchasedPrice<128):
    Discount=0.08
else:
    Discount=0.16

TotalPrice = purchasedPrice - (purchasedPrice * Discount)
print("Total Price is: ",TotalPrice,"$")


floorNum = int(input("Enter Number of floor: "))

AF = floorNum - 1 if floorNum > 13 else floorNum
print(AF)

"""
from math import sqrt
MSG1 = "HELLO"
MSG2 = "Hello"

print(MSG1 == MSG2)
print(MSG1 == str.upper(MSG2))

print(2==2.00000000000001)

x= sqrt(2)
y = 2

print(round(x*x,5) == y)
print (x*x)
print(y)

print("-QI">"PP")















