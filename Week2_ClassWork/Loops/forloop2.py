"""
# loop through string:
stateName = "Virginia"
for letters in stateName:
    print(letters)
   
#count control loop:
for i in range(0,101,20):
    print(i)
"""
balance = float(input("Enter your current salary: "))
interestRate = 0.05
years = 5
for y in range(1, years+1):
    balance = balance + (balance * interestRate)
    print(f"Year({y}) Balance: {balance}")
    print()

print("Answer is:",end="")
print(4+4)
    
"""   
for i in range(5,0,-1):
    print(i)"""