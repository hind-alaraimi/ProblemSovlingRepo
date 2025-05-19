b = 50
r= 1.5
n = 2
Expr = b*(1+r/100)**n
print(Expr)

# real Division (/) & Floor Division (//)
print(7/5)
print(7//5)

# Reminder (MOD %)
print(2%5)


# Find me the even and odd numbers between a & b
print("--Finding even and odd numbers between a & b--")
a = 6
b = 13
for x in range(a,b+1):
    if (x%2 == 0):
        print(x," is even")
    else:
        print(x," is odd")

print("\n--Finding if a,b are even or odd--")

if (a%2 == 0):
    print("a is even")
else:
    print("a is odd")
    
if (b%2 == 0):
    print("b is even")
else:
    print("b is odd")


Num = -6
if (Num<0):
    print(Num*-1)
else:
    print(Num)

print(abs(Num))
print(help(abs))

print(round(10.555,2))
print(round(10.555,1))
print(round(10.710000,8))

print(min(1,5,3,8,0,-7))
print(max(1,5,3,8,0,-7))

# Using Python Libraries:

import math
print(math.sqrt(25))

print(help(math))

print(math.ulp(6.9))






