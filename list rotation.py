lst = eval(input("Enter a list: "))
k = int(input("Enter k number of rotations: "))
m = int(input("Enter m number of constant elements: "))

# lst = lst[k:] + lst[:k] #clockwise

for i in range(k):
    for j in range(m):
        item = lst.pop()
        lst.insert(m, item)

print(lst)