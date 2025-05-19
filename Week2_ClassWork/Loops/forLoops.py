"""
total = 0.0
count = 0
inputStr = input("Enter Value: ")
while inputStr != "":
    value = float(inputStr)
    total += value
    count += 1
    inputStr = input("Enter Value: ")

if count > 0:
    average = total / count
else:
    average = 0.0

print("\nYou Entered",count,"Values")
print("Average: ",average)

#Evens
even = 0
count=0
inputStr = input("Enter Value: ")
while inputStr != "":
    value = int(inputStr)
    count += 1
    if(value%2 == 0):
        even+=1
    inputStr = input("Enter Value: ")

print("\nYou have entered",count," values")
print("There are",even," Even numbers")

#Range (0-100)
valid = False
while not valid:
    value = int(input("Please Enter a positiove num <100: "))
    if value>0 and value<100:
        valid = True
        print(value,"is valid")
    else:
        print("Invalid input")

#Maximum
strInput = input("Enter value: ")
maxvalue=0
while strInput!="":
    value = int(strInput)
    if(value>maxvalue):
        maxvalue=value
    strInput = input("Enter value: ")

print("Maximum value is: ",maxvalue)
  

#Minimum
strInput = input("Enter value: ")
minVal=0
while strInput!="":
    value = int(strInput)
    if(value<minVal):
        minVal=value
    strInput = input("Enter value: ")

print("Minimum value is: ",minVal)

# adjecence
OldVal=int(input("Enter value: "))
strInput = input("Enter value: ")
while strInput!="":
    value = int(strInput)
    if(value!=OldVal):
        OldVal=value
    else:
        print("Duplicate Value!")
    strInput = input("Enter value: ")
"""
#HERE WHILE LOOPS





















