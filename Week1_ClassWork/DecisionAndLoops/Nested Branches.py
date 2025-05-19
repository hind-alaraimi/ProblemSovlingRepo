"""
num = int(input("Enter Number: "))
if num > 0:
    if num%3 == 0:
        print(num,"is divisable by 3.")
    else:
        print(num,"is not divisable by 3.")
else:
    print("Number is negative or zero")
"""
#-------------
hour1 = int(input("Enter hour1: "))
min1 = int(input("Enter minute1: "))
hour2 = int(input("Enter hour2: "))
min2 = int(input("Enter minute2: "))

if(hour1<hour2):
    print(hour1,":",min1,"comes first")
else:
    if(hour1 == hour2):
        if(min1<min2):
            print(hour1,":",min1,"comes first")
        else:
            print(hour2,":",min2,"comes first")
    else:
        print(hour2,":",min2,"comes first")
        

