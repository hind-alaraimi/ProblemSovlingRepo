numFile = open("Numbers.txt",'r')
number = numFile.readline()
T = 0
c = 1
Lst = []
while number != "":
    T += float(number)
    c+=1
    Lst.append(number)
    number = numFile.readline()
numFile.close()

AnsFile = open("TotalAvg.txt",'w')
for i in Lst:
    AnsFile.write(i)
AnsFile.write("\n---------")
AnsFile.write(f"\nTotal:{T}")
Av = T/c
AnsFile.write(f"\nAverage:{c}")
AnsFile.close()