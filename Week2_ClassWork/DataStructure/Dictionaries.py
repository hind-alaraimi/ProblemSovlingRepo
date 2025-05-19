"""
favColor={"Ali":"Black","Ahmed":"Blue"}

print(favColor["Ali"])
"""
Dict1 = {"Student":["Ahmed","Ali","Hala"]}
#print(Dict1["Student"])

#for elements in Dict1["Student"]:
#    print(elements)

#if "Ali" in Dict1["Student"]:
#    print("Yes")

num = Dict1.get("Age")
#print(num)

#print(Dict1)
Dict1["Student"] = "Fatima"
#print(Dict1)

Dict1.update({"Age":16})
#print(Dict1)

#Printing keys:
for k in Dict1:
    print(k)
    
#printing values
for v in Dict1.values():
    print(v)
    
#printing pair of key and value:
for k,v in Dict1.items():
    print(k,"is:",v)
    


    
    
    
    