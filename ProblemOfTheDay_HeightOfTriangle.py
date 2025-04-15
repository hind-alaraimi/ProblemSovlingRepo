o = int(input("Enter number of white balls: "))
x = int(input("Enter number of black balls: "))
r=1
space=50
H=0

for i in range(space):
    full_row=1
    for j in range(1,i + 2):
        if(r%2==1) and (o>0) and (o>=r):
            print("o",end=" ")
            o-=1
        elif(r%2==0) and (x>0) and(x>=r):
            print("x",end=" ")
            x-=1
        else:
            full_row=0
            break
    if(full_row!=0):
        print("")
        H+=1
        r+=1
    
print(f"\nHeight of triangle: {H}")