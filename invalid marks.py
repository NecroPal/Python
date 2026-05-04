lst = eval(input("Enter a number: "))
ele = int(input("Enter a number: "))

for i in range(len(lst)-1,0,-1):
    if lst[i] == ele:
        lst.pop(i)

print(lst)