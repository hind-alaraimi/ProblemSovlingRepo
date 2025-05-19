"""
List=[1,2,3,4,5,10]

NoOfItems = int(input("Enter number of values to add: "))
for i in range(NoOfItems):
    item = int(input("Enter Item: "))
    List.insert(i,item)

print(List)
          
               

#HW: Different between this two typt of function:
#max(listname)
#listname.Insert()

n=5
nlst = []
for i in range(n):
    nlst.append(i*100-(i*5))
    

print(nlst)

#print(nlst.remove())
print(nlst)

lst2 = ['A','B','C']
print(nlst+lst2)

print("\n",nlst*3)
print("-----------")

print(sum(nlst))

print(max(nlst))

print(min(nlst))

lst5 = [1,7,2,8,78,31,3]
print(lst5)
lst5.sort()
print(lst5)



ls1 = [1,2,3,4,5,6]
ls2 = ls1
print(ls1)
print(ls2)

ls1.append(10)
print(ls1)
print(ls2)

ls2 = list(ls1)
ls1.pop(2)
print(ls1)
print(ls2)


Temprature = [18,21,24,33,39,40,39,36,30,22,18,23]
for i in range(4):
    print(f"Quarter{i+1}: {Temprature[i:i+3]}")
            


friends=["Ahemd","Ali","Abdullah","Mohammed"]
print(friends)
friends[:2]=["Hala","Fatma","Amal"]
print(friends)


n = int(input("Enter length of list: "))
values = []
tot=0
for i in range(1,n):
    values.append(2**i)
    tot+=(2**i)
print(values)
print(tot)
"""
#--------------

#Linear Search/Sequencial
Lst1 = [1,2,3,4,5,12,20]
value = 3
for i in range(len(Lst1)):
    if Lst1[i] == value:
        print(i) 
        
print(Lst1)




