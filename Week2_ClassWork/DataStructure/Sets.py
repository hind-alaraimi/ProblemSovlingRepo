"""
Lst = ['A','B','C']
print(type(Lst))
st = set(Lst)
print(type(st))


st = {1,2,3,'A','B'}
print(st)

#st.update(1,10)
print(st)

for i in range(len(st)):
    st.update([i*2])
print(st)
"""
#---------------
st1 = {1,2,3,'A','B'}
st2 = {'A','B','C','D','E'}


#Union:
print("Union:", st1 | st2)

#Intersection:
print("Intersection:", st1 & st2)

#Difference:
print("Difference:", st2 - st1)

#Symmetric Difference:
print("Symmetric difference:", st1 ^ st2)


newlst = (st1 | st2) - (st1 & st2)
print(newlst)