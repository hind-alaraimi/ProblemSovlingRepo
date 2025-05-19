# Search about differentce between methods and functions In Linked In
# Binary Search (Implement it and upload it in repo)

Lst1 = []
# we will create a list that contains multiples of 3 (0-250)
for i in range(251):
    Lst1.append(i*3)


#print(Lst1)
x = int(input("Enter number to be searched: "))
L = Lst1[0]
H = len(Lst1)-1

for i in Lst1:
    mid = (L+H)//2
    if((x in Lst1) and (L <= H)):
        if (x == Lst1[mid]):
            print(x," is at position: ",mid)
            break
        elif(x < Lst1[mid]):
            H = mid - 1
        else:
            L = mid + 1
    else:
        print(x,"is not found")
        break

