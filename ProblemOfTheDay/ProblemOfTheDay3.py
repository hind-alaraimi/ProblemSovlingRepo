h = int(input("Enter height of the triangle: "))
lst = []
sp=h
for i in range(h):
    lst.append(2**i)
    print(" "*(sp*2),end="")
    for j in lst:
        print(j, end=" ")
    for m in lst[-2::-1]:
        print(m, end=" ")
    print("")
    sp-=1
    
