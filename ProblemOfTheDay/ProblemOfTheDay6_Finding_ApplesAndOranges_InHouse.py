s = int(input("Enter the start point of the house: "))
t = int(input("Enter the end point of the house: "))
a = int(input("Enter the location of Apple tree: "))
b = int(input("Enter the location of Orange tree: "))

num_apples = int(input("Enter number of apples fell from the tree: "))
m = []
applesLoc = []
for i in range(num_apples):
    apple_dis = int(input(f"Enter the distance of apple({i+1}) from tree: "))
    m.append(apple_dis)

num_oranges = int(input("Enter number of oranges fell from the tree: "))
n = []
orangeLoc = []
for i in range(num_oranges):
    orange_dis = int(input(f"Enter the distance of Orange({i+1}) from tree: "))
    n.append(orange_dis)
    
m_loc = []
v = 0 
for i in m:
    v = i + a
    m_loc.append(v)
    
n_loc = []
v = 0 
for i in n:
    v = i + b
    n_loc.append(v)
print(m_loc,n_loc)

cApple = 0
cOrange = 0

for i in range(s,t+1):
    if(i in m_loc):
        cApple+=1
    if(i in n_loc):
        cOrange+=1
        
print(cApple,"Apples")
print(cOrange,"Oranges")
        
