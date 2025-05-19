"""
Name = input("enter your name: ")
if ("H" in Name):
    print("your name include H")


filename =  "CodeAcademy Oman"
if (filename.endswith(".py")):
    print("This is a Python file")
else:
    print("Another file type")
    
print(filename.count('e'))
print(filename.find('A'))

print("A123".isalnum()) #Consists Numbers

print("Abcd12".isalpha()) #Consists of only alp

print(filename.islower())  #All lowercase

print("       ".isspace()) #Only whitespace

print("HELLO".isupper()) #All uppercase

floornum = int(input("Enter floor number: "))
if (floornum <=0 or floornum>20):
    exit("Error: floor number must be between 1-20")
elif (floornum == 13):
    exit("floor 13 not available")
else:
    if(floornum < 13):
        print("floor number:",floornum)
    else:
        floornum -= 1
        print("floor number:",floornum)


if():
    print("username cannot be empty")
elif():
    print("username cannot contain spaces")
elif():
    print("password must have at least 8 char")
elif():
    print("password must contain at least 1 digit")
elif():
    print("password must contain at least 1 upper and lower char")
else:
    print("valid username/password")


username = input("Enter username: ")
password = input("Enter Password: ")


if(username == "" or username.isspace()):
    print("Invlid Username")
elif(len(password) < 8 or not(password.isalnum()) or (password.isupper() or password.islower())):
    exit("Invalid password")
else:
    print("valid username/password")
     
"""




balance = 10000
target = 25000
interestRatePerMonth = 0.1/12
m = 0
y = 0

while(balance <= target):
    balance = balance + (balance * interestRatePerMonth)
    m += 1
    if(m == 12):
        y += 1
        m=0
    
print(f"You need {y}.{m} years to reach",target)














