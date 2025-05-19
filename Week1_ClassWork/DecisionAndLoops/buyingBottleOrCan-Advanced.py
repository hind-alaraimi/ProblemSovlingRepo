numberOfCans = int(input("Enter Number of Cans: "))
numberOfBottles = int(input("Enter Number of Bottles: "))
literPerCan = float(input("Enter Liters per Can: "))
literPerBottle = float(input("Enter Liters per Bottle: "))

Can_TotalLiters = numberOfCans*literPerCan
Bottle_TotalLiters = numberOfBottles*literPerBottle

if(Can_TotalLiters > Bottle_TotalLiters):
    print("Select Can")
else:
    print("Select Bottle")
