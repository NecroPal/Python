# lst = list(input("Enter a list: ")) #converts input into chr type

# lst = eval(input("Enter a list: "))

lst = [20,10]
lst.append(30) #adds at end
lst.insert(2,25) #adds at spec index
# lst.append([40,50,60])
lst.extend([40,50,60]) #extends the collections in list

# lst.pop(2) #deletes the specified index
# del lst[0:2] #deletes a slice of index
# lst.remove(40) #deletes the data provided
# lst.clear() #clears the list without removing its existence

lst.sort(reverse=True) #sort is a method for list which is used with object calling

lst2 = [5,2,1,7,9,8]
lst3 = sorted(lst2) #this is a function which creates a new sorted list
# lst3 = sorted(lst2, reverse=True)
# print(lst2)
# print(lst3)

lst4 = [1,2,3]
print(lst4*2) #replicates the list within itself