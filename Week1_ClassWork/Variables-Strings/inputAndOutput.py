"""Message="Enter your age: "
age = int(input(Message))
print("My name is",age)

print(float(input("Enter your Height: ")),"cm")
"""
# Formatting
price = 21.21997
#print(round(price,2)) #This will change the value
# - instead we will use formatting
print("price per liter %.4d"%(price))
print(round(price,3))
print(price)

msg = "Data science"
print("This is python for %25s"%(msg))


quan = 8
total = 15
print("Quantity: %d  -   Total: %2.2f"%(quan,total))
print("%-40s"%("Hello this is class 4 "),"of Makeen")

print("%10.2f"%(price))
print("%-10s%10.2f" %("Total: ",price)) 


print("%d %.2f"%(price,price))