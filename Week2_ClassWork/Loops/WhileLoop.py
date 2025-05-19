"""
c = 1
tot = 0
while c <= 10:
    tot += c
    c += 1
print(tot)


n = "1729"
tot = 0
for i in n:
    tot += int(i)
print(tot)

n = "845"

i=0
tot=0
while i < len(n):
    tot += int(n[i])
    i+=1
print(tot)



c = 0
tot= 0
sal = 0.0
Notdone = True #flag to break the loop
while Notdone:
    sal = float(input("Enter salary or -1 to stop: "))
    if sal<0.0:
        Notdone = False
    else:
        tot += sal
        c += 1
print("")
print(c,"salaries Entered")
print("Total Salary: ",tot)



"""

bal = 0
done = False
tot=0
while not done:
    if tot >= 1000:
        done = True
    else:
        bal = float(input("Enter deposite amount: "))
        tot += bal
        print("Current balace: ",tot)
                
print("\nGoal reached! your balance:",tot)


