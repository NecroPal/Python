lst = [10,20,30]
l = list(lst) #creates a copy of the list in the constant pool
l[0] = 15 #this will change values of both lst and l(without list()) because of constant pool (both refer to same list)
print(l)
print(lst)